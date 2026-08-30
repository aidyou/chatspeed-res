---
title: "塞琳娜编码代理"
description: "一个功能齐全的编码代理，它使用符号操作（由语言服务器启用），即使在大型代码库中也能很好地工作。本质上是 Cursor 和 Windsurf Agents、Cline、Roo Code 等的免费替代品。"
---

# 塞琳娜编码代理

一个功能齐全的编码代理，它使用符号操作（由语言服务器启用），即使在大型代码库中也能很好地工作。本质上是 Cursor 和 Windsurf Agents、Cline、Roo Code 等的免费替代品。

style="width:500px">
   style="width:500px">

* :rocket: Serena 是一个强大的 **编码代理工具包**，能够将大型语言模型（LLM）转变为可以直接在您的代码库上工作的全功能代理。
* :wrench: Serena 提供了类似于 IDE 功能的基本 **语义代码检索和编辑工具**，能够在符号级别提取代码实体并利用关系结构。
* :free: Serena 是 **免费且开源的**，可以增强您已经可以免费访问的 LLM 的能力。

### 演示

这里是一个使用 Claude Desktop 的 Serena 实现一个小功能（更好的日志 GUI）的演示。请注意 Serena 的工具如何使 Claude 能够找到并编辑正确的符号。

[https://github.com/user-attachments/assets/6eaa9aa1-610d-4723-a2d6-bf1e487ba753](https://github.com/user-attachments/assets/6eaa9aa1-610d-4723-a2d6-bf1e487ba753)

### LLM 集成

Serena 为编码工作流程提供了必要的 [工具](#full-list-of-tools)，但需要 LLM 来实际执行任务，并协调工具的使用。

Serena 可以通过以下几种方式与 LLM 集成：
 * 通过使用 **模型上下文协议 (MCP)**。  
   Serena 提供了一个 MCP 服务器，可以与
     * Claude Desktop，
     * 如 VSCode、Cursor 或 IntelliJ 等 IDE，
     * 如 Cline 或 Roo Code 等扩展，
     * Goose（用于良好的 CLI 体验）
     * 以及许多其他工具集成，包括 [即将支持的 ChatGPT 应用程序](https://x.com/OpenAIDevs/status/1904957755829481737)
 * 通过使用 **Agno——模型无关的代理框架**。  
   基于 Agno 的 Serena 代理可以让您几乎将任何 LLM 转变为编码代理，无论是由 Google、OpenAI 或 Anthropic（需付费 API 密钥）提供的
   还是由 Ollama、Together 或 Anyscale 提供的免费模型。
 * 通过将 Serena 的工具整合到您选择的代理框架中。  
   Serena 的工具实现与特定框架的代码是解耦的，因此可以轻松适应任何代理框架。

### 编程语言支持与语义分析能力

Serena 的语义代码分析能力基于广泛实现的 **语言服务器** 和语言服务器协议 (LSP)。LSP 提供了一组基于对代码的符号理解的多功能代码查询和编辑功能。
配备了这些功能后，Serena 发现和编辑代码就像一位经验丰富的开发人员利用 IDE 的能力一样。
即使在非常大且复杂的项目中，Serena 也能高效地找到正确的上下文并做出正确的操作！因此，它不仅免费且开源，还经常比现有的收费解决方案取得更好的结果。

语言服务器支持广泛的编程语言。借助 Serena，我们提供

* 直接开箱即用的支持：
    * Python
    * Java (_注意_：启动较慢，初次启动尤其如此)
    * TypeScript
* 间接支持（可能需要一些代码更改/手动安装）：
    * Ruby（未测试）
    * Go（未测试）
    * C#（未测试）
    * Rust（未测试）
    * Kotlin（未测试）
    * Dart（未测试）
    * C/C++（未测试）

   这些语言由语言服务器库 [multilspy](https://github.com/microsoft/multilspy) 支持，Serena 在幕后使用该库。但我们没有明确测试这些语言的支持是否实际有效。
       
原则上，通过为新的语言服务器实现提供一个浅层适配器，可以轻松支持更多语言。

## 目录

- [我能用 Serena 做什么？](#我能用-serena-做什么)
- [使用 Serena 的免费编码代理](#使用-serena-的免费编码代理)
- [快速开始](#快速开始)
  * [设置与配置](#设置与配置)
  * [MCP 服务器 (Claude Desktop)](#mcp-服务器-claude-desktop)
  * [其他 MCP 客户端 - Cline, Roo-Code, Cursor, Windsurf 等](#其他-mcp-客户端---cline-roo-code-cursor-windsurf-等)
  * [Goose](#goose)
  * [Agno 代理](#agno-代理)
  * [其他代理框架](#其他代理框架)
- [Serena 的工具和配置](#serena-的工具和配置)
- [与其他编码代理的比较](#与其他编码代理的比较)
  * [基于订阅的编码代理](#基于订阅的编码代理)
  * [基于 API 的编码代理](#基于-api-的编码代理)
  * [其他基于 MCP 的编码代理](#其他基于-mcp-的编码代理)
- [入门和记忆](#入门和记忆)
- [与其他 MCP 服务器的组合](#与其他-mcp-服务器的组合)
- [使用 Serena 的建议](#使用-serena-的建议)
  * [选择哪个模型？](#选择哪个模型)
  * [入门](#入门-1)
  * [在编辑代码之前](#在编辑代码之前)
  * [代码编辑中可能出现的问题](#代码编辑中可能出现的问题)
  * [超出上下文限制](#超出上下文限制)
  * [控制工具执行](#控制工具执行)
  * [组织你的代码库](#组织你的代码库)
  * [日志、代码检查和测试](#日志-代码检查和测试)
  * [一般建议](#一般建议)
- [故障排除](#故障排除)
  * [Serena 日志](#serena-日志)
- [致谢](#致谢)
- [自定义 Serena](#自定义-serena)
- [工具完整列表](#工具完整列表)

## 我能用 Serena 做什么？

你可以使用 Serena 完成任何编码任务——无论是专注于分析、规划、设计新组件还是重构现有组件。
由于 Serena 的工具允许大语言模型（LLM）闭合认知感知-行动循环，基于 Serena 的代理可以从头到尾自主地执行编码任务——从最初的分析到实现、测试，最后到版本控制系统提交。

Serena 可以读取、编写和执行代码，阅读日志和终端输出。
虽然我们不一定鼓励这样做，“随性编程”当然是可能的，如果你想几乎感觉“代码不再存在”，
你可能会发现 Serena 比 IDE 内部的代理更适合随性编程（因为你将有一个独立的图形用户界面，真的可以让你忘记这一切）。

## 使用 Serena 的免费编码代理

即使是 Anthropic 的 Claude 的免费层级也支持 MCP 服务器，因此你可以免费使用 Claude 与 Serena。  
预计一旦添加了对 MCP 服务器的支持，很快也可以通过 ChatGPT Desktop 实现相同功能。  
通过 Agno，你还有选项可以使用一个免费/开放权重模型来使用 Serena。

Serena 是 [Oraios AI](https://oraios-ai.de/) 对开发者社区的贡献。  
我们自己也经常使用它。

我们厌倦了不得不支付多个基于 IDE 的订阅费用（如 Windsurf 或 Cursor），这些费用迫使我们在已经存在的聊天订阅成本之外还要购买更多的令牌。
像 Claude Code、Cline、Aider 等基于 API 的工具所产生的高额 API 费用同样不吸引人。
因此，我们构建了 Serena，希望能够取消大部分其他订阅。

## 快速开始

Serena 可以以多种方式使用，下面是一些选定集成的说明。

- 如果你只想将 Claude 转变为一个免费使用的编码代理，我们建议通过 Claude Desktop 使用 Serena。
- 如果你想使用 Gemini 或任何其他模型，并且想要一个图形用户界面体验，你应该使用 [Agno](#agno-agent)。在 macOS 上，你还可以使用 [goose](#goose) 的图形用户界面。
- 如果你更喜欢通过命令行界面使用 Serena，可以使用 [goose](#goose)。在那里几乎任何模型都是可能的。
- 如果你想在你的 IDE 中使用集成的 Serena，请参阅关于 [其他 MCP 客户端](#other-mcp-clients---cline-roo-code-cursor-windsurf-etc) 的部分。

### 设置和配置

1. 安装 `uv`（安装说明[在这里](https://docs.astral.sh/uv/getting-started/installation/)）
2. 将仓库克隆到 `/path/to/serena`。
3. 将 `serena_config.template.yml` 复制为 `serena_config.yml` 并调整设置。
4. 将 `myproject.template.yml` 复制为 `myproject.yml` 并根据你的项目调整特定设置。
   （对于每个希望 Serena 工作的项目，都添加这样一个文件。）
5. 如果希望 Serena 动态切换项目，在 `serena_config.yml` 中的 `projects` 列表里添加上一步创建的所有项目文件列表。

> ⚠️ **注意：** Serena 正在积极开发中。我们持续添加功能、改进稳定性和用户体验。
> 因此，配置可能会以破坏性的方式更改。如果你的配置无效，
> MCP 服务器或基于 Serena 的代理可能无法启动（在这种情况下，请检查 MCP 日志）。
> 在更新 Serena 时，请查看 [变更日志](https://github.com/oraios/serena/blob/HEAD/CHANGELOG.md)
> 并根据需要调整你的配置。

完成初始设置后，根据你想要如何使用 Serena，继续以下部分之一。

### MCP 服务器 (Claude 桌面版)

1. 为你的项目创建一个配置文件，例如 `myproject.yml`，基于 myproject.template.yml 模板。
2. 在客户端中配置 MCP 服务器。  
   对于 [Claude 桌面版](https://claude.ai/download)（适用于 Windows 和 macOS），请转到 文件 / 设置 / 开发者 / MCP 服务器 / 编辑配置，
   这将允许你打开 JSON 文件 `claude_desktop_config.json`。添加以下内容（并调整路径）以启用 Serena：

```json
   {
       "mcpServers": {
           "serena": {
               "command": "/abs/path/to/uv",
               "args": ["run", "--directory", "/abs/path/to/serena", "serena-mcp-server", "--project-file", "/abs/path/to/myproject.yml"]
           }
       }
   }
```

   :info: 如果你在配置中设置了 `enable_project_activation`，则传递项目文件是可选的，
   因为这样你可以简单地指示 Claude 激活你想要工作的项目。

   如果你在 Windows 上使用包含反斜杠的路径
   （请注意，你也可以只使用正斜杠），请确保正确转义它们（`\\`）。

就这样！保存配置，然后重新启动 Claude 桌面版。

注意：在 Windows 和 macOS 上有 Anthropic 提供的官方 Claude 桌面应用程序，对于 Linux 有一个 [开源社区版本](https://github.com/aaddrick/claude-desktop-debian)。

⚠️ 确保完全退出 Claude 桌面应用程序，因为关闭 Claude 只会将其最小化到系统托盘——至少在 Windows 上是这样。

重新启动后，你应该会在聊天界面中看到 Serena 的工具（注意小锤子图标）。

⚠️ 工具名称：Claude 桌面版（以及大多数 MCP 客户端）不会解析服务器的名称。因此你不应该说“使用 Serena 的工具”之类的话。相反，你可以指示 LLM 使用符号工具或通过引用其名称来使用特定工具。此外，如果你使用多个 MCP 服务器，可能会出现**工具名称冲突**，导致未定义的行为。例如，由于工具名称冲突，Serena 目前与 [文件系统 MCP 服务器](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) 不兼容。

ℹ️ 请注意，使用 stdio 作为协议的 MCP 服务器在客户端/服务器架构中是相对不常见的，因为为了通过服务器的标准输入/输出流进行通信，客户端必须启动服务器。换句话说，您不需要自己启动服务器。客户端应用程序（例如 Claude Desktop）会负责这一点，因此需要配置一个启动命令。

有关 Claude Desktop 的 MCP 服务器的更多信息，请参阅[官方快速入门指南](https://modelcontextprotocol.io/quickstart/user)。

### 其他 MCP 客户端 - Cline, Roo-Code, Cursor, Windsurf 等

作为一个 MCP 服务器，Serena 可以被任何 MCP 客户端包含。与上述相同的配置，可能加上一些特定于客户端的小修改即可工作。大多数流行的现有编码助手（IDE 扩展或类似 VSCode 的 IDE）都支持连接到 MCP 服务器。包括 Serena 通常可以通过提供符号操作工具来提高它们的性能。

在这种情况下，使用的计费继续由您选择的客户端控制（不像使用 Claude Desktop 客户端那样）。但您仍然可能希望通过这种方式使用 Serena，例如出于以下原因之一：

1. 您已经在使用一个编码助手（比如 Cline 或 Cursor），只是想让它更强大。
2. 您使用的是 Linux 并且不想使用[社区创建的 Claude Desktop](https://github.com/aaddrick/claude-desktop-debian)。
3. 您希望将 Serena 更紧密地集成到您的 IDE 中，并且不介意为此付费。

这里同样适用使用 Claude Desktop 的 Serena 时的注意事项（特别是工具名称冲突问题）。

当在内置有 AI 编码交互功能的 IDE 或扩展中使用时（实际上，所有这些都有），Serena 的全套工具可能会导致与您作为用户无法控制的客户端内部工具发生不必要的交互。这尤其适用于编辑工具，您可能需要为此目的禁用这些工具。随着我们在各种流行客户端中使用 Serena 积累更多经验，我们将收集并改进最佳实践，以实现顺畅体验。

### Goose

[goose](https://github.com/block/goose) 是一个独立的编码代理，它有一个针对 MCP 服务器的集成，并提供了 CLI（以及在 macOS 上的 GUI）。目前，使用 goose 是通过您选择的 LLM 通过 CLI 运行 Serena 的最简单方法。

请按照[此处](https://block.github.io/goose/docs/getting-started/installation/)的说明进行安装。

之后，使用 `goose configure` 来添加一个扩展。要添加 Serena，请选择 `Command-line Extension` 选项，将其命名为 `Serena` 并添加以下命令：

```
/abs/path/to/uv run --directory /abs/path/to/serena serena-mcp-server /optional/abs/path/to/project.yml
```

由于 Serena 可以执行所有必要的编辑和命令操作，您应该禁用 goose 默认启用的 `developer` 扩展。为此，请执行

```shell
goose configure
```
再次选择 `Toggle Extensions` 选项，并确保选中启用 Serena 而未选中 `developer`。

就这样。浏览 goose 的配置选项，看看你能用它做什么（功能很多，比如为工具执行设置不同级别的权限）。

> Goose 在会话结束时似乎并不总是能正确终止 MCP 服务器的 python 进程。
> 您可能需要禁用 Serena GUI 和/或在完成使用 goose 的工作后手动清理任何正在运行的 python 进程。

### Agno Agent

Agno 是一个模型无关的代理框架，允许您将 Serena 转变为一个代理（独立于 MCP 技术），并支持大量底层 LLM。目前，Agno 是在聊天 GUI 中运行 Serena 并选择任意 LLM 的最简单方法（除非您使用的是 Mac，在这种情况下您可能更喜欢几乎不需要设置的 goose）。

尽管 Agno 尚未完全稳定，但我们选择了它，因为它自带开源 UI，使得通过聊天界面直接使用代理变得非常容易。使用 Agno，Serena 变成一个代理（因此不再是 MCP 服务器），因此可以在编程方式下使用（例如用于基准测试或在您的应用程序中）。

其工作原理如下（另见 [Agno 的文档](https://docs.agno.com/introduction/playground)）：

1. 使用 npx 下载 agent-ui 代码
```shell
   npx create-agent-ui@latest
```
   或者，也可以手动克隆：
```shell
   git clone https://github.com/agno-agi/agent-ui.git
   cd agent-ui 
   pnpm install 
   pnpm dev
```

2. 安装带有可选要求的 serena：
```shell
   # 您也可以仅选择 agno,google 或 agno,anthropic 而不是 all-extras
   uv pip install --all-extras -r pyproject.toml -e .
```
   
3. 将 `.env.example` 复制到 `.env` 并填写打算使用的提供商的 API 密钥。

5. 启动 agno 代理应用：
```shell
   uv run python scripts/agno_agent.py
```
   默认情况下，脚本使用 Claude 作为模型，但您可以选择 Agno 支持的任何模型（本质上是任何现有的模型）。

5. 在新的终端中，启动 agno UI：
```shell
   cd agent-ui 
   pnpm dev
```
   将 UI 连接到上面启动的代理并开始聊天。您将拥有与 MCP 服务器版本相同的工具。

这是一个简短的演示，展示了 Serena 使用最新的 Gemini 模型执行一个小分析任务：

[https://github.com/user-attachments/assets/ccfcb968-277d-4ca9-af7f-b84578858c62](https://github.com/user-attachments/assets/ccfcb968-277d-4ca9-af7f-b84578858c62)

⚠️ 重要提示：与 MCP 服务器方法不同，Agno UI 中的工具执行不会请求用户的许可。特别是 shell 工具，因为它可以执行任意代码。虽然我们在使用 Claude 测试时从未遇到过任何问题，但允许这样做可能并不完全安全。您可以在 Serena 项目的配置文件（`.yml`）中为您自己的设置选择禁用某些工具。

### 其他代理框架

Agno 代理特别好用，因为它有 Agno UI，但将 Serena 集成到任何代理框架（如 [pydantic-ai](https://ai.pydantic.dev/), [langgraph](https://langchain-ai.github.io/langgraph/tutorials/introduction/) 或其他）中也非常容易。

你只需要为选择的框架编写一个从 Serena 工具到该框架工具的适配器，就像我们为 agno 在 [SerenaAgnoToolkit](https://github.com/oraios/serena/blob/HEAD/src/serena/agno.py) 中所做的那样。

## Serena 的工具和配置

Serena 结合了用于语义代码检索的工具、编辑功能和 shell 执行。完整的工具列表请参见[下方](#serenas-tools-and-configuration)。

通常建议使用所有工具，因为这可以让 Serena 提供最大的价值：只有通过执行 shell 命令（特别是测试），Serena 才能自主识别并纠正错误。

然而，需要注意的是，`execute_shell_command` 工具允许任意代码执行。当作为 MCP 服务器使用时，客户端通常会在执行工具前向用户请求许可，因此只要用户事先检查执行参数，这不应该是个问题。但是，如果你有任何顾虑，可以在项目的 .yml 配置文件中选择禁用某些命令。如果你只想纯粹地使用 Serena 分析代码并提出实现建议而不修改代码库，可以通过在项目配置文件中设置 `read_only: true` 来启用只读模式。这将自动禁用所有编辑工具，并防止对代码库进行任何修改，同时仍然允许所有的分析和探索能力。

总体来说，请确保备份你的工作，并使用版本控制系统以避免丢失任何工作。

## 与其他编码代理的比较

据我们所知，Serena 是第一个完全功能性的编码代理，其所有功能都可通过 MCP 服务器获得，因此不需要 API 密钥或订阅。

### 订阅制编码代理

最著名的基于订阅的编码代理是 IDE 的一部分，如 Windsurf、Cursor 和 VSCode。
Serena 的功能类似于 Cursor 的 Agent、Windsurf 的 Cascade 或即将推出的 VSCode 的 [agent mode](https://code.visualstudio.com/blogs/2025/02/24/introducing-copilot-agent-mode)。

Serena 的优势在于不需要订阅。
潜在的缺点是它没有直接集成到 IDE 中，因此新编写代码的检查不如那么无缝。

更多的技术差异包括：

* Serena 不绑定于特定的 IDE。
  Serena 的 MCP 服务器可以与任何 MCP 客户端（包括一些 IDE）一起使用，
  而基于 Agno 的代理提供了应用其功能的额外方式。
* Serena 不绑定于特定的大语言模型或 API。
* Serena 使用语言服务器来导航和编辑代码，因此它对代码有符号性的理解。
  基于 IDE 的工具通常使用基于 RAG 或纯文本的方法，这在大型代码库中通常
  效果较差。
* Serena 是开源的，并且代码库很小，因此可以轻松扩展和修改。

### 基于 API 的编码代理

订阅制代理的替代方案是像 Claude Code、Cline、Aider、Roo Code 等基于 API 的代理，其中使用成本直接映射到底层大语言模型 (LLM) 的 API 成本。
有些（如 Cline）甚至可以作为扩展集成到 IDE 中。
它们通常非常强大，主要缺点是（可能非常高）的 API 成本。

Serena 本身也可以用作基于 API 的代理（见上文关于 Agno 的部分）。
我们还没有为 Serena 编写 CLI 工具或专用的 IDE 扩展（后者可能也没有必要，因为 Serena 已经可以与支持 MCP 服务器的任何 IDE 一起使用）。
如果有需求将 Serena 作为类似于 Claude Code 的 CLI 工具，我们会考虑编写一个。

Serena 与其他基于 API 的代理的主要区别在于，Serena 也可以用作 MCP 服务器，因此不需要 API 密钥并绕过了 API 成本。这是 Serena 的独特特性。

### 其他基于 MCP 的编码代理

还有其他设计用于编码的 MCP 服务器，如 [DesktopCommander](https://github.com/wonderwhy-er/DesktopCommanderMCP) 和
[codemcp](https://github.com/ezyang/codemcp)。
然而，据我们所知，它们都没有提供语义代码检索和编辑工具；它们完全依赖于基于文本的分析。
正是语言服务器与 MCP 的结合使 Serena 在处理具有挑战性的编码任务时变得独一无二且非常强大，尤其是在较大的代码库上下文中。

## 引导和记忆

默认情况下，当 Serena 第一次启动一个项目时，它会执行引导过程。
该过程的目标是让 Serena 熟悉项目并存储记忆，以便在未来交互中引用这些记忆。

记忆文件存储在项目目录中的 `.serena/memories/` 文件夹内，代理可以选择读取这些文件。
您可以根据需要自由阅读和调整这些文件；您也可以手动添加新的记忆文件。
`.serena/memories/` 目录中的每个文件都是一个记忆文件。

我们发现记忆显著提升了用户与 Serena 交互的体验。
Serena 本身会在适当的时候被指示创建新的记忆。

## 与其他 MCP 服务器结合使用

当通过 MCP 客户端使用 Serena 时，您可以将其与其他 MCP 服务器一起使用。
但是，请注意工具名称冲突！详见上方信息。

目前，与流行的 Filesystem MCP 服务器存在冲突。由于 Serena 也提供了文件系统操作，因此很可能不需要同时启用这两个功能。

## 使用 Serena 的建议

随着 Serena 社区的发展，我们将继续收集最佳实践。以下是我们内部使用 Serena 时学到的一些简要概述。

这些建议中的大多数适用于任何编码代理，包括上述提到的所有代理。

### 选择哪个模型？

令我们惊讶的是，Serena 似乎在 Claude 3.7 的非思考版本上表现最好，而不是其思考版本（我们尚未与 Gemini 进行广泛比较）。思考版本花费的时间更长，在使用工具方面有更多的困难，并且经常会在没有充分阅读上下文的情况下直接编写代码。

在最初的实验中，Gemini 表现得非常好。不幸的是，Gemini 目前还不支持 MCP，因此唯一的使用方法是通过 API 密钥。好的一面是，Gemini 相对便宜，并且可以处理巨大的上下文长度。

### 入门

在第一次交互中，Serena 会被指示执行入门并写入第一个记忆文件。有时（取决于 LLM），文件可能不会被写入磁盘。在这种情况下，只需让 Serena 写入记忆即可。

在这个阶段，Serena 通常会读取和写入大量文本，从而填满上下文。我们建议您在完成入门后切换到另一个对话，以避免耗尽令牌。入门只会执行一次，除非您明确触发它。

入门完成后，我们建议您快速查看记忆内容，并在必要时进行编辑或添加额外的记忆。

### 在编辑代码之前

最好从一个干净的 git 状态开始代码生成任务。这样做不仅会让您更容易检查更改，而且模型本身也有机会通过调用 `git diff` 来查看它所做出的更改，从而纠正自己或在需要时继续后续对话。

:warning: **重要**：由于 Serena 将使用系统原生的换行符来写入文件，并且它可能需要查看 git diff，因此在 Windows 上设置 `git config core.autocrlf` 为 `true` 是很重要的。
如果在 Windows 上将 `git config core.autocrlf` 设置为 `false`，您可能会因为换行符的原因而得到巨大的差异。一般来说，在 Windows 上启用这个 git 设置是个好主意：

```shell
git config --global core.autocrlf true
```

### 代码编辑中可能出现的问题

根据我们的经验，LLM 在计数方面非常差，即它们在正确位置插入代码块时会有问题。大多数编辑操作可以在符号级别上进行，从而使这个问题得以克服。然而，有时，行级别的插入是有用的。

Serena 被指示仔细检查它将编辑的行号和任何代码块，但如果您遇到问题，可能会发现明确告诉它如何编辑代码是有用的。

### 上下文耗尽

对于长而复杂的任务，或者 Serena 阅读了大量内容的任务，你可能会接近上下文令牌的限制。在这种情况下，通常建议在一个新的对话中继续。Serena 有一个专门的工具来创建当前进度和所有相关信息的摘要，以便继续任务。你可以请求创建这个摘要并将其写入记忆中。然后，在一个新的对话中，你可以让 Serena 读取该记忆并继续执行任务。根据我们的经验，这种方法非常有效。此外，由于在单一会话中不涉及摘要化处理，Serena 通常不会迷失方向（与一些在后台进行摘要化的其他代理不同），并且它也被指示偶尔检查是否在正确的轨道上。

此外，Serena 被指示要节约使用上下文（例如，不要不必要的阅读代码符号的主体），但我们发现 Claude 在这方面并不总是表现得很好（Gemini 在这一点上似乎更好）。如果你知道不需要的话，可以明确指示它不要阅读这些主体部分。

### 控制工具执行

Claude Desktop 在执行工具前会询问你。对于大多数工具，你可以安全地点击“允许此聊天”，特别是当你的所有文件都在版本控制之下时。一个例外是 `execute_shell_command` 工具——在这种情况下，你可能需要单独检查每个调用。我们建议逐个审查对这个命令的调用，并且不要为整个聊天启用它。

### 结构化你的代码库

Serena 使用代码结构来查找、阅读和编辑代码。这意味着它将很好地处理结构良好的代码，但对于完全无结构的代码（如具有巨大而非模块化函数的 God-class）则可能失败。类型注解在这里也非常有帮助。你的代码越好，Serena 的工作效果就越好。因此，我们一般建议你编写结构良好、模块化且带有类型标注的代码——这不仅对你有帮助，也对你的 AI 有帮助；)。

### 日志记录、代码检查和测试

Serena 不能调试（据我们所知，目前还没有任何编码助手能做到这一点）。这意味着为了在_代理循环_中改进结果，Serena 需要通过执行测试、运行脚本、执行代码检查等手段获取信息。包含许多带有明确信息的日志消息以及拥有有意义的测试通常是非常有帮助的。尤其是后者经常帮助代理自我纠正。

我们通常建议从所有代码检查和测试都通过的状态开始编辑任务。

### 通用建议

我们发现，在实际实施任务之前，花一些时间概念化和规划任务通常是很有益的，特别是对于非简单的任务。这有助于取得更好的结果，并增加控制感和保持在循环中的感觉。你可以在一个会话中制定详细的计划，让Serena阅读你的大量代码以建立上下文，然后在另一个会话中继续实施（可能是在创建合适的记忆之后）。

## 故障排除

Claude Desktop 中对 MCP 服务器的支持以及各种 MCP 服务器 SDK 是相对较新的发展，可能会显示出不稳定性。

MCP 服务器的工作配置可能因平台而异，也可能因客户端而异。我们建议始终使用绝对路径，因为相对路径可能是错误的来源。语言服务器在一个单独的子进程中运行，并通过 asyncio 调用——有时客户端可能会导致其崩溃。如果你启用了 Serena 的日志窗口并且它消失了，那么你就知道发生了什么。

某些客户端（如 goose）可能无法正确终止 MCP 服务器，请注意挂起的 Python 进程并在必要时手动终止它们。

### Serena 日志记录

为了帮助故障排除，我们编写了一个用于日志记录的小型 GUI 工具。对于大多数客户端，如果你遇到问题，我们建议你通过项目配置 (`myproject.yml`) 启用它。许多客户端还会写入 MCP 日志，这可以帮助识别问题。

日志记录 GUI 可能不适用于所有客户端和所有系统。目前，它在 macOS 或 VSCode 扩展（如 Cline）内不起作用。

## 致谢

我们在多个现有的开源技术之上构建了 Serena，其中最重要的包括：

1. [multilspy](https://github.com/microsoft/multilspy)。
   它是围绕遵循 LSP 的语言服务器设计的一个精美包装器。它
   并不容易扩展以适应 Serena 所需的符号逻辑，因此我们没有将其作为依赖项引入，
   而是复制了源代码并根据我们的需求进行了调整。
2. [Python MCP SDK](https://github.com/modelcontextprotocol/python-sdk)
3. [Agno](https://github.com/agno-agi/agno) 和
   相关的 [agent-ui](https://github.com/agno-agi/agent-ui)，
   我们使用这些工具允许 Serena 与任何模型合作，而不仅仅是支持 MCP 的模型。
4. 我们通过 multilspy 使用的所有语言服务器。

没有这些项目，Serena 将不可能实现（或者将显著更难构建）。

## 自定义 Serena

非常容易用自己的想法扩展 Serena 的 AI 功能。
只需从 `serena.agent.Tool` 继承来实现一个新的工具，并实现 `apply` 方法（不是接口的一部分，请参见 `Tool` 中的注释）。默认情况下，`SerenaAgent` 将立即可以访问它。

添加[对新语言的支持](https://github.com/oraios/serena/blob/HEAD/CONTRIBUTING.md#adding-a-new-supported-language)也相对简单。我们期待着社区会带来什么！有关贡献的详细信息，请参阅[这里](https://github.com/oraios/serena/blob/HEAD/CONTRIBUTING.md)。

## 工具完整列表

以下是Serena工具的完整列表及其简短描述（`uv run serena-list-tools`命令的输出）：

* `activate_project`: 通过名称激活一个项目。
* `check_onboarding_performed`: 检查是否已经执行了入门操作。
* `create_text_file`: 在项目目录中创建/覆盖一个文件。
* `delete_lines`: 删除文件中的某一行范围。
* `delete_memory`: 从Serena的特定于项目的存储中删除一条记忆。
* `execute_shell_command`: 执行一个shell命令。
* `find_referencing_code_snippets`: 查找给定位置符号被引用的代码片段。
* `find_referencing_symbols`: 查找引用给定位置符号的其他符号（可按类型过滤）。
* `find_symbol`: 对具有/包含给定名称/子字符串的符号进行全局（或局部）搜索（可按类型过滤）。
* `get_active_project`: 获取当前激活的项目名称（如果有的话），并列出所有存在的项目
* `get_symbols_overview`: 获取顶级符号定义的概览

**官方网站：** [https://github.com/oraios/serena](https://github.com/oraios/serena)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `version control`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`/abs/path/to/uv`
- 参数：`run --directory /abs/path/to/serena serena-mcp-server --project-file /abs/path/to/myproject.yml`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/oraios-serena.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
