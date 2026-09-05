---
title: "Groq"
description: "OpenAI-compatible ultra-fast inference with a generous free tier (e.g. Llama 3.1 8B: 30 RPM / 14,400 RPD), no credit card required."
---

# Groq

OpenAI-compatible ultra-fast inference with a generous free tier (e.g. Llama 3.1 8B: 30 RPM / 14,400 RPD), no credit card required.

Groq runs LLMs on its LPU hardware at very high speeds (500+ tokens/s on some models) and offers an OpenAI-compatible API. The free tier is permanent (rate limits per organization, model by model, e.g. llama-3.1-8b-instant: 30 RPM / 14,400 RPD / 6000 TPM / 500K TPD) and needs no credit card; hitting a limit returns 429 with X-RateLimit headers. Free models include Llama 3.1/3.3/4 Scout, Kimi K2, Qwen3 32B, GPT-OSS 120B/20B and Whisper speech-to-text.

**Official site: ** [https://groq.com/](https://groq.com/)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `general`, `coding`, `reasoning`
- Tags: `groq`, `openai-compatible`, `free-tier`, `fast-inference`

## Provider Configuration

- Protocol: `openai`
- Base URL: `https://api.groq.com/openai/v1`
- Model count: 0
- Docs: [https://console.groq.com/docs/overview](https://console.groq.com/docs/overview)
- Model list: [https://console.groq.com/docs/models](https://console.groq.com/docs/models)
- API key: [https://console.groq.com/keys](https://console.groq.com/keys)

## Data source

Resource file: `resources/models/groq.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
