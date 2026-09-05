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
    """Get basic info of a specified stock code (powered by the efinance library).

    Args:
        stock_code: stock code (string, e.g. '600519' (Kweichow Moutai), '000001' (Ping An Bank)).
        
    Returns:
        Dictionary: stock basic info dict (field descriptions are in the function description).
    """
    return ef.stock.get_base_info(stock_code)  # call the efinance library to fetch data
Gradio interface configuration
demo = gr.Interface(
    fn=get_stock_base_info,  # bind the core function
    inputs=gr.Textbox(
        label="Stock Code",
        placeholder="Enter a 6-digit A-share code (e.g. 600519)",
        max_length=6  # limit input to 6 digits to avoid invalid input
    ),
    outputs=gr.JSON(label="Stock Basic Info"),  # output structured JSON
    title="Stock Basic Info Query MCP",
    description="Enter a 6-digit A-share code to get basic info such as company name, industry, total shares, etc. (data source: efinance)."
)
```
## 📝 Example Call
### 1. Browser Testing (Suitable for Beginners to Verify)
Open the local web interface http://127.0.0.1:7860/, enter 600519 (Kweichow Moutai) in the input box, click "Submit", and you can see the output result:
```
{
  "name": "Kweichow Moutai Co., Ltd.",
  "industry": "Liquor industry",
  "total_shares": "125619.78 (10k)",
  "listed_date": "2001-08-27",
  "exchange": "Shanghai Stock Exchange",
  "register_address": "Maotai Town, Renhuai, Zunyi, Guizhou",
  // more fields returned by efinance...
}
```
### 2. Model/Application Invocation (MCP Protocol)
Invoke the /mcp interface through a POST request (example using Python's requests library):
```
import requests

# MCP service address (replace with the actual address)
url = "http://127.0.0.1:7860/mcp"

# Request data (conforms to the MCP protocol format)
data = {
    "name": "get_stock_base_info",  # MCP function name (must match the code)
    "parameters": {"stock_code": "600519"}  # Input parameters (stock code)
}

# Send the POST request
response = requests.post(url, json=data)

# Print the result
print(response.json())
The output is the same as the browser test result.
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
