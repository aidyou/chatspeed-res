---
title: "jasnonaz"
description: "Vibe Worldbuilding MCP 一个用于通过Claude创建详细虚构世界的模型上下文协议（MCP），并附带自动图像生成功能。 概述 此MCP通过结构化的方法帮助您构建丰富且连贯的虚构世界。它利用Claude的能力来帮助您开发概念、探索细节并保持一致性。该MCP还可以生成图像以视觉上表示您的世界元素。 安装 1. 安装MCP CLI： pip install mcp 2. 安装所需的依…"
---

# jasnonaz

Vibe Worldbuilding MCP 一个用于通过Claude创建详细虚构世界的模型上下文协议（MCP），并附带自动图像生成功能。 概述 此MCP通过结构化的方法帮助您构建丰富且连贯的虚构世界。它利用Claude的能力来帮助您开发概念、探索细节并保持一致性。该MCP还可以生成图像以视觉上表示您的世界元素。 安装 1. 安装MCP CLI： pip install mcp 2. 安装所需的依…

# Vibe Worldbuilding MCP

一个用于通过Claude创建详细虚构世界的模型上下文协议（MCP），并附带自动图像生成功能。

## 概述

此MCP通过结构化的方法帮助您构建丰富且连贯的虚构世界。它利用Claude的能力来帮助您开发概念、探索细节并保持一致性。该MCP还可以生成图像以视觉上表示您的世界元素。

## 安装

1. 安装MCP CLI：
   
   pip install mcp
   

2. 安装所需的依赖项：
   
   pip install google-generativeai
   

3. 使用您的Google AI API密钥安装Vibe Worldbuilding MCP：
   
   cd /path/to/vibe-worldbuilding-mcp
   mcp install vibe_worldbuilding_server.py -v IMAGEN_API_KEY=your_api_key_here
   

   `-v` 标志设置了图像生成所需的环境变量。如果您没有用于Imagen的Google AI API密钥，仍然可以使用MCP进行世界构建，但图像生成功能将不可用。

   或者，您可以在开发模式下测试MCP：
   
   mcp dev vibe_worldbuilding_server.py -v IMAGEN_API_KEY=your_api_key_here
   

## 如何使用

MCP提供了几个提示来指导您的世界构建过程：

1. **start-worldbuilding** - 开始一个新的世界项目
2. **continue-worldbuilding** - 继续处理现有的世界
3. **world-foundation** - 发展您的世界的核心概念
4. **taxonomy** - 为世界元素创建分类系统
5. **world-entry** - 为特定元素创建详细的条目
6. **consistency-review** - 检查逻辑一致性
7. **entry-revision** - 修改和完善现有条目
8. **workflow** - 获取整个过程的指导

### 图像生成

MCP可以为您的世界元素生成图像。在为条目、分类或其他元素创建Markdown文件后，使用`generate_image_from_markdown_file`工具：

Use the generate_image_from_markdown_file tool with path="/path/to/your/file.md"

该工具将：
1. 读取您的Markdown文件内容
2. 提取标题和描述
3. 使用Google的Imagen API生成适当的图像
4. 将图像保存在Markdown文件旁边的“images”文件夹中

然后您可以将生成的图像上传到Claude，在对话中查看它。

## 世界构建工作流程

1. 从**start-worldbuilding**提示开始
2. 对于每个新会话，从**continue-worldbuilding**开始
3. 按以下顺序发展您的世界：
   - 世界基础（核心概念和概述）
   - 分类法（分类系统）
   - 具体条目（详细文章）
4. 通过发展您感兴趣的元素让您的世界有机地成长
5. 为您的世界元素生成图像，使其在视觉上生动起来

## 示例会话

用户：让我们创建一个新世界。

[用户从MCP菜单中选择"start-worldbuilding"提示]

Claude: [显示世界构建提示]

用户：我想创建一个声音具有魔法属性的世界。

Claude: [帮助开发概念并探讨其影响]

用户：让我们把这个作为我的世界概览文件保存。

Claude: [将内容保存到world-overview.md]

用户：现在为这个概览生成一张图片。

[用户使用generate_image_from_markdown_file工具]

Claude: [生成图像并保存到磁盘]

## 要求

- 用于Imagen的Google AI API密钥（设置为IMAGEN_API_KEY环境变量）
- Google Generative AI Python库 (`google-generativeai`)
- MCP CLI工具

## 成功小贴士

- 逐步构建您的世界，从核心概念开始
- 创建相关内容的集群
- 定期审查一致性
- 重视质量而非数量
- 让您的世界自然地浮现
- 使用生成的图像激发进一步的世界构建灵感

**官方网站：** [https://github.com/jasnonaz/vibe-worldbuilding-mcp](https://github.com/jasnonaz/vibe-worldbuilding-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`art and culture`, `image and video processing`, `content management systems`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`python3`
- 参数：`./vibe_worldbuilding_server.py`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/jasnonaz-vibe-worldbuilding.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
