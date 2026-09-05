---
title: "Apify MCP 服务器"
description: "mcp.apify.com The Apify Model Context Protocol (MCP) server at mcp.apify.com enables your AI agents to extract data from social media, search engines, maps, e-commerce sites, and any other website usi…"
---

# Apify MCP 服务器

mcp.apify.com The Apify Model Context Protocol (MCP) server at mcp.apify.com enables your AI agents to extract data from social media, search engines, maps, e-commerce sites, and any other website usi…

mcp.apify.com

    

    

    

    

The Apify Model Context Protocol (MCP) server at [**mcp.apify.com**](https://mcp.apify.com) enables your AI agents to extract data from social media, search engines, maps, e-commerce sites, and any other website using thousands of ready-made scrapers, crawlers, and automation tools from [Apify Store](https://apify.com/store). It supports OAuth, allowing you to connect from clients like Claude.ai or Visual Studio Code using just the URL.

> **🚀 Use the hosted Apify MCP Server!**
>
> For the best experience, connect your AI assistant to our hosted server at **[`https://mcp.apify.com`](https://mcp.apify.com)**. The hosted server supports the latest features - including output schema inference for structured Actor results - that are not available when running locally via stdio.

> ⚠️ **Legacy SSE transport removed.** The `https://mcp.apify.com/sse` endpoint has been removed in favor of Streamable HTTP. Migrate your client to **[`https://mcp.apify.com`](https://mcp.apify.com)** — drop the `/sse` suffix from your configuration.

💰 The server also supports [agentic payments](#-agentic-payments): buy a token from [AGI](#-agi-recommended) to run any Actor, or pay per-request via [direct x402](#-direct-x402) (Pay Per Event Actors only) or [Skyfire](#-skyfire).

Apify MCP Server is compatible with `Claude Code, Claude.ai, Cursor, VS Code` and any client that adheres to the Model Context Protocol.
Check out the [MCP clients section](#-mcp-clients) for more details or visit the [MCP configuration page](https://mcp.apify.com).

![Apify-MCP-server](https://raw.githubusercontent.com/apify/apify-mcp-server/refs/heads/master/docs/apify-mcp-server.png)

## Table of Contents
- [🌐 Introducing Apify MCP Server](#-introducing-apify-mcp-server)
- [🚀 Quickstart](#-quickstart)
- [🤖 MCP clients](#-mcp-clients)
- [🪄 Try Apify MCP instantly](#-try-apify-mcp-instantly)
- [💰 Agentic payments](#-agentic-payments)
  - [How agentic payments work](#how-agentic-payments-work)
  - [🪙 AGI (recommended)](#-agi-recommended)
  - [💸 Direct x402](#-direct-x402)
  - [🔥 Skyfire](#-skyfire)
- [🛠️ Tools, resources, and prompts](#%EF%B8%8F-tools-resources-and-prompts)
- [📊 Telemetry](#-telemetry)
- [💬 Usage examples](#-usage-examples)
- [🐛 Troubleshooting](#-troubleshooting)
- [⚙️ Development](#%EF%B8%8F-development)
- [🔒 Privacy policy](#-privacy-policy)
- [🤝 Contributing](#-contributing)
- [📚 Learn more](#-learn-more)

# 🌐 Introducing Apify MCP Server

The Apify MCP Server allows an AI assistant to use any [Apify Actor](https://apify.com/store) as a tool to perform a specific task.
For example, it can:
- Use [Facebook Posts Scraper](https://apify.com/apify/facebook-posts-scraper) to extract data from Facebook posts from multiple pages/profiles.
- Use [Google Maps Email Extractor](https://apify.com/lukaskrivka/google-maps-with-contact-details) to extract contact details from Google Maps.
- Use [Google Search Results Scraper](https://apify.com/apify/google-search-scraper) to scrape Google Search Engine Results Pages (SERPs).
- Use [Instagram Scraper](https://apify.com/apify/instagram-scraper) to scrape Instagram posts, profiles, places, photos, and comments.
- Use [RAG Web Browser](https://apify.com/apify/rag-web-browser) to search the web, scrape the top N URLs, and return their content.
- Use [Web Fetch](https://apify.com/apify/web-fetch) to fetch any URL and return its content as Markdown, plain text, HTML, or links — with JavaScript rendering and anti-bot protection.

**Video tutorial: Integrate 8,000+ Apify Actors and Agents with Claude**

[![Apify MCP Server Tutorial: Integrate 5,000+ Apify Actors and Agents with Claude](https://img.youtube.com/vi/BKu8H91uCTg/hqdefault.jpg)](https://www.youtube.com/watch?v=BKu8H91uCTg)

# 🚀 Quickstart

You can use the Apify MCP Server in two ways:

**HTTPS Endpoint (mcp.apify.com)**: Connect from your MCP client via OAuth or by including the `Authorization: Bearer 
` header in your requests. This is the recommended method for most use cases. Because it supports OAuth, you can connect from clients like [Claude.ai](https://claude.ai) or [Visual Studio Code](https://code.visualstudio.com/) using just the URL: `https://mcp.apify.com`.
- `https://mcp.apify.com` streamable transport

**Standard Input/Output (stdio)**: Ideal for local integrations and command-line tools like the Claude for Desktop client.
- Set the MCP client server command to `npx @apify/actors-mcp-server` and the `APIFY_TOKEN` environment variable to your Apify API token.
- See `npx @apify/actors-mcp-server --help` for more options.

You can find detailed instructions for setting up the MCP server in the [Apify documentation](https://docs.apify.com/platform/integrations/mcp).

# 🤖 MCP clients

Apify MCP Server is compatible with any MCP client that adheres to the [Model Context Protocol](https://modelcontextprotocol.org/), but the level of support for dynamic tool discovery and other features may vary between clients.

To interact with the Apify MCP Server, you can use clients such as [Claude Desktop](https://claude.ai/download), [Visual Studio Code](https://code.visualstudio.com/), or [Apify Tester MCP Client](https://apify.com/jiri.spilka/tester-mcp-client).

Visit [mcp.apify.com](https://mcp.apify.com) to configure the server for your preferred client.

![Apify-MCP-configuration-clients](https://raw.githubusercontent.com/apify/apify-mcp-server/refs/heads/master/docs/mcp-clients.png)

### Tested clients

- [Claude Desktop](https://docs.apify.com/platform/integrations/claude-desktop)
- Claude.ai (web)
- [ChatGPT](https://docs.apify.com/platform/integrations/chatgpt)
- VS Code (Genie)
- Cursor
- OpenCode
- [Kiro](https://kiro.dev)
- [Apify Tester MCP Client](https://apify.com/jiri.spilka/tester-mcp-client) — designed for testing Apify MCP servers

# 🪄 Try Apify MCP instantly

Want to try Apify MCP without any setup?

Check out [Apify Tester MCP Client](https://apify.com/jiri.spilka/tester-mcp-client)

This interactive, chat-like interface provides an easy way to explore the capabilities of Apify MCP without any local setup.
Sign in with your Apify account and start experimenting with web scraping, data extraction, and automation tools!

Or use the MCP bundle file (formerly known as Anthropic Desktop extension file, or DXT) for one-click installation: [Apify MCP Server MCPB file](https://github.com/apify/apify-mcp-server/releases/latest/download/apify-mcp-server.mcpb)

# 💰 Agentic payments

You can pay for Actor runs without an Apify API token using **AGI**, **direct x402**, or **Skyfire**.

- **AGI** ([agi.apify.com](https://agi.apify.com)) mints a prepaid Apify API token in exchange for an x402 or MPP payment. Use the token like a normal API token against `mcp.apify.com` and `api.apify.com` — works for any Actor, not just Pay Per Event ones. **Recommended** for new integrations; see [AGI (recommended)](#-agi-recommended) below.
- **Direct x402** pays with USDC on [Base](https://base.org) per request and does not require a separate platform account. It is fully supported by [`mcpc`](https://github.com/apify/mcpc) (`brew install apify/tap/mcpc` or `npm install -g @apify/mcpc`). We use `mcpc` because it is one of the few MCP clients that supports the latest features and the x402 protocol natively.
- **Skyfire** pays with PAY tokens and requires a Skyfire account with a funded wallet. It does not require a special MCP client; the entire payment flow is handled directly through the MCP tool call parameters.

> ℹ️ **Scope:** Both direct x402 and Skyfire are limited to Pay Per Event Actors, don't support Standby Actors, and settle per run instead of minting a token.

## How agentic payments work

Actor run costs vary, so both payment methods use a prepaid balance model. The payment flow happens in four steps:

1. **Discovery**: The agent discovers Actors with `search-actors` or `fetch-actor-details`. Those calls are free.
2. **Prepayment**: Before running a paid Actor tool, the agent funds a prepaid balance.
   - **Direct x402**: `mcpc` automatically signs a $1.00 USDC transaction.
   - **Skyfire**: The agent creates a PAY token (minimum $5.00) using Skyfire's `create-pay-token` tool.
3. **Execution**: The agent calls the Actor tool.
   - **Direct x402**: Handled automatically by `mcpc` using the prepaid balance.
   - **Skyfire**: The agent explicitly passes the PAY token in the `skyfire-pay-id` input property.
4. **Resolution**: The tool returns the Actor results. Unused funds stay available for later runs.
   - **Direct x402**: After 60 minutes of inactivity, the server refunds any unused balance to the wallet on [Base](https://base.org).
   - **Skyfire**: Skyfire returns unused funds when the token expires.

## 🪙 AGI (recommended)

[AGI](https://agi.apify.com) (Apify Agent General Interface) is the recommended way for autonomous agents to pay for Apify usage without an account. Pay once via x402 or MPP, receive a prepaid, spend-capped Apify API token, and use it directly against `mcp.apify.com` and `api.apify.com` (`Authorization: Bearer `) — for any Actor.

Full protocol, supported payment methods, and current terms (minimum amount, token lifetime, refund policy) are documented at **[agi.apify.com/AGENTS.md](https://agi.apify.com/AGENTS.md)** — treat it as the single source of truth.

## 💸 Direct x402

The [x402 protocol](https://www.x402.org/) enables direct, machine-to-machine payments. Your MCP client can use it to pay for Actor runs with USDC on the [Base blockchain](https://base.org/), completely bypassing the need for an Apify API token.

### Prerequisites

- A wallet with USDC on [Base](https://base.org) mainnet.

### Setup

Create or import a wallet:

```bash
# Create a new wallet
mcpc x402 init

# Import an existing wallet
mcpc x402 import 

# Show the wallet address and a funding QR code, so you can fund it with USDC on Base (https://base.org)
mcpc x402
```

Connect to the server with x402 enabled:

```bash
mcpc connect "mcp.apify.com?payment=x402" @apify --x402
```

You can now call a paid tool:

```bash
mcpc @apify tools-call call-actor actor:="apify/rag-web-browser" input:='{"query": "latest AI news"}'
```

## 🔥 Skyfire

[Skyfire](https://www.skyfire.xyz/) provides managed payment infrastructure for AI agents. Instead of authenticating with an Apify API token, your agent passes a Skyfire payment token to cover the cost of each tool call using PAY tokens.

### Prerequisites

- A [Skyfire account](https://www.skyfire.xyz/) with a funded wallet.
- An MCP client that supports multiple servers, such as Claude Desktop, OpenCode, or VS Code.

### Setup

Configure the Skyfire MCP server and the Apify MCP Server in your client. Add `payment=skyfire` to the Apify server URL:

```json
{
  "mcpServers": {
    "skyfire": {
      "url": "https://api.skyfire.xyz/mcp/sse",
      "headers": {
        "skyfire-api-key": ""
      }
    },
    "apify": {
      "url": "https://mcp.apify.com?payment=skyfire"
    }
  }
}
```

See the [Skyfire integration documentation](https://docs.apify.com/platform/integrations/skyfire) for setup details. The [Agentic Payments with Skyfire](https://blog.apify.com/agentic-payments-skyfire/) post provides additional background.

# 🛠️ Tools, resources, and prompts

The MCP server provides a set of tools for interacting with Apify Actors.
Since Apify Store is large and growing rapidly, the MCP server provides a way to dynamically discover and use new Actors.

### Actors

Any [Apify Actor](https://apify.com/store) can be used as a tool.
By default, the server is pre-configured with two Actors, `apify/rag-web-browser` and `apify/web-fetch`, and several helper tools.
The MCP server loads an Actor's input schema and creates a corresponding MCP tool.
This allows the AI agent to know exactly what arguments to pass to the Actor and what to expect in return.

For example, for the `apify/rag-web-browser` Actor, the input parameters are:

```json
{
  "query": "restaurants in San Francisco",
  "maxResults": 3
}
```
You don't need to manually specify which Actor to call or its input parameters; the LLM handles this automatically.
When a tool is called, the arguments are automatically passed to the Actor by the LLM.
You can refer to the specific Actor's documentation for a list of available arguments.

### Helper tools

One of the most powerful features of using MCP with Apify is dynamic tool discovery.
It allows an AI agent to find new tools (Actors) as needed and incorporate them.
Here are some special MCP operations and how the Apify MCP Server supports them:

- **Apify Actors**: Search for Actors, view their details, and use them as tools for the AI.
- **Apify documentation**: Search the Apify documentation and fetch specific documents to provide context to the AI.
- **Actor runs**: Get lists of your Actor runs, inspect their details, and retrieve logs.
- **Apify storage**: Access data from your datasets and key-value stores.
- **Actor tasks**: Create, inspect, and update your saved Actor tasks, and publish or unpublish their public landing pages.

### Overview of available tools

Here is an overview list of all the tools provided by the Apify MCP Server.

Legend for the **Enabled by default** column:
- ✅ — in the default tool set.
- ⚡ — auto-injected when `call-actor`, an Actor tool, or `get-actor-run` is present (which is true in the default configuration).
- ✅¹ — served by default, but only when telemetry is enabled and the client is not withheld: Anthropic surfaces (Claude.ai / Claude Desktop / Claude Code) or `local-agent-mode-apify`. To disable, pass an explicit `tools=` list that omits it.

| Tool name | Category | Description | Enabled by default |
| :--- | :--- | :--- | :---: |
| `search-actors` | actors | Search for Actors in Apify Store. | ✅ |
| `fetch-actor-details` | actors | Retrieve detailed information about a specific Actor, including its input schema, README (summary when available, full otherwise), pricing, and Actor output schema. | ✅ |
| `call-actor` | actors | Call an Actor and get its run results. Use fetch-actor-details first to get the Actor's input schema. | ✅ |
| `get-actor-run` | runs | Get detailed information about a specific Actor run. | ⚡ |
| `get-dataset-items` | storage | Retrieve items from a dataset with support for filtering and pagination. | ⚡ |
| `get-key-value-store-record`| storage | Get the value associated with a specific key in a key-value store. | ⚡ |
| `abort-actor-run` | runs | Abort a running Actor run, optionally gracefully. | ⚡ |
| `search-apify-docs` | docs | Search the Apify documentation for relevant pages. | ✅ |
| `fetch-apify-docs` | docs | Fetch the full content of an Apify documentation page by its URL. | ✅ |
| [`apify--rag-web-browser`](https://apify.com/apify/rag-web-browser) | Actor (see [tool configuration](#tools-configuration)) | An Actor tool to browse the web. | ✅ |
| [`apify--web-fetch`](https://apify.com/apify/web-fetch) | Actor (see [tool configuration](#tools-configuration)) | An Actor tool to fetch a URL and return its content. | ✅ |
| `report-problem` | dev | Report a problem with an Apify tool or Actor to the Apify team. | ✅¹ |
| `get-actor-run-list` | runs | Get a list of an Actor's runs, filterable by status. |  |
| `get-actor-log` | runs | Retrieve the logs for a specific Actor run. |  |
| `get-dataset` | storage | Get metadata about a specific dataset. |  |
| `get-dataset-schema` | storage | Generate a JSON schema from dataset items. |  |
| `get-key-value-store` | storage | Get metadata about a specific key-value store. |  |
| `get-key-value-store-keys`| storage | List the keys within a specific key-value store. |  |
| `get-dataset-list` | storage | List all available datasets for the user. |  |
| `get-key-value-store-list`| storage | List all available key-value stores for the user. |  |
| `create-actor-task` | tasks | Create a saved Actor task (a named, reusable Actor configuration). |  |
| `get-actor-task` | tasks | Get a saved Actor task, its publication state and public display configuration. |  |
| `update-actor-task` | tasks | Update a task's input, run options, or public display configuration. |  |
| `publish-actor-task` | tasks | Publish a task on its public landing page. |  |
| `unpublish-actor-task` | tasks | Unpublish a task from its public landing page. |  |

> **Note:**
>
> When `call-actor`, an Actor tool, or `get-actor-run` is present, the server auto-injects `get-actor-run`, `get-dataset-items`, `get-key-value-store-record`, and `abort-actor-run`.
>
> When you call an Actor — through `call-actor` or directly via an Actor tool (e.g., `apify--rag-web-browser`) — the response contains run metadata, storage IDs, and a `summary` + `nextStep`, but no dataset items. To fetch items, follow `nextStep` and call `get-dataset-items` (auto-injected), passing the `datasetId` returned from the call.

### Tool annotations

All tools include metadata annotations to help MCP clients and LLMs understand tool behavior:

- **`title`**: Short display name for the tool (e.g., "Search Actors", "Call Actor", "apify/rag-web-browser")
- **`readOnlyHint`**: `true` for tools that only read data without modifying state (e.g., `get-dataset`, `fetch-actor-details`)
- **`openWorldHint`**: `true` for tools that access external resources outside the Apify platform (e.g., `call-actor` executes external Actors). Tools that interact only with the Apify platform (like `search-actors` or `fetch-apify-docs`) do not have this hint.

### Tools configuration

The `tools` configuration parameter is used to specify loaded tools – either categories or specific tools directly, and Apify Actors. For example, `tools=storage,runs` loads two categories; `tools=call-actor` loads just one tool.

When no query parameters are provided, the MCP server loads the following `tools` by default:

- `actors`
- `docs`
- `apify/rag-web-browser`
- `apify/web-fetch`

If the tools parameter is specified, only the listed tools or categories will be enabled – no default tools will be included.

`report-problem` is served by default (subject to the gating in the footnote above) but lives in the `dev` category, so an explicit `tools=dev` selects it too. To disable it, pass an explicit `tools=` list that omits it (e.g. `tools=actors,docs`).

> **Easy configuration:**
>
> Use the [UI configurator](https://mcp.apify.com/) to configure your server, then copy the configuration to your client.

**Configuring the hosted server:**

The hosted server can be configured using query parameters in the URL. For example, to load the default tools, use:

```
https://mcp.apify.com?tools=actors,docs,apify/rag-web-browser,apify/web-fetch
```

For minimal configuration, if you want to use only a single Actor tool - without any discovery or generic calling tools, the server can be configured as follows:

```
https://mcp.apify.com?tools=apify/my-actor
```

This setup exposes only the specified Actor (`apify/my-actor`) as a tool. No other tools will be available.

**Configuring the CLI:**

The CLI can be configured using command-line flags. For example, to load the same tools as in the hosted server configuration, use:

```bash
npx @apify/actors-mcp-server --tools actors,docs,apify/rag-web-browser,apify/web-fetch
```

The minimal configuration is similar to the hosted server configuration:

```bash
npx @apify/actors-mcp-server --tools apify/my-actor
```

As above, this exposes only the specified Actor (`apify/my-actor`) as a tool. No other tools will be available.

> **⚠️ Important recommendation**
>
> **The default tools configuration may change in future versions.** When no `tools` parameter is specified, the server currently loads default tools, but this behavior is subject to change.
>
> **For production use and stable interfaces, always explicitly specify the `tools` parameter** to ensure your configuration remains consistent across updates.

### UI mode configuration

The `ui` parameter enables [MCP Apps](

**官方网站：** [https://github.com/apify/apify-mcp-server](https://github.com/apify/apify-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`browser`, `data`
- 标签：`web scraping`, `apify`, `browser automation`, `data extraction`, `official`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`@apify/actors-mcp-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/apify-mcp-server.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
