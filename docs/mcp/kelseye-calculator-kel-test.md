---
title: "科学计算器_kel"
description: "基于Model Context Protocol (MCP)的数值计算器，提供了简单的加减乘除、幂运算、平方根运算和整数阶乘运算。"
---

# 科学计算器_kel

基于Model Context Protocol (MCP)的数值计算器，提供了简单的加减乘除、幂运算、平方根运算和整数阶乘运算。

## 计算器 MCP
基于模型上下文协议（MCP）的数值计算器，提供加法、减法、乘法、除法、幂运算、平方根和整数阶乘等简单运算。

## 工具列表
| 名称 | 描述 |
| ----------- | ----------- |
| add  | 执行浮点数加法 |
| subtract | 执行浮点数减法 |
| multiply | 执行浮点数乘法 |
| divide | 执行浮点数除法。参数：b: 除数（必须非零） |
| power | 计算指数 |
| sqrt | 计算平方根 |
| factorial | 计算整数的阶乘 |

## 检查器

npx @modelcontextprotocol/inspector uvx mcp_calculator_kel

## MCP 服务器配置

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

**官方网站：** [https://github.com/kelseyee/mcp_calculator_kel](https://github.com/kelseyee/mcp_calculator_kel)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`mcp-calculator-kel@latest`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/kelseye-calculator-kel-test.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
