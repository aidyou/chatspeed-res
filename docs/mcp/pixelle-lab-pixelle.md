---
title: "Pixelle_MCP"
description: "Pixelle MCP - an all-modal fusion agent framework. An AIGC solution based on the MCP protocol that zero-code converts ComfyUI workflows into MCP Tools, joining forces between LLMs and ComfyUI. Officia…"
---

# Pixelle_MCP

Pixelle MCP - an all-modal fusion agent framework. An AIGC solution based on the MCP protocol that zero-code converts ComfyUI workflows into MCP Tools, joining forces between LLMs and ComfyUI. Officia…

# Pixelle MCP - All-Modal Fusion Agent Framework

An AIGC solution based on the MCP protocol that zero-code converts ComfyUI workflows into MCP Tools, joining forces between LLMs and ComfyUI.

### Official site: https://github.com/AIDC-AI/Pixelle-MCP

---

## Introduction

**Pixelle** is an open-source all-modal agent framework that seamlessly integrates ComfyUI with large language models (LLMs) through the **Model Context Protocol (MCP)**. It allows users to convert complex ComfyUI workflows into callable MCP tools **without any code**, enabling LLMs to perform various AIGC tasks including text, image, sound/speech, and video.

Pixelle is built on the extensible ComfyUI ecosystem and adopts a robust client-server architecture, providing a flexible and unified solution for developing, deploying, and leveraging multimodal AI generation capabilities.

---

## Key Features

- **All-modal support**: supports the conversion and generation of TISV (Text, Image, Sound/Speech, Video) across all modalities
- **ComfyUI ecosystem**: built on [ComfyUI](https://github.com/comfyanonymous/ComfyUI), compatible with all capabilities of its open ecosystem
- **Zero-code development**: an innovative "Workflow-as-MCP-Tool" approach that dynamically adds new tools with 0 code
- **MCP Server**: server-side based on the [MCP protocol](https://modelcontextprotocol.io/introduction), compatible with any MCP client (such as Cursor, Claude Desktop, etc.)
- **MCP Client**: client-side built on the [Chainlit](https://github.com/Chainlit/chainlit) framework, supporting rich interactive controls and integration with multiple MCP Servers
- **Flexible deployment**: can deploy the Server (server only), the Client (client only), or both together
- **Unified configuration**: YAML configuration manages all services in one file
- **Multiple LLM support**: supports mainstream LLMs including OpenAI, Ollama, Gemini, DeepSeek, Claude, Qwen, etc.

---

## Demo

| Demo name | Demo | Brief description |
| ----------------- | ---------------------------------------------------------------- | ----------------------------- |
| Mischievous Pixelle | [demo link](https://demo.pixelle.ai/?starter=wan) | Coherent story reasoning (reasoning and consistency capabilities) |
| Silent Route | [demo link](https://demo.pixelle.ai/?starter=silent-route) | Style-reference-based video re-rendering |
| Concept Car Promo Video | [demo link](http://demo.pixelle.ai/?starter=car) | Prototype concept design with Flux-Krea (fast compatibility with the latest model capabilities) |

> Each demo showcases all-modal agent capabilities in different scenarios; feel free to click and explore more features!

---

## Project Structure

| Module | Description |
| ------------- | --------------------------------------------------------------- |
| `mcp-base` | Basic services providing file storage and common service capabilities |
| `mcp-client` | MCP client, a web interface built on Chainlit |
| `mcp-server` | MCP server integrating various AIGC tools and services |

---

## Use Cases

- General multimodal agent development
- Zero-code customization of AIGC workflows
- Enhancing LLM tool-calling capabilities
- Flexible deployment of enterprise-level AI services

---

> Welcome to Star, Fork, submit Issues or PRs to help improve Pixelle MCP!

**Official site: ** [https://github.com/AIDC-AI/Pixelle-MCP](https://github.com/AIDC-AI/Pixelle-MCP)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `entertainment and media`, `art and culture`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `mcp-pixellab --secret=your-pixellab-secret-here`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/pixelle-lab-pixelle.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
