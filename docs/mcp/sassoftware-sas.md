---
title: "SAS Viya MCP 服务器"
description: "SAS Viya MCP Server A Model Context Protocol (MCP) server for executing SAS code, training AutoML projects, scoring models and so much more for SAS Viya environments. Features - 75 tools across 9 selectable tiers, spanni"
---

# SAS Viya MCP 服务器

SAS Viya MCP Server A Model Context Protocol (MCP) server for executing SAS code, training AutoML projects, scoring models and so much more for SAS Viya environments. Features - 75 tools across 9 selectable tiers, spanni

# SAS Viya MCP Server

A Model Context Protocol (MCP) server for executing SAS code, training AutoML projects, scoring models and so much more for SAS Viya environments.

## Features

- 75 tools across 9 selectable tiers, spanning the Analytics Life Cycle on SAS Viya
- Prompt Templates for improving your SAS Code
- OAuth2 authentication with PKCE flow
- HTTP-based MCP server compatible with MCP clients

## Articles & Videos

Here you can find getting articles on how to use and integrate the SAS MCP Server in different tools and what to build with it:

- [From REST APIs to AI Agents: Why the SAS Viya MCP Server Matters](https://communities.sas.com/t5/SAS-Communities-Library/From-REST-APIs-to-AI-Agents-Why-the-SAS-Viya-MCP-Server-Matters/ta-p/992010)
- [Connecting GitHub Copilot to SAS Viya with the SAS Viya MCP Server](https://communities.sas.com/t5/SAS-Communities-Library/Connecting-GitHub-Copilot-to-SAS-Viya-with-the-SAS-Viya-MCP/ta-p/987191)
- [Bring Your Own Key: SAS Viya MCP Server with GitHub Copilot CLI](https://communities.sas.com/t5/SAS-Communities-Library/Bring-Your-Own-Key-SAS-Viya-MCP-with-GitHub-Copilot-CLI/ta-p/991530)
- [Putting the SAS Viya MCP Server to Work in GitHub Copilot](https://communities.sas.com/t5/SAS-Communities-Library/Putting-the-SAS-Viya-MCP-Server-to-Work-in-GitHub-Copilot/ta-p/987193)
- [Connecting Claude Code CLI to SAS Viya with the SAS Viya MCP Server](https://communities.sas.com/t5/SAS-Communities-Library/Connecting-Claude-Code-CLI-to-SAS-Viya-with-the-SAS-Viya-MCP/ta-p/988775)
- [Putting the SAS Viya MCP Server to Work in Claude Code CLI](https://communities.sas.com/t5/SAS-Communities-Library/Putting-the-SAS-Viya-MCP-Server-to-Work-in-Claude-Code-CLI/ta-p/988922)
- [Integration with SAS Retrieval Agent Manager (RAM)](https://github.com/sassoftware/sas-retrieval-agent-manager-examples/tree/main/examples/container_mcp_servers/sas_mcp_server)

## Getting Started
### Prerequisites
- Required
    - [Python 3.12+](https://www.python.org/downloads)
    - [uv 0.8+](https://github.com/astral-sh/uv)
    - [SAS Viya environment](https://www.sas.com/en_us/software/viya.html) with compute service
    - Setup the Viya environment for MCP
        - See [configuration.md](https://github.com/sassoftware/sas-mcp-server/blob/HEAD/examples/configuration.md)

- Optional
    - [Docker](https://docs.docker.com/engine/install): refer to [container setup](https://github.com/sassoftware/sas-mcp-server/blob/HEAD/deploy/docker.md)
    - Kubernetes: sample manifests (Contour or nginx) and a Helm chart in [deploy/](https://github.com/sassoftware/sas-mcp-server/blob/HEAD/deploy/README.md)

### Installation

1. Clone the repository:
```sh
git clone 
cd sas-mcp-server
```

2. Install dependencies
```sh
uv sync
```

NOTE: This will by default create a virtual environment called .venv in the project's root directory.

If for some reason the virtual environment is not created, please run `uv venv` and then re-run `uv sync`.

### Usage

1. Configure environment variables:
```sh
cp .env.sample .env
```

Edit `.env` and set
```sh
VIYA_ENDPOINT=https://your-viya-server.com
```

2. Start the MCP server (see [Choosing a deployment mode](#choosing-a-deployment-mode) below):

**Option A: HTTP mode** (pre-run the server, connect from MCP client)
```sh
uv run app
```
The server will be available at `http://localhost:8134/mcp` by default. Authentication is handled via OAuth2 PKCE flow in the browser.

**Option B: Stdio mode** (MCP client starts the server on demand)

Authenticate once. Two equivalent options:

```sh
# Option B1 — if you have the SAS Viya CLI installed:
sas-viya auth loginCode

# Option B2 — built-in helper, no external CLI needed (Viya 2022.11+):
uv run sas-mcp-login
```

Both flows write an access token to a local cache (`~/.sas/credentials.json` and `~/.sas-mcp-server/credentials.json` respectively); the stdio server reads whichever it finds. When the token expires, re-run the same command.

Then configure your MCP client to launch the server directly (see below).

**Option C: Docker / Podman** (containerized deployment)

Pull the pre-built image from GitHub Container Registry:
```sh
docker pull ghcr.io/sassoftware/sas-mcp-server:latest
docker run -e VIYA_ENDPOINT=https://your-viya-server.com -p 8134:8134 ghcr.io/sassoftware/sas-mcp-server:latest
```

Or build locally from source:
```sh
docker build -t sas-mcp-server .
docker run -e VIYA_ENDPOINT=https://your-viya-server.com -p 8134:8134 sas-mcp-server
```

Available image tags:
- `latest` — most recent tagged release
- `..
` (e.g. `1.0.0`) — specific release
- `.` (e.g. `1.0`) — latest patch of a minor release
- `edge` — tip of `main` (unreleased, for testing)
- `sha-` — pinned to a specific commit

**Programmatic clients with a pre-existing Viya token**

If your caller already holds a Viya access token (e.g. an automation script that obtained one via the SAS Viya CLI), start the HTTP-mode server with `ALLOW_RAW_BEARER=true` and pass the token directly:

```sh
curl -H "Authorization: Bearer $VIYA_TOKEN" http://localhost:8134/mcp ...
```

The server validates the token against Viya's JWKS and uses it upstream as-is, bypassing the MCP JWT swap. The default OAuth2 PKCE flow keeps working alongside — both client types share the same `/mcp` endpoint.

If your Viya APIs are intentionally exposed without auth (for example, a local/dev Compute API endpoint), set `VIYA_AUTH=false` to bypass all SASLogon/OAuth flows in both HTTP and stdio modes. In this mode the server sends upstream requests without an `Authorization` header.

If your compute deployment does not expose `/compute/contexts` and only supports a fixed session, set `COMPUTE_SESSION_ID=`. The compute tools will use that session directly instead of creating context-backed sessions.

### Choosing a deployment mode

| | **HTTP** | **Stdio** | **Docker** | **Kubernetes** |
|---|---|---|---|---|
| **How it runs** | Long-running server you start separately | MCP client spawns it on demand | Containerized HTTP server | Containerized, behind an ingress |
| **Authentication** | OAuth2 PKCE flow (browser popup) | Cached token via `sas-viya` CLI or `sas-mcp-login` | OAuth2 PKCE flow (browser popup) | PKCE and/or raw Viya bearer token |
| **Best for** | Multi-user or shared setups; production-like environments | Single-user local development; quick experimentation | Team deployments; CI/CD; environments without Python installed | Shared/organisational deployments alongside Viya |
| **Requires** | Python + uv | Python + uv (+ optional `sas-viya` CLI) | Docker or Podman only | A cluster, an ingress controller, a TLS secret |
| **Credentials stored?** | No — user authenticates interactively | No — only an access token (not a password) is cached | No — user authenticates interactively | No — a signing key in a `Secret`; users authenticate themselves |
| **MCP client config** | Point client to `http://localhost:8134/mcp` | Client runs `uv run app-stdio` | Point client to `http://host:8134/mcp` | Point client to `https:///mcp` |

**Quick guidance:**
- **Starting out or exploring?** Use **stdio** — one `sas-viya auth loginCode` or `uv run sas-mcp-login`, then your MCP client manages the server lifecycle.
- **Need secure, interactive auth?** Use **HTTP** — no stored passwords, each user authenticates via browser.
- **Deploying for a team or on a server?** Use **Docker** — portable, no Python dependency on the host, easy to integrate with orchestrators.
- **Running it for a whole organisation?** Use **Kubernetes** — sample manifests and a Helm chart are in [deploy/](https://github.com/sassoftware/sas-mcp-server/blob/HEAD/deploy/README.md), including the routing the OAuth flow needs for either **Contour** (the chart's default, and the only one that can mount the server under a path prefix on an existing hostname) or **ingress-nginx**.
- **Using Gemini CLI?** Use **stdio** — Gemini CLI does not support HTTP mode or browser-based OAuth. See [Gemini CLI configuration](https://github.com/sassoftware/sas-mcp-server/blob/HEAD/examples/configuration.md#gemini-cli).
- **Installing from a client's server catalogue?** That path runs the published container in **stdio** mode (`app-stdio`), not as an HTTP server, so it authenticates from your `~/.sas` token cache — which has to be mounted into the container at `/app/.sas`.

### Limiting exposed tools (tiers)

Tools are grouped into numbered tiers. By default the server exposes all of them; set `MCP_TIERS` to expose only a subset — handy for keeping a client's tool list small and focused, or hiding capabilities a deployment shouldn't offer. Accepts ranges and comma lists (e.g. `MCP_TIERS=0-4` or `MCP_TIERS=0,1,6,7`); unset means all tiers.

| Tier | Group |
|---|---|
| 0 | Compute Contexts & Code Execution |
| 1 | Data Discovery |
| 2 | Data Operations & Files |
| 3 | Reports & Visualization |
| 4 | Batch Jobs & Async Execution |
| 5 | Automated Machine Learning |
| 6 | Model Management & Scoring |
| 7 | Decisioning (SAS Intelligent Decisioning) |
| 8 | Workbench (Execute Code Only) |

```sh
# Example: expose only compute/discovery/data-ops and reporting
MCP_TIERS=0-3 uv run app
```

### Read-only mode

Set `MCP_READ_ONLY=true` to expose only tools that neither change server-side state nor cause server-side work — 43 of the 75 tools. Withheld tools are never registered, so they are absent from the client's tool list entirely: the model cannot see them, so it cannot attempt them.

This is a filter over the tiers, not a tier of its own — the read/write split cuts across every tier (Tier 3 has both `get_report` and `delete_report`). The two settings compose:

```sh
# Every read tool, all tiers
MCP_READ_ONLY=true uv run app

# Read tools of the reporting and decisioning tiers only
MCP_TIERS=3,7 MCP_READ_ONLY=true uv run app
```

The definition is strict: a tool qualifies only if it can neither write nor start work. Beyond the obvious create/update/delete tools, that withholds:

| Withheld | Why |
|---|---|
| `execute_sas_code`, `submit_batch_job` | Run arbitrary code — can perform any operation, including deletes |
| `score_data`, `catalog_run_agent`, `catalog_run_adhoc_analysis` | Start server-side jobs and leave run records, though they return data |
| `promote_table_to_memory` | Mutates CAS in-memory state |
| `cancel_job`, `reset_compute_session` | Destroy something the caller owns |

Classification is fail-closed: a tool that is not explicitly classified as read-only is withheld. The list lives in [`src/sas_mcp_server/tools/_access.py`](https://github.com/sassoftware/sas-mcp-server/blob/HEAD/src/sas_mcp_server/tools/_access.py), and a test asserts it covers every registered tool, so a newly added tool cannot silently land in read-only mode.

### Tool annotations (what clients are told)

The same classification is **advertised** to every client as [MCP tool annotations](https://modelcontextprotocol.io/specification/2025-03-26/server/tools#tool-annotations) on each `tools/list` entry — whether or not read-only mode is on:

| Hint | Derived from |
|---|---|
| `readOnlyHint` | exactly the read-only set above — one table, so what a client is told and what `MCP_READ_ONLY` enforces cannot drift |
| `destructiveHint` | tools that can remove or overwrite existing state: arbitrary code (`execute_sas_code`, `submit_batch_job`), `delete_*`, `cancel_job`, `reset_compute_session`, the `update_*` PUTs, `apply_report_operations`, `create_report`/`copy_report` (their `replace` conflict policy), `publish_ml_champion_model` |
| `idempotentHint` | reads, the `update_*` PUTs, deletes, `cancel_job`, `reset_compute_session`, `promote_table_to_memory` |
| `openWorldHint` | only tools that can reach beyond Viya: arbitrary code and the upload tools' `url` source |

Clients use these to shape their approval UX — e.g. Claude groups read-only tools for one-click approval and warns before destructive ones — and to decide when to interrupt the user. They are hints, not enforcement: the spec tells clients to treat them as untrusted unless the server is trusted, and `MCP_READ_ONLY` remains the server-side control. Without annotations a client must assume the spec's pessimistic defaults (writable, destructive, open-world) for every tool, so this only ever reduces friction. The browser landing page marks each tool `read-only` / `write` / `destructive` from the same hints.

### Available Tools

The headings below match the numbered **tiers** above, so `MCP_TIERS` maps directly to the tools you expose (e.g. `MCP_TIERS=0-3` gives Tiers 0–3).

#### Tier 0 — Compute Contexts & Code Execution
- **execute_sas_code**: Execute SAS code snippets and retrieve execution results (log and listing output). Runs in a reusable, per-user compute session that is kept warm across calls, so SAS state (WORK tables, macro variables, assigned librefs) persists between successive calls — use **reset_compute_session** to start fresh.
- **list_compute_contexts**: List available compute contexts
- **reset_compute_session**: Delete the cached compute session for a context, discarding its SAS state and forcing a fresh session on the next call

#### Tier 1 — Data Discovery
*Information Catalog (metadata discovery & profiling):*
- **catalog_search**: Search the catalog for assets (tables, columns, reports, …) using the SAS catalog search grammar (free text, facets like `AssetType:Report`, ranges). Each hit carries a `resource_uri` you can hand to the matching tool (e.g. `get_report`, `get_castable_data`).
- **catalog_search_helper**: Discover how to query the catalog — list the available facets, or the valid values for one facet — so you can build precise `catalog_search` queries.
- **catalog_find_instance**: Resolve the catalog *instance* for a source-asset `resource_uri`, bridging a search hit to the profiling and download tools without handling an instance id by hand.
- **catalog_run_adhoc_analysis**: Submit an ad-hoc profiling job for a table. NLP enrichment (language, sentiment, semantic IDs) is on by default, populating `informationPrivacy`, `nlpTerms`, `nlpTags`, and `mostImportantFields`.
- **catalog_get_adhoc_analysis**: Poll a profiling job and cross-check the target instance, reporting `profile_ready` once results have landed on the asset — so a download isn't fired too early.
- **catalog_download_table_profile**: Download a table's data dictionary and column profile as CSV, identified by either `instance_id` or `resource_uri`.
- **catalog_list_agents**: List the catalog's discovery agents (the crawlers that populate metadata).
- **catalog_run_agent**: Start a discovery agent run (asynchronous) to crawl its data source and refresh catalog metadata.
- **catalog_get_agent_history**: Inspect an agent's run history — status and how much metadata each run enumerated/added/updated/removed.

*CAS data (in-memory):*
- **list_cas_servers**: List available CAS servers
- **list_caslibs**: List CAS libraries on a server
- **list_castables**: List tables in a CAS library
- **list_source_tables**: List source tables not yet loaded into memory (candidates for promotion)
- **get_castable_info**: Get table metadata (row count, columns, size)
- **get_castable_columns**: Get column names, types, labels, formats
- **get_castable_data**: Fetch sample rows from a CAS table
- **query_data**: Run a FedSQL `SELECT` against CAS or compute data and get the rows back — one SQL surface over both storage tiers. Pick the tier with `target` (`cas` for `caslib.table`, `compute` for `libref.table`); joins, subqueries, aggregation, and `UNION` all work, and the row cap is applied server-side by the tool (a `LIMIT` you write is ignored, since a malformed one is silently discarded by CAS). Optionally returns the query as `CREATE VIEW` text for you to run yourself. Reads only: writes are refused pre-flight, and SAS macro triggers (`%`/`&`) are rejected because the macro processor would expand them outside SQL. Note the two tiers cannot be joined in one statement.

*Compute libraries (SAS/Compute, within a compute context):*
- **list_compute_libraries**: List the SAS libraries (librefs) assigned in a compute context
- **list_compute_tables**: List the tables in a SAS library within a compute context
- **list_compute_columns**: List the columns of a table in a SAS library

#### Tier 2 — Data Operations & Files
- **upload_data**: Upload a data file into a CAS table — read **server-side** so the data never passes through the model's context — from `file_path` (the server reads it off disk) or `url` (the server fetches it and converts it to the multipart upload the endpoint requires). Ingests the formats the casManagement `uploadTable` API accepts — csv, tsv (csv + tab delimiter), xls, xlsx (single sheet), sas7bdat, sashdat — auto-detected from the extension or set with `data_format`. parquet is not accepted by that endpoint and is rejected up front with guidance (load via a path-based caslib + `promote_table_to_memory`, or convert to csv/sas7bdat).
- **upload_inline_data**: Create a *small* CAS table from inline csv/tsv text passed as a string (a lookup/mapping table the model builds on the fly, or a quick test table). The payload travels through the model's context, so it's for tiny tables only — use **upload_data** for files or anything larger.
- **promote_table_to_memory**: Load a source table into memory at global scope (idempotent)
- **list_files**: List files in the Viya Files Service
- **upload_file**: Upload a file to the Viya Files Service, optionally into a Content folder (`parent_folder_uri`). Content comes from exactly one of `content` (inline text), `file_path` (read **server-side**, binary-safe — xlsx, zip, images — gated by `ALLOW_LOCAL_FILE_UPLOAD`), or `url` (server-side fetch)
- **download_file**: Download file content

#### Tier 3 — Reports & Visualization
- **list_reports**: List Visual Analytics reports
- **get_report**: Get report metadata and definition
- **export_report**: export a report (or specific report objects) in any format the VA service supports — `package` (zip), `pdf`, `png`, `svg`, `csv`, `tsv`, `xlsx`, or `summary`. Text formats come back inline, `png` as image content, and binary formats (`package`/`pdf`/`xlsx`) as an embedded file with the right MIME type.
- **describe_report_objects**: Discover what a report can contain — the eight report operations and every addable object (bar chart, list table, geo map, key value, …) with a one-line purpose, its data roles, common options, and an example payload. Call with no arguments for the catalog (including an intent→object map, placement guide, layout recipes, and the API's hard limits), `object_type=` for one object's contract (colloquial aliases like `kpi` resolve), `category=` to filter, or `operation=` for one operation's full shape — `operation="addData"` documents `dataItems` (column renames, SAS formats, aggregations, geography classification). Backs the `apply_report_operations` loop.
- **create_report**: Create a Visual Analytics report and return its id. Optionally pass an `operations` array to build the whole report in one atomic call; the result carries the created page/object names+labels and a verify hint.
- **apply_report_operations**: The authoring workhorse — apply an ordered batch of native VA operations (`addData`, `addPage`, `addObject`, `updateObject`, `setParameterValue`, `updateData`, `changeData`, `applyDataView`) to a report. Give a page a **title** with `addPage`'s `title` field (a text band at the top of the page body — VA headers are controls-only); title every chart at add time via `options.object.title`; arrange objects with **placement** — `page`, `relativeToObject` (left/right/top/bottom for columns, rows, and grids), `container` (group into a `standardContainer`), or `report` (`new_page` creates-and-names a page inline for one-batch multi-page reports). The batch is atomic. Validates every operation, object key, and placement against the catalog first (reporting all errors at once), supports `dry_run`, handles the ETag concurrency handshake, and — with `result_report_name`/`result_folder` — applies the batch **save-as** to a new report, leaving the source untouched. Typical loop: `describe_report_objects` → `get_castable_columns` → `apply_report_operations` → `get_report_outline` / `export_re

**官方网站：** [https://github.com/sassoftware/sas-mcp-server](https://github.com/sassoftware/sas-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`, `development`
- 标签：`sas`, `data analysis`, `analytics`, `developer tools`, `official`

## MCP 配置

- 传输方式：`http`
- 启动命令：``
- 参数：无

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/sassoftware-sas.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
