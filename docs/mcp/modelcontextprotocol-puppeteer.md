---
title: "Puppeteer浏览器自动化"
description: "一个使用Puppeteer提供浏览器自动化功能的Model Context Protocol服务器。此服务器使LLM能够与网页交互、截屏以及在真实的浏览器环境中执行JavaScript。"
---

# Puppeteer浏览器自动化

一个使用Puppeteer提供浏览器自动化功能的Model Context Protocol服务器。此服务器使LLM能够与网页交互、截屏以及在真实的浏览器环境中执行JavaScript。

# Puppeteer

一个使用 Puppeteer 提供浏览器自动化功能的 Model Context Protocol 服务器。该服务器使 LLMs 能够与网页交互、截屏以及在真实的浏览器环境中执行 JavaScript。

## 组件

### 工具

- **puppeteer_navigate**
  - 在浏览器中导航到任何 URL
  - 输入：
    - `url` (字符串，必填)：要导航到的 URL
    - `launchOptions` (对象，可选)：PuppeteerJS 的 LaunchOptions。默认为 null。如果更改且不为 null，则会重启浏览器。示例：`{ headless: true, args: ['--user-data-dir="C:/Data"'] }`
    - `allowDangerous` (布尔值，可选)：允许降低安全性的危险 LaunchOptions。当设置为 false 时，像 `--no-sandbox`、`--disable-web-security` 这样的危险参数将抛出错误。默认为 false。

- **puppeteer_screenshot**
  - 捕获整个页面或特定元素的屏幕截图
  - 输入：
    - `name` (字符串，必填)：截图的名称
    - `selector` (字符串，可选)：要截图的元素的 CSS 选择器
    - `width` (数字，可选，默认为 800)：截图宽度
    - `height` (数字，可选，默认为 600)：截图高度

- **puppeteer_click**
  - 点击页面上的元素
  - 输入：`selector` (字符串)：要点击的元素的 CSS 选择器

- **puppeteer_hover**
  - 将鼠标悬停在页面上的元素上
  - 输入：`selector` (字符串)：要悬停的元素的 CSS 选择器

- **puppeteer_fill**
  - 填写输入字段
  - 输入：
    - `selector` (字符串)：输入字段的 CSS 选择器
    - `value` (字符串)：要填写的值

- **puppeteer_select**
  - 选择带有 SELECT 标签的元素
  - 输入：
    - `selector` (字符串)：要选择的元素的 CSS 选择器
    - `value` (字符串)：要选择的值

- **puppeteer_evaluate**
  - 在浏览器控制台中执行 JavaScript
  - 输入：`script` (字符串)：要执行的 JavaScript 代码

### 资源

服务器提供了访问两种类型的资源：

1. **控制台日志** (`console://logs`)
   - 以文本格式输出的浏览器控制台内容
   - 包括来自浏览器的所有控制台消息

2. **屏幕截图** (`screenshot://`)
   - 捕获的屏幕截图的 PNG 图像
   - 可通过捕获时指定的截图名称访问

## 主要特性

- 浏览器自动化
- 控制台日志监控
- 截图功能
- JavaScript 执行
- 基本的网页交互（导航、点击、表单填写）
- 可自定义的 Puppeteer 启动选项

## 使用 Puppeteer 服务器的配置
以下是使用 Puppeter 服务器的 Claude Desktop 配置：

### Docker

**注意** Docker 实现将使用无头 Chromium，而 NPX 版本将打开一个浏览器窗口。

```json
{
  "mcpServers": {
    "puppeteer": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "--init", "-e", "DOCKER_CONTAINER=true", "mcp/puppeteer"]
    }
  }
}
```

### NPX

```json
{
  "mcpServers": {
    "puppeteer": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-puppeteer"]
    }
  }
}
```

### 启动选项

你可以通过以下两种方式自定义 Puppeteer 的浏览器行为：

1. **环境变量**: 在MCP配置的`env`参数中设置`PUPPETEER_LAUNCH_OPTIONS`，其值为JSON编码的字符串：

```json
    {
      "mcpServers": {
        "mcp-puppeteer": {
          "command": "npx",
          "args": ["-y", "@modelcontextprotocol/server-puppeteer"],
          "env": {
            "PUPPETEER_LAUNCH_OPTIONS": "{ \"headless\": false, \"executablePath\": \"C:/Program Files/Google/Chrome/Application/chrome.exe\", \"args\": [] }",
            "ALLOW_DANGEROUS": "true"
          }
        }
      }
    }
```

2. **工具调用参数**: 向`puppeteer_navigate`工具传递`launchOptions`和`allowDangerous`参数：

```json
   {
     "url": "https://example.com",
     "launchOptions": {
       "headless": false,
       "defaultViewport": {"width": 1280, "height": 720}
     }
   }
```

## 构建

Docker构建：

```bash
docker build -t mcp/puppeteer -f src/puppeteer/Dockerfile .
```

## 许可证

此MCP服务器根据MIT许可证授权。这意味着您可以在遵守MIT许可证条款和条件的前提下自由使用、修改和分发该软件。更多详情，请参阅项目仓库中的LICENSE文件。

**官方网站：** [https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`browser`
- 标签：`browser automation`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @modelcontextprotocol/server-puppeteer`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/modelcontextprotocol-puppeteer.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
