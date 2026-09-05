---
title: "推特MCP"
description: "一个MCP服务器，它使克劳德能够与推特互动，从而实现发布推文和搜索推特内容的功能。"
---

# 推特MCP

一个MCP服务器，它使克劳德能够与推特互动，从而实现发布推文和搜索推特内容的功能。

# Twitter MCP 服务器

[Smithery](https://smithery.ai/server/@enescinar/twitter-mcp)

此MCP服务器允许客户端与Twitter进行交互，支持发布推文和搜索Twitter。

  

## 快速开始

1. 创建一个Twitter开发者账户，并从[Twitter开发者门户](https://developer.twitter.com/en/portal/dashboard)获取您的API密钥。

2. 将以下配置添加到您的Claude Desktop配置文件中：

**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`  
**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "twitter-mcp": {
      "command": "npx",
      "args": ["-y", "@enescinar/twitter-mcp"],
      "env": {
        "API_KEY": "your_api_key_here",
        "API_SECRET_KEY": "your_api_secret_key_here",
        "ACCESS_TOKEN": "your_access_token_here",
        "ACCESS_TOKEN_SECRET": "your_access_token_secret_here"
      }
    }
  }
}
```

3. 重启Claude Desktop

就这样！Claude现在可以通过两个工具与Twitter进行交互：

- `post_tweet`: 发布一条新推文
- `search_tweets`: 搜索推文

## 使用示例

尝试向Claude提问：
- "你能发一条推文说'Hello from Claude!'吗？"
- "你能搜索关于Claude AI的推文吗？"

## 故障排除

日志可以在以下位置找到：
- **Windows**: `%APPDATA%\Claude\logs\mcp-server-twitter.log`
- **macOS**: `~/Library/Logs/Claude/mcp-server-twitter.log`

## 开发

如果您想贡献代码或从源码运行：

1. 克隆仓库：
```bash
git clone https://github.com/EnesCinr/twitter-mcp.git
cd twitter-mcp
```

2. 安装依赖项：
```bash
npm install
```

3. 构建：
```bash
npm run build
```

4. 运行：
```bash
npm start
```

## 许可证

MIT

**官方网站：** [https://github.com/EnesCinr/twitter-mcp](https://github.com/EnesCinr/twitter-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`communication`
- 标签：`social media`, `communication`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @enescinar/twitter-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/enescinr-twitter.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
