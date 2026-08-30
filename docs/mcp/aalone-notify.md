---
title: "MCP通知服务器 - 微信/Telegram"
description: "💬 Notify MCP Server 提供消息推送的 MCP (Model Context Protocol) 服务器，支持企业微信、钉钉、Telegram、Bark、Lark、飞书、Home Assistant 安装 方式1: uvx yaml { \"mcpServers\": { \"mcp-notify\": { \"command\": \"uvx\", \"args\": [\"mcp-notify\"], \"env\": { \"WEWORKBOTKEY\": \"your-wework-bot-key\" } } } } 方式2:"
---

# MCP通知服务器 - 微信/Telegram

💬 Notify MCP Server 提供消息推送的 MCP (Model Context Protocol) 服务器，支持企业微信、钉钉、Telegram、Bark、Lark、飞书、Home Assistant 安装 方式1: uvx yaml { "mcpServers": { "mcp-notify": { "command": "uvx", "args": ["mcp-notify"], "env": { "WEWORKBOTKEY": "your-wework-bot-key" } } } } 方式2:

# 💬 Notify MCP Server

提供消息推送的 MCP (Model Context Protocol) 服务器，支持企业微信、钉钉、Telegram、Bark、Lark、飞书、Home Assistant

## 安装

### 方式1: uvx
```yaml
{
  "mcpServers": {
    "mcp-notify": {
      "command": "uvx",
      "args": ["mcp-notify"],
      "env": {
        "WEWORK_BOT_KEY": "your-wework-bot-key"
      }
    }
  }
}
```

### 方式2: [Smithery](https://smithery.ai/server/@aahl/mcp-notify)
> 需要通过OAuth授权或Smithery key

```yaml
{
  "mcpServers": {
    "mcp-aktools": {
      "url": "https://server.smithery.ai/@aahl/mcp-notify/mcp" # Streamable HTTP
    }
  }
}
```

### 方式3: Docker
```bash
mkdir /opt/mcp-notify
cd /opt/mcp-notify
wget https://raw.githubusercontent.com/aahl/mcp-notify/refs/heads/main/docker-compose.yml
docker-compose up -d
```
```yaml
{
  "mcpServers": {
    "mcp-notify": {
      "url": "http://0.0.0.0:8809/mcp" # Streamable HTTP
    }
  }
}
```

### 环境变量

#### 企业微信群机器人
- `WEWORK_BOT_KEY`: 企业微信群机器人默认key，也可以在提示词指定

#### 企业微信应用号
- `WEWORK_APP_CORPID`: 企业微信所属的企业ID
- `WEWORK_APP_SECRET`: 企业微信应用的凭证密钥
- `WEWORK_APP_AGENTID`: 企业微信应用的ID，默认: `1000002`
- `WEWORK_APP_TOUSER`: 企业微信默认接收人ID，也可以在提示词指定，默认: `@all`
- `WEWORK_BASE_URL`: 企业微信API反代理地址，用于可信IP，默认: `https://qyapi.weixin.qq.com`

#### 钉钉群机器人
- `DINGTALK_BOT_KEY`: 钉钉群机器人access_token
- `DINGTALK_BASE_URL`: 钉钉API地址，默认: `https://oapi.dingtalk.com`

#### 飞书/Lark群机器人
- `FEISHU_BOT_KEY`: 飞书群机器人key，也可以在提示词指定
- `FEISHU_BASE_URL`: 飞书API地址，默认: `https://open.feishu.cn`
- `LARK_BOT_KEY`: Lark群机器人key，也可以在提示词指定
- `LARK_BASE_URL`: Lark API地址，默认: `https://open.larksuite.com`

#### Bark
- `BARK_DEVICE_KEY`: Bark device key, Can also be specified in the prompt
- `BARK_BASE_URL`: Bark Base URL, Default: `https://api.day.app`

#### Telegram
- `TELEGRAM_DEFAULT_CHAT`: Telegram Default Chat ID, Can also be specified in the prompt
- `TELEGRAM_BOT_TOKEN`: Telegram Bot Token
- `TELEGRAM_BASE_URL`: Telegram Base URL, Default: `https://api.telegram.org`

#### Home Assistant
- `HASS_BASE_URL`: Home Assistant Base URL, Default: `http://homeassistant.local:8123`
- `HASS_ACCESS_TOKEN`: Home Assistant Long-Lived Access Token
- `HASS_MOBILE_KEY`: Home Assistant Mobile Device Key, Can also be specified in the prompt

### 快速开始
- 在线体验: [![fastmcp.cloud](/mcp-assets/0c8c5954cd83912dfc8e38f61cbd6b98.svg)](https://fastmcp.cloud/xiaomi/notify/chat)
- 在线体验: [Smithery](https://smithery.ai/server/@aahl/mcp-notify)
- 添加到 Cursor [![Install MCP Server](/mcp-assets/ec1e84b0a4f6576d1ecdf0b2651745c5.svg)](https://cursor.com/zh/install-mcp?name=notify&config=eyJjb21tYW5kIjoidXZ4IiwiYXJncyI6WyJtY3Atbm90aWZ5Il19)
- 添加到 VS Code [![Install MCP Server](/mcp-assets/a81c1fe0f0f40e3d2dd0ff4b019b0fc6.svg)](https://insiders.vscode.dev/redirect?url=vscode:mcp/install%3F%7B%22name%22%3A%22notify%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22mcp-notify%22%5D%7D)
- 添加到 Cherry Studio [![Install MCP Server](/mcp-assets/973fda9f33903868f3842a3f8c2c4449.svg)](https://gitee.com/link?target=cherrystudio%3A%2F%2Fmcp%2Finstall%3Fservers%3DeyJtY3BTZXJ2ZXJzIjp7Im5vdGlmeSI6eyJjb21tYW5kIjoidXZ4IiwiYXJncyI6WyJtY3Atbm90aWZ5Il19fX0%3D)
- 添加到 Claude Code, 执行命令: `claude mcp add notify -- uvx mcp-notify`
- 添加到 OpenAI CodeX, 执行命令: `codex mcp add notify -- uvx mcp-notify`

------

## 相关连接
- [大饼报告](https://t.me/s/mcpBtc) - 基于此MCP实现的Telegram频道
- https://github.com/hasscc/ai-conversation/discussions/3
- https://linux.do/t/topic/1098688

**官方网站：** [https://github.com/aahl/mcp-notify](https://github.com/aahl/mcp-notify)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`productivity`, `communication`, `media`
- 标签：`communication`, `entertainment and media`, `calendar management`, `notify`, `weixin`, `telegram`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`mcp-notify`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/aalone-notify.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
