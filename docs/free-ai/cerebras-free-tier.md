---
title: "Cerebras Free Tier"
description: "Ultra-fast OpenAI-compatible inference (up to ~2,000 tokens/s) with a free tier of roughly 1M tokens/day per model (e.g. Llama 3.3 70B); no credit card required."
---

# Cerebras Free Tier

Ultra-fast OpenAI-compatible inference (up to ~2,000 tokens/s) with a free tier of roughly 1M tokens/day per model (e.g. Llama 3.3 70B); no credit card required.

Cerebras runs open LLMs on wafer-scale chips with very high throughput via an OpenAI-compatible API (base https://api.cerebras.ai/v1). The free tier provides roughly 1M tokens/day per model with per-model RPM/TPM/TPD limits (values per the official rate-limits doc); hitting a limit returns 429. No credit card is required; the paid Developer tier offers about 10x higher limits.

**Official site: ** [https://www.cerebras.ai/](https://www.cerebras.ai/)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `general`, `coding`
- Tags: `cerebras`, `free-tier`, `api`, `fast-inference`

## Free Usage

- Access: `api`
- Requires login: `Yes`
- Has free tier: `Yes`
- Availability: `global`

Free tier: roughly 1M tokens/day per model (plus per-model RPM/TPM limits); no credit card required. Check the official rate-limits doc for current values.

### Per-model free quota

| Model | Free quota | Rate / frequency |
| --- | --- | --- |
| Free-tier models (e.g. Llama 3.3 70B, Qwen3 and other open models) | Free, ~1M tokens/day per model | RPM/TPM/TPD per model; see official doc |

## Registration & Limits
- Sign up: [https://cloud.cerebras.ai/](https://cloud.cerebras.ai/)
- Registration limit: Sign up with email; no credit card required. Rate limits are per organization/API key and model.
- Free policy doc: [https://inference-docs.cerebras.ai/support/rate-limits](https://inference-docs.cerebras.ai/support/rate-limits)

## ChatSpeed Import

This service includes a ChatSpeed provider config and can be imported directly. Call entry points:
- Protocol: `openai`
- Base URL: `https://api.cerebras.ai/v1`
- Logo: ![Cerebras](https://www.google.com/s2/favicons?domain=cerebras.ai&sz=64)
- Docs: [https://inference-docs.cerebras.ai/](https://inference-docs.cerebras.ai/)
- Model list: [https://inference-docs.cerebras.ai/](https://inference-docs.cerebras.ai/)
- API key: [https://cloud.cerebras.ai/](https://cloud.cerebras.ai/)

## Data source

Resource file: `resources/free-ai/cerebras-free-tier.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
