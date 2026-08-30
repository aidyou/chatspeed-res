---
title: "MCP虾任务管理器"
description: "MCP虾任务管理器是为AI代理构建的任务工具，强调思维链、反思和风格一致性。它将自然语言转换为具有依赖关系跟踪和迭代优化的结构化开发任务，使推理AI系统能够表现出类似代理的开发者行为。"
---

# MCP虾任务管理器

MCP虾任务管理器是为AI代理构建的任务工具，强调思维链、反思和风格一致性。它将自然语言转换为具有依赖关系跟踪和迭代优化的结构化开发任务，使推理AI系统能够表现出类似代理的开发者行为。

[English](https://github.com/cjo4m06/mcp-shrimp-task-manager/blob/HEAD/README.md) | [中文](https://github.com/cjo4m06/mcp-shrimp-task-manager/blob/HEAD/docs/zh/README.md)

# MCP 虾任务管理器

[Smithery](https://smithery.ai/server/@cjo4m06/mcp-shrimp-task-manager)

> 🚀 一个基于模型上下文协议（MCP）的智能任务管理系统，为AI代理提供高效的编程工作流框架。

  

虾任务管理器通过结构化的工作流程引导代理进行系统化的编程，增强任务内存管理机制，并有效避免冗余和重复的编码工作。

## ✨ 特性

- **任务规划与分析**：深入理解和分析复杂任务需求
- **智能任务分解**：自动将大型任务分解成可管理的小任务
- **依赖关系管理**：精确处理任务间的依赖关系，确保正确的执行顺序
- **执行状态跟踪**：实时监控任务执行进度和状态
- **任务完整性验证**：确保任务结果符合预期要求
- **任务复杂度评估**：自动评估任务复杂度并提供最佳处理建议
- **自动任务摘要更新**：任务完成后自动生成摘要，优化内存性能
- **任务记忆功能**：自动备份任务历史记录，提供长期记忆和参考能力
- **思维链过程**：逐步推理以系统地分析复杂问题
- **项目规则初始化**：定义项目标准和规则，保持大型项目的一致性

## 🔄 任务管理工作流

该系统提供了一个完整的任务管理生命周期：

1. **开始规划** `plan_task`: 分析任务问题，确定需求范围
2. **深入分析** `analyze_task`: 检查现有代码库以避免重复工作
3. **解决方案反思** `reflect_task`: 批判性地审查分析结果，确保全面的解决方案
4. **任务分解** `split_tasks`: 将复杂任务分解为较小的任务，建立清晰的依赖关系
5. **任务列表** `list_tasks`: 查看所有任务及其执行状态
6. **执行任务** `execute_task`: 在评估复杂性的同时执行特定任务
7. **结果验证** `verify_task`: 全面检查任务完成情况
8. **任务完成** `complete_task`: 标记任务为完成并生成报告，自动更新摘要
9. **任务管理** `delete_task`: 管理未完成的任务（已完成的任务仍保留在系统中）
10. **查询任务** `query_task`: 使用关键词在过去的记忆中搜索相关任务
11. **显示任务** `get_task_detail`: 显示完整的任务指导
12. **处理思路** `process_thought`: 对复杂问题进行逐步推理
13. **初始化项目规则** `init_project_rules`: 设置和维护项目标准和约定

## 🧠 任务记忆功能

虾米任务管理器具有长期记忆能力，能够自动保存任务执行历史，并在规划新任务时提供参考经验。

### 主要特点

- 系统自动将任务备份到记忆目录
- 备份文件按时间顺序命名，格式为 tasks_backup_YYYY-MM-DDThh-mm-ss.json
- 任务规划代理会自动接收如何使用记忆功能的指导

### 优势与益处

- **避免重复工作**: 参考过去任务，无需从头解决类似问题
- **借鉴成功经验**: 利用已被证明有效的解决方案，提高开发效率
- **学习与改进**: 识别过去的错误或低效解决方案，持续优化工作流程
- **知识积累**: 随着系统使用量的增加，形成不断扩大的知识库

通过有效利用任务记忆功能，系统可以不断积累经验，智能水平和工作效率不断提高。

## 🤔 思维链过程

思维链功能通过结构化思考增强问题解决能力：

- **系统推理**: 将复杂问题分解成逻辑步骤
- **假设测试**: 挑战假设以验证解决方案的方法
- **批判性分析**: 用严格的标准评估解决方案选项
- **改进决策**: 通过深思熟虑的思考得出更可靠的结论

当启用（默认设置）时，系统使用 `process_thought` 工具引导代理进行逐步推理，确保在实施前彻底分析问题。

## 📋 项目规则初始化

项目规则功能有助于保持代码库的一致性：

- **标准化开发**：建立一致的编码模式和实践
- **新开发者入门**：为项目贡献提供明确的指南
- **维护质量**：确保所有代码符合既定的项目标准

> **⚠️ 建议**：当您的项目规模变大或经历重大变更时，初始化项目规则。这有助于在复杂度增加时保持一致性和质量。

使用 `init_project_rules` 工具来设置或更新项目标准，适用于以下情况：

- 开始一个大型新项目
- 新团队成员加入
- 实施主要架构变更
- 采用新的开发约定

### 使用示例

您可以使用简单的自然语言命令轻松访问此功能：

- **初次设置**：只需告诉 Agent "init rules" 或 "init project rules"
- **更新**：当您的项目发展时，告诉 Agent "Update rules" 或 "Update project rules"

当您的代码库扩展或经历重大结构变化时，该工具特别有价值，有助于在整个项目生命周期中保持一致的开发实践。

## 📚 文档资源

- 系统架构：详细的系统设计和数据流说明
- [提示定制指南](https://github.com/cjo4m06/mcp-shrimp-task-manager/blob/HEAD/docs/en/prompt-customization.md)：通过环境变量自定义工具提示的说明
- [变更日志](https://github.com/cjo4m06/mcp-shrimp-task-manager/blob/HEAD/CHANGELOG.md)：记录该项目的所有重要变更

## 🔧 安装和使用

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@cjo4m06/mcp-shrimp-task-manager) 自动安装 Claude 桌面版的 Shrimp Task Manager：

```bash
npx -y @smithery/cli install @cjo4m06/mcp-shrimp-task-manager --client claude
```

### 手动安装

```bash
# Install dependencies
npm install

# Build and start service
npm run build
```

## 🔌 与 MCP 兼容客户端一起使用

Shrimp Task Manager 可以与任何支持模型上下文协议 (Model Context Protocol) 的客户端一起使用，例如 Cursor IDE。

### 在 Cursor IDE 中配置

Shrimp Task Manager 提供两种配置方法：全局配置和项目特定配置。

#### 全局配置

1. 打开 Cursor IDE 的全局配置文件（通常位于 `~/.cursor/mcp.json`）
2. 在 `mcpServers` 部分添加以下配置：

```json
{
  "mcpServers": {
    "shrimp-task-manager": {
      "command": "node",
      "args": ["/mcp-shrimp-task-manager/dist/index.js"],
      "env": {
        "DATA_DIR": "/path/to/project/data" // 必須使用絕對路徑
      }
    }
  }
}

or

{
  "mcpServers": {
    "shrimp-task-manager": {
      "command": "npx",
      "args": ["mcp-shrimp-task-manager"],
      "env": {
        "DATA_DIR": "/mcp-shrimp-task-manager/data"
      }
    }
  }
}
```

> ⚠️ 请将 `/mcp-shrimp-task-manager` 替换为您的实际路径。

#### 项目特定配置

您还可以为每个项目设置专用配置，以便为不同的项目使用独立的数据目录：

1. 在项目根目录下创建一个 `.cursor` 目录
2. 在此目录中创建一个 `mcp.json` 文件，并添加以下内容：

```json
{
  "mcpServers": {
    "shrimp-task-manager": {
      "command": "node",
      "args": ["/path/to/mcp-shrimp-task-manager/dist/index.js"],
      "env": {
        "DATA_DIR": "/path/to/project/data" // Must use absolute path
      }
    }
  }
}

or

{
  "mcpServers": {
    "shrimp-task-manager": {
      "command": "npx",
      "args": ["mcp-shrimp-task-manager"],
      "env": {
        "DATA_DIR": "/path/to/project/data" // 必須使用絕對路徑
      }
    }
  }
}
```

### ⚠️ 重要的配置注意事项

**DATA_DIR 参数**是 Shrimp 任务管理器存储任务数据、对话日志和其他信息的目录。正确设置此参数对于系统的正常运行至关重要。该参数必须使用**绝对路径**；使用相对路径可能导致系统错误地定位数据目录，从而导致数据丢失或功能失败。

> **警告**：使用相对路径可能会导致以下问题：
>
> - 数据文件未找到，导致系统初始化失败
> - 任务状态丢失或无法正确保存
> - 不同环境下应用程序行为不一致
> - 系统崩溃或无法启动

### 🔧 环境变量配置

Shrimp 任务管理器支持通过环境变量自定义提示行为，允许您在不修改代码的情况下微调 AI 助手的响应。您可以在配置中或通过 `.env` 文件设置这些变量：

```json
{
  "mcpServers": {
    "shrimp-task-manager": {
      "command": "node",
      "args": ["/path/to/mcp-shrimp-task-manager/dist/index.js"],
      "env": {
        "DATA_DIR": "/path/to/project/data",
        "MCP_PROMPT_PLAN_TASK": "Custom planning guidance...",
        "MCP_PROMPT_EXECUTE_TASK_APPEND": "Additional execution instructions...",
        "ENABLE_THOUGHT_CHAIN": "true"
      }
    }
  }
}
```

有两种自定义方法：

- **覆盖模式** (`MCP_PROMPT_[FUNCTION_NAME]`)：完全替换默认提示
- **追加模式** (`MCP_PROMPT_[FUNCTION_NAME]_APPEND`)：向现有提示添加内容

此外，还有其他系统配置变量：

- **DATA_DIR**：指定任务数据存储的目录
- **ENABLE_THOUGHT_CHAIN**：控制任务规划工作流中的思考模型。当设置为 `true`（默认值）时，系统引导用户使用 `process_thought` 工具进行逐步推理。当设置为 `false` 时，系统直接使用 `analyze_task` 提交分析结果，跳过详细的思考过程。

有关自定义提示的详细说明，包括支持的参数和示例，请参阅 [Prompt Customization Guide](https://github.com/cjo4m06/mcp-shrimp-task-manager/blob/HEAD/docs/en/prompt-customization.md)。

## 💡 系统提示指南

### Cursor IDE 配置

您可以启用 Cursor 设置 => 功能 => 自定义模式，并配置以下两种模式：

#### TaskPlanner 模式

```
You are a professional task planning expert. You must interact with users, analyze their needs, and collect project-related information. Finally, you must use "plan_task" to create tasks. When the task is created, you must summarize it and inform the user to use the "TaskExecutor" mode to execute the task.
You must focus on task planning. Do not use "execute_task" to execute tasks.
Serious warning: you are a task planning expert, you cannot modify the program code directly, you can only plan tasks, and you cannot modify the program code directly, you can only plan tasks.
```

#### TaskExecutor 模式

```
You are a professional task execution expert. When a user specifies a task to execute, use "execute_task" to execute the task.
If no task is specified, use "list_tasks" to find unexecuted tasks and execute them.
When the execution is completed, a summary must be given to inform the user of the conclusion.
You can only perform one task at a time, and when a task is completed, you are prohibited from performing the next task unless the user explicitly tells you to.
If the user requests "continuous mode", all tasks will be executed in sequence.
```

> 💡 根据需要选择合适的模式：
>
> - 在规划任务时使用 **TaskPlanner** 模式
> - 在执行任务时使用 **TaskExecutor** 模式

### 与其他工具一起使用

如果您的工具不支持自定义模式，您可以：

- 在不同阶段手动粘贴适当的提示
- 或者直接使用简单的命令，如 `请规划以下任务：......` 或 `请开始执行任务...`

## 🛠️ 可用工具概览

配置完成后，您可以使用以下工具：

| 类别                | 工具名称            | 描述                                      |
| ----------------------- | -------------------- | ------------------------------------------------ |
| **任务规划**       | `plan_task`          | 开始规划任务                             |
| **任务分析**       | `analyze_task`       | 深入分析任务需求           |
|                         | `process_thought`    | 逐步推理解决复杂问题      |
| **解决方案评估** | `reflect_task`       | 反思并改进解决方案概念            |
| **项目管理**  | `init_project_rules` | 初始化或更新项目标准和规则 |
| **任务管理**     | `split_tasks`        | 将任务分解为子任务                        |
|                         | `list_tasks`         | 显示所有任务及其状态                     |
|                         | `query_task`         | 搜索并列出任务                            |
|                         | `get_task_detail`    | 显示完整的任务详情                    |
|                         | `delete_task`        | 删除未完成的任务                          |
| **任务执行**      | `execute_task`       | 执行特定任务                           |
|                         | `verify_task`        | 验证任务完成情况                           |
|                         | `complete_task`      | 标记任务为已完成                          |

## 🔧 技术实现

- **Node.js**: 高性能的 JavaScript 运行环境
- **TypeScript**: 提供类型安全的开发环境
- **MCP SDK**: 与大型语言模型无缝交互的接口
- **UUID**: 生成唯一且可靠的任务标识符

## 📄 许可证

本项目采用 MIT 许可证发布

**官方网站：** [https://github.com/cjo4m06/mcp-shrimp-task-manager](https://github.com/cjo4m06/mcp-shrimp-task-manager)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`memory`
- 标签：`developer tools`, `knowledge and memory`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`/path/to/mcp-shrimp-task-manager/dist/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/cjo4m06-shrimp-task-manager.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
