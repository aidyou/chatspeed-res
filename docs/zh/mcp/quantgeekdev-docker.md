---
title: "Docker MCP工具"
description: "一个强大的模型上下文协议（MCP）服务器，用于Docker操作，通过Claude AI实现容器和组合堆栈的无缝管理。"
---

# Docker MCP工具

一个强大的模型上下文协议（MCP）服务器，用于Docker操作，通过Claude AI实现容器和组合堆栈的无缝管理。

# 🐳 docker-mcp

[![Python 3.12](/mcp-assets/e1a2b83f0b6cdff8bd20352d9134afb6.svg)](https://www.python.org/downloads/release/python-3120/)
[![License: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](/mcp-assets/c41a882f152367575bf9d86c0b2ec68e.svg)](https://github.com/psf/black)
[Smithery](https://smithery.ai/protocol/docker-mcp)

一个强大的用于 Docker 操作的 Model Context Protocol (MCP) 服务器，通过 Claude AI 实现无缝容器和 compose 堆栈管理。

## ✨ 特性

- 🚀 容器创建和实例化
- 📦 Docker Compose 堆栈部署
- 🔍 容器日志检索
- 📊 容器列表和状态监控

### 🎬 演示
#### 部署 Docker Compose 堆栈

[https://github.com/user-attachments/assets/b5f6e40a-542b-4a39-ba12-7fdf803ee278](https://github.com/user-attachments/assets/b5f6e40a-542b-4a39-ba12-7fdf803ee278)

#### 分析容器日志

[https://github.com/user-attachments/assets/da386eea-2fab-4835-82ae-896de955d934](https://github.com/user-attachments/assets/da386eea-2fab-4835-82ae-896de955d934)

## 🚀 快速开始

要在 Claude Desktop 应用程序中尝试此功能，请将以下内容添加到您的 claude 配置文件中：
```json
{
  "mcpServers": {
    "docker-mcp": {
      "command": "uvx",
      "args": [
        "docker-mcp"
      ]
    }
  }
}
```

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/protocol/docker-mcp) 自动为 Claude Desktop 安装 Docker MCP：

```bash
npx @smithery/cli install docker-mcp --client claude
```

### 先决条件

- UV（包管理器）
- Python 3.12+
- Docker Desktop 或 Docker Engine
- Claude Desktop

### 安装

#### Claude Desktop 配置

将服务器配置添加到您的 Claude Desktop 配置文件中：

**MacOS**: `~/Library/Application\ Support/Claude/claude_desktop_config.json`  
**Windows**: `%APPDATA%/Claude/claude_desktop_config.json`

  💻 开发配置

```json
{
  "mcpServers": {
    "docker-mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "
",
        "run",
        "docker-mcp"
      ]
    }
  }
}
```

  🚀 生产配置

```json
{
  "mcpServers": {
    "docker-mcp": {
      "command": "uvx",
      "args": [
        "docker-mcp"
      ]
    }
  }
}
```

## 🛠️ 开发

### 本地设置

1. 克隆仓库：
```bash
git clone https://github.com/QuantGeekDev/docker-mcp.git
cd docker-mcp
```

2. 创建并激活虚拟环境：
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. 安装依赖项：
```bash
uv sync
```

### 🔍 调试

启动 MCP Inspector 进行调试：

```bash
npx @modelcontextprotocol/inspector uv --directory 
 run docker-mcp
```

Inspector 将提供一个 URL 以访问调试界面。

## 📝 可用工具

服务器提供以下工具：

### create-container
创建一个独立的 Docker 容器
```json
{
    "image": "image-name",
    "name": "container-name",
    "ports": {"80": "80"},
    "environment": {"ENV_VAR": "value"}
}
```

### deploy-compose
部署 Docker Compose 堆栈
```json
{
    "project_name": "example-stack",
    "compose_yaml": "version: '3.8'\nservices:\n  service1:\n    image: image1:latest\n    ports:\n      - '8080:80'"
}
```

### get-logs
从特定容器检索日志
```json
{
    "container_name": "my-container"
}
```

### list-containers
列出所有 Docker 容器
```json
{}
```

## 🚧 当前限制

- 不支持内置环境变量
- 无卷管理
- 无网络管理
- 无容器健康检查
- 无容器重启策略
- 无容器资源限制

## 🤝 贡献

1. 从 [docker-mcp](https://github.com/QuantGeekDev/docker-mcp) 仓库分叉
2. 创建你的特性分支
3. 提交你的更改
4. 推送到分支
5. 打开 Pull Request

## 📜 许可证

该项目根据 MIT 许可证许可 - 有关详细信息，请参阅 [LICENSE](https://github.com/QuantGeekDev/docker-mcp/blob/HEAD/LICENSE) 文件。

## ✨ 作者

- **Alex Andru** - *初始工作 | 核心贡献者* - [@QuantGeekDev](https://github.com/QuantGeekDev)
- **Ali Sadykov** - *初始工作 | 核心贡献者* - [@md-archive](https://github.com/md-archive)

---
Made with ❤️

**官方网站：** [https://github.com/QuantGeekDev/docker-mcp](https://github.com/QuantGeekDev/docker-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`virtualization`, `developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`docker-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/quantgeekdev-docker.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
