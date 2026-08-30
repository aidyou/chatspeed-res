---
title: "Cloudflare Workers AI 免费额度"
description: "Cloudflare Workers AI 提供每日免费额度（约 10,000 Neurons/天），覆盖约 80 个模型（Llama、Mistral、Qwen、Gemma、GPT-OSS、FLUX 等）；注册免费，可设置限额防止超出计费。"
---

# Cloudflare Workers AI 免费额度

Cloudflare Workers AI 提供每日免费额度（约 10,000 Neurons/天），覆盖约 80 个模型（Llama、Mistral、Qwen、Gemma、GPT-OSS、FLUX 等）；注册免费，可设置限额防止超出计费。

Cloudflare Workers AI 在 Cloudflare 边缘网络提供无服务器推理。免费层按 Neurons 计量每日免费额度（当前约 10,000 Neurons/天，见官方定价页），可用于约 80 个模型，包括 Llama 3.x/4、Mistral、Qwen、Gemma、GPT-OSS、DeepSeek-R1 蒸馏版以及图像模型（FLUX、Stable Diffusion），各模型另有免费层限速（视模型约 150–1,500 次/分钟）。超出免费额度的请求按 Neurons 计费，可在控制台设置限额或硬停避免意外扣费。OpenAI 兼容端点 URL 中需要带账号 ID，在 ChatSpeed 中配置时需注意。每日免费额度与限速会调整，请以官方定价页为准。

**官方网站：** [https://developers.cloudflare.com/workers-ai/](https://developers.cloudflare.com/workers-ai/)
**状态：** `review`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`general`, `coding`, `image`
- 标签：`cloudflare`, `workers-ai`, `free-tier`, `api`

## 免费使用说明

- 访问方式：`api`
- 是否需要登录：`是`
- 是否有免费层：`是`
- 可用区域：`global`

每日免费额度约 10,000 Neurons/天（见官方定价）；各模型另有免费层限速（约 150–1,500 次/分钟）。超出部分按 Neurons 计费，可设置限额防止扣费。

### 分模型免费额度明细

| 模型 | 免费额度 | 频率与限速 |
| --- | --- | --- |
| Workers AI 全部模型（Llama 3.x/4、Mistral、Qwen、Gemma、GPT-OSS、DeepSeek-R1 蒸馏版、FLUX/SD 等） | 约 10,000 Neurons/天（免费配额） | 每日刷新；各模型限速约 150–1,500 次/分钟 |

## 注册与限制
- 注册入口：[https://dash.cloudflare.com/sign-up](https://dash.cloudflare.com/sign-up)
- 注册限制：邮箱注册 Cloudflare 账号即可，免费层无需信用卡；超出每日免费额度的请求会产生费用，建议在控制台设置限额或用完即停。
- 免费政策文档：[https://developers.cloudflare.com/workers-ai/platform/pricing/](https://developers.cloudflare.com/workers-ai/platform/pricing/)

## ChatSpeed 导入

该服务关联模型供应商 `cloudflare`，可从模型供应商列表导入配置，调用入口如下：
- 协议：`openai`
- Base URL：`https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1`
- Logo：![Cloudflare](https://www.google.com/s2/favicons?domain=cloudflare.com&sz=64)
- 官方文档：[https://developers.cloudflare.com/workers-ai/](https://developers.cloudflare.com/workers-ai/)
- 模型列表：[https://developers.cloudflare.com/workers-ai/models/](https://developers.cloudflare.com/workers-ai/models/)
- 密钥申请：[https://dash.cloudflare.com/profile/api-tokens](https://dash.cloudflare.com/profile/api-tokens)

## 数据来源

资源文件：`resources/free-ai/cloudflare-workers-ai-free.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
