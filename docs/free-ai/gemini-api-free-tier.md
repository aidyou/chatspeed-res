---
title: "Google Gemini API Free Tier"
description: "Free tier covers Flash / Flash-Lite family models (e.g. Gemini 2.5 Flash, Gemini 2.5 Flash-Lite, newer 3.x Flash Lite) with free input/output tokens; quotas are relatively generous for daily use and s…"
---

# Google Gemini API Free Tier

Free tier covers Flash / Flash-Lite family models (e.g. Gemini 2.5 Flash, Gemini 2.5 Flash-Lite, newer 3.x Flash Lite) with free input/output tokens; quotas are relatively generous for daily use and s…

Google's Gemini API provides a free tier for developers and small projects. Free-eligible models are the Flash and Flash-Lite families (e.g. Gemini 2.5 Flash, Gemini 2.5 Flash-Lite, newer 3.x Flash Lite variants) with free input/output tokens and relatively generous RPM/RPD quotas, which Google no longer fully publishes per model — check your effective limits in Google AI Studio, as they change over time (free-tier cuts happened historically). The free tier needs a Google account but no billing/credit card; rate limits apply per project. The API supports both the native protocol and an OpenAI-compatible endpoint.

**Official site: ** [https://ai.google.dev/gemini-api/docs/pricing](https://ai.google.dev/gemini-api/docs/pricing)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `general`, `coding`, `reasoning`
- Tags: `google`, `gemini`, `free-tier`, `api`

## Free Usage

- Access: `api`
- Requires login: `Yes`
- Has free tier: `Yes`
- Availability: `global`

Free tier covers Flash/Flash-Lite models with free input/output tokens; per-model RPM/RPD quotas are shown and adjusted in Google AI Studio (not fully published). No billing/credit card needed for the free tier.

### Per-model free quota

| Model | Free quota | Rate / frequency |
| --- | --- | --- |
| Gemini Flash family (e.g. Gemini 2.5 Flash, newer 3.x Flash) | Free input & output tokens | RPM/RPD per AI Studio; generous for daily use |
| Gemini Flash-Lite family (e.g. Gemini 2.5 Flash-Lite, newer 3.x Flash Lite) | Free input & output tokens | Higher quotas than Flash; check AI Studio |
| Other models (Pro family, previews etc.) | Free-tier eligibility varies | Check AI Studio |

## Registration & Limits
- Sign up: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
- Registration limit: Sign up with a Google account; the free tier needs no credit card. Availability is subject to Google's supported-regions policy.
- Free policy doc: [https://ai.google.dev/gemini-api/docs/rate-limits](https://ai.google.dev/gemini-api/docs/rate-limits)

## ChatSpeed Import

This service includes a ChatSpeed provider config and can be imported directly. Call entry points:
- Protocol: `gemini`
- Base URL: `https://generativelanguage.googleapis.com/v1beta`
- Logo: ![Gemini](https://www.gstatic.com/lamda/images/favicon_v1_150160cddff7f294ce30.svg)
- Docs: [https://ai.google.dev/docs](https://ai.google.dev/docs)
- Model list: [https://ai.google.dev/models/gemini](https://ai.google.dev/models/gemini)
- API key: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

## Data source

Resource file: `resources/free-ai/gemini-api-free-tier.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
