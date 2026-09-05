---
title: "Groq Free API"
description: "Permanent free tier, no credit card required: e.g. Llama 3.1 8B gets 30 RPM / 14,400 requests per day; Llama 3.3 70B, Llama 4 Scout, GPT-OSS 120B get 30 RPM / 1,000 RPD; Kimi K2/Qwen3 32B get 60 RPM /…"
---

# Groq Free API

Permanent free tier, no credit card required: e.g. Llama 3.1 8B gets 30 RPM / 14,400 requests per day; Llama 3.3 70B, Llama 4 Scout, GPT-OSS 120B get 30 RPM / 1,000 RPD; Kimi K2/Qwen3 32B get 60 RPM /…

Groq provides very fast inference (500+ tokens/s on some models) via an OpenAI-compatible API with a permanent free tier. Rate limits apply per organization and per model (see the quotas rows); they cover RPM, RPD, TPM and TPD, and the first one hit triggers 429 with X-RateLimit headers. No credit card is required. Free models include the Llama family, Kimi K2, Qwen3 32B, GPT-OSS 120B/20B and Whisper speech-to-text. Values change; check console.groq.com/docs/rate-limits for the current table.

**Official site: ** [https://groq.com/](https://groq.com/)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `general`, `coding`, `reasoning`
- Tags: `groq`, `free-tier`, `api`, `fast-inference`

## Free Usage

- Access: `api`
- Requires login: `Yes`
- Has free tier: `Yes`
- Availability: `global`

Free tier with per-model limits (RPM/RPD/TPM/TPD); e.g. llama-3.1-8b-instant: 30 RPM / 14,400 RPD / 6,000 TPM / 500K TPD. No credit card required. Check the official rate-limits table for current values.

### Per-model free quota

| Model | Free quota | Rate / frequency |
| --- | --- | --- |
| llama-3.1-8b-instant | Free | 30 RPM / 14,400 RPD / 6,000 TPM / 500K TPD |
| llama-3.3-70b-versatile, Llama 4 Scout, gpt-oss-120b/20b | Free | 30 RPM / 1,000 RPD (TPM 6,000–30,000 / TPD 100K–500K) |
| kimi-k2-instruct, qwen3-32b | Free | 60 RPM / 1,000 RPD |
| whisper-large-v3 / whisper-large-v3-turbo (speech-to-text) | Free | 20 RPM / 2,000 RPD |

## Registration & Limits
- Sign up: [https://console.groq.com/](https://console.groq.com/)
- Registration limit: Sign up with email or Google account; no credit card required. Rate limits are per organization, not per API key.
- Free policy doc: [https://console.groq.com/docs/rate-limits](https://console.groq.com/docs/rate-limits)

## ChatSpeed Import

This service is linked to model provider `groq`; import its config from the model provider list. Call entry points:
- Protocol: `openai`
- Base URL: `https://api.groq.com/openai/v1`
- Logo: ![Groq](https://www.google.com/s2/favicons?domain=groq.com&sz=64)
- Docs: [https://console.groq.com/docs/overview](https://console.groq.com/docs/overview)
- Model list: [https://console.groq.com/docs/models](https://console.groq.com/docs/models)
- API key: [https://console.groq.com/keys](https://console.groq.com/keys)

## Data source

Resource file: `resources/free-ai/groq-free-api.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
