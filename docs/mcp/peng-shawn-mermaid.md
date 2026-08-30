---
title: "Mermaid-MCP 服务器"
description: "一个将Mermaid图表转换为PNG图像的模型上下文协议（MCP）服务器。"
---

# Mermaid-MCP 服务器

一个将Mermaid图表转换为PNG图像的模型上下文协议（MCP）服务器。

# Mermaid MCP 服务器

一个模型上下文协议 (MCP) 服务器，可以将 Mermaid 图表转换为 PNG 图像。此服务器允许 AI 助手和其他应用程序使用 Mermaid markdown 语法从文本描述生成可视化图表。

## 功能

- 将 Mermaid 图表代码转换为 PNG 图像
- 支持多种图表主题（默认、森林、暗色、中性）
- 可自定义背景颜色
- 使用 Puppeteer 进行高质量的无头浏览器渲染
- 实现 MCP 协议，以便与 AI 助手无缝集成
- 灵活的输出选项：直接返回图像或保存到磁盘
- 带有详细错误信息的错误处理

## 工作原理

服务器使用 Puppeteer 启动无头浏览器，将 Mermaid 图表渲染为 SVG，并截取渲染图表的屏幕截图。过程包括：

1. 启动无头浏览器实例
2. 创建包含 Mermaid 代码的 HTML 模板
3. 加载 Mermaid.js 库
4. 将图表渲染为 SVG
5. 将渲染的 SVG 截图作为 PNG
6. 直接返回图像或将图像保存到磁盘

## 构建

```bash
npx tsc
```

## 使用

### 与 Claude 桌面版一起使用

```json
"mcpServers": {
  "mermaid": {
    "command": "npx",
    "args": [
      npx @peng-shawn/mermaid-mcp-server
    ]
  }
}
```

### 与 Cursor 和 Cline 一起使用

```bash
env CONTENT_IMAGE_SUPPORTED=false npx @peng-shawn/mermaid-mcp-server
```

你可以在 `./diagrams` 下找到一系列 Mermaid 图表，这些图表是使用 Cursor 代理通过提示 "generate mermaid diagrams and save them in a separate diagrams folder explaining how renderMermaidPng work" 生成并保存的。

### 使用检查器运行

使用检查器运行服务器以进行测试和调试：

```bash
npx @modelcontextprotocol/inspector node dist/index.js
```

服务器将启动并在 stdio 上监听 MCP 协议消息。

了解更多关于检查器的信息，请访问[这里](https://modelcontextprotocol.io/docs/tools/inspector)。

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@peng-shawn/mermaid-mcp-server) 自动安装 Claude Desktop 的 Mermaid 图表生成器：

```bash
npx -y @smithery/cli install @peng-shawn/mermaid-mcp-server --client claude
```

### Docker 和 Smithery 环境

在 Docker 容器（包括通过 Smithery）中运行时，你可能需要处理 Chrome 依赖项：

1. 服务器现在默认尝试使用 Puppeteer 的捆绑浏览器
2. 如果遇到浏览器相关的错误，你有两个选择：

   **选项 1：在构建 Docker 镜像期间:**
   - 在安装 Puppeteer 时设置 `PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true`
   - 在你的 Docker 容器中安装 Chrome/Chromium
   - 在运行时设置 `PUPPETEER_EXECUTABLE_PATH` 指向 Chrome 安装路径

   **选项 2：使用 Puppeteer 的捆绑 Chrome:**
   - 确保你的 Docker 容器具有 Chrome 所需的依赖项
   - 不需要设置 `PUPPETEER_SKIP_CHROMIUM_DOWNLOAD`
   - 代码将自动使用捆绑浏览器

对于 Smithery 用户，最新版本应该无需额外配置即可工作。

## API

服务器公开了一个工具：

- `generate`: 将 Mermaid 图表代码转换为 PNG 图像
  - 参数：
    - `code`: 要渲染的 Mermaid 图表代码
    - `theme`: （可选）图表的主题。选项：`"default"`、`"forest"`、`"dark"`、`"neutral"`
    - `backgroundColor`: （可选）图表的背景颜色，例如 `'white'`、`'transparent'`、`'#F0F0F0'`
    - `name`: 生成文件的名称（当 `CONTENT_IMAGE_SUPPORTED=false` 时必需）
    - `folder`: 保存图像的绝对路径（当 `CONTENT_IMAGE_SUPPORTED=false` 时必需）

`generate` 工具的行为取决于 `CONTENT_IMAGE_SUPPORTED` 环境变量：

- 当 `CONTENT_IMAGE_SUPPORTED=true`（默认）：工具直接在响应中返回图像
- 当 `CONTENT_IMAGE_SUPPORTED=false`：工具将图像保存到指定文件夹，并返回文件路径

## 环境变量

- `CONTENT_IMAGE_SUPPORTED`: 控制图像是直接在响应中返回还是保存到磁盘
  - `true`（默认）：图像直接在响应中返回
  - `false`：图像保存到磁盘，需要 `name` 和 `folder` 参数

## 示例

### 基本用法

```javascript
// Generate a flowchart with default settings
{
  "code": "flowchart TD\n    A[Start] --> B{Is it?}\n    B -->|Yes| C[OK]\n    B -->|No| D[End]"
}
```

### 使用主题和背景颜色

```javascript
// Generate a sequence diagram with forest theme and light gray background
{
  "code": "sequenceDiagram\n    Alice->>John: Hello John, how are you?\n    John-->>Alice: Great!",
  "theme": "forest",
  "backgroundColor": "#F0F0F0"
}
```

### 保存到磁盘（当 `CONTENT_IMAGE_SUPPORTED=false` 时）

```javascript
// Generate a class diagram and save it to disk
{
  "code": "classDiagram\n    Class01 
  

## 许可证

MIT
```

**官方网站：** [https://github.com/peng-shawn/mermaid-mcp-server](https://github.com/peng-shawn/mermaid-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `image and video processing`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @peng-shawn/mermaid-mcp-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/peng-shawn-mermaid.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
