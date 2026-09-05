---
title: "WordPress MCP 服务器"
description: "使用此MCP WordPress服务器与您的WordPress网站进行交互。 100% 使用Cline创建。如果您使用Cline，可以通过指向代码库并询问代码是否安全来让其评估代码。 请参阅READ.me以获取详细概述。 享受吧！"
---

# WordPress MCP 服务器

使用此MCP WordPress服务器与您的WordPress网站进行交互。 100% 使用Cline创建。如果您使用Cline，可以通过指向代码库并询问代码是否安全来让其评估代码。 请参阅READ.me以获取详细概述。 享受吧！

# WordPress MCP 服务器

适用于 WordPress 集成的 Model Context Protocol (MCP) 服务器，兼容 Windows、macOS 和 Linux。

## 概述

此 MCP 服务器通过 WordPress REST API 实现与 WordPress 站点的交互。它提供了使用 JSON-RPC 2.0 协议创建、检索和更新文章的工具。

## 安装

1. 克隆仓库
2. 安装依赖项：
```bash
npm install
```
3. 构建项目：
```bash
npm run build
```

## 配置

在您的 MCP 设置文件中添加服务器，并使用环境变量设置 WordPress 凭证：

```json
{
  "mcpServers": {
    "wordpress": {
      "command": "node",
      "args": ["path/to/build/index.js"],
      "env": {
        "WORDPRESS_SITE_URL": "https://your-wordpress-site.com",
        "WORDPRESS_USERNAME": "your-username",
        "WORDPRESS_PASSWORD": "your-app-password"
      }
    }
  }
}
```

环境变量包括：
- WORDPRESS_SITE_URL: 您的 WordPress 站点 URL
- WORDPRESS_USERNAME: WordPress 用户名
- WORDPRESS_PASSWORD: WordPress 应用程序密码

您也可以选择不在环境变量中提供这些凭证，而是在请求参数中直接提供。

## 可用方法

### create_post
创建新的 WordPress 文章。

参数：
- siteUrl: (如果已在环境变量中设置则可选) WordPress 站点 URL
- username: (如果已在环境变量中设置则可选) WordPress 用户名
- password: (如果已在环境变量中设置则可选) WordPress 应用程序密码
- title: 文章标题
- content: 文章内容
- status: (可选) 'draft' | 'publish' | 'private' (默认: 'draft')

### get_posts
检索 WordPress 文章。

参数：
- siteUrl: (如果已在环境变量中设置则可选) WordPress 站点 URL
- username: (如果已在环境变量中设置则可选) WordPress 用户名
- password: (如果已在环境变量中设置则可选) WordPress 应用程序密码
- perPage: (可选) 每页的文章数量 (默认: 10)
- page: (可选) 页码 (默认: 1)

### update_post
更新现有的 WordPress 文章。

参数：
- siteUrl: (如果已在环境变量中设置则可选) WordPress 站点 URL
- username: (如果已在环境变量中设置则可选) WordPress 用户名
- password: (如果已在环境变量中设置则可选) WordPress 应用程序密码
- postId: 要更新的文章 ID
- title: (可选) 新文章标题
- content: (可选) 新文章内容
- status: (可选) 'draft' | 'publish' | 'private'

## 安全提示

为了安全起见，建议使用 WordPress 应用程序密码而不是您的主账户密码。您可以在 WordPress 仪表板的用户 → 安全 → 应用程序密码下生成应用程序密码。

## 使用示例

使用环境变量：
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "create_post",
  "params": {
    "title": "My New Post",
    "content": "Hello World!",
    "status": "draft"
  }
}
```

不使用环境变量：
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "create_post",
  "params": {
    "siteUrl": "https://your-wordpress-site.com",
    "username": "your-username",
    "password": "your-app-password",
    "title": "My New Post",
    "content": "Hello World!",
    "status": "draft"
  }
}
```

## 要求

- Node.js 20.0.0 或更高版本
- 启用了 REST API 的 WordPress 站点
- 用于身份验证的 WordPress 应用程序密码

## 许可证

MIT 许可证 - 详情请参阅 LICENSE 文件

**官方网站：** [https://github.com/stefans71/wordpress-mcp-server](https://github.com/stefans71/wordpress-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`productivity`
- 标签：`other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`path/to/build/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/stefans71-wordpress.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
