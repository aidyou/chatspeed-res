---
title: "Cloudflare Workers MCP连接器"
description: "一个将 Claude Desktop 和其他 MCP 客户端连接到 Cloudflare Workers 的软件包，通过模型上下文协议（Model Context Protocol）， enables 自定义功能可以通过自然语言访问。"
---

# Cloudflare Workers MCP连接器

一个将 Claude Desktop 和其他 MCP 客户端连接到 Cloudflare Workers 的软件包，通过模型上下文协议（Model Context Protocol）， enables 自定义功能可以通过自然语言访问。

# `workers-mcp`

> **从 Claude Desktop 与 Cloudflare Worker 对话！**

> [!NOTE]  
> 您现在可以[构建并部署支持远程 MCP 连接的 MCP 服务器到 Cloudflare](https://developers.cloudflare.com/agents/guides/remote-mcp-server/) — 并[使用它们与 Claude Desktop、Cursor 和其他仅限本地的 MCP 客户端](https://developers.cloudflare.com/agents/guides/test-remote-mcp-server/)。如果您正在开始一个新的 MCP 服务器，您应该阅读这些指南。`workers-mcp` 是之前的一种仅限本地的方法来构建 MCP 服务器。

### 什么是 `workers-mcp`？

此包提供了 CLI 工具和在 Worker 中的逻辑，以将 Claude Desktop（或任何 [MCP Client](https://modelcontextprotocol.io/)）连接到您账户中的 Cloudflare Worker，以便您可以根据需要进行自定义。它通过一个构建步骤工作，可以将您的 Worker 的 TypeScript 方法转换为：

```ts
export class ExampleWorkerMCP extends WorkerEntrypoint {
  /**
   * Generates a random number. This is extra random because it had to travel all the way to
   * your nearest Cloudflare PoP to be calculated which... something something lava lamps?
   *
   * @return {string} A message containing a super duper random number
   * */
  async getRandomNumber() {
    return `Your random number is ${Math.random()}`
  }
  
  // ...etc
}
```

...成为本地 Node.js 服务器可以暴露给 MCP 客户端的工具。Node.js 服务器充当代理，在本地处理 stdio 传输，并调用运行在 Cloudflare 上的 Worker 的相关方法。这允许您将应用程序中的任何函数或 API，或 [Cloudflare 开发者平台](https://developers.cloudflare.com/products/)中的任何服务，暴露给您的编码代理、Claude Desktop 或其他 MCP 客户端中的 LLM。

![image](/mcp-assets/cda92264abb55aa0b4d0751b6b6fcca4.png)

> 是的，我知道 `Math.random()` 在 Worker 上的工作方式与在本地机器上相同，但不要告诉 Claude 🤫

## 使用方法

### 第一步：生成一个新的 Worker

使用 `create-cloudflare` 生成一个新的 Worker。

```shell
npx create-cloudflare@latest my-new-worker
```

我建议选择一个 `Hello World` worker。

### 第二步：安装 `workers-mcp`

```shell
cd my-new-worker # I always forget this bit
npm install workers-mcp
```

### 第三步：运行 `setup` 命令

```shell
npx workers-mcp setup
```

注意：如果出现问题，请运行 `npx workers-mcp help`

### 第四步..♾️：迭代

更改 Worker 代码后，只需运行 `npm run deploy` 即可更新 Claude 关于您的函数的元数据以及您的实时 Worker 实例。

但是，如果您更改了方法的名称、参数，或者添加或删除了方法，Claude 将不会看到更新，直到您重新启动它。

您永远不需要重新运行 `npx workers-mcp install:claude`，但如果想排除 Claude 配置作为错误来源，则这样做是安全的。

## 与其他 MCP 客户端一起使用

### Cursor

要让您的 Cloudflare MCP 服务器在 Cursor 中工作，您需要将配置文件中的 'command' 和 'args' 合并成一个字符串，并使用 type 'command'。

例如，如果您的配置文件如下所示：

```json
{
  "mcpServers": {
    "your-mcp-server-name": {
      "command": "/path/to/workers-mcp",
      "args": [
        "run",
        "your-mcp-server-name",
        "https://your-server-url.workers.dev",
        "/path/to/your/project"
      ],
      "env": {}
    }
  }
}
```

在 Cursor 中，创建一个 MCP 服务器条目：
* 类型：`command`
* 命令：`/path/to/workers-mcp run your-mcp-server-name https://your-server-url.workers.dev /path/to/your/project`

### 其他 MCP 客户端

对于 Windsurf 和其他 MCP 客户端，更新您的配置文件以包含您的 worker，这样您可以直接从客户端使用工具：

```json
{
  "mcpServers": {
    "your-mcp-server-name": {
      "command": "/path/to/workers-mcp",
      "args": [
        "run",
        "your-mcp-server-name",
        "https://your-server-url.workers.dev",
        "/path/to/your/project"
      ],
      "env": {}
    }
  }
}
```

确保将占位符替换为您的实际服务器名称、URL 和项目路径。

## 示例

请参阅 `examples` 目录，了解一些使用示例：

* `examples/01-hello-world` 是按照上述安装说明操作后生成的快照
* `examples/02-image-generation` 使用 Workers AI 运行 Flux 图像生成模型。Claude 在建议提示方面非常出色，并且实际上能够解释结果并决定尝试哪些新的提示以达到您想要的效果。
* TODO 浏览器渲染
* TODO 持久对象

**官方网站：** [https://github.com/cloudflare/workers-mcp](https://github.com/cloudflare/workers-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `cloud platforms`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`/path/to/workers-mcp`
- 参数：`run your-mcp-server-name https://your-server-url.workers.dev /path/to/your/project`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/cloudflare-workers.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
