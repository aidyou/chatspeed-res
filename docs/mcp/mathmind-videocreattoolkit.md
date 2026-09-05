---
title: "VideoCreatToolKit"
description: "I. Introduction: MathMind MCP Server provides a series of audio and video creation and synthesis tool services based on the MCP protocol. By adding MathMind-MCP service in any tool that supports MCP s…"
---

# VideoCreatToolKit

I. Introduction: MathMind MCP Server provides a series of audio and video creation and synthesis tool services based on the MCP protocol. By adding MathMind-MCP service in any tool that supports MCP s…

# I. Introduction:

MathMind MCP Server provides a series of audio and video creation and synthesis tool services based on the MCP protocol. By adding MathMind-MCP service in any tool that supports MCP services, users can describe scenes and requirements through natural language, and the tool will autonomously schedule a series of tools from MathMind to achieve intelligent generation of multimedia content.

# II. Core Tools
| No. | Tool Chinese Name | Tool English Name | Tool Description (Chinese) |
|----|--------------|--------------|------------------|
| 1  | Multiple images into a video | imgs2video | Synthesizes one or more images into a video, supporting the addition of background music and voiceover. |
| 2  | Multiple videos into one video | video2video | Synthesizes one or multiple video clips into a single video, supporting the upload of background music (optional) and voiceover (optional) to create a new video. Supports uploading separate head and tail videos, fixing the beginning and end of the video. Supports setting cover images, controlling voiceover volume, and customizing background music volume. |
| 3  | Video script extraction | video2txt | Extracts text from a video in real time; users just need to input the video link. It is recommended to upload videos under 5 minutes. |
| 4  | Video subtitle recognition | subtitleDynamic | Upload a video, and it will recognize subtitles and output the final video with subtitles. Subtitles support settings for font and position, etc. Supports passing in text. |
| 5  | Task query | taskFetch2 | Input the traceId output by the subtitleDynamic tool to get the video address after subtitles have been added. |
| 6  | Video clip extraction | videoCutRandom | Input the video link and specify the start and end positions to cut out a video segment. |
| 7  | Image to video | imageGenVideo | Upload an image and input prompt words to generate a video, using the VIDU model.
Supports both real-time and asynchronous generation. For asynchronous generation, you need to call the query tool: videoTaskFetch
Real-time directly generates a URL;
Asynchronous first only gives the traceId, and the user needs to call videoTaskFetch. |
| 8  | Image picture-in-picture | imgPip | Input a video and add images to it, such as logos or images related to the video content.
Supports customization of the width and height of the material, entry and exit times, animations, and display positions. If not specified, default values are used. |
| 9 | Picture-in-picture task query | cutTaskFetch | The above imgPip will only return ReqId, at which point you need to use the task query tool to actively check the results. |

# III. Quick Start
## Get API Key
Register on the MathMind Open Platform and obtain your API key, [go now](https://admin.mathmind.cn/login?referralCode=REF22431068)

## SSE Call Method

### Windsurf

Go to Windsurf > Settings > Cascade > Add Server > Add custom server to add the configuration:

{
  "mcpServers": {
    "mcp-server-mathmind": {
      "url": "https://mcp.mathmind.cn/sse?x-api-key="
    }
  }
}

### Cursor

Go to Cursor -> Preferences -> Cursor Settings -> MCP -> Add new global MCP Server to add the configuration:

{
  "mcpServers": {
    "mcp-server-mathmind": {
      "url": "https://mcp.mathmind.cn/sse?x-api-key="
    }
  }
}

### Tongyi Lingma

Go to Tongyi Lingma -> MCP Tools -> MCP Services -> Add New MCP Service via Configuration File -> lingma_mcp.json, and add the following configuration:

{
  "mcpServers": {
    "mcp-server-mathmind": {
      "url": "https://mcp.mathmind.cn/sse?x-api-key="
    }
  }
}

# IV. Additional Information

## Technical Support

Contact us via email: ai@mathmind.cn

Technical Support:

--- 
## Quick Links
- Official Website: https://mathmind.cn/
- Open Platform: https://admin.mathmind.cn/#/
- Plugin Marketplace: https://www.coze.cn/user/829510688450616
- Free Tutorials: https://mathmind.feishu.cn/wiki/OtIZwYuxbi1ErQkyovmc07HmnOh
- Paid Space: https://mathmind.feishu.cn/wiki/GvW8wyv2VithdnkNsVmcqhVNnYb
- Bilibili Video Tutorials: https://space.bilibili.com/87911991/channel/seriesdetail?sid=4634704
- Help Center: https://mathmind.feishu.cn/docx/Q6eodjvPLoq7yDxZaHOcfnFrntg
- Coze Discount: https://mathmind.feishu.cn/wiki/D9qSwIoaEixfqmkDupuceF62nFg

**Official site: ** [https://github.com/Runninghcm/MathMind-MCP-SERVER.git](https://github.com/Runninghcm/MathMind-MCP-SERVER.git)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `entertainment and media`, `developer tools`, `art and culture`, `视频`, `图生视频`, `视频剪辑`, `视频合成`, `剪映`, `剪辑`, `视频生成`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/mathmind-videocreattoolkit.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
