---
title: "MCP计算器"
description: "一种为LLM提供基本计算器功能的模型上下文协议服务器，使它们能够执行加法、减法、乘法、除法、模运算和平方根等数学运算。"
---

# MCP计算器

一种为LLM提供基本计算器功能的模型上下文协议服务器，使它们能够执行加法、减法、乘法、除法、模运算和平方根等数学运算。

## 计算 MCP

一个提供基本计算器功能的 Model Context Protocol (MCP) 服务器，该服务器能够实现浏览器自动化能力。
此服务器使 LLMs 能够与计算器交互。
（实际上我是为一个测试程序制作的）

### 使用案例

- 测试代码以连接 MCP 功能。
- 玩具项目

### 示例配置

```js
{
  "mcpServers": {
    "calculate": {
      "command": "npx",
      "args": [
        "-y",
        "@wrtnlabs/calculator@latest"
      ]
    }
  }
}
```

#### 在 VS Code 中安装

或者，您可以使用 VS Code CLI 安装 Playwright MCP 服务器：

```bash
# For VS Code
code --add-mcp '{"name":"calculator","command":"npx","args":["-y", "@wrtnlabs/calculator-mcp@latest"]}'
```

```bash
# For VS Code Insiders
code-insiders --add-mcp '{"name":"calculator","command":"npx","args":["-y", "@wrtnlabs/calculator-mcp@latest"]}'
```

安装后，Calculator MCP 服务器将可以在 VS Code 中与您的 GitHub Copilot 代理一起使用。

### 命令行选项

Calculator MCP 服务器支持以下命令行选项：

- `--port 
`: 监听 SSE 传输的端口

### 在没有 DISPLAY 的 Linux 上运行有头浏览器

当在没有显示或从 IDE 的工作进程运行有头浏览器时，
请从具有 DISPLAY 的环境中运行 MCP 服务器，并传递 `--port` 标志以启用 SSE 传输。

```bash
npx @wrtnlabs/calculator-mcp@latest --port 8931
```

然后在 MCP 客户端配置中，将 `url` 设置为 SSE 端点：

```js
{
  "mcpServers": {
    "calculator": {
      "url": "http://localhost:8931/sse"
    }
  }
}
```

### 使用自定义传输的编程用法

```js
import { createServer } from "@wrtnlabs/calculator-mcp";
// ... other import statement

const client = new Client({
  name: "test client",
  version: "0.1.0",
});

const server = createServer({
  name: "calculator",
  version: "1.0.0"
});

const [clientTransport, serverTransport] = InMemoryTransport.createLinkedPair();

await Promise.all([
  client.connect(clientTransport),
  server.connect(serverTransport),
]);
```

### 工具

- **add**
- **sub**
- **mul**
- **div**
- **mod**
- **sqrt**

**官方网站：** [https://github.com/wrtnlabs/calculator-mcp](https://github.com/wrtnlabs/calculator-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @wrtnlabs/calculator@latest`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/wrtnlabs-calculator.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
