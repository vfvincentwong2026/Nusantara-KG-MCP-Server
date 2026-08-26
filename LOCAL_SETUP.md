```markdown
# 本地开发指南

## 📦 环境要求

- Node.js >= 18
- npm >= 9
- Obsidian (推荐，用于数据策展)
- Cloudflare CLI (wrangler) [可选，用于部署]

---

## 🚀 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/vfvincentwong2026/Nusantara-KG-MCP-Server.git
cd Nusantara-KG-MCP-Server
2. 安装依赖
bash
npm install
3. 准备数据
方式 A: 使用示例数据
bash
cp -r examples/obsidian-vault/ ./obsidian-vault/
方式 B: 链接你的 Obsidian Vault
bash
ln -s ~/path/to/your/obsidian-vault ./obsidian-vault
4. 编译知识图谱
bash
npm run build
# 输出: data/nodes.json, data/edges.json
5. 启动 MCP Server
bash
npm run dev
# 服务运行在 http://localhost:3000
🧪 测试工具调用
测试 quick_estimate
bash
curl -X POST http://localhost:3000/sse \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
      "name": "quick_estimate",
      "arguments": {
        "style": "法式轻奢",
        "area": 120,
        "spaces": ["客厅", "卧室", "厨房"],
        "location": "Jakarta Selatan"
      }
    },
    "id": 1
  }'
测试 analyze_design_photo
bash
curl -X POST http://localhost:3000/sse \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
      "name": "analyze_design_photo",
      "arguments": {
        "image_url": "https://example.com/photo.jpg",
        "area": 120,
        "location": "Jakarta"
      }
    },
    "id": 2
  }'
📝 Obsidian 数据策展指南
创建新案例
在 obsidian-vault/01_Cases/ 下新建 案例_地区_风格.md

复制以下模板：

markdown
---
id: case_地区_风格
name:
  en: "English Name"
  zh: "中文名称"
  id: "Nama Indonesia"

style: [[风格名称]]
location: "地区"
total_area: 面积
budget: 总造价
spaces: [[空间1]] [[空间2]]
tags: ["标签1", "标签2"]
images: ["图片1.jpg", "图片2.jpg"]
---

## 项目概述
...

## 设计亮点
...

## 材料配置
- 地面: [[材料名称]] (品牌: XXX, 规格: XXX)
...

## 关键工艺
- [[工艺名称]]
...

## 实景照片
![[图片1.jpg]]
创建新工艺
在 obsidian-vault/05_Processes/ 下新建 工艺_名称.md

复制以下模板：

markdown
---
id: process_名称
name:
  en: "English Name"
  zh: "中文名称"
  id: "Nama Indonesia"

process_type: "分类"
difficulty_level: 3-5
space_applicable: [[空间1]] [[空间2]]
material_applicable: [[材料1]] [[材料2]]
images: ["工艺图1.jpg", "工艺图2.jpg"]
---

## 工艺参数
...

## 工序流程
### Step 1: 步骤名称
**描述**：...
**工具**：...
**验收**：...

## 验收标准
- ✅ 标准1
- ✅ 标准2

## 关联知识
- 推荐人工: [[人工节点]]
- 替代方案: [[替代工艺]]
双链规范
语法	说明
[[案例名称]]	链接到案例节点
[[工艺_名称]]	链接到工艺节点
![[图片.jpg]]	引用图片
key:: value	YAML 属性
🗂️ 数据验证
检查数据完整性
bash
npm run validate
# 检查: ID 唯一性, 双链有效性, 必填字段
查看图谱统计
bash
npm run stats
# 输出: 节点数, 边数, 各类实体数量
☁️ 部署到 Cloudflare
1. 登录 Cloudflare
bash
npx wrangler login
2. 配置 wrangler.toml
toml
name = "nusantara-kg-mcp"
main = "dist/index.js"
compatibility_date = "2024-11-01"

[[d1_databases]]
binding = "KG_DB"
database_name = "nusantara-kg"
database_id = "your-database-id"

[[r2_buckets]]
binding = "KG_IMAGES"
bucket_name = "nusantara-kg-images"
3. 部署
bash
npm run deploy
🐛 常见问题
Q: 编译时报错 "Cannot find module"
bash
rm -rf node_modules package-lock.json
npm install
Q: Obsidian 双链未被正确解析
检查文件路径是否在 obsidian-vault/ 目录下，双链语法是否为 [[文件名]]

Q: MCP Server 启动失败
检查端口 3000 是否被占用：

bash
lsof -i :3000
kill -9 [PID]
Q: 图片无法显示
确保图片在 obsidian-vault/images/ 目录，且引用路径正确

📚 推荐工具
工具	用途
Obsidian	数据策展编辑器
Obsidian Git	自动备份到 GitHub
Claude Desktop	本地 MCP 客户端测试
Postman	API 调试
