---
title: "Cloudflare Workers AI Free Quota"
description: "Cloudflare Workers AI grants a daily free allocation (about 10,000 Neurons/day) across ~80 models (Llama, Mistral, Qwen, Gemma, GPT-OSS, FLUX etc.); accounts are free and limits can be adjusted to avo…"
---

# Cloudflare Workers AI Free Quota

Cloudflare Workers AI grants a daily free allocation (about 10,000 Neurons/day) across ~80 models (Llama, Mistral, Qwen, Gemma, GPT-OSS, FLUX etc.); accounts are free and limits can be adjusted to avo…

Cloudflare Workers AI provides serverless inference on Cloudflare's edge network. The free tier grants a daily allocation measured in Neurons (currently about 10,000/day, per the pricing page) usable across ~80 models including Llama 3.x/4, Mistral, Qwen, Gemma, GPT-OSS, DeepSeek-R1 distills and image models (FLUX, Stable Diffusion), with per-model free rate limits (roughly 150–1,500 requests/min depending on the model). Requests beyond the free allocation are billed per Neurons unless you set limits/hard stops in the dashboard. The OpenAI-compatible endpoint URL includes your account ID, so configure it carefully in ChatSpeed. Free daily allocation and limits change; check the official pricing page.

**Official site: ** [https://developers.cloudflare.com/workers-ai/](https://developers.cloudflare.com/workers-ai/)
**Status: ** `review`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `general`, `coding`, `image`
- Tags: `cloudflare`, `workers-ai`, `free-tier`, `api`

## Free Usage

- Access: `api`
- Requires login: `Yes`
- Has free tier: `Yes`
- Availability: `global`

Daily free allocation about 10,000 Neurons/day (per official pricing); per-model free rate limits (~150–1,500 req/min). Above the allocation, usage is billed per Neurons unless limits are set.

### Per-model free quota

| Model | Free quota | Rate / frequency |
| --- | --- | --- |
| All Workers AI models (Llama 3.x/4, Mistral, Qwen, Gemma, GPT-OSS, DeepSeek-R1 distills, FLUX/SD etc.) | ~10,000 Neurons / day (free allocation) | Daily reset; per-model rate limits ~150–1,500 req/min |

## Registration & Limits
- Sign up: [https://dash.cloudflare.com/sign-up](https://dash.cloudflare.com/sign-up)
- Registration limit: Sign up with an email address; the free tier needs no credit card. Requests beyond the daily free allocation are billed, so set spending limits or hard stops in the dashboard.
- Free policy doc: [https://developers.cloudflare.com/workers-ai/platform/pricing/](https://developers.cloudflare.com/workers-ai/platform/pricing/)

## ChatSpeed Import

This service includes a ChatSpeed provider config and can be imported directly. Call entry points:
- Protocol: `openai`
- Base URL: `https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1`
- Logo: ![Cloudflare](https://www.google.com/s2/favicons?domain=cloudflare.com&sz=64)
- Docs: [https://developers.cloudflare.com/workers-ai/](https://developers.cloudflare.com/workers-ai/)
- Model list: [https://developers.cloudflare.com/workers-ai/models/](https://developers.cloudflare.com/workers-ai/models/)
- API key: [https://dash.cloudflare.com/profile/api-tokens](https://dash.cloudflare.com/profile/api-tokens)

## Data source

Resource file: `resources/free-ai/cloudflare-workers-ai-free.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
