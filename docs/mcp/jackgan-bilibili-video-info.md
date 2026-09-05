---
title: "bilibili_video_info"
description: "Bilibili Video Information Fetcher This is a Bilibili video information fetching tool based on Python and Gradio. It can quickly obtain detailed information about Bilibili videos, including the upload…"
---

# bilibili_video_info

Bilibili Video Information Fetcher This is a Bilibili video information fetching tool based on Python and Gradio. It can quickly obtain detailed information about Bilibili videos, including the upload…

# Bilibili Video Information Fetcher

This is a Bilibili video information fetching tool based on Python and Gradio. It can quickly obtain detailed information about Bilibili videos, including the uploader's information, basic video details, and video data, through video links or BV numbers.

## Features

- Supports input of Bilibili video links or direct input of BV numbers
- Retrieves detailed video information: title, type, description, release time, duration, etc.
- Obtains uploader information: nickname, user ID, number of followers, number of followings, etc.
- Retrieves video statistics: views, danmaku count, likes, coins, favorites, shares, etc.
- Provides a friendly web interface with example inputs
- Supports MCP server functionality for easy integration into other applications
- Generates publicly accessible links for convenient remote use

## Usage Instructions

1. Enter the Bilibili video link or BV number in the input box
2. Click the "Submit" button
3. View the fetched video details in the output box
4. Use the example buttons to quickly test

## MCP Server Functionality

This program supports MCP (Model Communication Protocol) server functionality, allowing other applications to communicate with this program via HTTP requests to fetch Bilibili video information.

### How to Use MCP Server

When the program runs, the MCP server will automatically start, and other applications can communicate with it as follows:

1. Send a POST request to the MCP server, with the request format as below:
http
POST /run/predict HTTP/1.1
Content-Type: application/json

{
  "data": ["Bilibili video link or BV number"]
}

2. The server will return a JSON formatted response containing the fetched video information

## Examples

### Example 1: Using BV Number
Input: `BV1XmtyzKEzQ`

### Example 2: Using Video Link
Input: `https://www.bilibili.com/video/BV1xx411x7x9/`

## Notes

- This tool is only for fetching publicly available video information and should not be used for any illegal purposes
- Please comply with Bilibili's user agreement and relevant regulations
- Due to Bilibili API restrictions, some video information may not be accessible or require login
- If you encounter issues during use, please check your network connection or try using a different video link

**Official site: ** [http://modelscope.cn/studios/JackGan/bilibili_video_info](http://modelscope.cn/studios/JackGan/bilibili_video_info)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `search`, `entertainment and media`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `mcp-remote https://jackgan-bilibili-video-info.ms.show/gradio_api/mcp/sse --transport sse-only`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/jackgan-bilibili-video-info.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
