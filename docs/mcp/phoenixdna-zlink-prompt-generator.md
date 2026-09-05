---
title: "Zlink-prompt-generator"
description: "功能说明： AIGC赛道苦于自己不会写专业提示词，这个mcp使用 Qwen3 模型优化输入的提示词，使其更适合指定的 AI 图像生成模型。 部署指南 环境依赖： ​​Node.js​​ 18+ 或 ​​Python​​ 3.8+（根据实际运行环境选择） 配置说明 参考以下 JSON 配置格式（以 SSE 传输为例）： json { \"mcpServers\": { \"your-server-name…"
---

# Zlink-prompt-generator

功能说明： AIGC赛道苦于自己不会写专业提示词，这个mcp使用 Qwen3 模型优化输入的提示词，使其更适合指定的 AI 图像生成模型。 部署指南 环境依赖： ​​Node.js​​ 18+ 或 ​​Python​​ 3.8+（根据实际运行环境选择） 配置说明 参考以下 JSON 配置格式（以 SSE 传输为例）： json { "mcpServers": { "your-server-name…

## 功能说明：
    AIGC赛道苦于自己不会写专业提示词，这个mcp使用 Qwen3 模型优化输入的提示词，使其更适合指定的 AI 图像生成模型。

## 部署指南

### 环境依赖：
​​Node.js​​ 18+ 或 ​​Python​​ 3.8+（根据实际运行环境选择）


### 配置说明
参考以下 JSON 配置格式（以 SSE 传输为例）：
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
## 使用示例

### 参数说明：
    Args:
        original_prompt (str): 用户提供的原始提示词（中/英文均可）。
        model_name (str): 用户选择的目标图像生成模型。
    
    Returns:
        str: 优化后的英文提示词，结构完整，包含主体、环境、光效、风格等要素。

### Example：

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
