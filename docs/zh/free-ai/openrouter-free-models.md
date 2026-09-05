---
title: "OpenRouter 免费模型"
description: "免费模型变体（模型 ID 加 :free 后缀）可通过 OpenAI 兼容 API 免费调用；新账号限速 20 次/分钟、每天最多 50 次，历史累计充值满 $10 后提升为每天 1,000 次。"
---

# OpenRouter 免费模型

免费模型变体（模型 ID 加 :free 后缀）可通过 OpenAI 兼容 API 免费调用；新账号限速 20 次/分钟、每天最多 50 次，历史累计充值满 $10 后提升为每天 1,000 次。

OpenRouter 是模型聚合与路由平台，通过一个 API Key 访问多家供应商的模型，在模型 ID 后追加 `:free` 后缀即可使用免费变体，便于快速体验与开发调试。免费变体与付费变体相比通常限速更低，可能出现排队或供应商偶发 429；平台侧免费限制会随政策调整（历史累计充值不足 $10 的账号每天最多 50 次，累计满 $10 后提升为每天 1,000 次）。OpenRouter 提供 OpenAI 兼容接口，可接入 ChatSpeed 使用。正式依赖前请查看所选模型的当前条款与官方限速文档。

**官方网站：** [https://openrouter.ai/docs/guides/routing/model-variants/free](https://openrouter.ai/docs/guides/routing/model-variants/free)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`general`, `coding`, `reasoning`
- 标签：`openrouter`, `free-models`, `api`

## 免费使用说明

- 访问方式：`api`
- 是否需要登录：`是`
- 是否有免费层：`是`
- 可用区域：`global`

免费模型变体限速 20 次/分钟；历史累计充值不足 $10 的账号每天最多 50 次，累计充值满 $10 后提升为每天 1,000 次。限制可能调整，以官方限速文档为准。

### 分模型免费额度明细

| 模型 | 免费额度 | 频率与限速 |
| --- | --- | --- |
| 全部免费变体（模型 ID 以 `:free` 结尾） | 免费 | 20 次/分钟 |
| 历史累计充值不足 $10 的账号 | 免费 | 每天最多 50 次 |
| 历史累计充值满 $10 的账号 | 免费 | 每天最多 1,000 次 |

## 注册与限制
- 注册入口：[https://openrouter.ai/](https://openrouter.ai/)
- 注册限制：邮箱注册即可，无需信用卡；免费日额度较低，可通过历史累计充值 $10+ 提升至每天 1,000 次，充值与支付方式以官方为准。
- 免费政策文档：[https://openrouter.ai/docs/api_reference/limits](https://openrouter.ai/docs/api_reference/limits)

## ChatSpeed 导入

该服务关联模型供应商 `openrouter`，可从模型供应商列表导入配置，调用入口如下：
- 协议：`openai`
- Base URL：`https://openrouter.ai/api/v1`
- Logo：![OpenRouter](https://openrouter.ai/favicon.ico)
- 文档：[https://openrouter.ai/docs](https://openrouter.ai/docs)
- 模型列表：[https://openrouter.ai/models](https://openrouter.ai/models)
- 密钥申请：[https://openrouter.ai/keys](https://openrouter.ai/keys)

## 数据来源

资源文件：`resources/free-ai/openrouter-free-models.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
