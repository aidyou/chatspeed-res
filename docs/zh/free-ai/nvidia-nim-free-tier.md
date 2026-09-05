---
title: "NVIDIA NIM API"
description: "免费注册 NVIDIA 开发者账号并申请 API Key（无需信用卡）即可调用托管模型接口，常见限速约 40 次/分钟，面向开发与原型验证，具体额度以模型页为准。"
---

# NVIDIA NIM API

免费注册 NVIDIA 开发者账号并申请 API Key（无需信用卡）即可调用托管模型接口，常见限速约 40 次/分钟，面向开发与原型验证，具体额度以模型页为准。

NVIDIA NIM 是 NVIDIA 在 build.nvidia.com 上提供的托管（无服务器）推理平台，汇集 DeepSeek、Qwen3-Coder、Kimi K2、MiniMax M2、Mistral、Devstral 等热门模型，并支持部分文生图模型（如 FLUX.1-dev）。新用户可以免费加入 NVIDIA 开发者计划并创建兼容 OpenAI 的 API Key（nvapi- 开头，创建后只显示一次，请立即保存）。免费层按官方定位属于面向开发与原型验证的试用性服务，不同模型的免费额度和速率限制（常见约 40 次/分钟）会在模型页面展示当前值。免费层不适合生产依赖；需要更高吞吐时可申请额度提升或转付费方案。

**官方网站：** [https://build.nvidia.com/explore/discover](https://build.nvidia.com/explore/discover)
**状态：** `review`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`general`, `coding`, `reasoning`
- 标签：`nvidia`, `nim`, `free-tier`, `api`

## 免费使用说明

- 访问方式：`api`
- 是否需要登录：`是`
- 是否有免费层：`是`
- 可用区域：`global`

新账号注册即送免费 API 额度（以模型页展示的 credits 计量，社区普遍反馈初始约 1,000）；文本模型常见限速约 40 次/分钟。免费额度和限速会因账号、模型与当前负载而异，请以模型页显示为准。

### 分模型免费额度明细

| 模型 | 免费额度 | 频率与限速 |
| --- | --- | --- |
| 多数文本模型（如 DeepSeek V3.2/R1、Qwen3-Coder 480B、Kimi K2、MiniMax M2、Mistral、Devstral） | 免费（按 credits 计量，新账号常见约 1,000） | 约 40 次/分钟（按模型与负载而异） |
| 部分文生图模型（如 FLUX.1-dev） | 免费，例如 25 次请求（近期示例） | 一次性额度，以模型页当前标注为准 |

## 注册与限制
- 注册入口：[https://build.nvidia.com/](https://build.nvidia.com/)
- 注册限制：邮箱可注册（实测 QQ 邮箱可用）。手机验证环节中国大陆（+86）手机号收不到验证码（已实测确认：联通、电信各一张均失败）；境外号码可正常收到验证码（已实测英国号码可用）。使用可正常接收短信的境外号码即可完成注册/验证。无需绑定信用卡；API Key（nvapi- 开头）创建后仅显示一次，需立即保存。

## ChatSpeed 导入

该服务自带 ChatSpeed 供应商配置，可直接导入，调用入口如下：
- 协议：`openai`
- Base URL：`https://integrate.api.nvidia.com/v1`
- Logo：![NVIDIA NIM](https://build.nvidia.com/favicon.ico)
- 文档：[https://docs.api.nvidia.com/nim/reference/llm-apis](https://docs.api.nvidia.com/nim/reference/llm-apis)
- 模型列表：[https://build.nvidia.com/models](https://build.nvidia.com/models)
- 密钥申请：[https://build.nvidia.com/settings/api-keys](https://build.nvidia.com/settings/api-keys)

## 数据来源

资源文件：`resources/free-ai/nvidia-nim-free-tier.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
