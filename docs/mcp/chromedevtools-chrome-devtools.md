---
title: "chrome-devtools-mcp"
description: "chrome-devtools-mcp lets your coding agent (such as Gemini, Claude, Cursor or Copilot) control and inspect a live Chrome browser."
---

# chrome-devtools-mcp

chrome-devtools-mcp lets your coding agent (such as Gemini, Claude, Cursor or Copilot) control and inspect a live Chrome browser.

# Chrome DevTools MCP

[![npm chrome-devtools-mcp package](/mcp-assets/f1fc73db44f37c32798e59572b5469ce.svg)](https://npmjs.org/package/chrome-devtools-mcp)

`chrome-devtools-mcp` lets your coding agent (such as Gemini, Claude, Cursor or Copilot)
control and inspect a live Chrome browser. It acts as a Model-Context-Protocol
(MCP) server, giving your AI coding assistant access to the full power of
Chrome DevTools for reliable automation, in-depth debugging, and performance analysis.

## Key features

- **Get performance insights**: Uses [Chrome
  DevTools](https://github.com/ChromeDevTools/devtools-frontend) to record
  traces and extract actionable performance insights.
- **Advanced browser debugging**: Analyze network requests, take screenshots and
  check the browser console.
- **Reliable automation**. Uses
  [puppeteer](https://github.com/puppeteer/puppeteer) to automate actions in
  Chrome and automatically wait for action results.

## Disclaimers

`chrome-devtools-mcp` exposes content of the browser instance to the MCP clients
allowing them to inspect, debug, and modify any data in the browser or DevTools.
Avoid sharing sensitive or personal information that you don't want to share with
MCP clients.

## Requirements

- [Node.js 22.12.0](https://nodejs.org/) or newer.
- [Chrome](https://www.google.com/chrome/) current stable version or newer.
- [npm](https://www.npmjs.com/).

## Getting started

Add the following config to your MCP client:

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
> Using `chrome-devtools-mcp@latest` ensures that your MCP client will always use the latest version of the Chrome DevTools MCP server.

### MCP Client configuration

  Claude Code
    Use the Claude Code CLI to add the Chrome DevTools MCP server (
guide
):

```bash
claude mcp add chrome-devtools npx chrome-devtools-mcp@latest
```

  Cline
  Follow https://docs.cline.bot/mcp/configuring-mcp-servers and use the config provided above.

  Codex
  Follow the 
configure MCP guide

  using the standard config from above. You can also install the Chrome DevTools MCP server using the Codex CLI:

```bash
codex mcp add chrome-devtools -- npx chrome-devtools-mcp@latest
```

  Copilot / VS Code
  Follow the MCP install 
guide
,
  with the standard config from above. You can also install the Chrome DevTools MCP server using the VS Code CLI:
  
```bash
  code --add-mcp '{"name":"chrome-devtools","command":"npx","args":["chrome-devtools-mcp@latest"]}'
```

  Cursor

**Click the button to install:**

[
](https://cursor.com/en/install-mcp?name=chrome-devtools&config=eyJjb21tYW5kIjoibnB4IGNocm9tZS1kZXZ0b29scy1tY3BAbGF0ZXN0In0%3D)

**Or install manually:**

Go to `Cursor Settings` -> `MCP` -> `New MCP Server`. Use the config provided above.

  Gemini CLI
  Follow the 
MCP guide

  using the standard config from above.

  Gemini Code Assist
  Follow the 
configure MCP guide

  using the standard config from above.

### Your first prompt

Enter the following prompt in your MCP Client to check if everything is working:

```
Check the performance of https://developers.chrome.com
```

Your MCP client should open the browser and record a performance trace.

> [!NOTE]  
> The MCP server will start the browser automatically once the MCP client uses a tool that requires a running browser instance. Connecting to the Chrome DevTools MCP server on its own will not automatically start the browser.

## Tools

- **Input automation** (7 tools)
  - [`click`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#click)
  - [`drag`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#drag)
  - [`fill`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#fill)
  - [`fill_form`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#fill_form)
  - [`handle_dialog`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#handle_dialog)
  - [`hover`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#hover)
  - [`upload_file`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#upload_file)
- **Navigation automation** (7 tools)
  - [`close_page`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#close_page)
  - [`list_pages`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#list_pages)
  - [`navigate_page`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#navigate_page)
  - [`navigate_page_history`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#navigate_page_history)
  - [`new_page`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#new_page)
  - [`select_page`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#select_page)
  - [`wait_for`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#wait_for)
- **Emulation** (3 tools)
  - [`emulate_cpu`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#emulate_cpu)
  - [`emulate_network`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#emulate_network)
  - [`resize_page`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#resize_page)
- **Performance** (3 tools)
  - [`performance_analyze_insight`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#performance_analyze_insight)
  - [`performance_start_trace`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#performance_start_trace)
  - [`performance_stop_trace`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#performance_stop_trace)
- **Network** (2 tools)
  - [`get_network_request`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#get_network_request)
  - [`list_network_requests`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#list_network_requests)
- **Debugging** (4 tools)
  - [`evaluate_script`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#evaluate_script)
  - [`list_console_messages`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#list_console_messages)
  - [`take_screenshot`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#take_screenshot)
  - [`take_snapshot`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/docs/tool-reference.md#take_snapshot)

## Configuration

The Chrome DevTools MCP server supports the following configuration option:

- **`--browserUrl`, `-u`**
  Connect to a running Chrome instance using port forwarding. For more details see: https://developer.chrome.com/docs/devtools/remote-debugging/local-server.
  - **Type:** string

- **`--headless`**
  Whether to run in headless (no UI) mode.
  - **Type:** boolean
  - **Default:** `false`

- **`--executablePath`, `-e`**
  Path to custom Chrome executable.
  - **Type:** string

- **`--isolated`**
  If specified, creates a temporary user-data-dir that is automatically cleaned up after the browser is closed.
  - **Type:** boolean
  - **Default:** `false`

- **`--channel`**
  Specify a different Chrome channel that should be used. The default is the stable channel version.
  - **Type:** string
  - **Choices:** `stable`, `canary`, `beta`, `dev`

Pass them via the `args` property in the JSON configuration. For example:

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

You can also run `npx chrome-devtools-mcp@latest --help` to see all available configuration options.

## Concepts

### User data directory

`chrome-devtools-mcp` starts a Chrome's stable channel instance using the following user
data directory:

- Linux / MacOS: `$HOME/.cache/chrome-devtools-mcp/chrome-profile-$CHANNEL`
- Window: `%HOMEPATH%/.cache/chrome-devtools-mcp/chrome-profile-$CHANNEL`

The user data directory is not cleared between runs and shared across
all instances of `chrome-devtools-mcp`. Set the `isolated` option to `true`
to use a temporary user data dir instead which will be cleared automatically after
the browser is closed.

## Known limitations

### Operating system sandboxes

Some MCP clients allow sandboxing the MCP server using macOS Seatbelt or Linux
containers. If sandboxes are enabled, `chrome-devtools-mcp` is not able to start
Chrome that requires permissions to create its own sandboxes. As a workaround,
either disable sandboxing for `chrome-devtools-mcp` in your MCP client or use
`--connect-url` to connect to a Chrome instance that you start manually outside
of the MCP client sandbox.

**Official site: ** [https://github.com/ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `browser`
- Tags: `browser automation`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `chrome-devtools-mcp@latest`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/chromedevtools-chrome-devtools.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
