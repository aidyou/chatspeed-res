---
title: "xhs-mcp"
description: "小红书MCP服务 特点 - [x] 采用js逆向出x-s,x-t,直接请求http接口,无须笨重的playwright - [x] 搜索笔记 - [x] 获取笔记内容 - [x] 获取笔记的评论 - [x] 发表评论"
---

# xhs-mcp

小红书MCP服务 特点 - [x] 采用js逆向出x-s,x-t,直接请求http接口,无须笨重的playwright - [x] 搜索笔记 - [x] 获取笔记内容 - [x] 获取笔记的评论 - [x] 发表评论

# Xiaohongshu MCP Service
[Smithery](https://smithery.ai/server/@jobsonlook/xhs-mcp)
## Features
- [x] Uses js to reverse-engineer x-s, x-t, and directly requests HTTP interfaces without the need for the cumbersome playwright.
- [x] Search for posts
- [x] Get post content
- [x] Get comments on a post
- [x] Post a comment

![Features](/mcp-assets/ddc5bcdafe75a173149b4161771f4e89.png)

## Quick Start

### 1. Environment
 * node
 * python 3.12
 * uv (pip install uv)

### 2. Install Dependencies
sh
git clone git@github.com:jobsonlook/xhs-mcp.git
cd xhs-mcp
uv sync

### 3. Obtain Xiaohongshu's Cookie
[Open Xiaohongshu Webpage](https://www.xiaohongshu.com/explore)
After logging in, obtain the cookie and configure it into the XHS_COOKIE environment variable as shown in step 4.
![Cookie](/mcp-assets/5b6ed853fa991ef7c1b5e18d9f8d4e6f.png)

### 4. Configure MCP Server

json
{
    "mcpServers": {
        "xhs-mcp": {
            "command": "uv",
            "args": [
                "--directory",
                "/Users/xxx/xhs-mcp",
                "run",
                "main.py"
            ],
            "env": {
                "XHS_COOKIE": "xxxx"
            }
        }
    }
}

## Disclaimer
This project is intended solely for learning and communication purposes. It is strictly prohibited from being used for any other purposes, especially those involving commercial profit. Any such use will be at your own risk.

**Official site: ** [https://github.com/jobsonlook/xhs-mcp](https://github.com/jobsonlook/xhs-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `communication`
- Tags: `communication`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uv`
- Args: `--directory /Users/xxx/xhs-mcp run main.py`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/larryguan-xhs.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
