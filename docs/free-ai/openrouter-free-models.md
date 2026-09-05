---
title: "OpenRouter Free Models"
description: "Free model variants (model IDs with the :free suffix) can be called free of charge through an OpenAI-compatible API; new accounts get 20 requests/minute and 50 requests/day, raised to 1,000 requests/d…"
---

# OpenRouter Free Models

Free model variants (model IDs with the :free suffix) can be called free of charge through an OpenAI-compatible API; new accounts get 20 requests/minute and 50 requests/day, raised to 1,000 requests/d…

OpenRouter is a model-aggregation and routing platform: one API key accesses models from many providers, and appending `:free` to a model ID enables the free variant for quick evaluation and prototyping. Free variants usually have lower rate limits than paid ones, may queue, and can hit upstream provider 429s; platform-level limits change with policy (accounts with less than $10 in lifetime purchases get 50 requests/day, raised to 1,000 after $10). The OpenAI-compatible endpoint can be connected to ChatSpeed directly.

**Official site: ** [https://openrouter.ai/docs/guides/routing/model-variants/free](https://openrouter.ai/docs/guides/routing/model-variants/free)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `general`, `coding`, `reasoning`
- Tags: `openrouter`, `free-models`, `api`

## Free Usage

- Access: `api`
- Requires login: `Yes`
- Has free tier: `Yes`
- Availability: `global`

Free variants: 20 requests/minute; accounts with less than $10 in lifetime credit purchases get up to 50 requests/day, raised to 1,000 requests/day after $10 in lifetime purchases. Limits may change; check the official rate-limit documentation.

### Per-model free quota

| Model | Free quota | Rate / frequency |
| --- | --- | --- |
| All free variants (model IDs ending in `:free`) | Free | 20 requests per minute |
| Accounts with less than $10 lifetime credit purchases | Free | Up to 50 requests per day |
| Accounts with $10+ lifetime credit purchases | Free | Up to 1,000 requests per day |

## Registration & Limits
- Sign up: [https://openrouter.ai/](https://openrouter.ai/)
- Registration limit: Sign up with email only; no credit card required. The free daily cap is low; you can raise it to 1,000 requests/day with $10+ in lifetime credit purchases (payment methods per official policy).
- Free policy doc: [https://openrouter.ai/docs/api_reference/limits](https://openrouter.ai/docs/api_reference/limits)

## ChatSpeed Import

This service includes a ChatSpeed provider config and can be imported directly. Call entry points:
- Protocol: `openai`
- Base URL: `https://openrouter.ai/api/v1`
- Logo: ![OpenRouter](https://openrouter.ai/favicon.ico)
- Docs: [https://openrouter.ai/docs](https://openrouter.ai/docs)
- Model list: [https://openrouter.ai/models](https://openrouter.ai/models)
- API key: [https://openrouter.ai/keys](https://openrouter.ai/keys)

## Data source

Resource file: `resources/free-ai/openrouter-free-models.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
