---
title: "Obsidian MCP 服务器"
description: "通过模型上下文协议，启用大型语言模型（LLMs）与Obsidian仓库之间的交互，支持安全的文件操作、内容管理和高级搜索功能。"
---

# Obsidian MCP 服务器

通过模型上下文协议，启用大型语言模型（LLMs）与Obsidian仓库之间的交互，支持安全的文件操作、内容管理和高级搜索功能。

# Obsidian MCP 服务器

[![TypeScript](/mcp-assets/49904649f602ceb829cc76dcf6be1703.svg)](https://www.typescriptlang.org/)
[![Model Context Protocol](/mcp-assets/15df3c754569f46c1a9b6856e5620bf8.svg)](https://modelcontextprotocol.io/)
[![Version](/mcp-assets/46be73c54a6f0d67a0045d4edeb92e7d.svg)]()
[![License](/mcp-assets/fa73b4786cfc281bb30f39f895ada091.svg)](https://opensource.org/licenses/Apache-2.0)
[![Status](/mcp-assets/d3182a787ddabc121c1e54b8d1c66233.svg)]()
[![GitHub](/mcp-assets/d0665bdc934c169f40d0d593787b9bb2.svg)](https://github.com/cyanheads/obsidian-mcp-server)

一个为 LLMs 设计的 Model Context Protocol 服务器，用于与 Obsidian 仓库交互。该服务器使用 TypeScript 构建，具备安全的 API 通信、高效的文件操作和全面的搜索功能，使 AI 助手能够通过简洁灵活的工具界面无缝管理知识库。

Model Context Protocol (MCP) 使 AI 模型能够通过标准化接口与外部工具和资源进行交互。

需要在 Obsidian 中启用 Local REST API 插件。

## 功能

### 文件操作

- 带验证的原子文件/目录操作
- 资源监控和清理
- 错误处理和优雅失败

### 搜索系统

- 可配置上下文的全文搜索
- 高级 JsonLogic 查询支持文件、标签和元数据
- 支持 glob 模式和 frontmatter 字段

### 属性管理

- YAML frontmatter 解析和智能合并
- 自动生成时间戳（由 Obsidian 创建，由服务器修改）
- 自定义字段支持

### 安全与性能

- 带速率限制和 SSL 选项的 API 密钥认证
- 资源监控和健康检查
- 优雅关闭处理

## 安装

注意：需要 Node.js

1. 在 Obsidian 中启用 Local REST API 插件
2. 克隆并构建：

```bash
git clone git@github.com:cyanheads/obsidian-mcp-server.git
cd obsidian-mcp-server
npm install
npm run build
```

或者从 npm 安装：

```bash
npm install obsidian-mcp-server
```

## 配置

将以下内容添加到您的 MCP 客户端设置中（例如 `claude_desktop_config.json` 或 `cline_mcp_settings.json`）：

```json
{
  "mcpServers": {
    "obsidian-mcp-server": {
      "command": "node",
      "args": ["/path/to/obsidian-mcp-server/build/index.js"],
      "env": {
        "OBSIDIAN_API_KEY": "your_api_key_here",
        "VERIFY_SSL": "false",
        "OBSIDIAN_PROTOCOL": "https",
        "OBSIDIAN_HOST": "127.0.0.1",
        "OBSIDIAN_PORT": "27124",
        "REQUEST_TIMEOUT": "5000",
        "MAX_CONTENT_LENGTH": "52428800",
        "MAX_BODY_LENGTH": "52428800",
        "RATE_LIMIT_WINDOW_MS": "900000",
        "RATE_LIMIT_MAX_REQUESTS": "200",
        "TOOL_TIMEOUT_MS": "60000"
      }
    }
  }
}
```

环境变量：

必需：

- `OBSIDIAN_API_KEY`: 从 Obsidian 的 Local REST API 插件设置中获取的 API 密钥

连接设置：

- `VERIFY_SSL`: 启用 SSL 证书验证（默认: false） # 对于自签名证书，必须设置为 false。如果您是本地运行或不理解这是什么意思，应将其设置为 false。
- `OBSIDIAN_PROTOCOL`: 使用的协议（默认: "https"）
- `OBSIDIAN_HOST`: 主机地址（默认: "127.0.0.1"）
- `OBSIDIAN_PORT`: 端口号（默认: 27124）

请求限制：

- `REQUEST_TIMEOUT`: 请求超时时间（以毫秒为单位，默认: 5000）
- `MAX_CONTENT_LENGTH`: 最大响应内容长度（以字节为单位，默认: 52428800 [50MB]）
- `MAX_BODY_LENGTH`: 最大请求体长度（以字节为单位，默认: 52428800 [50MB]）

速率限制：

- `RATE_LIMIT_WINDOW_MS`: 速率限制窗口（以毫秒为单位，默认: 900000 [15 分钟]）
- `RATE_LIMIT_MAX_REQUESTS`: 每个窗口的最大请求数（默认: 200）

工具执行：

- `TOOL_TIMEOUT_MS`: 工具执行超时时间（以毫秒为单位，默认：60000 [1分钟]）

## 项目结构

该项目遵循模块化架构，职责分明：

```
src/
  ├── index.ts          # Main entry point
  ├── mcp/              # MCP server implementation
  ├── obsidian/         # Obsidian API client and types
  ├── resources/        # MCP resource implementations
  ├── tools/            # MCP tool implementations
  │   ├── files/        # File operations tools
  │   ├── search/       # Search tools
  │   └── properties/   # Property management tools
  └── utils/            # Shared utilities
```

## 工具

### 文件管理

```typescript
// List vault contents
obsidian_list_files_in_vault: {
}

// List directory contents
obsidian_list_files_in_dir: {
  dirpath: string; // Path relative to vault root
}

// Get file contents
obsidian_get_file_contents: {
  filepath: string; // Path relative to vault root
}
```

### 搜索操作

```typescript
// Text search with context
obsidian_find_in_file: {
  query: string,
  contextLength?: number  // Default: 10
}

// Advanced search with JsonLogic
obsidian_complex_search: {
  query: JsonLogicQuery
  // Examples:
  // Find by tag:
  // {"in": ["#mytag", {"var": "frontmatter.tags"}]}
  //
  // Find markdown files in a directory:
  // {"glob": ["docs/*.md", {"var": "path"}]}
  //
  // Combine conditions:
  // {"and": [
  //   {"glob": ["*.md", {"var": "path"}]},
  //   {"in": ["#mytag", {"var": "frontmatter.tags"}]}
  // ]}
}

// Get all tags in vault or directory
obsidian_get_tags: {
  path?: string  // Optional: limit to specific directory
}
```

### 内容修改

```typescript
// Append to file
obsidian_append_content: {
  filepath: string,  // Path relative to vault root
  content: string    // Content to append
}

// Update file content
obsidian_patch_content: {
  filepath: string,  // Path relative to vault root
  content: string    // New content (replaces existing)
}
```

### 属性管理

```typescript
// Get note properties
obsidian_get_properties: {
  filepath: string  // Path relative to vault root
}

// Update note properties
obsidian_update_properties: {
  filepath: string,  // Path relative to vault root
  properties: {
    title?: string,
    author?: string,
    // Note: created/modified timestamps are managed automatically
    type?: Array,
    tags?: string[],  // Must start with #
    status?: Array,
    version?: string,
    platform?: string,
    repository?: string,  // URL
    dependencies?: string[],
    sources?: string[],
    urls?: string[],      // URLs
    papers?: string[],
    custom?: Record
  }
}
```

## 最佳实践

### 文件操作

- 使用带有验证的原子操作
- 处理错误并监控性能

### 搜索实现

- 根据任务选择合适的搜索工具：
  - 对于文本搜索使用 obsidian_find_in_file
  - 对于元数据/标签过滤使用 obsidian_complex_search
- 保持上下文大小合理（默认：10个字符）

### 属性管理

- 使用适当的类型并验证更新
- 正确处理数组和自定义字段
- 绝不手动设置时间戳（自动管理）

### 错误预防

- 验证输入并优雅地处理错误
- 监控模式并遵守速率限制

## 资源

MCP 服务器公开以下资源：

```
obsidian://tags  # List of all tags used across the vault
```

## 贡献

1. 分叉仓库
2. 创建特性分支
3. 提交 Pull Request

对于 Bug 和新功能，请在 [https://github.com/cyanheads/obsidian-mcp-server/issues](https://github.com/cyanheads/obsidian-mcp-server/issues) 创建问题。

## 发布

当推送版本标签时，包会自动发布到 npm：

```bash
# Update version in package.json
npm version patch  # or minor, or major
git push --follow-tags
```

这将触发 GitHub Action 来构建和发布包。

## 许可证

Apache License 2.0

---

使用 Model Context Protocol 构建

**官方网站：** [https://github.com/cyanheads/obsidian-mcp-server](https://github.com/cyanheads/obsidian-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`, `files`
- 标签：`file systems`, `note taking`, `search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`/path/to/obsidian-mcp-server/build/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/cyanheads-obsidian.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
