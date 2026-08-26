# 🌿 Nusantara-KG-MCP-Server

> **印尼高端室内设计知识图谱 · 通过 MCP 协议赋能一切 AI 助手**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-8A2BE2)](https://modelcontextprotocol.io)
[![Built with Obsidian](https://img.shields.io/badge/Built%20with-Obsidian-7C3AED)](https://obsidian.md)
[![Deployed on Cloudflare](https://img.shields.io/badge/Deployed%20on-Cloudflare-F38020)](https://cloudflare.com)

---

## 🎯 这是什么？

**Nusantara-KG-MCP-Server** 是一个将 **印尼高端室内设计的全链路知识** —— 从设计美学、材料特性、施工工艺，到人工配置与工期管控 —— 结构化为知识图谱，并通过 **MCP (Model Context Protocol)** 协议对外提供服务的智能引擎。

**它不是普通的装修知识库，而是一个「高端交付」的决策大脑。**

### 我们解决什么核心问题？

在印尼高端装修市场，最贵的不是材料，而是：

- ❌ **设计效果与落地严重不符** —— 效果图很美，完工后完全不是那回事
- ❌ **工艺标准缺失** —— 大板岩板铺贴空鼓、收口粗糙、阴阳角不直
- ❌ **人工错配** —— 用普通印尼技工做中国师傅才能驾驭的工艺
- ❌ **工期失控** —— 不知道每道工序该花多少天，项目无限延期
- ❌ **报价不透明** —— 增项不断，客户与设计师之间信任崩塌

**这个知识图谱，就是把「高端交付」的 know-how 结构化，让 AI 能够推理、比较、决策。**

### 知识覆盖范围

| 维度 | 内容 | 说明 |
| :--- | :--- | :--- |
| 🎨 **设计美学** | 8种风格 × 12类空间 × 25+真实案例 | 法式、现代、侘寂、意式极简…… |
| 🧱 **材料科学** | 特性、价格、效果、维护、适用场景 | 大理石/岩板/微水泥/艺术漆…… |
| 🔧 **施工工艺** | 工序流程、验收标准、难度等级 | 从基层处理到面层收口的全链路 |
| 👷 **人工配置** | 印尼普工/印尼技工/中国技工的工时与成本对比 | **高端落地质量的核心变量** |
| 📐 **工时定额** | 每道工序每平方米的标准工时 | 精确排期、控制工期 |
| 🖼️ **实景对照** | 231+张实景照片与工艺节点对应 | 效果图 vs 实景的「所见即所得」 |

---

## 🧠 核心能力

| 能力 | 说明 | 高端价值 |
| :--- | :--- | :--- |
| **精准估价** | 基于真实案例 + 工艺工时 + 人工等级 | 误差控制在5%以内，杜绝增项扯皮 |
| **人工配置建议** | 根据工艺难度推荐合适的工人等级 | 避免「印尼普工做中国工艺」的翻车事故 |
| **工期推演** | 按工序拆解，精确到天的施工排期 | 让业主对交付时间有确定性的信心 |
| **材料-工艺匹配** | 某材料必须配某工艺才能出效果 | 防止「用错工艺毁了好材料」 |
| **效果还原度评估** | 根据工艺选择，预判落地效果偏差 | 设计效果 ≠ 落地效果，我们量化这个差距 |
| **替代方案推理** | 预算调整时，推荐工艺/材料的平替路径 | 灵活应对预算变动，不牺牲核心品质 |
| **看图出方案** ⭐ | 上传参考图，自动识别元素并生成工艺+报价+工期 | 从「我说你听」到「你看图，我出方案」 |

---

## 📸 看图出方案 · 核心杀手锏

这是本项目最具商业价值的功能。

用户上传一张参考图（小红书/Instagram/Pinterest），系统自动：
上传图片 → 多模态识别 → 知识图谱匹配 → 推理计算 → 输出三件套
│ │ │ │ │
▼ ▼ ▼ ▼ ▼
参考图 识别出: 匹配工艺节点: 计算: 📋 工艺做法清单
(极简风) 悬浮吊顶 工艺_悬浮吊顶 材料费 💰 精确BOM报价
无主灯 工艺_无主灯预埋 人工费 ⏱️ 施工工期表
微水泥墙面 工艺_微水泥批刮 工时
大板通铺 工艺_大板铺贴 工期排期

text

**输出示例：**

| 识别元素 | 推荐工艺 | 推荐人工 | 工时 | 预估费用 |
| :--- | :--- | :--- | :--- | :--- |
| 悬浮吊顶 | 轻钢龙骨+L型整板 | 中国技工 | 2.5天 | Rp 18,500,000 |
| 无主灯 | 预埋型材+批灰找平 | 中国技工 | 1天 | Rp 6,200,000 |
| 微水泥墙面 | 四遍批刮+打磨 | 中国技工 | 4天 | Rp 42,000,000 |
| 大板通铺 | 薄贴法+调平器 | 中国技工 | 3天 | Rp 19,800,000 |
| **合计** | — | — | **10.5天** | **Rp 86,500,000** |

---

## 🔌 什么是 MCP？

[MCP (Model Context Protocol)](https://modelcontextprotocol.io) 是 Anthropic 发起的开放协议，它让 AI 应用能够以标准化的方式连接外部工具和数据源。

通过 MCP，这个知识图谱可以 **即插即用地接入任何支持 MCP 的 AI 生态**：

- 🤖 Claude Desktop / 任何 LLM 应用
- 💻 Cursor / VS Code 智能编程助手
- 🌐 你的 Next.js 应用 (`Nusantara-Atelier`)
- 📱 未来的 Indoscout 获客系统

---

## 🏗️ 知识模型 (Ontology)

这个知识图谱的核心实体及其关系如下：
┌─────────────────────────────────────────────────────────────────┐
│ 知识图谱实体模型 │
├─────────────────────────────────────────────────────────────────┤
│ │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐ │
│ │ 案例 │────▶│ 风格 │ │ 空间 │ │
│ │ (Case) │ │ (Style) │ │ (Space) │ │
│ └────┬─────┘ └──────────┘ └────┬─────┘ │
│ │ │ │
│ │ 包含 │ 包含 │
│ ▼ ▼ │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐ │
│ │ 材料 │◀────│ 工艺 │────▶│ 人工 │ │
│ │(Material)│ │(Process) │ │ (Labor) │ │
│ └────┬─────┘ └────┬─────┘ └──────────┘ │
│ │ │ │
│ │ 影响 │ 拆解为 │
│ ▼ ▼ │
│ ┌──────────┐ ┌──────────┐ │
│ │ 效果 │ │ 工时 │ │
│ │ (Effect)│ │(WorkHour)│ │
│ └──────────┘ └──────────┘ │
│ │
└─────────────────────────────────────────────────────────────────┘

text

### 实体详解

| 实体类型 | 说明 | 示例 |
| :--- | :--- | :--- |
| **案例 (Case)** | 真实落地项目，含实景图、造价、空间配置 | 雅加达南区法式公寓 |
| **风格 (Style)** | 设计风格定义与视觉特征 | 法式轻奢、意式极简、侘寂风 |
| **空间 (Space)** | 功能空间分类与设计要点 | 客厅、卧室、厨房、卫浴 |
| **材料 (Material)** | 规格、价格、特性、维护、品牌 | 大理石瓷砖、微水泥、艺术漆 |
| **工艺 (Process)** | 施工工序、难度、验收标准 | 湿铺法贴砖、冲筋找平、弧形吊顶 |
| **人工 (Labor)** | 工种等级、日薪、擅长领域 | 印尼普工/印尼技工/中国技工 |
| **工时 (WorkHour)** | 单位面积/工序的标准耗时 | 2.5 工时/m² |
| **效果 (Effect)** | 材料×工艺组合的最终呈现 | 高光/哑光/纹理/质感 |

---

## 🛠️ 技术栈

| 层级 | 技术 |
| :--- | :--- |
| **数据策展** | Obsidian (Markdown + 双向链接 + 图片引用) |
| **解析引擎** | Node.js / TypeScript |
| **服务部署** | Cloudflare Workers + D1 + R2 |
| **协议标准** | MCP (Model Context Protocol) |
| **传输方式** | SSE (Server-Sent Events) |
| **多模态识别** | GPT-4o / Claude Vision (通过 API 调用) |
| **依赖管理** | npm / yarn |

---

## 📂 数据目录结构
obsidian-vault/
├── 01_Cases/ # 真实落地案例 (25+)
│ └── 案例_雅加达南区_法式公寓.md
│
├── 02_Styles/ # 设计风格 (8种)
│ ├── 法式轻奢.md
│ ├── 意式极简.md
│ └── 侘寂风.md
│
├── 03_Spaces/ # 空间类型 (12类)
│ ├── 客厅.md
│ ├── 卧室.md
│ └── 厨房.md
│
├── 04_Materials/ # 材料库 (持续扩充)
│ ├── 大理石瓷砖.md
│ ├── 微水泥.md
│ └── 艺术漆.md
│
├── 05_Processes/ # 施工工艺 ⭐ 高端核心
│ ├── 工艺_湿铺法贴砖.md
│ ├── 工艺_冲筋找平.md
│ └── 工艺_弧形吊顶.md
│
├── 06_Labor/ # 人工配置 ⭐ 印尼特色
│ ├── 印尼本地普工.md
│ ├── 印尼本地技工.md
│ └── 中国技工.md
│
├── 07_WorkHours/ # 工时定额 ⭐ 工期管控
│ └── 工时_贴砖_湿铺法.md
│
└── 08_Effects/ # 效果矩阵
└── 效果_抛光砖_湿铺法.md

text

---

## 📝 数据策展规范 (Obsidian)

### 案例文件示例

`01_Cases/案例_雅加达南区_法式公寓.md`

```markdown
---
id: case_jakarta_selatan_01
name:
  en: "South Jakarta French Apartment"
  zh: "雅加达南区法式公寓"
  id: "Apartemen Prancis Jakarta Selatan"

style: [[法式轻奢]]
location: "雅加达南区"
total_area: 120
budget: 350,000,000
spaces: [[客厅]] [[卧室]] [[厨房]] [[卫浴]]

tags: ["三居室", "公寓", "高层", "精装交付"]

images:
  - "case_jkt_01_overview.jpg"
  - "case_jkt_01_living.jpg"
---

## 项目概述
120平米高层公寓，位于雅加达南区核心地段。业主为年轻华人家庭，偏好法式轻奢的浪漫与精致。

## 设计亮点
- 客餐一体化布局，以弧形线条弱化横梁
- 主卧套房设计，步入式衣帽间
- 厨房采用半开放式，岛台+社交餐区

## 材料配置
- 地面: [[大理石瓷砖]] (品牌: XXX, 规格: 120x60cm, 柔光面)
- 墙面: [[艺术漆]] (品牌: YYY, 颜色: 奶油白)
- 木作: [[胡桃木贴皮]] (定制柜体)

## 关键工艺
- [[工艺_冲筋找平]] → 保证墙面垂平，艺术漆施工基础
- [[工艺_湿铺法贴砖]] → 大板砖铺贴，中国技工施工
- [[工艺_弧形吊顶]] → 木工板基础 + 石膏板饰面

## 实景照片
![[case_jkt_01_living.jpg]]
![[case_jkt_01_kitchen.jpg]]
工艺文件示例 ⭐ 核心亮点
05_Processes/工艺_湿铺法贴砖.md

markdown
---
id: process_tiling_wet
name:
  en: "Wet Method Tiling"
  zh: "湿铺法地砖铺贴"
  id: "Pemasangan Ubin Metode Basah"

process_type: "铺贴"
difficulty_level: 4                    # 1-5，5为最难
space_applicable: [[客厅]] [[厨房]] [[卫浴]]
material_applicable: [[大理石瓷砖]] [[仿古砖]] [[岩板]]

images:
  - "process_tiling_01.jpg"
  - "process_tiling_02_step.jpg"
  - "process_tiling_03_finish.jpg"
---

## 工艺参数
thickness: 30-50mm
flatness_tolerance: 3mm/2m
hollow_ratio_standard: "< 3%"          # 高端标准严于国标

## 工序流程

### Step 1: 基层处理
**描述**：清理浮灰、油污，洒水湿润基层
**工具**：扫把、拖把、水管
**验收**：基层无明水、无浮灰

### Step 2: 1:3水泥砂浆找平
**描述**：水泥砂浆按1:3配比搅拌，铺设厚度30-50mm
**工具**：铁锹、抹子、2m靠尺
**验收**：平整度误差 < 3mm/2m

### Step 3: 瓷砖背面刮浆
**描述**：瓷砖背面涂抹纯水泥膏，使用齿形刮板拉槽
**工具**：齿形刮板 (10mm齿距)、抹子
**注意**：刮浆必须饱满，边角不得遗漏

### Step 4: 铺贴与振实
**描述**：将瓷砖铺设在砂浆层上，用橡皮锤振实
**工具**：橡皮锤、水平尺、激光水平仪
**验收**：四角平整，相邻砖高差 < 0.5mm

### Step 5: 调平器固定
**描述**：使用调平器系统固定缝隙，防止移位
**工具**：调平器、调平钳
**关键**：调平器是防止空鼓的关键工艺

### Step 6: 勾缝/美缝
**描述**：24-48小时后，清理缝隙，填充美缝剂
**工具**：美缝枪、压缝球、铲刀

## 验收标准 (QC)
- ✅ 空鼓率: 单块砖边角空鼓 < 3%，主要通道严禁空鼓
- ✅ 平整度: 2m靠尺检查，缝隙 < 1mm
- ✅ 坡度: 卫生间地漏处做坡度，倒水测试流畅无积水
- ✅ 缝宽: 1.5mm-2.5mm 均匀一致
- ✅ 颜色: 美缝颜色与砖色一致或协调

## 常见问题与避坑
| 问题 | 原因 | 解决方案 |
| :--- | :--- | :--- |
| 空鼓 | 基层未湿润/砂浆不饱满 | 铺贴前洒水湿润，刮浆饱满 |
| 不平整 | 未使用调平器 | 强制使用调平器系统 |
| 接缝高低差 | 砖变形/铺贴不实 | 选砖时挑平整度好的，铺贴时用橡皮锤振实 |
| 泛碱 (白华) | 水泥碱分渗出 | 使用防碱背涂剂，或选用瓷砖胶薄贴法 |

## 关联知识
- 推荐人工: [[中国技工]] (大板砖/岩板必须中国技工)
- 替代方案: [[工艺_薄贴法贴砖]] (适用于小规格砖)
- 相关材料: [[大理石瓷砖]], [[岩板]]
人工文件示例 ⭐ 印尼特色
06_Labor/中国技工.md

markdown
---
id: labor_chinese_master
name:
  en: "Chinese Master Craftsman"
  zh: "中国技工"
  id: "Tukang Ahli Tiongkok"

level: "高级"                      # 高级/中级/普通
skills: ["大板铺贴", "岩板无缝拼接", "精细收口", "极简工艺"]

images:
  - "labor_chinese_01.jpg"
---

## 适合工艺
- [[工艺_湿铺法贴砖]] (针对1.2m以上大板/岩板)
- [[工艺_冲筋找平]] (要求垂平度极高的场景)
- [[工艺_弧形吊顶]] (复杂造型)
- [[工艺_微水泥施工]]

## 工时与成本参考
daily_rate: 450,000 - 650,000 IDR
efficiency_per_10sqm: 1.5 工日
notes: "慢工出细活，日薪虽贵，但返工率极低，总体成本最优"

## 与本地技工对比
| 对比维度 | 中国技工 | 印尼本地技工 |
| :--- | :--- | :--- |
| 日薪 | 450k-650k IDR | 200k-300k IDR |
| 大板铺贴 | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| 收口精细度 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| 沟通成本 | 需翻译/图纸沟通 | 本地语言无障碍 |
| 工期 | 稳定可控 | 斋月/节假日可能延误 |

## 适用场景
- ✅ 极简风格 (追求无缝、无踢脚线)
- ✅ 大规格材料 (1.2m x 2.4m 岩板背景墙)
- ✅ 复杂造型 (弧形、异形)
- ✅ 业主对落地效果有极高要求

## 不适用场景
- ❌ 普通规格砖 (800x800mm以下) → 用本地技工性价比更高
- ❌ 简单的刮白/找平 → 本地普工即可胜任
- ❌ 工期极紧的项目 → 中国技工通常排期较满
📦 MCP Tools 清单
Tool Name	功能描述	输入参数	输出
quick_estimate	快速估价 (主项目调用)	style, area, spaces, location	价格区间 + 相似案例
query_case_by_style	按风格/空间/地区查询匹配案例	style, space, location	案例列表 + 实景图 + 造价
analyze_design_photo ⭐	上传参考图，识别元素并生成工艺+报价+工期	image_url, area, location	工艺清单 + BOM报价 + 工期表
precise_estimate	精确报价 (设计师后台)	processes, area, labor_level	BOM明细 + 人工拆解
recommend_labor	根据工艺推荐人工配置	process_ids	人工等级 + 日薪 + 工时
calculate_timeline	按工序拆解工期	processes, area, labor_level	甘特图式排期
match_material_to_process	推荐材料×工艺的最佳组合	material_id 或 process_id	组合方案 + 效果预测
compare_labor	对比同一工艺下不同人工的效果与成本	process_id, labor_levels	成本/工期/质量对比表
resolve_issue	施工问题诊断与解决方案	process_id, issue_description	原因分析 + 解决步骤
match_designer	根据项目需求匹配设计师	style, area, special_requirements	设计师列表 + 匹配分数
🤝 与主项目的关系
项目	角色	地址
Nusantara-Atelier	面向客户的展示网站 / 获客入口	GitHub Link
Nusantara-KG-MCP-Server	智能推理引擎 / MCP 服务 (本仓库)	当前仓库
协作模式
text
┌─────────────────────────────────────────────────────────────────┐
│                    Nusantara-Atelier (前端展示)                 │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐         │
│  │ 首页估价 │  │ AI识图  │  │ 案例详情 │  │ 设计师选 │         │
│  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘         │
└───────┼────────────┼────────────┼────────────┼────────────────┘
        │            │            │            │
        │  通过 MCP 协议通信 (SSE/HTTP)          │
        │            │            │            │
        ▼            ▼            ▼            ▼
┌─────────────────────────────────────────────────────────────────┐
│              Nusantara-KG-MCP-Server (智能引擎)                 │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  MCP Tools:                                             │    │
│  │  • quick_estimate       主项目快速估价                 │    │
│  │  • analyze_design_photo 识图分析  ← 核心杀手锏        │    │
│  │  • match_designer       设计师匹配                     │    │
│  │  • precise_estimate     精确报价 (设计师后台)          │    │
│  │  • calculate_timeline   工期推演                       │    │
│  │  • resolve_issue        问题诊断                       │    │
│  └─────────────────────────────────────────────────────────┘    │
│                              │                                  │
│                              ▼                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  Cloudflare D1 + R2 (知识图谱数据 + 图片存储)          │    │
│  │  • nodes.json (实体)                                   │    │
│  │  • edges.json (关系)                                   │    │
│  │  • images/ (工艺图/案例图/材料图)                      │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
📊 当前知识图谱规模
实体类型	数量	状态
真实案例	25+	✅ 已录入
实景照片	231+	✅ 已上传 R2
设计风格	8	✅ 已定义
空间类型	12	✅ 已定义
材料节点	50+	🚧 扩充中
工艺节点	20+	🚧 核心工艺优先
人工节点	3-5	✅ 印尼/中国对比
工时定额	20+	🚧 逐步录入
效果矩阵	持续生成	🔮 自动推理中
🚀 快速开始
1️⃣ 克隆仓库
bash
git clone https://github.com/vfvincentwong2026/Nusantara-KG-MCP-Server.git
cd Nusantara-KG-MCP-Server
npm install
2️⃣ 准备 Obsidian Vault
将你的知识库 Vault 链接到 /obsidian-vault/ 目录

3️⃣ 编译知识图谱
bash
npm run build
# 读取 .md 文件 → 输出 /data/nodes.json + /data/edges.json
4️⃣ 本地运行 MCP Server
bash
npm run dev
# 启动 MCP 服务，默认端口 3000
5️⃣ 在 Claude Desktop 中使用
claude_desktop_config.json:

json
{
  "mcpServers": {
    "nusantara-kg": {
      "url": "http://localhost:3000/sse"
    }
  }
}
☁️ Cloudflare 部署
bash
npm run deploy
# 使用 Wrangler 部署到 Cloudflare Workers
环境变量配置
变量名	说明
R2_ACCESS_KEY	R2 图片存储访问密钥
R2_BUCKET_URL	图片 CDN 地址
KG_DATA_URL	nodes.json / edges.json 地址
VISION_API_KEY	多模态识别 API 密钥 (GPT-4o/Claude Vision)
🔄 本地更新知识库 (零成本方案)
本项目支持 本地维护 → 自动同步线上 的完整工作流，全部使用免费服务：

text
本地 Obsidian 编辑 → Obsidian Git 插件自动提交 → GitHub 私有仓库 → 
GitHub Actions 自动编译 → Cloudflare Workers 自动部署 → MCP Server 加载新数据
详细步骤：

本地：在 Obsidian 中修改/新增 Markdown 文件，安装 Obsidian Git 插件自动提交

云端：GitHub Actions 在 push 时自动执行 npm run build 编译 JSON

部署：编译后的 JSON 自动部署到 Cloudflare R2 或 D1

生效：MCP Server 热加载或自动重启，新数据立即生效

全部免费额度：

GitHub: 免费私有仓库 + Actions 每月 2000 分钟

Cloudflare Workers: 每日 10 万次请求

Cloudflare R2: 10GB 免费存储 + 每月 1000 万次读取

🗺️ 产品路线图
阶段	目标	状态
Phase 1	基础图谱构建: 25案例 + 8风格 + 12空间	✅ 数据准备中
Phase 2	核心工艺录入: 贴砖/吊顶/找平/油漆 (含工时+人工对比)	🚧 开发中
Phase 3	MCP Server: quick_estimate + query_case + recommend_labor	🚧 开发中
Phase 3.5	多模态识图: analyze_design_photo 上线 ⭐	📋 新增重点
Phase 4	材料-工艺效果矩阵 + 替代方案推理	📋 规划中
Phase 5	前端集成: Atelier 调用 MCP 实现精准估价 + AI识图	📋 规划中
Phase 6	对外开放 MCP 服务，支持第三方订阅	🔮 未来
🤝 贡献指南
欢迎 PR！特别欢迎以下贡献：

新增工艺节点：按标准MD格式提交施工工艺

新增工时数据：印尼本地实际施工经验数据

新增材料信息：印尼本地高端建材的规格/价格/供应商

人工经验数据：不同工艺下各类工人的实际表现

实景照片：各工艺节点/材料效果的高清实景图

数据质量要求
所有数据必须基于真实落地经验，不得虚构

工时要注明数据来源 (如: 来自XX项目实际记录)

图片需有清晰的水印或无版权争议

📄 许可证
MIT License — 可自由使用、修改、商业化。

📬 联系方式
作者: @vfvincentwong2026

主项目: Nusantara-Atelier

参考知识库: Nusantara Knowledge Galaxy

Built with ❤️ for the Indonesian premium interior design community.

让每一分钱都花在看得见的地方。
