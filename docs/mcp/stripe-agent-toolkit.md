---
title: "agent-toolkit"
description: "The Stripe Model Context Protocol server allows you to integrate with Stripe APIs through function calling. This protocol supports various tools to interact with different Stripe services."
---

# agent-toolkit

The Stripe Model Context Protocol server allows you to integrate with Stripe APIs through function calling. This protocol supports various tools to interact with different Stripe services.

# Stripe Model Context Protocol

The Stripe [Model Context Protocol](https://modelcontextprotocol.com/) server allows you to integrate with Stripe APIs through function calling. This protocol supports various tools to interact with different Stripe services.

## Setup

To run the Stripe MCP server using npx, use the following command:

```bash
# To set up all available tools
npx -y @stripe/mcp --tools=all --api-key=YOUR_STRIPE_SECRET_KEY

# To set up specific tools
npx -y @stripe/mcp --tools=customers.create,customers.read,products.create --api-key=YOUR_STRIPE_SECRET_KEY

# To configure a Stripe connected account
npx -y @stripe/mcp --tools=all --api-key=YOUR_STRIPE_SECRET_KEY --stripe-account=CONNECTED_ACCOUNT_ID
```

Make sure to replace `YOUR_STRIPE_SECRET_KEY` with your actual Stripe secret key. Alternatively, you could set the STRIPE_SECRET_KEY in your environment variables.

### Usage with Claude Desktop

Add the following to your `claude_desktop_config.json`. See [here](https://modelcontextprotocol.io/quickstart/user) for more details.

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

## Available tools

| Tool                  | Description                     |
| --------------------- | ------------------------------- |
| `customers.create`    | Create a new customer           |
| `customers.read`      | Read customer information       |
| `products.create`     | Create a new product            |
| `products.read`       | Read product information        |
| `prices.create`       | Create a new price              |
| `prices.read`         | Read price information          |
| `paymentLinks.create` | Create a new payment link       |
| `invoices.create`     | Create a new invoice            |
| `invoices.update`     | Update an existing invoice      |
| `invoiceItems.create` | Create a new invoice item       |
| `balance.read`        | Retrieve balance information    |
| `refunds.create`      | Create a new refund             |
| `paymentIntents.read` | Read payment intent information |
| `documentation.read`  | Search Stripe documentation     |

## Debugging the Server

To debug your server, you can use the [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector).

First build the server

```
npm run build
```

Run the following command in your terminal:

```bash
# Start MCP Inspector and server with all tools
npx @modelcontextprotocol/inspector node dist/index.js --tools=all --api-key=YOUR_STRIPE_SECRET_KEY
```

### Instructions

1. Replace `YOUR_STRIPE_SECRET_KEY` with your actual Stripe API secret key.
2. Run the command to start the MCP Inspector.
3. Open the MCP Inspector UI in your browser and click Connect to start the MCP server.
4. You can see the list of tools you selected and test each tool individually.

**Official site: ** [https://github.com/stripe/agent-toolkit/tree/main/modelcontextprotocol](https://github.com/stripe/agent-toolkit/tree/main/modelcontextprotocol)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `finance`
- Tags: `finance`, `developer tools`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @stripe/mcp --tools=all --api-key=STRIPE_SECRET_KEY`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/stripe-agent-toolkit.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
