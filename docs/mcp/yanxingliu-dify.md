---
title: "dify-mcp-server"
description: "Server for using Dify. It achieves the invocation of the Dify workflow by calling the tools of MCP."
---

# dify-mcp-server

Server for using Dify. It achieves the invocation of the Dify workflow by calling the tools of MCP.

# Model Context Protocol (MCP) Server for dify workflows
A simple implementation of an MCP server for using [dify](https://github.com/langgenius/dify). It achieves the invocation of the Dify workflow by calling the tools of MCP.
## 🔨Installation
The server can be installed via [Smithery](https://smithery.ai/server/dify-mcp-server) or manually. Config.yaml is required for both methods. Thus, we need to prepare it before installation.

### Prepare config.yaml
Before using the mcp server, you should prepare a config.yaml to save your dify_base_url and dify_sks. The example config like this:
```yaml
dify_base_url: "https://cloud.dify.ai/v1"
dify_app_sks:
  - "app-sk1"
  - "app-sk2"
```
You can run the following command in your terminal to quickly create a configuration file:
```
mkdir -p ~/tools && cat > ~/tools/config.yaml
```

**Official site: ** [https://github.com/YanxingLiu/dify-mcp-server](https://github.com/YanxingLiu/dify-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `developer tools`, `other`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uv`
- Args: `--directory ${DIFY_MCP_SERVER_PATH} run dify_mcp_server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/yanxingliu-dify.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
