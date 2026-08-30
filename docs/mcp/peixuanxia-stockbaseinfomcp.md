---
title: "查询股票基础信息MCP"
description: "这是一个基于Gradio的MCP（Model Context Protocol）服务，用于查询股票的基础信息（依赖efinance库）。支持输入任意有效股票代码（如600519（贵州茅台）、TSLA（特斯拉）），返回包含公司名称、行业分类、总股本、上市日期等关键信息的结构化JSON数据，适用于需要股票基础数据的应用场景（如金融分析工具、股票查询小程序等）。\n\nA Gradio-based MCP (Model Context Protocol) service for querying basic information of stocks (powered by the efinance library). Accepts any valid stock code (e.g., 600519 for Kweichow Moutai, TSLA for Tesla) and returns structured JSON data including company name, industry, total shares, listing date, etc. Suitable for applications requiring stock basic data (e.g., financial analysis tools, stock query mini-programs)."
---

# 查询股票基础信息MCP

这是一个基于Gradio的MCP（Model Context Protocol）服务，用于查询股票的基础信息（依赖efinance库）。支持输入任意有效股票代码（如600519（贵州茅台）、TSLA（特斯拉）），返回包含公司名称、行业分类、总股本、上市日期等关键信息的结构化JSON数据，适用于需要股票基础数据的应用场景（如金融分析工具、股票查询小程序等）。

A Gradio-based MCP (Model Context Protocol) service for querying basic information of stocks (powered by the efinance library). Accepts any valid stock code (e.g., 600519 for Kweichow Moutai, TSLA for Tesla) and returns structured JSON data including company name, industry, total shares, listing date, etc. Suitable for applications requiring stock basic data (e.g., financial analysis tools, stock query mini-programs).

# StockBaseInfoMCP
一个基于Gradio的MCP服务，用于快速查询A股股票的基础信息（数据来源：efinance）。

## 📌 功能说明
输入：6位A股股票代码（字符串，如600519、000001）；

输出：结构化JSON数据，包含以下关键字段（示例）：

- name：公司全称（如贵州茅台酒股份有限公司）；
- industry：行业分类（如酿酒行业）；
- total_shares：总股本（单位：股，如125619.78万）；
- listed_date：上市日期（如2001-08-27）；

（注：更多字段由efinance库返回，以实际输出为准）。

## 🚀 快速开始
1. 环境准备
Python 3.7+；
安装依赖库（gradio用于构建接口，efinance用于获取股票数据）：
`pip install gradio efinance`

2. 运行服务
将代码保存为app.py，执行以下命令启动MCP服务器：
`python app.py`

启动后，终端会输出：

本地Web接口：http://127.0.0.1:7860/（可通过浏览器测试）；

MCP服务接口：http://127.0.0.1:7860/mcp（供模型/应用调用）；

共享链接（可选）：https://xxxx-xx-xx-xx-xx.gradio.live/（用于外网访问，有效期24小时）。

## 📖 MCP配置说明
核心函数定义
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
## 📝 示例调用
### 1. 浏览器测试（适合新人验证）
打开本地Web接口http://127.0.0.1:7860/，在输入框中输入600519（贵州茅台），点击“提交”，即可看到输出结果：
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
### 2. 模型/应用调用（MCP协议）
通过POST请求调用/mcp接口（示例用Python的requests库）：
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
⚠️ 注意事项
股票代码格式：必须输入有效股票代码（如上证主板600xxx、深证主板000xxx等），否则efinance库会返回错误；

数据来源：数据由efinance库提供，若返回字段缺失或错误，请检查efinance版本（建议安装最新版：pip install --upgrade efinance）；

端口占用：若7860端口被占用，可修改demo.launch()的server_port参数（如demo.launch(mcp_server=True, server_port=8000)）；

共享链接：share=True会生成外网可访问的临时链接（有效期24小时），适合测试，但不建议用于生产环境。

📜 许可证
本项目采用MIT许可证，详情请见LICENSE文件。

**官方网站：** [https://www.modelscope.cn/studios/PeixuanXia/StockBaseInfoMCP](https://www.modelscope.cn/studios/PeixuanXia/StockBaseInfoMCP)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`finance`
- 标签：`finance`, `search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`mcp-remote https://peixuanxia-stockbaseinfomcp.ms.show/gradio_api/mcp/sse --transport sse-only`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/peixuanxia-stockbaseinfomcp.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
