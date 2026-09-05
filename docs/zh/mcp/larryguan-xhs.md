---
title: "小红书MCP"
description: "该项目为小红书提供MCP（微服务控制面板）服务，包括搜索笔记、获取笔记内容和发表评论等功能。它使用JavaScript逆向解析出x-s和x-t，可以直接请求HTTP接口，无需使用笨重的Playwright等工具。"
---

# 小红书MCP

该项目为小红书提供MCP（微服务控制面板）服务，包括搜索笔记、获取笔记内容和发表评论等功能。它使用JavaScript逆向解析出x-s和x-t，可以直接请求HTTP接口，无需使用笨重的Playwright等工具。

# 小红书MCP服务
[Smithery](https://smithery.ai/server/@jobsonlook/xhs-mcp)
## 特点
- [x] 采用js逆向出x-s,x-t,直接请求http接口,无须笨重的playwright
- [x] 搜索笔记
- [x] 获取笔记内容
- [x] 获取笔记的评论
- [x] 发表评论

![特性](/mcp-assets/ddc5bcdafe75a173149b4161771f4e89.png)

## 快速开始

### 1. 环境
 * node
 * python 3.12
 * uv (pip install uv)

### 2. 安装依赖
```sh

git clone git@github.com:jobsonlook/xhs-mcp.git

cd xhs-mcp
uv sync 

```

### 3. 获取小红书的cookie
[打开web小红书](https://www.xiaohongshu.com/explore)
登录后，获取cookie，将cookie配置到第4步的 XHS_COOKIE 环境变量中
![cookie](/mcp-assets/5b6ed853fa991ef7c1b5e18d9f8d4e6f.png)

### 4. 配置mcp server

```json
{
    "mcpServers": {
        "xhs-mcp": {
            "command": "uv",
            "args": [
                "--directory",
                "/Users/xxx/xhs-mcp",
                "run",
                "main.py"
            ],
            "env": {
                "XHS_COOKIE": "xxxx"
            }
        }
    }
}
```

## 免责声明
本项目仅用于学习交流，禁止用于其他用途，任何涉及商业盈利目的均不得使用，否则风险自负。

**官方网站：** [https://github.com/jobsonlook/xhs-mcp](https://github.com/jobsonlook/xhs-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`communication`
- 标签：`communication`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`--directory /Users/xxx/xhs-mcp run main.py`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/larryguan-xhs.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
