---
title: "MCP PDF阅读器"
description: "赋予AI代理在项目背景下使用灵活的MCP工具安全地从PDF文件中读取和提取信息（文本、元数据、页数）的能力。"
---

# MCP PDF阅读器

赋予AI代理在项目背景下使用灵活的MCP工具安全地从PDF文件中读取和提取信息（文本、元数据、页数）的能力。

# PDF Reader MCP Server (@sylphlab/pdf-reader-mcp)

[![CI/CD Pipeline](/mcp-assets/b08d60102e2f72d9463fb5b1cb30fe6a.svg)](https://github.com/sylphlab/pdf-reader-mcp/actions/workflows/ci.yml)
[![codecov](/mcp-assets/9bb81fc5c61a436fc1cd92623a5129d9.svg)](https://codecov.io/gh/sylphlab/pdf-reader-mcp)
[![npm version](/mcp-assets/324b28f2272adfc508dc257fdc812e85.svg)](https://badge.fury.io/js/%40sylphlab%2Fpdf-reader-mcp)
[![Docker Pulls](/mcp-assets/dfdae949fb9b905b5571a7a6d41a6870.svg)](https://hub.docker.com/r/sylphlab/pdf-reader-mcp)
[![License: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)

赋予您的AI代理（如Cline）使用单一、灵活的工具在项目上下文中安全地读取和提取PDF文件中的信息（文本、元数据、页数）的能力。

  

## 安装

### 使用 npm (推荐)

在您的MCP主机环境或项目中作为依赖项安装：

```bash
pnpm add @sylphlab/pdf-reader-mcp # Or npm install / yarn add
```

配置您的MCP主机（例如，`mcp_settings.json`）以使用 `npx`：

```json
{
  "mcpServers": {
    "pdf-reader-mcp": {
      "command": "npx",
      "args": ["@sylphlab/pdf-reader-mcp"],
      "name": "PDF Reader (npx)"
    }
  }
}
```

_(确保主机为目标项目设置了正确的 `cwd`)_ 

### 使用 Docker

拉取镜像：

```bash
docker pull sylphlab/pdf-reader-mcp:latest
```

配置您的MCP主机以运行容器，并将您的项目目录挂载到 `/app`：

```json
{
  "mcpServers": {
    "pdf-reader-mcp": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-v",
        "/path/to/your/project:/app", // Or use "$PWD:/app", "%CD%:/app", etc.
        "sylphlab/pdf-reader-mcp:latest"
      ],
      "name": "PDF Reader (Docker)"
    }
  }
}
```

### 本地构建 (用于开发)

1. 克隆: `git clone https://github.com/sylphlab/pdf-reader-mcp.git`
2. 安装: `cd pdf-reader-mcp && pnpm install`
3. 构建: `pnpm run build`
4. 配置MCP主机:
```json
   {
     "mcpServers": {
       "pdf-reader-mcp": {
         "command": "node",
         "args": ["/path/to/cloned/repo/pdf-reader-mcp/build/index.js"],
         "name": "PDF Reader (Local Build)"
       }
     }
   }
```
   _(确保主机为目标项目设置了正确的 `cwd`)_ 

## 快速开始

假设服务器正在运行并在您的MCP主机中已配置：

**MCP 请求 (从本地PDF获取元数据和第2页文本):**

```json
{
  "tool_name": "read_pdf",
  "arguments": {
    "sources": [
      {
        "path": "./documents/my_report.pdf",
        "pages": [2]
      }
    ],
    "include_metadata": true,
    "include_page_count": false, // Default is true, explicitly false here
    "include_full_text": false // Ignored because 'pages' is specified
  }
}
```

**预期响应片段:**

```json
{
  "results": [
    {
      "source": "./documents/my_report.pdf",
      "success": true,
      "data": {
        "page_texts": [
          { "page": 2, "text": "Text content from page 2..." }
        ],
        "info": { ... },
        "metadata": { ... }
        // num_pages not included as requested
      }
    }
  ]
}
```

## 为什么选择这个项目？

- **🛡️ 安全:** 严格限制文件访问仅限于项目根目录。
- **🌐 灵活:** 同时处理本地相对路径和公共URL。
- **🧩 综合:** 单一的 `read_pdf` 工具满足多种提取需求（全文、特定页面、元数据、页数）。
- **⚙️ 结构化输出:** 返回的数据采用可预测的JSON格式，易于代理解析。
- **🚀 易于集成:** 通过 `npx` 或 Docker 在MCP环境中无缝使用设计。
- **✅ 健壮:** 使用 `pdfjs-dist` 进行可靠的解析和Zod进行输入验证。

## 性能优势

使用Vitest对示例PDF进行的初步基准测试显示，各种操作处理效率高：

| 场景                         | 每秒操作次数 (hz) | 相对速度 |
| :------------------------------- | :------------------------- | :------------- |
| 处理不存在的文件         | ~12,933                    | 最快        |
| 获取全文本                    | ~5,575                     |                |
| 获取特定页（第1页）       | ~5,329                     |                |
| 获取特定页（第1和第2页） | ~5,242                     |                |
| 获取元数据及页数        | ~4,912                     | 最慢        |

_(更高的 hz 值表示更好的性能。结果可能因 PDF 的复杂性和环境而异。)_

有关更多详细信息和未来计划，请参阅[性能文档](https://github.com/shtse8/pdf-reader-mcp/blob/HEAD/docs/performance/index.md)。

## 功能

- 从 PDF 文件中读取完整文本内容。
- 从特定页面或页面范围读取文本内容。
- 读取 PDF 元数据（作者、标题、创建日期等）。
- 获取 PDF 的总页数。
- 在单个请求中处理多个 PDF 源（本地路径或 URL）。
- 在定义的项目根目录内安全运行。
- 通过 MCP 提供结构化的 JSON 输出。
- 可通过 npm 和 Docker Hub 获取。

## 设计理念

服务器通过上下文限制优先考虑安全性，通过结构化数据传输提高效率，并且设计简单以便于集成到 AI 代理工作流程中。它力求最少依赖项，依靠强大的 `pdfjs-dist` 库。

查看完整的[设计理念](https://github.com/shtse8/pdf-reader-mcp/blob/HEAD/docs/design/index.md)文档。

## 与其他解决方案的比较

与直接文件访问（通常不可行）或通用文件系统工具相比，此服务器提供了专门针对 PDF 的解析能力。与外部 CLI 工具（例如 `pdftotext`）不同，它提供了一个安全的集成 MCP 接口，并具有结构化的输出，增强了 AI 代理的可靠性和易用性。

查看完整的[比较](https://github.com/shtse8/pdf-reader-mcp/blob/HEAD/docs/comparison/index.md)文档。

## 未来计划（路线图）

- **文档：**
  - 完成所有文档部分（指南、API、设计、比较）。
  - 解决 TypeDoc 问题并生成 API 文档。
  - 添加更多示例和高级使用模式。
  - 实现 PWA 支持和文档站点的移动优化。
  - 向文档站点添加分享按钮和增长指标。
- **基准测试：**
  - 使用多样化的 PDF 文件（大小、复杂性）进行全面基准测试。
  - 测量内存使用情况。
  - 比较 URL 与本地文件的性能。
- **核心功能：**
  - 探索针对非常大的 PDF 文件的潜在优化。
  - 调查提取图像或注释的选项（长期目标）。
- **测试：**
  - 尽可能将测试覆盖率提高到 100%。
  - 一旦可行，添加运行时测试。

## 文档

有关详细的使用说明、API 参考和指南，请访问**[完整文档网站](https://sylphlab.github.io/pdf-reader-mcp/)**（部署后更新链接）。

## 社区与支持

- **发现错误或有功能请求？** 请在 [GitHub Issues](https://github.com/sylphlab/pdf-reader-mcp/issues) 上提出问题。
- **想要贡献代码？** 我们欢迎贡献！请参阅 [CONTRIBUTING.md](https://github.com/shtse8/pdf-reader-mcp/blob/HEAD/CONTRIBUTING.md)。
- **点赞 & 关注：** 如果您觉得这个项目有用，请考虑在 [GitHub](https://github.com/sylphlab/pdf-reader-mcp) 上为仓库点个星 ⭐ 并关注 👀，以表示您的支持并保持更新！

## 许可证

本项目采用 [MIT 许可证](https://github.com/shtse8/pdf-reader-mcp/blob/HEAD/LICENSE)。

**官方网站：** [https://github.com/shtse8/pdf-reader-mcp](https://github.com/shtse8/pdf-reader-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`files`
- 标签：`file systems`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`@sylphlab/pdf-reader-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/sylphlab-pdf-reader.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
