---
title: "BrowserBase云浏览器自动化"
description: "该服务器使用 Browserbase、Puppeteer 和 Stagehand 提供云浏览器自动化功能。此服务器使大型语言模型（LLMs）能够与网页交互、截屏以及在云浏览器环境中执行 JavaScript。"
---

# BrowserBase云浏览器自动化

该服务器使用 Browserbase、Puppeteer 和 Stagehand 提供云浏览器自动化功能。此服务器使大型语言模型（LLMs）能够与网页交互、截屏以及在云浏览器环境中执行 JavaScript。

# Browserbase MCP 服务器

## 开始使用

1. 运行 `npm install` 安装必要的依赖项，然后运行 `npm run build` 以获取 `dist/index.js`。

2. 设置你的 Claude Desktop 配置以使用该服务器。  

```json
{
  "mcpServers": {
    "browserbase": {
      "command": "node",
      "args": ["path/to/mcp-server-browserbase/browserbase/dist/index.js"],
      "env": {
        "BROWSERBASE_API_KEY": "",
        "BROWSERBASE_PROJECT_ID": ""
      }
    }
  }
}
```

3. 重启你的 Claude Desktop 应用程序，你应该会看到点击 🔨 图标后可用的工具。

4. 开始使用这些工具！下面是一张 Claude 关闭浏览器会话的图片。

   alt="demo" width="600"/>

## 工具

### Browserbase API

- **browserbase_create_session**

  - 使用 Browserbase 创建一个新的云浏览器会话
  - 不需要输入

- **browserbase_navigate**

  - 在浏览器中导航到任何 URL
  - 输入: `url` (字符串)

- **browserbase_screenshot**

  - 捕获整个页面或特定元素的截图
  - 输入:
    - `name` (字符串, 必需): 截图名称
    - `selector` (字符串, 可选): 要截取的元素的 CSS 选择器
    - `width` (数字, 可选, 默认: 800): 截图宽度
    - `height` (数字, 可选, 默认: 600): 截图高度

- **browserbase_click**

  - 点击页面上的元素
  - 输入: `selector` (字符串): 要点击的元素的 CSS 选择器

- **browserbase_fill**

  - 填写输入字段
  - 输入:
    - `selector` (字符串): 输入字段的 CSS 选择器
    - `value` (字符串): 要填写的值

- **browserbase_evaluate**

  - 在浏览器控制台中执行 JavaScript
  - 输入: `script` (字符串): 要执行的 JavaScript 代码

- **browserbase_get_content**

  - 从当前页面提取所有内容
  - 输入: `selector` (字符串, 可选): 从特定元素获取内容的 CSS 选择器

- **browserbase_parallel_sessions**
  - 创建多个浏览器会话并导航到不同的 URL
  - 输入: `sessions` (数组): 包含以下对象的数组：
    - `url` (字符串): 要导航到的 URL
    - `id` (字符串): 会话标识符

### 资源

该服务器提供了两种类型的资源访问：

1. **控制台日志** (`console://logs`)

   - 文本格式的浏览器控制台输出
   - 包括来自浏览器的所有控制台消息

2. **截图** (`screenshot://`)
   - 捕获的 PNG 格式的截图
   - 可通过捕获时指定的截图名称访问

## 主要功能

- 云端浏览器自动化
- 网页数据提取
- 控制台日志监控
- 截图功能
- JavaScript 执行
- 基本的网页交互（导航、点击、表单填写）

## 许可证

此 MCP 服务器根据 MIT 许可证许可。这意味着你可以在遵守 MIT 许可证条款和条件的前提下自由使用、修改和分发该软件。有关更多详细信息，请参见项目存储库中的 LICENSE 文件。

**官方网站：** [https://github.com/browserbase/mcp-server-browserbase/tree/main/browserbase](https://github.com/browserbase/mcp-server-browserbase/tree/main/browserbase)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`browser`
- 标签：`browser automation`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`path/to/mcp-server-browserbase/browserbase/dist/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/browserbase-browserbase.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
