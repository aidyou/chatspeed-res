---
title: "Cerebras 免费层"
description: "OpenAI 兼容的极速推理（可达约 2,000 tokens/秒），免费层每模型每天约 100 万 tokens（如 Llama 3.3 70B）；无需信用卡。"
---

# Cerebras 免费层

OpenAI 兼容的极速推理（可达约 2,000 tokens/秒），免费层每模型每天约 100 万 tokens（如 Llama 3.3 70B）；无需信用卡。

Cerebras 使用晶圆级芯片托管开源 LLM，通过 OpenAI 兼容 API（https://api.cerebras.ai/v1）提供极高吞吐。免费层每模型每天约 100 万 tokens，并按模型设置 RPM/TPM/TPD 限速（数值见官方 rate-limits 文档）；超限返回 429。无需信用卡；付费 Developer 层限速约为免费层 10 倍。

**官方网站：** [https://www.cerebras.ai/](https://www.cerebras.ai/)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`general`, `coding`
- 标签：`cerebras`, `free-tier`, `api`, `fast-inference`

## 免费使用说明

- 访问方式：`api`
- 是否需要登录：`是`
- 是否有免费层：`是`
- 可用区域：`global`

免费层约每模型每天 100 万 tokens（另按模型设 RPM/TPM 限速）；无需信用卡；当前数值以官方 rate-limits 文档为准。

### 分模型免费额度明细

| 模型 | 免费额度 | 频率与限速 |
| --- | --- | --- |
| 免费层模型（如 Llama 3.3 70B、Qwen3 等开源模型） | 免费，每模型约 100 万 tokens/天 | 按模型设 RPM/TPM/TPD，见官方文档 |

## 注册与限制
- 注册入口：[https://cloud.cerebras.ai/](https://cloud.cerebras.ai/)
- 注册限制：邮箱注册即可，无需信用卡；限速按组织/API Key 与模型计。
- 免费政策文档：[https://inference-docs.cerebras.ai/support/rate-limits](https://inference-docs.cerebras.ai/support/rate-limits)

## ChatSpeed 导入

该服务关联模型供应商 `cerebras`，可从模型供应商列表导入配置，调用入口如下：
- 协议：`openai`
- Base URL：`https://api.cerebras.ai/v1`
- Logo：![Cerebras](https://www.google.com/s2/favicons?domain=cerebras.ai&sz=64)
- 文档：[https://inference-docs.cerebras.ai/](https://inference-docs.cerebras.ai/)
- 模型列表：[https://inference-docs.cerebras.ai/](https://inference-docs.cerebras.ai/)
- 密钥申请：[https://cloud.cerebras.ai/](https://cloud.cerebras.ai/)

## 数据来源

资源文件：`resources/free-ai/cerebras-free-tier.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
