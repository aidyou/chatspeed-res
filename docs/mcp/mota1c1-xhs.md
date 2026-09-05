---
title: "xhs-mcp"
description: "An MCP server for Xiaohongshu (RED) that supports account login, copywriting generation, and automatic publishing through conversation. It supports automatic login and publishing for multiple accounts…"
---

# xhs-mcp

An MCP server for Xiaohongshu (RED) that supports account login, copywriting generation, and automatic publishing through conversation. It supports automatic login and publishing for multiple accounts…

# xhs-mcp

An MCP server for Xiaohongshu (RED) that supports account login, copywriting generation, and automatic publishing through conversation. Compared to existing implementations, the advantage is that account login and post publishing can all be automated within the conversation, and it supports batch publishing across multiple accounts. In addition, when calling the post-publishing API, the tool can automatically generate Xiaohongshu-style cover images based on the copy content.

## How it works

It uses browser simulation, launching a browser via ChromeDriver to automatically log in to accounts (a verification code is sent to the phone) and publish posts. After login, the Cookie is saved, so subsequent post publishing no longer requires re-login. The project integrates webdriver-manager, so there is no need to manually download and configure ChromeDriver - you only need to download and install the Chrome browser itself (download: https://www.google.com/intl/zh-CN/chrome/).

## Examples

## Environment Setup

1. Make sure Chrome is installed on the system (download: https://www.google.com/intl/zh-CN/chrome/)
2. Install uv

```
pip install uv # note: if you use anaconda for environment management, run pip in the base environment
```

## Starting the Server

When publishing a post with images, at least one cover image is required. So when the post-publishing tool is called, it automatically generates a Xiaohongshu-style cover image based on the copy. The DeepSeek chat model is used to generate the small cover image, so you need to configure the DEEPSEEK_API_KEY environment variable. To switch to another model, configure the BASE_URL environment variable; it defaults to DeepSeek's address.

### Method 1: Run the command directly

```
env DEEPSEEK_API_KEY=xxxx uvx --from lcl_xhs_mcp@latest xhs-server
```

To switch models:

```
env DEEPSEEK_API_KEY=xxxx BASE_URL=xxxx uvx --from lcl_xhs_mcp@latest xhs-server
```

To keep things concise, the BASE_URL environment variable configuration is omitted from the methods below.

### Method 2: Run via config file

Add the following to your config file:

```
{
  "mcpServers": {
    "xhs": {
      "command": "env",
      "args": [
        "DEEPSEEK_API_KEY=xxxx",
        "uvx",
        "--from",
        "lcl_xhs_mcp@latest",
        "xhs-server"
      ]
    }
  }
}
```

### Method 3: Install from source and run

This gives you the latest code.

```
git clone https://github.com/SoftEgLi/xhs-mcp.git
cd xhs-mcp
pip install -e . # note: if anaconda is installed, run pip in the base environment
```

MCP config file:

```
{
  "mcpServers": {
    "xhs-test": {
      "command": "xhs-server",
      "args": [],
      "env": {
        "DEEPSEEK_API_KEY": "xxxx"
      }
    }
  }
}
```

## Notes

The Cookie is valid for one month. If you log in to Xiaohongshu on the web yourself, the previous Cookie may become invalid; after it expires, publishing a post will go through the MCP login flow again.

## License

MIT

**Official site: ** [https://github.com/SoftEgLi/xhs-mcp](https://github.com/SoftEgLi/xhs-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `communication`
- Tags: `communication`

## MCP Configuration

- Transport: `stdio`
- Command: `env`
- Args: `DEEPSEEK_API_KEY=xxxx uvx --from lcl_xhs_mcp@latest xhs-server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/mota1c1-xhs.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
