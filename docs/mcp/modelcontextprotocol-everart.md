---
title: "everart"
description: "Image generation server for Claude Desktop using EverArt's API."
---

# everart

Image generation server for Claude Desktop using EverArt's API.

# EverArt MCP Server

Image generation server for Claude Desktop using EverArt's API.

## Install
```bash
npm install
export EVERART_API_KEY=your_key_here
```

## Config
Add to Claude Desktop config:

### Docker
```json
{
  "mcpServers": {
    "everart": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "-e", "EVERART_API_KEY", "mcp/everart"],
      "env": {
        "EVERART_API_KEY": "your_key_here"
      }
    }
  }
}
```

### NPX

```json
{
  "mcpServers": {
    "everart": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-everart"],
      "env": {
        "EVERART_API_KEY": "your_key_here"
      }
    }
  }
}
```

## Tools

### generate_image
Generates images with multiple model options. Opens result in browser and returns URL.

Parameters:
```typescript
{
  prompt: string,       // Image description
  model?: string,       // Model ID (default: "207910310772879360")
  image_count?: number  // Number of images (default: 1)
}
```

Models:
- 5000: FLUX1.1 (standard)
- 9000: FLUX1.1-ultra
- 6000: SD3.5
- 7000: Recraft-Real
- 8000: Recraft-Vector

All images generated at 1024x1024.

Sample usage:
```javascript
const result = await client.callTool({
  name: "generate_image",
  arguments: {
    prompt: "A cat sitting elegantly",
    model: "7000",
    image_count: 1
  }
});
```

Response format:
```
Image generated successfully!
The image has been opened in your default browser.

Generation details:
- Model: 7000
- Prompt: "A cat sitting elegantly"
- Image URL: https://storage.googleapis.com/...

You can also click the URL above to view the image again.
```

## Building w/ Docker

```sh
docker build -t mcp/everart -f src/everart/Dockerfile . 
```

**Official site: ** [https://github.com/modelcontextprotocol/servers/tree/main/src/everart](https://github.com/modelcontextprotocol/servers/tree/main/src/everart)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `art and culture`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @modelcontextprotocol/server-everart`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/modelcontextprotocol-everart.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
