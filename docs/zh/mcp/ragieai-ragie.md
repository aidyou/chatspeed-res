---
title: "Ragie 检索服务器"
description: "一个MCP服务器，它使AI模型能够通过简单的“检索”工具从Ragie的知识库中获取信息。"
---

# Ragie 检索服务器

一个MCP服务器，它使AI模型能够通过简单的“检索”工具从Ragie的知识库中获取信息。

![image](/mcp-assets/83c61dd838391a10eff0cc084cfcdaff.png)

# Ragie 模型上下文协议服务器

一个模型上下文协议（MCP）服务器，提供访问Ragie知识库检索功能的接口。

## 说明

该服务器实现了模型上下文协议，使AI模型能够从Ragie知识库中检索信息。它提供了一个名为“retrieve”的工具，允许查询知识库以获取相关信息。

## 先决条件

- Node.js >= 18
- 一个Ragie API密钥

## 安装

服务器需要以下环境变量：

- `RAGIE_API_KEY` (必需): 您的Ragie API认证密钥

服务器将启动并在标准输入输出上监听MCP协议消息。

使用npx安装并运行服务器：

```bash
RAGIE_API_KEY=your_api_key npx @ragieai/mcp-server
```

### 命令行选项

该服务器支持以下命令行选项：

- `--description, -d `: 使用自定义文本覆盖默认工具描述
- `--partition, -p 
`: 指定要查询的Ragie分区ID

示例：

```bash
# With custom description
RAGIE_API_KEY=your_api_key npx @ragieai/mcp-server --description "Search the company knowledge base for information"

# With partition specified
RAGIE_API_KEY=your_api_key npx @ragieai/mcp-server --partition your_partition_id

# Using both options
RAGIE_API_KEY=your_api_key npx @ragieai/mcp-server --description "Search the company knowledge base" --partition your_partition_id
```

## Cursor 配置

为了与Cursor一起使用此MCP服务器：

### 选项1：创建MCP配置文件

1. 保存名为`mcp.json`的文件

* **对于特定于项目的工具**，在您的项目目录中创建一个`.cursor/mcp.json`文件。这允许您定义仅在该项目内可用的MCP服务器。
* **对于希望跨所有项目使用的工具**，在您的主目录中创建一个`~/.cursor/mcp.json`文件。这样可以让MCP服务器在所有的Cursor工作空间中都可用。

示例`mcp.json`：
```json
{
  "mcpServers": {
    "ragie": {
      "command": "npx",
      "args": [
        "-y",
        "@ragieai/mcp-server",
        "--partition",
        "optional_partition_id"
      ],
      "env": {
        "RAGIE_API_KEY": "your_api_key"
      }
    }
  }
}
```

### 选项2：使用shell脚本

1. 在系统上保存名为`ragie-mcp.sh`的文件：
```bash
#!/usr/bin/env bash

export RAGIE_API_KEY="your_api_key"

npx -y @ragieai/mcp-server --partition optional_partition_id
```

2. 给文件执行权限：`chmod +x ragie-mcp.sh`

3. 通过进入Cursor UI中的**设置** -> **Cursor设置** -> **MCP服务器**来添加MCP服务器脚本。

将`your_api_key`替换为您的实际Ragie API密钥，并根据需要设置分区ID（如果需要的话）。

## Claude 桌面配置

为了与Claude桌面版一起使用此MCP服务器：

1. 创建MCP配置文件`claude_desktop_config.json`：

* 对于MacOS: 使用`~/Library/Application Support/Claude/claude_desktop_config.json`
* 对于Windows: 使用`%APPDATA%/Claude/claude_desktop_config.json`

示例`claude_desktop_config.json`：
```json
{
  "mcpServers": {
    "ragie": {
      "command": "npx",
      "args": [
        "-y",
        "@ragieai/mcp-server",
        "--partition",
        "optional_partition_id"
      ],
      "env": {
        "RAGIE_API_KEY": "your_api_key"
      }
    }
  }
}
```

将`your_api_key`替换为您的实际Ragie API密钥，并根据需要设置分区ID（如果需要的话）。

2. 重启Claude桌面版以使更改生效。

现在，您可以在Claude桌面对话中使用Ragie检索工具了。

## 功能

### 检索工具

服务器提供了一个`retrieve`工具，可用于搜索知识库。它接受以下参数：

- `query` (字符串): 要查找相关信息的搜索查询

该工具返回：
- 包含来自知识库匹配文本的内容块数组

## 开发

该项目用TypeScript编写，并使用了以下主要依赖项：

- `@modelcontextprotocol/sdk`: 用于实现MCP服务器
- `ragie`: 用于与Ragie API交互
- `zod`: 用于运行时类型验证

### 开发环境设置

在开发模式下运行服务器：

```bash
RAGIE_API_KEY=your_api_key npm run dev -- --partition optional_partition_id
```

构建项目：

```bash
npm run build
```

## 许可证

MIT许可证 - 详情请参阅LICENSE.txt。

**官方网站：** [https://github.com/ragieai/ragie-mcp-server](https://github.com/ragieai/ragie-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`memory`
- 标签：`search`, `knowledge and memory`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @ragieai/mcp-server --partition optional_partition_id`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/ragieai-ragie.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
