---
title: "OpenCode Zen 免费模型"
description: "在 opencode 编码代理中，登录 OpenCode Zen 账号即可限时免费使用 MiMo-V2.5 Free、Big Pickle、Nemotron 3 Ultra Free 等模型，无需添加账单信息。"
---

# OpenCode Zen 免费模型

在 opencode 编码代理中，登录 OpenCode Zen 账号即可限时免费使用 MiMo-V2.5 Free、Big Pickle、Nemotron 3 Ultra Free 等模型，无需添加账单信息。

OpenCode Zen 是 OpenCode 团队（SST）维护的 AI 网关，主要在 opencode 编码代理（TUI / CLI）内使用：登录后在 /connect 中粘贴 Zen API Key，再通过 /models 选择模型。当前有一组模型限时免费（MiMo-V2.5 Free、Big Pickle、Nemotron 3 Ultra Free、Nemotron 3.5 Lightning Free、Ling 3.0 Flash Fin Free、Muse Spark 1.2 Contributor Free），无需添加账单信息；付费模型按 token 计费（余额低于 $5 时自动充值 $20，可关闭）。同时暴露 OpenAI 兼容端点 https://opencode.ai/zen/v1，也可在 ChatSpeed 中配置。免费名单轮换频繁，请以官方文档为准。

**官方网站：** [https://opencode.ai/docs/zen/](https://opencode.ai/docs/zen/)
**状态：** `review`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`coding`
- 标签：`opencode`, `zen`, `free-models`, `coding`, `api`

## 免费使用说明

- 访问方式：`api`
- 是否需要登录：`是`
- 是否有免费层：`是`
- 可用区域：`global`

一组模型限时免费（MiMo-V2.5 Free、Big Pickle、Nemotron 3 Ultra Free 等）；免费模型无需账单信息。名单会轮换，以官方文档为准。

### 分模型免费额度明细

| 模型 | 免费额度 | 频率与限速 |
| --- | --- | --- |
| MiMo-V2.5 Free / Big Pickle / Nemotron 3 Ultra Free / Nemotron 3.5 Lightning Free / Ling 3.0 Flash Fin Free / Muse Spark 1.2 Contributor Free（当前名单） | 免费 | 限时免费，名单轮换，以官方文档为准 |

## 注册与限制
- 注册入口：[https://opencode.ai/zen](https://opencode.ai/zen)
- 注册限制：在 opencode 中或通过 Zen 网站注册/登录账号即可；免费模型无需账单信息，使用付费模型需添加账单（默认余额低于 $5 自动充值 $20，可关闭或调低）。
- 免费政策文档：[https://opencode.ai/docs/zen/](https://opencode.ai/docs/zen/)

## ChatSpeed 导入

该服务关联模型供应商 `opencode-zen`，可从模型供应商列表导入配置，调用入口如下：
- 协议：`openai`
- Base URL：`https://opencode.ai/zen/v1`
- Logo：![OpenCode Zen](https://www.google.com/s2/favicons?domain=opencode.ai&sz=64)
- 文档：[https://opencode.ai/docs/zen/](https://opencode.ai/docs/zen/)
- 模型列表：[https://opencode.ai/zen/v1/models](https://opencode.ai/zen/v1/models)
- 密钥申请：[https://opencode.ai/zen](https://opencode.ai/zen)

## 数据来源

资源文件：`resources/free-ai/opencode-zen-free-models.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
