---
title: "MongoDB MCP Server"
description: "MongoDB MCP Server A Model Context Protocol server for interacting with MongoDB Databases and MongoDB Atlas. Quick Start Using the official MongoDB plugins for AI agents MongoDB MCP Server comes bundl…"
---

# MongoDB MCP Server

MongoDB MCP Server A Model Context Protocol server for interacting with MongoDB Databases and MongoDB Atlas. Quick Start Using the official MongoDB plugins for AI agents MongoDB MCP Server comes bundl…

# MongoDB MCP Server

A Model Context Protocol server for interacting with MongoDB Databases and MongoDB Atlas.

### Quick Start

#### Using the official MongoDB plugins for AI agents

MongoDB MCP Server comes bundled with the official MongoDB plugins for AI agents. The following plugins are available:

**`mongodb-atlas`** — connects to the MongoDB-hosted Atlas MCP server over OAuth. This does not require you to run anything locally, and is the recommended way to connect to MongoDB Atlas from your AI agent:

- Cursor: [marketplace](https://cursor.com/marketplace/mongodb/mongodb-atlas)
- VSCode: Open the Extensions view (`⇧⌘X` / `Ctrl+Shift+X`), search for `@agentPlugins`, and install `mongodb-atlas`.
- Claude: [marketplace](https://claude.com/plugins/mongodb-atlas)
- Codex: Open `/plugins` and install `mongodb-atlas`.
- GitHub Copilot CLI: Run `copilot plugin install mongodb-atlas`.
- Grok: Open `/marketplace` in Grok Build and install `mongodb-atlas`.

**`mongodb`** — runs the MongoDB MCP server locally and connects to any self-managed deployment:

- Cursor: [marketplace](https://cursor.com/marketplace/mongodb/mongodb)
- Claude: [marketplace](https://claude.com/plugins/mongodb)
- Gemini: [marketplace](https://geminicli.com/extensions/?name=mongodbagent-skills)
- Codex: Run `codex plugin marketplace add mongodb/agent-skills`, then open `/plugins` and install `mongodb`.
- GitHub Copilot CLI: Run `copilot plugin install mongodb`.
- Grok: Open `/marketplace` in Grok Build and install `mongodb`.

#### Using the setup script

You can manually set up the local MCP server by running the following command:

```bash
npx -y mongodb-mcp-server@latest setup
```

This will guide you through an interactive setup process, including configuring your MongoDB connection string or Atlas API credentials.

For more advanced setup options, see the [Manual Setup](#manual-setup) section below.

#### Using the MongoDB MCP Server setup skill

You can add and use the MongoDB MCP Server setup skill to configure your local MCP server using an AI agent.

```bash
npx skills add https://github.com/mongodb/agent-skills --skill mongodb-mcp-setup
```

#### Using manual configuration

See [Manual Setup](#manual-setup) for instructions on how to manually configure the MongoDB MCP Server.

## 📚 Table of Contents

- [🚀 Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Manual Setup](#manual-setup)
- [🛠️ Supported Tools](#supported-tools)
  - [MongoDB Atlas Tools](#mongodb-atlas-tools)
  - [MongoDB Database Tools](#mongodb-database-tools)
  - [MongoDB Assistant Tools](#mongodb-assistant-tools)
- [📄 Supported Resources](#supported-resources)
- [⚙️ Configuration](#configuration)
  - [Configuration Options](#configuration-options)
  - [Atlas API Access](#atlas-api-access)
  - [Configuration Methods](#configuration-methods)
    - [Environment Variables](#environment-variables)
    - [Command-Line Arguments](#command-line-arguments)
    - [MCP Client Configuration](#mcp-configuration-file-examples)
    - [Proxy Support](#proxy-support)
- [🚀 Deploy on Public Clouds](#deploy-on-public-clouds)
  - [Azure Cloud](#azure)
- [🤝 Contributing](#contributing)

## Prerequisites

> [!NOTE]
> Node 20.x support is deprecated and will be removed in a future release. Please upgrade to Node 22.13 or later. See https://nodejs.org/en/blog/migrations/v20-to-v22 for migration details.

- Node.js
  - At least v22.13.0. Check with `node -v`.

- A MongoDB connection string or Atlas API credentials.
  - **_Service Accounts Atlas API credentials_** are required to use the Atlas tools. You can create a service account in MongoDB Atlas and use its credentials for authentication. See [Atlas API Access](#atlas-api-access) for more details.
  - If you have a MongoDB connection string, you can use it directly to connect to your MongoDB instance.

## Manual Setup

> **🔒 Security Recommendation 1:** When using Atlas API credentials, be sure to assign only the minimum required permissions to your service account. See [Atlas API Permissions](#atlas-api-permissions) for details.

> **🔒 Security Recommendation 2:** For enhanced security, we strongly recommend using environment variables to pass sensitive configuration such as connection strings and API credentials instead of command line arguments. Command line arguments can be visible in process lists and logged in various system locations, potentially exposing your secrets. Environment variables provide a more secure way to handle sensitive information.

Most MCP clients require a configuration file to be created or modified to add the MCP server.

Note: The configuration file syntax can be different across clients. Please refer to the following links for the latest expected syntax:

- [Devin AI](https://www.mongodb.com/docs/mcp-server/get-started/?ai-client=devin)
- [Claude Desktop & Web](https://www.mongodb.com/docs/mcp-server/get-started/?ai-client=claude-desktop-web)
- [Cursor](https://www.mongodb.com/docs/mcp-server/get-started/?ai-client=cursor)
- [Codex](https://www.mongodb.com/docs/mcp-server/get-started/?ai-client=codex)
- [Other AI clients](https://www.mongodb.com/docs/mcp-server/get-started/?ai-client=other)

> **Default Safety Notice:** All examples below include `--readOnly` by default to ensure safe, read-only access to your data. Remove `--readOnly` if you need to enable write operations.

#### Option 1: Connection String

You can pass your connection string via environment variables, make sure to use a valid username and password.

```json
{
  "mcpServers": {
    "MongoDB": {
      "command": "npx",
      "args": ["-y", "mongodb-mcp-server@latest", "--readOnly"],
      "env": {
        "MDB_MCP_CONNECTION_STRING": "mongodb://localhost:27017/myDatabase"
      }
    }
  }
}
```

NOTE: The connection string can be configured to connect to any MongoDB cluster, whether it's a local instance or an Atlas cluster.

#### Option 2: Connect to the MongoDB Atlas-Managed MCP Server

When working with MongoDB Atlas, the recommended approach is to install the [`mongodb-atlas` plugin](#using-the-official-mongodb-plugins-for-ai-agents) for your AI agent, which handles OAuth authentication automatically.

For manual configuration, see the [client-specific instructions](https://www.mongodb.com/docs/mcp-server/get-started/) for setting up the Atlas Remote MCP server with OAuth. Alternatively, you can connect using the [`mongodb-atlas-mcp-remote`](https://github.com/mongodb-js/mongodb-mcp-server/blob/HEAD/packages/mongodb-atlas-mcp-remote/README.md) package with Service Account credentials — see the [package README](https://github.com/mongodb-js/mongodb-mcp-server/blob/HEAD/packages/mongodb-atlas-mcp-remote/README.md) for setup instructions.

> **Note:** You cannot authenticate to the remote MongoDB MCP server using a static API key over HTTP. You must either:
>
> - Use a client that supports the OAuth flow.
> - Use the [`mongodb-atlas-mcp-remote`](https://github.com/mongodb-js/mongodb-mcp-server/blob/HEAD/packages/mongodb-atlas-mcp-remote/README.md) stdio server, which you can authenticate into using the static `MDB_MCP_API_CLIENT_ID` and `MDB_MCP_API_CLIENT_SECRET` environment variables.

To connect with the `mongodb-atlas-mcp-remote` stdio server using Service Account credentials, add it to your client's MCP configuration:

```json
{
  "mcpServers": {
    "mongodb-atlas-mcp-remote": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "mongodb-atlas-mcp-remote@latest"],
      "env": {
        "MDB_MCP_API_CLIENT_ID": "$CLIENT_ID",
        "MDB_MCP_API_CLIENT_SECRET": "$SECRET"
      }
    }
  }
}
```

#### Option 3: Atlas API Credentials

Use your Atlas API Service Accounts credentials. Must follow all the steps in [Atlas API Access](#atlas-api-access) section.

```json
{
  "mcpServers": {
    "MongoDB": {
      "command": "npx",
      "args": ["-y", "mongodb-mcp-server@latest", "--readOnly"],
      "env": {
        "MDB_MCP_API_CLIENT_ID": "your-atlas-service-accounts-client-id",
        "MDB_MCP_API_CLIENT_SECRET": "your-atlas-service-accounts-client-secret"
      }
    }
  }
}
```

#### Option 4: Standalone Service using environment variables and command line arguments

You can source environment variables defined in a config file or explicitly set them like we do in the example below and run the server via npx.

```shell
# Set your credentials as environment variables first
export MDB_MCP_API_CLIENT_ID="your-atlas-service-accounts-client-id"
export MDB_MCP_API_CLIENT_SECRET="your-atlas-service-accounts-client-secret"

# Then start the server
npx -y mongodb-mcp-server@latest --readOnly
```

> **💡 Platform Note:** The examples above use Unix/Linux/macOS syntax. For Windows users, see [Environment Variables](#environment-variables) for platform-specific instructions.

- For a complete list of configuration options see [Configuration Options](#configuration-options)
- To configure your Atlas Service Accounts credentials please refer to [Atlas API Access](#atlas-api-access)
- Connection String via environment variables in the MCP file [example](#connection-string-with-environment-variables)
- Atlas API credentials via environment variables in the MCP file [example](#atlas-api-credentials-with-environment-variables)

#### Option 5: Using Docker

You can run the MongoDB MCP Server in a Docker container, which provides isolation and doesn't require a local Node.js installation.

#### Run with Environment Variables

You may provide either a MongoDB connection string OR Atlas API credentials:

##### Option A: No configuration

```shell
docker run --rm -i \
  mongodb/mongodb-mcp-server:latest
```

##### Option B: With MongoDB connection string

```shell
# Set your credentials as environment variables first
export MDB_MCP_CONNECTION_STRING="mongodb+srv://username:password@cluster.mongodb.net/myDatabase"

# Then start the docker container
docker run --rm -i \
  -e MDB_MCP_CONNECTION_STRING \
  -e MDB_MCP_READ_ONLY="true" \
  mongodb/mongodb-mcp-server:latest
```

> **💡 Platform Note:** The examples above use Unix/Linux/macOS syntax. For Windows users, see [Environment Variables](#environment-variables) for platform-specific instructions.

##### Option C: With Atlas API credentials

```shell
# Set your credentials as environment variables first
export MDB_MCP_API_CLIENT_ID="your-atlas-service-accounts-client-id"
export MDB_MCP_API_CLIENT_SECRET="your-atlas-service-accounts-client-secret"

# Then start the docker container
docker run --rm -i \
  -e MDB_MCP_API_CLIENT_ID \
  -e MDB_MCP_API_CLIENT_SECRET \
  -e MDB_MCP_READ_ONLY="true" \
  mongodb/mongodb-mcp-server:latest
```

> **💡 Platform Note:** The examples above use Unix/Linux/macOS syntax. For Windows users, see [Environment Variables](#environment-variables) for platform-specific instructions.

##### Docker in MCP Configuration File

Without options:

```json
{
  "mcpServers": {
    "MongoDB": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-e",
        "MDB_MCP_READ_ONLY=true",
        "-i",
        "mongodb/mongodb-mcp-server:latest"
      ]
    }
  }
}
```

With connection string:

```json
{
  "mcpServers": {
    "MongoDB": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "-e",
        "MDB_MCP_CONNECTION_STRING",
        "-e",
        "MDB_MCP_READ_ONLY=true",
        "mongodb/mongodb-mcp-server:latest"
      ],
      "env": {
        "MDB_MCP_CONNECTION_STRING": "mongodb+srv://username:password@cluster.mongodb.net/myDatabase"
      }
    }
  }
}
```

With Atlas API credentials:

```json
{
  "mcpServers": {
    "MongoDB": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "-e",
        "MDB_MCP_READ_ONLY=true",
        "-e",
        "MDB_MCP_API_CLIENT_ID",
        "-e",
        "MDB_MCP_API_CLIENT_SECRET",
        "mongodb/mongodb-mcp-server:latest"
      ],
      "env": {
        "MDB_MCP_API_CLIENT_ID": "your-atlas-service-accounts-client-id",
        "MDB_MCP_API_CLIENT_SECRET": "your-atlas-service-accounts-client-secret"
      }
    }
  }
}
```

## 🛠️ Supported Tools

### Tool List

#### MongoDB Database Tools

- `aggregate` - Run an aggregation against a MongoDB collection
- `aggregate-db` - Run an aggregation against a MongoDB database
- `collection-indexes` - Describe the indexes for a collection
- `collection-schema` - Describe the schema for a collection
- `collection-storage-size` - Gets the size of the collection
- `connect` - Connect to a MongoDB instance
- `count` - Gets the number of documents in a MongoDB collection using db.collection.count() and query as an optional filter parameter
- `create-collection` - Creates a new collection in a database. If the database doesn't exist, it will be created automatically.
- `create-index` - Create an index for a collection
- `db-stats` - Returns statistics that reflect the use state of a single database
- `delete-many` - Removes all documents that match the filter from a MongoDB collection
- `disconnect` - Close a MongoDB connection and revoke its connectionId.
- `drop-collection` - Removes a collection or view from the database. The method also removes any indexes associated with the dropped collection.
- `drop-database` - Removes the specified database, deleting the associated data files
- `drop-index` - Drop an index for the provided database and collection.
- `explain` - Returns statistics describing the execution of the winning plan chosen by the query optimizer for the evaluated method
- `export` - Export a query or aggregation results in the specified EJSON format.
- `find` - Run a find query against a MongoDB collection
- `insert-many` - Insert an array of documents into a MongoDB collection. If the list of documents is above com.mongodb/maxRequestPayloadBytes, consider inserting them in batches.
- `list-collections` - List all collections for a given database
- `list-connections` - List the active MongoDB connections and their connectionIds. Use this to find a connectionId established earlier.
- `list-databases` - List all databases for a MongoDB connection
- `mongodb-logs` - Returns the most recent logged mongod events
- `rename-collection` - Renames a collection in a MongoDB database
- `update-many` - Updates all documents that match the specified filter for a collection. If the list of documents is above com.mongodb/maxRequestPayloadBytes, consider updating them in batches.

#### MongoDB Atlas Tools

- `atlas-connect-cluster` - Connect to MongoDB Atlas cluster and get back a connectionId to pass to the other MongoDB tools. Each call establishes a new, independent connection — multiple connections can be active at the same time.
- `atlas-create-access-list` - Allow Ip/CIDR ranges to access your MongoDB Atlas clusters.
- `atlas-create-cluster` - Create a MongoDB Atlas cluster (M10–M80, replica set or single shard). Compute autoscaling is enabled by default: min instance size is set to the selected instance size, max is set two tiers above. Disk autoscaling is always enabled. Encryption at rest with customer-managed keys (CMK) is supported, the CMK provider must already have a valid encryption at rest configuration in the project. The tool returns immediately, use the atlas-inspect-cluster tool to poll the cluster state for readiness (state: IDLE). Connection strings are unavailable until the cluster reaches IDLE state.
- `atlas-create-db-user` - Create an MongoDB Atlas database user
- `atlas-create-free-cluster` - Create a free MongoDB Atlas cluster
- `atlas-create-project` - Create a MongoDB Atlas project
- `atlas-get-performance-advisor` - Get MongoDB Atlas performance advisor recommendations and suggestions, which includes the operations: suggested indexes, drop index suggestions, schema suggestions, and a sample of the most recent (max 50) slow query logs
- `atlas-get-regions` - List supported MongoDB Atlas regions for a cloud provider.
- `atlas-inspect-access-list` - Inspect Ip/CIDR ranges with access to your MongoDB Atlas clusters.
- `atlas-inspect-cluster` - Inspect metadata of a MongoDB Atlas cluster
- `atlas-list-alerts` - List triggered alerts for a MongoDB Atlas project. These are alerts Atlas has raised, not the alert configurations that define them. Defaults to OPEN alerts; set status to TRACKING or CLOSED to see others.
- `atlas-list-clusters` - List MongoDB Atlas clusters
- `atlas-list-db-users` - List MongoDB Atlas database users
- `atlas-list-orgs` - List MongoDB Atlas organizations
- `atlas-list-projects` - List MongoDB Atlas projects.
- `atlas-load-sample-dataset` - Load a MongoDB sample dataset into an Atlas cluster, or check the status of a previously-initiated load. To start a new load, provide `clusterName` — the load runs asynchronously and the response includes a `jobId` and initial state. To check progress, call this tool again with `jobId` (sample dataset loads typically take 1–5 minutes). State can be WORKING, COMPLETED, or FAILED.
- `atlas-pause-resume-cluster` - Pause or resume a dedicated (M10+) MongoDB Atlas cluster.
- `atlas-streams-build` - Create Atlas Stream Processing resources. Use this tool for 'set up a Kafka pipeline', 'create a workspace', 'add a connection', or 'deploy a processor'. Use resource='workspace' to create a new workspace (specify cloud provider, region, and tier). Use resource='connection' to add a data source or sink to an existing workspace. Use resource='processor' to deploy a stream processor with a pipeline. Use resource='privatelink' to set up private networking. Typical workflow: create workspace → add connections → deploy processor.
- `atlas-streams-discover` - Discover and inspect Atlas Stream Processing resources. Also use for 'why is my processor failing', 'what workspaces do I have', 'show processor stats', or 'check processor health'. Use 'list-workspaces' to see all workspaces in a project. Use inspect actions for details on a specific resource. Use 'diagnose-processor' for a combined health report including state, stats, connection health, and recent errors. Use 'get-networking' for PrivateLink and account details.
- `atlas-streams-manage` - Manage Atlas Stream Processing resources: start/stop processors, modify pipelines, update configurations. Also use for 'change the pipeline', 'scale up my processor', or 'update my workspace tier'. Common workflow: action='stop-processor' → action='modify-processor' → action='start-processor'. Use `atlas-streams-discover` with action 'inspect-processor' to check state before managing.
- `atlas-streams-teardown` - Delete Atlas Stream Processing resources. Also use for 'remove my workspace', 'disconnect a source', 'delete all processors', or 'clean up my streams environment'. Performs basic safety checks before deletion: summarizes counts of processors and connections, highlights connections referenced by processors where possible, and surfaces API errors if processors are still running when deletion is attempted. Use `atlas-streams-discover` to review resources before deleting.
- `atlas-upgrade-cluster` - Upgrade or scale a MongoDB Atlas cluster. Free and Flex clusters can be upgraded to Flex or M10 Dedicated. Dedicated clusters can be scaled to a different instance size, and compute autoscaling settings can be updated. When scaling a Dedicated cluster, at least one of targetTier, computeAutoScaling, minInstanceSize, or maxInstanceSize must be provided. Compute autoscaling defaults to enabled when upgrading to M10 Dedicated: min instance size is set to the selected instance size, max is set two tiers above, unless overridden. Note to LLM: If provider and region are not already known, ask for both together in a single question before calling this tool. Use atlas-get-regions to resolve natural-language locations or uncertain region codes before calling this tool.

NOTE: atlas tools are only available when you set credentials on [configuration](#configuration) section.

#### MongoDB Atlas Local Tools

- `atlas-local-connect-deployment` - Connect to a MongoDB Atlas Local deployment and get back a connectionId to pass to the other 

**Official site: ** [https://github.com/mongodb-js/mongodb-mcp-server](https://github.com/mongodb-js/mongodb-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`, `development`
- Tags: `database`, `mongodb`, `developer tools`, `official`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y mongodb-mcp-server@latest setup`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/mongodb-js-mongodb-mcp.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
