---
title: "学术搜索助手"
description: "启用从多个来源实时搜索和检索学术论文信息的功能，提供对论文元数据、摘要和全文内容（如有可用）的访问，并以结构化数据响应的形式提供，以便与支持工具/功能调用的AI模型进行集成。"
---

# 学术搜索助手

启用从多个来源实时搜索和检索学术论文信息的功能，提供对论文元数据、摘要和全文内容（如有可用）的访问，并以结构化数据响应的形式提供，以便与支持工具/功能调用的AI模型进行集成。

# 学术论文搜索 MCP 服务器

[Smithery](https://smithery.ai/server/@afrise/academic-search-mcp-server)

这是一个 [模型上下文协议 (MCP)](https://www.anthropic.com/news/model-context-protocol) 服务器，能够从多个来源搜索和检索学术论文信息。

该服务器为大型语言模型 (LLMs) 提供以下功能：
- 实时学术论文搜索功能
- 访问论文元数据和摘要
- 在可用时获取全文内容
- 遵循 MCP 规范的结构化数据响应

虽然该服务器主要设计用于与 Anthropic 的 Claude Desktop 客户端集成，但 MCP 规范允许其可能与其他支持工具/函数调用能力的人工智能模型和客户端兼容（例如 OpenAI 的 API）。

**注意**：此软件正在积极开发中。特性和功能可能会发生变化。

## 功能

该服务器提供了以下工具：
- `search_papers`：跨多个来源搜索学术论文
  - 参数：
    - `query` (str): 搜索查询文本
    - `limit` (int, 可选): 返回的最大结果数量（默认：10）
  - 返回：包含论文详情的格式化字符串
  
- `fetch_paper_details`：检索特定论文的详细信息
  - 参数：
    - `paper_id` (str): 论文标识符（DOI 或 Semantic Scholar ID）
    - `source` (str, 可选): 数据源 ("crossref" 或 "semantic_scholar", 默认: "crossref")
  - 返回：包含全面论文元数据的格式化字符串，包括：
    - 标题、作者、年份、DOI
    - 发表场所、开放访问状态、PDF URL（仅限 Semantic Scholar）
    - 摘要和 TL;DR 总结（如果可用）

- `search_by_topic`：按主题搜索论文，并可选择日期范围过滤
  - 参数：
    - `topic` (str): 搜索查询文本（限制在 300 个字符内）
    - `year_start` (int, 可选): 日期范围的起始年份
    - `year_end` (int, 可选): 日期范围的结束年份
    - `limit` (int, 可选): 返回的最大结果数量（默认：10）
  - 返回：包含搜索结果的格式化字符串，包括：
    - 论文标题、作者和年份
    - 摘要和 TL;DR 总结（如果可用）
    - 发表场所和开放访问信息

## 设置

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@afrise/academic-search-mcp-server) 自动为 Claude Desktop 安装学术论文搜索服务器：

```bash
npx -y @smithery/cli install @afrise/academic-search-mcp-server --client claude
```

***注意*** 此方法尚未经过大量测试，因为他们的服务器似乎遇到了一些问题。您可以按照独立安装说明操作，直到 Smithery 修复为止。

### 通过 uv 手动安装:

1. 安装依赖项：
```sh
uv add "mcp[cli]" httpx
```

2. 在您的环境或 `.env` 文件中设置所需的 API 密钥：
```sh
#  These are not actually implemented
SEMANTIC_SCHOLAR_API_KEY=your_key_here 
CROSSREF_API_KEY=your_key_here  # Optional but recommended
```

3. 运行服务器：
```sh
uv run server.py
```

## 与 Claude Desktop 的使用

1. 将服务器添加到您的 Claude Desktop 配置中 (`claude_desktop_config.json`)：
```json
{
  "mcpServers": {
    "academic-search": {
      "command": "uv",
      "args": ["run ", "/path/to/server/server.py"],
      "env": {
        "SEMANTIC_SCHOLAR_API_KEY": "your_key_here",
        "CROSSREF_API_KEY": "your_key_here"
      }
    }
  }
}
```

2. 重启 Claude Desktop

## 开发

此服务器使用以下技术构建：
- Python MCP SDK
- FastMCP 用于简化服务器实现
- httpx 用于 API 请求

## API 来源

- Semantic Scholar API
- Crossref API

## 许可证

本项目采用 GNU Affero General Public License v3.0 (AGPL-3.0) 许可证。该许可证确保：

- 您可以自由使用、修改和分发此软件
- 任何修改都必须以相同的许可证开源
- 使用此软件提供网络服务的任何人都必须公开源代码
- 允许商业使用，但软件及其衍生作品必须保持免费和开源

请参阅 [LICENSE](https://github.com/afrise/academic-search-mcp-server/blob/HEAD/LICENSE) 文件获取完整的许可证文本。

## 贡献

欢迎贡献！您可以按以下步骤帮助我们：

1. 叉取仓库
2. 创建一个功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交您的更改 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 打开一个 Pull Request

请注意：
- 遵循现有的代码风格和约定
- 为任何新功能添加测试
- 根据需要更新文档
- 确保您的更改遵守 AGPL-3.0 许可证条款

通过贡献此项目，您同意您的贡献将根据 AGPL-3.0 许可证进行授权。

**官方网站：** [https://github.com/afrise/academic-search-mcp-server](https://github.com/afrise/academic-search-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`, `data`
- 标签：`search`, `research and data`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`run  /path/to/server/server.py`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/afrise-academic-search.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
