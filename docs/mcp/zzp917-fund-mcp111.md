---
title: "基金知识库"
description: "基于Model Context Protocol (MCP)的基金知识库服务器，提供基金相关知识的查询和检索功能。支持多种部署模式，包括标准MCP协议、HTTP REST API和Server-Sent Events (SSE)。"
---

# 基金知识库

基于Model Context Protocol (MCP)的基金知识库服务器，提供基金相关知识的查询和检索功能。支持多种部署模式，包括标准MCP协议、HTTP REST API和Server-Sent Events (SSE)。

# Fund MCP Server

一个基于 Model Context Protocol (MCP) 的基金知识库服务器，提供基金相关知识的查询和检索功能。

## 服务介绍

Fund MCP Server 是一个专门为基金投资领域设计的 MCP 服务器，通过集成外部知识库 API，为用户提供基金知识查询服务。该服务器支持多种部署模式，包括标准 MCP 协议、HTTP REST API 和 Server-Sent Events (SSE) 模式。

### 主要功能

- **基金知识查询**: 通过关键词搜索基金相关知识库
- **多协议支持**: 支持 MCP 标准协议、HTTP REST API 和 SSE
- **灵活部署**: 支持本地部署、Docker 部署和生产环境部署
- **跨平台**: 支持 Windows、Linux 和 macOS

### 技术特性

- 基于 TypeScript 开发，类型安全
- 使用 Zod 进行参数验证
- 支持环境变量配置
- 提供健康检查和监控接口

## 服务配置

### MCP sever configuration

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

### HTTP REST API 配置

启动 HTTP 模式服务：

```bash
npm run start:http
```

服务将在 `http://localhost:3000` 启动，提供以下 API 端点：

- `GET /api/health` - 健康检查
- `GET /api/tools` - 获取可用工具列表
- `POST /api/tools/call` - 调用工具

### SSE 模式配置

启动 SSE 模式服务：

```bash
npm run start:sse
```

SSE 端点：`http://localhost:3000/sse`

## 环境变量配置

### 必需环境变量

创建 `llm-config.env` 文件或设置以下环境变量：

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

### 环境变量说明

| 变量名            | 默认值                                                           | 说明                |
| ----------------- | ---------------------------------------------------------------- | ------------------- |
| `FUND_KB_API_URL` | `https://report.haiyu.datavita.com.cn/api/admin/knowledge/query` | 基金知识库 API 地址 |
| `PORT`            | `3000`                                                           | 服务监听端口        |
| `NODE_ENV`        | `development`                                                    | 运行环境            |
| `MCP_TRANSPORT`   | `stdio`                                                          | MCP 传输模式        |

## 快速开始

### 🚀 一键部署

#### Windows 用户

```cmd
# 双击运行或在命令行执行
deploy.bat
```

#### Linux/macOS 用户

```bash
# 给脚本执行权限并运行
chmod +x deploy.sh
./deploy.sh
```

### 📦 手动部署

1. **安装依赖**

```bash
   npm install
```
2. **构建项目**

```bash
   npm run build
```
3. **启动服务**

```bash
   # HTTP 模式
   npm run start:http

   # SSE 模式
   npm run start:sse

   # 标准 MCP 模式
   npm start
```

## 部署选项

### 1. 快速部署 (开发环境)

- **Windows**: `deploy.bat` 或 `scripts\deploy.bat`
- **Linux/macOS**: `./deploy.sh` 或 `./scripts/deploy.sh`

### 2. 生产环境部署

- **Linux**: `./scripts/deploy-production.sh deploy`
- **systemd 服务**: 参考 `scripts/DEPLOYMENT.md`

### 3. Docker 部署

```bash
cd scripts
docker-compose up -d
```

### 4. 查看详细部署说明

- 查看 `scripts/README.md` 获取脚本说明
- 查看 `scripts/DEPLOYMENT.md` 获取详细部署指南

## 项目结构

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

## 端口配置

默认端口：3000

- 环境变量：`PORT=8080`
- 命令行：`--port 8080`

## 开发

### 安装依赖

```bash
npm install
```

### 开发模式

```bash
npm run watch
```

### 构建

```bash
npm run build
```

### 测试

```bash
npm test
```

## 服务管理

### 生产环境

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

## 故障排除

### 常见问题

1. **端口被占用**

```bash
   lsof -i :3000
   kill -9 

```
2. **权限问题**

```bash
   chmod +x scripts/*.sh
```
3. **依赖问题**

```bash
   npm cache clean --force
   rm -rf node_modules package-lock.json
   npm install
```

### 日志位置

- 应用日志：`logs/fund-mcp-server.log`
- 错误日志：`logs/fund-mcp-server-error.log`

## 贡献

1. Fork 项目
2. 创建功能分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

## 许可证

Apache-2.0

## 支持

- 📖 部署文档：`scripts/DEPLOYMENT.md`
- 🐛 问题反馈：GitHub Issues
- 💬 讨论：GitHub Discussions

**官方网站：** [https://github.com/zhenzp/fund-mcp-server](https://github.com/zhenzp/fund-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`finance`
- 标签：`finance`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y fund-mcp-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/zzp917-fund-mcp111.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
