---
title: "auto_video_mcp"
description: "Digital Human and Multimedia Creation MCP server. Available tools: Avatar Tools (create personal digital human from photo or video), Voice Tools (clone voice from file or create from text), Video Crea…"
---

# auto_video_mcp

Digital Human and Multimedia Creation MCP server. Available tools: Avatar Tools (create personal digital human from photo or video), Voice Tools (clone voice from file or create from text), Video Crea…

## 🛠️ Available Tools

The server provides the following tools, which can be directly invoked by LLMs or other clients:

### Digital Human and Multimedia Creation Tools
- **Avatar Tools (`avatar_tools`)**:
  - `create_personal_avatar_by_photo`: Create a personal digital human from a single photo.
  - `create_personal_avatar_by_video`: Create a personal digital human from a video file.
- **Voice Tools (`voice_tools`)**:
  - `create_voice_by_file`: Clone a voice from an audio file.
  - `create_voice_by_text`: Create a voice from text (for voice customization).
- **Video Creation Tools (`video_tools`)**:
  - `create_video_by_audio`: Create a video using a specified digital human and audio file.
  - `create_video_by_script`: Create a video using a specified digital human and text script.
- **Audio Creation Tools (`audio_tools`)**:
  - `create_audio_by_text`: Convert text to speech.
- **File Upload Tools (`upload_tools`)**:
  - `upload_file`: Upload media files (audio, video) to the server.

### Web and Content Tools (`web_tools`)
- `get_baidu_trending`: Get Baidu trending topics.
- `get_36kr_news`: Get the latest news from 36Kr.
- `get_autohome_news`: Get the latest news from Autohome.
- `get_custom_rss`: Fetch content from a specified RSS feed.
- `crawl_website`: Crawl structured content from a specified webpage.
- `web_search`: Perform a web search.

### Query Tools (`query_tools`)
- `query_task_status`: Query the current status and result of a specified task.
- `query_personal_avatars`: Query the list of created personal digital humans.
- `query_personal_voices`: Query the list of created personal voices.
- `query_public_avatars`: Query the list of public digital humans.
- `query_public_voices`: Query the list of public voices.
- `query_video_templates`: Query available video templates.

#### Command Line Tools

After installation, you can use the `auto_video_mcp` command line tool to start the server:

```bash

# Activate the virtual environment

source .venv/bin/activate

# HTTP mode (default port 8000)

python -m auto_video_mcp.server --transport http

# Custom host and port

python -m auto_video_mcp.server --transport http --host 0.0.0.0 --port 8080 

# SSE mode

python -m auto_video_mcp.server --transport sse

# STDIO mode (for MCP integration)

python -m auto_video_mcp.server --transport stdio

```
Or use the installed command line tool:

```bash

# HTTP mode (default port 8000)

auto_video_mcp --transport http

# Custom host and port

auto_video_mcp --transport http --host 0.0.0.0 --port 8080 

# SSE mode

auto_video_mcp --transport sse

# STDIO mode (for MCP integration)

auto_video_mcp --transport stdio

```
#### Configuration Methods

Server configuration items (such as host, port, etc.) can be set in three ways, with priorities from high to low:

1.  **Command Line Arguments**: Pass arguments directly at startup, with the highest priority.
2.  **Configuration File**: Specify a JSON configuration file via the `--config` parameter.
3.  **Environment Variables**: Load from a `.env` file, typically used for storing sensitive information such as API Tokens.

#### Transport Protocols (Transport)

FastMCP supports multiple transport protocols, which you can choose through different subcommands:

-   **`http` (default)**: Start a Web server based on Streamable HTTP. This is the recommended way for Web service deployment.
```bash
    # Use the default config (http://127.0.0.1:8000)
    python -m auto_video_mcp.server --transport http

    # Custom host and port
    python -m auto_video_mcp.server --transport http --host 0.0.0.0 --port 8080
```
-   **`sse`**: Start a server based on Server-Sent Events (SSE). This is an older protocol, and new projects are recommended to use `http`.
```bash
    python -m auto_video_mcp.server --transport sse
```
-   **`stdio`**: Start a server based on standard input/output. This is mainly used for integration with MCP clients.
```bash
    python -m auto_video_mcp.server --transport stdio
```
#### Command Line Parameters

You can use the following parameters to configure the operation of the server:

-   `--transport `: Transport protocol type, options are `http`, `sse`, `stdio`.
-   `--host 
`: The host address the server listens on (default is `127.0.0.1`).
-   `--port `: The port the server listens on (default is `8000`).
-   `--path `: URL path under HTTP mode (default is `/mcp/`).
-   `--log-level `: Set the log level (`debug`, `info`, `warning`, `error`, `critical`).
-   `--config `: Specify the path to the configuration file.

#### Client Connection Configuration

##### Cursor IDE Integration

Cursor IDE supports integration with Feiying Digital Human servers via the MCP protocol. There are two main ways to connect:

**Method One: Through `stdio` (Standard Input/Output)**

This is the most direct way of integration, where Cursor will automatically start and stop the MCP server process as needed.

1.  Edit Cursor's MCP configuration file (`~/.cursor/mcp.json`):

```json

    {

      "mcpServers": {

        "auto_video_mcp": {

          "command": "uvx",

          "args": ["auto_video_mcp", "--transport", "stdio"],

          "env": {

            "FLYWORKS_API_TOKEN": "YOUR_API_TOKEN"

          }

        }

      }

    }

```
2.  Ensure that `auto_video_mcp` is installed in your Python environment.

3.  In Cursor, select "auto_video_mcp" as the MCP server.

**Method Two: Through `http` Connection**If you have manually started the MCP server (for example, running locally or in Docker), you can connect to it via HTTP.

1. First, make sure the server is running. For example:

```bash

    python -m auto_video_mcp.server --transport http --host 127.0.0.1 --port 8000

```
2. Edit the Cursor's MCP configuration file (`~/.cursor/mcp.json`), and add the following configuration:

```json

    {

      "mcpServers": {

        "auto_video_mcp_http": {

          "transport": "http",

          "url": "http://127.0.0.1:8000/mcp/"

        }

      }

    }

```
> **Note**:
> - The path in `url` (`/mcp/`) needs to match the `SERVER_PATH` environment variable configured on the server.
> - If the server is running on a different host or port, modify the `url` accordingly.

3. In Cursor, select "auto_video_mcp_http" as the MCP server.

##### Remote Connection (HTTP)

If you need to deploy the service as a web service, you can use an HTTP connection.

1. **Start the Server**:

```bash

    python -m auto_video_mcp.server --transport http --host 0.0.0.0 --port 8000

```
2. **Configure the Client**:
   In the client's configuration file, add an entry pointing to your server URL.

```json

    {

      "mcpServers": {

        "auto_video_mcp-remote": {

          "transport": "http",

          "url": "http://your-server-ip:8000/mcp/"

        }

      }

    }

```
> **Note**: Replace `your-server-ip` with the actual IP address or domain name of the machine running the server.

After completing the configuration and restarting the client, you will be able to connect to the Feiying Digital Human MCP server.

**Official site: ** [https://github.com/fancyboi999/auto_video_mcp](https://github.com/fancyboi999/auto_video_mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `entertainment and media`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `auto_video_mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/fancyboi999-auto-video.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
