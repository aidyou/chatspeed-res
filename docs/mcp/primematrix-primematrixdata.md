---
title: "质数幻方-企业数据MCP 1.0"
description: "质数幻方 MCP 使用文档 --- 接入指南 以下为任何支持 MCP 协议的 AI 工具（如 WorkBuddy、ClaudeCode、QoderWork 等）的通用接入方式。 接入步骤如下： 获取 MCP 接入凭证 在质数幻方官方平台（https://mcp.yidian.cn/）完成账号注册并登录，进入「API KEY 服务」生成新密钥，在「一键使用」区域获取全套 MCP 配置内容（带上你的 API Key），可直接复制使用。 配置 MCP 服务 在智能体客户端找到「添加 MCP 服务 / MCP 配置」入口，"
---

# 质数幻方-企业数据MCP 1.0

质数幻方 MCP 使用文档 --- 接入指南 以下为任何支持 MCP 协议的 AI 工具（如 WorkBuddy、ClaudeCode、QoderWork 等）的通用接入方式。 接入步骤如下： 获取 MCP 接入凭证 在质数幻方官方平台（https://mcp.yidian.cn/）完成账号注册并登录，进入「API KEY 服务」生成新密钥，在「一键使用」区域获取全套 MCP 配置内容（带上你的 API Key），可直接复制使用。 配置 MCP 服务 在智能体客户端找到「添加 MCP 服务 / MCP 配置」入口，

# 质数幻方 MCP 使用文档

---

## 接入指南

以下为任何支持 MCP 协议的 AI 工具（如 WorkBuddy、ClaudeCode、QoderWork 等）的通用接入方式。

接入步骤如下：

### 获取 MCP 接入凭证

