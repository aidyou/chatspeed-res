---
title: "Alibaba Cloud Model Studio Free Quota"
description: "First activation auto-grants per-model new-user free quota (usually 1M tokens per model, valid 90 days, Beijing region, no real-name needed); Qwen Code OAuth adds an independent 2,000 calls/day."
---

# Alibaba Cloud Model Studio Free Quota

First activation auto-grants per-model new-user free quota (usually 1M tokens per model, valid 90 days, Beijing region, no real-name needed); Qwen Code OAuth adds an independent 2,000 calls/day.

Alibaba Cloud Model Studio (百炼) is Alibaba Cloud's model platform for Qwen and ecosystem models. On first activation it automatically grants each model a new-user free quota (usually 1M tokens per model, valid 90 days, Beijing region only); no real-name verification is required to consume the free quota, and unverified accounts default to a hard stop (403 FreeTierOnly) once it is exhausted. Qwen Code OAuth authentication carries an independent free quota of 2,000 calls/day. The OpenAI-compatible endpoint can be connected to ChatSpeed. Free quota only covers real-time inference, not batch/tuning.

**Official site: ** [https://bailian.console.aliyun.com/](https://bailian.console.aliyun.com/)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `general`, `coding`
- Tags: `aliyun`, `bailian`, `free-quota`, `api`, `china`

## Free Usage

- Access: `api`
- Requires login: `Yes`
- Has free tier: `Yes`
- Availability: `regional`

Per-model new-user quota (usually 1M tokens/model, 90 days, Beijing region) + Qwen Code OAuth 2,000 calls/day; no real-name verification needed for the free quota. Check the official help doc for current values.

### Per-model free quota

| Model | Free quota | Rate / frequency |
| --- | --- | --- |
| New-user quota per model (qwen-plus, qwen-max, qwen3-series etc.) | Usually 1M tokens per model (independent per model) | Valid 90 days; Beijing (cn-beijing) region only |
| Qwen Code OAuth authentication | 2,000 calls / day | Independent of API-key free quota; daily |

## Registration & Limits
- Sign up: [https://bailian.console.aliyun.com/](https://bailian.console.aliyun.com/)
- Registration limit: Register an Alibaba Cloud account (phone/email) to activate the platform; free quota needs no real-name verification, but continuing on a pay-as-you-go basis requires verification and top-up. Mainland China access expected.
- Free policy doc: [https://help.aliyun.com/zh/model-studio/new-free-quota](https://help.aliyun.com/zh/model-studio/new-free-quota)

## ChatSpeed Import

This service is linked to model provider `aliyun-bailian`; import its config from the model provider list. Call entry points:
- Protocol: `openai`
- Base URL: `https://dashscope.aliyuncs.com/compatible-mode/v1`
- Logo: ![Bailian](https://img.alicdn.com/tfs/TB1_ZXuNcfpK1RjSZFOXXa6nFXa-32-32.ico)
- Docs: [https://help.aliyun.com/zh/model-studio/getting-started/what-is-model-studio](https://help.aliyun.com/zh/model-studio/getting-started/what-is-model-studio)
- Model list: [https://help.aliyun.com/zh/model-studio/models](https://help.aliyun.com/zh/model-studio/models)
- API key: [https://bailian.console.aliyun.com/?apiKey=1#/api-key](https://bailian.console.aliyun.com/?apiKey=1#/api-key)

## Data source

Resource file: `resources/free-ai/aliyun-bailian-free-quota.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
