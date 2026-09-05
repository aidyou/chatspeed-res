---
title: "生物数据助手"
description: "一个模型上下文协议服务器，用于与Biomart数据库接口，允许模型发现生物数据集、探索属性/过滤器、检索生物数据以及在不同生物标识符之间进行转换。"
---

# 生物数据助手

一个模型上下文协议服务器，用于与Biomart数据库接口，允许模型发现生物数据集、探索属性/过滤器、检索生物数据以及在不同生物标识符之间进行转换。

# Biomart MCP

### 一个用于与Biomart接口的MCP服务器

[模型上下文协议](https://modelcontextprotocol.io/introduction) (MCP) 是一种开放协议，它标准化了应用程序如何为[Anthropic](https://www.anthropic.com/)开发的LLM提供上下文。这里我们使用[MCP python-sdk](https://github.com/modelcontextprotocol/python-sdk)创建了一个通过[pybiomart](https://github.com/jrderuiter/pybiomart)包与Biomart接口的MCP服务器。

有一个简短的[演示视频](https://github.com/jzinno/biomart-mcp/blob/HEAD/assets/mcp-demo.mp4)，展示了在Claude Desktop上运行的MCP服务器。

## 安装

### 克隆仓库

```bash
git clone https://github.com/jzinno/biomart-mcp.git
cd biomart-mcp
```

### Claude Desktop

```bash
uv run --with mcp[cli] mcp install --with pybiomart biomart-mcp.py
```

### Cursor

通过Cursor的代理模式，其他模型也可以利用MCP服务器，例如来自OpenAI或DeepSeek的模型。点击光标设置齿轮图标并导航到`功能` -> `MCP服务器` -> `添加新的MCP服务器`。将名称设置为`biomart`（或者你喜欢的任何名称），并将`类型`设置为`命令`。

设置命令为：

```bash
uv run --with mcp[cli] --with pybiomart mcp run /your/path/to/biomart-mcp.py
```

### Glama

  

### 开发

```bash
# Create a virtual environment
uv venv

# MacOS/Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate

uv sync #or uv add mcp[cli] pybiomart

# Run the server in dev mode
mcp dev biomart-mcp.py
```

## 功能

Biomart-MCP提供了几个工具来与Biomart数据库交互：

- **Mart和数据集发现**：列出可用的marts和数据集以探索Biomart数据库结构
- **属性和过滤器探索**：查看特定数据集的常用或所有可用属性和过滤器
- **数据检索**：使用特定属性和过滤器查询Biomart以获取生物数据
- **ID转换**：在不同的生物标识符之间进行转换（例如，基因符号到Ensembl ID）

## 贡献

欢迎提交拉取请求！关于开发的一些小提示：

- 我们特意只在这里使用`@mcp.tool()`，这是为了最大化与支持MCP客户端的兼容性，如[文档](https://modelcontextprotocol.io/clients)所示。
- 我们使用`@lru_cache`来缓存计算成本高或调用外部API的功能的结果。
- 我们需要注意不要超出模型的上下文窗口限制，例如你会看到很多地方有`df.to_csv(index=False).replace("\r", "")`。这种CSV风格的返回比像`df.to_string()`这样的方式更节省token，后者中的大部分token是空白字符。同时也要注意，从染色体中拉取所有基因或其他类似的大请求也会超过上下文窗口的大小。

## 潜在的未来功能

当然还有很多可以添加的功能，其中一些可能超出了`biomart-mcp`这个名字的范围。这里是一些想法：

- 使用 `bs4` 对资源网站进行网页抓取，例如我们获取了NOTCH1的Ensembl基因ID，那么在某些情况下，可能从[UCSC页面](https://genome.ucsc.edu/cgi-bin/hgGene?db=hg38&hgg_chrom=chr9&hgg_gene=ENST00000651671.1&hgg_start=136494433&hgg_end=136546048&hgg_type=knownGene)中抓取“Comments and Description Text from UniProtKB”部分的内容会很有用。
- $...$

**官方网站：** [https://github.com/jzinno/biomart-mcp](https://github.com/jzinno/biomart-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`research and data`, `databases`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`run --with mcp[cli] --with pybiomart mcp run /your/path/to/biomart-mcp.py`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/jzinno-biomart.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
