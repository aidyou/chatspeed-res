---
title: "Google Gemini API 免费层"
description: "免费层覆盖 Flash / Flash-Lite 系列模型（如 Gemini 2.5 Flash、2.5 Flash-Lite 及更新的 3.x Flash Lite），输入输出 token 免费；额度相对宽裕、适合日常使用，具体数值需在 AI Studio 查看。"
---

# Google Gemini API 免费层

免费层覆盖 Flash / Flash-Lite 系列模型（如 Gemini 2.5 Flash、2.5 Flash-Lite 及更新的 3.x Flash Lite），输入输出 token 免费；额度相对宽裕、适合日常使用，具体数值需在 AI Studio 查看。

Google Gemini API 为开发者和小型项目提供免费层。免费可用模型主要是 Flash 与 Flash-Lite 系列（如 Gemini 2.5 Flash、Gemini 2.5 Flash-Lite 以及更新的 3.x Flash Lite 变体），输入输出 token 免费，RPM/RPD 配额相对宽裕；Google 已不再逐模型完整公布免费层限速，请在 Google AI Studio 查看当前生效额度（历史上免费额度曾多次调整，例如 2025 年底收紧）。免费层只需 Google 账号，无需绑定账单或信用卡；限速按项目维度计算。API 同时支持原生协议与 OpenAI 兼容端点。

**官方网站：** [https://ai.google.dev/gemini-api/docs/pricing](https://ai.google.dev/gemini-api/docs/pricing)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`general`, `coding`, `reasoning`
- 标签：`google`, `gemini`, `free-tier`, `api`

## 免费使用说明

- 访问方式：`api`
- 是否需要登录：`是`
- 是否有免费层：`是`
- 可用区域：`global`

免费层覆盖 Flash / Flash-Lite 系列模型，输入输出 token 免费；各模型 RPM/RPD 配额在 Google AI Studio 展示并动态调整（官方不再完整公布）。免费层无需绑定账单或信用卡。

### 分模型免费额度明细

| 模型 | 免费额度 | 频率与限速 |
| --- | --- | --- |
| Gemini Flash 系列（如 Gemini 2.5 Flash 及更新的 3.x Flash） | 输入输出 token 免费 | RPM/RPD 以 AI Studio 为准，日常使用较宽裕 |
| Gemini Flash-Lite 系列（如 Gemini 2.5 Flash-Lite 及更新的 3.x Flash Lite） | 输入输出 token 免费 | 额度通常高于 Flash，以 AI Studio 为准 |
| 其他模型（Pro 系列、预览版等） | 是否计入免费层视模型而定 | 以 AI Studio 为准 |

## 注册与限制
- 注册入口：[https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
- 注册限制：使用 Google 账号注册即可，免费层无需信用卡；部分地区不可用，可用区域以官方政策为准。
- 免费政策文档：[https://ai.google.dev/gemini-api/docs/rate-limits](https://ai.google.dev/gemini-api/docs/rate-limits)

## ChatSpeed 导入

该服务关联模型供应商 `gemini`，可从模型供应商列表导入配置，调用入口如下：
- 协议：`gemini`
- Base URL：`https://generativelanguage.googleapis.com/v1beta`
- Logo：![Gemini](https://www.gstatic.com/lamda/images/favicon_v1_150160cddff7f294ce30.svg)
- 官方文档：[https://ai.google.dev/docs](https://ai.google.dev/docs)
- 模型列表：[https://ai.google.dev/models/gemini](https://ai.google.dev/models/gemini)
- 密钥申请：[https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

## 数据来源

资源文件：`resources/free-ai/gemini-api-free-tier.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
