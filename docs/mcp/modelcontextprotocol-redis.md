---
title: "redis"
description: "A Model Context Protocol server that provides access to Redis databases. This server enables LLMs to interact with Redis key-value stores through a set of standardized tools."
---

# redis

A Model Context Protocol server that provides access to Redis databases. This server enables LLMs to interact with Redis key-value stores through a set of standardized tools.

# Redis

A Model Context Protocol server that provides access to Redis databases. This server enables LLMs to interact with Redis key-value stores through a set of standardized tools.

## Prerequisites

1. Redis server must be installed and running
   - [Download Redis](https://redis.io/download)
   - For Windows users: Use [Windows Subsystem for Linux (WSL)](https://redis.io/docs/getting-started/installation/install-redis-on-windows/) or [Memurai](https://www.memurai.com/) (Redis-compatible Windows server)
   - Default port: 6379

## Common Issues & Solutions

### Connection Errors

**ECONNREFUSED**
  - **Cause**: Redis server is not running or unreachable
  - **Solution**: 
    - Verify Redis is running: `redis-cli ping` should return "PONG"
    - Check Redis service status: `systemctl status redis` (Linux) or `brew services list` (macOS)
    - Ensure correct port (default 6379) is not blocked by firewall
    - Verify Redis URL format: `redis://hostname:port`

### Server Behavior

- The server implements exponential backoff with a maximum of 5 retries
- Initial retry delay: 1 second, maximum delay: 30 seconds
- Server will exit after max retries to prevent infinite reconnection loops

## Components

### Tools

- **set**
  - Set a Redis key-value pair with optional expiration
  - Input:
    - `key` (string): Redis key
    - `value` (string): Value to store
    - `expireSeconds` (number, optional): Expiration time in seconds

- **get**
  - Get value by key from Redis
  - Input: `key` (string): Redis key to retrieve

- **delete**
  - Delete one or more keys from Redis
  - Input: `key` (string | string[]): Key or array of keys to delete

- **list**
  - List Redis keys matching a pattern
  - Input: `pattern` (string, optional): Pattern to match keys (default: *)

## Usage with Claude Desktop

To use this server with the Claude Desktop app, add the following configuration to the "mcpServers" section of your `claude_desktop_config.json`:

### Docker

* when running docker on macos, use host.docker.internal if the server is running on the host network (eg localhost)
* Redis URL can be specified as an argument, defaults to "redis://localhost:6379"

```json
{
  "mcpServers": {
    "redis": {
      "command": "docker",
      "args": [
        "run", 
        "-i", 
        "--rm", 
        "mcp/redis", 
        "redis://host.docker.internal:6379"]
    }
  }
}
```

### NPX

```json
{
  "mcpServers": {
    "redis": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-redis",
        "redis://localhost:6379"
      ]
    }
  }
}
```

## Building

Docker:

```sh
docker build -t mcp/redis -f src/redis/Dockerfile . 
```

## License

This MCP server is licensed under the MIT License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the MIT License. For more details, please see the LICENSE file in the project repository.

**Official site: ** [https://github.com/modelcontextprotocol/servers/tree/main/src/redis](https://github.com/modelcontextprotocol/servers/tree/main/src/redis)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `developer tools`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @modelcontextprotocol/server-redis REDIS_URL`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/modelcontextprotocol-redis.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
