---
title: "Sequential Thinking"
description: "一种MCP服务器实现，它通过结构化的思维过程提供了一种动态且反射性的解决问题的工具。"
---

# Sequential Thinking

一种MCP服务器实现，它通过结构化的思维过程提供了一种动态且反射性的解决问题的工具。

# 顺序思维 MCP 服务器

一个提供通过结构化思维过程进行动态和反思性问题解决的工具的MCP服务器实现。

## 特性

- 将复杂问题分解为可管理的步骤
- 随着理解的深入修订和完善想法
- 分支到不同的推理路径
- 动态调整总思考次数
- 生成并验证解决方案假设

## 工具

### sequential_thinking

促进详细、逐步的问题解决和分析思维过程。

**输入：**
- `thought` (字符串)：当前思考步骤
- `nextThoughtNeeded` (布尔值)：是否需要另一个思考步骤
- `thoughtNumber` (整数)：当前思考编号
- `totalThoughts` (整数)：估计所需的总思考次数
- `isRevision` (布尔值, 可选)：这是否是对先前思考的修订
- `revisesThought` (整数, 可选)：正在重新考虑哪个思考
- `branchFromThought` (整数, 可选)：分支点思考编号
- `branchId` (字符串, 可选)：分支标识符
- `needsMoreThoughts` (布尔值, 可选)：是否需要更多思考

## 使用

顺序思维工具设计用于：
- 将复杂问题分解为步骤
- 具有修订空间的规划和设计
- 可能需要修正路线的分析
- 初始时可能不清楚全部范围的问题
- 需要在多个步骤中保持上下文的任务
- 需要过滤掉无关信息的情况

## 配置

### 与 Claude 桌面版一起使用

将以下内容添加到您的 `claude_desktop_config.json` 文件中：

#### npx

```json

{

  "mcpServers": {

    "sequential-thinking": {

      "command": "npx",

      "args": [

        "-y",

        "@modelcontextprotocol/server-sequential-thinking"

      ]

    }

  }

}

```
#### docker

```json

{

  "mcpServers": {

    "sequentialthinking": {

      "command": "docker",

      "args": [

        "run",

        "--rm",

        "-i",

        "mcp/sequentialthinking"

      ]

    }

  }

}

```
要禁用思考信息的日志记录，请设置环境变量 `DISABLE_THOUGHT_LOGGING` 为 `true`。

### 与 VS Code 一起使用

快速安装请点击下面的安装按钮之一...

[![使用 NPX 在 VS Code 中安装](/mcp-assets/820599078c9a33253e497cdff7a6f7f7.svg)](https://insiders.vscode.dev/redirect/mcp/install?name=sequentialthinking&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40modelcontextprotocol%2Fserver-sequential-thinking%22%5D%7D) [![使用 NPX 在 VS Code Insiders 中安装](/mcp-assets/5bede1abbb096ca971f89cdd95154d42.svg)](https://insiders.vscode.dev/redirect/mcp/install?name=sequentialthinking&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40modelcontextprotocol%2Fserver-sequential-thinking%22%5D%7D&quality=insiders)

[![使用 Docker 在 VS Code 中安装](/mcp-assets/615447f368859665ebd2f40a2de6e777.svg)](https://insiders.vscode.dev/redirect/mcp/install?name=sequentialthinking&config=%7B%22command%22%3A%22docker%22%2C%22args%22%3A%5B%22run%22%2C%22--rm%22%2C%22-i%22%2C%22mcp%2Fsequentialthinking%22%5D%7D) [![使用 Docker 在 VS Code Insiders 中安装](/mcp-assets/49320713ff1e41ecebdc5836428df687.svg)](https://insiders.vscode.dev/redirect/mcp/install?name=sequentialthinking&config=%7B%22command%22%3A%22docker%22%2C%22args%22%3A%5B%22run%22%2C%22--rm%22%2C%22-i%22%2C%22mcp%2Fsequentialthinking%22%5D%7D&quality=insiders)

对于手动安装，您可以使用以下方法之一配置MCP服务器：

**方法1：用户配置（推荐）**
将配置添加到您的用户级MCP配置文件。打开命令面板 (`Ctrl + Shift + P`) 并运行 `MCP: 打开用户配置`。这将打开您的用户 `mcp.json` 文件，在其中可以添加服务器配置。

**方法2：工作区配置**
或者，您可以在工作区中的 `.vscode/mcp.json` 文件中添加配置。这样可以让您与他人共享配置。

> 有关在VS Code中配置MCP的更多详细信息，请参阅 [官方VS Code MCP文档](https://code.visualstudio.com/docs/copilot/mcp)。

对于NPX安装：

```json

{

  "servers": {

    "sequential-thinking": {

      "command": "npx",

      "args": [

        "-y",

        "@modelcontextprotocol/server-sequential-thinking"

      ]

    }

  }

}

```
对于Docker安装：

```json

{

  "servers": {

    "sequential-thinking": {

      "command": "docker",

      "args": [

        "run",

        "--rm",

        "-i",

        "mcp/sequentialthinking"

      ]

    }

  }

}

```
## 构建

Docker:

```bash

docker build -t mcp/sequentialthinking -f src/sequentialthinking/Dockerfile .

```
## 许可证此MCP服务器根据MIT许可证授权。这意味着您可以在遵守MIT许可证的条款和条件的前提下自由使用、修改和分发该软件。有关更多详细信息，请参阅项目仓库中的LICENSE文件。

**官方网站：** [https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`research and data`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @modelcontextprotocol/server-sequential-thinking`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/modelcontextprotocol-sequentialthinking.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
