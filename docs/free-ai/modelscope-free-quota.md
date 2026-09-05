---
title: "ModelScope Free Inference Quota"
description: "Free sign-up; after linking an Alibaba Cloud account and completing real-name verification, each account gets 2,000 free API-Inference calls per day in total, with a per-model cap of usually 500 calls…"
---

# ModelScope Free Inference Quota

Free sign-up; after linking an Alibaba Cloud account and completing real-name verification, each account gets 2,000 free API-Inference calls per day in total, with a per-model cap of usually 500 calls…

ModelScope (魔搭) is Alibaba's model community and hosted-inference platform, providing free API-Inference for 60,000+ models (Qwen, DeepSeek, Tongyi and more) plus image-generation capabilities. The API is OpenAI-compatible and also offers an Anthropic-compatible endpoint (used by Claude Code style tools), which suits users who want to evaluate popular open models over an API and connect the provider to ChatSpeed. The currently callable (free) models can be listed through the OpenAI-compatible endpoint `GET /v1/models`; models returned there are callable under the free quota. The free quota is stable, but popular models occasionally get removed or adjusted, and the official side does not publish a per-model quota table — confirm with the official limits document and model pages before relying on it. Note: calls fail with 401 until the account is linked, and the free quota resets per calendar day.

**Official site: ** [https://modelscope.cn/docs](https://modelscope.cn/docs)
**Status: ** `review`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `general`, `coding`, `reasoning`
- Tags: `modelscope`, `free-quota`, `api`, `china`

## Free Usage

- Access: `api`
- Requires login: `Yes`
- Has free tier: `Yes`
- Availability: `regional`

After sign-up, Alibaba Cloud account linking and real-name verification: 2,000 API-Inference calls/day in total; a single model is usually capped at 500 calls/day, and some large models are currently capped at 200 calls/day (community-reported; the official side does not publish a per-model table). The callable model list is available via `GET /v1/models`. Limits may be adjusted dynamically; follow the official limits documentation.

### Per-model free quota

| Model | Free quota | Rate / frequency |
| --- | --- | --- |
| All models (API-Inference, daily total) | 2,000 calls / day in total | Shared by all models per day |
| Single general model (e.g. Qwen series) | Up to 500 calls / day per model | Per model per day |
| Large models such as deepseek-ai/DeepSeek-R1-0528, DeepSeek-V3.1 | 200 calls / day per model (current) | Per model per day; may change dynamically |

## Registration & Limits
- Sign up: [https://modelscope.cn/](https://modelscope.cn/)
- Registration limit: Sign up with a phone number/email, then link an Alibaba Cloud account and complete Alibaba Cloud real-name verification before the API works; no credit card is required. Unlinked or unverified accounts receive 401 errors from the API.
- Free policy doc: [https://modelscope.cn/docs/model-service/API-Inference/limits](https://modelscope.cn/docs/model-service/API-Inference/limits)

## ChatSpeed Import

This service includes a ChatSpeed provider config and can be imported directly. Call entry points:
- Protocol: `openai`
- Base URL: `https://api-inference.modelscope.cn/v1`
- Logo: ![ModelScope](https://g.alicdn.com/sail-web/maas/2.7.13/favicon/128.ico)
- Docs: [https://modelscope.cn/docs/home](https://modelscope.cn/docs/home)
- Model list: [https://modelscope.cn/models](https://modelscope.cn/models)
- API key: [https://modelscope.cn/my/myaccesstoken](https://modelscope.cn/my/myaccesstoken)

## Data source

Resource file: `resources/free-ai/modelscope-free-quota.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
