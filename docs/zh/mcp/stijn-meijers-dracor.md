---
title: "stijn-meijers"
description: "DraCor MCP 服务器 一个用于与戏剧语料库项目（DraCor）API 交互的模型上下文协议（MCP）服务器。此 MCP 服务器使您能够通过 Claude 或其他大型语言模型（LLM）无缝分析戏剧文本及其角色网络。 概述 该项目使用官方的 Model Context Protocol Python SDK 实现了一个 MCP 服务器，提供了对 DraCor API v1 的访问。它允许 Cl…"
---

# stijn-meijers

DraCor MCP 服务器 一个用于与戏剧语料库项目（DraCor）API 交互的模型上下文协议（MCP）服务器。此 MCP 服务器使您能够通过 Claude 或其他大型语言模型（LLM）无缝分析戏剧文本及其角色网络。 概述 该项目使用官方的 Model Context Protocol Python SDK 实现了一个 MCP 服务器，提供了对 DraCor API v1 的访问。它允许 Cl…

# DraCor MCP 服务器

一个用于与戏剧语料库项目（DraCor）API 交互的模型上下文协议（MCP）服务器。此 MCP 服务器使您能够通过 Claude 或其他大型语言模型（LLM）无缝分析戏剧文本及其角色网络。

## 概述

该项目使用官方的 Model Context Protocol Python SDK 实现了一个 MCP 服务器，提供了对 DraCor API v1 的访问。它允许 Claude 和其他 LLM 与戏剧文本语料库进行交互，分析角色网络，检索剧本信息，并生成关于不同语言和时期的戏剧作品的见解。

该项目包括两种实现：

1. `dracor_mcp_fastmcp.py` - 使用基于装饰器的 FastMCP API 的简化实现，支持 v1 API

## 功能

- 通过统一接口访问 DraCor API v1
- 无需认证（DraCor API 是公开可访问的）
- 结构化的 DraCor 实体数据模型
- 支持的操作：
  - 语料库和剧本信息检索
  - 角色网络分析
  - 剧本指标和统计数据
  - 角色信息和台词
  - 剧本比较分析
  - 搜索功能
  - 角色关系数据
  - 多种格式的网络数据（CSV、GEXF、GraphML）
  - 跨剧本的性别分析
  - **纯文本和 TEI XML 格式的全文检索**
  - **完整的剧本文本分析**

## 设置

### 先决条件

- Python 3.10 或更高版本
- UV 包管理器（推荐）或 pip

### 使用 UV 安装

1. 安装 UV：

pip install uv

2. 创建虚拟环境并安装依赖项：

uv venv
source .venv/bin/activate  # 在 Windows 上：.venvScriptsactivate
uv pip install -e .

3. 在 Claude Desktop 中安装 MCP 服务器：

对于标准实现（v0 API）：

mcp install dracor_mcp_server.py

或者对于 FastMCP 实现（v1 API，推荐）：

mcp install dracor_mcp_fastmcp.py

### 开发模式

用于测试和开发：

mcp dev dracor_mcp_server.py

或者对于 FastMCP 实现（v1 API，推荐）：

mcp dev dracor_mcp_fastmcp.py

这将启动 MCP Inspector，在其中您可以交互式地测试您的工具和资源。

### Claude 配置

您还可以直接配置 Claude 以使用 DraCor MCP 服务器，方法是在您的 Claude 配置文件中添加以下内容：

json
{
  "tools": {
    "DraCor API v1": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "mcp[cli]",
        "--with",
        "requests",
        "--with",
        "pydantic",
        "--with",
        "python-multipart",
        "mcp",
        "run",
        "/path/to/dracor-mcp/dracor_mcp_fastmcp.py"
      ]
    }
  }
}

将 `/path/to/dracor-mcp/` 替换为实际的 dracor-mcp 目录路径。此配置使用 `uv run` 执行 MCP 服务器，并带有必要的依赖项，而无需预先安装。

### Docker（可选）

如果您更喜欢使用 Docker：

docker build -t dracor-mcp .
docker run dracor-mcp

