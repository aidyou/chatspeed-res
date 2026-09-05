---
title: "网页抓取助手"
description: "使大型语言模型能够通过Puppeteer执行浏览器自动化任务，进行网页浏览、截屏和运行JavaScript。"
---

# 网页抓取助手

使大型语言模型能够通过Puppeteer执行浏览器自动化任务，进行网页浏览、截屏和运行JavaScript。

# Puppeteer

一个使用Puppeteer提供浏览器自动化功能的模型上下文协议服务器。该服务器使LLM能够与网页进行交互、截取屏幕截图并在真实的浏览器环境中执行JavaScript。

## 组件

### 工具

- **puppeteer_navigate**
  - 在浏览器中导航到任何URL
  - 输入: `url` (字符串)

- **puppeteer_screenshot**
  - 捕获整个页面或特定元素的屏幕截图
  - 输入:
    - `name` (字符串, 必填): 截图名称
    - `selector` (字符串, 可选): 要截图元素的CSS选择器
    - `width` (数字, 可选, 默认: 800): 截图宽度
    - `height` (数字, 可选, 默认: 600): 截图高度

- **puppeteer_click**
  - 点击页面上的元素
  - 输入: `selector` (字符串): 要点击元素的CSS选择器

- **puppeteer_hover**
  - 鼠标悬停在页面上的元素上
  - 输入: `selector` (字符串): 要悬停元素的CSS选择器

- **puppeteer_fill**
  - 填写输入字段
  - 输入:
    - `selector` (字符串): 输入字段的CSS选择器
    - `value` (字符串): 要填写的值

- **puppeteer_select**
  - 选择带有SELECT标签的元素
  - 输入:
    - `selector` (字符串): 要选择元素的CSS选择器
    - `value` (字符串): 要选择的值

- **puppeteer_evaluate**
  - 在浏览器控制台中执行JavaScript
  - 输入: `script` (字符串): 要执行的JavaScript代码

### 资源

服务器提供了两种类型的资源访问：

1. **控制台日志** (`console://logs`)
   - 文本格式的浏览器控制台输出
   - 包括来自浏览器的所有控制台消息

2. **屏幕截图** (`screenshot://`)
   - 捕获的屏幕截图的PNG图像
   - 通过捕获时指定的截图名称访问

## 主要特性

- 浏览器自动化
- 控制台日志监控
- 屏幕截图功能
- JavaScript执行
- 基本的网页交互（导航、点击、表单填写）

## 使用Puppeteer服务器的配置
这是使用Puppeteer服务器的Claude Desktop配置示例：

### Docker

**注意** Docker实现将使用无头Chromium，而NPX版本将打开一个浏览器窗口。

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

## 构建

Docker构建：

```bash
docker build -t mcp/puppeteer -f src/puppeteer/Dockerfile .
```

## 许可证

此MCP服务器根据MIT许可证发布。这意味着您可以在遵守MIT许可证条款和条件的前提下自由使用、修改和分发该软件。更多详情，请参阅项目仓库中的LICENSE文件。

**官方网站：** [https://github.com/jwaldor/mcp-scrape-copilot](https://github.com/jwaldor/mcp-scrape-copilot)
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

资源文件：`resources/mcp/jwaldor-scrape-copilot.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
