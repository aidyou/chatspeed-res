---
title: "fund-mcp111"
description: "一个基于 Model Context Protocol (MCP) 的基金知识库服务器，提供基金相关知识的查询和检索功能。 Fund MCP Server 是一个专门为基金投资领域设计的 MCP 服务器，通过集成外部知识库 API，为用户提供基金知识查询服务。该服务器支持多种部署模式，包括标准 MCP 协议、HTTP REST API 和 Server-Sent Events (SSE) 模式。…"
---

# fund-mcp111

一个基于 Model Context Protocol (MCP) 的基金知识库服务器，提供基金相关知识的查询和检索功能。 Fund MCP Server 是一个专门为基金投资领域设计的 MCP 服务器，通过集成外部知识库 API，为用户提供基金知识查询服务。该服务器支持多种部署模式，包括标准 MCP 协议、HTTP REST API 和 Server-Sent Events (SSE) 模式。…

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

# 知识库 API 配置

FUND_KB_API_URL=https://report.haiyu.datavita.com.cn/api/admin/knowledge/query

# 服务端口配置

PORT=3000

# 运行环境

NODE_ENV=production

# MCP 传输模式 (可选: sse, http)

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

# 双击运行或在命令行执行

deploy.bat

```
#### For Linux/macOS Users

```bash

# 给脚本执行权限并运行

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

   # HTTP 模式

   npm run start:http

   # SSE 模式

   npm run start:sse

   # 标准 MCP 模式

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

├── deploy.bat                    # Windows 部署入口

├── deploy.sh                     # Linux/macOS 部署入口

├── scripts/                      # 部署脚本文件夹

│   ├── README.md                # 脚本说明

│   ├── DEPLOYMENT.md            # 详细部署指南

│   ├── deploy.sh                # Linux 快速部署

│   ├── deploy.bat               # Windows 快速部署

│   ├── deploy-production.sh     # 生产环境部署

│   ├── fund-mcp-server.service  # systemd 服务配置

│   ├── Dockerfile               # Docker 镜像

│   └── docker-compose.yml       # Docker Compose

├── tool-registry/               # 工具注册表

├── tool-handlers/               # 工具处理器

├── common/                      # 公共模块

├── dist/                        # 构建输出

└── package.json                 # 项目配置

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

# 查看状态

./scripts/deploy-production.sh status

# 查看日志

./scripts/deploy-production.sh logs

# 重启服务

./scripts/deploy-production.sh restart

```
### Docker

```bash

# 查看状态

docker-compose ps

# 查看日志

docker-compose logs -f

# 重启服务

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
