---
title: "Pollinations Free API"
description: "Open-source generative API (text/image/audio/video); the OpenAI-compatible text endpoint works without sign-up or API key for free models."
---

# Pollinations Free API

Open-source generative API (text/image/audio/video); the OpenAI-compatible text endpoint works without sign-up or API key for free models.

Pollinations is an open-source generative-AI platform exposing simple HTTP APIs for text, image, audio and video generation. The text API is OpenAI-compatible (https://text.pollinations.ai/openai) and remains free without sign-up or API key for the free model set; image generation is served at image.pollinations.ai. Some newer or higher-priority models may require account/token-based access. Rate limits are relatively loose but adjust with load, so confirm with the official repo/docs before relying on it.

**Official site: ** [https://pollinations.ai/](https://pollinations.ai/)
**Status: ** `review`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `general`, `image`
- Tags: `pollinations`, `free-api`, `no-key`, `multimodal`

## Free Usage

- Access: `api`
- Requires login: `No`
- Has free tier: `Yes`
- Availability: `global`

Free models are usable without sign-up or API key; rate limits are loose but adjust with load. Some newer models may require account/token access. Check the official repo for current limits.

### Per-model free quota

| Model | Free quota | Rate / frequency |
| --- | --- | --- |
| Free text models (OpenAI-compatible endpoint) | Free | No key needed; rate limits per official repo |
| Image generation (image.pollinations.ai) | Free | No key needed; rate limits per official repo |

## Registration & Limits
- Registration limit: No registration required for free text/image APIs; higher-priority or newer models may require account/token access per the official docs.

## ChatSpeed Import

This service includes a ChatSpeed provider config and can be imported directly. Call entry points:
- Protocol: `openai`
- Base URL: `https://text.pollinations.ai/openai`
- Logo: ![Pollinations](https://pollinations.ai/favicon-32x32.png)
- Docs: [https://github.com/pollinations/pollinations/blob/master/APIDOCS.md](https://github.com/pollinations/pollinations/blob/master/APIDOCS.md)
- Model list: [https://text.pollinations.ai/models](https://text.pollinations.ai/models)

## Data source

Resource file: `resources/free-ai/pollinations-free-api.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
