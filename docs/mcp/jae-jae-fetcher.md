---
title: "MCP抓取器"
description: "一个专用的MCP服务器，使用Playwright无头浏览器获取网页内容，具备智能内容提取和批量URL处理的能力。"
---

# MCP抓取器

一个专用的MCP服务器，使用Playwright无头浏览器获取网页内容，具备智能内容提取和批量URL处理的能力。

# Fetcher MCP

使用无头浏览器 Playwright 抓取网页内容的 MCP 服务器。

## 优势

- **JavaScript 支持**：与传统的网络爬虫不同，Fetcher MCP 使用 Playwright 执行 JavaScript，能够处理动态网页内容和现代 Web 应用程序。
- **智能内容提取**：内置的 Readability 算法可以自动从网页中提取主要内容，去除广告、导航和其他非必要元素。
- **灵活的输出格式**：支持 HTML 和 Markdown 输出格式，易于与各种下游应用集成。
- **并行处理**：`fetch_urls` 工具可以并发抓取多个 URL，显著提高批量操作的效率。
- **资源优化**：自动阻止不必要的资源（如图片、样式表、字体、媒体）以减少带宽使用并提高性能。
- **强大的错误处理**：全面的错误处理和日志记录确保即使在处理有问题的网页时也能可靠运行。
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

## 功能

注意：原文档中的代码块 (`#0`, `#1`, `#2`, `#3`) 似乎缺少具体内容。请根据实际需要填充这些部分。

- `fetch_url` - 从指定的 URL 检索网页内容
  - 使用 Playwright 无头浏览器解析 JavaScript
  - 支持智能提取主要内容并转换为 Markdown
  - 支持以下参数：
    - `url`: 要获取的网页的 URL（必需参数）
    - `timeout`: 页面加载超时时间（以毫秒为单位），默认是 30000（30 秒）
    - `waitUntil`: 指定导航何时被视为完成，选项：'load', 'domcontentloaded', 'networkidle', 'commit'，默认是 'load'
    - `extractContent`: 是否智能提取主要内容，默认为 true
    - `maxLength`: 返回内容的最大长度（以字符为单位），默认没有限制
    - `returnHtml`: 是否返回 HTML 内容而不是 Markdown，默认为 false
    - `waitForNavigation`: 在初始页面加载后是否等待额外的导航（对于具有反爬虫验证的网站很有用），默认为 false
    - `navigationTimeout`: 等待额外导航的最大时间（以毫秒为单位），默认是 10000（10 秒）
    - `disableMedia`: 是否禁用媒体资源（图片、样式表、字体、媒体），默认为 true
    - `debug`: 是否启用调试模式（显示浏览器窗口），如果指定了此选项，则会覆盖命令行中的 --debug 标志

- `fetch_urls` - 并行批量检索多个 URL 的网页内容
  - 使用多标签页并行获取以提高性能
  - 返回合并的结果，并在网页之间有清晰的分隔
  - 支持以下参数：
    - `urls`: 要获取的 URL 数组（必需参数）
    - 其他参数与 `fetch_url` 相同

## 提示

### 处理特殊网站场景

#### 应对反爬虫机制
- **等待完全加载**：对于使用验证码、重定向或其他验证机制的网站，在提示中包含：
```
  请等待页面完全加载
```
  这将使用 `waitForNavigation: true` 参数。

- **增加超时时间**：对于加载缓慢的网站：
```
  请将页面加载超时时间设置为 60 秒
```
  这将相应地调整 `timeout` 和 `navigationTimeout` 参数。

#### 内容检索调整
- **保留原始 HTML 结构**：当内容提取可能失败时：
```
  请保留原始 HTML 内容
```
  设置 `extractContent: false` 和 `returnHtml: true`。

- **获取完整页面内容**：当提取的内容太有限时：
```
  请获取完整的网页内容而不是仅主要内容
```
  设置 `extractContent: false`。

- **以 HTML 格式返回内容**：当需要 HTML 格式而不是默认的 Markdown 格式时：
```
  请以 HTML 格式返回内容
```
  设置 `returnHtml: true`。

### 调试和身份验证

#### 启用调试模式

- **动态调试激活**：要在特定的抓取操作期间显示浏览器窗口：
```
  请为此抓取操作启用调试模式
```
  即使服务器启动时没有使用 `--debug` 标志，这也会将 `debug: true` 设置为真。

#### 使用自定义 Cookie 进行身份验证
- **手动登录**：要使用您自己的凭据登录：
```
  请以调试模式运行，以便我可以手动登录网站
```
  将 `debug: true` 设置为真或使用 `--debug` 标志，保持浏览器窗口打开以进行手动登录。

- **与调试浏览器交互**：当启用调试模式时：
  1. 浏览器窗口保持打开状态
  2. 您可以使用您的凭据手动登录网站
  3. 登录完成后，将以您的已认证会话获取内容

- **为特定请求启用调试**：即使服务器已经在运行，您也可以为特定请求启用调试模式：
```
  请为此身份验证步骤启用调试模式
```
  仅为该特定请求设置 `debug: true`，打开浏览器窗口进行手动登录。

## 开发

### 安装依赖

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

您还可以启用可见浏览器模式来进行调试：

```bash
node build/index.js --debug
```

## 相关项目

- [g-search-mcp](https://github.com/jae-jae/g-search-mcp)：一个强大的用于 Google 搜索的 MCP 服务器，支持同时使用多个关键词进行并行搜索。非常适合批量搜索操作和数据收集。

## 许可证

本项目根据 [MIT License](https://choosealicense.com/licenses/mit/) 许可。

**官方网站：** [https://github.com/jae-jae/fetcher-mcp](https://github.com/jae-jae/fetcher-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`, `browser`
- 标签：`browser automation`, `search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y fetcher-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/jae-jae-fetcher.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
