---
title: "Stripe支付代理工具"
description: "Stripe模型上下文协议服务器允许您通过函数调用与Stripe API集成。该协议支持各种工具与不同的Stripe服务进行交互。"
---

# Stripe支付代理工具

Stripe模型上下文协议服务器允许您通过函数调用与Stripe API集成。该协议支持各种工具与不同的Stripe服务进行交互。

# Stripe Model Context Protocol

Stripe [Model Context Protocol](https://modelcontextprotocol.com/) 服务器允许您通过函数调用来集成 Stripe API。此协议支持多种工具以与不同的 Stripe 服务进行交互。

## 设置

要使用 npx 运行 Stripe MCP 服务器，请使用以下命令：

```bash
# To set up all available tools
npx -y @stripe/mcp --tools=all --api-key=YOUR_STRIPE_SECRET_KEY

# To set up specific tools
npx -y @stripe/mcp --tools=customers.create,customers.read,products.create --api-key=YOUR_STRIPE_SECRET_KEY

# To configure a Stripe connected account
npx -y @stripe/mcp --tools=all --api-key=YOUR_STRIPE_SECRET_KEY --stripe-account=CONNECTED_ACCOUNT_ID
```

请确保将 `YOUR_STRIPE_SECRET_KEY` 替换为您的实际 Stripe 密钥。或者，您也可以在环境变量中设置 STRIPE_SECRET_KEY。

### 与 Claude Desktop 一起使用

在您的 `claude_desktop_config.json` 中添加以下内容。更多详情请参见[这里](https://modelcontextprotocol.io/quickstart/user)。

```
{
  "mcpServers": {
    "stripe": {
      "command": "npx",
      "args": [
          "-y",
          "@stripe/mcp",
          "--tools=all",
          "--api-key=STRIPE_SECRET_KEY"
      ]
    }
  }
}
```

## 可用工具

| 工具                  | 描述                     |
| --------------------- | ------------------------ |
| `customers.create`    | 创建新客户               |
| `customers.read`      | 读取客户信息             |
| `products.create`     | 创建新产品               |
| `products.read`       | 读取产品信息             |
| `prices.create`       | 创建新价格               |
| `prices.read`         | 读取价格信息             |
| `paymentLinks.create` | 创建新的支付链接         |
| `invoices.create`     | 创建新发票               |
| `invoices.update`     | 更新现有发票             |
| `invoiceItems.create` | 创建新发票项             |
| `balance.read`        | 检索余额信息             |
| `refunds.create`      | 创建新退款               |
| `paymentIntents.read` | 读取支付意图信息         |
| `documentation.read`  | 搜索 Stripe 文档         |

## 调试服务器

要调试您的服务器，您可以使用 [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector)。

首先构建服务器

```
npm run build
```

在终端中运行以下命令：

```bash
# Start MCP Inspector and server with all tools
npx @modelcontextprotocol/inspector node dist/index.js --tools=all --api-key=YOUR_STRIPE_SECRET_KEY
```

### 指示

1. 将 `YOUR_STRIPE_SECRET_KEY` 替换为您实际的 Stripe API 密钥。
2. 运行命令以启动 MCP Inspector。
3. 在浏览器中打开 MCP Inspector UI 并点击连接以启动 MCP 服务器。
4. 您可以看到所选工具列表，并单独测试每个工具。

**官方网站：** [https://github.com/stripe/agent-toolkit/tree/main/modelcontextprotocol](https://github.com/stripe/agent-toolkit/tree/main/modelcontextprotocol)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`finance`
- 标签：`finance`, `developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @stripe/mcp --tools=all --api-key=STRIPE_SECRET_KEY`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/stripe-agent-toolkit.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
