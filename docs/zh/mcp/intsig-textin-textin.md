---
title: "TextIn-MCP OCR服务器"
description: "一台启用OCR功能的服务器，可以从图像、PDF和Word文档中识别文本，将其转换为Markdown格式，并提取关键信息。"
---

# TextIn-MCP OCR服务器

一台启用OCR功能的服务器，可以从图像、PDF和Word文档中识别文本，将其转换为Markdown格式，并提取关键信息。

# Textin MCP Server

TextIn MCP Server 是一个用于从文档中提取文本并执行OCR的工具，包括文档文本识别、身份证识别和发票识别。它还支持将文档转换为Markdown格式。

  

## 工具
- `recognition_text`
  - 从图片、Word文档和PDF文件中进行文本识别。
  - 输入: `file path` (字符串)
  - 返回: 文档的文本。

- `doc_to_markdown`
  - 将图片、PDF和Word文档转换为Markdown。
  - 输入: `file path` (字符串)
  - 返回: 文档的Markdown。

- `general_information_extration`
  - 自动且智能地从文档中提取关键信息。
  - 输入: `file path` (字符串)
  - 返回: 关键信息的JSON。

## 设置

### APP_ID 和 APP_SECRET

点击[这里](https://www.textin.com/user/login?from=github_mcp)注册一个TextIn账户。

按照[此处](https://www.textin.com/doc/guide/account/%E5%A6%82%E4%BD%95%E8%8E%B7%E5%8F%96app%20id?status=first)的说明获取Textin APP_ID和APP_SECRET。

### NPX

```json
{
  "mcpServers": {
    "textin-ocr": {
      "command": "npx",
      "args": [
        "-y",
        "@intsig/server-textin"
      ],
      "env": {
        "APP_ID": "",
        "APP_SECRET": "",
        "MCP_SERVER_REQUEST_TIMEOUT": "600000"
      },
      "timeout": 600
    }
  }
}
```

## 许可证

此MCP服务器采用MIT许可证授权。这意味着您可以在遵守MIT许可证条款和条件的前提下自由使用、修改和分发该软件。更多详情，请参见项目仓库中的LICENSE文件。

**官方网站：** [https://github.com/intsig-textin/textin-mcp](https://github.com/intsig-textin/textin-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`files`
- 标签：`image and video processing`, `file systems`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @intsig/server-textin`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/intsig-textin-textin.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
