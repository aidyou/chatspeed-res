---
title: "B站视频信息获取器（MCP&Agent挑战赛）"
description: "B站视频信息获取器 这是一个基于Python和Gradio的B站视频信息获取工具，可以通过视频链接或BV号快速获取B站视频的详细信息，包括UP主信息、视频基本信息和视频数据。 功能特点 - 支持输入B站视频链接或直接输入BV号 - 获取视频的详细信息：标题、类型、简介、发布时间、时长等 - 获取UP主信息：昵称、用户ID、粉丝数、关注数等 - 获取视频统计数据：播放量、弹幕数、点赞数、投币数、收藏数、分享数等 - 提供友好的Web界面，支持示例输入 - 支持MCP服务器功能，便于集成到其他应用 - 生成公共可访问链"
---

# B站视频信息获取器（MCP&Agent挑战赛）

B站视频信息获取器 这是一个基于Python和Gradio的B站视频信息获取工具，可以通过视频链接或BV号快速获取B站视频的详细信息，包括UP主信息、视频基本信息和视频数据。 功能特点 - 支持输入B站视频链接或直接输入BV号 - 获取视频的详细信息：标题、类型、简介、发布时间、时长等 - 获取UP主信息：昵称、用户ID、粉丝数、关注数等 - 获取视频统计数据：播放量、弹幕数、点赞数、投币数、收藏数、分享数等 - 提供友好的Web界面，支持示例输入 - 支持MCP服务器功能，便于集成到其他应用 - 生成公共可访问链

# B站视频信息获取器

这是一个基于Python和Gradio的B站视频信息获取工具，可以通过视频链接或BV号快速获取B站视频的详细信息，包括UP主信息、视频基本信息和视频数据。

## 功能特点

- 支持输入B站视频链接或直接输入BV号
- 获取视频的详细信息：标题、类型、简介、发布时间、时长等
- 获取UP主信息：昵称、用户ID、粉丝数、关注数等
- 获取视频统计数据：播放量、弹幕数、点赞数、投币数、收藏数、分享数等
- 提供友好的Web界面，支持示例输入
- 支持MCP服务器功能，便于集成到其他应用
- 生成公共可访问链接，方便远程使用

## 使用说明

1. 在输入框中输入B站视频链接或直接输入BV号
2. 点击"提交"按钮
3. 在输出框中查看获取到的视频详细信息
4. 可以使用示例按钮快速测试

## MCP服务器功能

该程序支持MCP（Model Communication Protocol）服务器功能，允许其他应用程序通过HTTP请求与本程序进行通信，获取B站视频信息。

### MCP服务器使用方法

当程序运行时，MCP服务器会自动启动，其他应用可以通过以下方式与其通信：

1. 向MCP服务器发送POST请求，请求格式如下：
```http
POST /run/predict HTTP/1.1
Content-Type: application/json

{
  "data": ["B站视频链接或BV号"]
}
```

2. 服务器将返回JSON格式的响应，包含获取到的视频信息

## 示例

### 示例1：使用BV号
输入：`BV1XmtyzKEzQ`

### 示例2：使用视频链接
输入：`https://www.bilibili.com/video/BV1xx411x7x9/`

## 注意事项

- 本工具仅用于获取公开的视频信息，不得用于任何非法用途
- 请遵守B站的用户协议和相关规定
- 由于B站API限制，部分视频信息可能无法获取或需要登录
- 使用过程中如遇到问题，请检查网络连接或尝试更换视频链接

**官方网站：** [http://modelscope.cn/studios/JackGan/bilibili_video_info](http://modelscope.cn/studios/JackGan/bilibili_video_info)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`search`, `entertainment and media`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`mcp-remote https://jackgan-bilibili-video-info.ms.show/gradio_api/mcp/sse --transport sse-only`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/jackgan-bilibili-video-info.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
