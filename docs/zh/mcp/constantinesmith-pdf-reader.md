---
title: "pdf阅读"
description: "该项目为AI代理提供了一个安全且灵活的工具，用于从PDF文件中读取和提取信息。它支持全文、特定页面、元数据和页数提取。服务器可以通过npm、Docker或本地构建集成到MCP环境中。"
---

# pdf阅读

该项目为AI代理提供了一个安全且灵活的工具，用于从PDF文件中读取和提取信息。它支持全文、特定页面、元数据和页数提取。服务器可以通过npm、Docker或本地构建集成到MCP环境中。

# PDF Reader MCP Server (@sylphlab/pdf-reader-mcp)

[![CI/CD Pipeline](/mcp-assets/b08d60102e2f72d9463fb5b1cb30fe6a.svg)](https://github.com/sylphlab/pdf-reader-mcp/actions/workflows/ci.yml)
[![codecov](/mcp-assets/9bb81fc5c61a436fc1cd92623a5129d9.svg)](https://codecov.io/gh/sylphlab/pdf-reader-mcp)
[![npm version](/mcp-assets/324b28f2272adfc508dc257fdc812e85.svg)](https://badge.fury.io/js/%40sylphlab%2Fpdf-reader-mcp)
[![Docker Pulls](/mcp-assets/dfdae949fb9b905b5571a7a6d41a6870.svg)](https://hub.docker.com/r/sylphlab/pdf-reader-mcp)
[![License: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)

Empower your AI agents (like Cline) with the ability to securely read and extract information (text, metadata, page count) from PDF files within your project context using a single, flexible tool.

  

## Installation

### Using npm (Recommended)

Install as a dependency in your MCP host environment or project:

```bash
pnpm add @sylphlab/pdf-reader-mcp # Or npm install / yarn add
```

Configure your MCP host (e.g., `mcp_settings.json`) to use `npx`:

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

_(Ensure the host sets the correct `cwd` for the target project)_

### Using Docker

Pull the image:

```bash
docker pull sylphlab/pdf-reader-mcp:latest
```

Configure your MCP host to run the container, mounting your project directory to `/app`:

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

### Local Build (For Development)

1. Clone: `git clone https://github.com/sylphlab/pdf-reader-mcp.git`
2. Install: `cd pdf-reader-mcp && pnpm install`
3. Build: `pnpm run build`
4. Configure MCP Host:
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
   _(Ensure the host sets the correct `cwd` for the target project)_

## Quick Start

Assuming the server is running and configured in your MCP host:

**MCP Request (Get metadata and page 2 text from a local PDF):**

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

**Expected Response Snippet:**

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

## Why Choose This Project?

- **🛡️ Secure:** Confines file access strictly to the project root directory.
- **🌐 Flexible:** Handles both local relative paths and public URLs.
- **🧩 Consolidated:** A single `read_pdf` tool serves multiple extraction needs (full text, specific pages, metadata, page count).
- **⚙️ Structured Output:** Returns data in a predictable JSON format, easy for agents to parse.
- **🚀 Easy Integration:** Designed for seamless use within MCP environments via `npx` or Docker.
- **✅ Robust:** Uses `pdfjs-dist` for reliable parsing and Zod for input validation.

## Performance Advantages

Initial benchmarks using Vitest on a sample PDF show efficient handling of various operations:

| Scenario                         | Operations per Second (hz) | Relative Speed |
| :------------------------------- | :------------------------- | :------------- |
| Handle Non-Existent File         | ~12,933                    | Fastest        |
| Get Full Text                    | ~5,575                     |                |
| Get Specific Page (Page 1)       | ~5,329                     |                |
| Get Specific Pages (Pages 1 & 2) | ~5,242                     |                |
| Get Metadata & Page Count        | ~4,912                     | Slowest        |

_(Higher hz indicates better performance. Results may vary based on PDF complexity and environment.)_

See the [Performance Documentation](https://github.com/sylphxltd/pdf-reader-mcp/blob/HEAD/docs/performance/index.md) for more details and future plans.

## Features

- Read full text content from PDF files.
- Read text content from specific pages or page ranges.
- Read PDF metadata (author, title, creation date, etc.).
- Get the total page count of a PDF.
- Process multiple PDF sources (local paths or URLs) in a single request.
- Securely operates within the defined project root.
- Provides structured JSON output via MCP.
- Available via npm and Docker Hub.

## Design Philosophy

The server prioritizes security through context confinement, efficiency via structured data transfer, and simplicity for easy integration into AI agent workflows. It aims for minimal dependencies, relying on the robust `pdfjs-dist` library.

See the full [Design Philosophy](https://github.com/sylphxltd/pdf-reader-mcp/blob/HEAD/docs/design/index.md) documentation.

## Comparison with Other Solutions

Compared to direct file access (often infeasible) or generic filesystem tools, this server offers PDF-specific parsing capabilities. Unlike external CLI tools (e.g., `pdftotext`), it provides a secure, integrated MCP interface with structured output, enhancing reliability and ease of use for AI agents.

See the full [Comparison](https://github.com/sylphxltd/pdf-reader-mcp/blob/HEAD/docs/comparison/index.md) documentation.

## Future Plans (Roadmap)

- **Documentation:**
  - Finalize all documentation sections (Guide, API, Design, Comparison).
  - Resolve TypeDoc issue and generate API documentation.
  - Add more examples and advanced usage patterns.
  - Implement PWA support and mobile optimization for the docs site.
  - Add share buttons and growth metrics to the docs site.
- **Benchmarking:**
  - Conduct comprehensive benchmarks with diverse PDF files (size, complexity).
  - Measure memory usage.
  - Compare URL vs. local file performance.
- **Core Functionality:**
  - Explore potential optimizations for very large PDF files.
  - Investigate options for extracting images or annotations (longer term).
- **Testing:**
  - Increase test coverage towards 100% where practical.
  - Add runtime tests once feasible.

## Documentation

For detailed usage, API reference, and guides, please visit the **[Full Documentation Website](https://sylphlab.github.io/pdf-reader-mcp/)** (Link to be updated upon deployment).

## Community & Support

- **Found a bug or have a feature request?** Please open an issue on [GitHub Issues](https://github.com/sylphlab/pdf-reader-mcp/issues).
- **Want to contribute?** We welcome contributions! Please see [CONTRIBUTING.md](https://github.com/sylphxltd/pdf-reader-mcp/blob/HEAD/CONTRIBUTING.md).
- **Star & Watch:** If you find this project useful, please consider starring ⭐ and watching 👀 the repository on [GitHub](https://github.com/sylphlab/pdf-reader-mcp) to show your support and stay updated!

## License

This project is licensed under the [MIT License](https://github.com/sylphxltd/pdf-reader-mcp/blob/HEAD/LICENSE).

**官方网站：** [https://github.com/sylphxltd/pdf-reader-mcp](https://github.com/sylphxltd/pdf-reader-mcp)
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

资源文件：`resources/mcp/constantinesmith-pdf-reader.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
