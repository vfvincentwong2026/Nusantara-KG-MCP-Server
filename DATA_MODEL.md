# 数据模型详解（v2 · 2026-08 修订）

> 本文档以 `obsidian-vault/05_Processes/` 下已录入的 23 个工艺节点为**事实标准**。
> 所有新数据必须遵循本 schema；`templates/` 下的生成提示词已同步到本版本。

---

## 📊 实体类型一览

| `type` | 目录 | 说明 | 当前数量 |
| :--- | :--- | :--- | :--- |
| `process` | `05_Processes/` | 施工工艺 ⭐ 高端核心 | 23 ✅ |
| `labor` | `06_Labor/` | 人工配置 ⭐ 印尼特色 | 0 📋 |
| `workhour` | `07_WorkHours/` | 工时定额 ⭐ 工期管控 | 0 📋 |
| `material` | `04_Materials/` | 建材 | 0 📋（Atelier 有 51 SKU，待映射） |
| `case` | `01_Cases/` | 真实落地项目 | 事实源在 Atelier（25 案例） |
| `style` | `02_Styles/` | 设计风格 | 0 📋 |
| `space` | `03_Spaces/` | 功能空间 | 0 📋 |
| `effect` | `08_Effects/` | 效果矩阵 | P1 后自动生成 |

---

## 📝 通用 Frontmatter 契约（所有实体）

```yaml
---
id: wet-method-tiling            # 唯一标识，kebab-case，全库唯一
type: process                    # 实体类型，见上表
category: 01_construction_process
name:
  en: Wet Method Tiling
  zh: 湿铺法地砖铺贴
summary:
  en: <一句话英文摘要，含关键参数与适用场景>
  zh: <一句话中文摘要>
tags: [construction, tiling, wet-method, indonesia]
domain: [Construction]
hierarchy: Processes/Flooring/Wet-Method   # 分类路径
pantheon: N/A
relations:                       # 结构化关系（图谱编译的边）
  - type: related_to
    target: thin-set-method      # 目标节点 id（裸 id，不加 [[]]）
  - type: recommended_for
    target: living-room
locations: [indonesia, java, bali]
cultural_elements: []
created_at: 2026-08-26
updated_at: 2026-08-26
status: published                # draft | published | verified
---
```

**字段纪律**：

- `relations[].target` 统一用**裸 id**（如 `thin-set-method`），不加 `[[]]`；正文内的双链才用 `[[id|显示名]]` 格式；
- `status` 三态：`draft`（AI 初稿）→ `published`（已入库）→ `verified`（Owner 校对过全部 ⚠️ 数字）；
- ⚠️ 标记：AI 生成的数字一律带 ⚠️，Owner 校对后删除 ⚠️ 并把 `status` 改为 `verified`；
- 悬空链接：允许指向尚不存在的节点 id（Obsidian 显示为待建节点），后续批次补齐。

## 🔗 关系类型词表（`relations[].type`）

| 关系类型 | 源 → 目标 | 说明 |
| :--- | :--- | :--- |
| `related_to` | 任意 → 任意 | 通用关联 |
| `recommended_for` | process → space | 推荐用于某空间 |
| `mandatory_prerequisite_for` | process → process | 前置工序（如防水 → 贴砖） |
| `requires_pretreatment` | process → process | 需要预处理 |
| `stricter_than` | process → process/standard | 标准严于某基准 |
| `mandatory_material` | process → material | 强制使用某材料 |
| `vulnerable_to` | process → issue/risk | 易受某风险影响 |
| `alternative_of` | process/material → 同类 | 平替方案 |
| `recommends_labor` | process → labor | 推荐人工等级 |
| `has_workhour` | process → workhour | 工时定额 |
| `uses_material` | case/process → material | 使用某材料 |
| `has_style` / `has_space` | case → style/space | 案例属性 |
| `produces_effect` | material×process → effect | 产生某效果 |
| `similar_to` | case → case | 案例相似 |

## 📄 正文结构契约（process 类型）

```markdown
# <英文名> (<中文名>)

## English (EN)
### Overview
### Process Parameters        ← 数字带 ⚠️
### Step-by-Step Workflow     ← 6-10 步，每步含 Tools / Acceptance
### Quality Control (QC) Standards   ← 表格
### Common Issues & Prevention        ← 表格，≥4 行印尼工地真实高发问题
### Related Knowledge (Labor & Materials)   ← [[id|显示名]] 双链

## 中文 (ZH)
### 概览 / 工艺参数 / 工序流程 / 验收标准 (QC) / 常见问题与避坑 / 关联知识
（与 EN 镜像对应）

## 知识关联 / Knowledge Relations
（按 工艺与工法 / 材料与应用 / 人力资源 / 地理与环境 分组的双链列表）

## 双链闭环结构 / Bi-Directional Link Closure
\`\`\`text
（核心节点的树状关系图，必须包在代码围栏内）
\`\`\`

## 索引与检索标签 / Indexing Tags
- `tag1` ...
```

> ⚠️ **从网页版 AI 复制时，严禁带入 `text` / `复制` / `下载` 等 UI 按钮文字**——2026-08 已清理过一批。

## 🧾 其他类型字段要点

### Labor（人工）
- frontmatter 增加：`level`（高级/中级/普通）、`skills: []`、`daily_rate: {min, max}`（IDR ⚠️）、`efficiency_per_10sqm` ⚠️
- 正文必须含：适合工艺、工时与成本参考、与其他等级对比表（含斋月/节假日因素）、适用与不适用场景

### WorkHour（工时）
- frontmatter 增加：`process: <工艺id>`、`labor_level`、`value` ⚠️、`unit`（工时/m² | 工时/项）
- 正文必须含：影响因素（斋月/雨季/难度折算）、数据来源说明

### Material（材料）
- frontmatter 增加：`category`、`specs`、`brand`、`price: {per_unit, per_m2}`（IDR ⚠️）
- 正文必须含：印尼气候表现、施工要求（关联工艺双链）、供应商参考

## 📊 查询示例（图谱编译后的逻辑视图）

```cypher
// 某工艺的前置工序与强制材料
MATCH (p:process {id: 'wet-method-tiling'})
OPTIONAL MATCH (pre:process)-[:mandatory_prerequisite_for]->(p)
OPTIONAL MATCH (p)-[:mandatory_material]->(m:material)
RETURN pre, m

// 某工艺的人工与工时
MATCH (p:process {id: 'wet-method-tiling'})-[:recommends_labor]->(l:labor)
MATCH (p)-[:has_workhour]->(w:workhour)
RETURN l.name, w.value, w.unit
```

## 💡 扩展方向

- `supplier` 供应商节点（与 material 建立 `supplies`）
- `tool` 工具节点（与 process 建立 `uses_tool`）
- `issue` 问题节点（把避坑表升级为可检索实体，`vulnerable_to` 已预留）
- `cost` 费用节点（材料费/人工费/管理费拆解）

---

| 文档 | 用途 |
| :--- | :--- |
| `README.md` | 项目概览 + 路线图 |
| `DATA_MODEL.md` | 本文件，数据契约 |
| `templates/00_使用指引.md` | AI 生成工作流 |
| `templates/01-04` | 各类型生成提示词（已同步本 schema） |
