---
title: "mcp-ip-geo"
description: "mcp-ip-geo"
---

# mcp-ip-geo

mcp-ip-geo

📝 mcp-ip-geo

  English | 
简体中文

---

`mcp-ip-geo` is an `MCP` (`Model Context Protocol`) server that provides IP geolocation lookup services (country, region, city, etc.) using the ip-api.com service.

# 🔌 MCP Integration

You can integrate the `mcp-ip-geo` service in two ways:

## Method 1: Using the go run command (Stdio)

Add the following to your `MCP` configuration to run the latest version directly from GitHub:

```json
{
  "mcpServers": {
    "mcp-ip-geo": {
      "command": "go",
      "args": [
        "run",
        "github.com/chenmingyong0423/mcp-ip-geo/cmd/mcp-ip-geo@latest"
      ]
    }
  }
}
```

## Method 2: Using Docker (Streamable HTTP)

### 🐳 Docker Deployment

#### Step 1: Clone the repository

```bash
git clone https://github.com/chenmingyong0423/mcp-ip-geo.git
cd mcp-ip-geo
```

#### Step 2: Build the Docker image

```bash
docker build -t mcp-ip-geo-server .
```

#### Step 3: Run the container

```bash
docker run -d --name mcp-ip-geo-server -p 8000:8000 mcp-ip-geo-server
```

Once running successfully, the service will listen on `0.0.0.0:8000` within the container (listening on all network interfaces), and can be accessed via `http://:8000/mcp`, where `` can be:
- Local development environment: Use `localhost` or `127.0.0.1`
- LAN environment: Use the server's internal IP address (e.g., `192.168.x.x`)
- Public network environment: Use the server's public IP address or domain name

> Note: The service is configured to listen on the `0.0.0.0` address inside the container, which is standard practice for containerized applications, ensuring the service can be accessed from outside the container.

#### Step 4: Configure MCP

Add the following to your `MCP` configuration:

```json
{
  "mcpServers": {
    "mcp-ip-geo": {
      "url": "http://:8000/mcp"
    }
  }
}
```

Replace `` with the actual server IP address or domain name of your deployment environment.

# ⚠️ License Notice

> Note: This project uses the free version of ip-api.com, which is **for non-commercial use only**. If you intend to use this project for commercial purposes, please comply with their terms of service or purchase the paid version: https://ip-api.com/

**Official site: ** [https://github.com/chenmingyong0423/mcp-ip-geo](https://github.com/chenmingyong0423/mcp-ip-geo)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `location services`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `go`
- Args: `run github.com/chenmingyong0423/mcp-ip-geo/cmd/mcp-ip-geo@latest`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/chenmingyong0423-ip-geo.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
