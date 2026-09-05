---
title: "NVIDIA NIM APIs"
description: "Sign up a free NVIDIA developer account and create an API key (nvapi-...) without a credit card to call hosted model endpoints; the common limit is about 40 requests per minute, intended for developme…"
---

# NVIDIA NIM APIs

Sign up a free NVIDIA developer account and create an API key (nvapi-...) without a credit card to call hosted model endpoints; the common limit is about 40 requests per minute, intended for developme…

NVIDIA NIM is NVIDIA's hosted (serverless) inference platform on build.nvidia.com, aggregating popular models such as DeepSeek, Qwen3-Coder, Kimi K2, MiniMax M2, Mistral and Devstral, plus some image-generation models (e.g. FLUX.1-dev). You can join the NVIDIA Developer Program for free and create an OpenAI-compatible API key; the free tier is positioned as a trial-style service for development and prototyping, and per-model free quotas and rate limits (commonly around 40 requests/minute) are displayed on each model page. The free tier is not for production reliance; for higher throughput you can request an increase or move to a paid NIM plan.

**Official site: ** [https://build.nvidia.com/explore/discover](https://build.nvidia.com/explore/discover)
**Status: ** `review`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `general`, `coding`, `reasoning`
- Tags: `nvidia`, `nim`, `free-tier`, `api`

## Free Usage

- Access: `api`
- Requires login: `Yes`
- Has free tier: `Yes`
- Availability: `global`

Free API credits are granted on sign-up (commonly reported as around 1,000 credits, in 'credits' units shown per model page); text models are commonly limited to about 40 requests per minute. Quotas and rate limits vary by account, model and current load; check the official model page.

### Per-model free quota

| Model | Free quota | Rate / frequency |
| --- | --- | --- |
| Most text models (e.g. DeepSeek V3.2/R1, Qwen3-Coder 480B, Kimi K2, MiniMax M2, Mistral, Devstral) | Free (credits-based; commonly ~1,000 on sign-up) | ~40 requests per minute (varies by model and load) |
| Some image-generation models (e.g. FLUX.1-dev) | Free, e.g. 25 requests (recent example) | One-time grant; check the current model page |

## Registration & Limits
- Sign up: [https://build.nvidia.com/](https://build.nvidia.com/)
- Registration limit: Email sign-up works (e.g. QQ Mail verified OK). For SMS verification, mainland China (+86) numbers never receive the code (confirmed by tests: one China Unicom and one China Telecom number both failed), while overseas numbers receive it fine (UK numbers verified working). Use an overseas number to complete registration/verification. No credit card required; the API key (nvapi- prefix) is shown only once at creation, so save it immediately.

## ChatSpeed Import

This service is linked to model provider `nvidia-nim`; import its config from the model provider list. Call entry points:
- Protocol: `openai`
- Base URL: `https://integrate.api.nvidia.com/v1`
- Logo: ![NVIDIA NIM](https://build.nvidia.com/favicon.ico)
- Docs: [https://docs.api.nvidia.com/nim/reference/llm-apis](https://docs.api.nvidia.com/nim/reference/llm-apis)
- Model list: [https://build.nvidia.com/models](https://build.nvidia.com/models)
- API key: [https://build.nvidia.com/settings/api-keys](https://build.nvidia.com/settings/api-keys)

## Data source

Resource file: `resources/free-ai/nvidia-nim-free-tier.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
