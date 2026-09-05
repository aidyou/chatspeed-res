---
title: "math_genie_calc"
description: "mathgeniecalc is a Python application focused on scientific calculation, providing users with convenient and accurate mathematical operations covering everything from basic arithmetic to complex trigo…"
---

# math_genie_calc

mathgeniecalc is a Python application focused on scientific calculation, providing users with convenient and accurate mathematical operations covering everything from basic arithmetic to complex trigo…

# math_genie_calc

`math_genie_calc` is a Python application focused on scientific calculation, providing users with convenient and accurate mathematical operations covering everything from basic arithmetic to complex trigonometric functions. It is suitable for students, researchers, and anyone who needs to perform mathematical calculations.

## Main Features

### Basic Operations

* **Addition**: adds two or more numbers, supporting integers, floats, and other numeric types.
* **Subtraction**: subtracts numbers, handling both positive and negative values.
* **Multiplication**: multiplies numbers, including multi-digit multiplication.
* **Division**: supports division and handles division-by-zero cases to avoid program errors.

### Trigonometric Functions

* Provides sine (sin), cosine (cos), and tangent (tan) calculations with radian input.
* Supports cotangent (cot), secant (sec), and cosecant (csc), derived from the reciprocals of the corresponding trigonometric functions, also with radian input.

### Other Operations

* **Exponentiation**: computes any power of a number, including integer and fractional powers.
* **Square root**: computes the square root of non-negative numbers with accurate results.
* **Factorial**: computes the factorial of non-negative integers, where 0! = 1, and handles large integers accurately.

## Installation

You can install `math_genie_calc` via PyPI with the following command:

```bash
pip install math_genie_calc
```

## Usage Example

```bash
npx @modelcontextprotocol/inspector uvx math_genie_calc
```

## MCP Server Configuration

```json
{
  "mcpServers": {
    "math_genie_calc": {
      "command": "uvx",
      "args": [
        "math_genie_calc@latest"
      ]
    }
  }
}
```

**Official site: ** [https://github.com/myailab/math_genie_calc_mcp_server](https://github.com/myailab/math_genie_calc_mcp_server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `communication`
- Tags: `developer tools`, `communication`, `计算器`, `数学`, `辅助工具`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `math_genie_calc@latest`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/stormcloud-math-genie-calc.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
