---
title: "Stock-Quant-Calculator-MCP"
description: "Based on the Qwen3 inference engine, the stock quant agent calculates the support levels for a specific stock when it is declining and provides recommendations. Detailed usage instructions can be obta…"
---

# Stock-Quant-Calculator-MCP

Based on the Qwen3 inference engine, the stock quant agent calculates the support levels for a specific stock when it is declining and provides recommendations. Detailed usage instructions can be obta…

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

**Official site: ** [https://www.modelscope.cn/mcp](https://www.modelscope.cn/mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `communication`, `finance`
- Tags: `communication`, `finance`, `股票量化`, `量化`, `支撑点位`, `股票`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/virgo777-stock-quant-calculator.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
