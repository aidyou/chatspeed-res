---
title: "ClickHouse MCP 服务器"
description: "ClickHouse MCP Server An MCP server for ClickHouse. Features ClickHouse Tools runquery Execute SQL queries on your ClickHouse cluster. Input: query (string): The SQL query to execute. Queries run in r…"
---

# ClickHouse MCP 服务器

ClickHouse MCP Server An MCP server for ClickHouse. Features ClickHouse Tools runquery Execute SQL queries on your ClickHouse cluster. Input: query (string): The SQL query to execute. Queries run in r…

# ClickHouse MCP Server


An MCP server for ClickHouse.

## Features

### ClickHouse Tools

* `run_query`
  * Execute SQL queries on your ClickHouse cluster.
  * Input: `query` (string): The SQL query to execute.
  * Queries run in read-only mode by default (`CLICKHOUSE_ALLOW_WRITE_ACCESS=false`), but writes can be enabled explicitly if needed.

* `list_databases`
  * List all databases on your ClickHouse cluster.

* `list_tables`
  * List tables in a database with pagination.
  * Required input: `database` (string).
  * Optional inputs:
    * `like` / `not_like` (string): Apply `LIKE` or `NOT LIKE` filters to table names.
    * `page_token` (string): Token returned by a previous call for fetching the next page.
    * `page_size` (int, default `50`): Number of tables returned per page.
    * `include_detailed_columns` (bool, default `true`): When `false`, omits column metadata for lighter responses while keeping the full `create_table_query`.
  * Response shape:
    * `tables`: Array of table objects for the current page.
    * `next_page_token`: Pass this value back to fetch the next page, or `null` when there are no more tables.
    * `total_tables`: Total count of tables that match the supplied filters.

### chDB Tools

