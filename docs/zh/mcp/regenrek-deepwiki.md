---
title: "Github的维基百科DeepWiKi"
description: "📖 MCP 服务器用于获取 deepwiki.com 的最新知识，并在 Cursor 和其他代码编辑器中使用"
---

# Github的维基百科DeepWiKi

📖 MCP 服务器用于获取 deepwiki.com 的最新知识，并在 Cursor 和其他代码编辑器中使用

# Deepwiki MCP 服务器

这是一个**非官方的 Deepwiki MCP 服务器**

它通过 MCP 接收一个 Deepwiki URL，爬取所有相关页面，将其转换为 Markdown 格式，并返回一个文档或按页面列出的列表。

## 功能

- 🔒 **域名安全**：仅处理来自 deepwiki.org 的 URL
- 🧹 **HTML 清理**：移除头部、尾部、导航、脚本和广告
- 🔗 **链接重写**：调整链接以在 Markdown 中工作
- 📄 **多种输出格式**：获取一个文档或结构化的页面
- 🚀 **性能**：快速爬取，可调节并发和深度
- **NLP**：仅用于搜索库名称

## 使用方法

您可以使用的提示：

```
deepwiki fetch how can i use gpt-image-1 with "vercel ai" sdk

deepwiki fetch how can i create new blocks in shadcn?

deepwiki fetch i want to understand how X works
```

获取完整文档（默认）

```
use deepwiki https://deepwiki.org/shadcn-ui/ui
use deepwiki multiple pages https://deepwiki.org/shadcn-ui/ui
```

单个页面

```
use deepwiki fetch single page https://deepwiki.org/tailwindlabs/tailwindcss/2.2-theme-system
```

使用简短形式获取

```
use deepwiki fetch tailwindlabs/tailwindcss

deepwiki fetch library

deepwiki fetch url
deepwiki fetch /

deepwiki multiple pages ...
deepwiki single page url ...
```

## 光标

将以下内容添加到 `.cursor/mcp.json` 文件中。

```json
{
  "mcpServers": {
    "mcp-deepwiki": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-deepwiki@latest"
      ]
    }
  }
}
```

### MCP 工具集成

该包注册了一个名为 `deepwiki_fetch` 的工具，您可以在任何与 MCP 兼容的客户端中使用它：

```json
{
  "action": "deepwiki_fetch",
  "params": {
    "url": "https://deepwiki.org/user/repo",
    "mode": "aggregate",
    "maxDepth": "1"
  }
}
```

#### 参数

- `url`（必需）：Deepwiki 仓库的起始 URL
- `mode`（可选）：输出模式，可以是 "aggregate" 表示单个 Markdown 文档（默认），或者 "pages" 表示结构化的页面数据
- `maxDepth`（可选）：要爬取的最大页面深度（默认：10）

### 响应格式

#### 成功响应（聚合模式）

```json
{
  "status": "ok",
  "data": "# 页面标题

页面内容...

---

# 另一个页面

更多内容...",
  "totalPages": 5,
  "totalBytes": 25000,
  "elapsedMs": 1200
}
```

#### 成功响应（页面模式）

```json
{
  "status": "ok",
  "data": [
    {
      "path": "index",
      "markdown": "# 主页

欢迎来到仓库。"
    },
    {
      "path": "section/page1",
      "markdown": "# 第一页

这是第一页的内容。"
    }
  ],
  "totalPages": 2,
  "totalBytes": 12000,
  "elapsedMs": 800
}
```

#### 错误响应

```json
{
  "status": "error",
  "code": "DOMAIN_NOT_ALLOWED",
  "message": "仅允许 deepwiki.org 域名"
}
```

#### 部分成功响应

```json
{
  "status": "partial",
  "data": "# 页面标题

页面内容...",
  "errors": [
    {
      "url": "https://deepwiki.org/user/repo/page2",
      "reason": "HTTP 错误: 404"
    }
  ],
  "totalPages": 1,
  "totalBytes": 5000,
  "elapsedMs": 950
}
```

### 进度事件

在使用工具时，您会在爬取过程中收到进度事件：

Fetched https://deepwiki.org/user/repo: 12500 bytes in 450ms (status: 200)
Fetched https://deepwiki.org/user/repo/page1: 8750 bytes in 320ms (status: 200)
Fetched https://deepwiki.org/user/repo/page2: 6200 bytes in 280ms (status: 200)

## 本地开发 - 安装

### 本地使用

