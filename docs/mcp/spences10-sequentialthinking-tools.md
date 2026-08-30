---
title: "MCP问题解决工具"
description: "# 翻译\n这是MCP顺序思维服务器的一个改编版本，旨在指导在解决问题时如何使用工具。该服务器有助于将复杂问题分解为可管理的步骤，并提供在每个阶段使用哪些MCP工具最为有效的建议。"
---

# MCP问题解决工具

# 翻译
这是MCP顺序思维服务器的一个改编版本，旨在指导在解决问题时如何使用工具。该服务器有助于将复杂问题分解为可管理的步骤，并提供在每个阶段使用哪些MCP工具最为有效的建议。

# mcp-sequentialthinking-tools

这是对
[MCP Sequential Thinking Server](https://github.com/modelcontextprotocol/servers/blob/main/src/sequentialthinking/index.ts)
的改编版本，旨在指导解决问题时的工具使用。该服务器帮助将复杂问题分解为可管理的步骤，并提供在每个阶段最有效的MCP工具推荐。

  

这是一个结合了顺序思维与智能工具建议的模型上下文协议（MCP）服务器。对于解决问题过程中的每一步，它都会根据信心分数提供哪些工具应该使用的建议，以及为何这些工具适合的理由。

## 功能特点

- 🤔 通过顺序思考进行动态且反思性的问题解决
- 🔄 灵活适应并进化的思考过程
- 🌳 支持思想分支和修订
- 🛠️ 每步都有智能工具推荐
- 📊 工具建议的信心评分
- 🔍 详细的工具推荐理由
- 📝 带有预期结果的步骤跟踪
- 🔄 进度监控，包括已完成及剩余步骤
- 🎯 每步的替代工具建议

## 工作原理

此服务器分析您思考过程中的每一步，并推荐合适的MCP工具来帮助完成任务。每条建议都包含：

- 一个信心分数（0-1），表示工具与当前需求的匹配程度
- 清晰的理由说明为什么该工具会有帮助
- 一个优先级水平，用于建议工具执行顺序
- 可以使用的替代工具

服务器可以与您环境中可用的任何MCP工具一起工作。它根据当前步骤的要求提供建议，但实际工具执行由消费者（如Claude）处理。

## 使用示例

这里有一个例子展示了服务器如何引导工具使用：

```json
{
    "thought": "Initial research step to understand what universal reactivity means in Svelte 5",
    "current_step": {
        "step_description": "Gather initial information about Svelte 5's universal reactivity",
        "expected_outcome": "Clear understanding of universal reactivity concept",
        "recommended_tools": [
            {
                "tool_name": "search_docs",
                "confidence": 0.9,
                "rationale": "Search Svelte documentation for official information",
                "priority": 1
            },
            {
                "tool_name": "tavily_search",
                "confidence": 0.8,
                "rationale": "Get additional context from reliable sources",
                "priority": 2
            }
        ],
        "next_step_conditions": [
            "Verify information accuracy",
            "Look for implementation details"
        ]
    },
    "thought_number": 1,
    "total_thoughts": 5,
    "next_thought_needed": true
}
```

服务器会追踪您的进度并支持：

- 创建分支探索不同的方法
- 根据新信息修改先前的想法
- 在多个步骤间保持上下文
- 根据当前发现建议下一步

## 配置

此服务器需要通过您的MCP客户端进行配置。以下是在不同环境下的配置示例：

### Cline 配置

将以下内容添加到您的Cline MCP设置中：

```json
{
    "mcpServers": {
        "mcp-sequentialthinking-tools": {
            "command": "npx",
            "args": ["-y", "mcp-sequentialthinking-tools"]
        }
    }
}
```

### Claude Desktop with WSL 配置

对于WSL环境，请将以下内容添加到您的Claude Desktop配置中：

```json
{
    "mcpServers": {
        "mcp-sequentialthinking-tools": {
            "command": "wsl.exe",
            "args": [
                "bash",
                "-c",
                "source ~/.nvm/nvm.sh && /home/username/.nvm/versions/node/v20.12.1/bin/npx mcp-sequentialthinking-tools"
            ]
        }
    }
}
```

## API

该服务器实现了一个带有可配置参数的单个MCP工具：

### sequentialthinking_tools

一个通过思考来进行动态且反思性问题解决的工具，附带智能工具推荐。

参数：

- `thought` (字符串, 必填): 你当前的思考步骤
- `next_thought_needed` (布尔值, 必填): 是否需要另一个思考步骤
- `thought_number` (整数, 必填): 当前思考步骤编号
- `total_thoughts` (整数, 必填): 预计总共需要的思考步骤数量
- `is_revision` (布尔值, 可选): 是否修订了之前的思考
- `revises_thought` (整数, 可选): 正在重新考虑的思考步骤编号
- `branch_from_thought` (整数, 可选): 分支点的思考步骤编号
- `branch_id` (字符串, 可选): 分支标识符
- `needs_more_thoughts` (布尔值, 可选): 是否需要更多的思考步骤
- `current_step` (对象, 可选): 当前步骤建议，包含:
  - `step_description`: 需要做什么
  - `recommended_tools`: 带有置信度分数的工具推荐数组
  - `expected_outcome`: 从这一步骤中可以期待什么结果
  - `next_step_conditions`: 下一步骤的条件
- `previous_steps` (数组, 可选): 已经推荐的步骤
- `remaining_steps` (数组, 可选): 即将到来的步骤的高层描述

## 开发

### 设置

1. 克隆仓库
2. 安装依赖项：

```bash
pnpm install
```

3. 构建项目：

```bash
pnpm build
```

4. 在开发模式下运行：

```bash
pnpm dev
```

### 发布

该项目使用 changesets 进行版本管理。要发布：

1. 创建一个 changeset：

```bash
pnpm changeset
```

2. 对包进行版本控制：

```bash
pnpm changeset version
```

3. 发布到 npm：

```bash
pnpm release
```

## 贡献

欢迎贡献！请随时提交 Pull Request。

## 许可证

MIT 许可证 - 详情请参阅 [LICENSE](https://github.com/spences10/mcp-sequentialthinking-tools/blob/HEAD/LICENSE) 文件。

## 致谢

- 基于 [Model Context Protocol](https://github.com/modelcontextprotocol)
- 改编自 [MCP Sequential Thinking Server](https://github.com/modelcontextprotocol/servers/blob/main/src/sequentialthinking/index.ts)

**官方网站：** [https://github.com/spences10/mcp-sequentialthinking-tools](https://github.com/spences10/mcp-sequentialthinking-tools)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`productivity`
- 标签：`other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y mcp-sequentialthinking-tools`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/spences10-sequentialthinking-tools.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
