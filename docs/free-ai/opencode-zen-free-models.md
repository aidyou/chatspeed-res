---
title: "OpenCode Zen Free Models"
description: "Inside the opencode coding agent, limited-time free models (MiMo-V2.5 Free, Big Pickle, Nemotron 3 Ultra Free, etc.) are usable after signing in, without adding billing details."
---

# OpenCode Zen Free Models

Inside the opencode coding agent, limited-time free models (MiMo-V2.5 Free, Big Pickle, Nemotron 3 Ultra Free, etc.) are usable after signing in, without adding billing details.

OpenCode Zen is the AI gateway maintained by the OpenCode team (SST), used inside the opencode coding agent (TUI / CLI): sign in, run /connect with your Zen API key, then /models to pick a model. A set of models is currently free for a limited time (MiMo-V2.5 Free, Big Pickle, Nemotron 3 Ultra Free, Nemotron 3.5 Lightning Free, Ling 3.0 Flash Fin Free, Muse Spark 1.2 Contributor Free) without billing details; paid models are metered per token (auto-recharge defaults to $20 when balance < $5). OpenAI-compatible endpoints are exposed at https://opencode.ai/zen/v1, so it can also be configured in ChatSpeed. The free list rotates frequently; check the official docs.

**Official site: ** [https://opencode.ai/docs/zen/](https://opencode.ai/docs/zen/)
**Status: ** `review`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `coding`
- Tags: `opencode`, `zen`, `free-models`, `coding`, `api`

## Free Usage

- Access: `api`
- Requires login: `Yes`
- Has free tier: `Yes`
- Availability: `global`

A set of models is free for a limited time (MiMo-V2.5 Free, Big Pickle, Nemotron 3 Ultra Free etc.); no billing details needed for free models. The list rotates; check the official docs.

### Per-model free quota

| Model | Free quota | Rate / frequency |
| --- | --- | --- |
| MiMo-V2.5 Free / Big Pickle / Nemotron 3 Ultra Free / Nemotron 3.5 Lightning Free / Ling 3.0 Flash Fin Free / Muse Spark 1.2 Contributor Free (current list) | Free | Limited-time free; list rotates, check official docs |

## Registration & Limits
- Sign up: [https://opencode.ai/zen](https://opencode.ai/zen)
- Registration limit: Sign up/connect with a Zen account inside opencode (or via the Zen website); free models need no billing details, paid models require adding billing (auto-recharge default $20).
- Free policy doc: [https://opencode.ai/docs/zen/](https://opencode.ai/docs/zen/)

## ChatSpeed Import

This service is linked to model provider `opencode-zen`; import its config from the model provider list. Call entry points:
- Protocol: `openai`
- Base URL: `https://opencode.ai/zen/v1`
- Logo: ![OpenCode Zen](https://www.google.com/s2/favicons?domain=opencode.ai&sz=64)
- Docs: [https://opencode.ai/docs/zen/](https://opencode.ai/docs/zen/)
- Model list: [https://opencode.ai/zen/v1/models](https://opencode.ai/zen/v1/models)
- API key: [https://opencode.ai/zen](https://opencode.ai/zen)

## Data source

Resource file: `resources/free-ai/opencode-zen-free-models.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
