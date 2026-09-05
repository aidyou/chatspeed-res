---
title: "math_genie_calc"
description: "math\\genie\\calc mathgeniecalc是一款专注于科学计算的 Python 应用，为用户提供便捷、准确的各类数学运算功能，涵盖了基础运算到复杂三角函数等多种计算需求，适合学生、科研人员以及任何需要进行数学计算的场景使用。 主要功能 基础运算 加法：实现两个及多个数字的相加运算，支持整数、浮点数等多种数值类型。 减法：进行数字间的减法操作，可处理正数与负数的运算。 乘法：完成数字…"
---

# math_genie_calc

math\genie\calc mathgeniecalc是一款专注于科学计算的 Python 应用，为用户提供便捷、准确的各类数学运算功能，涵盖了基础运算到复杂三角函数等多种计算需求，适合学生、科研人员以及任何需要进行数学计算的场景使用。 主要功能 基础运算 加法：实现两个及多个数字的相加运算，支持整数、浮点数等多种数值类型。 减法：进行数字间的减法操作，可处理正数与负数的运算。 乘法：完成数字…

# math\_genie\_calc

`math_genie_calc`是一款专注于科学计算的 Python 应用，为用户提供便捷、准确的各类数学运算功能，涵盖了基础运算到复杂三角函数等多种计算需求，适合学生、科研人员以及任何需要进行数学计算的场景使用。

## 主要功能

### 基础运算

*   **加法**：实现两个及多个数字的相加运算，支持整数、浮点数等多种数值类型。
*   **减法**：进行数字间的减法操作，可处理正数与负数的运算。
*   **乘法**：完成数字的乘法计算，包括多位数相乘。
*   **除法**：支持除法运算，同时会对除数为 0 的情况进行处理，避免程序错误。

### 三角函数计算

*   提供正弦（sin）、余弦（cos）、正切（tan）函数的计算，输入参数为弧度值。
*   支持余切（cot）、正割（sec）、余割（csc）函数的计算，通过相应三角函数的倒数推导得出，同样以弧度为输入单位。

### 其他运算

*   **幂运算**：能够计算一个数的任意次幂，包括整数幂、小数幂等。
*   **平方根**：可对非负数字进行平方根计算，返回精确的结果。
*   **阶乘**：计算非负整数的阶乘，0 的阶乘为 1，对于较大的整数也能准确处理。

## 安装方法

你可以通过 PyPI 来安装`math_genie_calc`，使用以下命令：

bash
pip install math_genie_calc

## 使用示例

bash
npx @modelcontextprotocol/inspector uvx math_genie_calc

## MCP 服务器配置

json
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
