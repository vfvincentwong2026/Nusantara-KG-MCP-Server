# P1 · quick_estimate 估价引擎设计（2026-08-27）

> 状态：设计稿，待 Owner 评审。落地形式：**Atelier 内部 TS 模块**（非 MCP，非独立 Worker）。
> 前置依赖：KG 数据 ⚠️ 数字校对完成（`status: verified`）。

---

## 0. 关键数据事实（先核查，再设计）

2026-08-27 对 Atelier `data/cases.json` 的实测：

| 字段 | 覆盖率 | 结论 |
|---|---|---|
| 案例总数 | 25 | — |
| `area` 有值 | 15 / 25 | 部分可用 |
| `hard_cost_per_sqm` 有值 | **3 / 25** | ❌ 不足以做价格基准 |
| `soft_cost_per_sqm` 有值 | 3 / 25 | ❌ 同上 |
| 案例地域 | 以中国城市为主 | ❌ 造价口径不是印尼 IDR |

**设计决策（重要）**：

- ❌ 放弃"按相似案例平米单价外推"的路线——数据撑不住，且是中国价格；
- ✅ 采用**自下而上（bottom-up）BOM 合成**：`风格 → 配置模板 → 工序展开 → KG 工时×人工费率 + Atelier SKU 材料价 → 汇总`。价格锚完全落在 KG（已含 IDR 人工费率）和 Atelier SKU（已锚定印尼公开零售价）上；
- 📌 25 个案例的角色重新定义为：**风格→空间/材料配置模板 + 效果参考**，不作为价格基准；
- 📌  Owner 可选动作：给有造价的 3 个案例补全数据、或提供 2-3 个真实印尼项目造价用于回测（见 §5）。

---

## 1. 输入 / 输出

**输入**（对齐 Atelier `/upload` 现有表单）：

```typescript
interface EstimateInput {
  style: string;        // 风格：法式 | 现代 | 侘寂 | 奶油风 | 意式极简 | 现代轻奢 ...
  area: number;         // 建筑面积 m²
  spaces: string[];     // ["living","kitchen","bedroom","bathroom",...]
  location: string;     // jakarta | bali | ...（影响区域系数，P1 先只支持 jakarta）
  tier?: "standard" | "premium" | "luxury";  // 默认 premium
}
```

**输出**：

```typescript
interface EstimateOutput {
  total_idr: { low: number; mid: number; high: number };  // 区间 = mid ±15%
  per_sqm_idr: { low: number; mid: number; high: number };
  breakdown: ProcessEstimate[];    // 逐工序明细（见 §3 Step5）
  timeline_days: { min: number; likely: number; max: number };
  crew_plan: CrewPlan[];           // 班组配置建议
  confidence: "low" | "medium";    // P1 阶段只有这两档
  data_gaps: string[];             // 如实列出估算中走了默认值的环节
}
```

---

## 2. 推理管线（6 步）

```text
输入 → ①输入规范化 → ②配置模板匹配 → ③工序展开 → ④人工选择 → ⑤单项计算 → ⑥汇总输出
```

### Step ① 输入规范化
- 风格字符串 → 风格 id（容错映射表：法式/法式轻奢/法式奶油 → `french`）；
- spaces 英文枚举 → KG 空间节点 id。

### Step ② 配置模板匹配（案例的角色）
- 按风格从 cases.json 取同风格案例的**空间配置与材料搭配**（annotations 的 room + 材料描述）；
- 命中 <2 个同风格案例 → 用 `STYLE_DEFAULT_CONFIG` 内置默认配置（见 §6 开放问题），并在 `data_gaps` 标注。

### Step ③ 工序展开
- 对每个空间 × 材料，经 KG `relations` 查 `requires_process` → 得到工序清单；
- 每个工序经 `mandatory_prerequisite_for` 补前置工序（如贴砖自动补防水/找平）；
- 每个工序关联面积规则：地面工序按 `area×系数`、墙面工序按 `周长估算×层高`（P1 用 `area` 的简化换算表，见伪代码）。

### Step ④ 人工选择规则（硬规则，来自 KG 共识）
```text
工艺 difficulty ≥ 4 或材料为岩板/大板(≥1.2m)  → china-skilled-labor（强制）
微水泥/无缝结晶/弧形造型                     → china-skilled-labor（强制）
常规规格铺贴/防水/安装类                     → indonesian-skilled-labor
普工                                        → 仅辅助，按技工工日 × 0.5 自动配比
```

### Step ⑤ 单项计算
```typescript
// 材料费
materialCost = sku.price_idr × qty × sku.waste_factor;   // waste_factor 已在 Atelier SKU 中（如 1.12）
// 人工费
laborCost = (workhour.value × qty / 8) × labor.daily_rate.mid;
// 普工辅助
auxCost = laborDays × 0.5 × generalLabor.daily_rate.mid;  // 仅大板/防水/贴砖类计入
// 单项工期
processDays = workhour.value × qty / 8;
```

