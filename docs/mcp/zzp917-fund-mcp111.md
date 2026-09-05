---
title: "fund-mcp111"
description: "A fund knowledge base server based on the Model Context Protocol (MCP), providing query and retrieval functions for fund-related knowledge. Fund MCP Server is an MCP server specifically designed for t…"
---

# fund-mcp111

A fund knowledge base server based on the Model Context Protocol (MCP), providing query and retrieval functions for fund-related knowledge. Fund MCP Server is an MCP server specifically designed for t…

# Fund MCP Server

A fund knowledge base server based on the Model Context Protocol (MCP), providing query and retrieval functions for fund-related knowledge.

## Service Introduction

Fund MCP Server is an MCP server specifically designed for the fund investment field, offering users fund knowledge query services by integrating with external knowledge base APIs. This server supports multiple deployment modes, including standard MCP protocol, HTTP REST API, and Server-Sent Events (SSE) mode.

### Main Features

- **Fund Knowledge Query**: Search the fund-related knowledge base via keywords
- **Multi-Protocol Support**: Supports MCP standard protocol, HTTP REST API, and SSE
- **Flexible Deployment**: Supports local deployment, Docker deployment, and production environment deployment
- **Cross-Platform**: Supports Windows, Linux, and macOS

### Technical Features

- Developed in TypeScript, type-safe
- Uses Zod for parameter validation
- Supports environment variable configuration
- Provides health check and monitoring interfaces

## Service Configuration

### MCP Server Configuration

```json

{

    "mcpServers": {

        "fund-mcp-server": {

            "command": "npx",

            "args": [

                "-y",

                "fund-mcp-server"

            ]

        }

    }

}

```
### HTTP REST API Configuration

Start the HTTP mode service:

```bash

npm run start:http

```
The service will start at `http://localhost:3000` and provide the following API endpoints:

- `GET /api/health` - Health check
- `GET /api/tools` - Get the list of available tools
- `POST /api/tools/call` - Call a tool

### SSE Mode Configuration

Start the SSE mode service:

```bash

npm run start:sse

```
SSE endpoint: `http://localhost:3000/sse`

## Environment Variable Configuration

### Required Environment Variables

Create a `llm-config.env` file or set the following environment variables:

```env

# Knowledge base API configuration

FUND_KB_API_URL=https://report.haiyu.datavita.com.cn/api/admin/knowledge/query

# Service port configuration

PORT=3000

# Runtime environment

NODE_ENV=production

# MCP transport mode (optional: sse, http)

MCP_TRANSPORT=http

```
### Environment Variable Description

| Variable Name            | Default Value                                                           | Description                |
| ------------------------ | ----------------------------------------------------------------------- | -------------------------- |
| `FUND_KB_API_URL`        | `https://report.haiyu.datavita.com.cn/api/admin/knowledge/query`        | Fund knowledge base API URL|
| `PORT`                   | `3000`                                                                  | Service listening port     |
| `NODE_ENV`               | `development`                                                           | Running environment        |
| `MCP_TRANSPORT`          | `stdio`                                                                 | MCP transport mode         |

## Quick Start

### 🚀 One-Click Deployment

#### For Windows Users

```cmd

# Double-click to run, or execute in the command line

deploy.bat

```
#### For Linux/macOS Users

```bash

# Give the script execute permission and run it

chmod +x deploy.sh

./deploy.sh

```
### 📦 Manual Deployment

1. **Install Dependencies**

```bash

   npm install

```
2. **Build the Project**

```bash

   npm run build

```
3. **Start the Service**

```bash

   # HTTP mode

   npm run start:http

   # SSE mode

   npm run start:sse

   # Standard MCP mode

   npm start

```
## Deployment Options

### 1. Quick Deployment (Development Environment)

- **Windows**: `deploy.bat` or `scripts\deploy.bat`
- **Linux/macOS**: `./deploy.sh` or `./scripts/deploy.sh`

### 2. Production Environment Deployment

- **Linux**: `./scripts/deploy-production.sh deploy`
- **systemd Service**: Refer to `scripts/DEPLOYMENT.md`

### 3. Docker Deployment

```bash

cd scripts

docker-compose up -d

```
### 4. View Detailed Deployment Instructions

- Check `scripts/README.md` for script instructions
- Check `scripts/DEPLOYMENT.md` for detailed deployment guidelines

## Project Structure

```

fund-mcp-server/

├── deploy.bat                    # Windows deployment entry

├── deploy.sh                     # Linux/macOS deployment entry

├── scripts/                      # Deployment scripts folder

│   ├── README.md                # Script documentation

│   ├── DEPLOYMENT.md            # Detailed deployment guide

│   ├── deploy.sh                # Linux quick deployment

│   ├── deploy.bat               # Windows quick deployment

│   ├── deploy-production.sh     # Production environment deployment

│   ├── fund-mcp-server.service  # systemd service configuration

│   ├── Dockerfile               # Docker image

│   └── docker-compose.yml       # Docker Compose

├── tool-registry/               # Tool registry

├── tool-handlers/               # Tool handlers

├── common/                      # Common modules

├── dist/                        # Build output

└── package.json                 # Project configuration

```
## Port Configuration

Default Port: 3000

- Environment Variable: `PORT=8080`
- Command Line: `--port 8080`

## Development

### Install Dependencies

```bash

npm install

```
### Development Mode

```bash

npm run watch

```
### Build

```bash

npm run build

```
### Test

```bash

npm test

```
## Service Management

### Production Environment

```bash

# Check status

./scripts/deploy-production.sh status

# Check logs

./scripts/deploy-production.sh logs

# Restart the service

./scripts/deploy-production.sh restart

```
### Docker

```bash

# Check status

docker-compose ps

# Check logs

docker-compose logs -f

# Restart the service

docker-compose restart

```
## Troubleshooting

### Common Issues

1. **Port Occupied**

```bash

   lsof -i :3000

   kill -9 

```
2. **Permission Issues**

```bash

   chmod +x scripts/*.sh

```
3. **Dependency Issues**

```bash

   npm cache clean --force

   rm -rf node_modules package-lock.json

   npm install

```
### Log Locations

- Application Logs: `logs/fund-mcp-server.log`
- Error Logs: `logs/fund-mcp-server-error.log`

## Contribution

1. Fork the project
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

Apache-2.0

## Support

- 📖 Deployment Documentation: `scripts/DEPLOYMENT.md`
- 🐛 Issue Reporting: GitHub Issues
- 💬 Discussions: GitHub Discussions

**Official site: ** [https://github.com/zhenzp/fund-mcp-server](https://github.com/zhenzp/fund-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `finance`
- Tags: `finance`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y fund-mcp-server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/zzp917-fund-mcp111.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
