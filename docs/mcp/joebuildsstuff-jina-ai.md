---
title: "Claude-Jina AI服务"
description: "一个MCP服务器，通过Claude提供对Jina AI强大网络服务（页面阅读、网络搜索、事实核查）的访问。"
---

# Claude-Jina AI服务

一个MCP服务器，通过Claude提供对Jina AI强大网络服务（页面阅读、网络搜索、事实核查）的访问。

# Jina AI MCP 服务器
[Smithery](https://smithery.ai/server/jina-ai-mcp)
[Smithery](https://smithery.ai/server/jina-ai-mcp-server)

一个通过 Claude 提供访问 Jina AI 强大网络服务的 MCP 服务器。该服务器实现了三个主要工具：

- 网页阅读和内容提取
- 网络搜索
- 事实核查/基础验证

## 特性

### 工具

#### `read_webpage`
- 以优化格式从网页中提取内容，适用于大型语言模型 (LLMs)
- 支持多种输出格式（默认、Markdown、HTML、文本、屏幕截图、页面截图）
- 可选项包括包含链接和图片
- 能够为图片生成替代文本
- 缓存控制选项

#### `search_web`
- 使用 Jina AI 的搜索 API 进行网络搜索
- 可配置的结果数量（默认：5）
- 支持保留图片和生成替代文本
- 多种返回格式（Markdown、文本、HTML）
- 返回结构化结果，包括标题、描述和内容

#### `fact_check`
- 使用 Jina AI 的基础引擎进行事实核查
- 提供事实性评分和支持证据
- 可选深入模式，进行更彻底的分析
- 返回带有关键引用和支持/矛盾分类的参考资料

## 设置

### 前提条件

使用此服务器需要一个 Jina AI API 密钥。您可以在 [https://jina.ai/](https://jina.ai/) 免费获取。

### 安装

有两种方法可以使用此服务器：

#### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/jina-ai-mcp-server) 自动安装适用于 Claude Desktop 的 Jina AI：

```bash
npx -y @smithery/cli install jina-ai-mcp-server --client claude
```

#### 选项 1：NPX（推荐）
将以下配置添加到您的 Claude Desktop 配置文件中：

```json
{
  "mcpServers": {
    "jina-ai-mcp-server": {
      "command": "npx",
      "args": [
        "-y",
        "jina-ai-mcp-server"
      ],
      "env": {
        "JINA_API_KEY": ""
      }
    }
  }
}
```

#### 选项 2：本地安装
1. 克隆仓库
2. 安装依赖项：
```bash
npm install
```

3. 构建服务器：
```bash
npm run build
```

4. 将以下配置添加到您的 Claude Desktop 配置中：
```json
{
  "mcpServers": {
    "jina-ai-mcp-server": {
      "command": "node",
      "args": [
        "/path/to/jina-ai-mcp-server/dist/index.js"
      ],
      "env": {
        "JINA_API_KEY": ""
      }
    }
  }
}
```

### 配置文件位置

在 MacOS 上：
```bash
~/Library/Application Support/Claude/claude_desktop_config.json
```

在 Windows 上：
```bash
%APPDATA%/Claude/claude_desktop_config.json
```

### 调试

由于 MCP 服务器通过 stdio 通信，调试可能具有挑战性。我们建议使用 [MCP 检查器](https://github.com/modelcontextprotocol/inspector)：

```bash
npm run inspector
```

检查器将提供一个 URL，以便您在浏览器中访问调试工具。

## API 响应类型

所有工具都返回结构化的 JSON 响应，其中包括：

- 状态码和元数据
- 根据请求的输出类型格式化的内容
- 使用情况信息（令牌计数）
- 在适用时：图片、链接和额外的元数据

有关详细的模式信息，请参阅 `schemas.ts`。

**官方网站：** [https://github.com/joeBlockchain/mcp-jina-ai](https://github.com/joeBlockchain/mcp-jina-ai)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`browser`
- 标签：`browser automation`, `search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y jina-ai-mcp-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/joebuildsstuff-jina-ai.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