### Step ⑥ 汇总与系数
- **总价**：Σ(材料费 + 人工费 + 辅助费) × 区域系数（jakarta=1.0，bali=1.1 ⚠️待定）；
- **区间**：low = mid × 0.85，high = mid × 1.15（P1 固定带宽，回测后校准）；
- **工期**：Σ 工序工期 × 并行系数 0.7（多工种交叉施工）× 斋月系数（斋月期间 1.3）；
- **data_gaps**：凡走了默认值/未 verified 的数据，逐项列出。

---

## 3. 核心伪代码

```typescript
function quickEstimate(input: EstimateInput): EstimateOutput {
  const style = normalizeStyle(input.style);
  const config = matchStyleConfig(style, input.spaces) ?? DEFAULT_CONFIG[style]; // Step②
  const gaps: string[] = config.isDefault ? [`${style} 风格案例不足，走默认配置`] : [];

  const processes = expandProcesses(config, kg);        // Step③ 含前置工序
  const items: ProcessEstimate[] = [];

  for (const p of processes) {
    const qty = areaFor(p, input.area);                 // 地面/墙面/吊顶换算
    const labor = selectLabor(p, kg);                   // Step④ 硬规则
    const wh = kg.workhour(p.id, labor.id);             // 工时定额
    if (wh.status !== "verified") gaps.push(`${p.id} 工时未校对`);

    items.push({
      process: p.id,
      qty,
      materialCost: materialCostOf(p, qty, skus),       // Step⑤
      laborCost: laborCostOf(wh, qty, labor),
      auxCost: needsAux(p) ? auxCostOf(wh, qty) : 0,
      days: wh.value * qty / 8,
      crew: labor.id,
    });
  }

  return assemble(items, input.location, gaps);         // Step⑥
}
```

---

## 4. 与现有系统的关系

- **不重复造轮子**：Atelier Phase 3b 已有 BOM 数量引擎 + `materials.json`（含 `waste_factor`、`labor_rate_idr`）。P1 模块**复用其材料价与损耗系数**，KG 只补充：工艺展开逻辑、人工选择规则、KG 工时定额；
- **合并策略**：同一工序的材料费以 Atelier SKU 为准，工时以 KG 为准——两个数据源的边界写死在模块注释里，防止日后双头维护；
- **部署形态**：`apps/web/lib/estimate/` 下的纯函数 TS 模块 + 单元测试，供 `/upload` 的"精报"标签调用；不新增 Worker。

---

## 5. 误差验证方案（三级）

| 级别 | 方法 | 目标 | 何时做 |
|---|---|---|---|
| **A. 逻辑自洽** | 用同一输入跑 P1 模块 vs Atelier `/upload` 现有估价，对比偏差 | 偏差 <25% 且可解释 | 模块完成后立即 |
| **B. 真实回测** | Owner 提供 2-3 个已交付印尼项目的真实造价，跑模块对比 | **MAPE ≤15%**（quick_estimate 验收线） | 数据 verified 后 |
| **C. 敏感性分析** | 对工时/日薪/材料价分别 ±20%，看总价波动 | 找出最敏感变量 → 反推 Owner 校对优先级 | B 之前，帮 Owner 排校对顺序 |

> README 中"误差 5% 以内"的目标属于 `precise_estimate`（设计师后台，逐项确认工程量后），
> quick_estimate 的诚实目标是 **15%**，文档与官网文案统一按此口径。

---

## 6. 开放问题（待 Owner 拍板）

1. `STYLE_DEFAULT_CONFIG`：8 种风格 × 标准空间组合的默认材料配置——需要 Owner 经验填一版（我可以先起草）；
2. bali 区域系数 1.1 是否准确？其他城市的系数表？
3. 普工辅助配比 0.5（辅助工日 = 技工工日 × 0.5）是否符合你的班组实际？
4. 回测用的 2-3 个真实印尼项目，能提供吗（只需总造价 + 面积 + 风格 + 主要工序）？
5. 工期并行系数 0.7 的口径：你的项目实际交叉施工能压到什么程度？

---

## 7. 里程碑

| 步骤 | 依赖 | 产出 |
|---|---|---|
| M1 设计评审（本文档） | Owner 拍板 §6 | 定稿 |
| M2 敏感性分析脚本 | 无（可用 draft 数据先跑） | 校对优先级报告 |
| M3 模块开发 | M1 + KG 数据 verified | `lib/estimate/` + 测试 |
| M4 A/B 验证 | M3 | 验收报告 |
