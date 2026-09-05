---
title: "EasyPrompt--Prompt管理工具"
description: "前言 这是一个管理你 prompt 的工具，直接你在 ai 对话里面搜索你自己的 prompt。 使用很简单，所以叫EasyPrompt 使用环境 - EasyPrompt支持在CherryStdio和Chatbox里面使用 - EasyPrompt支持在Trae，Cursor等支持mcp的编程工具中使用 - EasyPrompt支持在Chrome浏览器，豆包PC端浏览器环境使用。通过浏览器插件，…"
---

# EasyPrompt--Prompt管理工具

前言 这是一个管理你 prompt 的工具，直接你在 ai 对话里面搜索你自己的 prompt。 使用很简单，所以叫EasyPrompt 使用环境 - EasyPrompt支持在CherryStdio和Chatbox里面使用 - EasyPrompt支持在Trae，Cursor等支持mcp的编程工具中使用 - EasyPrompt支持在Chrome浏览器，豆包PC端浏览器环境使用。通过浏览器插件，…

# 前言


这是一个管理你 prompt 的工具，直接你在 ai 对话里面搜索你自己的 prompt。

使用很简单，所以叫EasyPrompt~

# 使用环境

- EasyPrompt支持在CherryStdio和Chatbox里面使用
- EasyPrompt支持在Trae，Cursor等支持mcp的编程工具中使用
- EasyPrompt支持在Chrome浏览器，豆包PC端浏览器环境使用。通过浏览器插件，一键获取你自己的Prompt。（小白用户推荐用这种方式！）

# 使用方法


1. 先去官网https://prompt.code2ai.top  注册一个用户

2. 点击【头像】->【User Center】 -> api-keys

3. 创建一个 API key


# 配置 mcp


```

{

  "mcpServers": {

    "codexun-prompt": {

      "command": "npx",

      "args": [

        "codexun-prompt-mcp@1.0.11",

        "--token",

        "sk-you-api-key"

      ],

      "disabled": false,

      "alwaysAllow": []

    }

  }

}

```

配置的时候需要把 sk-you-api-key 体会成你自己申请的 api-key

备注：codexun-prompt-mcp 有可能更新版本，建议使用最新版本



# 使用教程

https://mp.weixin.qq.com/s/Sm58jONFtsLEa38aF0rkPQ

# 浏览器插件

https://prompt.code2ai.top/posts/prompt-browser-ext

# 官网

https://prompt.code2ai.top/

**官方网站：** [https://www.npmjs.com/package/codexun-prompt-mcp?activeTab=code](https://www.npmjs.com/package/codexun-prompt-mcp?activeTab=code)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`browser`, `media`
- 标签：`developer tools`, `browser automation`, `entertainment and media`, `prompt`, `prompt管理`, `prompt收藏`, `prompt插件`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`codexun-prompt-mcp@1.0.11 --token sk-you-api-key`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/miv2024-codexun-prompt.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
