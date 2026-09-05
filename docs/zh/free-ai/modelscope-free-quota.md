---
title: "魔塔免费调用额度"
description: "免费注册并绑定阿里云账号、完成实名认证后，每个账号每天可免费调用模型推理 API（API-Inference）总计 2,000 次，单个模型一般每天不超过 500 次，部分大模型另有更低的单模型额度。"
---

# 魔塔免费调用额度

免费注册并绑定阿里云账号、完成实名认证后，每个账号每天可免费调用模型推理 API（API-Inference）总计 2,000 次，单个模型一般每天不超过 500 次，部分大模型另有更低的单模型额度。

魔塔（ModelScope）是阿里旗下的模型社区与托管推理平台，提供 6 万多个模型（Qwen 千问、DeepSeek、通义等系列，含文生图能力）的免费 API-Inference 在线推理。API 采用 OpenAI 兼容协议，并提供 Anthropic 兼容端点（可用于 Claude Code 类工具），适合希望通过 API 体验热门开源模型并把供应商配置接入 ChatSpeed 的用户。当前可免费调用的模型可通过 OpenAI 兼容的模型列表接口 `GET /v1/models` 获取，接口能取到的模型即可按免费额度调用。免费额度较为稳定，但热门模型有时会调整或下架，官方未逐一公布每个模型的具体额度，以官方限流文档和模型页为准。注意：未完成账号关联时调用会收到 401 提示，免费额度按自然日重新计算。

**官方网站：** [https://modelscope.cn/docs](https://modelscope.cn/docs)
**状态：** `review`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`general`, `coding`, `reasoning`
- 标签：`modelscope`, `free-quota`, `api`, `china`

## 免费使用说明

- 访问方式：`api`
- 是否需要登录：`是`
- 是否有免费层：`是`
- 可用区域：`regional`

注册并绑定阿里云账号、完成实名认证后，每天可调用 API-Inference 总计 2,000 次；单个模型一般每天不超过 500 次，部分大模型当前为 200 次/天（社区整理，官方未逐一明确）。可用模型列表以 `GET /v1/models` 接口返回为准。额度可能动态调整，以官方限流文档为准。

### 分模型免费额度明细

| 模型 | 免费额度 | 频率与限速 |
| --- | --- | --- |
| 全部模型（API-Inference 每日总额） | 每天总计 2,000 次 | 全模型合计，按自然日 |
| 单个一般模型（如 Qwen 系列） | 每个模型每天不超过 500 次 | 按模型按天 |
| deepseek-ai/DeepSeek-R1-0528、DeepSeek-V3.1 等大型模型 | 每个模型每天 200 次（当前） | 按模型按天，平台可能动态调整 |

## 注册与限制
- 注册入口：[https://modelscope.cn/](https://modelscope.cn/)
- 注册限制：手机号/邮箱免费注册魔搭账号后，需绑定阿里云账号并完成阿里云实名认证方可调用 API；无需信用卡。未绑定或未实名时接口返回 401（please bind your alibaba cloud...）。
- 免费政策文档：[https://modelscope.cn/docs/model-service/API-Inference/limits](https://modelscope.cn/docs/model-service/API-Inference/limits)

## ChatSpeed 导入

该服务自带 ChatSpeed 供应商配置，可直接导入，调用入口如下：
- 协议：`openai`
- Base URL：`https://api-inference.modelscope.cn/v1`
- Logo：![ModelScope](https://g.alicdn.com/sail-web/maas/2.7.13/favicon/128.ico)
- 文档：[https://modelscope.cn/docs/home](https://modelscope.cn/docs/home)
- 模型列表：[https://modelscope.cn/models](https://modelscope.cn/models)
- 密钥申请：[https://modelscope.cn/my/myaccesstoken](https://modelscope.cn/my/myaccesstoken)

## 数据来源

资源文件：`resources/free-ai/modelscope-free-quota.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
