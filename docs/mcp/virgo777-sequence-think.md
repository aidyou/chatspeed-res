---
title: "sequence_think"
description: "This tool aids in problem analysis through a flexible thought process, which can adapt to changes and continuously evolve. As understanding deepens, each node of thought can supplement, question, or r…"
---

# sequence_think

This tool aids in problem analysis through a flexible thought process, which can adapt to changes and continuously evolve. As understanding deepens, each node of thought can supplement, question, or r…

# XH-Plan MCP Server

## Introduction
**Intelligent Task Planning MCP Service**  
An intelligent planning tool based on the Chain-of-Thought (CoT) technology, which generates structured travel plans through phased reasoning. It supports dynamic adjustment of the thinking path, multi-round iterative optimization, and ultimately outputs a JSON-formatted planning document containing the complete thought process, execution plan, and action steps.

## Usage Guide: Local Execution with SSE Stream Configuration
Local Input:
json
{
    "mcpServers": {
        "sequence_think": {
            "type": "sse",
            "url": "http://211.159.225.228:9002/sse"
        }
    }
}

---

## Tools

### `think_planner`
**Features**
- ✅ **Multi-stage Decomposition**: Covers all scenarios from 1-day tours to multi-day tours and themed travels
- 🔁 **Dynamic Adjustment**: Supports adding, deleting, or modifying thought nodes mid-process
- 🧪 **Hypothesis Validation**: Automatically generates alternative plans (e.g., weather contingency plans)
- 📈 **Iterative Optimization**: Refines from a rough framework to detailed execution steps

**Input Parameters**
- `query` (string): Travel requirements described in natural language
  *Default Example*: `"Nanjing one-day tour planning"`

**Output Format**
json
{
  "travel_plan": [
    {
      "step": 1,
      "description": "Planning Stage 1: Objective Analysis",
      "parameters": {
        "thought": "Analyze user's core needs",
        "plan": "Determine time frame and key attractions",
        "action": "Extract geographic location and opening hours data"
      }
    }
  ]
}

**Official site: ** [http://211.159.225.228:9002/sse](http://211.159.225.228:9002/sse)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `files`, `communication`
- Tags: `communication`, `developer tools`, `file systems`, `chinese`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/virgo777-sequence-think.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