* `run_chdb_select_query`
  * Execute SQL queries using [chDB](https://github.com/chdb-io/chdb)'s embedded ClickHouse engine.
  * Input: `query` (string): The SQL query to execute.
  * Query data directly from various sources (files, URLs, databases) without ETL processes.
  * Requires the optional `chdb` extra: `pip install 'mcp-clickhouse[chdb]'`

### Health Check Endpoint

When running with HTTP or SSE transport, a health check endpoint is available at `/health`. This endpoint:
- Returns `200 OK` (body: `OK`) if the server is healthy and can connect to ClickHouse
- Returns `503 Service Unavailable` with a generic error message if the server cannot connect to ClickHouse
- Returns `503` if a ClickHouse probe does not finish within two seconds. Concurrent requests share one in-flight probe

GET and HEAD requests to the endpoint are intentionally unauthenticated and exempt from Host and Origin validation so orchestrator probes (e.g. Kubernetes liveness/readiness, load balancers) can use runtime-assigned pod or target IPs without extra configuration. `/health` is reserved and cannot be used as the MCP transport path. The response body is deliberately minimal to avoid leaking backend version strings or error details; debug failures via the server logs.

Example:
```bash
curl http://localhost:8000/health
# Response: OK
```

## Security

### Authentication for HTTP/SSE Transports

When using HTTP or SSE transport, authentication is **required by default**. The `stdio` transport (default) does not require authentication as it only communicates via standard input/output.

Three authentication modes are supported. Pick one:

| Mode                       | When to use                               | Env var                                                                                        |
|----------------------------|-------------------------------------------|------------------------------------------------------------------------------------------------|
| Static bearer token        | Simple deployments, internal services     | `CLICKHOUSE_MCP_AUTH_TOKEN`                                                                    |
| OAuth / OIDC (via FastMCP) | Azure Entra, Google, GitHub, WorkOS, etc. | `FASTMCP_SERVER_AUTH=
` (+ provider-specific `FASTMCP_SERVER_AUTH_*` vars) |
| Disabled                   | Local development only                    | `CLICKHOUSE_MCP_AUTH_DISABLED=true`                                                            |

Startup fails if none of these are configured for HTTP/SSE transports.

#### Setting Up Authentication

1. Generate a secure token (can be any random string):
```bash
   # Using uuidgen (macOS/Linux)
   uuidgen

   # Using openssl
   openssl rand -hex 32
```

2. Configure the server with the token:
```bash
   export CLICKHOUSE_MCP_AUTH_TOKEN="your-generated-token"
```

3. Configure your MCP client to include the token in requests:

   For Claude Desktop with HTTP/SSE transport:
```json
   {
     "mcpServers": {
       "mcp-clickhouse": {
         "url": "http://127.0.0.1:8000",
         "headers": {
           "Authorization": "Bearer your-generated-token"
         }
       }
     }
   }
```

   Note: the `/health` endpoint is intentionally unauthenticated (see [Health Check Endpoint](#health-check-endpoint) above). To verify that bearer-token auth is actually rejecting unauthenticated requests, hit the MCP endpoint itself e.g. with the MCP Inspector, or by POSTing a JSON-RPC request to `/mcp` with and without the `Authorization` header and confirming the unauthenticated call returns `401`.

#### OAuth / OIDC via FastMCP

For production deployments with identity providers (Azure Entra, Google, GitHub, WorkOS, etc.), delegate authentication to [FastMCP's built-in auth providers](https://gofastmcp.com/servers/auth) instead of using a static token. Set `FASTMCP_SERVER_AUTH` to the **full class path** of a FastMCP auth provider, along with the provider-specific `FASTMCP_SERVER_AUTH_*` variables, and leave `CLICKHOUSE_MCP_AUTH_TOKEN` unset.

Example (Azure Entra):

```bash
export FASTMCP_SERVER_AUTH=fastmcp.server.auth.providers.azure.AzureProvider
export FASTMCP_SERVER_AUTH_AZURE_TENANT_ID=""
export FASTMCP_SERVER_AUTH_AZURE_CLIENT_ID=""
export FASTMCP_SERVER_AUTH_AZURE_CLIENT_SECRET=""
```

See the [FastMCP docs](https://gofastmcp.com/servers/auth) for the full list of providers and their required environment variables.

#### Development Mode (Disabling Authentication)

For local development and testing only, you can disable authentication by setting:
```bash
export CLICKHOUSE_MCP_AUTH_DISABLED=true
export CLICKHOUSE_MCP_ALLOWED_HOSTS=127.0.0.1:8000,localhost:8000
```

**WARNING:** Only use this for local development. Do not disable authentication when the server is exposed to any network.

## Configuration

This MCP server supports both ClickHouse and chDB. You can enable either or both depending on your needs.

1. Open the Claude Desktop configuration file located at:
   * On macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   * On Windows: `%APPDATA%/Claude/claude_desktop_config.json`

2. Add the following:

```json
{
  "mcpServers": {
    "mcp-clickhouse": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "mcp-clickhouse",
        "--python",
        "3.10",
        "mcp-clickhouse"
      ],
      "env": {
        "CLICKHOUSE_HOST": "",
        "CLICKHOUSE_PORT": "",
        "CLICKHOUSE_USER": "",
        "CLICKHOUSE_PASSWORD": "",
        "CLICKHOUSE_ROLE": "",
        "CLICKHOUSE_SECURE": "true",
        "CLICKHOUSE_VERIFY": "true",
        "CLICKHOUSE_CONNECT_TIMEOUT": "30"
      }
    }
  }
}
```

Update the environment variables to point to your own ClickHouse service.

Or, if you'd like to try it out with the [ClickHouse SQL Playground](https://sql.clickhouse.com/), you can use the following config:

```json
{
  "mcpServers": {
    "mcp-clickhouse": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "mcp-clickhouse",
        "--python",
        "3.10",
        "mcp-clickhouse"
      ],
      "env": {
        "CLICKHOUSE_HOST": "sql-clickhouse.clickhouse.com",
        "CLICKHOUSE_PORT": "8443",
        "CLICKHOUSE_USER": "demo",
        "CLICKHOUSE_PASSWORD": "",
        "CLICKHOUSE_SECURE": "true",
        "CLICKHOUSE_VERIFY": "true",
        "CLICKHOUSE_CONNECT_TIMEOUT": "30"
      }
    }
  }
}
```

For chDB (embedded ClickHouse engine), add the following configuration:

```json
{
  "mcpServers": {
    "mcp-clickhouse": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "mcp-clickhouse[chdb]",
        "--python",
        "3.10",
        "mcp-clickhouse"
      ],
      "env": {
        "CHDB_ENABLED": "true",
        "CLICKHOUSE_ENABLED": "false",
        "CHDB_DATA_PATH": "/path/to/chdb/data"
      }
    }
  }
}
```

You can also enable both ClickHouse and chDB simultaneously:

```json
{
  "mcpServers": {
    "mcp-clickhouse": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "mcp-clickhouse[chdb]",
        "--python",
        "3.10",
        "mcp-clickhouse"
      ],
      "env": {
        "CLICKHOUSE_HOST": "",
        "CLICKHOUSE_PORT": "",
        "CLICKHOUSE_USER": "",
        "CLICKHOUSE_PASSWORD": "",
        "CLICKHOUSE_SECURE": "true",
        "CLICKHOUSE_VERIFY": "true",
        "CLICKHOUSE_CONNECT_TIMEOUT": "30",
        "CHDB_ENABLED": "true",
        "CHDB_DATA_PATH": "/path/to/chdb/data"
      }
    }
  }
}
```

3. Locate the command entry for `uv` and replace it with the absolute path to the `uv` executable. This ensures that the correct version of `uv` is used when starting the server. On a mac, you can find this path using `which uv`.

4. Restart Claude Desktop to apply the changes.

### Optional Write Access

By default, this MCP enforces read-only queries so that accidental mutations cannot happen during exploration. To allow DDL or INSERT statements, set the `CLICKHOUSE_ALLOW_WRITE_ACCESS` environment variable to `true`. The server keeps enforcing read-only mode if the ClickHouse instance itself disallows writes.

### Destructive Operation Protection

Even when write access is enabled (`CLICKHOUSE_ALLOW_WRITE_ACCESS=true`), destructive operations require an additional opt-in flag for safety. The check covers any `DROP` statement (including the `ALTER TABLE ... DROP PARTITION` / `DROP PART` / `DROP COLUMN` clauses), any `TRUNCATE`, `DELETE` and `UPDATE` (both the lightweight statements and the `ALTER TABLE ... DELETE` / `ALTER TABLE ... UPDATE` mutations), `REPLACE TABLE`, `CREATE OR REPLACE`, `ALTER TABLE ... REPLACE PARTITION`, `ALTER TABLE ... CLEAR COLUMN` / `CLEAR INDEX` / `CLEAR PROJECTION`, and `DETACH ... PERMANENTLY`. Keywords inside string literals, quoted identifiers, and SQL comments are ignored, so they neither trigger the check nor hide a statement from it.

This check runs in the MCP server and is a best-effort guard against accidents. It is not a security boundary. The security boundary is the ClickHouse user's grants. Read-only mode (the default) is enforced server-side via `readonly=1`. The destructive-operation gate is not server-enforced.

For write mode, give the MCP server a dedicated ClickHouse user with only the privileges it needs:

```sql
CREATE USER mcp_agent IDENTIFIED BY '...';
GRANT SELECT, INSERT, CREATE TABLE, ALTER ADD COLUMN ON mydb.* TO mcp_agent;
```

Every statement outside these grants then fails server-side with `ACCESS_DENIED`, regardless of MCP flags. The server settings `max_table_size_to_drop` and `max_partition_size_to_drop` can also cap blast radius if pinned with settings constraints.

To enable destructive operations, set both flags:
```json
"env": {
  "CLICKHOUSE_ALLOW_WRITE_ACCESS": "true",
  "CLICKHOUSE_ALLOW_DROP": "true"
}
```

This two-tier approach makes accidental deletion difficult:
- **Write operations** (INSERT, CREATE, ALTER ADD COLUMN) require `CLICKHOUSE_ALLOW_WRITE_ACCESS=true`
- **Destructive operations** (DROP, TRUNCATE, DELETE, UPDATE, and the rest of the list above) additionally require `CLICKHOUSE_ALLOW_DROP=true`

### Running Without uv (Using System Python)

If you prefer to use the system Python installation instead of uv, you can install the package from PyPI and run it directly:

1. Install the package using pip:
```bash
   python3 -m pip install mcp-clickhouse
```

   To install chDB support as well:
```bash
   python3 -m pip install 'mcp-clickhouse[chdb]'
```

   To upgrade to the latest version:
```bash
   python3 -m pip install --upgrade mcp-clickhouse
```

2. Update your Claude Desktop configuration to use Python directly:

```json
{
  "mcpServers": {
    "mcp-clickhouse": {
      "command": "python3",
      "args": [
        "-m",
        "mcp_clickhouse.main"
      ],
      "env": {
        "CLICKHOUSE_HOST": "",
        "CLICKHOUSE_PORT": "",
        "CLICKHOUSE_USER": "",
        "CLICKHOUSE_PASSWORD": "",
        "CLICKHOUSE_SECURE": "true",
        "CLICKHOUSE_VERIFY": "true",
        "CLICKHOUSE_CONNECT_TIMEOUT": "30"
      }
    }
  }
}
```

Alternatively, you can use the installed script directly:

```json
{
  "mcpServers": {
    "mcp-clickhouse": {
      "command": "mcp-clickhouse",
      "env": {
        "CLICKHOUSE_HOST": "",
        "CLICKHOUSE_PORT": "",
        "CLICKHOUSE_USER": "",
        "CLICKHOUSE_PASSWORD": "",
        "CLICKHOUSE_SECURE": "true",
        "CLICKHOUSE_VERIFY": "true",
        "CLICKHOUSE_CONNECT_TIMEOUT": "30"
      }
    }
  }
}
```

Note: Make sure to use the full path to the Python executable or the `mcp-clickhouse` script if they are not in your system PATH. You can find the paths using:
- `which python3` for the Python executable
- `which mcp-clickhouse` for the installed script

## Custom Middleware

You can add custom middleware to the MCP server without modifying the source code. FastMCP provides a middleware system that allows you to intercept and process MCP protocol messages (tool calls, resource reads, prompts, etc.).

### How to Use

1. Create a Python module with middleware classes extending `Middleware` and a `setup_middleware(mcp)` function:

```python
# my_middleware.py
import logging
from fastmcp.server.middleware import Middleware, MiddlewareContext, CallNext

logger = logging.getLogger("my-middleware")

class LoggingMiddleware(Middleware):
    """Log all tool calls."""
    
    async def on_call_tool(self, context: MiddlewareContext, call_next: CallNext):
        tool_name = context.message.name if hasattr(context.message, 'name') else 'unknown'
        logger.info(f"Calling tool: {tool_name}")
        result = await call_next(context)
        logger.info(f"Tool {tool_name} completed")
        return result

def setup_middleware(mcp):
    """Register middleware with the MCP server."""
    mcp.add_middleware(LoggingMiddleware())
```

2. Set the `MCP_MIDDLEWARE_MODULE` environment variable to the module name (without `.py` extension):

```json
{
  "mcpServers": {
    "mcp-clickhouse": {
      "command": "uv",
      "args": ["run", "--with", "mcp-clickhouse", "--python", "3.10", "mcp-clickhouse"],
      "env": {
        "CLICKHOUSE_HOST": "",
        "CLICKHOUSE_USER": "",
        "CLICKHOUSE_PASSWORD": "",
        "MCP_MIDDLEWARE_MODULE": "my_middleware"
      }
    }
  }
}
```

3. Ensure your middleware module is in Python's import path (e.g., in the same directory where the MCP server runs, or installed as a package).

### Example Middleware

An example middleware module is provided in `example_middleware.py` showing common patterns:
- Logging all MCP requests
- Logging tool calls specifically
- Measuring request processing time

To use the example:
```json
"env": {
  "MCP_MIDDLEWARE_MODULE": "example_middleware"
}
```

### Middleware Capabilities

The `Middleware` base class provides hooks for different MCP operations:

- `on_message(context, call_next)` - Called for all messages
- `on_request(context, call_next)` - Called for all requests
- `on_notification(context, call_next)` - Called for all notifications
- `on_call_tool(context, call_next)` - Called when a tool is executed
- `on_read_resource(context, call_next)` - Called when a resource is read
- `on_get_prompt(context, call_next)` - Called when a prompt is retrieved
- `on_list_tools(context, call_next)` - Called when listing tools
- `on_list_resources(context, call_next)` - Called when listing resources
- `on_list_resource_templates(context, call_next)` - Called when listing resource templates
- `on_list_prompts(context, call_next)` - Called when listing prompts

Each hook receives a `MiddlewareContext` object containing the message and metadata, and a `call_next` function to continue the pipeline.

### Dynamic Client Configuration via Context State

Middleware can override ClickHouse client configuration on a per-request basis using the `CLIENT_CONFIG_OVERRIDES_KEY` context state key. The server merges these overrides with the base configuration from environment variables.

```python
from fastmcp.server.dependencies import get_context
from mcp_clickhouse.mcp_server import CLIENT_CONFIG_OVERRIDES_KEY

ctx = get_context()
ctx.set_state(CLIENT_CONFIG_OVERRIDES_KEY, {
    "connect_timeout": 60,
    "send_receive_timeout": 120
})
```

This enables advanced use cases like dynamic timeout adjustments, tenant-specific routing, or per-user connection settings.

The state value must be a dictionary. Nested `settings` and `generic_args` values must be
mappings and are merged with the base configuration. Invalid values fail the tool call before
a ClickHouse client is created. `CLICKHOUSE_ROLE` remains active unless the override explicitly
supplies `settings.role`. Top-level `role` and `ch_role` keys, plus the same keys under
`generic_args`, are rejected.

Treat these overrides as trusted middleware input. Middleware must authenticate and authorize
request-derived values before setting them. A per-request ClickHouse role is connection
configuration, not a tenant authorization boundary. Enforce tenant isolation with ClickHouse
users, roles, and grants.

## Development

1. In `test-services` directory run `docker compose up -d` to start the ClickHouse cluster.

2. Add the following variables to a `.env` file in the root of the repository.

*Note: The use of the `default` user in this context is intended solely for local development purposes.*

```bash
CLICKHOUSE_HOST=localhost
CLICKHOUSE_PORT=8123
CLICKHOUSE_USER=default
CLICKHOUSE_PASSWORD=clickhouse
```

3. Run `uv sync` to install the dependencies. To install `uv` follow the instructions [here](https://docs.astral.sh/uv/). Then do `source .venv/bin/activate`.

4. For easy testing with the MCP Inspector, run `fastmcp dev mcp_clickhouse/mcp_server.py` to start the MCP server.

5. To test with HTTP transport and the health check endpoint:
```bash
   # For development, disable authentication
   CLICKHOUSE_MCP_SERVER_TRANSPORT=http CLICKHOUSE_MCP_AUTH_DISABLED=true CLICKHOUSE_MCP_ALLOWED_HOSTS=127.0.0.1:8000,localhost:8000 python -m mcp_clickhouse.main

   # Or with authentication (generate a token first)
   CLICKHOUSE_MCP_SERVER_TRANSPORT=http CLICKHOUSE_MCP_AUTH_TOKEN="your-token" python -m mcp_clickhouse.main

   # Then in another terminal:
   curl http://localhost:8000/health
```

### Environment Variables

Configuration is split into **independent** groups. Mixing them up is a common cause of hard-to-debug connection failures:

| Group | Variables | Controls |
|-------|-----------|----------|
| **ClickHouse database connection** | `CLICKHOUSE_HOST`, `CLICKHOUSE_PORT`, `CLICKHOUSE_SECURE`, `CLICKHOUSE_VERIFY`, … | How **this MCP server** connects to your ClickHouse cluster over the **HTTP interface** |
| **MCP server / transport** | `CLICKHOUSE_MCP_*`, `FASTMCP_SERVER_AUTH`, `FASTMCP_SERVER_AUTH_*` | MCP transport, authentication, and query-tool execution limits |
| **Middleware / chDB** | `MCP_MIDDLEWARE_MODULE`, `CHDB_*` | Optional extensions |

> [!IMPORTANT]
> Variables such as `CLICKHOUSE_SECURE`, `CLICKHOUSE_VERIFY`, and `CLICKHOUSE_PORT` apply to the **ClickHouse database** connection only. They do **not** configure TLS, ports, or auth for the MCP protocol endpoint.
>
> Example: if the MCP server runs in Kubernetes behind an ingress that terminates TLS, that is an **MCP transport** concern. Keep `CLICKHOUSE_SECURE` aligned with how the pod reaches ClickHouse itself (HTTPS → `true`, plain HTTP → `false`). Setting `CLICKHOUSE_SECURE=false` because the MCP server is behind an ingress will make the server dial ClickHouse over HTTP—often against an HTTPS-only port—and produce opaque HTTP/TLS errors in the server logs.

#### ClickHouse database connecti

**官方网站：** [https://github.com/ClickHouse/mcp-clickhouse](https://github.com/ClickHouse/mcp-clickhouse)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`, `development`
- 标签：`database`, `clickhouse`, `sql`, `developer tools`, `official`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`run mcp-clickhouse`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/clickhouse-mcp.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
