---
title: "calculator-mcp"
description: "A Model Context Protocol server that provides basic calculator functionality for LLMs, enabling them to perform mathematical operations like addition, subtraction, multiplication, division, modulo, an…"
---

# calculator-mcp

A Model Context Protocol server that provides basic calculator functionality for LLMs, enabling them to perform mathematical operations like addition, subtraction, multiplication, division, modulo, an…

## Calculate MCP

A Model Context Protocol (MCP) server that provides browser automation capabilities using basic calculator feature.
This server enables LLMs to interact with calculator.
(I actually made it for a test program)

### Use Cases

- The test code for to connect MCP feature.
- The toy projects

### Example config

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

#### Installation in VS Code

Alternatively, you can install the Playwright MCP server using the VS Code CLI:

```bash
# For VS Code
code --add-mcp '{"name":"calculator","command":"npx","args":["-y", "@wrtnlabs/calculator-mcp@latest"]}'
```

```bash
# For VS Code Insiders
code-insiders --add-mcp '{"name":"calculator","command":"npx","args":["-y", "@wrtnlabs/calculator-mcp@latest"]}'
```

After installation, the Calculator MCP server will be available for use with your GitHub Copilot agent in VS Code.

### CLI Options

The Calculator MCP server supports the following command-line options:

- `--port 
`: Port to listen on for SSE transport

### Running headed browser on Linux w/o DISPLAY

When running headed browser on system w/o display or from worker processes of the IDEs,
run the MCP server from environment with the DISPLAY and pass the `--port` flag to enable SSE transport.

```bash
npx @wrtnlabs/calculator-mcp@latest --port 8931
```

And then in MCP client config, set the `url` to the SSE endpoint:

```js
{
  "mcpServers": {
    "calculator": {
      "url": "http://localhost:8931/sse"
    }
  }
}
```

### Programmatic usage with custom transports

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

### Tools

- **add**
- **sub**
- **mul**
- **div**
- **mod**
- **sqrt**

**Official site: ** [https://github.com/wrtnlabs/calculator-mcp](https://github.com/wrtnlabs/calculator-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `developer tools`, `other`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @wrtnlabs/calculator@latest`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/wrtnlabs-calculator.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
