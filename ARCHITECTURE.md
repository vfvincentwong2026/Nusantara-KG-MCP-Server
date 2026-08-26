# 架构设计文档

## 🏗️ 整体架构
┌─────────────────────────────────────────────────────────────────┐
│ 数据策展层 │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ Obsidian Vault (Markdown + YAML + 双链 + 图片) │ │
│ │ 01_Cases/ 02_Styles/ 03_Spaces/ 04_Materials/ │ │
│ │ 05_Processes/ 06_Labor/ 07_WorkHours/ 08_Effects/ │ │
│ └─────────────────────────────────────────────────────────┘ │
│ │ │
│ ▼ (Git Push) │
├─────────────────────────────────────────────────────────────────┤
│ 编译层 │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ GitHub Actions + parser.js │ │
│ │ • 读取所有 .md 文件 │ │
│ │ • 解析 YAML Frontmatter │ │
│ │ • 提取 [[双链]] 关系 │ │
│ │ • 输出 nodes.json + edges.json │ │
│ └─────────────────────────────────────────────────────────┘ │
│ │ │
│ ▼ (Deploy) │
├─────────────────────────────────────────────────────────────────┤
│ 服务层 │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ Cloudflare Workers (MCP Server) │ │
│ │ • 加载 nodes.json + edges.json │ │
│ │ • 提供 MCP 协议 SSE 服务 │ │
│ │ • 多模态识别 (调用 Vision API) │ │
│ └─────────────────────────────────────────────────────────┘ │
│ │ │
│ ▼ (MCP Protocol) │
├─────────────────────────────────────────────────────────────────┤
│ 消费层 │
│ ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐ │
│ │ Claude │ │ Cursor │ │ Atelier │ │ 其他AI │ │
│ │ Desktop │ │ │ │ (主项目) │ │ Agent │ │
│ └───────────┘ └───────────┘ └───────────┘ └───────────┘ │
└─────────────────────────────────────────────────────────────────┘

text

---

## 📊 数据模型

### 核心实体

