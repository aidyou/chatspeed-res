---
title: "阿里云百炼新人免费额度"
description: "首次开通自动发放各模型新人免费额度（通常每模型 100 万 Token，有效期 90 天，华北2北京地域，无需实名）；另有 Qwen Code OAuth 独立免费额度每天 2,000 次。"
---

# 阿里云百炼新人免费额度

首次开通自动发放各模型新人免费额度（通常每模型 100 万 Token，有效期 90 天，华北2北京地域，无需实名）；另有 Qwen Code OAuth 独立免费额度每天 2,000 次。

阿里云百炼是阿里云的大模型服务平台（千问 Qwen 及生态模型）。首次开通百炼时，系统自动为每个模型发放新人免费额度（通常每模型 100 万 Token，有效期 90 天，仅华北2（北京）地域生效）；使用免费额度无需实名认证，未认证账号额度耗尽后默认强制用完即停（返回 403 FreeTierOnly）。此外，Qwen Code 的 OAuth 认证提供独立于 API Key 体系的免费额度（每天 2,000 次调用）。通过 OpenAI 兼容端点可接入 ChatSpeed。注意免费额度仅抵扣实时推理，不抵扣 Batch、模型调优、部署等费用。

**官方网站：** [https://bailian.console.aliyun.com/](https://bailian.console.aliyun.com/)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`general`, `coding`
- 标签：`aliyun`, `bailian`, `free-quota`, `api`, `china`

## 免费使用说明

- 访问方式：`api`
- 是否需要登录：`是`
- 是否有免费层：`是`
- 可用区域：`regional`

每模型新人免费额度（通常 100 万 Token/模型，有效期 90 天，华北2地域）+ Qwen Code OAuth 每天 2,000 次；免费额度无需实名认证。以官方帮助文档当前说明为准。

### 分模型免费额度明细

| 模型 | 免费额度 | 频率与限速 |
| --- | --- | --- |
| 各模型新人免费额度（qwen-plus、qwen-max、qwen3 系列等） | 通常每模型 100 万 Token（各模型独立） | 有效期 90 天；仅华北2（北京）地域 |
| Qwen Code OAuth 认证 | 每天 2,000 次调用 | 与 API Key 免费额度相互独立，按自然日 |

## 注册与限制
- 注册入口：[https://bailian.console.aliyun.com/](https://bailian.console.aliyun.com/)
- 注册限制：注册阿里云账号（手机号/邮箱）并开通百炼即可；免费额度无需实名认证，但额度用完后按量付费需要实名并充值（未认证默认停止调用）。面向中国大陆用户。
- 免费政策文档：[https://help.aliyun.com/zh/model-studio/new-free-quota](https://help.aliyun.com/zh/model-studio/new-free-quota)

## ChatSpeed 导入

该服务自带 ChatSpeed 供应商配置，可直接导入，调用入口如下：
- 协议：`openai`
- Base URL：`https://dashscope.aliyuncs.com/compatible-mode/v1`
- Logo：![Bailian](https://img.alicdn.com/tfs/TB1_ZXuNcfpK1RjSZFOXXa6nFXa-32-32.ico)
- 文档：[https://help.aliyun.com/zh/model-studio/getting-started/what-is-model-studio](https://help.aliyun.com/zh/model-studio/getting-started/what-is-model-studio)
- 模型列表：[https://help.aliyun.com/zh/model-studio/models](https://help.aliyun.com/zh/model-studio/models)
- 密钥申请：[https://bailian.console.aliyun.com/?apiKey=1#/api-key](https://bailian.console.aliyun.com/?apiKey=1#/api-key)

## 数据来源

资源文件：`resources/free-ai/aliyun-bailian-free-quota.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