```json
{
  "mcpServers": {
    "mcp-deepwiki": {
      "command": "node",
      "args": [
        "./bin/cli.mjs"
      ]
    }
  }
}
```

### 从源代码安装

```bash
# 克隆仓库
git clone https://github.com/regenrek/mcp-deepwiki.git
cd mcp-deepwiki

# 安装依赖
npm install

# 构建包
npm run build
```

#### 直接 API 调用

对于 HTTP 传输，您可以直接进行 API 调用：

```bash
curl -X POST http://localhost:3000/mcp 
-H "Content-Type: application/json" 
-d '{
"id": "req-1",
"action": "deepwiki_fetch",
"params": {
"url": "https://deepwiki.org/user/repo",
"mode": "aggregate"
}
}'
```

## 配置

### 环境变量

- `DEEPWIKI_MAX_CONCURRENCY`: 最大并发请求数 (默认: 5)
- `DEEPWIKI_REQUEST_TIMEOUT`: 请求超时时间（毫秒）(默认: 30000)
- `DEEPWIKI_MAX_RETRIES`: 失败请求的最大重试次数 (默认: 3)
- `DEEPWIKI_RETRY_DELAY`: 重试退避的基本延迟时间（毫秒）(默认: 250)

要配置这些环境变量，请在项目根目录下创建一个 `.env` 文件：

DEEPWIKI_MAX_CONCURRENCY=10
DEEPWIKI_REQUEST_TIMEOUT=60000
DEEPWIKI_MAX_RETRIES=5
DEEPWIKI_RETRY_DELAY=500

## Docker 部署（未测试）

构建并运行 Docker 镜像：

```bash
# 构建镜像
docker build -t mcp-deepwiki .

# 使用 stdio 传输方式运行（适用于开发）
docker run -it --rm mcp-deepwiki

# 使用 HTTP 传输方式运行（适用于生产）
docker run -d -p 3000:3000 mcp-deepwiki --http --port 3000

# 使用环境变量运行
docker run -d -p 3000:3000 
-e DEEPWIKI_MAX_CONCURRENCY=10 
-e DEEPWIKI_REQUEST_TIMEOUT=60000 
mcp-deepwiki --http --port 3000
```

## 开发

```bash
# 安装依赖
pnpm install

# 使用 stdio 方式以开发模式运行
pnpm run dev-stdio

# 运行测试
pnpm test

# 运行代码检查
pnpm run lint

# 构建包
pnpm run build
```

## 故障排除

### 常见问题

1. **权限被拒绝**：如果在运行 CLI 时遇到 EACCES 错误，请确保二进制文件是可执行的：
   bash
   chmod +x ./node_modules/.bin/mcp-deepwiki

2. **连接被拒绝**：确保端口可用且未被防火墙阻止：
   bash
   # 检查端口是否正在使用
   lsof -i :3000

3. **超时错误**：对于大型仓库，考虑增加超时时间和并发数：

   DEEPWIKI_REQUEST_TIMEOUT=60000 DEEPWIKI_MAX_CONCURRENCY=10 npx mcp-deepwiki

## 贡献

我们欢迎贡献！详情请参阅 [CONTRIBUTING.md](https://github.com/regenrek/deepwiki-mcp/blob/HEAD/CONTRIBUTING.md)。

## 许可证

MIT

## 链接

- X/Twitter: [@kregenrek](https://x.com/kregenrek)
- Bluesky: [@kevinkern.dev](https://bsky.app/profile/kevinkern.dev)

## 课程

- 学习 Cursor AI: [Ultimate Cursor Course](https://www.instructa.ai/en/cursor-ai)
- 学习用 AI 构建软件: [instructa.ai](https://www.instructa.ai)

## 查看我的其他项目：

* [AI Prompts](https://github.com/instructa/ai-prompts/blob/main/README.md) - 为 Cursor AI、Cline、Windsurf 和 Github
  Copilot 策划的 AI 提示
* [codefetch](https://github.com/regenrek/codefetch) - 通过一个简单的终端命令将代码转换为 Markdown 格式，以便于 LLMs 使用
* [aidex](https://github.com/regenrek/aidex) - 一个 CLI 工具，提供关于 AI 语言模型的详细信息，帮助开发者选择适合他们需求的模型。

**官方网站：** [https://github.com/regenrek/deepwiki-mcp](https://github.com/regenrek/deepwiki-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`, `memory`, `data`
- 标签：`search`, `knowledge and memory`, `research and data`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y mcp-deepwiki@latest`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/regenrek-deepwiki.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
