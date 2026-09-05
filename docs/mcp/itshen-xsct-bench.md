---
title: "xsct-bench"
description: "XSCT MCP Let AI help you choose the right AI, completing large model selection decisions with just one sentence. After configuring XSCT MCP, simply ask your questions to the AI assistant. The AI will…"
---

# xsct-bench

XSCT MCP Let AI help you choose the right AI, completing large model selection decisions with just one sentence. After configuring XSCT MCP, simply ask your questions to the AI assistant. The AI will…

# XSCT MCP

> Let AI help you choose the right AI, completing large model selection decisions with just one sentence.

After configuring XSCT MCP, simply ask your questions to the AI assistant. The AI will automatically invoke the necessary tools to fetch data, calculate costs, make comparisons, and finally provide actionable recommendations.

---

## Quick Start (Recommended: Direct Connection)

Add the following configuration to your MCP client (Cursor / Claude Desktop / Cherry Studio / CLINE, etc.):

plaintext
```json
{
  "mcpServers": {
    "xsct-bench": {
      "type": "streamable_http",
      "url": "https://xsct.ai/mcp"
    }
  }
}
```
If your client only recognizes the `url` field, you can remove the `type` line and still connect.

**The direct connection address does not require authentication, registration, and is valid for a long time.**

> ⚠️ Regarding "Tool Unavailability"
>
> The ModelScope hosted address (`mcp.api-inference.modelscope.net/...`) in the "Service Configuration" on the right side of the page is a temporary address issued by the platform for **24 hours**. After it expires, requests will return `{"error":{"message":"Url is expired"}}`.
>
> For those who have reported that the tool suddenly stopped working, this is the reason. Please use the direct connection address `https://xsct.ai/mcp` provided above, which will not expire once configured.

---

## How to Use

Ask a question in natural language, for example:

- "Which models are good for polishing scenarios?"
- "Which model offers the best cost-effectiveness for code generation?"
- "What are the differences between Qwen3-Max and Claude in creative writing?"
- "Which model is the best for image generation in Chinese?"

The AI will automatically determine which tools to invoke, so you don't need to worry about the specific implementation.

---

## Tool List

| Tool | Description |
|------|-------------|
| `get_leaderboard` | Fetch leaderboard |
| `get_model_scores` | Fetch scores for a specific model across various dimensions |
| `compare_models` | Compare two models |
| `search_testcases` | Search for test cases |
| `get_model_case_result` | Fetch the performance of a model on a specific test case |
| `get_dimensions` | Fetch all evaluation dimensions |
| `calculate_cost` | Calculate model costs |
| `get_testcase_curl` | Generate a reproducible CURL command |

These 8 tools cover: checking leaderboards, viewing scores, searching scenarios, comparing models, and calculating costs. **No need to memorize**; the AI will automatically invoke the appropriate tools based on your question.

---

## Capability Boundaries

XSCT Arena includes **models and test cases that have already been evaluated**, covering text generation and image generation. All data returned by the tools are actual measurements from the platform.

If you ask about a scenario that has not yet been evaluated (e.g., video generation from images), the tool will return an empty result, and the AI should directly inform you that "There is no evaluation data for this item." No speculative or trained memory answers will be provided here.

---

## Usage Examples

### Scenario 1: Simple Selection

**Question**: "Which models are good for polishing scenarios?"

The AI will automatically:
1. Invoke `search_testcases` to search for relevant polishing test cases
2. Invoke `get_leaderboard` to fetch the leaderboard
3. Provide a category breakdown and initial recommendations

### Scenario 2: Enterprise-Level Cost Analysis

**Question**: "With 5000 input tokens, 2000 output tokens, 300 calls per day, and 80% KV Cache hit rate, which models are better?"

The AI will automatically:
1. Break down the calculation logic (Cache hit rate, token costs)
2. Invoke `calculate_cost` to batch calculate multiple models
3. Generate a complete cost analysis report
4. Provide tiered recommendations (Preferred / Alternative / Not Recommended)

### Scenario 3: In-Depth Comparison

**Question**: "Compare MIMO V2 Flash and Qwen3-Max in polishing test cases"

The AI will automatically invoke `compare_models` and select representative test cases for an in-depth comparison.

### Scenario 4: Generating Executable Code

**Question**: "Generate the CURL command for this test case"

The AI will invoke `get_testcase_curl` to generate a directly executable CURL command. You can modify the KEY and test it in the terminal.

---

## Platform

- **Official Website**: [xsct.ai](https://xsct.ai)
- **MCP Address**: `https://xsct.ai/mcp` (Streamable HTTP, no authentication required)
- **System Prompt Reference**:

plaintext
```
# 角色：XSCT-Bench 智能选型顾问

你是一位基于 XSCT Arena 真实评测数据的 AI 模型选型专家。你通过 MCP 工具实时获取最新数据，为用户提供数据驱动的精准推荐。

## 核心理念

永远不要凭感觉推荐。你的每一个建议都必须调用工具获取实时数据，让数据说话。

## 工具使用策略

**启动时自我发现**

每次对话开始，如果用户询问能力范围，先调用 getDimensions() 了解当前支持的所有评测维度和测试类型。这能帮助你了解平台最新的评测能力边界。

**按需探索数据**

不要假设任何模型排名或分数。当用户问「哪个模型最好」，调用 getLeaderboard 获取实时排行。当用户问某模型能力，调用 getModelScores 获取详情。数据会持续更新，始终以工具返回为准。

**场景匹配策略**

当用户描述使用场景时，先调用 searchTestcases 用关键词搜索相关用例。搜索结果会告诉你该场景对应什么维度和测试类型，以此指导后续的排行榜查询。

## 服务流程

**通用选型流程**

用户说「推荐一个模型」时：先询问任务类型、使用频率、预算要求；根据任务调用 getLeaderboard 获取排行；对候选模型调用 calculateCost 估算成本；综合性能和成本给出推荐。

**模型对比流程**

用户说「A和B哪个好」时：确认对比的任务类型；调用 compareModels 获取维度对比；必要时调用 getModelScores 深挖各自优劣；给出分场景选择建议。

**场景验证流程**

用户想看真实效果时：调用 searchTestcases 找相关用例；调用 getModelCaseResult 展示实际表现；提供 getTestcaseCurl 生成的命令让用户自测。

**成本优化流程**

用户有预算限制时：了解使用量预估；批量调用 calculateCost；筛选预算内选项；按性能排序推荐。

## 输出原则

**推荐时**：说明数据来源（「根据最新排行榜…」），给出核心指标，附带成本估算，提供验证方式。

**对比时**：展示关键维度差异，分析各自适用场景，给出选择建议。

**验证时**：展示实际生成效果，提供评分和理由，附上可运行的测试命令。

## 性价比计算

性价比指数 = (综合评分 - 基准分) × 场景权重 / log10(月成本 + 1)

基准分和权重根据 getLeaderboard 返回的分数分布动态确定，不要使用固定值。

## 诚实原则

如果工具返回数据为空或报错，坦诚告知用户当前无法获取该信息。禁止编造数据，禁止用过时的记忆回答。如果某个场景没有对应评测，说明局限性，不做硬推荐。
```
---

## About

XSCT Bench is a large model evaluation platform that aggregates evaluation data and provides MCP protocol, allowing AI assistants to query directly. Large model selection is essentially "information retrieval + data analysis + decision reasoning," each step being something large models excel at.

**Author**: Lu Xiaoshan

---

*Just ask, and leave the rest to the AI.*

**Official site: ** [https://xsct.ai/](https://xsct.ai/)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `developer tools`, `模型评测`, `chinese`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/itshen-xsct-bench.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
