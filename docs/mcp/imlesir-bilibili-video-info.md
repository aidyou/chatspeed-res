---
title: "哔哩哔哩视频信息获取"
description: "这是一个基于MCP（模型上下文协议）的服务器，可以获取Bilibili视频的字幕、弹幕和评论信息。"
---

# 哔哩哔哩视频信息获取

这是一个基于MCP（模型上下文协议）的服务器，可以获取Bilibili视频的字幕、弹幕和评论信息。

# MCP Server for Bilibili Video Info

这是一个基于 MCP (Model Context Protocol) 的服务器，可以获取 Bilibili 视频的字幕、弹幕和评论信息。

## MCP 工具列表

### 1. 获取视频字幕列表

```json
{
  "name": "get_subtitles",
  "arguments": {
    "url": "https://www.bilibili.com/video/BV1x341177NN"
  }
}
```

### 2. 获取视频弹幕

```json
{
  "name": "get_danmaku",
  "arguments": {
    "url": "https://www.bilibili.com/video/BV1x341177NN"
  }
}
```

### 3. 获取视频评论

```json
{
  "name": "get_comments",
  "arguments": {
    "url": "https://www.bilibili.com/video/BV1x341177NN"
  }
}
```

## 使用方法

MCP 客户端配置
```json
{
    "mcpServers": {
        "bilibili-video-info-mcp": {
            "command": "uvx",
            "args": [
                "bilibili-video-info-mcp"
            ],
            "env": {
                "SESSDATA": "your valid sessdata"
            }
        }
    }
}
```

## 常见问题

### 1. 找不到 SESSDATA 怎么办？

1. 登录 Bilibili 网站
2. 打开浏览器开发者工具 (F12)
3. 进入 Application/Storage -> Cookies
4. 找到 SESSDATA 对应的值

### 2. 报错 "SESSDATA environment variable is required"

确保已经设置了环境变量：

```bash
export SESSDATA="你的SESSDATA值"
```

### 3. 视频链接支持哪些格式？

支持标准的 Bilibili 视频链接，例如：
- https://www.bilibili.com/video/BV1x341177NN
- https://b23.tv/xxxxx (短链接)
- 包含 BV 号的任何链接

## 许可证

MIT

**官方网站：** [https://github.com/lesir831/bilibili-video-info-mcp](https://github.com/lesir831/bilibili-video-info-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`entertainment and media`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`bilibili-video-info-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/imlesir-bilibili-video-info.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
