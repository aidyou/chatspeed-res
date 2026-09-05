---
title: "Cloudflare Workers AI"
description: "Cloudflare 边缘网络上的无服务器 AI 推理，兼容 OpenAI 接口（Base URL 需带账号 ID），每日免费额度约 10,000 Neurons。"
---

# Cloudflare Workers AI

Cloudflare 边缘网络上的无服务器 AI 推理，兼容 OpenAI 接口（Base URL 需带账号 ID），每日免费额度约 10,000 Neurons。

Cloudflare Workers AI 在边缘网络提供无服务器模型推理，覆盖约 80 个模型（Llama 3.x/4、Mistral、Qwen、Gemma、GPT-OSS、DeepSeek-R1 蒸馏版、FLUX/SD 等）。OpenAI 兼容端点为 https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1，其中 {account_id} 需替换为你自己的 Cloudflare 账号 ID；鉴权使用控制台创建的 API Token。每日免费额度约 10,000 Neurons，并含各模型限速；超出免费额度部分按 Neurons 计费，可在控制台设置限额防止扣费。免费额度与限速会调整，请以官方定价页为准。

**官方网站：** [https://developers.cloudflare.com/workers-ai/](https://developers.cloudflare.com/workers-ai/)
**状态：** `review`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`general`, `coding`, `vision`
- 标签：`cloudflare`, `workers-ai`, `serverless`, `openai-compatible`

## 供应商配置

- 协议：`openai`
- Base URL：`https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1`
- 模型数量：0
- 文档：[https://developers.cloudflare.com/workers-ai/](https://developers.cloudflare.com/workers-ai/)
- 模型列表：[https://developers.cloudflare.com/workers-ai/models/](https://developers.cloudflare.com/workers-ai/models/)
- 密钥申请：[https://dash.cloudflare.com/profile/api-tokens](https://dash.cloudflare.com/profile/api-tokens)

## 数据来源

资源文件：`resources/models/cloudflare.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
