---
title: "Fiscal Data 连接器"
description: "连接到美国财政部的财政数据API，使用户能够获取特定的财政部报表、访问历史数据并生成格式化的报告。"
---

# Fiscal Data 连接器

连接到美国财政部的财政数据API，使用户能够获取特定的财政部报表、访问历史数据并生成格式化的报告。

## 概述

[Fiscal Data MCP 服务器](https://github.com/QuantGeekDev/fiscal-data-mcp) 展示了一个连接到美国财政部 Fiscal Data API 的MCP服务器的实际实现。它展示了以下功能：

- 获取特定财政报表的工具
- 访问历史数据的资源
- 生成格式化报告的提示

## 快速开始

### 1. 使用 Claude Desktop 安装和使用

将此配置添加到您的 Claude Desktop 配置文件中：

**MacOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "fiscal-data": {
      "command": "npx",
      "args": ["fiscal-data-mcp"]
    }
  }
}
```

### 2. 示例交互

配置完成后，您可以通过 Claude 与服务器进行交互：

```
Human: Can you get the treasury statement for the 20th of September 2023?
```

## 功能

### 1. 每日财政报表

使用 `get_daily_treasury_statement` 工具获取特定日期的财政数据：

```typescript
// Example usage through Claude
Human: Get the treasury statement for 2024-03-01
Assistant: I'll fetch that information for you using the treasury statement tool.
```

### 2. 历史数据资源

通过资源系统访问30天的历史财政数据：
- 自动缓存1小时
- 按需更新
- 提供格式化的 JSON 数据

### 3. 报告生成

使用 `daily_treasury_report` 提示生成格式化的财政报告：

```typescript
// Example usage through Claude
Human: Generate a treasury report for 2024-03-01
Assistant: I'll use the daily treasury report prompt to create a formatted report...
```

**官方网站：** [https://github.com/QuantGeekDev/fiscal-data-mcp](https://github.com/QuantGeekDev/fiscal-data-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`finance`, `data`
- 标签：`finance`, `research and data`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`fiscal-data-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/quantgeekdev-fiscal-data.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
