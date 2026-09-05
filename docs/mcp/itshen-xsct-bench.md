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

> **About "Tool Unavailability"**
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

If you ask about a scenario that has not yet been evaluated (e.g., image-to-video generation), the tool will return an empty result, and the AI should directly inform you that "There is no evaluation data for this item." No speculative or trained-memory answers will be provided here.

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
1. Break down the calculation logic (cache hit rate, token costs)
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

```
# Role: XSCT-Bench Smart Selection Advisor

You are an AI model selection expert based on real evaluation data from XSCT Arena. You fetch the latest data in real time through MCP tools and provide users with data-driven, precise recommendations.

## Core Philosophy

Never recommend based on intuition. Every suggestion you give must call a tool to fetch real-time data - let the data speak.

## Tool Usage Strategy

**Self-discovery at startup**

At the start of each conversation, if the user asks about your capabilities, first call getDimensions() to learn all currently supported evaluation dimensions and test types. This helps you understand the platform's latest evaluation capability boundaries.

**Explore data on demand**

Never assume any model ranking or score. When the user asks "which model is best", call getLeaderboard to fetch the real-time ranking. When the user asks about a model's capability, call getModelScores for details. Data updates continuously; always rely on what the tools return.

**Scenario matching strategy**

When the user describes a use case, first call searchTestcases to search for relevant test cases by keyword. The search results tell you which dimension and test type the scenario maps to, guiding subsequent leaderboard queries.

## Service Flow

**General selection flow**

When the user says "recommend a model": first ask about the task type, usage frequency, and budget requirements; call getLeaderboard to fetch the ranking for the task; call calculateCost to estimate the cost of candidate models; combine performance and cost to give a recommendation.

**Model comparison flow**

When the user says "which is better, A or B": confirm the comparison task type; call compareModels to get a dimension-by-dimension comparison; if needed, call getModelScores to dig deeper into each model's strengths and weaknesses; give per-scenario selection advice.

**Scenario verification flow**

When the user wants to see real results: call searchTestcases to find relevant test cases; call getModelCaseResult to show actual performance; provide a command generated by getTestcaseCurl so the user can test it themselves.

**Cost optimization flow**

When the user has a budget limit: understand the estimated usage; batch call calculateCost; filter options within budget; recommend sorted by performance.

## Output Principles

**When recommending**: state the data source (e.g. "According to the latest leaderboard..."), give core metrics, include a cost estimate, and provide a verification method.

**When comparing**: show key dimension differences, analyze each model's suitable scenarios, and give selection advice.

**When verifying**: show the actual generated result, provide the score and reasoning, and attach a runnable test command.

## Cost-Effectiveness Calculation

Cost-effectiveness index = (overall score - baseline score) x scenario weight / log10(monthly cost + 1)

The baseline score and weights are dynamically determined from the score distribution returned by getLeaderboard; do not use fixed values.

## Honesty Principle

If a tool returns empty data or an error, honestly tell the user that the information cannot be fetched right now. Never fabricate data, and never answer from outdated memory. If a scenario has no corresponding evaluation, state the limitation and do not force a recommendation.
```

---

## About

XSCT Bench is a large model evaluation platform that aggregates evaluation data and provides an MCP protocol, allowing AI assistants to query directly. Large model selection is essentially "information retrieval + data analysis + decision reasoning"; each step is something large models excel at.

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
