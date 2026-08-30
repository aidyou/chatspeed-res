---
title: "World Bank MCP - 世界银行 MCP"
description: "世界银行MCP 🌐 基于世界银行开放数据API的世界银行模型上下文协议服务，提供全球经济发展数据的查询功能。 📋 功能 - ✅ 国家信息查询 - ✅ 指标搜索（教育、健康、环境等） - ✅ 经济数据查询（GDP、通货膨胀、失业率等） - ✅ 社会发展数据查询（人口、预期寿命、互联网使用情况等） - ✅ 教育数据查询（识字率、入学率等） - ✅ 健康与营养数据查询（医院、免疫接种、HIV感染率、营养不良等） - ✅ 实时世界银行API集成 - ✅ 模型上下文协议兼容性 📦 安装 使用npm全局安装 bash npm "
---

# World Bank MCP - 世界银行 MCP

世界银行MCP 🌐 基于世界银行开放数据API的世界银行模型上下文协议服务，提供全球经济发展数据的查询功能。 📋 功能 - ✅ 国家信息查询 - ✅ 指标搜索（教育、健康、环境等） - ✅ 经济数据查询（GDP、通货膨胀、失业率等） - ✅ 社会发展数据查询（人口、预期寿命、互联网使用情况等） - ✅ 教育数据查询（识字率、入学率等） - ✅ 健康与营养数据查询（医院、免疫接种、HIV感染率、营养不良等） - ✅ 实时世界银行API集成 - ✅ 模型上下文协议兼容性 📦 安装 使用npm全局安装 bash npm 

# 世界银行MCP 🌐