```typescript
// 节点 (Node)
interface Node {
  id: string;                    // 唯一标识
  type: EntityType;              // case | style | space | material | process | labor | workhour | effect
  name: {
    en: string;
    zh: string;
    id: string;
  };
  properties: Record<string, any>; // 类型特定的属性
  images?: string[];
  indegree?: number;             // 被引用次数 (热度)
  tags?: string[];
}

// 关系边 (Edge)
interface Edge {
  source: string;                // 源节点 ID
  target: string;                // 目标节点 ID
  relation: RelationType;        // contains | recommends | requires | matches | alternative_of
  weight?: number;               // 关系强度 (0-1)
}
关系类型
关系	说明	示例
contains	包含关系	案例 → 空间, 空间 → 材料
recommends	推荐关系	工艺 → 人工, 风格 → 材料
requires	必需关系	工艺 → 工具, 材料 → 工艺
matches	匹配关系	案例 → 风格, 材料 → 风格
alternative_of	替代关系	工艺A → 工艺B (平替)
🔌 MCP 协议实现
工具定义
typescript
interface MCPTool {
  name: string;
  description: string;
  inputSchema: {
    type: "object";
    properties: Record<string, any>;
    required?: string[];
  };
}
工具注册
typescript
// src/tools/index.ts
export const tools: MCPTool[] = [
  {
    name: "quick_estimate",
    description: "快速估价，基于风格+面积+空间+地区",
    inputSchema: {
      type: "object",
      properties: {
        style: { type: "string", description: "设计风格" },
        area: { type: "number", description: "面积 (m²)" },
        spaces: { type: "array", items: { type: "string" }, description: "空间列表" },
        location: { type: "string", description: "地区" }
      },
      required: ["style", "area"]
    }
  },
  // ... 更多工具
];
调用流程
text
用户请求 → MCP Server 接收 → 验证参数 → 
执行工具函数 → 查询知识图谱 → 推理计算 → 
返回结构化结果
🧠 推理引擎设计
估价推理
text
用户输入: { style: "法式轻奢", area: 120, location: "Jakarta" }
    ↓
1. 查询匹配案例
    SELECT * FROM nodes WHERE type='case' AND style='法式轻奢'
    → 返回 3 个最相似案例
    ↓
2. 查询空间配置
    根据案例中的 spaces 字段，提取空间列表
    → [客厅, 卧室, 厨房, 卫浴]
    ↓
3. 查询材料推荐
    对每个空间，查询推荐的 materials
    → { 客厅: [大理石瓷砖, 艺术漆], ... }
    ↓
4. 查询工艺与人工
    对每个材料，查询所需工艺和推荐人工
    → { 大理石瓷砖: { process: 湿铺法贴砖, labor: 中国技工 } }
    ↓
5. 查询工时定额
    对每个工艺，查询工时/m²
    → { 湿铺法贴砖: 2.5 工时/m² }
    ↓
6. 计算总价
    材料费 + 人工费 (日薪 × 工日) + 辅材费
    ↓
返回: { total: 285,000,000, breakdown: {...}, timeline: {...} }
识图推理
text
用户输入: { image_url: "https://...", area: 120 }
    ↓
1. 多模态识别 (调用 Vision API)
    → 识别出: ["悬浮吊顶", "无主灯", "微水泥", "大板通铺"]
    ↓
2. 关键词 → 图谱节点
    查询 nodes 中匹配关键词的实体
    → [工艺_悬浮吊顶, 工艺_无主灯, 工艺_微水泥, 工艺_大板铺贴]
    ↓
3. 对每个工艺节点:
    • 查询推荐人工 → 中国技工
    • 查询工时定额 → X 工时/m²
    • 查询对应材料 → 推荐材料列表
    ↓
4. 计算总价与工期
    • 各工序材料费 + 人工费
    • 各工序工时累加 → 总工期
    ↓
返回: { processes: [...], total_cost: ..., total_timeline: ... }
📁 项目结构
text
Nusantara-KG-MCP-Server/
├── .github/
│   └── workflows/
│       └── deploy.yml              # GitHub Actions 部署流水线
├── src/
│   ├── index.ts                    # MCP Server 入口
│   ├── tools/                      # MCP 工具实现
│   │   ├── index.ts                # 工具注册
│   │   ├── quick-estimate.ts
│   │   ├── analyze-photo.ts
│   │   ├── precise-estimate.ts
│   │   └── ...
│   ├── graph/                      # 知识图谱查询引擎
│   │   ├── loader.ts               # 加载 nodes.json + edges.json
│   │   ├── query.ts                # 图谱查询函数
│   │   └── reasoning.ts            # 推理引擎
│   ├── parser/                     # Obsidian → JSON 解析器
│   │   ├── index.ts                # 入口
│   │   ├── md-parser.ts            # Markdown 解析
│   │   └── link-extractor.ts       # [[双链]] 提取
│   └── types/                      # TypeScript 类型定义
│       └── index.ts
├── obsidian-vault/                 # 数据源 (git submodule)
│   ├── 01_Cases/
│   ├── 02_Styles/
│   ├── 03_Spaces/
│   ├── 04_Materials/
│   ├── 05_Processes/
│   ├── 06_Labor/
│   ├── 07_WorkHours/
│   └── 08_Effects/
├── data/                           # 编译输出
│   ├── nodes.json
│   └── edges.json
├── package.json
├── tsconfig.json
├── wrangler.toml                   # Cloudflare 部署配置
└── README.md
🔐 安全与权限
层级	访问控制	说明
Obsidian Vault	私有	核心数据，仅团队内部可访问
GitHub 数据仓库	私有	存储 MD 文件和图片
GitHub Actions	私有	编译和部署流水线
Cloudflare R2	公开读	图片 CDN，支持缓存
MCP Server	API Key 鉴权	所有工具调用需验证
主项目调用	内部 Token	无需外部鉴权
📈 扩展性设计
新增实体类型：在 types/index.ts 中扩展 EntityType

新增 MCP 工具：在 src/tools/ 下新建文件，在 index.ts 注册

新增数据源：支持从 CSV/API 导入，只需实现 parser/ 接口

多模态模型切换：通过环境变量配置 API 端点，可替换为任何 Vision API
