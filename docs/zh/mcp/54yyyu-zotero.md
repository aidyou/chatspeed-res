---
title: "Zotero MCP工具"
description: "通过模型上下文协议将您的Zotero研究库与克劳德和其他人工智能助手连接起来，使您能够搜索您的库、访问内容、讨论论文、获取摘要和分析引文。"
---

# Zotero MCP工具

通过模型上下文协议将您的Zotero研究库与克劳德和其他人工智能助手连接起来，使您能够搜索您的库、访问内容、讨论论文、获取摘要和分析引文。

# Zotero MCP: 您的研究库在 Claude 中

  

    

  

  

    

  

  

    

  

**Zotero MCP** 通过 [Model Context Protocol](https://modelcontextprotocol.io/introduction) 无缝连接您的 [Zotero](https://www.zotero.org/) 研究库与 [Claude](https://www.anthropic.com/claude) 及其他 AI 助手（如 [Cherry Studio](https://cherry-ai.com/), [Cursor](https://www.cursor.com/) 等）。您可以讨论论文、获取摘要、分析引用、提取 PDF 注释等！

## ✨ 功能

### 🔍 搜索您的图书馆
- 通过标题、作者或内容查找论文、文章和书籍
- 使用多个条件进行复杂搜索
- 浏览集合、标签和最近添加的内容

### 📚 访问您的内容
- 获取任何项目的详细元数据
- 获取全文内容（如果可用）
- 访问附件、笔记和子项目

### 📝 处理注释
- 直接提取和搜索 PDF 注释
- 访问 Zotero 的原生注释
- 创建和更新笔记和注释

### 🌐 灵活的访问方法
- 本地方法，适用于离线访问（无需 API 密钥）
- Web API 用于云库访问
- 既适合本地研究也适合远程协作

## 🚀 快速安装

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@54yyyu/zotero-mcp) 自动为 Claude Desktop 安装 Zotero MCP：

```bash
npx -y @smithery/cli install @54yyyu/zotero-mcp --client claude
```

### 手动安装

#### 通过 uv 安装

```bash
uv tool install "git+https://github.com/54yyyu/zotero-mcp.git"
zotero-mcp setup  # Auto-configure for Claude Desktop
```

#### 通过 pip 安装

```bash
pip install git+https://github.com/54yyyu/zotero-mcp.git
zotero-mcp setup  # Auto-configure for Claude Desktop
```

## 🖥️ 设置与使用

完整文档请参阅 [Zotero MCP 文档](https://stevenyuyy.us/zotero-mcp/)。

**要求**
- Python 3.10+
- Zotero 7+（用于具有全文访问权限的本地 API）
- Claude Desktop 或兼容的 AI 助手

### 对于 Claude Desktop

#### 配置
安装后，您可以选择：

1. **自动配置**（推荐）：
```bash
   zotero-mcp setup
```

2. **手动配置**：
   在您的 `claude_desktop_config.json` 文件中添加以下内容：
```json
   {
     "mcpServers": {
       "zotero": {
         "command": "zotero-mcp",
         "env": {
           "ZOTERO_LOCAL": "true"
         }
       }
     }
   }
```

#### 使用

1. 启动 Zotero 桌面版（确保在偏好设置中启用了本地 API）
2. 启动 Claude Desktop
3. 通过 Claude Desktop 的工具界面访问 Zotero-MCP 工具

示例提示：

- "在我的图书馆中搜索关于机器学习的论文"
- "找到我最近添加的关于气候变化的文章"
- "总结我关于量子计算的论文中的关键发现"
- "从我的神经网络论文中提取所有PDF注释"
- "在我的笔记和注释中搜索提到'强化学习'的内容"

### 对于 Cherry Studio

#### 配置
前往设置 -> MCP 服务器 -> 编辑 MCP 配置，并添加以下内容：

```json
{
  "mcpServers": {
    "zotero": {
      "name": "zotero",
      "type": "stdio",
      "isActive": true,
      "command": "zotero-mcp",
      "args": [],
      "env": {
        "ZOTERO_LOCAL": "true"
      }
    }
  }
}
```
然后点击“保存”。

Cherry Studio 还提供了用于常规设置和工具选择的可视化配置方法。

## 🔧 高级配置

### 使用 Web API 而不是本地 API

为了通过 Web API 访问您的 Zotero 图书馆（对于远程设置非常有用）：

```bash
zotero-mcp setup --no-local --api-key YOUR_API_KEY --library-id YOUR_LIBRARY_ID
```

### 环境变量

- `ZOTERO_LOCAL=true`: 使用本地 Zotero API（默认：false）
- `ZOTERO_API_KEY`: 您的 Zotero API 密钥（用于 Web API）
- `ZOTERO_LIBRARY_ID`: 您的 Zotero 图书馆 ID（用于 Web API）
- `ZOTERO_LIBRARY_TYPE`: 图书馆类型（用户或群组，默认：用户）

### 命令行选项

```bash
# Run the server directly
zotero-mcp serve

# Specify transport method
zotero-mcp serve --transport stdio|sse

# Get help on setup options
zotero-mcp setup --help
```

## 📑 PDF 注释提取

Zotero MCP 包含高级 PDF 注释提取功能：

- **直接 PDF 处理**: 直接从 PDF 文件中提取注释，即使它们尚未被 Zotero 索引
- **增强搜索**: 搜索 PDF 注释和评论
- **图像注释支持**: 从 PDF 中提取图像注释
- **无缝集成**: 与 Zotero 的原生注释系统协同工作

为了获得最佳的注释提取效果，**强烈建议**安装 [Better BibTeX 插件](https://retorque.re/zotero-better-bibtex/installation/)。注释相关功能主要是在此插件上进行测试，并在有此插件的情况下提供增强的功能。

首次使用 PDF 注释功能时，必要的工具将自动下载。

## 📚 可用工具

### 搜索工具
- `zotero_search_items`: 搜索您的图书馆
- `zotero_advanced_search`: 执行复杂搜索
- `zotero_get_collections`: 列出集合
- `zotero_get_collection_items`: 获取集合中的项目
- `zotero_get_tags`: 列出所有标签
- `zotero_get_recent`: 获取最近添加的项目

### 内容工具
- `zotero_get_item_metadata`: 获取详细元数据
- `zotero_get_item_fulltext`: 获取全文内容
- `zotero_get_item_children`: 获取附件和笔记

### 注释和笔记工具
- `zotero_get_annotations`: 获取注释（包括直接从 PDF 提取）
- `zotero_get_notes`: 从您的 Zotero 图书馆检索笔记
- `zotero_search_notes`: 在笔记和注释中搜索（包括从 PDF 提取的内容）
- `zotero_create_note`: 为某个项目创建新笔记（测试版功能）

## 🔍 故障排除

- **未找到结果**: 确保 Zotero 正在运行并且已启用本地 API
- **无法连接到图书馆**: 如果使用 Web API，请检查您的 API 密钥和图书馆 ID
- **全文不可用**: 确保您正在使用 Zotero 7+ 以访问本地全文

## 📄 许可证

MIT

**官方网站：** [https://github.com/54yyyu/zotero-mcp](https://github.com/54yyyu/zotero-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`, `data`
- 标签：`research and data`, `search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`zotero-mcp`
- 参数：无

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/54yyyu-zotero.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
