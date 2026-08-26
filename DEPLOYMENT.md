```markdown
# 部署指南

## 🎯 部署目标

- **Cloudflare Workers**: MCP Server 运行环境
- **Cloudflare D1**: 知识图谱数据存储
- **Cloudflare R2**: 图片/静态资源存储
- **GitHub Actions**: CI/CD 自动化流水线

---

## 📋 前置条件

- [ ] Cloudflare 账号 (免费)
- [ ] GitHub 账号 (免费)
- [ ] 域名 (可选，可用 workers.dev 子域名)
- [ ] Vision API 密钥 (GPT-4o / Claude Vision)

---

## ☁️ Cloudflare 资源创建

### 1. 创建 R2 存储桶

```bash
npx wrangler r2 bucket create nusantara-kg-images
2. 创建 D1 数据库
bash
npx wrangler d1 create nusantara-kg
# 记录 database_id
3. 创建 Workers 项目
bash
npx wrangler init
# 选择 TypeScript 模板
🔧 环境变量配置
在 Cloudflare Dashboard 中设置：

变量名	值	说明
R2_BUCKET_URL	https://...r2.cloudflarestorage.com	R2 图片访问地址
R2_ACCESS_KEY	xxx	R2 访问密钥
KG_DATA_URL	https://.../nodes.json	图谱数据地址
VISION_API_KEY	xxx	多模态识别 API 密钥
VISION_API_ENDPOINT	https://api.openai.com/v1/chat/completions	Vision API 端点
ALLOWED_ORIGINS	https://your-atelier.com	CORS 白名单
🔄 GitHub Actions 自动部署
配置 Secrets
在 GitHub 仓库 Settings → Secrets and variables → Actions 中添加：

Secret 名称	值
CLOUDFLARE_API_TOKEN	Cloudflare API Token
CLOUDFLARE_ACCOUNT_ID	Cloudflare Account ID
R2_ACCESS_KEY	R2 访问密钥
R2_SECRET_KEY	R2 密钥
VISION_API_KEY	Vision API 密钥
