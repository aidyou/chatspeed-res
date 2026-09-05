---
title: "StockBaseInfoMCP"
description: "This is a Gradio-based MCP (Model Context Protocol) service for querying basic information of stocks (powered by the efinance library). It supports input of any valid stock code (such as 600519 (Kweic…"
---

# StockBaseInfoMCP

This is a Gradio-based MCP (Model Context Protocol) service for querying basic information of stocks (powered by the efinance library). It supports input of any valid stock code (such as 600519 (Kweic…

# StockBaseInfoMCP
A Gradio-based MCP service for quickly querying the basic information of A-share stocks (data source: efinance).

## 📌 Function Description
Input: 6-digit A-share stock code (string, such as 600519, 000001);

Output: Structured JSON data, containing the following key fields (example):

- name: Full company name (e.g., Kweichow Moutai Co., Ltd.);
- industry: Industry classification (e.g., Liquor Industry);
- total_shares: Total shares (unit: shares, e.g., 125619.78 million);
- listed_date: Listing date (e.g., 2001-08-27);

(Note: More fields are returned by the efinance library, and the actual output should be taken as the standard).

## 🚀 Quick Start
1. Environment Preparation
Python 3.7+;
Install dependency libraries (gradio for building the interface, efinance for obtaining stock data):
`pip install gradio efinance`

2. Run the Service
Save the code as app.py, and execute the following command to start the MCP server:
`python app.py`

After starting, the terminal will output:

Local Web Interface: http://127.0.0.1:7860/ (can be tested via a browser);

MCP Service Interface: http://127.0.0.1:7860/mcp (for model/application invocation);

Share Link (optional): https://xxxx-xx-xx-xx-xx.gradio.live/ (for external network access, valid for 24 hours).

## 📖 MCP Configuration Explanation
Core function definition
```
def get_stock_base_info(stock_code: str) -> dict:
    """获取指定股票代码的基础信息（依赖efinance库）。

    Args:
        stock_code: 股票代码（字符串，如'600519'（贵州茅台）、'000001'（平安银行））。
        
    Returns:
        Dictionary: 股票基础信息字典（字段说明见功能说明）。
    """
    return ef.stock.get_base_info(stock_code)  # 调用efinance库获取数据
Gradio接口配置
demo = gr.Interface(
    fn=get_stock_base_info,  # 绑定核心函数
    inputs=gr.Textbox(
        label="股票代码",
        placeholder="请输入6位A股代码（如600519）",
        max_length=6  # 限制输入长度为6位，避免无效输入
    ),
    outputs=gr.JSON(label="股票基础信息"),  # 输出结构化JSON
    title="股票基础信息查询MCP",
    description="输入6位A股代码，获取公司名称、行业、总股本等基础信息（数据来源：efinance）。"
)
```
## 📝 Example Call
### 1. Browser Testing (Suitable for Beginners to Verify)
Open the local web interface http://127.0.0.1:7860/, enter 600519 (Kweichow Moutai) in the input box, click "Submit", and you can see the output result:
```
{
  "name": "贵州茅台酒股份有限公司",
  "industry": "酿酒行业",
  "total_shares": "125619.78万",
  "listed_date": "2001-08-27",
  "exchange": "上海证券交易所",
  "register_address": "贵州省遵义市仁怀市茅台镇",
  // 更多字段由efinance返回...
}
```
### 2. Model/Application Invocation (MCP Protocol)
Invoke the /mcp interface through a POST request (example using Python's requests library):
```
import requests

# MCP服务地址（需替换为实际运行地址）
url = "http://127.0.0.1:7860/mcp"

# 请求数据（符合MCP协议格式）
data = {
    "name": "get_stock_base_info",  # MCP函数名（必须与代码中一致）
    "parameters": {"stock_code": "600519"}  # 输入参数（股票代码）
}

# 发送POST请求
response = requests.post(url, json=data)

# 打印结果
print(response.json())
输出结果与浏览器测试一致。
```
⚠️ Notes
Stock Code Format: You must enter a valid stock code (such as Shanghai Main Board 600xxx, Shenzhen Main Board 000xxx, etc.), otherwise, the efinance library will return an error;

Data Source: The data is provided by the efinance library. If there are missing or incorrect fields, please check the version of efinance (it is recommended to install the latest version: pip install --upgrade efinance);

Port Occupation: If port 7860 is occupied, you can modify the server_port parameter of demo.launch() (e.g., demo.launch(mcp_server=True, server_port=8000));

Share Link: share=True will generate a temporary link accessible from the external network (valid for 24 hours), suitable for testing but not recommended for production environments.

📜 License
This project uses the MIT license. For details, please refer to the LICENSE file.

**Official site: ** [https://www.modelscope.cn/studios/PeixuanXia/StockBaseInfoMCP](https://www.modelscope.cn/studios/PeixuanXia/StockBaseInfoMCP)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `finance`
- Tags: `finance`, `search`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `mcp-remote https://peixuanxia-stockbaseinfomcp.ms.show/gradio_api/mcp/sse --transport sse-only`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/peixuanxia-stockbaseinfomcp.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
