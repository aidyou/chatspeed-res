---
title: "热榜新闻"
description: "English | | [!NOTE] 这是一个仅支持中文的演示版本。后续将发布支持更好自定义和英文内容的完整版本。"
---

# 热榜新闻

English | | [!NOTE] 这是一个仅支持中文的演示版本。后续将发布支持更好自定义和英文内容的完整版本。

English | [简体中文](https://github.com/See-lo/newsnow/blob/HEAD/README.zh-CN.md) | [日本語](https://github.com/See-lo/newsnow/blob/HEAD/README.ja-JP.md)

> [!NOTE]
> 这是一个目前仅支持中文的演示版本。后续将发布一个功能更全面、支持自定义和英文内容的完整版本。

**_优雅阅读实时和最热门新闻_**

## 功能

- 清爽优雅的UI设计，提供最佳阅读体验
- 实时更新热门新闻
- 支持GitHub OAuth登录并同步数据
- 默认缓存时间为30分钟（已登录用户可以强制刷新）
- 根据源更新频率自适应抓取间隔（最小2分钟），以优化资源使用并防止IP被封禁
- 支持MCP服务器

```json

{

  "mcpServers": {

    "newsnow": {

      "command": "npx",

      "args": [

        "-y",

        "newsnow-mcp-server"

      ],

      "env": {

        "BASE_URL": "https://newsnow.busiyi.world"

      }

    }

  }

}

```
你可以将`BASE_URL`更改为自己的域名。

## 部署

### 基本部署

对于不需要登录和缓存的部署：

1. Fork此仓库
2. 导入到Cloudflare Page或Vercel等平台

### Cloudflare Page配置

- 构建命令: `pnpm run build`
- 输出目录: `dist/output/public`

### GitHub OAuth设置

1. [创建一个GitHub应用](https://github.com/settings/applications/new)
2. 不需要特殊权限
3. 将回调URL设置为: `https://your-domain.com/api/oauth/github`（将`your-domain`替换为你的实际域名）
4. 获取Client ID和Client Secret

### 环境变量

参考`example.env.server`。对于本地开发，将其重命名为`.env.server`并进行配置：

```env

# Github Client ID

G_CLIENT_ID=

# Github Client Secret

G_CLIENT_SECRET=

# JWT Secret, usually the same as Client Secret

JWT_SECRET=

# Initialize database, must be set to true on first run, can be turned off afterward

INIT_TABLE=true

# Whether to enable cache

ENABLE_CACHE=true

```
### 数据库支持

支持的数据库连接器：https://db0.unjs.io/connectors
**推荐使用Cloudflare D1数据库**。

1. 在Cloudflare Worker仪表板中创建D1数据库
2. 在`wrangler.toml`中配置`database_id`和`database_name`
3. 如果不存在`wrangler.toml`，请将`example.wrangler.toml`重命名并修改配置
4. 更改将在下次部署时生效

### Docker部署

在项目根目录下：

```sh

docker compose up

```
你也可以在`docker-compose.yml`中设置环境变量。

## 开发

> [!Note]
> 需要Node.js >= 20

```sh

corepack enable

pnpm i

pnpm dev

```
### 添加数据源

参考`shared/sources`和`server/sources`目录。项目提供了完整的类型定义和清晰的架构。

有关如何添加新数据源的详细说明，请参阅[CONTRIBUTING.md](https://github.com/See-lo/newsnow/blob/HEAD/CONTRIBUTING.md)。

## 路线图

- 增加**多语言支持**（英语、中文等）。
- 改进**个性化选项**（基于类别的新闻、保存偏好设置）。
- 扩展**数据源**以覆盖多种语言的全球新闻。

**_准备就绪后发布_**
![](/mcp-assets/2197d28504147a4aea26ca6d6a172b1b.gif)

## 贡献

欢迎贡献！随时提交拉取请求或创建问题来提出功能请求和报告错误。

有关如何贡献的详细指南，特别是关于添加新的数据源，请参阅[CONTRIBUTING.md](https://github.com/See-lo/newsnow/blob/HEAD/CONTRIBUTING.md)。

## 许可证

[MIT](https://github.com/See-lo/newsnow/blob/HEAD/LICENSE) © ourongxing

**官方网站：** [https://github.com/See-lo/newsnow](https://github.com/See-lo/newsnow)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`entertainment and media`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y newsnow-mcp-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/seeloqaq-newsnow.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
