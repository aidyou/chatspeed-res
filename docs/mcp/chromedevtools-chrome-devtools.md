---
title: "Chrome开发者工具MCP"
description: "chrome-devtools-mcp 是一个工具，允许编码代理控制和检查实时的 Chrome 浏览器。它作为一个 MCP 服务器运行，提供对 Chrome DevTools 的完全访问权限，以实现自动化、调试和性能分析。"
---

# Chrome开发者工具MCP

chrome-devtools-mcp 是一个工具，允许编码代理控制和检查实时的 Chrome 浏览器。它作为一个 MCP 服务器运行，提供对 Chrome DevTools 的完全访问权限，以实现自动化、调试和性能分析。

# Chrome DevTools MCP

[![npm chrome-devtools-mcp package](/mcp-assets/f1fc73db44f37c32798e59572b5469ce.svg)](https://npmjs.org/package/chrome-devtools-mcp)

`chrome-devtools-mcp` 使您的编码代理（如 Gemini、Claude、Cursor 或 Copilot）能够控制和检查实时的 Chrome 浏览器。它充当 Model-Context-Protocol (MCP) 服务器，让您的 AI 编码助手能够访问 Chrome DevTools 的全部功能，以实现可靠的自动化、深入调试和性能分析。

## 主要特性

- **获取性能洞察**：使用 [Chrome DevTools](https://github.com/ChromeDevTools/devtools-frontend) 记录跟踪并提取可操作的性能洞察。
- **高级浏览器调试**：分析网络请求、截屏并检查浏览器控制台。
- **可靠的自动化**。使用 [puppeteer](https://github.com/puppeteer/puppeteer) 在 Chrome 中自动执行操作，并自动等待操作结果。

## 免责声明

`chrome-devtools-mcp` 将浏览器实例的内容暴露给 MCP 客户端，允许它们检查、调试和修改浏览器或 DevTools 中的任何数据。避免共享您不想与 MCP 客户端共享的敏感或个人信息。

## 要求

- [Node.js 22.12.0](https://nodejs.org/) 或更新版本。
- [Chrome](https://www.google.com/chrome/) 当前稳定版本或更新版本。
- [npm](https://www.npmjs.com/)。

## 开始使用

将以下配置添加到您的 MCP 客户端中：

```json

{

  "mcpServers": {

    "chrome-devtools": {

      "command": "npx",

      "args": ["chrome-devtools-mcp@latest"]

    }

  }

}

```
> [!NOTE]  
> 使用 `chrome-devtools-mcp@latest` 确保您的 MCP 客户端始终使用最新版本的 Chrome DevTools MCP 服务器。

### MCP 客户端配置

  Claude Code
    使用 Claude Code CLI 添加 Chrome DevTools MCP 服务器（
指南
）：

```bash

claude mcp add chrome-devtools npx chrome-devtools-mcp@latest

```

  Cline
  遵循 https://docs.cline.bot/mcp/configuring-mcp-servers 并使用上面提供的配置。

  Codex
  遵循 
配置 MCP 指南

  使用上面的标准配置。您还可以使用 Codex CLI 安装 Chrome DevTools MCP 服务器：

```bash

codex mcp add chrome-devtools -- npx chrome-devtools-mcp@latest

```

  Copilot / VS Code
  遵循 MCP 安装 
指南
，
  使用上面的标准配置。您还可以使用 VS Code CLI 安装 Chrome DevTools MCP 服务器：
  
```bash
  
  code --add-mcp '{"name":"chrome-devtools","command":"npx","args":["chrome-devtools-mcp@latest"]}'
  
```

  Cursor

**点击按钮安装：**

[
](https://cursor.com/en/install-mcp?name=chrome-devtools&config=eyJjb21tYW5kIjoibnB4IGNocm9tZS1kZXZ0b29scy1tY3BAbGF0ZXN0In0%3D)

**或者手动安装：**

转到 `Cursor 设置` -> `MCP` -> `新建 MCP 服务器`。使用上面提供的配置。

  Gemini CLI
  遵循 
MCP 指南

  使用上面的标准配置。

  Gemini Code Assist
  遵循 
配置 MCP 指南

  使用上面的标准配置。

### 您的第一个提示

在您的 MCP 客户端中输入以下提示，以检查一切是否正常工作：

```

Check the performance of https://developers.chrome.com

```
您的 MCP 客户端应打开浏览器并记录性能跟踪。

> [!NOTE]  
> MCP 服务器将在 MCP 客户端使用需要运行浏览器实例的工具时自动启动浏览器。仅连接到 Chrome DevTools MCP 服务器本身不会自动启动浏览器。

## 工具

- **输入自动化**（7 个工具）
  - [`click`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#click)
  - [`drag`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#drag)- [`fill`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#fill)
  - [`fill_form`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#fill_form)
  - [`handle_dialog`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#handle_dialog)
  - [`hover`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#hover)
  - [`upload_file`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#upload_file)
- **导航自动化** (7 个工具)
  - [`close_page`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#close_page)
  - [`list_pages`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#list_pages)
  - [`navigate_page`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#navigate_page)
  - [`navigate_page_history`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#navigate_page_history)
  - [`new_page`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#new_page)
  - [`select_page`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#select_page)
  - [`wait_for`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#wait_for)
- **模拟** (3 个工具)
  - [`emulate_cpu`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#emulate_cpu)
  - [`emulate_network`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#emulate_network)
  - [`resize_page`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#resize_page)
- **性能** (3 个工具)
  - [`performance_analyze_insight`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#performance_analyze_insight)
  - [`performance_start_trace`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#performance_start_trace)
  - [`performance_stop_trace`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#performance_stop_trace)
- **网络** (2 个工具)
  - [`get_network_request`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#get_network_request)
  - [`list_network_requests`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#list_network_requests)
- **调试** (4 个工具)
  - [`evaluate_script`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#evaluate_script)
  - [`list_console_messages`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#list_console_messages)
  - [`take_screenshot`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#take_screenshot)
  - [`take_snapshot`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#take_snapshot)

## 配置

Chrome DevTools MCP 服务器支持以下配置选项：

- **`--browserUrl`, `-u`**
  使用端口转发连接到正在运行的 Chrome 实例。更多详情请参见：https://developer.chrome.com/docs/devtools/remote-debugging/local-server。
  - **类型:** 字符串

- **`--headless`**
  是否以无头（无 UI）模式运行。
  - **类型:** 布尔值
  - **默认值:** `false`

- **`--executablePath`, `-e`**
  自定义 Chrome 可执行文件的路径。
  - **类型:** 字符串

- **`--isolated`**
  如果指定，则创建一个在浏览器关闭后自动清理的临时用户数据目录。
  - **类型:** 布尔值
  - **默认值:** `false`

- **`--channel`**
  指定应使用的不同 Chrome 通道。默认是稳定版通道版本。
  - **类型:** 字符串
  - **选项:** `stable`, `canary`, `beta`, `dev`

通过 JSON 配置中的 `args` 属性传递这些选项。例如：

```json

{

  "mcpServers": {

    "chrome-devtools": {

      "command": "npx",

      "args": [

        "chrome-devtools-mcp@latest",

        "--channel=canary",

        "--headless=true",

        "--isolated=true"

      ]

    }

  }

}

```
您还可以运行 `npx chrome-devtools-mcp@latest --help` 来查看所有可用的配置选项。

## 概念

### 用户数据目录

`chrome-devtools-mcp` 使用以下用户数据目录启动 Chrome 的稳定版实例：

- Linux / MacOS: `$HOME/.cache/chrome-devtools-mcp/chrome-profile-$CHANNEL`
- Windows: `%HOMEPATH%/.cache/chrome-devtools-mcp/chrome-profile-$CHANNEL`

用户数据目录在多次运行之间不会被清除，并且在所有 `chrome-devtools-mcp` 实例之间共享。将 `isolated` 选项设置为 `true` 以使用一个临时用户数据目录，该目录将在浏览器关闭后自动清除。

## 已知限制

### 操作系统沙箱

某些 MCP 客户端允许使用 macOS Seatbelt 或 Linux 容器对 MCP 服务器进行沙箱化。如果启用了沙箱，`chrome-devtools-mcp` 将无法启动需要权限来创建自己沙箱的 Chrome。作为解决方法，您可以在您的 MCP 客户端中禁用 `chrome-devtools-mcp` 的沙箱，或者使用 `--connect-url` 连接到您手动在 MCP 客户端沙箱之外启动的 Chrome 实例。

**官方网站：** [https://github.com/ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`browser`
- 标签：`browser automation`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`chrome-devtools-mcp@latest`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/chromedevtools-chrome-devtools.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
