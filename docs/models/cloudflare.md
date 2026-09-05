---
title: "Cloudflare Workers AI"
description: "Serverless AI inference on Cloudflare's edge network, OpenAI-compatible (base URL contains your account ID), with a daily free allocation of about 10,000 Neurons."
---

# Cloudflare Workers AI

Serverless AI inference on Cloudflare's edge network, OpenAI-compatible (base URL contains your account ID), with a daily free allocation of about 10,000 Neurons.

Cloudflare Workers AI provides serverless model inference on the edge network, covering about 80 models (Llama 3.x/4, Mistral, Qwen, Gemma, GPT-OSS, DeepSeek-R1 distills, FLUX/SD etc.). The OpenAI-compatible endpoint is https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1 where {account_id} must be replaced with your own Cloudflare account ID; authentication uses an API token from the Cloudflare dashboard. A daily free allocation of about 10,000 Neurons applies, with per-model rate limits; usage beyond the free allocation is billed per Neurons unless you set limits in the dashboard. Free allocation and limits change; check the official pricing page.

**Official site: ** [https://developers.cloudflare.com/workers-ai/](https://developers.cloudflare.com/workers-ai/)
**Status: ** `review`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `general`, `coding`, `vision`
- Tags: `cloudflare`, `workers-ai`, `serverless`, `openai-compatible`

## Provider Configuration

- Protocol: `openai`
- Base URL: `https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1`
- Model count: 0
- Docs: [https://developers.cloudflare.com/workers-ai/](https://developers.cloudflare.com/workers-ai/)
- Model list: [https://developers.cloudflare.com/workers-ai/models/](https://developers.cloudflare.com/workers-ai/models/)
- API key: [https://dash.cloudflare.com/profile/api-tokens](https://dash.cloudflare.com/profile/api-tokens)

## Data source

Resource file: `resources/models/cloudflare.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
