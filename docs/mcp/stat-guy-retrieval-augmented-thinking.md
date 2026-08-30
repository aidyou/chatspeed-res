---
title: "检索增强思维"
description: "通过结构化的、带有检索增强的思维过程来提升人工智能模型的能力，这些过程能够实现动态思维链、并行探索路径以及递归精化周期，从而改善推理能力。"
---

# 检索增强思维

通过结构化的、带有检索增强的思维过程来提升人工智能模型的能力，这些过程能够实现动态思维链、并行探索路径以及递归精化周期，从而改善推理能力。

# 检索增强思维 MCP 服务器

这是一个实现了结构化、检索增强思维过程的MCP（模型上下文协议）服务器。该服务器能够支持动态思维链、并行探索路径以及递归改进周期，以提高推理和解决问题的能力。

## 特性

- **自适应思维链**：保持连贯的推理流程，并具有分支和修订能力
- **迭代假设生成**：实施假设测试的验证周期
- **上下文一致性**：在非线性推理路径上保持上下文的一致性
- **动态范围调整**：支持灵活的探索与细化
- **质量评估**：实时评估思维过程
- **分支管理**：处理并行探索路径
- **修订追踪**：管理递归改进周期

## 安装

```bash
npm install @modelcontextprotocol/server-retrieval-augmented-thinking
```

## 使用方法

### 命令行

```bash
mcp-server-retrieval-augmented-thinking
```

### 编程使用

```typescript
import { Server } from '@modelcontextprotocol/sdk/server';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio';

// Initialize and run the server
const server = new Server({
  name: 'retrieval-augmented-thinking',
  version: '0.1.0'
});

// Connect transport
const transport = new StdioServerTransport();
await server.connect(transport);
```

## 工具配置

服务器提供了一个工具，包含以下参数：

- `thought` (字符串)：当前推理步骤
- `thoughtNumber` (数字)：在推理链中的位置
- `totalThoughts` (数字)：估计范围
- `nextThoughtNeeded` (布尔值)：链继续信号
- `isRevision` (布尔值, 可选)：标记改进步骤
- `revisesThought` (数字, 可选)：引用目标思想
- `branchFromThought` (数字, 可选)：分支起点
- `branchId` (字符串, 可选)：分支标识符
- `needsMoreThoughts` (布尔值, 可选)：范围扩展信号

## 高级特性

### 思维链分析

服务器跟踪各种指标来评估思维链的质量：

- 链条有效性
- 修订影响
- 分支成功率
- 整体质量
- 单个思维度量（复杂性、深度、质量、影响）

### 模式识别

分析思维模式以实现：

- 推理结构
- 上下文保存
- 假设验证
- 解决方案一致性

## 开发

```bash
# Build
npm run build

# Watch mode
npm run watch
```

## 贡献

欢迎贡献！请阅读我们的贡献指南并提交拉取请求。

## 许可证

MIT

**官方网站：** [https://github.com/stat-guy/retrieval-augmented-thinking](https://github.com/stat-guy/retrieval-augmented-thinking)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`memory`, `data`
- 标签：`knowledge and memory`, `research and data`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`mcp-server-rat-node`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/stat-guy-retrieval-augmented-thinking.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
