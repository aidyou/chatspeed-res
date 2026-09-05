---
title: "表情包MCP生成器"
description: "一个简单的模型上下文协议服务器，允许人工智能模型使用ImgFlip API生成表情图像，使用户能够通过文本提示创建表情。"
---

# 表情包MCP生成器

一个简单的模型上下文协议服务器，允许人工智能模型使用ImgFlip API生成表情图像，使用户能够通过文本提示创建表情。

# Meme MCP 服务器

一个使用 ImgFlip API 生成梗图的简单模型上下文协议 (MCP) 服务器。该服务器使 AI 模型和工具能够根据用户提示生成梗图。

  

## 工具

该服务器实现了一个名为 `generateMeme` 的工具。

该工具接受以下参数：

- `templateNumericId`: 要使用的梗图模板的数字 ID。
- `text0`: 第一个占位符的文本。
- `text1`: 第二个占位符的文本。

## 使用方法

你可以使用 [`meme-mcp`](https://www.npmjs.com/package/meme-mcp) NPM 包在客户端中配置梗图生成器服务器。这是一个 Claude Desktop（设置 -> 开发者 -> 编辑配置）的示例配置：

```json
{
  "mcpServers": {
    "meme": {
      "command": "npx",
      "args": ["-y", "meme-mcp"],
      "env": {
        "IMGFLIP_USERNAME": "
",
        "IMGFLIP_PASSWORD": "
"
      }
    }
  }
}
```

> 注意：你需要在 [ImgFlip](https://imgflip.com/signup) 上创建一个免费账户以获取你的用户名和密码。

### 故障排除

有时 Claude Desktop 无法找到正确的 `npx` 版本（特别是如果你正在使用 NVM，详情请参阅此 [问题](https://github.com/modelcontextprotocol/servers/issues/64)）。在这种情况下，你可以手动全局安装 `meme-mcp`，然后直接使用它。

```bash
npm install -g meme-mcp
```

你可以在终端中运行 `which node` 来找到你的 `node` 可执行文件的路径。之后，你的配置应如下所示：

```json
{
  "mcpServers": {
    "meme": {
      "command": "/Users//.nvm/versions/node/v20.18.2/bin/node",
      "args": ["/Users//.nvm/versions/node/v20.18.2/lib/node_modules/meme-mcp/dist/index.js"],
      "env": {
        "IMGFLIP_USERNAME": "
",
        "IMGFLIP_PASSWORD": "
"
      }
    }
  }
}
```

## 示例

配置好 Claude Desktop 后，你需要重新启动它，然后你会在聊天输入框右下角看到一个小锤子图标。然后你可以让 Claude 为你生成一张梗图。

## 作者

该项目由 [Vladimir Haltakov](https://haltakov.net) 出于兴趣创建。如果你觉得有趣，可以在 X 上给我发消息 [@haltakov](https://x.com/haltakov)。

**官方网站：** [https://github.com/haltakov/meme-mcp](https://github.com/haltakov/meme-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`image and video processing`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y meme-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/haltakov-meme.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
