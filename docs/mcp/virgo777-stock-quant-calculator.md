---
title: "股票量化支撑点位计算器"
description: "基于Qwen3推理引擎的股票量化智能体，计算特定股票下跌时的介入支撑位，并提供建议。\n其详细使用方法可通过MCP平台内置的《查询操作手册》获取。\n网页版请登录：http://49.235.53.176:929\nFor detailed usage instructions on the Qwen3-powered quantitative trading agent with advanced reasoning capabilities for stock market analysis, please refer to the MCP Query Cookbook accessible via the platform's built-in documentation system."
---

# 股票量化支撑点位计算器

基于Qwen3推理引擎的股票量化智能体，计算特定股票下跌时的介入支撑位，并提供建议。
其详细使用方法可通过MCP平台内置的《查询操作手册》获取。
网页版请登录：http://49.235.53.176:929
For detailed usage instructions on the Qwen3-powered quantitative trading agent with advanced reasoning capabilities for stock market analysis, please refer to the MCP Query Cookbook accessible via the platform's built-in documentation system.

# 股票量化MCP服务使用手册

## 📌 简介  
**智能股票量化支撑点位计算服务（MCP）** 是基于Qwen3大模型推理能力与远程量化计算服务器构建的专业金融分析工具，提供以下核心功能：  
- 目标股票支撑介入价位计算  
- 标准化API接口与SSE流式数据传输  

---

## ⚙️ 服务配置说明  
在您的系统中添加以下JSON配置启用服务：  
```json
{
    "mcpServers": {
        "quant_mcp_server": {
            "type": "sse",
            "url": "http://www.socoo.xyz:9000/sse"
        }
    }
}
```
---
# 🛠️ 直接使用方法：
# 建议直接使用上方提供的SSE地址

| 工具名称             | 使用方法                    | 描述                            |
|:-----------------|:------------------------|:------------------------------|
| cookbook         | 这个socoo股票MCP服务怎么用？      | 返回socoo量化服务MCP的使用指南           |
| get_support_quant_price | 帮我计算一下000858.SZ的支撑位是多少？ | 返回特定股票量化计算得到的支撑位（保守位，正常位，极限位） |
| get-     | 请求...接口                 | 冗余量化计算接口服务                    |



## ❓ 常见问题解答
Q1：如何获取详细文档？

输入示例：
```text
    股票量化MCP服务的使用方法有哪些？  (在安装MCP服务过多时候，最好带有socoo关键字)
    这个socoo股票MCP服务怎么用？
    这个socoo量化怎么用？
    能否提供一份关于量化交易MCP服务的详细说明文档？
    我想了解如何使用MCP服务进行股票数据分析。
    MCP服务支持哪些函数调用，这些函数的功能是什么？
    给我讲一下这个股票量化MCP服务的使用方法；
    讲一下这个量化MCP的使用方法；
    这个股票MCP服务怎么用？
    这个股票量化怎么用？
```


## 技术支持:
官方文档：https://mcp-docs.socoo.xyz
  
开发者邮箱：virgo_wang@qq.com

**官方网站：** [https://www.modelscope.cn/mcp](https://www.modelscope.cn/mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`communication`, `finance`
- 标签：`communication`, `finance`, `股票量化`, `量化`, `支撑点位`, `股票`

## MCP 配置

- 传输方式：`http`
- 启动命令：``
- 参数：无

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/virgo777-stock-quant-calculator.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
