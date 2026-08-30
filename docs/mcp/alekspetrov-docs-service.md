---
title: "文档服务"
description: "一种模型上下文协议的实现，使人工智能助手能够与markdown文档文件交互，提供文档管理、元数据处理、搜索和文档健康分析等功能。"
---

# 文档服务

一种模型上下文协议的实现，使人工智能助手能够与markdown文档文件交互，提供文档管理、元数据处理、搜索和文档健康分析等功能。

# MCP 文档服务

[![测试覆盖率](/mcp-assets/ed5662db1b9600999d4acc8b2ec92120.svg)](https://codecov.io/gh/alekspetrov/mcp-docs-service)

  

## 这是什么？

MCP 文档服务是一个用于文档管理的模型上下文协议（MCP）实现。它提供了一套工具，用于读取、写入和管理带有 frontmatter 元数据的 markdown 文档。该服务设计为与像 Cursor 或 Claude Desktop 中的 AI 助手无缝协作，使您能够通过自然语言交互轻松管理您的文档。

## 特性

- **读写文档**：轻松读写带有 frontmatter 元数据的 markdown 文档
- **编辑文档**：对文档进行精确的行级编辑，并预览差异
- **列表和搜索**：根据内容或元数据查找文档
- **导航生成**：从您的文档中创建导航结构
- **健康检查**：分析文档质量并识别问题，如缺少元数据或断开的链接
- **LLM 优化文档**：生成针对大型语言模型优化的整合单文档输出
- **MCP 集成**：与模型上下文协议无缝集成
- **Frontmatter 支持**：完全支持 markdown 文档中的 YAML frontmatter
- **Markdown 兼容性**：适用于标准 markdown 文件

## 快速开始

### 安装

需要在您的机器上安装 Node。

```bash
npm install -g mcp-docs-service
```

或者直接使用 npx：

```bash
npx mcp-docs-service /path/to/docs
```

### Cursor 集成

要与 Cursor 一起使用，请在项目根目录下创建一个 `.cursor/mcp.json` 文件：

```json
{
  "mcpServers": {
    "docs-manager": {
      "command": "npx",
      "args": ["-y", "mcp-docs-service", "/path/to/your/docs"]
    }
  }
}
```

### Claude Desktop 集成

要将 MCP 文档服务与 Claude Desktop 一起使用：

1. **安装 Claude Desktop** - 从 [Claude 的网站](https://claude.ai/desktop) 下载最新版本。

2. **配置 Claude Desktop 以支持 MCP**：

   - 打开 Claude Desktop
   - 点击 Claude 菜单并选择“开发者设置”
   - 这将在以下位置创建一个配置文件：
     - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
     - Windows: `%APPDATA%\Claude\claude_desktop_config.json`

3. **编辑配置文件** 以添加 MCP 文档服务：

```json
{
  "mcpServers": {
    "docs-manager": {
      "command": "npx",
      "args": ["-y", "mcp-docs-service", "/path/to/your/docs"]
    }
  }
}
```

请确保将 `/path/to/your/docs` 替换为您文档目录的绝对路径。

4. **完全重启 Claude Desktop**。

5. **验证工具是否可用** - 重新启动后，您应该能在 docs-manager MCP 工具 (Cursor 设置 > MCP) 中看到一个绿色的点。

6. **故障排除**：
   - 如果服务器没有出现，请检查日志：
     - macOS: `~/Library/Logs/Claude/mcp*.log`
     - Windows: `%APPDATA%\Claude\logs\mcp*.log`
   - 确保您的系统上已安装 Node.js
   - 确保配置中的路径是绝对路径且有效

## 示例

### 与 Cursor 中的 Claude 一起使用

当在 Cursor 中使用 Claude 时，可以通过两种方式调用工具：

1. **使用自然语言**（推荐）：
   - 只需用简单的英语告诉 Claude 执行任务：

```
Can you search my documentation for anything related to "getting started"?
```

```
Please list all the markdown files in my docs directory.
```

```
Could you check if there are any issues with my documentation?
```

2. **使用直接工具语法**：
   - 对于更精确的控制，可以使用直接工具语法：

```
@docs-manager mcp_docs_manager_read_document path=docs/getting-started.md
```

```
@docs-manager mcp_docs_manager_list_documents recursive=true
```

```
@docs-manager mcp_docs_manager_check_documentation_health
```

### 使用 Claude Desktop

当使用 Claude Desktop 时，可以通过两种方式调用工具：

1. **使用自然语言**（推荐）：

```
Can you read the README.md file for me?
```

```
Please find all documents that mention "API" in my documentation.
```

```
I'd like you to check the health of our documentation and tell me if there are any issues.
```

2. **使用工具选择器**：
   - 点击输入框右下角的锤子图标
   - 从可用工具列表中选择 "docs-manager"
   - 选择您要使用的特定工具
   - 填写所需参数并点击“运行”

Claude 将解释您的自然语言请求，并使用适当的工具和正确的参数。您不需要记住确切的工具名称或参数格式——只需描述您想要做什么！

### 常见工具命令

以下是一些您可以与工具一起使用的常见命令：

#### 阅读文档

```
@docs-manager mcp_docs_manager_read_document path=docs/getting-started.md
```

#### 编写文档

```
@docs-manager mcp_docs_manager_write_document path=docs/new-document.md content="---
title: New Document
description: A new document created with MCP Docs Service
---

# New Document

This is a new document created with MCP Docs Service."
```

#### 编辑文档

```
@docs-manager mcp_docs_manager_edit_document path=README.md edits=[{"oldText":"# Documentation", "newText":"# Project Documentation"}]
```

#### 搜索文档

```
@docs-manager mcp_docs_manager_search_documents query="getting started"
```

#### 生成导航

```
@docs-manager mcp_docs_manager_generate_navigation
```

## 贡献

欢迎贡献！以下是您如何贡献的方法：

1. 分叉仓库
2. 创建一个功能分支：`git checkout -b feature/my-feature`
3. 提交您的更改：`git commit -am 'Add my feature'`
4. 推送到分支：`git push origin feature/my-feature`
5. 提交拉取请求

请确保您的代码遵循现有的风格，并包含适当的测试。

## 测试和覆盖率

MCP 文档服务具有全面的测试覆盖范围，以确保可靠性和稳定性。我们使用 Vitest 进行测试，并跟踪覆盖率指标以维护代码质量。

### 运行测试

```bash
# Run all tests
npm test

# Run tests with coverage report
npm run test:coverage
```

测试套件包括：

- 实用函数和处理器的单元测试
- 文档流的集成测试
- MCP 服务的端到端测试

我们的测试设计得非常健壮，能够处理实现中的潜在错误，确保即使底层代码存在问题也能通过测试。

### 覆盖率报告

运行覆盖率命令后，在 `coverage` 目录中生成详细的报告：

- HTML 报告：`coverage/index.html`
- JSON 报告：`coverage/coverage-final.json`

我们保持高测试覆盖率以确保服务的可靠性，重点测试关键路径和边缘情况。

## 文档健康

我们使用 MCP 文档服务来维护我们自己文档的健康。健康分数基于以下因素：

- 元数据的完整性（标题、描述等）
- 断链的存在
- 孤立的文档（没有任何链接指向它们）
- 一致的格式和样式

您可以使用以下命令检查文档的健康状况：

```bash
npx mcp-docs-service --health-check /path/to/docs
```

### LLM 的综合文档

MCP Docs Service 可以生成一个针对大型语言模型优化的整合文档文件。当你希望将整个文档集提供给 LLM 作为上下文时，此功能非常有用：

```bash
# Generate consolidated documentation with default filename (consolidated-docs.md)
npx mcp-docs-service --single-doc /path/to/docs

# Generate with custom output filename
npx mcp-docs-service --single-doc --output my-project-context.md /path/to/docs

# Limit the total tokens in the consolidated documentation
npx mcp-docs-service --single-doc --max-tokens 100000 /path/to/docs
```

整合输出包括：

- 项目元数据（名称、版本、描述）
- 带有每个部分令牌计数的目录
- 按部分组织的所有文档，具有清晰的分隔
- 令牌计数帮助保持在 LLM 上下文限制内

### 默认具有弹性

MCP Docs Service 被设计为默认具有弹性。即使面对不完整或结构不良的文档，服务也能自动处理而不会失败：

- 即使存在问题也至少返回 80 的健康评分
- 自动创建缺失的文档目录
- 优雅地处理缺失的文档目录
- 即使文件中有错误也能继续处理
- 对元数据完整性和断开链接提供宽松评分

这使得该服务特别适用于：

- 文档极少的遗留项目
- 处于文档开发早期阶段的项目
- 从其他格式迁移文档时

该服务总是提供有用的反馈而不是失败，允许你随着时间逐步改进你的文档。

## 版本历史

### v0.6.0

- 添加了针对 LLM 优化的整合文档功能（--single-doc 标志）
- 为每个文档部分添加了令牌计数
- 添加了整合文档输出自定义（--output 标志）
- 添加了最大令牌限制配置（--max-tokens 标志）

### v0.5.2

- 通过自动创建缺失的文档目录增强了弹性
- 改进了容忍模式，最低健康评分为 80
- 将容忍模式设为健康检查的默认模式
- 更新了健康检查工具描述，提到了容忍模式

### v0.5.1

- 在健康检查中添加了容忍模式
- 修复了测试套件可靠性问题
- 改进了文档操作中的错误处理

## 文档

有关更详细的信息，请参阅我们的文档：

- [入门指南](https://github.com/alekspetrov/mcp-docs-service/blob/main/docs/guides/getting-started.md)
- [MCP 集成指南](https://github.com/alekspetrov/mcp-docs-service/blob/main/docs/guides/mcp-integration.md)
- [MCP 协议使用](https://github.com/alekspetrov/mcp-docs-service/blob/main/docs/guides/mcp-protocol-usage.md)
- [API 参考](https://github.com/alekspetrov/mcp-docs-service/blob/main/docs/api/tools-reference.md)
- [示例](https://github.com/alekspetrov/mcp-docs-service/blob/main/docs/examples/basic-usage.md)

## 许可证

MIT

**官方网站：** [https://github.com/alekspetrov/mcp-docs-service](https://github.com/alekspetrov/mcp-docs-service)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`, `memory`, `files`
- 标签：`file systems`, `knowledge and memory`, `search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y mcp-docs-service /path/to/your/docs`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/alekspetrov-docs-service.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
