---
title: "wechat_send_mcp_serve"
description: "wechatsend MCP 服务 一个通过企业微信机器人 Webhook 接口发送文件到微信群的 MCP (Model Context Protocol) 服务。 功能特性 - 🚀 支持多种文件输入方式：本地文件、网络文件、Base64 编码文件 - 🔧 基于 MCP 协议，可集成到各种 AI 助手和自动化工具中 - 📱 专为企业微信群聊设计，支持文件分享 - 🛡️ 完善的错误处理和临时文件管理…"
---

# wechat_send_mcp_serve

wechatsend MCP 服务 一个通过企业微信机器人 Webhook 接口发送文件到微信群的 MCP (Model Context Protocol) 服务。 功能特性 - 🚀 支持多种文件输入方式：本地文件、网络文件、Base64 编码文件 - 🔧 基于 MCP 协议，可集成到各种 AI 助手和自动化工具中 - 📱 专为企业微信群聊设计，支持文件分享 - 🛡️ 完善的错误处理和临时文件管理…

# wechat_send MCP 服务

一个通过企业微信机器人 Webhook 接口发送文件到微信群的 MCP (Model Context Protocol) 服务。

## 功能特性

- 🚀 支持多种文件输入方式：本地文件、网络文件、Base64 编码文件
- 🔧 基于 MCP 协议，可集成到各种 AI 助手和自动化工具中
- 📱 专为企业微信群聊设计，支持文件分享
- 🛡️ 完善的错误处理和临时文件管理

## 安装依赖

```bash
pip install -r requirements.txt
```

## 启动方式

### 1. 作为独立 MCP Server 通过 stdio 启动：
```bash
python server.py
```

### 2. 作为 HTTP 服务启动（适用于 Dify 等平台）：
```bash
python server.py --http 8000
```

## 工具说明

### send_file 工具

通过企业微信机器人发送文件到群聊。

**参数说明：**
- `webhook_url` (必需): 企业微信机器人 Webhook 地址
- `file_path` (可选): 本地文件路径
- `file_url` (可选): 通过 HTTP(S) 下载的文件 URL  
- `file_base64` (可选): 文件内容的 Base64 编码

**使用方式：**
三种文件输入方式三选一：
- 直接传 `file_path` - 指定本地文件路径
- 传 `file_url` - 自动下载网络文件到临时目录
- 传 `file_base64` - 将 Base64 编码的文件内容解码为临时文件

## 配置说明

### 企业微信机器人配置

1. 在企业微信群中添加机器人
2. 获取 Webhook 地址，格式如：`https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=YOUR_KEY`
3. 将 Webhook 地址作为 `webhook_url` 参数传入

### 环境变量

- `WEBHOOK_URL`: 默认的企业微信机器人 Webhook 地址（可选）

## 使用示例

### MCP 客户端调用示例

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "send_file",
    "arguments": {
      "webhook_url": "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=YOUR_KEY",
      "file_url": "https://example.com/file.pdf"
    }
  }
}
```

### HTTP API 调用示例

```bash
curl -X POST https://your-server.com/ \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/call",
    "params": {
      "name": "send_file",
      "arguments": {
        "webhook_url": "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=YOUR_KEY",
        "file_path": "/path/to/your/file.pdf"
      }
    }
  }'
```

## 技术架构

- **核心模块**: `main.py` - 包含文件发送的核心逻辑
- **MCP 服务**: `server.py` - 基于 FastMCP 框架的 MCP 服务器
- **配置管理**: `mcp.json` - 服务配置和元数据
- **依赖管理**: `requirements.txt` - Python 包依赖

## 部署说明

### 本地部署
```bash
git clone 
cd wechat_send
pip install -r requirements.txt
python server.py
```

### 云平台部署
- 支持 Railway、Heroku、Docker 等平台
- 确保安装 Python 3.8+ 和所需依赖
- 设置必要的环境变量

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request 来改进这个项目。

**Official site: ** [https://github.com/NANYAN-01/wechat-send-mcp](https://github.com/NANYAN-01/wechat-send-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `communication`
- Tags: `communication`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx wechat-send`
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/nanyan001-wechat-send-serve.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
