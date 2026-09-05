# ChatSpeed Resource Center

独立的 ChatSpeed 资源中心，部署地址为 `https://res.aidyou.ai`。

当前仓库包含少量用于验证契约的示例：Context7、NVIDIA NIM、OpenRouter 和 ModelScope。它们不是完整资源库，后续按规范逐步补充。

免费额度是动态信息。NVIDIA NIM 和 OpenRouter 的免费可用性/限制需要以官方页面为准；“魔塔认证后 2000 次/天”当前作为待核验声明保存，不会被程序当作固定保证。

## 技术方案

- VuePress 2 + Vite + vuepress-theme-hope：负责站点展示、SEO、频道列表和独立资源详情页。
- JSON 资源文件：每个资源一个文件，便于审查、回滚和协作。
- Python 索引生成器：只使用 Python 标准库，生成索引前强制校验资源。
- GitHub Actions：校验资源、生成索引并构建站点。

## 本地开发

```bash
pnpm install
pnpm docs:dev
```

开发服务器默认地址为 `http://localhost:8080`。`pnpm docs:dev` 会同时监视 `resources/**/*.json`：修改资源后，脚本自动重新生成导入索引和 VuePress 详情页，页面会热更新。

生产构建：

```bash
pnpm build
```

## 添加资源

资源规范和字段说明见 [`RESOURCE_SPEC.md`](./RESOURCE_SPEC.md)。模板位于：

- `resources/mcp/`：MCP 服务资源。
- `resources/free-ai/`：免费 AI/API 服务资源；自带 `provider` 配置的服务可直接导入 ChatSpeed。

添加资源后运行：

```bash
pnpm catalog:check  # 只校验，不改写索引
pnpm catalog:build  # 校验通过后生成索引
```

- `public/catalog/`：公开的 ChatSpeed 导入索引。
- `docs/`：由脚本生成的 VuePress 列表页和独立详情页。
- `src/data/generated/`：内部兼容数据产物。

## 目录接口

- `GET /catalog/index.json`（频道目录和条数）
- `GET /catalog/mcp.json`（兼容 `Mcp.vue`）
- `GET /catalog/model-providers.json`（兼容 `Model.vue`；由自带 `provider` 配置的免费 AI 资源生成，`models.json` 为其兼容别名）
- `GET /catalog/free-ai.json`（免费服务说明与供应商配置）

索引是公开数据，不得放入 API Key、密码、Bearer Token 或其他用户凭据。需要填写密钥的资源只能声明参数名称和申请地址。

## 发布

Cloudflare Pages 建议配置：

- 构建命令：`pnpm build`
- 输出目录：`docs/.vuepress/dist`
- Node.js：18 或更高版本
- 自定义域名：`res.aidyou.ai`

详细阶段计划见 [`PLAN.md`](./PLAN.md)。
