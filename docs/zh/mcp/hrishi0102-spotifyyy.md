---
title: "Spotify音乐推荐"
description: "通过搜索歌曲、创建播放列表、获取推荐和管理Spotify账户中的音乐，使克劳德能够与Spotify进行互动。"
---

# Spotify音乐推荐

通过搜索歌曲、创建播放列表、获取推荐和管理Spotify账户中的音乐，使克劳德能够与Spotify进行互动。

# Spotify MCP 服务器

一个简单的模型上下文协议 (MCP) 服务器，让你可以通过 Claude 与 Spotify 进行交互。这个服务器使 Claude 能够使用你的 Spotify 账户搜索歌曲、创建播放列表、获取推荐等。

## 功能

- 在 Spotify 上搜索曲目
- 查看你的 Spotify 个人资料
- 创建播放列表
- 将曲目添加到播放列表
- 获取个性化音乐推荐

## 可用工具

| 工具名称                  | 描述                                              |
| -------------------------- | -------------------------------------------------------- |
| `set-spotify-credentials`  | 设置你的 Spotify 认证凭据              |
| `check-credentials-status` | 检查你的凭据是否有效以及谁已登录 |
| `search-tracks`            | 按名称、艺术家或关键词搜索曲目           |
| `get-current-user`         | 获取你的 Spotify 个人资料信息                     |
| `create-playlist`          | 在你的账户上创建一个新的播放列表                    |
| `add-tracks-to-playlist`   | 将曲目添加到现有的播放列表                       |
| `get-recommendations`      | 根据种子曲目获取推荐                 |

## 设置说明

### 1. 前提条件

- Node.js v16 或更高版本
- npm
- 一个 Spotify 账户
- 一个注册的 Spotify 开发者应用程序

### 2. 创建 Spotify 开发者应用

1. 前往 [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
2. 使用你的 Spotify 账户登录
3. 点击“创建一个应用”
4. 填写应用名称和描述
5. 添加 `http://localhost:8888/callback` 作为重定向 URI
6. 记下你的客户端 ID 和客户端密钥

### 3. 安装项目

```bash
# Clone or download the project first
cd spotify-mcp-server

# Install dependencies
npm install
```

### 4. 获取你的 Spotify 令牌

编辑 `spotify-auth.js` 文件以包含你的客户端 ID 和客户端密钥：

```javascript
// Replace these with your Spotify app credentials
const CLIENT_ID = "your_client_id_here";
const CLIENT_SECRET = "your_client_secret_here";
```

然后运行认证脚本：

```bash
node spotify-auth.js
```

这将：

1. 在浏览器中打开一个 URL
2. 提示你登录 Spotify
3. 请求你的权限来访问你的账户
4. 将令牌保存到 `secrets.json`

### 5. 构建 MCP 服务器

```bash
npm run build
```

### 6. 配置 Claude 桌面版

编辑你的 Claude 桌面版配置文件：

- 在 macOS 上：`~/Library/Application Support/Claude/claude_desktop_config.json`
- 在 Windows 上：`%APPDATA%\Claude\claude_desktop_config.json`

添加以下配置：

```json
{
  "mcpServers": {
    "spotify": {
      "command": "node",
      "args": ["/full/path/to/spotify-mcp-server/build/spotify-mcp-server.js"]
    }
  }
}
```

将 `/full/path/to/spotify-mcp-server` 替换为你的项目目录的实际路径。

### 7. 重启 Claude 桌面版

关闭并重新打开 Claude 桌面版以加载新配置。

## 使用方法

当你开始与 Claude 对话时，首先需要设置你的 Spotify 凭据：

1. 查看你的 `secrets.json` 文件以获取凭据
2. 使用 `set-spotify-credentials` 工具进行认证
3. 然后可以使用任何其他 Spotify 工具

## 示例提示

### 设置凭据

```
I want to connect to my Spotify account. Here are my credentials from secrets.json:

Tool: set-spotify-credentials
Parameters:
{
  "clientId": "your_client_id",
  "clientSecret": "your_client_secret",
  "accessToken": "your_access_token",
  "refreshToken": "your_refresh_token"
}
```

### 基本命令

检查你的账户：

```
Can you check who I'm logged in as on Spotify?

Tool: get-current-user
Parameters: {}
```

搜索曲目：

```
Search for songs by Weekend

Tool: search-tracks
Parameters:
{
  "query": "Taylor Swift",
  "limit": 5
}
```

希望这些步骤对你有所帮助！如果你有任何问题，请随时联系支持团队。

创建播放列表：

```
Create a new playlist called "My Pretty pretty girlfriend"

Tool: create-playlist
Parameters:
{
  "name": "My Pretty pretty girlfriend",
  "description": "For my girlfriend. Created with Claude and the Spotify MCP server"
}
```

### 多步骤任务

根据歌曲创建播放列表：

```
I want to create a workout playlist with energetic songs. First, search for some high-energy songs. Then create a playlist called "Workout Mix" and add those songs to it.
```

基于喜好获取推荐：

```
I like the song "Blinding Lights" by The Weeknd. Can you search for it, then find similar songs, and create a playlist with those recommendations?
```

## 故障排除

- **错误：没有可用的访问令牌**：您需要先使用 `set-spotify-credentials` 工具设置您的凭证
- **认证失败**：您的令牌可能已过期。请再次运行认证脚本以获取新的令牌
- **无效的凭证**：请仔细检查您是否使用了正确的客户端ID和客户端密钥

## 注意事项

- 服务器仅在内存中存储凭证
- 每次开始新的对话时，您都需要设置凭证
- 如果 Claude Desktop 重启，您需要再次设置凭证

**官方网站：** [https://github.com/hrishi0102/spotifyyy-mcp](https://github.com/hrishi0102/spotifyyy-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`entertainment and media`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`/full/path/to/spotify-mcp-server/build/spotify-mcp-server.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/hrishi0102-spotifyyy.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
