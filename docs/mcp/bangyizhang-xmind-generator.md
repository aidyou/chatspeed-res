---
title: "Xmind生成器"
description: "一种允许大型语言模型创建具有分层主题结构的Xmind思维导图的MCP服务器，支持笔记、标签和标记等功能。"
---

# Xmind生成器

一种允许大型语言模型创建具有分层主题结构的Xmind思维导图的MCP服务器，支持笔记、标签和标记等功能。

# Xmind 生成器 MCP 服务器

一个用于生成 Xmind 思维导图的 MCP（模型上下文协议）服务器。此服务器允许通过 MCP 协议创建结构化的思维导图。

## 特性

- 生成具有层次主题结构的 Xmind 思维导图
- 支持主题注释、标签和标记
- 将思维导图保存到本地文件
- 易于与 Claude Desktop 及其他 MCP 客户端集成

## 前提条件

- **Node.js**：需要版本 18 或更高
- **Xmind**：安装 [Xmind](https://xmind.app/) 桌面应用程序以打开和编辑生成的思维导图
- **Claude Desktop**：作为扩展使用此工具时必需

## 与 Claude Desktop 集成

### 选项 1：使用 npx（推荐）

1. 创建或编辑 Claude Desktop 配置文件：
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`

2. 添加以下配置：
```json
   {
     "mcpServers": {
       "xmind-generator": {
         "command": "npx",
         "args": ["xmind-generator-mcp"],
         "env": {
           "outputPath": "/path/to/save/xmind/files",
           "autoOpenFile": "false"
         }
       }
     }
   }
```

3. 重启 Claude Desktop
4. 开始在对话中使用 Xmind 生成器

### 选项 2：本地安装

1. 克隆仓库：
```bash
   git clone https://github.com/BangyiZhang/xmind-generator-mcp.git
   cd xmind-generator-mcp
   npm install
   npm run build
```

2. 创建或编辑 Claude Desktop 配置文件：
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`

3. 添加以下配置：
```json
   {
     "mcpServers": {
       "xmind-generator": {
         "command": "node",
         "args": ["path/to/xmind-generator-mcp/dist/index.js"],
         "env": {
           "outputPath": "/path/to/save/xmind/files",
           "autoOpenFile": "false"
         }
       }
     }
   }
```

4. 将 `path/to/xmind-generator-mcp` 替换为实际克隆项目的路径
5. 重启 Claude Desktop
6. 开始在对话中使用 Xmind 生成器

**注意**：`env` 部分是可选的。它允许您为服务器设置环境变量：
- `outputPath`：Xmind 文件将被保存的默认目录或文件路径。这可以通过工具调用中的 `outputPath` 参数覆盖。
- `autoOpenFile`：控制生成的 Xmind 文件是否在创建后自动打开。设置为 "false" 以禁用自动打开（默认为 "true"）。

## 可用工具

### generate-mind-map

从主题的层次结构生成 Xmind 思维导图。

参数：

- `title` (字符串): 思维导图的标题（根主题）
- `topics` (数组): 要包含在思维导图中的主题数组
  - `title` (字符串): 主题的标题
  - `ref` (字符串, 可选): 主题的引用ID
  - `note` (字符串, 可选): 主题的备注
  - `labels` (字符串数组, 可选): 主题的标签
  - `markers` (字符串数组, 可选): 主题的标记（格式: "Category.name"，例如: "Arrow.refresh"）
  - `children` (数组, 可选): 子主题数组
- `relationships` (数组, 可选): 主题之间的关系数组
- `outputPath` (字符串, 可选): Xmind文件的自定义输出路径。如果设置了此选项，则会覆盖环境变量。

## 示例

以下是如何使用 `generate-mind-map` 工具的一个示例：

```json
{
  "title": "Project Plan",
  "topics": [
    {
      "title": "Research",
      "ref": "topic:research",
      "note": "Gather information about the market",
      "children": [
        {
          "title": "Market Analysis",
          "labels": ["Priority: High"]
        },
        {
          "title": "Competitor Research",
          "markers": ["Task.quarter"]
        }
      ]
    },
    {
      "title": "Development",
      "children": [
        {
          "title": "Frontend",
          "markers": ["Arrow.refresh"]
        },
        {
          "title": "Backend"
        }
      ]
    }
  ]
}
```

## 许可证

MIT

**官方网站：** [https://github.com/BangyiZhang/xmind-generator-mcp](https://github.com/BangyiZhang/xmind-generator-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`memory`
- 标签：`knowledge and memory`, `note taking`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`xmind-generator-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/bangyizhang-xmind-generator.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
