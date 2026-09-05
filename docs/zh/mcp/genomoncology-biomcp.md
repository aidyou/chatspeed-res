---
title: "BioMCP 生物医学模型上下文协议工具"
description: "通过模型上下文协议为大型语言模型提供对关键生物医学数据库（包括PubTator3（PubMed/PMC）、ClinicalTrials.gov和MyVariant.info）的结构化访问。"
---

# BioMCP 生物医学模型上下文协议工具

通过模型上下文协议为大型语言模型提供对关键生物医学数据库（包括PubTator3（PubMed/PMC）、ClinicalTrials.gov和MyVariant.info）的结构化访问。

# BioMCP: 生物医学模型上下文协议

BioMCP 是一个开源（MIT 许可证）工具包，它为 AI 助手和代理提供了专门的生物医学知识。它遵循模型上下文协议 (MCP) 构建，将 AI 系统连接到权威的生物医学数据源，使它们能够精准且深入地回答关于临床试验、科学文献和基因变异的问题。

[Watch video](https://www.youtube.com/watch?v=bKxOWrWUUhM)

## 为什么选择 BioMCP？

虽然大型语言模型具有广泛的一般知识，但它们通常缺乏特定领域的专业知识或访问最新资源的能力。BioMCP 通过以下方式填补了生物医学领域的这一空白：

- 提供**结构化访问**临床试验、生物医学文献和基因变异
- 支持对专业数据库进行**自然语言查询**而无需了解其具体语法
- 通过一致的接口支持**生物医学研究**工作流程
- 作为 AI 助手和代理的**MCP 服务器**运行

## 生物医学数据源

BioMCP 集成了三个关键的生物医学数据源：

- **PubTator3/PubMed** - 带有实体注释的生物医学文献
- **ClinicalTrials.gov** - 临床试验注册表和结果数据库
- **MyVariant.info** - 来自多个数据库的综合遗传变异注释

## 可用的 MCP 工具

### PubMed & PubTator3

- `article_searcher`: 按基因、疾病、变异或关键词搜索文章
- `article_details`: 获取包括摘要和全文在内的详细文章信息

### ClinicalTrials.gov

- `trial_searcher`: 通过条件、干预、阶段等进行高级试验搜索
- `trial_protocol`: 详细的试验方案信息
- `trial_locations`: 试验地点和联系信息
- `trial_outcomes`: 结果和结局指标
- `trial_references`: 相关出版物

### MyVariant.info

- `variant_searcher`: 使用复杂的过滤器搜索遗传变异
- `variant_details`: 来自多个来源的全面注释（CIViC, ClinVar, COSMIC, dbSNP 等）

## 快速开始

### 对于 Claude Desktop 用户

1. 如果还没有安装 `uv`（推荐），请先**安装 `uv`**：

```bash
   # MacOS
   brew install uv

   # Windows/Linux
   pip install uv
```

2. **配置 Claude Desktop**：
   - 打开 Claude Desktop 设置
   - 导航到开发者部分
   - 点击“编辑配置”并添加：
```json
   {
     "mcpServers": {
       "biomcp": {
         "command": "uv",
         "args": ["run", "--with", "biomcp-python", "biomcp", "run"]
       }
     }
   }
```
   - 重启 Claude Desktop 并开始讨论生物医学话题！

### Python 包安装

```bash
# Using pip
pip install biomcp-python

# Using uv (recommended for faster installation)
uv pip install biomcp-python

# Run directly without installation
uv run --with biomcp-python biomcp trial search --condition "lung cancer"
```

## 命令行界面

BioMCP 提供了一个全面的 CLI 以直接与数据库交互：

```bash
# Get help
biomcp --help

# Run the MCP server
biomcp run

# Examples
biomcp article search --gene BRAF --disease Melanoma
biomcp article get 21717063 --full
biomcp trial search --condition "Lung Cancer" --phase PHASE3
biomcp trial get NCT04280705 Protocol
biomcp variant search --gene TP53 --significance pathogenic
biomcp variant get rs113488022
```

## 测试与验证

使用 MCP Inspector 测试您的 BioMCP 设置：

```bash
npx @modelcontextprotocol/inspector uv run --with biomcp-python biomcp run
```

这将打开一个网页界面，您可以在其中探索和测试所有可用工具。

## 企业版：OncoMCP

OncoMCP 在 BioMCP 的基础上扩展了 GenomOncology 的企业级精准肿瘤平台（POP），提供以下功能：

- **符合 HIPAA 的部署**：安全的本地部署选项
- **实时试验匹配**：最新状态和分组级别匹配
- **医疗集成**：无缝 EHR 和数据仓库连接
- **精选知识库**：15,000 多项试验和 FDA 批准
- **高级患者匹配**：使用集成的临床和分子档案
- **高级 NLP**：从非结构化文本中进行结构化提取
- **全面的生物标志物处理**：突变和规则处理

了解更多：[GenomOncology](https://genomoncology.com/)

## MCP 注册表

[Smithery](https://smithery.ai/server/@genomoncology/biomcp)

## 文档

如需完整的文档，请访问 [https://biomcp.org](https://biomcp.org)

## BioMCP 示例仓库

想看看 BioMCP 的实际应用吗？

请查看配套仓库：
👉 **[biomcp-examples](https://github.com/genomoncology/biomcp-examples)**

该仓库包含真实的提示、AI 生成的研究简报以及不同模型的评估运行。
您可以使用它来探索功能、比较输出或基准测试您的设置。

有自己的精彩示例？
**我们非常欢迎您贡献！** 只需 fork 该仓库并提交带有您实验的 PR 即可。

## 许可证

本项目采用 MIT 许可证。

**官方网站：** [https://github.com/genomoncology/biomcp](https://github.com/genomoncology/biomcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`, `data`
- 标签：`research and data`, `search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`run --with biomcp-python biomcp run`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/genomoncology-biomcp.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
