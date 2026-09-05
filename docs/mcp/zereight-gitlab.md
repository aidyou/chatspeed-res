---
title: "GitLab MCP"
description: "GitLab MCP Server English 한국어 简体中文 📖 Documentation → Setup guides, environment variables, and the full tool reference live on the hosted docs site. @zereight/mcp-gitlab Agent-workflow-optimized GitLab…"
---

# GitLab MCP

GitLab MCP Server English 한국어 简体中文 📖 Documentation → Setup guides, environment variables, and the full tool reference live on the hosted docs site. @zereight/mcp-gitlab Agent-workflow-optimized GitLab…

# GitLab MCP Server


[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/zereight/gitlab-mcp)
[![MCP Toplist](https://mcptoplist.com/badge/io.github.zereight%2Fgitlab-mcp.svg)](https://mcptoplist.com/server/io.github.zereight%2Fgitlab-mcp) [![mcpindex](https://mcpindex.ai/api/v1/badge/io-github-zereight-gitlab-mcp)](https://mcpindex.ai/server/io-github-zereight-gitlab-mcp)

[English](https://github.com/zereight/gitlab-mcp/blob/HEAD/README.md) | [한국어](https://github.com/zereight/gitlab-mcp/blob/HEAD/README.ko.md) | [简体中文](https://github.com/zereight/gitlab-mcp/blob/HEAD/README.zh-CN.md)

📖 **[Documentation →](https://zereight.github.io/gitlab-mcp/)** Setup guides, environment variables, and the full tool reference live on the hosted docs site.

[![Star History Chart](https://github.com/zereight/gitlab-mcp/blob/HEAD/assets/star-history.png)](https://www.star-history.com/?repos=zereight%2Fgitlab-mcp&type=date&legend=top-left)

## @zereight/mcp-gitlab

**Agent-workflow-optimized GitLab MCP** — manage projects, merge requests, issues, pipelines, wiki, releases, tags, milestones, and more through stdio, SSE, and Streamable HTTP.

Supports PAT, OAuth, read-only mode, dynamic API URLs, and remote authorization for VS Code, Claude, Cursor, Copilot, and other MCP clients.

### Why use this GitLab MCP?

- **229 tools + `discover_tools`** — start with a small toolset; activate more at runtime without CQRS-style grouping
- **MR 2-step review** — `list_merge_request_changed_files` → batched `get_merge_request_file_diff`
- **Agent Skill built in** — workflow guidance in `skills/gitlab-mcp/`
- **Flexible auth** — Personal Access Token, local OAuth2 browser flow, MCP OAuth proxy, and per-request remote authorization
- **Multiple transports** — stdio for local clients, SSE for legacy clients, and Streamable HTTP for modern remote deployments
- **Client-friendly setup** — examples for Claude Code, Codex, Antigravity, OpenCode, Copilot, Cline, Roo Code, Cursor, Kilo Code, and Amp Code
- **Self-hosted ready** — works with custom GitLab instances, proxy settings, and dynamic API URL routing

### How we compare

| | @zereight/mcp-gitlab | GitLab MCP A (community CQRS-style) |
|---|----------------------|-------------------------------------|
| **Best for** | AI agent workflows | Enterprise multi-instance / grouped tools |
| **Tool model** | ~229 granular tools + `discover_tools` | ~50–60 grouped `browse_*` / `manage_*` tools |
| **MR review** | 2-step batched diff | Varies |
| **Node.js** | >=18 | Often >=24 |
| **License** | MIT | Varies |

[Full comparison →](https://github.com/zereight/gitlab-mcp/blob/HEAD/docs/comparison/community-gitlab-mcp-a.md)

Quick start: choose either Personal Access Token or OAuth2 setup below, install `@zereight/mcp-gitlab`, and use `zereight-mcp-gitlab` in your MCP client configuration.

### Client Setup Guides

- [Claude Code Setup Guide](https://github.com/zereight/gitlab-mcp/blob/HEAD/docs/clients/claude-code.md)
- [VS Code Setup Guide](https://github.com/zereight/gitlab-mcp/blob/HEAD/docs/clients/vscode.md)
- [GitHub Copilot Setup Guide](https://github.com/zereight/gitlab-mcp/blob/HEAD/docs/clients/copilot.md)
- [Codex Setup Guide](https://github.com/zereight/gitlab-mcp/blob/HEAD/docs/clients/codex.md)
- [Cursor Setup Guide](https://github.com/zereight/gitlab-mcp/blob/HEAD/docs/clients/cursor.md)
- JSON-Based MCP Clients Setup Guide - for Factory AI Droid, OpenClaw, and OpenCode style clients
- [OAuth2 Authentication Setup Guide](https://github.com/zereight/gitlab-mcp/blob/HEAD/docs/auth/oauth-setup.md)
- [Environment Variables Reference](https://github.com/zereight/gitlab-mcp/blob/HEAD/docs/configuration/environment-variables.md)
- [Stateless Mode — Multi-Pod HPA](https://github.com/zereight/gitlab-mcp/blob/HEAD/docs/configuration/stateless-mode.md)
- [Custom Agents and Multiple PAT Setup](https://github.com/zereight/gitlab-mcp/blob/HEAD/docs/auth/custom-agent-multiple-pat.md)

## Usage

### Setup Overview

#### Authentication Methods

The server supports four authentication methods:

**For local/desktop use** (most common):

1. **Personal Access Token** (`GITLAB_PERSONAL_ACCESS_TOKEN`) — simplest setup
2. **OAuth2 — Local Browser** (`GITLAB_USE_OAUTH`) — recommended for better security

**For server/remote deployments**:

3. **OAuth2 — MCP Proxy** (`GITLAB_MCP_OAUTH`) — for remote MCP clients such as Claude.ai
4. **Remote Authorization** (`REMOTE_AUTHORIZATION`) — multi-user deployments where each caller provides their own token

#### Quick setup paths

- **Claude Code**: see [Claude Code Setup Guide](https://github.com/zereight/gitlab-mcp/blob/HEAD/docs/clients/claude-code.md)
- **VS Code**: see [VS Code Setup Guide](https://github.com/zereight/gitlab-mcp/blob/HEAD/docs/clients/vscode.md)
- **GitHub Copilot**: see [GitHub Copilot Setup Guide](https://github.com/zereight/gitlab-mcp/blob/HEAD/docs/clients/copilot.md)
- **Codex**: see [Codex Setup Guide](https://github.com/zereight/gitlab-mcp/blob/HEAD/docs/clients/codex.md)
- **Cursor**: see [Cursor Setup Guide](https://github.com/zereight/gitlab-mcp/blob/HEAD/docs/clients/cursor.md)
- **Factory AI Droid / OpenClaw / OpenCode style clients**: see JSON-Based MCP Clients Setup Guide
- **OAuth browser flow details**: see [OAuth2 Authentication Setup Guide](https://github.com/zereight/gitlab-mcp/blob/HEAD/docs/auth/oauth-setup.md)
- **OAuth without a localhost callback** (SSO, remote shell, background clients): run `zereight-mcp-gitlab auth` (GitLab 17.9+ device flow; 17.2–17.8 need `oauth2_device_grant_flow`), then start the server with `GITLAB_USE_OAUTH=true`. See [standalone device-flow command](https://github.com/zereight/gitlab-mcp/blob/HEAD/docs/auth/oauth-setup.md#standalone-device-flow-auth-command).

For the simplest local setup, start with a Personal Access Token. For browser-based local auth, use OAuth2. For remote or multi-user deployments, continue to the MCP OAuth and Remote Authorization sections later in this README.

Install the server once:

```shell
brew tap zereight/gitlab-mcp https://github.com/zereight/gitlab-mcp
brew install zereight/gitlab-mcp/zereight-mcp-gitlab
```

Or with npm:

```shell
npm install -g @zereight/mcp-gitlab
```

The examples use `zereight-mcp-gitlab`, a less collision-prone alias for the legacy `mcp-gitlab` binary. If your MCP client cannot find it, use the absolute path from `which zereight-mcp-gitlab`.

No global install? Pin `npx` to the previous stable release (the version these docs recommend), for example `npx -y @zereight/mcp-gitlab@2.1.53`. If you always want the newest release, use `npx -y @zereight/mcp-gitlab@latest` instead. The server prints a notice to stderr on startup when a newer version is available (disable with `GITLAB_DISABLE_VERSION_CHECK=true`).

#### Using CLI Arguments (for clients with env var issues)

Some MCP clients (like GitHub Copilot CLI) have issues with environment variables. Use CLI arguments instead:

```json
{
  "mcpServers": {
    "gitlab": {
      "command": "zereight-mcp-gitlab",
      "args": ["--token=YOUR_GITLAB_TOKEN", "--api-url=https://gitlab.com/api/v4"],
      "tools": ["*"]
    }
  }
}
```

**Available CLI arguments:**

- `--token` - GitLab Personal Access Token (replaces `GITLAB_PERSONAL_ACCESS_TOKEN`)
- `--api-url` - GitLab API URL (replaces `GITLAB_API_URL`)
- `--read-only=true` - Enable read-only mode (replaces `GITLAB_READ_ONLY_MODE`, deprecated — prefer `--permission-mode=readonly`)
- `--permission-mode` - Permission level: `readonly`, `modify` (no delete tools), or `full` (replaces `GITLAB_PERMISSION_MODE`, default `full`)
- `--use-wiki=true` - Enable wiki API (replaces `USE_GITLAB_WIKI`, legacy — prefer `GITLAB_TOOLSETS=wiki`)
- `--use-milestone=true` - Enable milestone API (replaces `USE_MILESTONE`, legacy — prefer `GITLAB_TOOLSETS=milestones`)
- `--use-pipeline=true` - Enable pipeline API (replaces `USE_PIPELINE`, legacy — prefer `GITLAB_TOOLSETS=pipelines`)
- `--disable-version-check=true` - Disable the startup new-version notice (replaces `GITLAB_DISABLE_VERSION_CHECK`)

CLI arguments take precedence over environment variables.

`zereight-mcp-gitlab auth` is a subcommand (not an MCP server flag). It runs GitLab device flow and exits. See [CLI Arguments](https://github.com/zereight/gitlab-mcp/blob/HEAD/docs/getting-started/cli-arguments.md#auth).

> **Fine-grained tool filtering:** use `GITLAB_PERMISSION_MODE=modify` to allow create/update while
> blocking every delete tool (including delete mutations through `execute_graphql` and
> `push_files` `delete`/`move` actions), or
> `GITLAB_PERMISSION_MODE=readonly` for read-only access. You can also
> enable toolset groups with `GITLAB_TOOLSETS=`, allow-list individual tools with
> `GITLAB_TOOLS=` (e.g. read-only groups plus a few specific write tools), and
> deny-list by pattern with `GITLAB_DENIED_TOOLS_REGEX`. The legacy `USE_GITLAB_WIKI` /
> `USE_MILESTONE` / `USE_PIPELINE` flags are kept for backward compatibility only.
> See [Tools Reference](https://github.com/zereight/gitlab-mcp/blob/HEAD/docs/tools/index.md#feature-toggles) and
> [Environment Variables](https://github.com/zereight/gitlab-mcp/blob/HEAD/docs/configuration/environment-variables.md).

- sse

```shell
docker run -i --rm \
  -e HOST=0.0.0.0 \
  -e GITLAB_PERSONAL_ACCESS_TOKEN=your_gitlab_token \
  -e GITLAB_API_URL="https://gitlab.com/api/v4" \
  -e GITLAB_PERMISSION_MODE=readonly \
  -e GITLAB_TOOLSETS=wiki,milestones,pipelines \
  -e SSE=true \
  -e SSE_AUTH_TOKEN=your_mcp_sse_token \
  -p 3333:3002 \
  zereight050/gitlab-mcp
```

```json
{
  "mcpServers": {
    "gitlab": {
      "type": "sse",
      "url": "http://localhost:3333/sse",
      "headers": {
        "Authorization": "Bearer your_mcp_sse_token"
      }
    }
  }
}
```

- streamable-http

```shell
docker run -i --rm \
  -e HOST=0.0.0.0 \
  -e REMOTE_AUTHORIZATION=true \
  -e GITLAB_API_URL="https://gitlab.com/api/v4" \
  -e GITLAB_PERMISSION_MODE=readonly \
  -e GITLAB_TOOLSETS=wiki,milestones,pipelines \
  -e STREAMABLE_HTTP=true \
  -p 3333:3002 \
  zereight050/gitlab-mcp
```

```json
{
  "mcpServers": {
    "gitlab": {
      "type": "streamable-http",
      "url": "http://localhost:3333/mcp",
      "headers": {
        "Authorization": "Bearer glpat-..."
      }
    }
  }
}
```

#### Using MCP OAuth Proxy (`GITLAB_MCP_OAUTH`)

> **For server/remote deployments only.** This mode requires the MCP server to be deployed with a publicly accessible HTTPS URL. For local/desktop use, see `GITLAB_USE_OAUTH` above.

For remote MCP clients that support the MCP OAuth specification (e.g. Claude.ai).
The server acts as a full OAuth 2.0 authorization server — unauthenticated requests
receive a `401 + WWW-Authenticate` response, which triggers the OAuth browser flow
automatically on the client side.

Remote MCP clients such as OpenCode, MCPJam, and Claude.ai can send their own
callback URL during authorization. If you cannot register every client callback
URL in GitLab, enable `GITLAB_OAUTH_CALLBACK_PROXY=true`. With callback proxy
mode, GitLab only needs one registered redirect URI: `{MCP_SERVER_URL}/callback`.

`GITLAB_OAUTH_REDIRECT_URI` is for local OAuth (`GITLAB_USE_OAUTH`) only. It does
not override remote MCP OAuth client callback URLs and should not be used to fix
remote `Unregistered redirect_uri` errors.

This variable exists because the local OAuth flow starts a browser on the same
machine as the MCP server and listens for the callback on a local HTTP server,
for example `http://127.0.0.1:8888/callback`.

Remote MCP OAuth is different. In `GITLAB_MCP_OAUTH=true` mode, the MCP client
provides its own callback URL during `/authorize`. `GITLAB_OAUTH_REDIRECT_URI`
does not replace that client-provided URL.

| Mode             | Enable with             | Callback variable                  | GitLab redirect URI                                     |
| ---------------- | ----------------------- | ---------------------------------- | ------------------------------------------------------- |
| Local OAuth      | `GITLAB_USE_OAUTH=true` | `GITLAB_OAUTH_REDIRECT_URI`        | `http://127.0.0.1:8888/callback` or your local callback |
| Remote MCP OAuth | `GITLAB_MCP_OAUTH=true` | `GITLAB_OAUTH_CALLBACK_PROXY=true` | `{MCP_SERVER_URL}/callback`                             |

Use `GITLAB_OAUTH_REDIRECT_URI` only when the MCP server itself owns the local
browser callback. Use `GITLAB_OAUTH_CALLBACK_PROXY=true` when a remote MCP client
owns the callback URL.

**How it works**: You deploy this MCP server somewhere with a public HTTPS URL. MCP
clients connect to `{MCP_SERVER_URL}/mcp`. The server handles the OAuth 2.0 flow,
exchanging credentials with GitLab on behalf of the client.

**Prerequisites**:

1. A publicly accessible HTTPS server URL (`MCP_SERVER_URL`) — use [ngrok](https://ngrok.com) for local testing
2. A pre-registered GitLab OAuth application with `api` (or `read_api`) scopes
   — Go to `Admin area` → `Applications`, set Redirect URI to `{MCP_SERVER_URL}/callback`

| Environment Variable          | Required | Description                                                                                                                             |
| ----------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `GITLAB_MCP_OAUTH`            | ✅       | Set to `true` to enable                                                                                                                 |
| `GITLAB_API_URL`              | ✅       | GitLab API base URL                                                                                                                     |
| `GITLAB_OAUTH_APP_ID`         | ✅       | GitLab OAuth Application ID                                                                                                             |
| `MCP_SERVER_URL`              | ✅       | Public HTTPS URL of this MCP server                                                                                                     |
| `STREAMABLE_HTTP`             | ✅       | Must be `true`                                                                                                                          |
| `GITLAB_OAUTH_CALLBACK_PROXY` | optional | Set to `true` to use the MCP server's fixed `/callback` URL                                                                             |
| `GITLAB_OAUTH_SCOPES`         | optional | Comma-separated scopes (default: `api,read_api,read_user`)                                                                              |
| `GITLAB_OAUTH_ALLOWED_GROUPS` | optional | Comma-separated group full paths — only members (and subgroup members) may obtain a token (replaces deprecated `GITLAB_ALLOWED_GROUPS`) |

When `STREAMABLE_HTTP=true`, server-side GitLab credentials (`GITLAB_PERSONAL_ACCESS_TOKEN`, `GITLAB_JOB_TOKEN`, `GITLAB_AUTH_COOKIE_PATH`, or `GITLAB_USE_OAUTH`) require `REMOTE_AUTHORIZATION=true`, `GITLAB_MCP_OAUTH=true`, or `STREAMABLE_HTTP_AUTH_TOKEN`.

> **Troubleshooting `Unregistered redirect_uri`**
>
> Check the `redirect_uri` in the browser URL. If it points to a client callback
> such as `http://127.0.0.1:xxxxx/.../callback`, enable:
>
> ```env
> GITLAB_OAUTH_CALLBACK_PROXY=true
> ```
>
> Do not fix remote MCP OAuth by changing `GITLAB_OAUTH_REDIRECT_URI`. That
> variable is for local OAuth (`GITLAB_USE_OAUTH`) only.

```shell
docker run -i --rm \
  -e HOST=0.0.0.0 \
  -e GITLAB_MCP_OAUTH=true \
  -e GITLAB_OAUTH_CALLBACK_PROXY=true \
  -e STREAMABLE_HTTP=true \
  -e MCP_SERVER_URL=https://your-server.example.com \
  -e GITLAB_API_URL="https://gitlab.com/api/v4" \
  -e GITLAB_OAUTH_APP_ID=your_app_id \
  -p 3000:3002 \
  zereight050/gitlab-mcp
```

MCP client configuration:

```json
{
  "mcpServers": {
    "gitlab": {
      "type": "http",
      "url": "https://your-server.example.com/mcp"
    }
  }
}
```

#### Using Remote Authorization (`REMOTE_AUTHORIZATION`)

> **For server/remote deployments only.** Each HTTP caller provides their own GitLab token directly in request headers — no OAuth flow involved.

For multi-user or multi-tenant deployments where each caller provides their own
GitLab token in the HTTP request header. No OAuth flow — the MCP server forwards
the token to GitLab on behalf of the caller.

**Header priority**: `Private-Token` > `JOB-TOKEN` > `Authorization: Bearer`

| Environment Variable                          | Required | Description                                                                                                             |
| --------------------------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------- |
| `REMOTE_AUTHORIZATION`                        | ✅       | Set to `true` to enable                                                                                                 |
| `STREAMABLE_HTTP`                             | ✅       | Must be `true`                                                                                                          |
| `ENABLE_DYNAMIC_API_URL`                      | optional | Allow per-request GitLab URL via `X-GitLab-API-URL` header                                                              |
| `GITLAB_ALLOWED_HOSTS`                        | optional | Comma-separated allowed `X-GitLab-API-URL` hosts; `GITLAB_API_URL` hosts are always allowed                             |
| `GITLAB_ALLOW_UNAUTHENTICATED_TOOL_DISCOVERY` | optional | Allow unauthenticated `initialize`, `notifications/initialized`, and `tools/list` only (tool calls still require auth)  |
| `MCP_SERVER_URL` / `MCP_ALLOWED_HOSTS` / `MCP_ALLOWED_ORIGINS` | optional | Allowed public `/mcp` host/origin values for DNS rebinding protection                                   |
| `MCP_TRUST_PROXY`                             | optional | Trust `Forwarded` / `X-Forwarded-*` headers behind a reverse proxy (download URLs, Express `req.ip`, `/mcp` IP rate limits, OAuth rate limits) |

`GITLAB_ALLOW_UNAUTHENTICATED_TOOL_DISCOVERY=true` is intended for MCP gateways
or admin UIs that need to inspect tool metadata before a user provides a GitLab
token. Leave it disabled unless the tool list is safe to expose in your deployment.

When `MCP_SERVER_URL` is not set, remote download URLs fall back to the local
server address. Set `MCP_TRUST_PROXY=true` only if the server is reachable through a
trusted reverse proxy and direct client access to the MCP server is blocked.
This enables Express `trust proxy` for Streamable HTTP and SSE, derives public
download URLs from `Forwarded` / `X-Forwarded-Proto` / `X-Forwarded-Host` /
`X-Forwarded-Prefix`, and keeps OAuth endpoint rate limiting working when
proxies send `X-Forwarded-For` with a client port (for example `1.2.3.4:5678`).
Existing OAuth+proxy deployments must set this explicitly after the flag was
introduced.

**Example request headers**:

```http
Private-Token: glpat-xxxxxxxxxxxxxxxxxxxx
```

or using a Bearer token:

```http
Authorization: Bearer glpat-xxxxxxxxxxxxxxxxxxxx
```

> ⚠️ `REMOTE_AUTHORIZATION` is **not compatible** with SSE transport. `STREAMABLE_HTTP=true` is required.

### Environment Variables

Use the dedicated reference for the full environment variable list:

- [Environment Variables Reference](https://github.com/zereight/gitlab-mcp/blob/HEAD/docs/configuration/environment-variables.md)

Most users only need one of these starting sets:

- **Local PAT**: `GITLAB_PERSONAL_ACCESS_TOKEN`, `GITLAB_API_URL`
- **Local OAuth**: `GITLAB_USE_OAUTH=true`, `GITLAB_OAUTH_CLIENT_ID`, `GITLAB_OAUTH_REDIRECT_URI`, `GITLAB_API_URL`
- **Remote multi-user HTTP**: `STREAMABLE_HTTP=true`, `REMOTE_AUTHORIZATION=true` (or `GITLAB_MCP_OAUTH=true`), `MCP_TRUST_PROXY=true` (behind a reverse proxy), `MAX_REQUESTS_PER_MINUTE=300`, `MCP_SERVER_URL` or `MCP_ALLOWED_HOSTS`, `HOST`, `PORT`
- **Multiple side-by-side deployments**: set a distinct `MCP_SERVER_NAME` per instance (e.g. `gitlab-selfhosted-readonly`) so clients, logs, and telemetry can tell them apart
- **Multi-pod HPA (stateless)**: above + `OAUTH_STATELESS_MODE=true`, `OAUTH_STATELESS_SECRET` (same across all pods). See [Stateless Mode](https://github.com/zereight/gitlab-mcp/blob/HEAD/docs/configuration/stateless-mode.md).

Commonly referenced variables:

- `GITLAB_API_URL`
- `GITLAB_PERSONAL_ACCESS_TOKEN`
- `GITLAB_USE_OAUTH`
- `REMOTE_AUTHORIZATION`
- `MCP_TRUST_PROXY`
- `MAX_REQUESTS_PER_MINUTE`
- `MAX_SESSIONS`
- `MCP_ALLOWED_HOSTS`
- `MCP_ALLOWED_ORIGINS`
- `GITLAB_MCP_OAUTH`
- `GITLAB_OAUTH_CALLBACK_PROXY`
- `OAUTH_REGISTER_RATE_LIMIT_PER_HOUR`
- `OAUTH_STATELESS_MODE`
- `OAUTH_STATELESS_SECRET`

The reference document also covers:

- auth and OAuth variables
- MCP OAuth proxy variables
- project and tool filtering variables
- dynamic tool discovery via `discover_tools` (on-demand toolset activation)
- transport and session variables
- proxy and TLS variables

For callback proxy mode details, see 

**Official site: ** [https://github.com/zereight/gitlab-mcp](https://github.com/zereight/gitlab-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `developer tools`, `gitlab`, `version control`, `ci/cd`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @zereight/mcp-gitlab --token YOUR_GITLAB_TOKEN --url https://gitlab.com`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/zereight-gitlab.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
