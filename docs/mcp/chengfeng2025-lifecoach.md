---
title: "lifecoach"
description: "Life Coach Agent, Exploring Life Decisions"
---

# lifecoach

Life Coach Agent, Exploring Life Decisions

# Life Coach MCP Project

An intelligent life coach system based on the Model Context Protocol (MCP), providing professional prompts and intelligent conversation features from 12 well-known life coaches.

## Features

- **Intelligent life coach conversations** - professional advice from 12 well-known life coaches
- **Multi-perspective thinking** - supports multiple coaches analyzing a problem simultaneously
- **Dynamic coach selection** - intelligently matches the most suitable coach based on the question type

## Available Coaches

| Coach | Specialty | Use cases |
|------|----------|----------|
| Li Xiaolai | Applied cognitive science | personal growth, learning methods |
| Socrates | Socratic dialogue | critical thinking, philosophical inquiry |
| Jay Forrester | System dynamics | systems thinking, feedback mechanisms |
| Mirror Me | Personal memory analysis | self-dialogue, reflection |
| God of Dialectics | Reverse thinking | logical analysis, finding flaws |
| David Hume | Truth interrogation | deep thinking, critical reasoning |
| Archaeologist of Problems | Uncovering problem essences | complex problem analysis |
| The Alchemist | Emotional transformation | handling negative emotions |
| Steve Jobs | Product thinking | user experience, perfectionism |
| Charlie Munger | Multidisciplinary thinking | investing mindset, wise decisions |
| CBT Psychologist | Cognitive behavioral therapy | mental health, emotional regulation |
| Elon Musk | First principles | innovative thinking, disruptive ideas |

## Quick Start

### 1. Installation

**Install via npm (recommended)**
```bash
npm install -g lifecoach-mcp-server
```

**Install from source**
```bash
cd mcp-server
npm install
npm start
```

### 2. Configure Claude Desktop

Add the MCP server in Claude Desktop settings:

**Global install configuration:**
```json
{
  "mcpServers": {
    "lifecoach": {
      "command": "lifecoach-mcp-server"
    }
  }
}
```

**Config file locations:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%/Claude/claude_desktop_config.json`

### 3. Start using it

In Claude Desktop, say:
- "Start life coach"
- "I want advice from Li Xiaolai"
- "Search for coaches related to thinking"

## Project Structure

```
lifecoach-mcp/
├── mcp-server/           # MCP server (npm: lifecoach-mcp-server)
├── worker/              # Cloudflare Worker API
├── config/              # Configuration docs
└── README.md           # Project documentation
```

## Technical Architecture

```
User -> Claude Desktop -> MCP Server -> Cloudflare Worker -> Supabase
```

## API Tools

### start_lifecoach
Starts a life coach conversation mode

### get_lifecoach
Gets information about a specific coach
```json
{
  "name": "get_lifecoach",
  "arguments": {
    "name": "Li Xiaolai"
  }
}
```

### list_lifecoaches
Gets the list of all coaches

### search_lifecoach
Searches for a matching coach
```json
{
  "name": "search_lifecoach",
  "arguments": {
    "keyword": "thinking"
  }
}
```

## License

MIT License

**Official site: ** [https://www.npmjs.com/package/lifecoach-mcp-server](https://www.npmjs.com/package/lifecoach-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `communication`
- Tags: `communication`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y lifecoach-mcp-server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/chengfeng2025-lifecoach.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
