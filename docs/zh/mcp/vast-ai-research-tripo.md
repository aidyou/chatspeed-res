---
title: "Trippo AI连接器"
description: "通过模型上下文协议为人工智能助手和Tripo AI之间提供接口，从而实现从自然语言生成3D资产并将其导入Blender的功能。"
---

# Trippo AI连接器

通过模型上下文协议为人工智能助手和Tripo AI之间提供接口，从而实现从自然语言生成3D资产并将其导入Blender的功能。

# Tripo MCP 服务器

Tripo MCP 通过 [Model Context Protocol (MCP)](https://github.com/anthropics/anthropic-cookbook/tree/main/mcp) 提供 AI 助手与 [Tripo AI](https://www.tripo3d.ai) 之间的接口。

> **注意：** 该项目目前处于 alpha 阶段。当前支持 Tripo Blender 插件集成。

## 当前功能

- 使用 Tripo 的 API 从自然语言生成 3D 资产并导入到 Blender
- 兼容 Claude 和其他支持 MCP 的 AI 助手

## 快速开始

### 前提条件
- Python 3.10+
- [Blender](https://www.blender.org/download/)
- [Tripo AI Blender 插件](https://www.tripo3d.ai/app/home)
- Claude 桌面版或 Cursor IDE

### 安装步骤

1. 从 [Tripo AI 网站](https://www.tripo3d.ai/app/home)安装 Tripo AI Blender 插件。

2. 在 Claude Desktop 或 Cursor 中配置 MCP 服务器。

3. 开始愉快地创作 3D 内容吧！例如：“生成一个未来风格的椅子的 3D 模型”。

## 致谢

- **[Tripo AI](https://www.tripo3d.ai)**
- **[blender-mcp](https://github.com/ahujasid/blender-mcp)** 由 [Siddharth Ahuja](https://github.com/ahujasid) 提供

**特别感谢**  
特别感谢 Siddharth Ahuja 的 blender-mcp 项目，它为 MCP + 3D 提供了启发性的想法。

**官方网站：** [https://github.com/VAST-AI-Research/tripo-mcp](https://github.com/VAST-AI-Research/tripo-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`art and culture`, `image and video processing`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`tripo-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/vast-ai-research-tripo.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
