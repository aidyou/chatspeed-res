---
title: "提示词生成器（MCP&Agent挑战赛）"
description: "功能说明： AIGC赛道苦于自己不会写专业提示词，这个mcp使用 Qwen3 模型优化输入的提示词，使其更适合指定的 AI 图像生成模型。 部署指南 环境依赖： Node.js 18+ 或 Python 3.8+（根据实际运行环境选择） 配置说明 参考以下 JSON 配置格式（以 SSE 传输为例）： json { \"mcpServers\": { \"your-server-name\": { \"args\": [ \"mcp-remote\", \"https://phoenixdna-prompt-generator-mc"
---

# 提示词生成器（MCP&Agent挑战赛）

功能说明： AIGC赛道苦于自己不会写专业提示词，这个mcp使用 Qwen3 模型优化输入的提示词，使其更适合指定的 AI 图像生成模型。 部署指南 环境依赖： Node.js 18+ 或 Python 3.8+（根据实际运行环境选择） 配置说明 参考以下 JSON 配置格式（以 SSE 传输为例）： json { "mcpServers": { "your-server-name": { "args": [ "mcp-remote", "https://phoenixdna-prompt-generator-mc

## 功能说明：
    AIGC赛道苦于自己不会写专业提示词，这个mcp使用 Qwen3 模型优化输入的提示词，使其更适合指定的 AI 图像生成模型。

## 部署指南

### 环境依赖：
Node.js 18+ 或 Python 3.8+（根据实际运行环境选择）

### 配置说明
参考以下 JSON 配置格式（以 SSE 传输为例）：
json
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

## 使用示例

### 参数说明：
    Args:
        original_prompt (str): 用户提供的原始提示词（中/英文均可）。
        model_name (str): 用户选择的目标图像生成模型。
    
    Returns:
        str: 优化后的英文提示词，结构完整，包含主体、环境、光效、风格等要素。

### 示例：

**官方网站：** [https://www.modelscope.cn/studios/phoenixdna/prompt-generator-mcp](https://www.modelscope.cn/studios/phoenixdna/prompt-generator-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`entertainment and media`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`mcp-remote https://phoenixdna-prompt-generator-mcp.ms.show/gradio_api/mcp/sse --transport sse-only`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/phoenixdna-zlink-prompt-generator.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
