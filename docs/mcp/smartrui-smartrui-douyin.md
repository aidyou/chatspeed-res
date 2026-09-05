---
title: "smartrui-douyin-mcp-server"
description: "TikTok Video Text Content Parsing and Watermark-Free Video Download 1. 简介 本文档将介绍如何解析抖音视频中的文本内容，并提供一种方法来下载无水印的抖音视频。 2. 抖音视频文本内容解析 2.1 获取视频链接 首先，你需要获取你想要解析的抖音视频的分享链接。例如： https://v.douyin.com/xxxxxx/ 2.2…"
---

# smartrui-douyin-mcp-server

TikTok Video Text Content Parsing and Watermark-Free Video Download 1. 简介 本文档将介绍如何解析抖音视频中的文本内容，并提供一种方法来下载无水印的抖音视频。 2. 抖音视频文本内容解析 2.1 获取视频链接 首先，你需要获取你想要解析的抖音视频的分享链接。例如： https://v.douyin.com/xxxxxx/ 2.2…

TikTok Video Text Content Parsing and Watermark-Free Video Download

## 1. 简介
本文档将介绍如何解析抖音视频中的文本内容，并提供一种方法来下载无水印的抖音视频。

## 2. 抖音视频文本内容解析
### 2.1 获取视频链接
首先，你需要获取你想要解析的抖音视频的分享链接。例如：

https://v.douyin.com/xxxxxx/

### 2.2 使用API解析
你可以使用第三方API来解析抖音视频的内容。这里我们以一个假设的API为例：
python
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

### 2.3 解析结果
解析后的结果通常包含视频标题、描述、作者信息等。例如：
json
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

## 3. 无水印视频下载
### 3.1 获取无水印视频链接
通过解析得到的`play_addr`通常是带有水印的视频链接。为了获取无水印的视频链接，可以使用以下方法：
python
def get_watermark_free_link(play_addr):
    # 假设通过某种方式可以转换为无水印链接
    watermark_free_link = play_addr.replace("playwm", "play")
    return watermark_free_link

watermark_free_link = get_watermark_free_link(result["play_addr"])
print(watermark_free_link)

### 3.2 下载无水印视频
使用Python的`requests`库可以轻松下载视频：
python
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

## 4. 总结
本文介绍了如何解析抖音视频中的文本内容以及如何下载无水印的抖音视频。希望这些信息对你有所帮助！

更多关于抖音API的信息，请参考[官方文档](https://developers.douyin.com/)。

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