要改为使用 FastMCP 实现（v1 API）：

docker run -e IMPLEMENTATION=fastmcp dracor-mcp

## 实现细节

### 标准 MCP 实现（v0 API）

在 `dracor_mcp_server.py` 中的标准实现使用了核心 MCP SDK 类与旧的 v0 API：

- `Resource` - 用于定义 API 资源
- `MCPToolImpl` - 用于实现工具
- `PromptTemplate` - 用于创建提示模板

### FastMCP 实现（v1 API）

在 `dracor_mcp_fastmcp.py` 中的 FastMCP 实现使用了更简洁的基于装饰器的方法与当前的 v1 API：

- `@mcp.resource()` - 用于定义 API 资源
- `@mcp.tool()` - 用于实现工具
- `@mcp.prompt()` - 用于创建提示模板

这种方法使得代码更加清晰且易于维护，同时提供相同的功能但可以访问更多全面的 API 特性。

## v1 API 特性v1 API 实现提供了访问许多额外端点和功能的途径：

- **API 信息** - DraCor API 的版本信息
- **语料库元数据** - 语料库中所有剧本的详细元数据
- **剧本度量** - 网络度量和分析数据
- **角色网络数据** - CSV、GEXF 和 GraphML 格式
- **角色关系** - 角色之间的显式关系
- **口语文本过滤器** - 按性别、关系类型或角色身份过滤
- **舞台指示** - 获取带有或不带发言者的舞台指示
- **角色查找** - 查找包含特定角色（通过 Wikidata ID）的剧本

## 使用方法

在 Claude Desktop 中安装后，您可以通过 Claude 与 DraCor API 进行交互。以下是一些示例：

### 基本查询

1. 要求 Claude 列出可用的戏剧语料库：

   
   Can you list all available drama corpora in DraCor?
   

2. 获取关于特定剧本的信息：

   
   Tell me about Goethe s Faust in the German corpus
   

3. 分析角色网络：

   
   Analyze the character network in Hamlet from the Shakespeare corpus
   

### 高级查询

1. 分析角色关系：

   
   What are the strongest character relationships in Pushkin s Boris Godunov?
   

2. 比较剧本：

   
   Compare Goethe s Faust and Schiller s Die Räuber in terms of network density and character count
   

3. 分析角色重要性：

   
   Who are the most central characters in Shakespeare s Hamlet based on speaking time and relationships?
   

4. 分析性别表现：

   
   Analyze the gender distribution and representation in Molière s Le Misanthrope
   

5. 在不同剧本中查找一个角色：

   
   Find all plays that feature a character named "Hamlet" or similar
   

6. 分析剧本全文：

   
   Provide a comprehensive analysis of the full text of Goethe s Faust
   

7. 从剧本文本中提取主题：

   
   What are the main themes and motifs in the full text of Shakespeare s Hamlet?
   

8. 分析语言模式：

   
   Analyze the language patterns and style in Chekhov s The Cherry Orchard
   

### 文学分析查询

1. 分析剧本结构：

   
   Analyze the structure of Molière s Le Misanthrope in terms of acts, scenes, and dialogue distribution
   

2. 比较作者：

   
   Compare the network structures in plays by Shakespeare and Molière
   

3. 历史背景：

   
   Put Pushkin s Boris Godunov in its historical context and analyze how this is reflected in the character network
   

## 资源 (v1 API)

FastMCP 服务器公开了以下资源：

