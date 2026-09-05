---
title: "Fetch MCP 工具"
description: "通过简单的API调用，提供获取和转换网络内容（HTML、JSON、纯文本和Markdown格式）的功能。"
---

# Fetch MCP 工具

通过简单的API调用，提供获取和转换网络内容（HTML、JSON、纯文本和Markdown格式）的功能。

# 获取 MCP 服务器


此 MCP 服务器提供以多种格式（包括 HTML、JSON、纯文本和 Markdown）获取网页内容的功能。

### 工具

- **fetch_html**

  - 获取网站内容并以 HTML 格式返回
  - 输入参数：
    - `url` (字符串, 必填): 要获取的网站 URL
    - `headers` (对象, 可选): 请求中包含的自定义头
  - 返回网页的原始 HTML 内容

- **fetch_json**

  - 从 URL 获取 JSON 文件
  - 输入参数：
    - `url` (字符串, 必填): 要获取的 JSON 的 URL
    - `headers` (对象, 可选): 请求中包含的自定义头
  - 返回解析后的 JSON 内容

- **fetch_txt**

  - 获取网站内容并以纯文本格式返回（无 HTML）
  - 输入参数：
    - `url` (字符串, 必填): 要获取的网站 URL
    - `headers` (对象, 可选): 请求中包含的自定义头
  - 返回移除 HTML 标签、脚本和样式的网页文本内容

- **fetch_markdown**
  - 获取网站内容并以 Markdown 格式返回
  - 输入参数：
    - `url` (字符串, 必填): 要获取的网站 URL
    - `headers` (对象, 可选): 请求中包含的自定义头
  - 返回转换为 Markdown 格式的网页内容

### 启动方式

1. bun

```bash
bun i
bun start
```

2. docker

```bash
docker compose up --build -d
```

### 使用方法

```json
{
  "mcpServers": {
    "fetch-mcp": {
      "transport": "sse",
      "url": "http://localhost:3000/sse",
      "headers": {
        "Authorization": "Bearer your-token-here",
        "X-Custom-Header": "custom-value"
      },
      "useNodeEventSource": true
    }
  }
}
```

### 资源

此服务器不提供任何持久化资源。它被设计为按需获取和转换网页内容。

### 参考资料

- [原仓库 zcaceres/fetch-mcp](https://github.com/zcaceres/fetch-mcp)

**官方网站：** [https://github.com/phpmac/fetch_mcp](https://github.com/phpmac/fetch_mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`browser`
- 标签：`browser automation`, `chinese`

## MCP 配置

- 传输方式：`http`
- 启动命令：``
- 参数：无

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/phpmac-fetch.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
