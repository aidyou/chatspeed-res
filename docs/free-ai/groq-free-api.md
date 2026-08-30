---
title: "Groq 免费 API"
description: "长期免费层、无需信用卡：如 Llama 3.1 8B 为 30 次/分钟、每天 14,400 次；Llama 3.3 70B、Llama 4 Scout、GPT-OSS 120B 为 30 次/分钟、每天 1,000 次；Kimi K2 / Qwen3 32B 为 60 次/分钟、每天 1,000 次。"
---

# Groq 免费 API

长期免费层、无需信用卡：如 Llama 3.1 8B 为 30 次/分钟、每天 14,400 次；Llama 3.3 70B、Llama 4 Scout、GPT-OSS 120B 为 30 次/分钟、每天 1,000 次；Kimi K2 / Qwen3 32B 为 60 次/分钟、每天 1,000 次。

Groq 通过 OpenAI 兼容 API 提供极速推理（部分模型 500+ tokens/秒），并设有长期免费层。限速按组织维度、分模型计算（见明细表），涉及 RPM、RPD、TPM、TPD 四类指标，先达到任一即返回 429 并附 X-RateLimit 响应头。注册无需信用卡。免费模型包括 Llama 系列、Kimi K2、Qwen3 32B、GPT-OSS 120B/20B 以及 Whisper 语音转写。数值可能调整，当前完整表格见 console.groq.com/docs/rate-limits。

**官方网站：** [https://groq.com/](https://groq.com/)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`general`, `coding`, `reasoning`
- 标签：`groq`, `free-tier`, `api`, `fast-inference`

## 免费使用说明

- 访问方式：`api`
- 是否需要登录：`是`
- 是否有免费层：`是`
- 可用区域：`global`

免费层按模型限速（RPM/RPD/TPM/TPD）；如 llama-3.1-8b-instant：30 次/分钟、每天 14,400 次、TPM 6,000、TPD 500,000。无需信用卡；当前数值以官方限速表为准。

### 分模型免费额度明细

| 模型 | 免费额度 | 频率与限速 |
| --- | --- | --- |
| llama-3.1-8b-instant | 免费 | 30 次/分钟 / 每天 14,400 次 / TPM 6,000 / TPD 500,000 |
| llama-3.3-70b-versatile、Llama 4 Scout、gpt-oss-120b/20b | 免费 | 30 次/分钟 / 每天 1,000 次（TPM 6,000–30,000 / TPD 10 万–50 万） |
| kimi-k2-instruct、qwen3-32b | 免费 | 60 次/分钟 / 每天 1,000 次 |
| whisper-large-v3 / whisper-large-v3-turbo（语音转写） | 免费 | 20 次/分钟 / 每天 2,000 次 |

## 注册与限制
- 注册入口：[https://console.groq.com/](https://console.groq.com/)
- 注册限制：邮箱或 Google 账号注册即可，无需信用卡。限速按组织计，而非按 API Key 计。
- 免费政策文档：[https://console.groq.com/docs/rate-limits](https://console.groq.com/docs/rate-limits)

## ChatSpeed 导入

该服务关联模型供应商 `groq`，可从模型供应商列表导入配置，调用入口如下：
- 协议：`openai`
- Base URL：`https://api.groq.com/openai/v1`
- Logo：![Groq](https://www.google.com/s2/favicons?domain=groq.com&sz=64)
- 官方文档：[https://console.groq.com/docs/overview](https://console.groq.com/docs/overview)
- 模型列表：[https://console.groq.com/docs/models](https://console.groq.com/docs/models)
- 密钥申请：[https://console.groq.com/keys](https://console.groq.com/keys)

## 数据来源

资源文件：`resources/free-ai/groq-free-api.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
