---
title: "谷歌云盘文件管理器"
description: "该MCP服务器与Google Drive集成，以允许列出、读取和搜索文件。"
---

# 谷歌云盘文件管理器

该MCP服务器与Google Drive集成，以允许列出、读取和搜索文件。

# Google Drive 服务器

此 MCP 服务器与 Google Drive 集成，允许列出、读取和搜索文件。

## 组件

### 工具

- **search**
  - 在 Google Drive 中搜索文件
  - 输入：`query` (字符串)：搜索查询
  - 返回匹配文件的文件名和 MIME 类型

### 资源

该服务器提供对 Google Drive 文件的访问：

- **文件** (`gdrive:///`)
  - 支持所有文件类型
  - Google Workspace 文件会自动导出：
    - 文档 → Markdown
    - 表格 → CSV
    - 演示文稿 → 纯文本
    - 图表 → PNG
  - 其他文件以原始格式提供

## 快速开始

1. [创建一个新的 Google Cloud 项目](https://console.cloud.google.com/projectcreate)
2. [启用 Google Drive API](https://console.cloud.google.com/workspace-api/products)
3. [配置 OAuth 同意屏幕](https://console.cloud.google.com/apis/credentials/consent)（测试时选择“内部”即可）
4. 添加 OAuth 范围 `https://www.googleapis.com/auth/drive.readonly`
5. [为应用程序类型“桌面应用”创建 OAuth 客户端 ID](https://console.cloud.google.com/apis/credentials/oauthclient)
6. 下载客户端的 OAuth 密钥 JSON 文件
7. 将密钥文件重命名为 `gcp-oauth.keys.json` 并放置在此仓库的根目录中（即 `servers/gcp-oauth.keys.json`）

确保使用 `npm run build` 或 `npm run watch` 构建服务器。

### 认证

要进行认证并保存凭据：

1. 使用 `auth` 参数运行服务器：`node ./dist auth`
2. 这将在系统浏览器中打开一个认证流程
3. 完成认证过程
4. 凭据将保存在此仓库的根目录中（即 `servers/.gdrive-server-credentials.json`）

### 与桌面应用集成

要将此服务器与桌面应用集成，请在应用的服务器配置中添加以下内容：

#### Docker

认证：

假设您已经在 Google Cloud 上完成了 OAuth 应用程序的设置，现在可以使用以下命令对服务器进行认证，将 `/path/to/gcp-oauth.keys.json` 替换为您的 OAuth 密钥文件路径：

```bash
docker run -i --rm --mount type=bind,source=/path/to/gcp-oauth.keys.json,target=/gcp-oauth.keys.json -v mcp-gdrive:/gdrive-server -e GDRIVE_OAUTH_PATH=/gcp-oauth.keys.json -e "GDRIVE_CREDENTIALS_PATH=/gdrive-server/credentials.json" -p 3000:3000 mcp/gdrive auth
```

该命令将打印出要在浏览器中打开的 URL。在浏览器中打开此 URL 并完成认证过程。凭据将保存在 `mcp-gdrive` 卷中。

一旦认证完成，您可以在应用的服务器配置中使用该服务器：

```json
{
  "mcpServers": {
    "gdrive": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "-v", "mcp-gdrive:/gdrive-server", "-e", "GDRIVE_CREDENTIALS_PATH=/gdrive-server/credentials.json", "mcp/gdrive"]
    }
  }
}
```

#### NPX

```json
{
  "mcpServers": {
    "gdrive": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-gdrive"
      ]
    }
  }
}
```

## 许可

此 MCP 服务器根据 MIT 许可证许可。这意味着您可以自由地使用、修改和分发软件，但需遵守 MIT 许可证的条款和条件。有关更多详细信息，请参阅项目仓库中的 LICENSE 文件。

**官方网站：** [https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive](https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`research and data`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @modelcontextprotocol/server-gdrive`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/modelcontextprotocol-gdrive.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
