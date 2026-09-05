---
title: "我的小红书知识卡片"
description: "MD2Card MCP 服务器 homepage: https://md2card.cn"
---

# 我的小红书知识卡片

MD2Card MCP 服务器 homepage: https://md2card.cn

# mycard MCP 服务器

> 官方网站: https://md2card.cn/zh/my/api-keys

## 简介

mycard 是一个强大的 Markdown 转知识卡片工具，能够将普通的 Markdown 文档转换为精美的知识卡片，支持多种视觉风格和自定义选项。无论是用于社交媒体分享、学习笔记还是专业演示，mycard 都能满足您的需求。

## 安装与使用

在开始使用前，您需要先获取 API 密钥。请访问 [mycard 官网](https://md2card.cn/zh?referralCode=github) 申请您的专属密钥。

### 方法一：使用 npx（推荐）

这是最简单的方式，无需安装，直接使用 npx 运行：

```bash
# 设置API密钥并运行
MYCARD_API_KEY="您的API密钥" npx mycard-mcp-server
```

### 方法二：全局安装

如果您需要频繁使用，可以选择全局安装：

```bash
# 全局安装
npm install -g mycard-mcp-server

# 运行服务
MYCARD_API_KEY="您的API密钥" mycard-mcp-server
```

### 方法三：本地配置

对于开发者或需要自定义功能的用户：

1. 克隆项目到本地
2. 找到 index.js 文件路径
3. 将该路径替换到您的客户端 MCP 配置文件中

## 功能特性

### 丰富的主题选择

mycard 提供 22 种精美主题样式，满足不同场景需求：

- **日常风格**：苹果备忘录、笔记本、简约高级灰
- **艺术风格**：波普艺术、艺术装饰、水彩艺术、中国传统
- **现代设计**：玻璃拟态、梦幻渐变、暗黑科技、赛博朋克
- **特色风格**：温暖柔和、清新自然、紫色小红书、复古打字机、儿童童话、商务简报、日本杂志、极简黑白

### 智能功能

- **智能尺寸适配**：自动调整内容布局，确保在不同尺寸下都能完美展示
- **三种内容拆分模式**：默认自动拆分，也支持手动控制拆分方式
- **标准化接口**：通过 MCP 协议提供服务，易于集成到各种工作流程中

### 最新功能

- **直接读取 Markdown 文件**：支持从文件路径直接读取内容，无需手动复制粘贴
- **自定义卡片类型/尺寸**：支持通过 type 参数直接指定卡片类型和尺寸，更加灵活

## 使用方法

mycard 提供了多种灵活的使用方式，您可以根据自己的需求选择最适合的方法。

### 方法一：直接提供 Markdown 内容

最基本的使用方式，直接传入 Markdown 文本：

```json
{
  "markdown": "# 我的知识卡片\n\n这是一段示例内容，支持所有标准的 **Markdown** 语法。\n\n- 列表项 1\n- 列表项 2\n\n> 引用文本也能完美支持"
}
```

### 方法二：提供 Markdown 文件路径

适合处理已有的 Markdown 文件，无需复制内容：

```json
{
  "markdownFile": "/path/to/your/file.md"
}
```

### 方法三：自定义卡片类型和尺寸

#### 预设卡片类型

mycard 支持以下预设类型，方便快速创建特定场景的卡片：

| 类型 | 尺寸 | 适用场景 |
|------|------|----------|
| 小红书 | 440×586 | 小红书笔记、社交媒体分享 |
| 正方形 | 500×500 | 通用社交媒体、头像、缩略图 |
| 手机海报 | 440×782 | 手机端展示的长图文内容 |
| A4 纸打印 | 595×842 | 打印文档、PDF 导出 |

使用示例：

```json
{
  "markdown": "# 我的小红书笔记\n\n分享一些有趣的内容...",
  "type": "小红书"
}
```

#### 自定义尺寸

您也可以通过 width 和 height 参数完全自定义卡片尺寸：

```json
{
  "markdown": "# 自定义尺寸卡片\n\n完全按照我的需求定制尺寸",
  "width": 600,
  "height": 800
}
```

> **提示**：为获得最佳效果，建议保持宽高比在 1:1 到 1:2 之间

## 客户端配置

mycard 支持通过 MCP（Model Control Protocol）协议与各种客户端集成，下面是常见客户端的配置方法。

### 通用 MCP 客户端配置

对于支持 MCP 协议的通用客户端，在配置文件中添加以下内容：

```json
{
  "mycard-server": {
    "command": "npx",
    "args": ["mycard-mcp-server@latest"],
    "env": {
      "MYCARD_API_KEY": "您的API密钥"
    }
  }
}
```

### Cursor 编辑器配置

[Cursor](https://cursor.sh/) 是一个支持 AI 功能的代码编辑器，您可以在其 MCP 配置文件中添加：

```json
{
  "mycard-server": {
    "command": "npx",
    "args": ["-y", "mycard-mcp-server@latest"],
    "env": {
      "MYCARD_API_KEY": "您的API密钥"
    }
  }
}
```

### 其他编辑器和工具

mycard 可以与任何支持 MCP 协议的工具集成，包括但不限于：

- VS Code（通过插件）
- JetBrains 系列 IDE
- 命令行工具

## 注意事项

- **API 密钥**：MYCARD_API_KEY 环境变量是必需的，只有在实际运行时才会检查此环境变量。安装包时不需要此环境变量。
- **版本更新**：使用 `@latest` 标签可以确保始终使用最新版本，也可以指定特定版本号。
- **自定义配置**：高级用户可以通过修改源代码进行更深度的自定义。

## 获取帮助

- **官方文档**：访问 [mycard 官网](https://md2card.cn) 获取完整文档
- **API 密钥申请**：通过 [此链接](https://md2card.cn/zh?referralCode=github) 申请您的 API 密钥
- **问题反馈**：如有问题或建议，请通过官网联系我

**官方网站：** [https://github.com/maqi1520/md2card-mcp-server](https://github.com/maqi1520/md2card-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`memory`
- 标签：`knowledge and memory`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y md2card-mcp-server@latest`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/undoom-my-mdcard.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
