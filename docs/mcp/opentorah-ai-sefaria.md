---
title: "Sefaria检索服务器"
description: "通过标准化接口，启用大型语言模型从Sefaria图书馆检索犹太文本和评论。"
---

# Sefaria检索服务器

通过标准化接口，启用大型语言模型从Sefaria图书馆检索犹太文本和评论。

# Sefaria 犹太图书馆 MCP 服务器

[Smithery](https://smithery.ai/server/mcp-sefaria-server)
这是一个 MCP（模型上下文协议）服务器，提供对 Sefaria 图书馆中犹太文本的访问。此服务器使大型语言模型能够通过标准化接口检索和引用犹太文本。

## 特性

- 按引用检索犹太文本
- 检索给定文本的注释

## 安装

需要 Python 3.10 或更高版本。

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/mcp-sefaria-server) 自动为 Claude Desktop 安装 Sefaria 犹太图书馆：

```bash
npx -y @smithery/cli install mcp-sefaria-server --client claude
```

### 克隆仓库
```bash
git clone https://github.com/sivan22/mcp-sefaria-server.git
cd mcp-sefaria-server
```

## 运行服务器

可以直接运行服务器：

```bash
uv --directory path/to/directory run sefaria_jewish_library
```

或者通过支持模型上下文协议 (MCP) 的客户端运行。
对于 Claude 桌面应用程序和 cline，您应使用以下配置：
```
{
  "mcpServers": {        
      "sefaria_jewish_library": {
          "command": "uv",
          "args": [
              "--directory",
              "C:/dev/mcp-sefaria-server",
              "run",
              "sefaria_jewish_library"
          ],
          "env": {
            "PYTHONIOENCODING": "utf-8" 
          }
      }
  }
}
```

## 可用工具

服务器通过 MCP 接口提供以下工具：

### get_text

按引用检索特定的犹太文本。

示例：
```
reference: "Genesis 1:1"
reference: "שמות פרק ב פסוק ג"
reference: "משנה ברכות פרק א משנה א"
```

### get_commentaries

检索给定文本的注释列表。

示例：
```
reference: "Genesis 1:1"
reference: "שמות פרק ב פסוק ג"
reference: "משנה ברכות פרק א משנה א"
```

## 开发

该项目使用：
- [MCP SDK](https://github.com/modelcontextprotocol/sdk) 用于服务器实现
- [Sefaria API](https://github.com/Sefaria/Sefaria-API) 用于访问犹太文本

## 要求

- Python >= 3.10
- MCP SDK >= 1.1.1
- Sefaria API

## 许可证

MIT 许可证

**官方网站：** [https://github.com/opentorah-ai/mcp-sefaria-server](https://github.com/opentorah-ai/mcp-sefaria-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`art and culture`, `search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`--directory C:/dev/mcp-sefaria-server run sefaria_jewish_library`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/opentorah-ai-sefaria.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
