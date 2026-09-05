---
title: "智思工具"
description: "实现了Anthropic公司为克劳德开发的“思考”工具，为在复杂问题解决任务中进行结构化推理提供了专门的空间，从而提高了推理链和政策遵循方面的表现。"
---

# 智思工具

实现了Anthropic公司为克劳德开发的“思考”工具，为在复杂问题解决任务中进行结构化推理提供了专门的空间，从而提高了推理链和政策遵循方面的表现。

# MCP Think Tool Server

一个实现用于提升 Claude 复杂推理能力的“思考”工具的 Model Context Protocol (MCP) 服务器。

## 概述

此 MCP 服务器实现了 Anthropic 的“思考”工具，该工具在解决复杂问题时为 Claude 提供了一个专门的空间来进行结构化思考。正如 [Anthropic 的博客文章](https://www.anthropic.com/engineering/claude-think-tool) 所描述的那样，“思考”工具已被证明能够显著提高需要遵循政策和进行长链工具调用推理的复杂任务的表现。

## 自定义指令

添加这些自定义指令到 Claude 中以优化其使用“思考”工具：

```
You have access to a "think" tool that provides a dedicated space for structured reasoning. Using this tool significantly improves your performance on complex tasks. 

## When to use the think tool 
Before taking any action or responding to the user after receiving tool results, use the think tool as a scratchpad to: 
- List the specific rules that apply to the current request 
- Check if all required information is collected 
- Verify that the planned action complies with all policies 
- Iterate over tool results for correctness 
- Analyze complex information from web searches or other tools 
- Plan multi-step approaches before executing them 

## How to use the think tool effectively 
When using the think tool: 
1. Break down complex problems into clearly defined steps 
2. Identify key facts, constraints, and requirements 
3. Check for gaps in information and plan how to fill them 
4. Evaluate multiple approaches before choosing one 
5. Verify your reasoning for logical errors or biases
```

## 主要使用场景

- **复杂的工具链**：当 Claude 需要调用复杂的工具并仔细分析输出时
- **遵守政策**：在有详细指南的政策密集型环境中导航
- **顺序决策**：每一步都基于前一步，并且错误成本高昂
- **多步骤分析**：将复杂问题分解成可管理的步骤

## 安装

```bash
npm install -g @cgize/mcp-think-tool
```

## 配置

将此配置添加到您的 MCP 配置文件中：

```json
{
  "mcpServers": {
    "think-tool": {
      "command": "npx",
      "args": [
        "-y",
        "@cgize/mcp-think-tool"
      ],
      "type": "stdio",
      "pollingInterval": 30000,
      "startupTimeout": 30000,
      "restartOnFailure": true
    }
  }
}
```

配置文件位置：
- `C:\Users\[username]\AppData\Roaming\Claude\claude_desktop_config.json`

如果全局安装，您还可以使用：

```json
{
  "mcpServers": {
    "think-tool": {
      "command": "claude-mcp-think-tool",
      "args": [],
      "type": "stdio",
      "pollingInterval": 30000,
      "startupTimeout": 30000,
      "restartOnFailure": true
    }
  }
}
```

## 可用工具

- **think**：在解决问题过程中记录结构化推理
- **get_thoughts**：检索所有记录的想法
- **clear_thoughts**：重置思考过程
- **get_thought_stats**：分析思考模式

## 示例提示

```
Using the think tool, solve this multi-step problem:

A train travels at a constant speed of 60 km/h. It departs from station A at 9:00 AM and arrives at station B at 11:30 AM. What is the distance between stations A and B?
```

## 许可证

MIT

**官方网站：** [https://github.com/cgize/claude-mcp-think-tool](https://github.com/cgize/claude-mcp-think-tool)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`memory`
- 标签：`knowledge and memory`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @cgize/mcp-think-tool`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/cgize-claude-think-tool.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
