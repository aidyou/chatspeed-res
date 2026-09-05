---
title: "Terraform MCP Server (HashiCorp)"
description: "Terraform MCP Server The Terraform MCP Server is a Model Context Protocol (MCP) server that integrates seamlessly with Terraform Registry and HCP Terraform APIs, enabling advanced automation and inter…"
---

# Terraform MCP Server (HashiCorp)

Terraform MCP Server The Terraform MCP Server is a Model Context Protocol (MCP) server that integrates seamlessly with Terraform Registry and HCP Terraform APIs, enabling advanced automation and inter…

# 
 Terraform MCP Server

The Terraform MCP Server is a [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction)
server that integrates seamlessly with [Terraform Registry](https://developer.hashicorp.com/terraform/registry/api-docs) and [HCP Terraform](https://developer.hashicorp.com/terraform/cloud-docs/api-docs) APIs, enabling advanced
automation and interaction capabilities for Infrastructure as Code (IaC) development.

## Table of Contents

Get started

Client integrations

Build and run

Features

Prerequisites

Command Line Options

Instructions

Installation

Visual Studio Code

Cursor

Claude Desktop, Amazon Q Developer, and Kiro CLI

Claude Code

Codex CLI

Gemini extensions

Bob IDE and Shell

Install from source

Building the Docker Image locally

Transport Support

Stdio Transport

StreamableHTTP Transport

Server capabilities

Deployment and security

Help and contributing

Available Tools

Available Resources

Available Metrics

Tool Filtering

Session Modes

Token Passthrough for Centralized Deployments

Client IP Forwarding

Trust model

Trusted hops

Limitations

Migrating from earlier versions

Supported Headers

Security Considerations

Centralized Deployment Example

Troubleshooting

Corporate Proxy and TLS Inspection

Development

Contributing

License

Security

Support

## Features

- **Dual Transport Support**: Both Stdio and StreamableHTTP transports with configurable endpoints
- **Terraform Registry Integration**: Direct integration with public Terraform Registry APIs for providers, modules, and policies
- **HCP Terraform & Terraform Enterprise Support**: Full workspace management, organization/project listing, and private registry access
- **Workspace Operations**: Create, update, delete workspaces with support for variables, tags, and run management
- **OTel metrics for monitoring tool usage**: Integration with open telemetry meters to track tool-call volume, latency and failures in Streamable HTTP mode. Also exposes default http server metrics when this feature is enabled

> **Security Note:** Depending on the query, the MCP server may expose certain Terraform data to the MCP client and LLM. Do not use the MCP server with untrusted MCP clients or LLMs.

> **Legal Note:** Your use of a third party MCP Client/LLM is subject solely to the terms of use for such MCP/LLM, and IBM is not responsible for the performance of such third party tools. IBM expressly disclaims any and all warranties and liability for third party MCP Clients/LLMs, and may not be able to provide support to resolve issues which are caused by the third party tools.

> **Caution:**  The outputs and recommendations provided by the MCP server are generated dynamically and may vary based on the query, model, and the connected MCP client. Users should thoroughly review all outputs/recommendations to ensure they align with their organization’s security best practices, cost-efficiency goals, and compliance requirements before implementation.

## Prerequisites

1. Ensure [Docker](https://www.docker.com/) is installed and running to use the server in a containerized environment.
1. Install an AI assistant that supports the Model Context Protocol (MCP).

## Command Line Options

**Environment Variables:**

| Variable | Description | Default |
|----------|-------------|---------|
| `TFE_ADDRESS` | Sets the Terraform Enterprise/HCP Terraform address for API calls. Must include the protocol (e.g., `https://app.terraform.io`). In streamable-http mode this is the only way to set the address; it cannot be supplied by clients via header or query parameter. | Optional |
| `TFE_TOKEN` | Terraform Enterprise API token | `""` (empty) |
| `TF_MCP_SHARED_SECRET` | Shared secret sent as the `X-Tf-Mcp-Secret` header on requests to HCP Terraform / TFE, used to identify requests originating from a hosted MCP deployment. Should only be used over TLS. | `""` (empty) |
| `TFE_SKIP_TLS_VERIFY` | Skip HCP Terraform or Terraform Enterprise TLS verification | `false` |
| `LOG_LEVEL` | Logging level: `trace`, `debug`, `info`, `warn`, `error`, `fatal`, `panic` (overrides `--log-level` flag) | `info` |
| `LOG_FORMAT` | Logging format: `text` or `json` (overrides `--log-format` flag)| `text` |
| `TRANSPORT_MODE` | Set to `streamable-http` to enable HTTP transport (legacy `http` value still supported) | `stdio` |
| `TRANSPORT_HOST` | Host to bind the HTTP server | `127.0.0.1` |
| `TRANSPORT_PORT` | HTTP server port | `8080` |
| `MCP_ENDPOINT` | HTTP server endpoint path | `/mcp` |
| `MCP_REDIRECT_ROOT_URL` | URL to redirect requests to `/` to | `""` |
| `MCP_KEEP_ALIVE` | Keep-alive interval for SSE connections (e.g., 30s, 1m). 0 to disable | `0` |
| `MCP_SESSION_MODE` | Session mode: `stateful` or `stateless` | `stateful` |
| `MCP_ALLOWED_ORIGINS` | Comma-separated list of allowed origins for CORS | `""` (empty) |
| `MCP_CORS_MODE` | CORS mode: `strict`, `development`, or `disabled` | `strict` |
| `MCP_TLS_CERT_FILE` | Path to TLS cert file, required for non-localhost deployment (e.g. `/path/to/cert.pem`) | `""` (empty) |
| `MCP_TLS_KEY_FILE` |  Path to TLS key file, required for non-localhost deployment (e.g. `/path/to/key.pem`)| `""` (empty) |
| `MCP_RATE_LIMIT_GLOBAL` | Global rate limit (format: `rps:burst`) | `10:20` |
| `MCP_RATE_LIMIT_SESSION` | Per-session rate limit (format: `rps:burst`) | `5:10` |
| `MCP_ORGANIZATION_ALLOWLIST` | CSV list of HCP Terraform organization names allowed to access the HTTP server | `""` (empty) |
| `MCP_FORWARD_CLIENT_IP` | Forward the client IP to HCP Terraform / TFE via `X-Forwarded-For`. Set to `true` to enable | `false` |
| `MCP_REMOTE_IP_METHOD` | How the client IP is sourced when forwarding is enabled: `RemoteAddr` (direct connection only), `X-Real-IP`, or `X-Forwarded-For` | `RemoteAddr` |
| `MCP_XFF_TRUSTED_HOPS` | Number of trusted proxy hops counted from the right of the `X-Forwarded-For` chain. Only used when `MCP_REMOTE_IP_METHOD=X-Forwarded-For` | `0` |
| `ENABLE_TF_OPERATIONS` | Enable tools that require explicit approval | `false` |
| `OTEL_METRICS_ENABLED` | Enable tools and server metrics using otel | `false` |
| `OTEL_METRICS_SERVICE_VERSION` | Version of the terraform-mcp-server sending metrics, which is used to set metric attributes. It also helps track metrics across different deployments | `latest` |
| `OTEL_METRICS_SERVICE_NAME` | Identifies the source of the metrics (e.g., "terraform-mcp-server") | `terraform-mcp-server` |
| `OTEL_METRICS_EXPORT_INTERVAL` | Controls the frequency of metric flushes | `2` |
| `OTEL_METRICS_ENDPOINT` | URL of your OTel Collector or backend | `localhost:4318` |
| `INSTANA_ENABLED` | Enable Instana instrumentation (metrics and HTTP request tracing) for the streamable-http server. Requires an Instana agent that is reachable by the server. | `false` |
| `INSTANA_SERVICE_NAME` | If Instana instrumentation is enabled, the service name to use for the MCP server | `terraform-mcp-server` |

```bash
# Stdio mode
terraform-mcp-server stdio [--log-file /path/to/log] [--log-level info] [--log-format text] [--toolsets ] [--tools ]

# StreamableHTTP mode
terraform-mcp-server streamable-http [--transport-port 8080] [--transport-host 127.0.0.1] [--mcp-endpoint /mcp] [--organization-allowlist ] [--log-file /path/to/log] [--log-level info] [--log-format text] [--toolsets ] [--tools ]
```

## Instructions

Default instructions for the MCP server is located in `cmd/terraform-mcp-server/instructions.md`, if those do not seem appropriate for your organization's Terraform practices or if the MCP server is producing inaccurate responses, please replace them with your own instructions and rebuild the container or binary. An example of such instruction is located in `instructions/example-mcp-instructions.md`

`AGENTS.md` essentially behaves as READMEs for coding agents: a dedicated, predictable place to provide the context and instructions to help AI coding agents work on your project. One `AGENTS.md` file works with different coding agents. An example of such instruction is located in `instructions/example-AGENTS.md`, in order to use it commit a file name `AGENTS.md` to the directory where your Terraform configurations reside.

## Installation

### Usage with Visual Studio Code

Add the following JSON block to your User Settings (JSON) file in VS Code. You can do this by pressing `Ctrl + Shift + P` and typing `Preferences: Open User Settings (JSON)`.

More about using MCP server tools in VS Code's [agent mode documentation](https://code.visualstudio.com/docs/copilot/chat/mcp-servers).

Version 0.3.0+ or greater

Version 0.2.3 or lower

```json
{
  "mcp": {
    "servers": {
      "terraform": {
        "command": "docker",
        "args": [
          "run",
          "-i",
          "--rm",
          "-e", "TFE_TOKEN=${input:tfe_token}",
          "-e", "TFE_ADDRESS=${input:tfe_address}",
          "hashicorp/terraform-mcp-server:1.3.0"
        ]
      }
    },
    "inputs": [
      {
        "type": "promptString",
        "id": "tfe_token",
        "description": "Terraform API Token",
        "password": true
      },
      {
        "type": "promptString",
        "id": "tfe_address",
        "description": "Terraform Address",
        "password": false
      }
    ]
  }
}
```

```json
{
  "mcp": {
    "servers": {
      "terraform": {
        "command": "docker",
        "args": [
          "run",
          "-i",
          "--rm",
          "hashicorp/terraform-mcp-server:0.2.3"
        ]
      }
    }
  }
}
```

Optionally, you can add a similar example (i.e. without the mcp key) to a file called `.vscode/mcp.json` in your workspace. This will allow you to share the configuration with others.

Version 0.3.0+ or greater

Version 0.2.3 or lower

```json
{
  "servers": {
    "terraform": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e", "TFE_TOKEN=${input:tfe_token}",
        "-e", "TFE_ADDRESS=${input:tfe_address}",
        "hashicorp/terraform-mcp-server:1.3.0"
      ]
    }
  },
  "inputs": [
    {
      "type": "promptString",
      "id": "tfe_token",
      "description": "Terraform API Token",
      "password": true
    },
    {
      "type": "promptString",
      "id": "tfe_address",
      "description": "Terraform Address",
      "password": false
    }
  ]
}
```

```json
{
  "servers": {
    "terraform": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "hashicorp/terraform-mcp-server:0.2.3"
      ]
    }
  }
}
```

[
](https://vscode.dev/redirect?url=vscode%3Amcp%2Finstall%3F%7B%22name%22%3A%22terraform%22%2C%22command%22%3A%22docker%22%2C%22args%22%3A%5B%22run%22%2C%22-i%22%2C%22--rm%22%2C%22hashicorp%2Fterraform-mcp-server%22%5D%7D)
[
](https://insiders.vscode.dev/redirect?url=vscode-insiders%3Amcp%2Finstall%3F%7B%22name%22%3A%22terraform%22%2C%22command%22%3A%22docker%22%2C%22args%22%3A%5B%22run%22%2C%22-i%22%2C%22--rm%22%2C%22hashicorp%2Fterraform-mcp-server%22%5D%7D)

### Usage with Cursor

Add this to your Cursor config (`~/.cursor/mcp.json`) or via Settings → Cursor Settings → MCP:

Version 0.3.0+ or greater

Version 0.2.3 or lower

```json
{
  "mcpServers": {
    "terraform": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e", "TFE_ADDRESS=",
        "-e", "TFE_TOKEN=",
        "hashicorp/terraform-mcp-server:1.3.0"
      ]
    }
  }
}
```

```json
{
  "servers": {
    "terraform": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "hashicorp/terraform-mcp-server:0.2.3"
      ]
    }
  }
}
```

  

### Usage with Claude Desktop / Amazon Q Developer / Kiro CLI

More about using MCP server tools in Claude Desktop [user documentation](https://modelcontextprotocol.io/quickstart/user). Read more about using MCP server in [Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/qdev-mcp.html) and [Kiro CLI](https://kiro.dev/docs/mcp/).

Version 0.3.0+ or greater

Version 0.2.3 or lower

```json
{
  "mcpServers": {
    "terraform": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e", "TFE_ADDRESS=",
        "-e", "TFE_TOKEN=",
        "hashicorp/terraform-mcp-server:1.3.0"
      ]
    }
  }
}
```

```json
{
  "mcpServers": {
    "terraform": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "hashicorp/terraform-mcp-server:0.2.3"
      ]
    }
  }
}
```

### Usage with Claude Code

More about using and adding MCP server tools in Claude Code [user documentation](https://docs.claude.com/en/docs/claude-code/mcp)

- Local (`stdio`) Transport

```sh
claude mcp add terraform -s user -t stdio -- docker run -i --rm hashicorp/terraform-mcp-server
```

- Remote (`streamable-http`) Transport

```sh
# Run server (example)
docker run -p 8080:8080 --rm -e TRANSPORT_MODE=streamable-http -e TRANSPORT_HOST=0.0.0.0 hashicorp/terraform-mcp-server

# Add to Claude Code
claude mcp add --transport http terraform http://localhost:8080/mcp
```

### Usage with Codex CLI

More about using and adding MCP server tools in Codex CLI [user documentation](https://learn.chatgpt.com/docs/extend/mcp?surface=app).

> **Note:** Add `TFE_ADDRESS` and `TFE_TOKEN` to the Docker commands for authenticated HCP Terraform or Terraform Enterprise tools.

- Local (`stdio`) Transport

```sh
codex mcp add terraform -- docker run -i --rm hashicorp/terraform-mcp-server
```

- Remote (`streamable-http`) Transport

```sh
# Run server (example)
docker run --rm -p 127.0.0.1:8080:8080 -e TRANSPORT_MODE=streamable-http -e TRANSPORT_HOST=0.0.0.0 hashicorp/terraform-mcp-server

# Add to Codex
codex mcp add terraform --url http://localhost:8080/mcp
```

### Usage with Gemini extensions

For security, avoid hardcoding your credentials, create or update `~/.gemini/.env` (where ~ is your home or project directory) for storing HCP Terraform or Terraform Enterprise credentials

```
# ~/.gemini/.env
TFE_ADDRESS=your_tfe_address_here
TFE_TOKEN=your_tfe_token_here
```

Install the extension & run Gemini

```
gemini extensions install https://github.com/hashicorp/terraform-mcp-server
gemini
```

### Usage with Bob IDE / Shell

More about using and adding MCP servers tools in Bob IDE or Shell [Using MCP in Bob](https://bob.ibm.com/docs/ide/configuration/mcp/mcp-in-bob).

Version 0.3.0+ or greater

Version 0.2.3 or lower

```json
{
  "mcpServers": {
    "terraform": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e", "TFE_ADDRESS=",
        "-e", "TFE_TOKEN=",
        "hashicorp/terraform-mcp-server:1.3.0"
      ],
      "disabled": false
    }
  }
}
```

```json
{
  "mcpServers": {
    "terraform": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "hashicorp/terraform-mcp-server:0.2.3"
      ],
      "disabled": false
    }
  }
}
```

## Install from source

Use the latest release version:

```console
go install github.com/hashicorp/terraform-mcp-server/cmd/terraform-mcp-server@latest
```

Use the main branch:

```console
go install github.com/hashicorp/terraform-mcp-server/cmd/terraform-mcp-server@main
```

Version 0.3.0+ or greater

Version 0.2.3 or lower

```json
{
  "mcp": {
    "servers": {
      "terraform": {
        "type": "stdio",
        "command": "/path/to/terraform-mcp-server",
        "env": {
          "TFE_TOKEN": ">"
        },
      }
    }
  }
}
```

```json
{
  "mcp": {
    "servers": {
      "terraform": {
        "type": "stdio",
        "command": "/path/to/terraform-mcp-server"
      }
    }
  }
}
```

## Building the Docker Image locally

Before using the server, you need to build the Docker image locally:

1. Clone the repository:
```bash
git clone https://github.com/hashicorp/terraform-mcp-server.git
cd terraform-mcp-server
```

2. Build the Docker image:
```bash
make docker-build
```

3. This will create a local Docker image that you can use in the following configuration.

```bash
# Run in stdio mode
docker run -i --rm terraform-mcp-server:dev

# Run in streamable-http mode
docker run -p 8080:8080 --rm -e TRANSPORT_MODE=streamable-http -e TRANSPORT_HOST=0.0.0.0 terraform-mcp-server:dev

# Filter tools (optional)
docker run -i --rm terraform-mcp-server:dev --toolsets=registry,terraform
docker run -i --rm terraform-mcp-server:dev --tools=search_providers,get_provider_details
```

> **Note:** When running in Docker, you should set `TRANSPORT_HOST=0.0.0.0` to allow connections from outside the container.

4. (Optional) Test connection in http mode

```bash
# Test the connection
curl http://localhost:8080/health
```

5. You can use it on your AI assistant as follow:

```json
{
  "mcpServers": {
    "terraform": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "terraform-mcp-server:dev"
      ]
    }
  }
}
```

## Available Tools

[Check out available tools here :link:](https://developer.hashicorp.com/terraform/docs/tools/mcp-server/reference#available-tools)

## Available Resources

[Check out available resources here :link:](https://developer.hashicorp.com/terraform/docs/tools/mcp-server/reference#available-tools)

## Available Metrics

Two kinds of metrics are collected.
First, standard HTTP server metrics are added by wrapping the HTTP mux with otelhttp.NewHandler(...). This emits:

1. http.server.request.body.size
2. http.server.response.body.size
3. http.server.request.duration

Second, the MCP server records custom tool metrics around tool execution using MCP hooks (BeforeCallTool / AfterCallTool). These emit:

1. mcp_tool_calls_total
2. mcp_tool_errors_total
3. mcp_tool_duration_seconds

### Tool Filtering

Control which tools are available using `--toolsets` (groups) or `--tools` (individual):

```bash
# Enable tool groups (default: registry)
terraform-mcp-server --toolsets=registry,terraform

# Enable specific tools only
terraform-mcp-server --tools=search_providers,get_provider_details,list_workspaces
```

Available toolsets: `registry`, `registry-private`, `terraform`, `all`, `default`. See `pkg/toolsets/mapping.go` for individual tool names. Cannot use both flags together.

## Transport Support

The Terraform MCP Server supports multiple transport protocols:

### 1. Stdio Transport (Default)
Standard input/output communication using JSON-RPC messages. Ideal for local development and direct integration with MCP clients.

### 2. StreamableHTTP Transport
Modern HTTP-based transport supporting both direct HTTP requests and Server-Sent Events (SSE) streams. This is the recommended transport for remote/distributed setups.

**Features:**
- **Endpoint**: `http://{hostname}:8080/mcp`
- **Health Check**: `http://{hostname}:8080/health`
- **Environment Configuration**: Set `TRANSPORT_MODE=http` or `TRANSPORT_PORT=8080` to enable
- **Organization Allowlist**: Set `MCP_ORGANIZATION_ALLOWLIST` or `--organization-allowlist` to a CSV list of allowed HCP Terraform organization names

## Session Modes

The Terraform MCP Server supports two session modes when using the StreamableHTTP transport:

- **Stateful Mode (Default)**: Maintains session state between requests, enabling context-aware operations.
- **Stateless Mode**: Each request is processed independently without maintaining session state, which can be useful for high-availability deployments or when using load balancers.

To enable stateless mode, set the environment variable:
```bash
export MCP_SESSION_MODE=stateless
```

## Token Passthrough for Centralized Deployments

When running the MCP server centrally (StreamableHTTP mode) for multiple users, each user can pass their own Terraform token via HTTP headers for RBAC enforcement. This allows a single server instance to serve multiple users with different permissions.

When `MCP_ORGANIZATION_ALLOWLIST` or `--organization-allowlist` is conf

**Official site: ** [https://github.com/hashicorp/terraform-mcp-server](https://github.com/hashicorp/terraform-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `developer tools`, `terraform`, `hashicorp`, `iac`, `official`

## MCP Configuration

- Transport: `stdio`
- Command: `docker`
- Args: `run -i --rm -v ${PWD}:/workdir ghcr.io/hashicorp/terraform-mcp-server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/hashicorp-terraform-mcp.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
