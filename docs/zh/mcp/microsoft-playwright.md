---
title: "微软Playwright"
description: "一种模型上下文协议服务器，它使大型语言模型能够通过结构化的可访问性快照与网页交互，而无需使用视觉模型或截图。"
---

# 微软Playwright

一种模型上下文协议服务器，它使大型语言模型能够通过结构化的可访问性快照与网页交互，而无需使用视觉模型或截图。

## Playwright MCP

一个使用 [Playwright](https://playwright.dev) 提供浏览器自动化功能的 Model Context Protocol (MCP) 服务器。该服务器使 LLM 能够通过结构化的无障碍快照与网页进行交互，从而绕过了对屏幕截图或视觉调优模型的需求。

### 主要特性

- **快速且轻量**：使用 Playwright 的无障碍树，而不是基于像素的输入。
- **LLM 友好**：无需视觉模型，纯粹基于结构化数据操作。
- **确定性的工具应用**：避免了基于屏幕截图方法常见的歧义。

### 使用场景

- 网页导航和表单填写
- 从结构化内容中提取数据
- 由 LLM 驱动的自动化测试
- 适用于代理的一般用途浏览器交互

### 示例配置

```js
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest"
      ]
    }
  }
}
```

#### 在 VS Code 中安装

使用以下按钮之一在 VS Code 中安装 Playwright MCP 服务器：

[
](https://insiders.vscode.dev/redirect?url=vscode-insiders%3Amcp%2Finstall%3F%257B%2522name%2522%253A%2522playwright%2522%252C%2522command%2522%253A%2522npx%2522%252C%2522args%2522%253A%255B%2522-y%2522%252C%2522%2540playwright%252Fmcp%2540latest%2522%255D%257D)

或者，您可以使用 VS Code CLI 安装 Playwright MCP 服务器：

```bash
# For VS Code
code --add-mcp '{"name":"playwright","command":"npx","args":["@playwright/mcp@latest"]}'
```

```bash
# For VS Code Insiders
code-insiders --add-mcp '{"name":"playwright","command":"npx","args":["@playwright/mcp@latest"]}'
```

安装后，您可以在 VS Code 中使用 GitHub Copilot 代理来使用 Playwright MCP 服务器。

### 命令行选项

Playwright MCP 服务器支持以下命令行选项：

- `--browser 
`：使用的浏览器或 Chrome 通道。可能的值：
  - `chrome`, `firefox`, `webkit`, `msedge`
  - Chrome 通道：`chrome-beta`, `chrome-canary`, `chrome-dev`
  - Edge 通道：`msedge-beta`, `msedge-canary`, `msedge-dev`
  - 默认值：`chrome`
- `--cdp-endpoint `：连接到的 CDP 端点
- `--executable-path 
`：浏览器可执行文件的路径
- `--headless`：以无头模式运行浏览器（默认为有头模式）
- `--port 
`：监听的端口用于 SSE 传输
- `--user-data-dir 
`：用户数据目录的路径
- `--vision`：运行使用屏幕截图的服务器（默认使用 Aria 快照）

### 用户数据目录

Playwright MCP 将使用新的配置文件启动浏览器，位于

```
- `%USERPROFILE%\AppData\Local\ms-playwright\mcp-chrome-profile` on Windows
- `~/Library/Caches/ms-playwright/mcp-chrome-profile` on macOS
- `~/.cache/ms-playwright/mcp-chrome-profile` on Linux
```

所有登录信息将存储在该配置文件中，您可以在会话之间删除它以清除离线状态。

### 运行无头浏览器（无 GUI 的浏览器）。

此模式对于后台或批处理操作非常有用。

```js
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest",
        "--headless"
      ]
    }
  }
}
```

### 在没有 DISPLAY 的 Linux 上运行有头浏览器

当在没有显示的系统上运行有头浏览器或从IDE的工作进程中运行时，请在具有DISPLAY环境的环境中运行MCP服务器，并传递`--port`标志以启用SSE传输。

```bash
npx @playwright/mcp@latest --port 8931
```

然后，在MCP客户端配置中，将`url`设置为SSE端点：

```js
{
  "mcpServers": {
    "playwright": {
      "url": "http://localhost:8931/sse"
    }
  }
}
```

### 工具模式

这些工具提供两种模式：

1. **快照模式**（默认）：使用可访问性快照以提高性能和可靠性
2. **视觉模式**：使用屏幕截图进行基于视觉的交互

要使用视觉模式，在启动服务器时添加`--vision`标志：

```js
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest",
        "--vision"
      ]
    }
  }
}
```

视觉模式最适合那些能够根据提供的屏幕截图使用X Y坐标空间与元素交互的计算机使用模型。

### 使用自定义传输的编程用法

```js
import { createServer } from '@playwright/mcp';

// ...

const server = createServer({
  launchOptions: { headless: true }
});
transport = new SSEServerTransport("/messages", res);
server.connect(transport);
```

### 快照模式

Playwright MCP 提供了一组用于浏览器自动化的工具。以下是所有可用工具：

- **browser_navigate**
  - Description: Navigate to a URL
  - Parameters:
    - `url` (string): The URL to navigate to

- **browser_go_back**
  - Description: Go back to the previous page
  - Parameters: None

- **browser_go_forward**
  - Description: Go forward to the next page
  - Parameters: None

- **browser_click**
  - Description: Perform click on a web page
  - Parameters:
    - `element` (string): Human-readable element description used to obtain permission to interact with the element
    - `ref` (string): Exact target element reference from the page snapshot

- **browser_hover**
  - Description: Hover over element on page
  - Parameters:
    - `element` (string): Human-readable element description used to obtain permission to interact with the element
    - `ref` (string): Exact target element reference from the page snapshot

- **browser_drag**
  - Description: Perform drag and drop between two elements
  - Parameters:
    - `startElement` (string): Human-readable source element description used to obtain permission to interact with the element
    - `startRef` (string): Exact source element reference from the page snapshot
    - `endElement` (string): Human-readable target element description used to obtain permission to interact with the element
    - `endRef` (string): Exact target element reference from the page snapshot

- **browser_type**
  - Description: Type text into editable element
  - Parameters:
    - `element` (string): Human-readable element description used to obtain permission to interact with the element
    - `ref` (string): Exact target element reference from the page snapshot
    - `text` (string): Text to type into the element
    - `submit` (boolean): Whether to submit entered text (press Enter after)

- **browser_select_option**
  - Description: Select option in a dropdown
  - Parameters:
    - `element` (string): Human-readable element description used to obtain permission to interact with the element
    - `ref` (string): Exact target element reference from the page snapshot
    - `values` (array): Array of values to select in the dropdown.

- **browser_choose_file**
  - Description: Choose one or multiple files to upload
  - Parameters:
    - `paths` (array): The absolute paths to the files to upload. Can be a single file or multiple files.

- **browser_press_key**
  - Description: Press a key on the keyboard
  - Parameters:
    - `key` (string): Name of the key to press or a character to generate, such as `ArrowLeft` or `a`

- **browser_snapshot**
  - Description: Capture accessibility snapshot of the current page (better than screenshot)
  - Parameters: None

- **browser_save_as_pdf**
  - Description: Save page as PDF
  - Parameters: None

- **browser_take_screenshot**
  - Description: Capture screenshot of the page
  - Parameters:
    - `raw` (string): Optionally returns lossless PNG screenshot. JPEG by default.

- **browser_wait**
  - Description: Wait for a specified time in seconds
  - Parameters:
    - `time` (number): The time to wait in seconds (capped at 10 seconds)

- **browser_close**
  - Description: Close the page
  - Parameters: None

### 视觉模式

视觉模式提供了使用屏幕截图进行基于视觉的交互的工具。以下是所有可用工具：

- **browser_navigate**
  - 描述：导航到指定URL
  - 参数：
    - `url` (字符串): 要导航到的URL

- **browser_go_back**
  - 描述：返回上一页
  - 参数：无

- **browser_go_forward**
  - 描述：前进到下一页
  - 参数：无

- **browser_screenshot**
  - 描述：捕获当前页面的截图
  - 参数：无

- **browser_move_mouse**
  - 描述：将鼠标移动到指定坐标
  - 参数：
    - `x` (数字): X 坐标
    - `y` (数字): Y 坐标

- **browser_click**
  - 描述：在指定坐标点击
  - 参数：
    - `x` (数字): 点击的X坐标
    - `y` (数字): 点击的Y坐标

- **browser_drag**
  - 描述：执行拖放操作
  - 参数：
    - `startX` (数字): 开始X坐标
    - `startY` (数字): 开始Y坐标
    - `endX` (数字): 结束X坐标
    - `endY` (数字): 结束Y坐标

- **browser_type**
  - 描述：在指定坐标输入文本
  - 参数：
    - `text` (字符串): 要输入的文本
    - `submit` (布尔值): 是否提交输入的文本（输入后按Enter键）

- **browser_press_key**
  - 描述：按下键盘上的某个键
  - 参数：
    - `key` (字符串): 要按下的键名或要生成的字符，例如 `ArrowLeft` 或 `a`

- **browser_choose_file**
  - 描述：选择一个或多个文件上传
  - 参数：
    - `paths` (数组): 要上传文件的绝对路径。可以是一个文件或多文件。

- **browser_save_as_pdf**
  - 描述：将页面保存为PDF
  - 参数：无

- **browser_wait**
  - 描述：等待指定秒数
  - 参数：
    - `time` (数字): 等待的时间（以秒为单位，上限为10秒）

- **browser_close**
  - 描述：关闭页面
  - 参数：无

**官方网站：** [https://github.com/microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`, `browser`
- 标签：`browser automation`, `developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`@playwright/mcp@latest`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/microsoft-playwright.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
