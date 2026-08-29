# 资源中心实施计划

## 目标

建设独立站点 `res.aidyou.ai`，集中维护并发布 ChatSpeed 生态资源：

1. MCP 服务目录，可按频道、分类、标签搜索，并支持导入 ChatSpeed。
2. 模型供应商和模型目录，兼容 `src/components/setting/Model.vue` 的供应商导入流程。
3. 免费 AI 网站目录，记录免费额度、登录要求、有效性验证时间，并为后续模型/API 导入保留关联字段。
4. 所有资源通过程序校验后自动生成机器可读索引，避免手工维护索引。

当前仓库仅保留少量契约示例：Context7、NVIDIA NIM、OpenRouter 和 ModelScope；后续资源录入不改变目录和索引接口。


- VuePress 2 + Vite + vuepress-theme-hope 静态站点骨架。
- 多语言资源字段约定：`en`、`zh-Hans`、`zh-Hant`。
- `resources/mcp/`：MCP 服务资源。
- `resources/models/`：模型供应商资源。
- `resources/free-ai/`：免费 AI/API 服务资源。
- Python 标准库索引生成器。
- 资源唯一 ID、分类、URL、状态、更新时间、跨资源引用校验。
- ChatSpeed 兼容的 MCP `config.mcpServers` 和模型供应商 `provider` 字段。
- Cloudflare Pages 配置说明和 GitHub Actions 发布入口。

## 数据流

```text
resources/**/*.json
        |
        v
scripts/build-index.py
  |  校验资源、交叉引用、URL、重复 ID
        |
        +--> public/catalog/*.json       给网站访客和 ChatSpeed 使用
        +--> docs/**/*.md                给 VuePress 列表和详情页使用
        +--> VuePress build              生成静态站点
```

## 阶段二：填充和展示资源

1. 按模板录入首批 MCP 资源。
2. 迁移当前 `public/presetMcp.json`，保留原有配置语义。
3. 按模板录入模型供应商，将当前 `public/presetTextAiProvider.json` 的字段映射到 `provider`。
4. 开发 MCP、模型供应商、免费 AI 的频道列表、分类筛选和搜索组件。
5. 为每个资源生成独立详情页，并完善标题、描述、关键词和结构化数据。
6. 为缺少翻译的资源提供回退策略，并逐步补齐三种语言。

## 阶段三：接入 ChatSpeed

### MCP

`Mcp.vue` 当前需要的核心结构是：

```js
{
  name,
  description,
  website,
  config: {
    mcpServers: {
      [name]: {
        type,
        command,
        args,
        env,
        url,
        bearer_token,
        proxy
      }
    }
  }
}
```

资源站索引保留该结构，ChatSpeed 只需将本地 `/presetMcp.json` 的读取地址切换为远程 `/catalog/mcp.json`，并把搜索字段扩展到本地化名称、描述、分类和标签。

### 模型供应商

`Model.vue` 当前导入流程接收供应商对象，重点字段为：

```js
{
  protocol,
  name,
  logo,
  desc,
  baseUrl,
  models,
  maxTokens,
  temperature,
  topP,
  topK,
  documentationUrl,
  modelListUrl,
  keyApplyUrl
}
```

- `GET /catalog/index.json`：频道索引和资源数量。
- `GET /catalog/mcp.json`：兼容 `Mcp.vue` 的 MCP 预设结构。
- `GET /catalog/model-providers.json`：兼容 `Model.vue` 的供应商预设结构。
- `GET /catalog/free-ai.json`：免费 AI/API 服务描述和模型供应商关联。

### 免费 AI

免费 AI 网站不是全部都能导入 ChatSpeed，因此数据模型区分两种情况：

- 只有网站访问入口：用户点击详情页访问。
- 同时提供 API/模型配置：通过 `freeAi.modelProviderRef` 和可选的 `freeAi.integrations.chatSpeedModel` 关联一个模型供应商资源，声明 API 协议、Base URL、模型列表和密钥申请地址，但不存储任何密钥。

这种设计可以让“免费 AI 网站”和“免费模型 API”统一展示，又不会误导用户认为所有网站都有可导入 API。

## 阶段四：自动化和质量控制

每次 Pull Request 至少执行：

1. `python3 scripts/build-index.py --check`
2. `pnpm build`

校验失败时不得生成或发布索引。后续可以增加：

- 资源链接定期可用性检查；
- `lastVerifiedAt` 超期提醒；
- GitHub CODEOWNERS 审核；
- 自动生成变更摘要；
- 人工确认后更新 `status`。

## 阶段五：Cloudflare 发布

使用 Cloudflare Pages 连接 `aidyou/chatspeed-res`：

- 构建命令：`pnpm build`
- 输出目录：`dist`
- 生产域名：`res.aidyou.ai`
- 预览部署：Pull Request 自动生成预览地址

第一阶段不需要 Worker、D1 或登录系统。静态 JSON 由 Pages CDN 发布，足以支撑目录、搜索和 ChatSpeed 读取。资源数量或管理需求明显增加后，再增加 Worker API、D1 和后台审核，不改变资源文件与索引格式。

## 非目标

第一阶段不做：

- 在线用户投稿后台；
- 用户账号、收藏和评论；
- 代理运行 MCP 服务；
- 代存用户 API Key；
- 对免费 AI 服务做自动登录或绕过限制；
- 直接抓取并未经审核发布第三方配置。

## 风险和原则

- 远程 MCP 配置是不可信输入，ChatSpeed 仍需保留现有 URL、命令、参数和占位符校验。
- 资源的“免费”和“有效”具有时效性，必须展示 `lastVerifiedAt`，过期资源进入待复核状态。
- 任何目录文件都不能包含真实密钥。
- `provider` 和 `config` 是对现有客户端的兼容层，内部资源格式可以继续扩展，但不能破坏这两个公开契约。
