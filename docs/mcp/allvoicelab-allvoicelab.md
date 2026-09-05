---
title: "AllVoiceLab"
description: "Official AllVoiceLab Model Context Protocol (MCP) server, supporting interaction with powerful text-to-speech and video translation APIs. Enables MCP clients like Claude Desktop, Cursor, Windsurf, Ope…"
---

# AllVoiceLab

Official AllVoiceLab Model Context Protocol (MCP) server, supporting interaction with powerful text-to-speech and video translation APIs. Enables MCP clients like Claude Desktop, Cursor, Windsurf, Ope…

![image](/mcp-assets/40a0b7b61195a896a844e0080c111fe9.jpeg)

  

  

  

  

     style="display: inline-block; vertical-align: middle;"/>
  

   

    

  

Official AllVoiceLab Model Context Protocol (MCP) server, supporting interaction with powerful text-to-speech and video translation APIs. Enables MCP clients like Claude Desktop, Cursor, Windsurf, OpenAI Agents to generate speech, translate videos, and perform intelligent voice conversion. Serves scenarios such as short drama localization for global markets, AI-Generated audiobooks, AI-Powered production of film/TV narration.

## Why Choose AllVoiceLab MCP Server?

- Multi-engine technology unlocks infinite possibilities for voice: With simple text input, you can access video generation, speech synthesis, voice cloning, and more.
- AI Voice Generator (TTS): Natural voice generation in 30+ languages with ultra-high realism
- Voice Changer: Real-time voice conversion, ideal for gaming, live streaming, and privacy protection
- Vocal Separation: Ultra-fast 5ms separation of vocals and background music, with industry-leading precision
- Multilingual Dubbing: One-click translation and dubbing for short videos/films, preserving emotional tone and rhythm
- Speech-to-Text (STT): AI-powered multilingual subtitle generation with over 98% accuracy
- Subtitle Removal: Seamless hard subtitle erasure, even on complex backgrounds
- Voice Cloning: 3-Second Ultra-Fast Cloning with Human-like Voice Synthesis 

## Documentation

[中文文档](https://github.com/allvoicelab/AllVoiceLab-MCP/blob/HEAD/doc/README_CN.md)

## Quickstart

1. Get your API key from [AllVoiceLab](https://www.allvoicelab.com/).
2. Install `uv` (Python package manager), install with `curl -LsSf https://astral.sh/uv/install.sh | sh`
3. **Important**: The server addresses of APIs in different regions need to match the keys of the corresponding regions, otherwise there will be an error that the tool is unavailable.

|Region| Global  | Mainland  |
|:--|:-----|:-----|
|ALLVOICELAB_API_KEY| go get from [AllVoiceLab](https://www.allvoicelab.com/workbench/api-keys) | go get from [AllVoiceLab](https://www.allvoicelab.cn/workbench/api-keys) |
|ALLVOICELAB_API_DOMAIN| https://api.allvoicelab.com | https://api.allvoicelab.cn |

### Claude Desktop

Go to Claude > Settings > Developer > Edit Config > claude_desktop_config.json to include the following:
```json
{
  "mcpServers": {
    "AllVoceLab": {
      "command": "uvx",
      "args": ["allvoicelab-mcp"],
      "env": {
        "ALLVOICELAB_API_KEY": "
",
        "ALLVOICELAB_API_DOMAIN": "
",
        "ALLVOICELAB_BASE_PATH":"optional, default is user home directory.This is uesd to store the output files."
      }
    }
  }
}
```

If you're using Windows, you will have to enable "Developer Mode" in Claude Desktop to use the MCP server. Click "Help" in the hamburger menu in the top left and select "Enable Developer Mode".

### Cursor
Go to Cursor -> Preferences -> Cursor Settings -> MCP -> Add new global MCP Server to add above config.

That's it. Your MCP client can now interact with AllVoiceLab.

## Available methods

| Methods | Brief description |
| --- | --- |
| text_to_speech | Convert text to speech |
| speech_to_speech | Convert audio to another voice while preserving the speech content |
| isolate_human_voice | Extract clean human voice by removing background noise and non-speech sounds |
| clone_voice | Create a custom voice profile by cloning from an audio sample |
| remove_subtitle | Remove hardcoded subtitles from a video using OCR |
| video_translation_dubbing | Translate and dub video speech into different languages ​​|
| text_translation | Translate a text file into another language |
| subtitle_extraction | Extract subtitles from a video using OCR |

## Example usage

⚠️ Warning: AllVoiceLab credits are needed to use these tools.

### 1. Text to Speech

Try asking: Convert "At All Voice Lab, we’re reshaping the future of audio workflows with AI-powered solutions, making authentic voices accessible to creators everywhere." into voice.

![image](/mcp-assets/22aa3405fd79d117ce4b6019c21e1a98.png)

### 2. Voice Conversion

After generating the audio from the previous example, select the audio file and ask: Convert this to a male voice.

![image](/mcp-assets/42ecf0797cb972370ced8f5f50efde8a.png)

### 3. Remove Background Noise

Select an audio file with rich sounds (containing both BGM and human voice) and ask: Remove the background noise.

![image](/mcp-assets/138c7a1ab4d4a76ab856ced75a47bffd.png)

### 4. Voice Cloning

Select an audio file with a single voice and ask: Clone this voice.

![image](/mcp-assets/87d9bf2ca5c36e84e9a89fca8e31f621.png)

### 5. Video Translation

Select a video file (English) and ask: Translate this video to japanese.

![image](/mcp-assets/36a780f60ab1bfa39567f46123e62b0d.png)

Original video: 

![image](/mcp-assets/26a26214a1fe74ea59bb8e129602c854.png)

After translation: 

![image](/mcp-assets/b13a053fd0161e74cb27cd8d511e71aa.png)

### 6. Remove Subtitles

Select a video with subtitles and ask: Remove the subtitles from this video.

![image](/mcp-assets/2f1f6430b8f5081d32d4f4d54e2f5990.png)

Original video: 

![image](/mcp-assets/fcd9197b79e64b69b3155e90da7b4341.png)

After the task is completed: 

### 7. Text Translation

Select a long text (for example, "The Foolish Old Man Removes the Mountains") and ask: Translate this text to japanese.
If no language is specified, it will be translated to English by default.

![image](/mcp-assets/68e77f1e8092f7205103dfb286a0be0c.png)

### 8. Subtitle Extraction

Select a video with subtitles and ask: Extract the subtitles from this video.

![image](/mcp-assets/aa76d4a0c5b339b7c4573eb2271a385e.png)

After the task is completed, you will get an SRT file as shown below:

![image](/mcp-assets/20031174e1e67191d843962f6c209c82.png)

## Troubleshooting

Logs can be found at:

- Windows: C:\Users\\.mcp\allvoicelab_mcp.log
- macOS: ~/.mcp/allvoicelab_mcp.log

Please contact us by email(tech@allvoicelab.com) with log files

**Official site: ** [https://github.com/allvoicelab/AllVoiceLab-MCP](https://github.com/allvoicelab/AllVoiceLab-MCP)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `entertainment and media`, `art and culture`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `allvoicelab-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/allvoicelab-allvoicelab.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
