---
title: "深度思考推理工具"
description: "促进使用DeepSeek进行详细分析的两阶段推理过程，并支持多种响应模型，例如Claude 3.5、Sonnet和OpenRouter，保持对话上下文并增强人工智能驱动的交互。"
---

# 深度思考推理工具

促进使用DeepSeek进行详细分析的两阶段推理过程，并支持多种响应模型，例如Claude 3.5、Sonnet和OpenRouter，保持对话上下文并增强人工智能驱动的交互。

# Deepseek-Thinking-Claude-3.5-Sonnet-CLINE-MCP

[Smithery](https://smithery.ai/server/@newideas99/Deepseek-Thinking-Claude-3.5-Sonnet-CLINE-MCP)

这是一个模型上下文协议（MCP）服务器，它通过OpenRouter结合了DeepSeek R1的推理能力和Claude 3.5 Sonnet的响应生成能力。此实现使用两阶段处理过程，其中DeepSeek提供结构化的推理，然后将其整合到Claude的响应生成中。

## 功能

- **两阶段处理**：
  - 使用DeepSeek R1进行初始推理（50k字符上下文）
  - 使用Claude 3.5 Sonnet生成最终响应（600k字符上下文）
  - 通过OpenRouter的统一API访问两个模型
  - 将DeepSeek的推理令牌注入Claude的上下文中

- **智能对话管理**：
  - 通过文件修改时间检测活动对话
  - 处理多个并发对话
  - 自动过滤已结束的对话
  - 在需要时支持清除上下文

- **优化参数**：
  - 模型特定的上下文限制：
    * DeepSeek：50,000个字符用于集中推理
    * Claude：600,000个字符用于全面响应
  - 推荐设置：
    * temperature: 0.7 以平衡创造力
    * top_p: 1.0 以使用完整的概率分布
    * repetition_penalty: 1.0 以防重复

## 安装

### 通过Smithery安装

要通过[Smithery](https://smithery.ai/server/@newideas99/Deepseek-Thinking-Claude-3.5-Sonnet-CLINE-MCP)自动为Claude Desktop安装DeepSeek Thinking with Claude 3.5 Sonnet：

```bash
npx -y @smithery/cli install @newideas99/Deepseek-Thinking-Claude-3.5-Sonnet-CLINE-MCP --client claude
```

### 手动安装
1. 克隆仓库：
```bash
git clone https://github.com/yourusername/Deepseek-Thinking-Claude-3.5-Sonnet-CLINE-MCP.git
cd Deepseek-Thinking-Claude-3.5-Sonnet-CLINE-MCP
```

2. 安装依赖项：
```bash
npm install
```

3. 创建一个包含您的OpenRouter API密钥的`.env`文件：
```env
# Required: OpenRouter API key for both DeepSeek and Claude models
OPENROUTER_API_KEY=your_openrouter_api_key_here

# Optional: Model configuration (defaults shown below)
DEEPSEEK_MODEL=deepseek/deepseek-r1  # DeepSeek model for reasoning
CLAUDE_MODEL=anthropic/claude-3.5-sonnet:beta  # Claude model for responses
```

4. 构建服务器：
```bash
npm run build
```

## 与Cline一起使用

将以下内容添加到您的Cline MCP设置中（通常在`~/.vscode/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`）：

```json
{
  "mcpServers": {
    "deepseek-claude": {
      "command": "/path/to/node",
      "args": ["/path/to/Deepseek-Thinking-Claude-3.5-Sonnet-CLINE-MCP/build/index.js"],
      "env": {
        "OPENROUTER_API_KEY": "your_key_here"
      },
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

## 工具使用

服务器提供了两个工具用于生成和监控响应：

### generate_response

主要工具，用于生成响应，具有以下参数：

```typescript
{
  "prompt": string,           // Required: The question or prompt
  "showReasoning"?: boolean, // Optional: Show DeepSeek's reasoning process
  "clearContext"?: boolean,  // Optional: Clear conversation history
  "includeHistory"?: boolean // Optional: Include Cline conversation history
}
```

### check_response_status

用于检查响应生成任务状态的工具：

```typescript
{
  "taskId": string  // Required: The task ID from generate_response
}
```

### 响应轮询

服务器使用轮询机制来处理长时间运行的请求：

1. 初始请求：
   - `generate_response`立即返回一个任务ID
   - 响应格式：`{"taskId": "uuid-here"}`

2. 状态检查：
   - 使用`check_response_status`轮询任务状态
   - **注意：** 响应可能需要最多60秒才能完成
   - 状态依次经过：pending → reasoning → responding → complete

在Cline中的示例用法：
```typescript
// Initial request
const result = await use_mcp_tool({
  server_name: "deepseek-claude",
  tool_name: "generate_response",
  arguments: {
    prompt: "What is quantum computing?",
    showReasoning: true
  }
});

// Get taskId from result
const taskId = JSON.parse(result.content[0].text).taskId;

// Poll for status (may need multiple checks over ~60 seconds)
const status = await use_mcp_tool({
  server_name: "deepseek-claude",
  tool_name: "check_response_status",
  arguments: { taskId }
});

// Example status response when complete:
{
  "status": "complete",
  "reasoning": "...",  // If showReasoning was true
  "response": "..."    // The final response
}
```

## 开发

对于带有自动重建功能的开发：
```bash
npm run watch
```

## 工作原理

1. **推理阶段（DeepSeek R1）**:
   - 使用 OpenRouter 的推理令牌功能
   - 提示被修改为在捕获推理时输出 'done'
   - 从响应元数据中提取推理

2. **响应阶段（Claude 3.5 Sonnet）**:
   - 接收原始提示和 DeepSeek 的推理
   - 生成包含推理的最终响应
   - 维护对话上下文和历史记录

## 许可证

MIT 许可证 - 详情请参阅 LICENSE 文件。

## 致谢

基于 [Skirano](https://x.com/skirano/status/1881922469411643413) 提出的 RAT（检索增强思考）概念，该概念通过结构化推理和知识检索来增强 AI 响应。

此实现特别结合了 DeepSeek R1 的推理能力和 Claude 3.5 Sonnet 的响应生成能力，通过 OpenRouter 的统一 API 实现。

**官方网站：** [https://github.com/newideas99/RAT-retrieval-augmented-thinking-MCP](https://github.com/newideas99/RAT-retrieval-augmented-thinking-MCP)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`productivity`
- 标签：`other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`/path/to/node`
- 参数：`/path/to/Deepseek-Thinking-Claude-3.5-Sonnet-CLINE-MCP/build/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/newideas99-deepseek-thinking-claude-3-5-sonnet-cline.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
