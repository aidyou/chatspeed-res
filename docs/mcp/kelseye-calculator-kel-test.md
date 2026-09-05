---
title: "mcp_calculator_kel_test"
description: "计算器 MCP 基于 Model Context Protocol (MCP) 的数值计算器，提供了简单的加减乘除、幂运算、平方根运算和整数阶乘运算。 工具列表 | name | description | | ----------- | ----------- | | add | 执行浮点数加法运算 | | subtract | 执行浮点数减法运算 | | multiply | 执行浮点数乘法运…"
---

# mcp_calculator_kel_test

计算器 MCP 基于 Model Context Protocol (MCP) 的数值计算器，提供了简单的加减乘除、幂运算、平方根运算和整数阶乘运算。 工具列表 | name | description | | ----------- | ----------- | | add | 执行浮点数加法运算 | | subtract | 执行浮点数减法运算 | | multiply | 执行浮点数乘法运…

## Calculator MCP
A numerical calculator based on the Model Context Protocol (MCP), providing simple operations such as addition, subtraction, multiplication, division, power, square root, and integer factorial.

## Tool List
| name | description |
| ----------- | ----------- |
| add  | Performs floating-point addition |
| subtract | Performs floating-point subtraction |
| multiply | Performs floating-point multiplication |
| divide | Performs floating-point division. Args: b: divisor (must be non-zero) |
| power | Calculates exponentiation |
| sqrt | Calculates square root |
| factorial | Calculates the factorial of an integer |

## Inspector

npx @modelcontextprotocol/inspector uvx mcp_calculator_kel

## MCP Server Configuration

{
    "mcpServers": {
      "mcp_calculator_kel": {
          "command": "uvx",
          "args": [
            "mcp-calculator"
          ]
        }
    }
}

**Official site: ** [https://github.com/kelseyee/mcp_calculator_kel](https://github.com/kelseyee/mcp_calculator_kel)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `developer tools`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `mcp-calculator-kel@latest`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/kelseye-calculator-kel-test.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
