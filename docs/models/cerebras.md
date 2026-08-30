---
title: "Cerebras"
description: "OpenAI 兼容的晶圆级推理服务，免费层约 100 万 tokens/天（如 Llama 3.3 70B），无需信用卡。"
---

# Cerebras

OpenAI 兼容的晶圆级推理服务，免费层约 100 万 tokens/天（如 Llama 3.3 70B），无需信用卡。

Cerebras 使用晶圆级芯片托管开源 LLM，吞吐极高（部分模型可达约 2,000 tokens/秒），提供 OpenAI 兼容接口。免费层每个模型每天约 100 万 tokens，并按模型设置 RPM/TPM/TPD 限速，无需信用卡；超限返回 429。付费 Developer 层限速约为免费层 10 倍。当前限速值以官方 rate-limits 文档为准。

**官方网站：** [https://www.cerebras.ai/](https://www.cerebras.ai/)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`general`, `coding`
- 标签：`cerebras`, `openai-compatible`, `free-tier`, `fast-inference`

## 供应商配置

- 协议：`openai`
- Base URL：`https://api.cerebras.ai/v1`
- 模型数量：0
- 文档：[https://inference-docs.cerebras.ai/](https://inference-docs.cerebras.ai/)
- 模型列表：[https://inference-docs.cerebras.ai/](https://inference-docs.cerebras.ai/)
- 密钥申请：[https://cloud.cerebras.ai/](https://cloud.cerebras.ai/)

## 数据来源

资源文件：`resources/models/cerebras.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
