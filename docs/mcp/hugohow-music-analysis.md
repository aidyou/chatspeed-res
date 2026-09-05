---
title: "mcp-music-analysis"
description: "MCP to analyse local audio file."
---

# mcp-music-analysis

MCP to analyse local audio file.

# MCP Music Analysis

This repository contains a **Model Context Provider (MCP)** that uses MCP and [librosa](https://librosa.org/) for audio analysis on audio in local, youtube link, or audio link.

## Usage with Claude Desktop

   alt="alt text" width="40%">
   alt="alt text" width="40%">

## Installation

```bash
# Clone repository
git clone git@github.com:hugohow/mcp-music-analysis.git
cd mcp-music-analysis

# Create virtual environment and install
uv venv
source .venv/bin/activate  # On Windows: .venvScriptsactivate
uv pip install -e .
```

### Usage with Claude Desktop

#### Locate Configuration File

The configuration file location depends on your operating system:

- **macOS**:
```
  ~/Library/Application Support/Claude/claude_desktop_config.json
```

- **Windows**:
```
  %APPDATA%Claudeclaude_desktop_config.json
```

- **Linux**:
```
  ~/.config/Claude/claude_desktop_config.json
```

Add the following to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "music-analysis": {
      "command": "uvx",
      "args": ["-n", "mcp-music-analysis"]
    }
  }
}
```

## Example Prompts

Here are some sample prompts you might use in a conversational or chat-based context once the server is running. The MCP will understand these requests and execute the relevant tools:

```
Can you analyze the beat of /Users/hugohow-choong/Desktop/sample-6s.mp3?
Could you give me the duration of https://download.samplelib.com/mp3/sample-15s.mp3 ?
Please compute the MFCC for this file: /path/to/another_audio.mp3
What are the spectral centroid values for /path/to/music.wav?
I'd like to know the onset times for https://www.youtube.com/watch?v=8HFiFd9vx1c
```

## To-Do List

- [x] Add URL to audio file download
- [x] Add YouTube to audio file transformation
- [ ] Experiment with multiple Python environments (testing)
- [ ] Improve installation guide
- [ ] Integrate Whisper for lyrics
- [ ] Implement a Docker solution

## Author

Hugo How-Choong

**Official site: ** [https://github.com/hugohow/mcp-audio-analysis](https://github.com/hugohow/mcp-audio-analysis)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `files`
- Tags: `file systems`, `image and video processing`, `other`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `-n mcp-music-analysis`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/hugohow-music-analysis.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
