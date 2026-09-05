---
title: "简易文件向量存储"
description: "一个非常简单的向量存储，它能够监视目录列表，并自动将目录中的所有markdown、html和文本文件索引到向量存储中，以增强上下文。"
---

# 简易文件向量存储

一个非常简单的向量存储，它能够监视目录列表，并自动将目录中的所有markdown、html和文本文件索引到向量存储中，以增强上下文。

# @lishenxydlgzs/simple-files-vectorstore

一个提供文件间语义搜索功能的模型上下文协议（MCP）服务器。该服务器监控指定目录，并创建文件内容的向量嵌入，从而实现文档间的语义搜索。

## 安装与使用
在您的MCP设置文件中添加：
```json
{
  "mcpServers": {
    "files-vectorstore": {
      "command": "npx",
      "args": [
        "-y",
        "@lishenxydlgzs/simple-files-vectorstore"
      ],
      "env": {
        "WATCH_DIRECTORIES": "/path/to/your/directories"
      },
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

MCP设置文件位置：
- VSCode Cline扩展：`~/Library/Application Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`
- Claude桌面应用程序：`~/Library/Application Support/Claude/claude_desktop_config.json`

## 配置

服务器需要通过环境变量进行配置：

### 必需的环境变量

您必须使用以下方法之一指定要监视的目录：

- `WATCH_DIRECTORIES`: 用逗号分隔的目录列表
- `WATCH_CONFIG_FILE`: 包含`watchList`数组的JSON配置文件路径

使用`WATCH_DIRECTORIES`的例子：
```json
{
  "mcpServers": {
    "files-vectorstore": {
      "command": "npx",
      "args": [
        "-y",
        "@lishenxydlgzs/simple-files-vectorstore"
      ],
      "env": {
        "WATCH_DIRECTORIES": "/path/to/dir1,/path/to/dir2"
      },
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

使用`WATCH_CONFIG_FILE`的例子：
```json
{
  "mcpServers": {
    "files-vectorstore": {
      "command": "npx",
      "args": [
        "-y",
        "@lishenxydlgzs/simple-files-vectorstore"
      ],
      "env": {
        "WATCH_CONFIG_FILE": "/path/to/watch-config.json"
      },
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

监视配置文件应具有如下结构：
```json
{
  "watchList": [
    "/path/to/dir1",
    "/path/to/dir2",
    "/path/to/specific/file.txt"
  ]
}
```

### 可选的环境变量

- `CHUNK_SIZE`: 文本块处理大小（默认: 1000）
- `CHUNK_OVERLAP`: 块之间的重叠部分（默认: 200）
- `IGNORE_FILE`: .gitignore风格文件的路径，用于基于模式排除文件/目录

包含所有可选参数的例子：
```json
  {
    "mcpServers": {
      "files-vectorstore": {
        "command": "npx",
        "args": [
          "-y",
          "@lishenxydlgzs/simple-files-vectorstore"
        ],
        "env": {
          "WATCH_DIRECTORIES": "/path/to/dir1,/path/to/dir2",
          "CHUNK_SIZE": "2000",
          "CHUNK_OVERLAP": "500",
          "IGNORE_FILE": "/path/to/.gitignore"
        },
        "disabled": false,
        "autoApprove": []
      }
    }
  }
```
## MCP工具

此服务器提供了以下MCP工具：

### 1. search

对索引文件执行语义搜索。

参数：
- `query` (必需): 搜索查询字符串
- `limit` (可选): 返回的最大结果数 (默认: 5, 最大: 20)

示例响应：
```json
[
  {
    "content": "matched text content",
    "source": "/path/to/file",
    "fileType": "markdown",
    "score": 0.85
  }
]
```

### 2. get_stats

获取关于索引文件的统计信息。

参数: 无

示例响应：
```json
{
  "totalDocuments": 42,
  "watchedDirectories": ["/path/to/docs"],
  "processingFiles": []
}
```

## 特性

- 实时文件监控和索引
- 使用向量嵌入的语义搜索
- 支持多种文件类型
- 可配置的文本块大小和重叠
- 文件的后台处理
- 自动处理文件变更和删除

## 仓库

[GitHub 仓库](https://github.com/lishenxydlgzs/simple-files-vectorstore)

**官方网站：** [https://github.com/lishenxydlgzs/simple-files-vectorstore](https://github.com/lishenxydlgzs/simple-files-vectorstore)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`files`
- 标签：`file systems`, `knowledge and memory`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @lishenxydlgzs/simple-files-vectorstore`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/lishenxydlgzs-simple-files-vectorstore.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
