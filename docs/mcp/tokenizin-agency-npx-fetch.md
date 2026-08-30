---
title: "内容抓取转换器"
description: "一个强大的MCP服务器，可以轻松地将网页内容抓取并转换为各种格式（HTML、JSON、Markdown、纯文本）。"
---

# 内容抓取转换器

一个强大的MCP服务器，可以轻松地将网页内容抓取并转换为各种格式（HTML、JSON、Markdown、纯文本）。

# MCP NPX Fetch

[![npm version](/mcp-assets/f158cbea937d67f46dd06a0879b88710.svg)](https://www.npmjs.com/package/@tokenizin/mcp-npx-fetch)
[![License: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)
[![TypeScript](/mcp-assets/49904649f602ceb829cc76dcf6be1703.svg)](https://www.typescriptlang.org/)
[![Model Context Protocol](/mcp-assets/dea21ef1b755e12c928a6fd915869854.svg)](https://github.com/modelcontextprotocol)

一个强大的MCP服务器，可以轻松地将网页内容抓取并转换为各种格式（HTML、JSON、Markdown、纯文本）。

[安装](#installation) •
[特性](#features) •
[使用](#usage) •
[文档](#documentation) •
[贡献](#contributing)

---

## 🚀 特性

- 🌐 **通用内容抓取**: 支持HTML、JSON、纯文本和Markdown格式
- 🔒 **自定义头部支持**: 在请求中添加身份验证和自定义头部
- 🛠 **内置转换**: 自动在不同格式之间进行转换
- ⚡ **高性能**: 使用现代JavaScript特性和优化以提高速度
- 🔌 **MCP兼容**: 无缝集成Claude Desktop和其他MCP客户端
- 🎯 **类型安全**: 用TypeScript编写，具有完整的类型定义

## 📦 安装

### NPM 全局安装

```bash
npm install -g @tokenizin/mcp-npx-fetch

```

### 直接通过NPX使用

```bash
npx @tokenizin/mcp-npx-fetch
```

## 📚 文档

### 可用工具

#### `fetch_html`

从任何URL获取并返回原始HTML内容。

```typescript
{
  url: string;     // Required: Target URL
  headers?: {      // Optional: Custom request headers
    [key: string]: string;
  };
}
```

#### `fetch_json`

从任何URL获取并解析JSON数据。

```typescript
{
  url: string;     // Required: Target URL
  headers?: {      // Optional: Custom request headers
    [key: string]: string;
  };
}
```

#### `fetch_txt`

获取并返回干净的纯文本内容，移除HTML标签和脚本。

```typescript
{
  url: string;     // Required: Target URL
  headers?: {      // Optional: Custom request headers
    [key: string]: string;
  };
}
```

#### `fetch_markdown`

获取内容并将其转换为格式良好的Markdown。

```typescript
{
  url: string;     // Required: Target URL
  headers?: {      // Optional: Custom request headers
    [key: string]: string;
  };
}
```

## 🔧 使用

### CLI 使用

直接启动MCP服务器：

```bash
mcp-npx-fetch
```

或者通过npx：

```bash
npx @tokenizin/mcp-npx-fetch
```

### Claude Desktop 集成

1. 找到你的Claude Desktop配置文件：

   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%/Claude/claude_desktop_config.json`
   - Linux: `~/.config/Claude/claude_desktop_config.json`

2. 在你的`mcpServers`对象中添加以下配置：

```json
{
  "mcpServers": {
    "fetch": {
      "command": "npx",
      "args": ["-y", "@tokenizin/mcp-npx-fetch"],
      "env": {}
    }
  }
}
```

## 💻 本地开发

1. 克隆仓库：

```bash
git clone https://github.com/tokenizin-agency/mcp-npx-fetch.git
cd mcp-npx-fetch
```

2. 安装依赖项：

```bash
npm install
```

3. 启动开发模式：

```bash
npm run dev
```

4. 运行测试：

```bash
npm test
```

## 🛠 技术栈

- [Model Context Protocol SDK](https://github.com/modelcontextprotocol/sdk) - 核心MCP功能
- [JSDOM](https://github.com/jsdom/jsdom) - HTML解析和操作
- [Turndown](https://github.com/mixmark-io/turndown) - HTML到Markdown转换
- [TypeScript](https://www.typescriptlang.org/) - 类型安全和现代JavaScript特性
- [Zod](https://github.com/colinhacks/zod) - 运行时类型验证

## 🤝 贡献

希望这符合您的要求！如果有任何需要进一步调整的地方，请告诉我。

欢迎贡献！请随时提交 Pull Request。对于重大更改，请先打开一个 issue 来讨论您想要进行的更改。

1. 叉取仓库
2. 创建您的功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 将更改推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

## 📄 许可证

本项目根据 MIT 许可证授权 - 详情请参阅 [LICENSE](https://github.com/tokenizin-agency/mcp-npx-fetch/blob/HEAD/LICENSE) 文件。

---

由 
PT Tokenizin Technology Agency
 用 ❤️ 制作

**官方网站：** [https://github.com/tokenizin-agency/mcp-npx-fetch](https://github.com/tokenizin-agency/mcp-npx-fetch)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`browser`
- 标签：`browser automation`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @tokenizin/mcp-npx-fetch`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/tokenizin-agency-npx-fetch.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
