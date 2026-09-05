---
title: "ip2region"
description: "You can obtain the local public IP and also support querying the归属地 (location) of any IP address. It seems like a part of your sentence was left in Chinese. I assume you meant to say \"querying the loc…"
---

# ip2region

You can obtain the local public IP and also support querying the归属地 (location) of any IP address. It seems like a part of your sentence was left in Chinese. I assume you meant to say "querying the loc…

### 提供2个免费mcp工具，无需认证，无需付费，开箱即用
#### 1. ip2region 支持任意IP地址归属地查询
#### 2. get_local_ip 获取您本地公网IP

### 非mcp调用，请使用 ifconfig.cc 同样免费
### 使用方法：将以下json添加到配置文件中
```
{
  "mcpServers": {
    "ip2region": {
      "url": "https://mcp.ifconfig.cc"
    }
  }
}
```

**Official site: ** [https://ifconfig.cc](https://ifconfig.cc)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `developer tools`, `location services`, `search`, `ip`, `归属地`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/nmgliangwei-ip2region.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
