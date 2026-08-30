---
title: "Groq"
description: "OpenAI 兼容的超快推理服务，免费层额度宽裕（如 Llama 3.1 8B：30 次/分钟、每天 14,400 次），无需信用卡。"
---

# Groq

OpenAI 兼容的超快推理服务，免费层额度宽裕（如 Llama 3.1 8B：30 次/分钟、每天 14,400 次），无需信用卡。

Groq 使用自研 LPU 芯片提供极速 LLM 推理（部分模型 500+ tokens/秒），并提供 OpenAI 兼容接口。免费层长期存在，限速按组织维度、分模型计算（例如 llama-3.1-8b-instant：30 次/分钟、每天 14,400 次、TPM 6,000、TPD 500,000），无需信用卡；超限返回 429 并附 X-RateLimit 响应头。免费模型包括 Llama 3.1/3.3/Llama 4 Scout、Kimi K2、Qwen3 32B、GPT-OSS 120B/20B 以及 Whisper 语音转写等。

**官方网站：** [https://groq.com/](https://groq.com/)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`general`, `coding`, `reasoning`
- 标签：`groq`, `openai-compatible`, `free-tier`, `fast-inference`

## 供应商配置

- 协议：`openai`
- Base URL：`https://api.groq.com/openai/v1`
- 模型数量：0
- 文档：[https://console.groq.com/docs/overview](https://console.groq.com/docs/overview)
- 模型列表：[https://console.groq.com/docs/models](https://console.groq.com/docs/models)
- 密钥申请：[https://console.groq.com/keys](https://console.groq.com/keys)

## 数据来源

资源文件：`resources/models/groq.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
