---
title: "硅基流动免费模型与额度"
description: "新用户注册送约 ¥14（约合 2,000 万 tokens）额度，完成实名认证后可长期免费使用大量开源模型（DeepSeek、Qwen、Llama、GLM 等），免费模型费用为 0、限速固定。"
---

# 硅基流动免费模型与额度

新用户注册送约 ¥14（约合 2,000 万 tokens）额度，完成实名认证后可长期免费使用大量开源模型（DeepSeek、Qwen、Llama、GLM 等），免费模型费用为 0、限速固定。

硅基流动（SiliconFlow）是国内 MaaS 平台，在一个 OpenAI 兼容端点后提供 200+ 开源模型。免费政策：新账号注册赠送约 ¥14 额度（约相当于 2,000 万 tokens 的 Qwen 类模型调用）；完成实名认证后可使用全部永久免费模型（名称不带 Pro/ 前缀），调用费用为 0、限速固定。文本（语言）模型一般允许 RPM 1,000–10,000、TPM 5 万–500 万（按模型与用量级别）；图像生成模型限 IPM 2 / IPD 400。免费政策与限速可能调整，请以官方速率限制与计费文档为准。该接口可接入 ChatSpeed。

**官方网站：** [https://siliconflow.cn/](https://siliconflow.cn/)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`general`, `coding`, `reasoning`
- 标签：`siliconflow`, `free-models`, `api`, `china`

## 免费使用说明

- 访问方式：`api`
- 是否需要登录：`是`
- 是否有免费层：`是`
- 可用区域：`regional`

注册赠约 ¥14（约合 2,000 万 tokens）额度；实名认证后免费模型调用费用为 0，文本模型约 RPM 1,000–10,000 / TPM 5 万–500 万，图像模型 IPM 2 / IPD 400；以官方文档当前值为准。

### 分模型免费额度明细

| 模型 | 免费额度 | 频率与限速 |
| --- | --- | --- |
| 新用户注册额度（全模型按 token 消耗） | 约 ¥14（约合 2,000 万 tokens 的 Qwen 类模型） | 一次性赠送，具体以官方计费文档为准 |
| 永久免费模型（文本，如 DeepSeek、Qwen、Llama、GLM 变体） | 免费（费用 0） | RPM 1,000–10,000 / TPM 5 万–500 万（按模型） |
| 图像生成模型 | 免费（费用 0） | IPM 2 / IPD 400 |

## 注册与限制
- 注册入口：[https://siliconflow.cn/](https://siliconflow.cn/)
- 注册限制：手机号/邮箱注册即可；免费模型需完成实名认证后方可使用全部免费模型。无需信用卡，中国大陆用户可直接注册使用。
- 免费政策文档：[https://docs.siliconflow.cn/cn/userguide/rate-limits/rate-limit-and-upgradation](https://docs.siliconflow.cn/cn/userguide/rate-limits/rate-limit-and-upgradation)

## ChatSpeed 导入

该服务关联模型供应商 `siliconflow`，可从模型供应商列表导入配置，调用入口如下：
- 协议：`openai`
- Base URL：`https://api.siliconflow.cn/v1`
- Logo：![SiliconFlow](https://framerusercontent.com/images/4li2PjWxZJmoGkzXRMJWU1rJmI.svg)
- 文档：[https://docs.siliconflow.cn/cn/userguide/introduction](https://docs.siliconflow.cn/cn/userguide/introduction)
- 模型列表：[https://cloud.siliconflow.cn/models](https://cloud.siliconflow.cn/models)
- 密钥申请：[https://cloud.siliconflow.cn/account/ak](https://cloud.siliconflow.cn/account/ak)

## 数据来源

资源文件：`resources/free-ai/siliconflow-free-models.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