[![npm version](/mcp-assets/85282d2522c3ad09bd6756ee61e7d586.svg)](https://www.npmjs.com/package/worldbank-mcp)
[![License: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)
[![GitHub issues](/mcp-assets/a5455c15cf287264ca31cd6dbdf53fd3.svg)](https://github.com/tianyuio/worldbank-mcp/issues)

基于世界银行开放数据API的世界银行模型上下文协议服务，提供全球经济发展数据的查询功能。

## 📋 功能

- ✅ 国家信息查询
- ✅ 指标搜索（教育、健康、环境等）
- ✅ 经济数据查询（GDP、通货膨胀、失业率等）
- ✅ 社会发展数据查询（人口、预期寿命、互联网使用情况等）
- ✅ 教育数据查询（识字率、入学率等）
- ✅ 健康与营养数据查询（医院、免疫接种、HIV感染率、营养不良等）
- ✅ 实时世界银行API集成
- ✅ 模型上下文协议兼容性

## 📦 安装

### 使用npm全局安装
```bash
npm install -g worldbank-mcp
```
### 使用npx即时运行
```bash
npx worldbank-mcp
```
## 💻 在MCP客户端中的使用

要在支持MCP的客户端（如Claude Desktop、Cursor、Cherry Studio等）中使用此服务，您需要按如下方式配置：

配置示例：

### 如果已全局安装，请使用npm运行：

```json

{

  "mcpServers": {

    "worldbank-mcp": {

      "name": "World Bank Data",

      "command": "worldbank-mcp",

      "description": "World Bank Open Data MCP Server"

    }

  }

}

```
### 使用npx即时运行：

```json

{

  "mcpServers": {

    "worldbank-mcp": {

      "name": "World Bank Data",

      "command": "npx",

      "args": ["worldbank-mcp"],

      "description": "World Bank Open Data MCP Server"

    }

  }

}

```
### 直接使用node运行：

```json

{

  "mcpServers": {

    "worldbank-mcp": {

      "name": "World Bank Data",

      "command": "node",

      "args": ["path/to/worldbank-mcp/build/index.js"],

      "description": "World Bank Open Data MCP Server"

    }

  }

}

```
将`path/to/`替换为您的项目目录的实际路径。

## 📎 使用示例

### 🧑‍💻 用户
> 用表格比较中国和美国的经济

### 🤖 助手
> 我将帮助你用详细的表格比较中国和美国的经济。让我收集两国的综合经济数据。

> *世界银行数据 : 获取经济数据* ✅

> #### **中国与美国经济对比 (2010-2024)**
> 
> 根据世界银行的数据，以下是中美两国经济的详细对比表：
> 
> ##### **表1：GDP对比（万亿美元）**
> | 年份 | 中国GDP | 美国GDP | 美国占中国的百分比 | 中国增长率 |
> |------|-----------|--------|------------------|-------------------|
> | 2024 | 18.74 | 29.18 | 156% | 2.6% |
> | 2023 | 18.27 | 27.72 | 152% | 6.2% |
> | 2022 | 18.32 | 26.01 | 142% | -2.5% |
> | 2021 | 18.20 | 23.68 | 130% | 9.2% |
> | 2020 | 14.99 | 21.35 | 142% | -17.6% |
> | 2019 | 14.56 | 21.54 | 148% | 2.9% |
> | 2018 | 14.15 | 20.66 | 146% | 12.9% |
> | 2017 | 12.54 | 19.61 | 156% | 10.0% |
> | 2016 | 11.46 | 18.80 | 164% | 7.9% |
> | 2015 | 11.28 | 18.29 | 162% | 5.9% |
> | 2014 | 10.67 | 17.61 | 165% | 9.5% |
> | 2013 | 9.74 | 16.88 | 173% | 12.4% |
> | 2012 | 8.67 | 16.25 | 187% | 13.1% |
> | 2011 | 7.67 | 15.60 | 203% | 19.1% |
> | 2010 | 6.19 | 15.05 | 243% | - |
> 
> **关键见解：**
> - 美国经济仍然显著更大（2024年大56%）
> - 自2010年以来，中国的GDP增长了203%
> - 两国经济差距正在缩小
> 
> ##### **表2：人均GDP（美元）**
> ##### **表3：GDP增长率（%）**
> ##### **表4：通货膨胀率（%）**
> ##### **表5：失业率（%）**
> ##### **表6：出口占GDP的百分比**
> ##### **表7：外国直接投资净流入（十亿美元）**
>
> ##### **总结分析**
> 
> ###### **经济规模与增长**
> - **美国**：经济规模更大，成熟增长（每年2-3%）
> - **中国**：规模较小但增长更快（最近5-6%），正在追赶
> 
> ###### **发展水平**
> - **美国**：高收入发达国家（人均85,000美元）
> - **中国**：上中等收入发展中国家（人均13,000美元）
>
> ###### **经济稳定性**
> - **中国**：通胀和失业更稳定
> - **美国**：波动较大，但在繁荣期实现更低的失业率
> 
> ###### **经济结构**
> - **中国**：出口导向型，以制造业为基础
> - **美国**：消费导向型，以服务业为基础
> 
> ###### **投资流动**> - **中国**: 传统上的净资本输出国，最近吸引了更多的外国直接投资
> - **美国**: 模式混合，在有利条件下吸引大量投资

这种比较突出了两个处于不同发展阶段的经济超级大国，每个国家都有其独特的优势、挑战和经济结构。

## 🔧 MCP 工具

### 1. 获取国家列表
```json
{
  "name": "get-countries",
  "description": "Get all countries supported by World Bank",
  "parameters": {
    "region": "Filter by region (optional)",
    "incomeLevel": "Filter by income level (optional)"
  }
}
```
### 2. 获取国家信息
```json
{
  "name": "get-country-info", 
  "description": "Get detailed information for a specific country",
  "parameters": {
    "countryCode": "Country code (e.g.: CN, US)"
  }
}
```
### 3. 搜索指标
```json
{
  "name": "search-indicators",
  "description": "Search for available indicators",
  "parameters": {
    "keyword": "Search keyword"
  }
}
```
### 4. 获取经济数据
```json
{
  "name": "get-economic-data",
  "description": "Get economic data for a country",
  "parameters": {
    "countryCode": "Country code",
    "indicator": "Economic indicator (GDP, GDP_GROWTH, GDP_PER_CAPITA, GNI, GNI_PER_CAPITA, EXPORTS_GDP, FDI_NET, INFLATION, UNEMPLOYMENT)",
    "years": "Number of years to query (optional, default 10 years)"
  }
}
```
### 5. 获取社会发展数据
```json
{
  "name": "get-social-data",
  "description": "Get social development data for a country", 
  "parameters": {
    "countryCode": "Country code",
    "indicator": "Social indicator (POPULATION, LIFE_EXPECTANCY, BIRTH_RATE, DEATH_RATE, INTERNET_USERS)",
    "years": "Number of years to query (optional, default 10 years)"
  }
}
```
### 6. 获取教育数据
```json
{
  "name": "get-education-data",
  "description": "Get education data for a country", 
  "parameters": {
    "countryCode": "Country code",
    "indicator": "Education indicator (LITERACY_RATE, SCHOOL_ENROLLMENT, SCHOOL_COMPLETION, TEACHERS_PRIMARY, EDUCATION_EXPENDITURE)",
    "years": "Number of years to query (optional, default 10 years)"
  }
}
```
### 7. 获取健康与营养数据
```json
{
  "name": "get-health-data",
  "description": "Get health and nutrition data for a country", 
  "parameters": {
    "countryCode": "Country code",
    "indicator": "Health indicator (HEALTH_EXPENDITURE, PHYSICIANS, HOSPITAL_BEDS, IMMUNIZATION, HIV_PREVALENCE, MALNUTRITION, TUBERCULOSIS)",
    "years": "Number of years to query (optional, default 10 years)"
  }
}
```
## 📖 支持的指标

### 经济指标

| 指标代码 | 描述 | 单位 |
|---------|------|------|
| GDP | 国内生产总值 | 当前美元 |
| GDP_GROWTH | GDP 增长率 | 年度 % |
| GDP_PER_CAPITA | 人均GDP | 当前美元 |
| GNI | 国民总收入 | 当前美元 |
| GNI_PER_CAPITA | 人均国民总收入 | 当前美元 |
| EXPORTS_GDP | 货物和服务出口 | 占GDP的百分比 |
| FDI_NET | 净流入的外国直接投资 | 当前美元 |
| INFLATION | 通货膨胀率 | 年度 % |
| UNEMPLOYMENT | 失业率 | 占总劳动力的百分比 |

### 社会指标

| 指标代码 | 描述 | 单位 |
|---------|------|------|
| POPULATION | 总人口 | 人 |
| LIFE_EXPECTANCY | 出生时预期寿命 | 年 |
| BIRTH_RATE | 出生率 | 每千人 |
| DEATH_RATE | 死亡率 | 每千人 |
| INTERNET_USERS | 互联网用户 | 占总人口的百分比 |

### 教育指标

| 指标代码 | 描述 | 单位 |
|---------|------|------|
| LITERACY_RATE | 识字率 | 占15岁及以上人口的百分比 |
| SCHOOL_ENROLLMENT | 小学入学率 | 毛入学率 % |
| SCHOOL_COMPLETION | 小学完成率 | 相关年龄组的百分比 |
| TEACHERS_PRIMARY | 小学教师人数 | 数量 |
| EDUCATION_EXPENDITURE | 政府教育支出 | 占GDP的百分比 |

### 健康与营养指标

| 指标代码 | 描述 | 单位 |
|---------|------|------|
| HEALTH_EXPENDITURE | 当前卫生支出 | 占GDP的百分比 |
| PHYSICIANS | 医生数量 | 每千人 |
| HOSPITAL_BEDS | 医院床位数 | 每千人 |
| IMMUNIZATION | 麻疹免疫接种率 | 占12-23个月儿童的百分比 |
| HIV_PREVALENCE | 艾滋病患病率 | 占15-49岁人口的百分比 |
| MALNUTRITION | 营养不良发生率 | 占总人口的百分比 |
| TUBERCULOSIS | 结核病发病率 | 每十万人 |

### 常见国家代码

| 国家 | 代码 | 国家 | 代码 |
|------|------|------|------|
| 中国 | CN | 美国 | US |
| 日本 | JP | 德国 | DE |
| 英国 | GB | 法国 | FR |
| 印度 | IN | 巴西 | BR |
| 俄罗斯 | RU | 澳大利亚 | AU |

## 项目结构

```

worldbank-mcp/

├── src/

│   ├── index.ts      # Main entry file

│   └── types.ts      # Type definitions

├── build/            # Compiled output

├── package.json      # Project configuration

├── tsconfig.json     # TypeScript configuration

└── README.md         # Documentation

```
## 技术栈

- **TypeScript** - 类型安全的开发语言
- **Model Context Protocol SDK** - MCP协议实现
- **Axios** - HTTP客户端
- **Zod** - 数据验证
- **Commander** - 命令行工具

## API端点

项目使用世界银行开放数据API：
- 基础URL: `https://api.worldbank.org/v2`
- 国家数据: `/countries`
- 指标数据: `/indicators`
- 国家指标数据: `/country/{code}/indicator/{id}`

## 许可证

该项目采用**MIT许可证** - 详情请参阅[LICENSE](https://github.com/tianyuio/worldbank-mcp/blob/HEAD/LICENSE)文件。

**官方网站：** [https://github.com/tianyuio/worldbank-mcp](https://github.com/tianyuio/worldbank-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`, `finance`, `data`
- 标签：`search`, `finance`, `research and data`, `world bank`, `世界银行`, `数据`, `经济`, `社会`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`worldbank-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/tianyuio-worldbank.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
