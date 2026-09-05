---
title: "jianying-mcp"
description: "JianYing MCP - JianYing video creation MCP server. An automation tool for JianYing (CapCut) video creation based on the Model Context Protocol (MCP), allowing AI assistants to create professional vide…"
---

# jianying-mcp

JianYing MCP - JianYing video creation MCP server. An automation tool for JianYing (CapCut) video creation based on the Model Context Protocol (MCP), allowing AI assistants to create professional vide…

# JianYing MCP - JianYing Video Creation MCP Server

[![Python](/mcp-assets/e6032a21a37092c71fd226dca6c53827.svg)](https://python.org)
[![MCP](/mcp-assets/dea21ef1b755e12c928a6fd915869854.svg)](https://modelcontextprotocol.io)
![License](/mcp-assets/fa73b4786cfc281bb30f39f895ada091.svg)

An automation tool for JianYing (CapCut) video creation based on the Model Context Protocol (MCP), allowing AI assistants to create professional video content through natural language.

## Project Introduction

JianYing MCP is a powerful video creation automation tool that lets AI:

- Automatically create JianYing draft projects
- Intelligently add audio, video, and text materials
- Apply various effects, filters, and animations
- Automate the video editing workflow
- Export to JianYing-editable project files

## Core Features

### Draft Management
- `rules` - video production guidelines
- `create_draft` - create a new video draft project
- `export_draft` - export as a JianYing project file

### Track Management
- `create_track` - create video/audio/text tracks

### Video Processing
- `add_video_segment` - add a video segment (local file or URL)
- `add_video_animation` - add entry/exit animations
- `add_video_transition` - add transition effects
- `add_video_filter` - apply filter effects
- `add_video_mask` - add mask effects
- `add_video_background_filling` - background fill
- `add_video_keyframe` - keyframe animation

### Audio Processing
- `add_audio_segment` - add an audio segment (local file or URL)
- `add_audio_effect` - audio effects (electro, reverb, etc.)
- `add_audio_fade` - fade in/out effects
- `add_audio_keyframe` - audio keyframes

### Text Processing
- `add_text_segment` - add a text segment
- `add_text_animation` - text animation effects
- `add_text_bubble` - text bubble effects
- `add_text_effect` - fancy text effects

### Utilities
- `parse_media_info` - parse media file information
- `find_effects_by_type` - find available effect resources

## Quick Start

### 1. Install uv

**Windows:**
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Clone the project and install dependencies

```bash
git clone https://github.com/your-username/jianying-mcp.git
cd jianying-mcp
uv sync
```

### 3. Configure the MCP client

Using Augment Code as an example, add the server config to your MCP client:

```json
{
  "mcpServers": {
    "jianying-mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "/your-path/jianying-mcp/jianyingdraft",
        "run",
        "server.py"
      ],
      "env": {
        "SAVE_PATH": "/your-path/draft",
        "OUTPUT_PATH": "/your-path/output"
      }
    }
  }
}
```
- SAVE_PATH: data storage path - stores the draft operation data
- OUTPUT_PATH: export path - where generated JianYing draft files are placed

## Demo Video

Watch the [full demo video](https://www.bilibili.com/video/BV1rhe4z1Eu1)

## Development Guide

### Debug mode

Debug with MCP Inspector:

```bash
uv run mcp dev jianyingdraft/server.py
```

## Acknowledgments

- [Model Context Protocol](https://modelcontextprotocol.io) - the powerful AI integration protocol
- [pyJianYingDraft](https://github.com/GuanYixuan/pyJianYingDraft) - the JianYing project file processing library

---

If this project helps you, please give it a Star!

**Official site: ** [https://github.com/hey-jian-wei/jianying-mcp](https://github.com/hey-jian-wei/jianying-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `entertainment and media`, `剪辑`

## MCP Configuration

- Transport: `stdio`
- Command: `uv`
- Args: `--directory /your-path/jianying-mcp/jianyingdraft run server.py`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/heyboy-jianying.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
