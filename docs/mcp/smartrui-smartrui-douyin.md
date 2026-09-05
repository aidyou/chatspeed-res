---
title: "smartrui-douyin-mcp-server"
description: "TikTok Video Text Content Parsing and Watermark-Free Video Download: this document explains how to parse the text content of Douyin (TikTok China) videos and provides a way to download watermark-free…"
---

# smartrui-douyin-mcp-server

TikTok Video Text Content Parsing and Watermark-Free Video Download: this document explains how to parse the text content of Douyin (TikTok China) videos and provides a way to download watermark-free…

# TikTok Video Text Content Parsing and Watermark-Free Video Download

## 1. Introduction
This document explains how to parse the text content of Douyin (TikTok China) videos and provides a way to download watermark-free Douyin videos.

## 2. Parsing Douyin Video Text Content
### 2.1 Get the video link
First, get the share link of the Douyin video you want to parse. For example:

https://v.douyin.com/xxxxxx/

### 2.2 Parse with an API
You can use a third-party API to parse the Douyin video content. Here we use a hypothetical API as an example:

```python
import requests

def parse_douyin_video(url):
    api_url = "https://api.example.com/parse"
    response = requests.get(api_url, params={"url": url})
    if response.status_code == 200:
        return response.json()
    else:
        return None

video_url = "https://v.douyin.com/xxxxxx/"
result = parse_douyin_video(video_url)
if result:
    print(result)
else:
    print("Failed to parse the video.")
```

### 2.3 Parse result
The parsed result usually contains the video title, description, author info, etc. For example:

```json
{
    "title": "Amazing Travel Vlog",
    "description": "Join me on this amazing journey through the mountains!",
    "author": {
        "name": "TravelBuddy",
        "id": "123456789"
    },
    "cover_image": "http://example.com/image.jpg",
    "play_addr": "http://example.com/video.mp4"
}
```

## 3. Downloading Watermark-Free Videos
### 3.1 Get the watermark-free video link
The `play_addr` obtained by parsing is usually a video link with a watermark. To get a watermark-free video link, you can use the following method:

```python
def get_watermark_free_link(play_addr):
    # Assume there is some way to convert it to a watermark-free link
    watermark_free_link = play_addr.replace("playwm", "play")
    return watermark_free_link

watermark_free_link = get_watermark_free_link(result["play_addr"])
print(watermark_free_link)
```

### 3.2 Download the watermark-free video
You can easily download the video using Python's `requests` library:

```python
def download_video(url, filename):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        print(f"Video downloaded successfully: {filename}")
    else:
        print("Failed to download the video.")

download_video(watermark_free_link, "video.mp4")
```

## 4. Summary
This document introduced how to parse the text content of Douyin videos and how to download watermark-free Douyin videos. We hope this information helps you!

For more information about the Douyin API, refer to the [official documentation](https://developers.douyin.com/).

**Official site: ** [https://github.com/smartruiandqq/douyin-mcp-server.git](https://github.com/smartruiandqq/douyin-mcp-server.git)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `entertainment and media`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `douyin-mcp-server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/smartrui-smartrui-douyin.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
