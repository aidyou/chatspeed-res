---
title: "Next.js DevTools MCP"
description: "Next.js DevTools MCP next-devtools-mcp is a Model Context Protocol (MCP) server that connects coding agents like Claude and Cursor to your running Next.js dev server. It is a thin connector. It discovers running Next.js "
---

# Next.js DevTools MCP

Next.js DevTools MCP next-devtools-mcp is a Model Context Protocol (MCP) server that connects coding agents like Claude and Cursor to your running Next.js dev server. It is a thin connector. It discovers running Next.js 

# Next.js DevTools MCP


`next-devtools-mcp` is a Model Context Protocol (MCP) server that connects coding agents like Claude and Cursor to your running Next.js dev server.

It is a **thin connector**. It discovers running Next.js 16+ dev servers and proxies their built-in MCP endpoint (`/_next/mcp`) so agents get live runtime errors, routes, and logs. It also ships two **gateways** that point agents at tools they run directly: version-accurate docs and the [`agent-browser`](https://github.com/vercel-labs/agent-browser) CLI.

> [!NOTE]
> Docs and migration workflows no longer live in this server. Next.js bundles its own docs at `node_modules/next/dist/docs/`, and upgrade / Cache Components workflows are distributed as agent skills. See [Migrating from 0.3.x](#migrating-from-03x).

## Requirements

- [Node.js](https://nodejs.org/) v20.19 or a newer [LTS](https://github.com/nodejs/Release#release-schedule) version
- [npm](https://www.npmjs.com/) or [pnpm](https://pnpm.io/)
- Next.js 16+ with a running dev server (for `nextjs_index` / `nextjs_call`)

## Install

Install for all your coding agents with [`add-mcp`](https://www.npmjs.com/package/add-mcp):

```bash
npx add-mcp next-devtools-mcp@latest
```

Add `-y` to skip the prompt and install to all detected agents. Add `-g` to install globally across all projects.

Or add the config to your MCP client manually:

```json
{
  "mcpServers": {
    "next-devtools": {
      "command": "npx",
      "args": ["-y", "next-devtools-mcp@latest"]
    }
  }
}
```

> [!NOTE]
> `next-devtools-mcp@latest` keeps your client on the latest version.

### Client-specific setup

Amp

```bash
amp mcp add next-devtools -- npx next-devtools-mcp@latest
```

Or follow [Amp's MCP docs](https://ampcode.com/manual#mcp) with the config above.

Claude Code

```bash
claude mcp add next-devtools npx next-devtools-mcp@latest
```

Or edit your MCP settings file with the config above.

Codex

```bash
codex mcp add next-devtools -- npx next-devtools-mcp@latest
```

**Windows 11:** add environment variables and a longer startup timeout to `.codex/config.toml`:

```toml
env = { SystemRoot="C:\\Windows", PROGRAMFILES="C:\\Program Files" }
startup_timeout_ms = 20_000
```

Cursor

[Install in Cursor](https://cursor.com/en/install-mcp?name=next-devtools&config=eyJjb21tYW5kIjoibnB4IC15IG5leHQtZGV2dG9vbHMtbWNwQGxhdGVzdCJ9)

Or go to `Cursor Settings` → `MCP` → `New MCP Server` and use the config above.

Gemini

```bash
# Project
gemini mcp add next-devtools npx next-devtools-mcp@latest

# Global
gemini mcp add -s user next-devtools npx next-devtools-mcp@latest
```

Google Antigravity

Add to `.gemini/antigravity/mcp_config.json`:

```json
{
  "mcpServers": {
    "next-devtools": {
      "command": "npx",
      "args": ["-y", "next-devtools-mcp@latest"]
    }
  }
}
```

See the [Antigravity MCP docs](https://antigravity.google/docs/mcp).

VS Code / Copilot

```bash
code --add-mcp '{"name":"next-devtools","command":"npx","args":["-y","next-devtools-mcp@latest"]}'
```

Or follow the official VS Code MCP setup guide.

Warp

`Settings | AI | Manage MCP Servers` → `+ Add`:
- Name: `next-devtools`
- Command: `npx`
- Arguments: `-y, next-devtools-mcp@latest`

## Quick Start

Start your Next.js dev server:

```bash
npm run dev
```

Next.js 16+ enables its MCP endpoint by default at `http://localhost:3000/_next/mcp`. `next-devtools-mcp` discovers and connects to it automatically — no config needed.

Then ask your agent about the running app:

```
Next Devtools, what errors are in my Next.js application?
Next Devtools, show me the structure of my routes
Next Devtools, what's in the development server logs?
```

The agent calls `nextjs_index` to discover servers, then `nextjs_call` to query their real state.

## Tools

| Tool           | What it does                                                                              |
| -------------- | ----------------------------------------------------------------------------------------- |
| `nextjs_index` | Discover running Next.js dev servers and list each one's runtime MCP tools.                |
| `nextjs_call`  | Call a runtime tool on a discovered server (errors, routes, logs, Server Actions).        |
| `nextjs_docs`  | **Gateway.** Point the agent at version-accurate docs in `node_modules/next/dist/docs/`.  |
| `browser_eval` | **Gateway.** Point the agent at the [`agent-browser`](https://github.com/vercel-labs/agent-browser) CLI for browser automation. |

The gateways do not do the work themselves — they tell the agent where the docs are or how to install/run the CLI, and the agent runs it directly (faster than proxying through MCP).

nextjs_index — discover servers

Scans common ports for running Next.js 16+ dev servers and lists each server's built-in runtime tools at `/_next/mcp`. No parameters.

Runtime tools exposed by Next.js (varies by version):
- `get_errors` — current build, runtime, and type errors
- `get_logs` — path to the dev log file (browser console + server output)
- `get_page_metadata` — routes, pages, component metadata
- `get_project_metadata` — project structure, config, dev server URL
- `get_server_action_by_id` — resolve a Server Action ID to its source file

Output: JSON listing discovered servers (port, PID, URL) and their tools.

nextjs_call — run a runtime tool

Calls one runtime tool on a discovered server. Run `nextjs_index` first to find the port and tool name.

Input:
- `port` (required) — dev server port
- `toolName` (required) — runtime tool to invoke
- `args` (optional) — arguments object, only if the tool requires them

```jsonc
{ "port": 3000, "toolName": "get_errors" }
```

Output: JSON with the tool's result.

nextjs_docs — find version-accurate docs

Does **not** fetch docs. Next.js 16+ ships its full docs (markdown, matching your installed version) at `node_modules/next/dist/docs/`. This tool returns that path and how to read it, so the agent uses version-accurate docs instead of training-data guesses. On older Next.js, it recommends `npx @next/codemod@latest upgrade latest`.

Input: `topic` (optional), `project_path` (optional, defaults to cwd).

browser_eval — set up browser automation

Does **not** drive the browser. It detects whether [`agent-browser`](https://github.com/vercel-labs/agent-browser) is installed and returns either the entry point (`agent-browser skills get core --full`) or the install steps (`npm install -g agent-browser`, then `agent-browser install`), so the agent runs the CLI directly.

Input: `task` (optional) — used only to tailor the guidance.

## Migrating from 0.3.x

Starting in 0.4.0, `next-devtools-mcp` is a thin connector.

**Changed:**
- `nextjs_docs` no longer fetches docs over the network. It points the agent at the docs Next.js bundles at `node_modules/next/dist/docs/` (or recommends upgrading). The `nextjs-docs://llms-index` resource is removed.

**Removed:**
- `init` tool — it only enforced the old docs-fetch workflow.
- `upgrade_nextjs_16` and `enable_cache_components` tools and their prompts — now distributed as agent skills.
- All `cache-components://`, `nextjs16://`, and `nextjs-fundamentals://` resources — superseded by the bundled docs.

What remains: `nextjs_index`, `nextjs_call`, `nextjs_docs`, and `browser_eval`.

## Privacy & Telemetry

`next-devtools-mcp` collects anonymous usage telemetry to improve the tool:

- **Tool usage** — which MCP tools are invoked (e.g. `nextjs_index`, `nextjs_call`)
- **Error events** — anonymous error messages when tools fail
- **Session metadata** — session ID, timestamps, basic environment (OS, Node.js version)

**Not collected:** your code, file contents or paths, personal data, credentials, or tool arguments (only tool names).

Local files live under `~/.next-devtools-mcp/` (anonymous `telemetry-id`, `telemetry-salt`, and a debug log `mcp.log`).

**Opt out** by setting the environment variable (add it to `~/.zshrc` / `~/.bashrc` to persist):

```bash
export NEXT_TELEMETRY_DISABLED=1
```

Delete local telemetry data anytime:

```bash
rm -rf ~/.next-devtools-mcp
```

## Troubleshooting

**`ERR_MODULE_NOT_FOUND` referencing `next-devtools-mcp/dist`** — clear your npx cache and restart your MCP client. The server reinstalls fresh.

**`[error] No server info found`** — `nextjs_index` / `nextjs_call` need a running Next.js 16+ dev server:
1. Start it: `npm run dev`
2. Confirm Next.js 16+ (the `/_next/mcp` endpoint only exists there)
3. Verify it started without errors

`browser_eval` and `nextjs_docs` work without a dev server.

## Local Development

```bash
git clone https://github.com/vercel/next-devtools-mcp.git
cd next-devtools-mcp
pnpm install
pnpm build
```

Point your MCP client at the local build:

```json
{
  "mcpServers": {
    "next-devtools": {
      "command": "node",
      "args": ["/absolute/path/to/next-devtools-mcp/dist/index.js"]
    }
  }
}
```

Or with Codex:

```bash
codex mcp add next-devtools-local -- node dist/index.js
```

See the [Next.js MCP documentation](https://nextjs.org/docs/app/guides/mcp) for how MCP works with Next.js and coding agents.

## License

MIT

**官方网站：** [https://github.com/vercel/next-devtools-mcp](https://github.com/vercel/next-devtools-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `next.js`, `react`, `web development`, `official`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`next-devtools-mcp@latest`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/vercel-next-devtools.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