在质数幻方官方平台（[https://mcp.yidian.cn/](https://mcp.yidian.cn/?ref=alimoda)）完成账号注册并登录，进入「API KEY 服务」生成新密钥，在「一键使用」区域获取全套 MCP 配置内容（带上你的 API Key），可直接复制使用。

### 配置 MCP 服务

在智能体客户端找到「添加 MCP 服务 / MCP 配置」入口，粘贴上面复制的 JSON，保存并重启；或者在智能体对话框中输入「请配置质数幻方 MCP」，并粘贴上面复制的 JSON，智能体即可自动完成 MCP 配置。

### 验证 MCP 接入效果

在对话中输入企业查询问题，例如“请查询华为技术有限公司的企业主体信息”。若正常返回企业工商信息，即说明 MCP 接入成功，可正常使用全部服务能力。

---

## 产品介绍

质数幻方提供企业主体、风险信息、经营情况、财务数据、知识产权五大 MCP 核心能力，助力 AI 商查场景。通过标准化的 MCP（Model Context Protocol）工具，开发者可以快速将企业信息查询能力集成到各类 AI 应用中，实现智能化企业查询、风险评估、商业决策支持等场景。

---

## 接入配置

### 认证方式

所有 MCP 请求需在 HTTP Header 中携带 `Authorization` 认证头，格式为 `Bearer 
`。API Key 可在控制台"API 密钥"页面创建和管理。

```text
"Authorization": "Bearer 
"
```

所有 MCP 请求需在服务地址中携带服务代码：

```text
https://mcp.yidian.cn/mcp/{service_code}
```

### 传输协议

```text
Transport: streamable-http
```

---

## 入参/出参规范

以下为各工具可能使用的入参说明，具体每个工具支持的参数详见工具列表。

### 入参规范

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| `ent_name` | String | 企业名称或统一社会信用代码（大部分工具通用，建议传入准确企业全称） |
| `credit_code` | String | 统一社会信用代码（18位） |

### 出参规范

所有 MCP 工具的返回结果均遵循 MCP 协议标准响应格式。

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| `content` | Array | 响应内容数组 |
| `content[].type` | String | 内容类型，固定值为 text |
| `content[].text` | String | 返回的业务数据内容，通常为 JSON 格式字符串 |
| `isError` | Boolean | 是否发生错误，true 表示错误，false 表示成功 |

响应示例：

```json
{
  "content": [
    {
      "type": "text",
      "text": "{\"CODE\":200,\"MSG\":\"ok\",\"DATA\":{...}}"
    }
  ],
  "isError": false
}
```

---

## MCP 工具列表

### 主体识别与查询

提供企业主体的身份识别与基础信息查询服务，包含企业模糊搜索、受益所有人结果、企业基本信息、变更信息、企业联系方式、主要人员信息、企业股东信息等工具。

| 工具名称 | 中文名称 | 功能描述 | 入参说明 |
| --- | --- | --- | --- |
| `get_company_precise_name` | 企业精准匹配 | 根据企业简称或关键词模糊搜索，返回唯一精确匹配主体或候选清单。 | ent_name (String, 必填): 企业简称或关键词 |
| `get_registration_info` | 核心登记信息 | 查询企业核心工商登记信息，包括法定代表人、注册资本、成立日期、登记状态等。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_branches` | 分支机构 | 查询企业分支机构名称、负责人、地区、成立日期、登记状态等。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_company_profile` | 企业简介 | 查询企业简介和主体概况，快速了解企业经营与基础画像。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_change_records` | 变更记录 | 查询企业历史变更事项、变更前后内容及变更日期。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_shareholder_info` | 股东信息 | 查询企业股东及出资信息，上市企业可返回十大股东信息。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_listing_info` | 上市信息 | 查询上市企业股票代码、上市日期、交易所、板块、总市值等信息。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_external_investments` | 对外投资 | 查询企业对外投资信息，包括被投资企业名称、经营状态、成立日期、注册资本、持股比例等。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |

### 风险信息

获取企业司法风险、运营风险及资产风险，覆盖失信被执行、裁判文书、经营异常、行政处罚、股权冻结等风险场景。

| 工具名称 | 中文名称 | 功能描述 | 入参说明 |
| --- | --- | --- | --- |
| `get_dishonest_info` | 失信被执行人 | 查询失信被执行人名称、涉案金额、执行法院、发布日期等。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_judgment_debtor_info` | 被执行人 | 查询被执行人案件信息，包括立案日期、执行标的、执行法院等。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_high_consumption_restriction` | 限制高消费 | 查询限制高消费记录，包括限制对象、立案日期和发布法院等。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_terminated_execution` | 终本案件 | 查询终本案件，包括终本日期、执行标的、未履行金额等。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_judicial_auction` | 司法拍卖 | 查询司法拍卖信息，包括标题、评估价、起拍价、拍卖时间等。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_bankruptcy_info` | 破产信息 | 查询企业破产重组、破产清算等破产相关信息。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_case_filing_info` | 立案信息 | 查询法院立案信息，包括案号、案由、立案日期、原被告信息等。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_hearing_notice` | 开庭公告 | 查询开庭公告，包括案号、案由、开庭时间、当事人身份等。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_court_notice` | 法院公告 | 查询法院公告，包括公告类型、案由、原被告信息等。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_judicial_documents` | 裁判文书 | 查询裁判文书，包括案号、案由、裁判结果、涉案金额等。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_service_notice` | 送达公告 | 查询送达公告，包括案号、案由、法院、发布日期等。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_business_exception` | 经营异常 | 查询经营异常名录，包括列入日期、移除原因和决定机关等。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_serious_violation` | 严重违法 | 查询严重违法失信名单记录及对应监管信息。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_cancellation_record_info` | 注销备案 | 查询注销备案情况，包括注销原因、注销日期、注销状态等。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_simple_cancellation_info` | 简易注销 | 查询简易注销信息，包括注销结果、登记机关、公告期等。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_administrative_penalty` | 行政处罚 | 查询行政处罚，包括处罚结果、处罚单位、金额、日期等。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_environmental_penalty` | 环保处罚 | 查询环保行政处罚，包括处罚结果、处罚单位、金额、日期等。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_procurement_debarment_list` | 失信名单 | 查询企业是否被列入政府采购严重违法失信名单，包括列入原因、处罚结果、处罚时间、执法单位等。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_tax_abnormal` | 税务非正常 | 查询税务非正常户记录及相关税务监管信息。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_tax_arrears_notice` | 欠税公告 | 查询欠税税种、欠税金额、发布单位、发布日期等。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_tax_violation` | 税收违法 | 查询税收违法案件性质、税务机关、发布日期等。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_chattel_mortgage_info` | 动产抵押 | 查询动产抵押登记编号、抵押权人、金额、状态、登记日期等。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_equity_freeze` | 股权冻结 | 查询股权司法冻结，包括冻结数额、期限、执行法院等。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_stock_pledge_info` | 股权质押 | 查询上市企业股权质押，包括质押人、质权人、股份数额、市值等。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_equity_pledge_info` | 股权出质 | 查询股权出质人、质权人、股权数额、状态、登记日期等。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_ipr_pledge` | 知识产权出质 | 查询知识产权出质类型、名称、期限、公告日期等。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |

### 经营情况

洞察企业真实经营活力，涵盖资质许可、招投标动态、融资历程、信用评级、新闻舆情与招聘信息。

| 工具名称 | 中文名称 | 功能描述 | 入参说明 |
| --- | --- | --- | --- |
| `get_administrative_license` | 行政许可 | 查询企业行政许可信息及许可事项。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_qualifications` | 资质证书 | 查询资质名称、证书编号、类别、等级、有效期、状态等。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_honor_info` | 荣誉信息 | 查询荣誉名称、类型、级别、发布日期、发布单位等。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_credit_evaluation` | 信用评级 | 查询官方信用评级、纳税信用等级等评价信息。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_financing_records` | 融资信息 | 查询创投融资、上市融资、增发融资等融资记录。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_bidding_info` | 招投标信息 | 查询招投标项目名称、中标情况、金额、招标单位等。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_random_check` | 双随机检查 | 查询双随机抽查检查记录及检查结果。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_spot_check_info` | 抽查检查 | 查询检查实施机关、类型、日期、结果等。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_news_sentiment` | 新闻舆情 | 查询新闻标题、发布时间、情感类型等舆情信息。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_taxpayer_qualification` | 纳税人资质 | 查询纳税人识别号、资格类型、主管税务机关、有效期等。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_recruitment_info` | 招聘信息 | 查询职位、月薪、学历、经验、办公地点、发布日期等。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |

### 财务数据

结构化输出上市企业核心财务数据及分析指标，覆盖资产负债表、现金流量表、利润表及综合财务指标。

| 工具名称 | 中文名称 | 功能描述 | 入参说明 |
| --- | --- | --- | --- |
| `get_financial_data` | 核心财务指标 | 查询上市企业的核心财务数据和分析指标 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_balance_sheet` | 资产负债表 | 查询上市公司资产负债表数据。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_cash_flow_statement` | 现金流量表 | 查询上市公司现金流量表数据。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_income_statement` | 利润表 | 查询上市公司利润表数据。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |

### 知识产权

评估企业科创硬实力，提供专利、商标、软件著作权、作品著作权及网络备案等知识产权信息。

| 工具名称 | 中文名称 | 功能描述 | 入参说明 |
| --- | --- | --- | --- |
| `get_patent_info` | 专利信息 | 查询专利总数、授权总数及不超过 20 条专利详情。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_copyright_work_info` | 作品著作权 | 查询作品名称、类别、登记号、登记日期等。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_software_copyright_info` | 软件著作权 | 查询软件全称、简称、版本号、登记号、登记时间等。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_trademark_info` | 商标信息 | 查询商标名称、国际分类、状态、申请号、注册号、申请日期等。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |
| `get_internet_service_info` | 网络备案 | 查询网站 ICP 备案、APP 备案、小程序备案、算法备案等。 | ent_name (String, 必填): 企业名称或统一社会信用代码 |

---

## 调用示例

以下展示用户与 AI 交互时，MCP 工具的实际调用效果。

### 示例1：工商股东查询

> 问题：帮我查一下腾讯的工商信息和股东信息

**AI 应用调用流程：**

**步骤1：** 调用 `get_company_precise_name`

```json
{
  "ent_name": "腾讯"
}
```

结果：返回匹配企业列表，确认全称为「深圳市腾讯计算机系统有限公司」

**步骤2：** 调用 `get_registration_info`

```json
{
  "ent_name": "深圳市腾讯计算机系统有限公司"
}
```

结果：返回企业工商登记信息，包括法定代表人、注册资本、成立日期、经营状态等

**步骤3：** 调用 `get_shareholder_info`

```json
{
  "ent_name": "深圳市腾讯计算机系统有限公司"
}
```

结果：返回企业股东及出资信息，辅助识别股权结构

### 示例2：风险信息查询

> 问题：查询腾讯是否存在经营异常、行政处罚和股权冻结风险

**AI 应用调用流程：**

**步骤1：** 调用 `get_company_precise_name`

```json
{
  "ent_name": "腾讯"
}
```

结果：返回匹配企业列表，确认全称为「深圳市腾讯计算机系统有限公司」

**步骤2：** 调用 `get_business_exception`

```json
{
  "ent_name": "深圳市腾讯计算机系统有限公司"
}
```

结果：返回经营异常记录，如无记录则返回空结果

**步骤3：** 调用 `get_administrative_penalty`

```json
{
  "ent_name": "深圳市腾讯计算机系统有限公司"
}
```

结果：返回行政处罚记录，包含处罚决定、处罚机关、处罚日期等

**步骤4：** 调用 `get_equity_freeze`

```json
{
  "ent_name": "深圳市腾讯计算机系统有限公司"
}
```

结果：返回股权司法冻结信息，用于辅助判断资产风险

### 示例3：招投标信息查询

> 问题：帮我查一下腾讯最近的招投标信息

**AI 应用调用流程：**

**步骤1：** 调用 `get_company_precise_name`

```json
{
  "ent_name": "腾讯"
}
```

结果：返回匹配企业列表，确认全称为「深圳市腾讯计算机系统有限公司」

**步骤2：** 调用 `get_bidding_info`

```json
{
  "ent_name": "深圳市腾讯计算机系统有限公司"
}
```

结果：返回招投标项目名称、中标情况、金额、招标单位等信息

**官方网站：** [https://mcp.yidian.cn](https://mcp.yidian.cn)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`finance`, `data`
- 标签：`research and data`, `search`, `finance`, `mcp`, `chinese`

## MCP 配置

- 传输方式：`http`
- 启动命令：``
- 参数：无

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/primematrix-primematrixdata.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
