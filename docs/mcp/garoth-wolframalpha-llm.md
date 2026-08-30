---
title: "Wolfram Alpha LLM接口"
description: "启用对 WolframAlpha 的 LLM API 进行自然语言问题的查询，提供经过结构化和简化的答案，这些答案针对 LLM 的使用进行了优化。"
---

# Wolfram Alpha LLM接口

启用对 WolframAlpha 的 LLM API 进行自然语言问题的查询，提供经过结构化和简化的答案，这些答案针对 LLM 的使用进行了优化。

# WolframAlpha LLM MCP 服务器

 width="256" alt="WolframAlpha LLM MCP Logo" />

一个提供访问 WolframAlpha 的 LLM API 的 Model Context Protocol (MCP) 服务器。[https://products.wolframalpha.com/llm-api/documentation](https://products.wolframalpha.com/llm-api/documentation)

   width="609" alt="WolframAlpha MCP 服务器示例 1" />

   width="609" alt="WolframAlpha MCP 服务器示例 2" />

## 特性

- 使用自然语言问题查询 WolframAlpha 的 LLM API
- 回答复杂的数学问题
- 查询关于科学、物理、历史、地理等领域的事实
- 获取优化后的结构化响应，适合 LLM 消费
- 支持简化答案和带有章节的详细响应

## 可用工具

- `ask_llm`: 向 WolframAlpha 提问并获取结构化的 llm 友好响应
- `get_simple_answer`: 获取简化答案
- `validate_key`: 验证 WolframAlpha API 密钥

## 安装

```bash
git clone https://github.com/Garoth/wolframalpha-llm-mcp.git
npm install
```

## 配置

1. 从 [developer.wolframalpha.com](https://developer.wolframalpha.com/) 获取您的 WolframAlpha API 密钥

2. 将其添加到 VSCode 设置中的 Cline MCP 设置文件中（例如：~/.config/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json）：

```json
{
  "mcpServers": {
    "wolframalpha": {
      "command": "node",
      "args": ["/path/to/wolframalpha-mcp-server/build/index.js"],
      "env": {
        "WOLFRAM_LLM_APP_ID": "your-api-key-here"
      },
      "disabled": false,
      "autoApprove": [
        "ask_llm",
        "get_simple_answer",
        "validate_key"
      ]
    }
  }
}
```

## 开发

### 设置测试

测试使用真实的 API 调用来确保准确的响应。要运行测试：

1. 复制示例环境文件：
```bash
   cp .env.example .env
```

2. 编辑 `.env` 并添加您的 WolframAlpha API 密钥：
```
   WOLFRAM_LLM_APP_ID=your-api-key-here
```
   注意：`.env` 文件被 gitignore 掉，以防止提交敏感信息。

3. 运行测试：
```bash
   npm test
```

### 构建

```bash
npm run build
```

## 许可证

MIT

**官方网站：** [https://github.com/Garoth/wolframalpha-llm-mcp](https://github.com/Garoth/wolframalpha-llm-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`search`, `research and data`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`/path/to/wolframalpha-mcp-server/build/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/garoth-wolframalpha-llm.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
