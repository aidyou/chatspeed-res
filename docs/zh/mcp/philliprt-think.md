---
title: "Think推理服务器"
description: "Anthropic的“think”工具的官方实现，该工具为Claude提供了一个专门用于结构化推理的空间，从而在需要多步骤解决问题的复杂任务上，性能最多可提高54%。"
---

# Think推理服务器

Anthropic的“think”工具的官方实现，该工具为Claude提供了一个专门用于结构化推理的空间，从而在需要多步骤解决问题的复杂任务上，性能最多可提高54%。

# Think Tool MCP Server

[Smithery](https://smithery.ai/server/@PhillipRt/think-mcp-server)

**Anthropic 的 "think" 工具的官方 MCP 服务器实现** - 通过结构化思考显著提高 Claude 的推理能力。

## 什么是 Think 工具？

这个 MCP 服务器实现了 Anthropic 在其[工程博客文章](https://www.anthropic.com/engineering/claude-think-tool)中介绍的确切 "think" 工具。Think 工具为 Claude 在处理复杂问题时提供了一个专门的空间进行结构化推理，从而生成更周到、准确和可靠的响应。

## 经验证明的性能优势

Anthropic 的研究表明，在使用 "think" 工具时，有显著的改进：

- **在复杂的客户服务任务上提高了 54%**
- **更好地遵守详细的政策和指南**
- **在多次执行同一任务时增强了一致性**
- **在软件工程基准测试中表现更好**
- **与其他增强技术相比，实施开销最小**

"think" 工具在其他方法不足的地方表现出色：
- **对于需要复杂工具链的情况，优于扩展思考**
- **对于政策密集型场景，比基线提示更有效**
- **与优化后的提示结合使用时特别强大**

## 快速安装

### 对于 Claude 桌面版

```bash
npx -y @smithery/cli@latest install @PhillipRt/think-mcp-server --client claude --config "{}"
```

### 对于 Cursor

```bash
npx -y @smithery/cli@latest install @PhillipRt/think-mcp-server --client cursor --config "{}"
```

## 工作原理

"think" 工具实现了 Anthropic 工程博客中描述的确切机制。与扩展思考（在 Claude 开始响应之前发生）不同，"think" 工具允许 Claude 在响应生成过程中暂停和反思。

**关键机制：** 该工具不执行任何外部操作或检索新信息 - 它只是为 Claude 提供了一个专用的草稿本，使其能够逐步推理，从而显著提高在复杂任务上的表现。

当 Claude 使用 "think" 工具时：
1. **在继续复杂的推理链之前，它会暂停以组织思路**
2. **对多步骤问题采取结构化的方法**
3. **更彻底和一致地验证政策合规性**
4. **在决定下一步之前仔细分析工具输出**
5. **在长时间互动中保持更好的上下文意识**

### 何时使用 Think 工具

"think" 工具在以下情况下特别有价值：

1. **与其他 MCP 工具一起工作** - 非常适合分析来自数据库、文件系统或 API 的输出
2. **遵循复杂的政策** - 适用于客户服务、法律或合规情况
3. **做出顺序决策** - 适用于后续步骤依赖于先前步骤的工作流程
4. **处理网络搜索结果** - 帮助 Claude 从多个来源综合信息
5. **解决编码挑战** - 提高软件工程任务的成功率

## 用于获得最佳结果的系统提示

Anthropic 的研究表明，**将“思考”工具与优化的提示相结合可以带来最强的性能提升**。为了获得最佳效果，请在与 Claude 交互时添加以下优化系统提示：

### 对于 Claude 桌面版（自定义指令）

1. 转到设置 > 自定义指令
2. 添加以下系统提示：

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

Remember that using the think tool has been shown to improve your performance by up to 54% on complex tasks, especially when working with multiple tools or following detailed policies.
```

### 对于 Cursor（全局规则）

要将思考工具作为 Cursor 规则添加：

1. 打开 Cursor 设置
2. 导航到常规 > AI 规则
3. 添加一条新规则，内容如下：

```
After any context change (viewing new files, running commands, or receiving tool outputs), use the "mcp_think" tool to organize your reasoning before responding.

Specifically, always use the think tool when:
- After examining file contents or project structure
- After running terminal commands or analyzing their outputs
- After receiving search results or API responses
- Before making code suggestions or explaining complex concepts
- When transitioning between different parts of a task

When using the think tool:
- List the specific rules or constraints that apply to the current task
- Check if all required information is collected
- Verify that your planned approach is correct
- Break down complex problems into clearly defined steps
- Analyze outputs from other tools thoroughly
- Plan multi-step approaches before executing them

The think tool has been proven to improve performance by up to 54% on complex tasks, especially when working with multiple tools or following detailed policies.
```

## 手动安装

如果您希望在本地运行服务器：

1. **克隆仓库**：
```bash
   git clone https://github.com/PhillipRt/think-mcp-server.git
   cd think-mcp-server
```

2. **安装依赖**：
```bash
   npm install
```

3. **构建并运行**：
```bash
   npm run build
   npm start
```

4. **手动配置 Claude 桌面版**：
   - 查找或创建配置文件：
     - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
     - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
   - 添加您的服务器配置：

```json
   {
     "mcpServers": {
       "think-tool": {
         "command": "node",
         "args": ["path/to/think-mcp-server/dist/server.js"]
       }
     }
   }
```

## 许可证

MIT License

**官方网站：** [https://github.com/PhillipRt/think-mcp-server](https://github.com/PhillipRt/think-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`memory`
- 标签：`knowledge and memory`, `developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`path/to/think-mcp-server/dist/server.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/philliprt-think.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
