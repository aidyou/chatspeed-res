---
title: "Kuaizi-MCP"
description: "Kuaizi MCP Server has created a seamless integration of LLM Agents and the capabilities of the Kuaizi SaaS platform. Through six core service interfaces, it empowers the commercial video production pr…"
---

# Kuaizi-MCP

Kuaizi MCP Server has created a seamless integration of LLM Agents and the capabilities of the Kuaizi SaaS platform. Through six core service interfaces, it empowers the commercial video production pr…

## Product Introduction

Kuaizi MCP Server has created a seamless integration of LLM Agents and the capabilities of the Kuaizi SaaS platform.  Through six core service interfaces, it empowers the commercial video production process in all aspects.  From AI script generation, Lingguangsuo creative mining, Zhijing video structure analysis, to one-click automatic synthesis of finished videos, intelligent slicing of long videos and multi-language AI dubbing, we provide users with end-to-end video content production solutions.

Below is a virtual simplified usage scenario to help users understand the capabilities of various tools in Kuaizi MCP service:

> Traditional Workflow
>
> After receiving a beauty client's request, editor Xiao Lin manually searches for popular video inspirations, spends 3 hours writing storyboard scripts, and rents additional microscopic equipment to reshoot product close-ups due to unfamiliarity with laboratory shots. During editing, he repeatedly adjusts transition effects, and after exporting, he adjusts video dimensions and subtitle positions for Douyin and Xiaohongshu respectively, taking a total of 48 hours.
>
> Agent Intelligent Workflow
>
> 1.  Xiao Lin inputs the client's requirements to the Agent, and the Agent uses Inspiration Search to automatically generate keywords "mask makeup test/oily skin extreme challenge"
> 2.  After importing competitive hit videos to the Agent, the Agent uses the Smart Mirror analysis tool to break down the "pain point amplification + data endorsement + ordinary person comparison" structure
> 3.  Based on Xiao Lin's requirements, the Agent uses the AI script generation tool to output storyboards: virtual laboratory microscopic animation opening (0-3 seconds) + blogger wearing mask sports footage (4-12 seconds) + AI-generated 12-hour makeup retention dynamic chart (13-15 seconds)
> 4.  Finally, the Agent uses one-click video creation to automatically compose horizontal and vertical versions, simultaneously adding "makeup smudge sound effects" and dynamic large subtitles, with the Douyin version additionally generating Sichuan-Chongqing dialect dubbing
>
> Efficiency Leap
>
> The production time is compressed from 2 days to 90 minutes, and the finished video simultaneously tops Douyin's beauty rankings and Xiaohongshu's popular searches.

## Capability Introduction

### AI Script Generation

Input video topics and keywords to automatically generate structured video scripts including shot grouping, scene descriptions, and voice-over scripts.

*   Input

    *   input: Script topic, product selling points, promotional mechanisms, and other information (string, required)
    *   language: video script language (string, not required, default Chinese)
*   Output

    *   script: Structured video script containing shot grouping, scene descriptions, and voice-over scripts (string)

### Inspiration Search

Input product or industry keywords to generate relevant marketing inspirations and content strategy reports through AI analysis of internet-wide data.

*   Input

    *   query: Search content, such as product or industry keywords (string, required)
*   Output

    *   content: Marketing inspiration and content strategy report (string)
    *   image_list: Strategy report related images (array)

        *   url: Image URL (string)
    *   video_list: Strategy report related videos (array)

        *   url: Image URL (string)

### Smart Mirror Video Analysis

Input popular video links to intelligently analyze video structure and generate reusable creative script templates.

*   Input

    *   vedio_url: Analysis video link (string, required)
*   Output

    *   content: Video analysis script markdown text (string)

### One-Click Video Creation

Input product materials and core selling points to automatically compose multiple versions of marketing videos with AI dubbing, subtitles, and background music.

*   Input

    *   input: Marketing video keywords, brand name, product name, product selling points, etc. (string, required)
    *   material_list: Images or video materials used for composition (string)

        *   type: Material type, picture pic, video video (string, required)
        *   value: Material link URL (string, required)
*   Output

    *   video_list: Composed marketing video information (array)

        *   cover_url: Video cover image (string)
        *   video_url: Video link (string)
        *   video_name: Video name (string)
        *   video_duration: Video duration (float)

## Usage Methods

### Using in Cursor

Add the following configuration to `.cursor/mcp.json` in your Cursor project:

    {
      "mcpServers": {
        "mcp-server-kuaizi": {
          "url": "http://dev-mcp-video.kuaizi.co/sse"
        },
        "Other tools": {
          "...": "..."
        }
      }
    }

### Using in Trae

Find the MCP configuration page in your Trae AI assistant settings and manually add the custom MCP configuration JSON as follows:

    {
      "mcpServers": {
        "mcp-server-kuaizi": {
          "url": "http://dev-mcp-video.kuaizi.co/sse"
        },
        "Other tools": {
          "...": "..."
        }
      }
    }

### Using in Other MCP Clients

You can also use it in any other MCP Client by properly configuring the Server SSE connection as http://dev-mcp-video.kuaizi.co/sse to connect to the Kuaizi MCP Server.

**Official site: ** [https://www.modelscope.cn/mcp](https://www.modelscope.cn/mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `entertainment and media`, `art and culture`, `chinese`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/kuaizi-kuaizi.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
