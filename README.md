# Nusantara-KG-MCP-Server
印尼本土室内设计知识与真实落地案例 结构化为知识图谱，并通过 MCP (Model Context Protocol) 协议对外提供服务的智能引擎。
# 🌿 Nusantara-KG-MCP-Server

> **印尼室内设计知识图谱 · 通过 MCP 协议赋能一切 AI 助手**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-8A2BE2)](https://modelcontextprotocol.io)
[![Built with Obsidian](https://img.shields.io/badge/Built%20with-Obsidian-7C3AED)](https://obsidian.md)
[![Deployed on Cloudflare](https://img.shields.io/badge/Deployed%20on-Cloudflare-F38020)](https://cloudflare.com)

---

## 🎯 这是什么？

**Nusantara-KG-MCP-Server** 是一个将 **印尼本土室内设计知识与真实落地案例** 结构化为知识图谱，并通过 **MCP (Model Context Protocol)** 协议对外提供服务的智能引擎。

**简单说：它是印尼家装界的「AI 外挂大脑」。**

- 🏠 覆盖 **25+** 真实落地案例、**231** 张实景照片
- 🎨 涵盖 **8** 种主流风格（法式、现代、侘寂、意式极简……）
- 🛋️ 包含 **12** 类空间体系（客厅、卧室、厨房、卫生间……）
- 🧱 集成印尼本地建材供应链数据（价格持续更新中）

---

## 🧠 核心能力

| 能力 | 说明 |
| :--- | :--- |
| **智能估价** | 基于真实案例 + 空间维度，精准估算装修预算 |
| **材料推荐** | 根据风格和空间，推荐印尼本地可用材料及价格 |
| **案例匹配** | 按风格、预算、空间类型，匹配最相似的真实落地案例 |
| **BOM 生成** | 自动生成精确的物料清单（Bill of Materials）|
| **设计方案推理** | 根据户型特征和用户偏好，生成初步设计方案建议 |

---

## 🔌 什么是 MCP？

[MCP (Model Context Protocol)](https://modelcontextprotocol.io) 是 Anthropic 发起的开放协议，它让 AI 应用能够以标准化的方式连接外部工具和数据源。

通过 MCP，这个知识图谱可以 **即插即用地接入任何支持 MCP 的 AI 生态**：

- 🤖 Claude Desktop
- 💻 Cursor / VS Code 智能编程助手
- 🌐 你自己的 Next.js 应用 (`Nusantara-Atelier`)
- 🔌 任何支持 MCP 协议的 AI Agent

---

## 🏗️ 架构设计
┌─────────────────────────────────────────────────────────────┐
│ 数据策展层 (Obsidian) │
│ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ │
│ │案例A │ │案例B │ │客厅 │ │法式 │ │大理石│ ← 双向链接 │
│ └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘ │
└─────┼───────┼───────┼───────┼───────┼────────────────────┘
│ │ │ │ │
└───────┴───────┴───────┴───────┘
│ Git Push
▼
┌─────────────────────────────────────────────────────────────┐
│ 编译层 (GitHub Actions) │
│ Markdown → 结构化 JSON (Nodes + Edges) │
└─────────────────────────────────────────────────────────────┘
│ 部署
▼
┌─────────────────────────────────────────────────────────────┐
│ 服务层 (Cloudflare Workers) │
│ MCP Server (SSE) + D1 / R2 缓存 │
└─────────────────────────────────────────────────────────────┘
│ MCP 协议
┌───────────┼───────────┬───────────┐
▼ ▼ ▼ ▼
┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐
│Claude │ │Cursor │ │Atelier│ │其他AI │
└───────┘ └───────┘ └───────┘ └───────┘

text

---

## 🛠️ 技术栈

| 层级 | 技术 |
| :--- | :--- |
| **数据策展** | Obsidian (Markdown + 双向链接) |
| **解析引擎** | Node.js / TypeScript |
| **服务部署** | Cloudflare Workers + D1 + R2 |
| **协议标准** | MCP (Model Context Protocol) |
| **传输方式** | SSE (Server-Sent Events) |
| **依赖管理** | npm / yarn |

---

## 🚀 快速开始

### 1️⃣ 克隆仓库

```bash
git clone https://github.com/vfvincentwong2026/Nusantara-KG-MCP-Server.git
cd Nusantara-KG-MCP-Server
npm install
2️⃣ 准备知识图谱数据
将你的 Obsidian Vault 中编译好的知识图谱数据放入 /data 目录：

text
/data/
  ├── nodes.json      # 所有实体 (案例/风格/空间/材料)
  └── edges.json      # 所有关系 (包含/推荐/关联)
💡 开发阶段：你可以使用 npm run build 从 Obsidian 的 Markdown 文件编译生成这两个 JSON 文件（详见下方「数据策展指南」）。

3️⃣ 本地运行 MCP Server
bash
npm run dev
# 启动本地 MCP 服务，默认端口 3000
4️⃣ 在 Claude Desktop 中接入
编辑 claude_desktop_config.json：

json
{
  "mcpServers": {
    "nusantara-kg": {
      "url": "http://localhost:3000/sse"
    }
  }
}
重启 Claude Desktop，即可通过自然语言查询印尼家装知识！

5️⃣ 调用示例
在 Claude 中输入：

“雅加达南区 120平 三居室，想做轻法式风格，预算大概多少？推荐什么材料？”

知识图谱将返回：

json
{
  "matched_cases": [
    {
      "name": "雅加达南区_法式公寓",
      "budget": "250,000,000 IDR",
      "similarity_score": 0.92
    }
  ],
  "recommended_materials": [
    { "name": "大理石瓷砖", "brand": "XXX", "price_per_m2": 850000 },
    { "name": "艺术漆", "brand": "YYY", "price_per_m2": 350000 }
  ],
  "estimated_range": "220,000,000 - 280,000,000 IDR"
}
📦 MCP Tools 清单
Tool Name	功能描述	输入参数
query_case_by_style	按风格查询匹配的落地案例	style, city, budget_range
recommend_materials	按空间+风格推荐材料	space_type, style, preferred_brand
calculate_bom	生成精确物料清单	style, total_area, rooms
match_similar_project	匹配最相似的真实项目	style, space_count, location
get_design_suggestions	生成初步设计方案建议	style, space_type, special_requirements
🤝 与主项目的关系
项目	角色	地址
Nusantara-Atelier	面向客户的展示网站 / 获客入口	GitHub Link
Nusantara-KG-MCP-Server	智能推理引擎 / MCP 服务（本仓库）	当前仓库
两者通过 MCP 协议通信，实现 前端展示 与 智能推理 的完全解耦。

📊 当前知识图谱规模
实体类型	数量	说明
真实案例	25+	印尼本地落地项目，含实景图
实景照片	231+	高质量完工实景
设计风格	8	法式、现代、侘寂、意式极简……
空间类型	12	客厅、卧室、厨房、浴室……
材料节点	持续扩充	印尼本地建材 SKU
关系边	持续扩充	双向链接自动生成
🗺️ 产品路线图
阶段	目标	状态
Phase 1	基础图谱构建 (25案例结构化)	✅ 数据准备中
Phase 2	MCP Server 上线，提供 query_case 工具	🚧 开发中
Phase 3	集成 floorplan-ontology-skill，支持户型图解析	📋 规划中
Phase 4	接入印尼本地材料供应链实时价格	📋 规划中
Phase 5	对外开放 MCP 服务，支持第三方订阅	🔮 未来
📝 数据策展指南 (Obsidian)
本项目的数据源头在 Obsidian，建议的文件结构如下：

text
Nusantara-KG-Data/
├── 01_Cases/
│   └── 案例_雅加达南区_法式公寓.md
├── 02_Spaces/
│   ├── 客厅.md
│   └── 卧室.md
├── 03_Materials/
│   ├── 大理石瓷砖.md
│   └── 艺术漆.md
└── 04_Styles/
    └── 法式轻奢.md
单个案例文件示例 (案例_雅加达南区_法式公寓.md)：

markdown
---
style: [[法式轻奢]]
location: 雅加达南区
total_area: 120
spaces: [[客厅]] [[卧室]] [[厨房]]
budget: 250,000,000 IDR
---

## 实景照片
![[photo_01.jpg]]
![[photo_02.jpg]]

## 材料清单
- 地面: [[大理石瓷砖]] (品牌: XXX, 单价: 850,000/m²)
- 墙面: [[艺术漆]] (品牌: YYY, 单价: 350,000/m²)
所有 [[双链]] 将在编译时自动解析为图谱中的 关系边 (Edge)。

编译命令
bash
npm run build
# 读取 /obsidian-vault/ 目录下的所有 .md 文件
# 输出 /data/nodes.json 和 /data/edges.json
☁️ Cloudflare 部署
部署 Worker
bash
npm run deploy
# 使用 Wrangler 部署到 Cloudflare Workers
配置环境变量
在 Cloudflare Dashboard 中设置：

变量名	说明
KG_DATA_URL	R2 中 nodes.json / edges.json 的访问地址
MCP_API_KEY	（可选）API 鉴权密钥
🤝 贡献指南
欢迎 PR！特别欢迎以下贡献：

新增案例数据：提交标准格式的 Markdown 文件到 /obsidian-vault/01_Cases/

新增材料数据：印尼本地建材的价格/品牌信息

新增 MCP Tool：扩展知识图谱的推理能力

优化解析引擎：提升 Markdown → JSON 的编译效率

PR 流程
Fork 本仓库

创建你的特性分支 (git checkout -b feature/amazing-feature)

提交改动 (git commit -m 'Add some amazing feature')

推送到分支 (git push origin feature/amazing-feature)

开启一个 Pull Request

📄 许可证
MIT License — 可自由使用、修改、商业化。

📬 联系方式
作者：@vfvincentwong2026

主项目：Nusantara-Atelier

Built with ❤️ for the Indonesian interior design community.
