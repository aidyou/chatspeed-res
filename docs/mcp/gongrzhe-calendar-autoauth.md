---
title: "日历自动认证MCP服务器"
description: "用于Cluade桌面端与Google日历集成的服务器，支持自动身份验证。此服务器使人工智能助手能够通过自然语言交互来管理Google日历事件。"
---

# 日历自动认证MCP服务器

用于Cluade桌面端与Google日历集成的服务器，支持自动身份验证。此服务器使人工智能助手能够通过自然语言交互来管理Google日历事件。

# Calendar AutoAuth MCP 服务器

一个用于 Claude Desktop 中 Google 日历集成的支持自动认证的 Model Context Protocol (MCP) 服务器。该服务器使 AI 助手能够通过自然语言交互来管理 Google 日历事件。

![](/mcp-assets/c1486b4e2d8cfd67ed0257afeefda188.svg 'MCP 服务器')
[Smithery](https://smithery.ai/server/@gongrzhe/server-calendar-autoauth-mcp)
[![npm 版本](/mcp-assets/8e7cef31ffd2a60eb8a10d31be875b35.svg)](https://www.npmjs.com/package/@gongrzhe/server-calendar-autoauth-mcp)
[![许可证: ISC](/mcp-assets/3c4ddecb6971fce104f5f6280854eae3.svg)](https://opensource.org/licenses/ISC)

## 功能

- 创建带有标题、时间、描述和位置的日历事件
- 通过事件 ID 检索事件详情
- 更新现有事件（标题、时间、描述、位置）
- 删除事件
- 列出指定时间范围内的事件
- 完全集成 Google 日历 API
- 简单的 OAuth2 认证流程，支持自动浏览器启动
- 支持桌面应用程序和服务端应用凭据
- 全局凭据存储以方便使用

## 安装与认证

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@gongrzhe/server-calendar-autoauth-mcp) 自动安装适用于 Claude Desktop 的 Calendar AutoAuth 服务器：

```bash
npx -y @smithery/cli install @gongrzhe/server-calendar-autoauth-mcp --client claude
```

1. 创建 Google Cloud 项目并获取凭据：

   a. 创建 Google Cloud 项目：
      - 前往 [Google Cloud Console](https://console.cloud.google.com/)
      - 创建一个新项目或选择一个现有项目
      - 为您的项目启用 Google 日历 API

   b. 创建 OAuth 2.0 凭据：
      - 转到“API 和服务”>“凭据”
      - 点击“创建凭据”>“OAuth 客户端 ID”
      - 选择“桌面应用”或“Web 应用程序”作为应用程序类型
      - 给它命名并点击“创建”
      - 对于 Web 应用程序，将 `http://localhost:3000/oauth2callback` 添加到授权重定向 URI 列表中
      - 下载客户端的 OAuth 密钥 JSON 文件
      - 将密钥文件重命名为 `gcp-oauth.keys.json`

2. 运行身份验证：

   您可以通过两种方式进行身份验证：

   a. 全局身份验证（推荐）：
```bash
   # 首次使用：将 gcp-oauth.keys.json 放在主目录下的 .calendar-mcp 文件夹中
   mkdir -p ~/.calendar-mcp
   mv gcp-oauth.keys.json ~/.calendar-mcp/

   # 可以从任何位置运行身份验证
   npx @gongrzhe/server-calendar-autoauth-mcp auth
```

   b. 本地身份验证：
```bash
   # 将 gcp-oauth.keys.json 放在当前目录中
   # 文件将自动复制到全局配置
   npx @gongrzhe/server-calendar-autoauth-mcp auth
```

   身份验证过程将：
   - 在当前目录或 `~/.calendar-mcp/` 中查找 `gcp-oauth.keys.json`
   - 如果在当前目录找到，则将其复制到 `~/.calendar-mcp/`
   - 打开默认浏览器进行 Google 身份验证
   - 将凭据保存为 `~/.calendar-mcp/credentials.json`

   > **注意**:
   > - 成功认证后，凭据存储在 `~/.calendar-mcp/` 中，并可以从任何目录访问
   > - 同时支持桌面应用和 Web 应用程序凭据
   > - 对于 Web 应用程序凭据，请确保将 `http://localhost:3000/oauth2callback` 添加到您的授权重定向 URI 列表中

3. 在 Claude Desktop 中配置：

```json
{
  "mcpServers": {
    "calendar": {
      "command": "npx",
      "args": [
        "@gongrzhe/server-calendar-autoauth-mcp"
      ]
    }
  }
}
```

### Docker 支持

如果您更喜欢使用 Docker：

1. 身份验证：
```bash
docker run -i --rm \
  --mount type=bind,source=/path/to/gcp-oauth.keys.json,target=/gcp-oauth.keys.json \
  -v mcp-calendar:/calendar-server \
  -e CALENDAR_OAUTH_PATH=/gcp-oauth.keys.json \
  -e "CALENDAR_CREDENTIALS_PATH=/calendar-server/credentials.json" \
  -p 3000:3000 \
  mcp/calendar auth
```

2. 使用方法：
```json
{
  "mcpServers": {
    "calendar": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-v",
        "mcp-calendar:/calendar-server",
        "-e",
        "CALENDAR_CREDENTIALS_PATH=/calendar-server/credentials.json",
        "mcp/calendar"
      ]
    }
  }
}
```

## 使用示例

服务器提供了几种可以通过 Claude Desktop 使用的工具：

### 创建事件
```json
{
  "summary": "Team Meeting",
  "start": {
    "dateTime": "2024-01-20T10:00:00Z"
  },
  "end": {
    "dateTime": "2024-01-20T11:00:00Z"
  },
  "description": "Weekly team sync",
  "location": "Conference Room A"
}
```

### 列出事件
```json
{
  "timeMin": "2024-01-01T00:00:00Z",
  "timeMax": "2024-12-31T23:59:59Z",
  "maxResults": 10,
  "orderBy": "startTime"
}
```

### 更新事件
```json
{
  "eventId": "event123",
  "summary": "Updated Meeting Title",
  "start": {
    "dateTime": "2024-01-20T11:00:00Z"
  },
  "end": {
    "dateTime": "2024-01-20T12:00:00Z"
  }
}
```

### 删除事件
```json
{
  "eventId": "event123"
}
```

## 安全须知

- OAuth 凭据安全地存储在您的本地环境 (`~/.calendar-mcp/`) 中
- 服务器使用离线访问来保持持久的身份验证
- 切勿共享或将凭据提交到版本控制系统
- 定期检查并在 Google 帐户设置中撤销未使用的访问权限
- 凭据是全局存储的，但仅当前用户可访问

## 故障排除

1. **找不到 OAuth 密钥**
   - 确保 `gcp-oauth.keys.json` 文件位于当前目录或 `~/.calendar-mcp/` 目录中
   - 检查文件权限

2. **无效的凭证格式**
   - 确保证书文件中包含 `web` 或 `installed` 凭证
   - 对于 Web 应用程序，请验证重定向 URI 是否正确配置

3. **端口已被占用**
   - 如果 3000 端口已被占用，请在运行身份验证之前释放该端口
   - 您可以找到并停止使用该端口的进程

## 贡献

欢迎贡献！请随时提交 Pull Request。

## 许可证

本项目采用 ISC 许可证。

## 作者

gongrzhe

## 支持

如果您遇到任何问题或有疑问，请在 GitHub 仓库中提交一个 issue。

**官方网站：** [https://github.com/GongRzhe/Calendar-Autoauth-MCP-Server](https://github.com/GongRzhe/Calendar-Autoauth-MCP-Server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`productivity`
- 标签：`calendar management`, `communication`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`@gongrzhe/server-calendar-autoauth-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/gongrzhe-calendar-autoauth.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
