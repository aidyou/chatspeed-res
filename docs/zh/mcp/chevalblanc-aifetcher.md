---
title: "MCP-网页爬虫"
description: "| | | | | | | MCP 服务器用于通过 Playwright 无头浏览器抓取网页内容。 🌟 推荐：- 强大的 Ollama AI 模型管理器。-"
---

# MCP-网页爬虫

| | | | | | | MCP 服务器用于通过 Playwright 无头浏览器抓取网页内容。 🌟 推荐：- 强大的 Ollama AI 模型管理器。-

[中文](https://www.readme-i18n.com/jae-jae/fetcher-mcp?lang=zh) |
[德语](https://www.readme-i18n.com/jae-jae/fetcher-mcp?lang=de) | 
[西班牙语](https://www.readme-i18n.com/jae-jae/fetcher-mcp?lang=es) | 
[法语](https://www.readme-i18n.com/jae-jae/fetcher-mcp?lang=fr) | 
[日语](https://www.readme-i18n.com/jae-jae/fetcher-mcp?lang=ja) | 
[韩语](https://www.readme-i18n.com/jae-jae/fetcher-mcp?lang=ko) | 
[葡萄牙语](https://www.readme-i18n.com/jae-jae/fetcher-mcp?lang=pt) | 
[俄语](https://www.readme-i18n.com/jae-jae/fetcher-mcp?lang=ru) 

# Fetcher MCP

使用无头浏览器 Playwright 获取网页内容的 MCP 服务器。

> 🌟 **推荐**: [OllaMan](https://ollaman.com/) - 强大的 Ollama AI 模型管理器。

## 优势

- **JavaScript 支持**：与传统的网页抓取工具不同，Fetcher MCP 使用 Playwright 执行 JavaScript，能够处理动态网页内容和现代 Web 应用程序。
- **智能内容提取**：内置的 Readability 算法自动从网页中提取主要内容，去除广告、导航和其他非必要元素。
- **灵活的输出格式**：支持 HTML 和 Markdown 输出格式，易于与各种下游应用集成。
- **并行处理**：`fetch_urls` 工具支持并发获取多个 URL，显著提高批量操作的效率。
- **资源优化**：自动阻止不必要的资源（如图片、样式表、字体、媒体）以减少带宽使用并提高性能。
- **强大的错误处理**：全面的错误处理和日志记录确保在处理问题网页时也能可靠运行。
- **可配置参数**：对超时、内容提取和输出格式进行细粒度控制，以适应不同的使用场景。

## 快速开始

直接使用 npx 运行：

```bash

npx -y fetcher-mcp

```
首次设置 - 通过在终端中运行以下命令安装所需的浏览器：

```bash

npx playwright install chromium

```
### HTTP 和 SSE 传输

使用 `--transport=http` 参数同时启动 Streamable HTTP 端点和 SSE 端点服务：

```bash

npx -y fetcher-mcp --log --transport=http --host=0.0.0.0 --port=3000

```
启动后，服务器提供以下端点：

- `/mcp` - Streamable HTTP 端点（现代 MCP 协议）
- `/sse` - SSE 端点（旧版 MCP 协议）

客户端可以根据需要选择连接方式。

### 调试模式

使用 `--debug` 选项运行以显示浏览器窗口进行调试：

```bash

npx -y fetcher-mcp --debug

```
## 配置 MCP

在 Claude Desktop 中配置此 MCP 服务器：

在 MacOS 上：`~/Library/Application Support/Claude/claude_desktop_config.json`

在 Windows 上：`%APPDATA%/Claude/claude_desktop_config.json`

```json

{

  "mcpServers": {

    "fetcher": {

      "command": "npx",

      "args": ["-y", "fetcher-mcp"]

    }

  }

}

```
## Docker 部署

### 使用 Docker 运行

```bash

docker run -p 3000:3000 ghcr.io/jae-jae/fetcher-mcp:latest

```
### 使用 Docker Compose 部署

创建一个 `docker-compose.yml` 文件：

```yaml

version: "3.8"

services:

  fetcher-mcp:

    image: ghcr.io/jae-jae/fetcher-mcp:latest

    container_name: fetcher-mcp

    restart: unless-stopped

    ports:

      - "3000:3000"

    environment:

      - NODE_ENV=production

    # Using host network mode on Linux hosts can improve browser access efficiency

    # network_mode: "host"

    volumes:

      # For Playwright, may need to share certain system paths

      - /tmp:/tmp

    # Health check

    healthcheck:

      test: ["CMD", "wget", "--spider", "-q", "http://localhost:3000"]

      interval: 30s

      timeout: 10s

      retries: 3

```
然后运行：

```bash

docker-compose up -d

```
## 功能

- `fetch_url` - 从指定的 URL 获取网页内容

  - 使用 Playwright 无头浏览器解析 JavaScript
  - 支持智能提取主要内容并转换为 Markdown
  - 支持以下参数：
    - `url`：要获取的网页的 URL（必填参数）
    - `timeout`：页面加载超时时间（毫秒），默认为 30000（30 秒）
    - `waitUntil`：指定导航何时完成，选项：'load', 'domcontentloaded', 'networkidle', 'commit'，默认为 'load'
    - `extractContent`：是否智能提取主要内容，默认为 true
    - `maxLength`：返回内容的最大长度（字符数），默认无限制
    - `returnHtml`：是否返回 HTML 内容而不是 Markdown，默认为 false
    - `waitForNavigation`：是否在初始页面加载后等待额外的导航（对于具有反机器人验证的站点有用），默认为 false
    - `navigationTimeout`：等待额外导航的最大时间（毫秒），默认为 10000（10 秒）- `disableMedia`: 是否禁用媒体资源（图片、样式表、字体、媒体），默认为 true
- `debug`: 是否启用调试模式（显示浏览器窗口），如果指定了该参数，则会覆盖命令行中的 --debug 标志

- `fetch_urls` - 并行批量从多个 URL 检索网页内容
  - 使用多标签页并行检索以提高性能
  - 返回合并的结果，并在不同网页之间有清晰的分隔
  - 支持以下参数：
    - `urls`: 要检索的 URL 数组（必需参数）
    - 其他参数与 `fetch_url` 相同

## 提示

### 处理特殊网站场景

#### 应对反爬虫机制

- **等待完全加载**: 对于使用验证码、重定向或其他验证机制的网站，在提示中包含：

```

  Please wait for the page to fully load

```
  这将使用 `waitForNavigation: true` 参数。

- **增加超时时间**: 对于加载缓慢的网站：
```
  Please set the page loading timeout to 60 seconds
```
  这会相应地调整 `timeout` 和 `navigationTimeout` 参数。

#### 内容检索调整

- **保留原始 HTML 结构**: 当内容提取可能失败时：

```

  Please preserve the original HTML content

```
  设置 `extractContent: false` 和 `returnHtml: true`。

- **获取完整页面内容**: 当提取的内容过于有限时：

```

  Please fetch the complete webpage content instead of just the main content

```
  设置 `extractContent: false`。

- **以 HTML 格式返回内容**: 当需要 HTML 格式而不是默认的 Markdown 格式时：
```
  Please return the content in HTML format
```
  设置 `returnHtml: true`。

### 调试和身份验证

#### 启用调试模式

- **动态启用调试**: 在特定的检索操作期间显示浏览器窗口：
```
  Please enable debug mode for this fetch operation
```
  即使服务器启动时没有使用 `--debug` 标志，这也会设置 `debug: true`。

#### 使用自定义 Cookie 进行身份验证

- **手动登录**: 使用自己的凭据登录：

```

  Please run in debug mode so I can manually log in to the website

```
  设置 `debug: true` 或使用 `--debug` 标志，保持浏览器窗口打开以便手动登录。

- **与调试浏览器交互**: 当启用调试模式时：
  1. 浏览器窗口保持打开状态
  2. 可以使用您的凭据手动登录网站
  3. 登录完成后，将以经过身份验证的会话获取内容

- **为特定请求启用调试**: 即使服务器已经在运行，也可以为特定请求启用调试模式：
```
  Please enable debug mode for this authentication step
```
  仅为该特定请求设置 `debug: true`，打开浏览器窗口进行手动登录。

## 开发

### 安装依赖项

```bash

npm install

```
### 安装 Playwright 浏览器

安装 Playwright 所需的浏览器：

```bash

npm run install-browser

```
### 构建服务器

```bash

npm run build

```
## 调试

使用 MCP Inspector 进行调试：

```bash

npm run inspector

```
您还可以启用可见浏览器模式进行调试：

```bash

node build/index.js --debug

```
## 相关项目

- [g-search-mcp](https://github.com/jae-jae/g-search-mcp): 一个强大的 MCP 服务器，用于 Google 搜索，支持同时使用多个关键词进行并行搜索。非常适合批量搜索操作和数据收集。

## 许可证

根据 [MIT 许可证](https://choosealicense.com/licenses/mit/) 发布

[](https://dartnode.com "由 DartNode 提供支持 - 为开源提供免费 VPS")

**官方网站：** [https://github.com/taurusduan/fetcher-mcp](https://github.com/taurusduan/fetcher-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`browser`
- 标签：`browser automation`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y fetcher-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/chevalblanc-aifetcher.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
