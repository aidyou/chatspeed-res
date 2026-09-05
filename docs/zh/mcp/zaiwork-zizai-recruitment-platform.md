---
title: "自在招聘-MCP"
description: "自在招聘平台（https://zizai.work）MCP 服务是一个与 MCP 协议完全兼容的核心 API 服务，是中国第一家支持该协议的招聘平台服务提供商。"
---

# 自在招聘-MCP

自在招聘平台（https://zizai.work）MCP 服务是一个与 MCP 协议完全兼容的核心 API 服务，是中国第一家支持该协议的招聘平台服务提供商。

# 自在招聘 MCP Server

MCP Server for 自在招聘 API.

# 自在招聘
自在招聘（[https://zizai.work](https://zizai.work)）是一个基于专业测评的新一代智能招聘平台，帮助人才与职位高效、精准的智能匹配。

加入我们，立即体验智能招聘的魅力！

## Tools

1. `get-job-list`
   - 获取推荐的职位列表
   - Input:
     - `keyword` (string, 可选): 职位搜索关键词。
     - `recruitType` (number, 可选): 职位类型，1-社招，2-校招，2-实习
   - Returns:
     - Array of {
       - `workPin`: string
       - `name`: string
       - `entityName`: string
       - `entityShortname`: string
       - `responsibility`: string
       - `requirement`: string
       - `welfare`: string
       - `salary`: { minSalary: number, maxSalary: number } | string
       - `detailUrl`: string
     }

2. `apply-for-job`
   - 投递职位
   - Inputs:
     - `workPin` (string) 职位唯一码
   - Returns:

## Setup

### API Key
Get a ZIZAI Work API key by following the instructions [here](https://zizai.work/user/apikey).

### Usage with Claude Desktop

Add the following to your `claude_desktop_config.json`:

### NPX

```json
{
  "mcpServers": {
    "zaiwork": {
      "command": "npx",
      "args": [
        "-y",
        "@zizaiwork/mcp"
      ],
      "env": {
        "ZAI_API_KEY": ""
      }
    }
  }
}
```

## License

This MCP server is licensed under the Apache-2.0 License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the Apache-2.0 License. For more details, please see the LICENSE file in the project repository.

**官方网站：** [https://github.com/zaiwork/mcp](https://github.com/zaiwork/mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`search`, `research and data`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @zizaiwork/mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/zaiwork-zizai-recruitment-platform.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