- `info://` - API 信息和版本详情
- `corpora://` - 所有可用语料库的列表
- `corpus://{corpus_name}` - 关于特定语料库的信息
- `corpus_metadata://{corpus_name}` - 语料库中所有剧本的元数据
- `plays://{corpus_name}` - 特定语料库中的剧本列表
- `play://{corpus_name}/{play_name}` - 关于特定剧本的信息
- `play_metrics://{corpus_name}/{play_name}` - 特定剧本的网络度量
- `characters://{corpus_name}/{play_name}` - 特定剧本中的角色列表
- `spoken_text://{corpus_name}/{play_name}` - 剧本中的口语文本（可选过滤）
- `spoken_text_by_character://{corpus_name}/{play_name}` - 每个角色的发言文本
- `stage_directions://{corpus_name}/{play_name}` - 剧本中的舞台指示
- `network_data://{corpus_name}/{play_name}` - CSV 格式的网络数据
- `relations://{corpus_name}/{play_name}` - CSV 格式的角色关系数据
- `character_by_wikidata://{wikidata_id}` - 通过 Wikidata ID 列出包含特定角色的剧本
- `full_text://{corpus_name}/{play_name}` - 剧本的纯文本格式全文
- `tei_text://{corpus_name}/{play_name}` - 剧本的完整 TEI XML 文本

## 工具 (v1 API)

FastMCP 服务器提供了以下工具：

- `search_plays` - 根据查询搜索剧本
- `compare_plays` - 比较两个剧本的度量和结构- `analyze_character_relations` - 分析剧本中的人物关系
- `analyze_play_structure` - 分析剧本的结构
- `find_character_across_plays` - 在多个剧本中查找某个角色
- `analyze_full_text` - 分析剧本的全文，包括对话和舞台指示

## 提示模板 (v1 API)

FastMCP 服务器包含以下提示模板：

- `analyze_play` - 用于分析特定剧本的模板
- `character_analysis` - 用于分析特定角色的模板
- `network_analysis` - 用于分析角色网络的模板
- `comparative_analysis` - 用于比较两个剧本的模板
- `gender_analysis` - 用于分析剧本中性别表现的模板
- `historical_context` - 用于分析剧本历史背景的模板
- `full_text_analysis` - 用于分析剧本全文的模板

## 工作原理

该项目使用官方的 Model Context Protocol Python SDK 构建了一个 MCP 服务器，该服务器暴露了 Claude 可以用来与 DraCor API 交互的资源和工具。

当你向 Claude 询问关于戏剧文本的问题时，它可以：

1. 访问诸如语料库、剧本、角色和网络等资源
2. 使用工具来搜索、比较和分析剧本
3. 根据数据提供见解和可视化结果

DraCor API 是公开可访问的，因此不需要身份验证。

## 速率限制

请注意 DraCor 的速率限制政策。服务器包含了可以在 .env 文件中配置的可选速率限制设置。

## 故障排除

如果你遇到问题：

1. 确保你使用的是 Python 3.10 或更高版本
2. 尝试在开发模式下运行以进行调试：`mcp dev dracor_mcp_fastmcp.py`
3. 检查 DraCor API 的状态：https://dracor.org/doc/api

## 与 MCP 一起使用的提示

"你的任务是从 DraCor 数据库中分析历史剧本，以识别角色 ID 标签问题。具体来说：

1. 从 DraCor 数据库中选择一个剧本，并对其人物关系、全文和结构进行全面分析。
2. 识别所有可能的角色 ID 标签不一致之处，包括：
   - 角色名称的拼写变体
   - 角色名称混淆或合并
   - 历史拼写变体
   - 角色 ID 与舞台指示之间的差异
3. 创建一份详细的潜在角色 ID 标签错误报告，采用结构化表格格式，包含以下列：
   - 文本 ID（剧本的唯一标识符）
   - 当前数据库中使用的角色 ID
   - 文本中发现的问题变体
   - 错误类型（拼写、变体、混淆等）
   - 问题说明

针对此文本执行：[playname]"

## 许可证

MIT

## 致谢

该项目使用了：

- Model Context Protocol Python SDK 用于构建 MCP 服务器
- DraCor API v1 用于戏剧文本和网络数据
- Drama Corpora Project (DraCor) 用于提供基础数据和 API

**官方网站：** [https://github.com/stijn-meijers/dracor-mcp](https://github.com/stijn-meijers/dracor-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`art and culture`, `search`, `research and data`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`run --with mcp[cli] --with requests --with pydantic --with python-multipart mcp run /path/to/dracor-mcp/dracor_mcp_fastmcp.py`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/stijn-meijers-dracor.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
