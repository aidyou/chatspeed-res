---
title: "MCP Browser 控制器"
description: "一个MCP服务器，它通过自然语言命令使AI助手能够控制网络浏览器，允许它们通过SSE传输浏览网站和提取信息。"
---

# MCP Browser 控制器

一个MCP服务器，它通过自然语言命令使AI助手能够控制网络浏览器，允许它们通过SSE传输浏览网站和提取信息。

# ➡️ browser-use mcp server

[browser-use](https://github.com/browser-use/browser-use) MCP Server with SSE transport

### 要求

- uv

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 快速开始

```
uv sync
uv pip install playwright
uv run playwright install --with-deps --no-shell chromium
uv run server --port 8000
```

- .env 文件需要以下内容：

```
OPENAI_API_KEY=[your api key]
CHROME_PATH=[only change this if you have a custom chrome build]
PATIENT=false # Set to true if you want api calls to wait for tasks to complete (default is false)
```

- 我们将增加对其他 LLM 提供商的支持，以支持 browser-use（例如 Claude, Grok, Bedrock 等）

在构建 Docker 镜像时，您可以使用 Docker 秘钥来设置 VNC 密码：

```
# With Docker secrets (recommended for production)
echo "your-secure-password" > vnc_password.txt
docker run -v $(pwd)/vnc_password.txt:/run/secrets/vnc_password your-image-name

# Or during development with the default password
docker build .
```

### 工具

- [x] SSE 传输
- [x] browser_use - 使用 URL 和操作启动浏览器任务
- [x] browser_get_result - 获取异步浏览器任务的结果
- [x] VNC 服务器 - 将容器化的浏览器流式传输到客户端

### VNC

Dockerfile 中包含一个默认密码为 `browser-use` 的 VNC 服务器。连接方法如下：

```
docker build -t  browser-use-mcp-server .
docker run --rm -p8000:8000 -p5900:5900 browser-use-mcp-server
git clone https://github.com/novnc/noVNC
cd noVNC
./utils/novnc_proxy --vnc localhost:5900
```

### 支持的客户端

- cursor.ai
- claude desktop
- claude code
- windsurf ([windsurf](https://codeium.com/windsurf) 目前还不支持 SSE)

### 使用方法

运行服务器后，在您的客户端界面中添加 [http://localhost:8000/sse](http://localhost:8000/sse)，或者在 mcp.json 文件中添加：

```json
{
  "mcpServers": {
    "browser-use-mcp-server": {
      "url": "http://localhost:8000/sse"
    }
  }
}
```

#### cursor

- `./.cursor/mcp.json`

#### windsurf

- `~/.codeium/windsurf/mcp_config.json`

#### claude

- `~/Library/Application Support/Claude/claude_desktop_config.json`
- `%APPDATA%\Claude\claude_desktop_config.json`

然后尝试向您的 LLM 提出以下请求：

`打开 https://news.ycombinator.com 并返回排名最高的文章`

### 帮助

对于问题或兴趣，请联系 @ [https://cobrowser.xyz](https://cobrowser.xyz)

# 星标

**官方网站：** [https://github.com/co-browser/browser-use-mcp-server](https://github.com/co-browser/browser-use-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`browser`
- 标签：`browser automation`, `chinese`

## MCP 配置

- 传输方式：`http`
- 启动命令：``
- 参数：无

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/co-browser-browser-use.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
