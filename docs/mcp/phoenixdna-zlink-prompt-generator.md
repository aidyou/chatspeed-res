---
title: "Zlink-prompt-generator"
description: "Features: AIGC creators often struggle with writing professional prompts. This MCP uses the Qwen3 model to optimize input prompts, making them more suitable for the specified AI image generation model…"
---

# Zlink-prompt-generator

Features: AIGC creators often struggle with writing professional prompts. This MCP uses the Qwen3 model to optimize input prompts, making them more suitable for the specified AI image generation model…

## Features:
    AIGC creators often struggle with writing professional prompts. This MCP uses the Qwen3 model to optimize input prompts, making them more suitable for the specified AI image generation model.

## Deployment Guide

### Environment dependencies:
Node.js 18+ or Python 3.8+ (choose according to your runtime environment)

### Configuration
Refer to the following JSON configuration format (SSE transport as an example):
```json
{
  "mcpServers": {
    "your-server-name": {
      "args": [
        "mcp-remote",
        "https://phoenixdna-prompt-generator-mcp.ms.show/gradio_api/mcp/sse",
        "--transport",
        "sse-only"
      ],
      "command": "npx"
    }
  }
}
```

## Usage Example

### Parameters:
    Args:
        original_prompt (str): the user's original prompt (Chinese or English).
        model_name (str): the target image generation model selected by the user.

    Returns:
        str: an optimized English prompt with a complete structure, covering subject, environment, lighting, style, and other elements.

### Example:

**Official site: ** [https://www.modelscope.cn/studios/phoenixdna/prompt-generator-mcp](https://www.modelscope.cn/studios/phoenixdna/prompt-generator-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `entertainment and media`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `mcp-remote https://phoenixdna-prompt-generator-mcp.ms.show/gradio_api/mcp/sse --transport sse-only`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/phoenixdna-zlink-prompt-generator.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
