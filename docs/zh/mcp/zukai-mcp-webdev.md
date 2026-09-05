---
title: "网页开发MCP"
description: "一个提供网页开发工具的MCP服务器，例如屏幕捕捉功能，可以让AI代理获取并处理用户屏幕的截图。"
---

# 网页开发MCP

一个提供网页开发工具的MCP服务器，例如屏幕捕捉功能，可以让AI代理获取并处理用户屏幕的截图。

# webdev-mcp

An MCP server that provides useful web development tools.

## Usage

### Cursor

- To install in a project, add the MCP server to your `.cursor/mcp.json`:

```json
{
	"mcpServers": {
		"webdev": {
			"command": "npx",
			"args": ["webdev-mcp"],

		}
	}
}
```

- To install globally, add this command to your Cursor settings:

```bash
npx webdev-mcp
```

### Windsurf

- Add the MCP server to your `~/.codeium/windsurf/mcp_config.json` file:

```json
{
	"mcpServers": {
		"webdev": {
			"command": "npx",
			"args": ["webdev-mcp"]
		}
	}
}
```

## Tools

Currently, the only 2 tools are `takeScreenshot` and `listScreens`. Your agent can use the list screens tool to get the screen id of the screen it wants to screenshot.

The tool will return the screenshot as a base64 encoded string.

## Tips

Make sure YOLO mode is on and MCP tools protection is off in your Cursor settings for the best experience. You might have to allow Cursor to record your screen on MacOS.

**官方网站：** [https://github.com/ZukAi-MCP/webdev-mcp](https://github.com/ZukAi-MCP/webdev-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`browser`
- 标签：`developer tools`, `image and video processing`, `browser automation`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`webdev-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/zukai-mcp-webdev.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
