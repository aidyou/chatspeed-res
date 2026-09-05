---
title: "Pollinations 免费 API"
description: "开源生成式 AI API（文本/图像/音频/视频）；免费模型可直接通过 OpenAI 兼容文本端点调用，无需注册与 API Key。"
---

# Pollinations 免费 API

开源生成式 AI API（文本/图像/音频/视频）；免费模型可直接通过 OpenAI 兼容文本端点调用，无需注册与 API Key。

Pollinations 是开源生成式 AI 平台，提供文本、图像、音频、视频生成的简单 HTTP API。文本 API 采用 OpenAI 兼容格式（https://text.pollinations.ai/openai），免费模型无需注册和 API Key 即可调用；图像生成为 image.pollinations.ai。部分较新模型或需要更高优先级的调用可能要求账号/token 体系。限速较宽松但会随负载调整，正式依赖前请以官方仓库/文档为准。

**官方网站：** [https://pollinations.ai/](https://pollinations.ai/)
**状态：** `review`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`general`, `image`
- 标签：`pollinations`, `free-api`, `no-key`, `multimodal`

## 免费使用说明

- 访问方式：`api`
- 是否需要登录：`否`
- 是否有免费层：`是`
- 可用区域：`global`

免费模型无需注册与 API Key 即可使用；限速较宽松但会随负载调整。部分较新模型可能需要账号/token 体系。当前限制以官方仓库为准。

### 分模型免费额度明细

| 模型 | 免费额度 | 频率与限速 |
| --- | --- | --- |
| 免费文本模型（OpenAI 兼容端点） | 免费 | 无需密钥；限速以官方仓库为准 |
| 图像生成（image.pollinations.ai） | 免费 | 无需密钥；限速以官方仓库为准 |

## 注册与限制
- 注册限制：免费文本/图像 API 无需注册；更高优先级或较新模型可能需按官方说明使用账号/token 访问。

## ChatSpeed 导入

该服务关联模型供应商 `pollinations`，可从模型供应商列表导入配置，调用入口如下：
- 协议：`openai`
- Base URL：`https://text.pollinations.ai/openai`
- Logo：![Pollinations](https://pollinations.ai/favicon-32x32.png)
- 文档：[https://github.com/pollinations/pollinations/blob/master/APIDOCS.md](https://github.com/pollinations/pollinations/blob/master/APIDOCS.md)
- 模型列表：[https://text.pollinations.ai/models](https://text.pollinations.ai/models)

## 数据来源

资源文件：`resources/free-ai/pollinations-free-api.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
