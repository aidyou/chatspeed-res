---
title: "记忆知识库"
description: "基础记忆是一个知识管理系统，它允许你通过与人工智能助手的对话构建持久的语义图。所有知识都以标准的Markdown文件形式存储在你的计算机中，让你完全掌控和拥有自己的数据。它直接与Obsidian.md集成。"
---

# 记忆知识库

基础记忆是一个知识管理系统，它允许你通过与人工智能助手的对话构建持久的语义图。所有知识都以标准的Markdown文件形式存储在你的计算机中，让你完全掌控和拥有自己的数据。它直接与Obsidian.md集成。

[![License: AGPL v3](/mcp-assets/e817069efdf1f7a6a364a7bbeba8bb17.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![PyPI version](/mcp-assets/398bb891823a702c9022dbeeb34916b8.svg)](https://badge.fury.io/py/basic-memory)
[![Python 3.12+](/mcp-assets/5142151145d2dd1ac338bb460f878742.svg)](https://www.python.org/downloads/)
[![Tests](/mcp-assets/dc4eae1ef3939ffe44eb69395d31e600.svg)](https://github.com/basicmachines-co/basic-memory/actions)
[![Ruff](/mcp-assets/060891c43dd6eea42d433efb95f8d92e.svg)](https://github.com/astral-sh/ruff)
![](/mcp-assets/c1486b4e2d8cfd67ed0257afeefda188.svg 'MCP Server')
![](/mcp-assets/096e1130aefa8ee21de38bd1147752bc.svg 'MCP Dev')
[Smithery](https://smithery.ai/server/@basicmachines-co/basic-memory)

# Basic Memory

Basic Memory 使您能够通过与大型语言模型（如 Claude）的自然对话构建持久的知识，同时将所有内容保存在计算机上的简单 Markdown 文件中。它使用 Model Context Protocol (MCP) 来使任何兼容的 LLM 能够读取和写入您的本地知识库。

- 网站: https://basicmachines.co
- 文档: https://memory.basicmachines.co

## 从上次离开的地方继续对话

- AI 助手可以在新的对话中从本地文件加载上下文
- 笔记会实时保存为本地的 Markdown 文件
- 不需要项目知识或特殊提示

[https://github.com/user-attachments/assets/a55d8238-8dd0-454a-be4c-8860dbbd0ddc](https://github.com/user-attachments/assets/a55d8238-8dd0-454a-be4c-8860dbbd0ddc)

## 快速开始

```bash
# Install with uv (recommended)
uv tool install basic-memory

# Configure Claude Desktop (edit ~/Library/Application Support/Claude/claude_desktop_config.json)
# Add this to your config:
{
  "mcpServers": {
    "basic-memory": {
      "command": "uvx",
      "args": [
        "basic-memory",
        "mcp"
      ]
    }
  }
}
# Now in Claude Desktop, you can:
# - Write notes with "Create a note about coffee brewing methods"
# - Read notes with "What do I know about pour over coffee?"
# - Search with "Find information about Ethiopian beans"

```

您可以通过 `~/basic-memory`（默认目录位置）中的文件查看共享上下文。

### 通过 Smithery 安装

您可以使用 [Smithery](https://smithery.ai/server/@basicmachines-co/basic-memory) 自动配置 Claude 桌面版的 Basic Memory：

```bash
npx -y @smithery/cli install @basicmachines-co/basic-memory --client claude
```

这将在不需要手动编辑 Claude 桌面配置文件的情况下安装和配置 Basic Memory。Smithery 服务器托管 MCP 服务器组件，而您的数据仍然以 Markdown 文件的形式存储在本地。

### Glama.ai

  

## 为什么选择 Basic Memory？

大多数 LLM 交互都是短暂的——您提问，得到答案，然后一切都被遗忘。每次对话都是全新的，没有之前的上下文或知识。当前的解决方法有其局限性：

- 聊天记录可以捕获对话，但不是结构化的知识
- RAG 系统可以查询文档，但不允许 LLM 写回
- 向量数据库需要复杂的设置，并且通常位于云端
- 知识图谱通常需要专门的工具来维护

Basic Memory 通过一种简单的方法解决了这些问题：结构化的 Markdown 文件，既可由人类也可由 LLM 读写。主要优点包括：

- **本地优先：** 所有知识都保存在你控制的文件中
- **双向互动：** 你和大语言模型（LLM）都可以读写相同的文件
- **结构化但简单：** 使用熟悉的 Markdown 格式并带有语义模式
- **可遍历的知识图谱：** LLM 可以跟踪主题之间的链接
- **标准格式：** 与现有的编辑器如 Obsidian 兼容
- **轻量级基础设施：** 仅使用本地文件并在本地 SQLite 数据库中索引

使用 Basic Memory，你可以：

- 进行基于先前知识的对话
- 在自然对话中创建结构化的笔记
- 与记住之前讨论内容的大语言模型进行对话
- 语义地浏览你的知识图谱
- 保持所有内容本地化并由你控制
- 使用熟悉的工具如 Obsidian 查看和编辑笔记
- 构建随时间增长的个人知识库

## 实际工作原理

假设你正在探索咖啡冲泡方法，并希望记录你的知识。以下是具体步骤：

1. 首先开始正常的聊天：

```
I've been experimenting with different coffee brewing methods. Key things I've learned:

- Pour over gives more clarity in flavor than French press
- Water temperature is critical - around 205°F seems best
- Freshly ground beans make a huge difference
```

... 继续对话。

2. 请 LLM 帮助整理这些知识：

```
"Let's write a note about coffee brewing methods."
```

LLM 会在你的系统上创建一个新的 Markdown 文件（你可以立即在 Obsidian 或其他编辑器中看到）：

```markdown
---
title: Coffee Brewing Methods
permalink: coffee-brewing-methods
tags:
- coffee
- brewing
---

# Coffee Brewing Methods

## Observations

- [method] Pour over provides more clarity and highlights subtle flavors
- [technique] Water temperature at 205°F (96°C) extracts optimal compounds
- [principle] Freshly ground beans preserve aromatics and flavor

## Relations

- relates_to [[Coffee Bean Origins]]
- requires [[Proper Grinding Technique]]
- affects [[Flavor Extraction]]
```

该笔记嵌入了语义内容，并通过简单的 Markdown 格式链接到其他主题。

3. 你会实时在当前项目目录（默认为 `~/$HOME/basic-memory`）中看到这个文件。

- 实时同步功能在 v0.12.0 版本中默认启用

4. 在与 LLM 的对话中，你可以引用某个主题：

```
Look at `coffee-brewing-methods` for context about pour over coffee
```

LLM 现在可以从知识图谱中构建丰富的上下文。例如：

```
Following relation 'relates_to [[Coffee Bean Origins]]':
- Found information about Ethiopian Yirgacheffe
- Notes on Colombian beans' nutty profile
- Altitude effects on bean characteristics

Following relation 'requires [[Proper Grinding Technique]]':
- Burr vs. blade grinder comparisons
- Grind size recommendations for different methods
- Impact of consistent particle size on extraction
```

每个相关的文档都可以提供更多上下文，从而构建对你知识库的丰富语义理解。

这创建了一个双向流程，其中：

- 人类编写和编辑 Markdown 文件
- LLM 通过 MCP 协议读写
- 同步保持一切一致
- 所有知识都保存在本地文件中。

## 技术实现

在底层，Basic Memory：

1. 将所有内容存储在 Markdown 文件中
2. 使用 SQLite 数据库进行搜索和索引
3. 从简单的 Markdown 模式中提取语义意义
    - 文件成为 `Entity` 对象
    - 每个 `Entity` 可以有 `Observations`，即与其相关的事实
    - `Relations` 将实体连接在一起形成知识图谱
4. 维护从文件派生的本地知识图谱
5. 提供文件和知识图谱之间的双向同步
6. 实现用于 AI 集成的 Model Context Protocol (MCP)
7. 提供让 AI 助手遍历和操作知识图谱的工具
8. 使用 memory:// URL 在工具和对话之间引用实体

文件格式只是带有简单标记的 Markdown：

每个 Markdown 文件包含：

### 前置信息

```markdown
title: 
type: 
 (e.g. note)
permalink: 

-  (such as tags) 
```

### 观察

请注意，代码块中的内容（如 `#2`, `#3`, `#4`, `#5`, `#6`, `#7`）是占位符，实际内容需要根据具体情况填写。

观察是关于某个主题的事实。
它们可以通过创建具有特殊格式的 Markdown 列表来添加，该列表可以使用 "#" 字符引用 `category` 和 `tags`，以及可选的 `context`。

观察的 Markdown 格式：

```markdown
- [category] content #tag (optional context)
```

观察的例子：

```markdown
- [method] Pour over extracts more floral notes than French press
- [tip] Grind size should be medium-fine for pour over #brewing
- [preference] Ethiopian beans have bright, fruity flavors (especially from Yirgacheffe)
- [fact] Lighter roasts generally contain more caffeine than dark roasts
- [experiment] Tried 1:15 coffee-to-water ratio with good results
- [resource] James Hoffman's V60 technique on YouTube is excellent
- [question] Does water temperature affect extraction of different compounds differently?
- [note] My favorite local shop uses a 30-second bloom time
```

### 关系

关系是指向其他主题的链接。它们定义了知识图谱中实体之间的连接方式。

Markdown 格式：

```markdown
- relation_type [[WikiLink]] (optional context)
```

关系的例子：

```markdown
- pairs_well_with [[Chocolate Desserts]]
- grown_in [[Ethiopia]]
- contrasts_with [[Tea Brewing Methods]]
- requires [[Burr Grinder]]
- improves_with [[Fresh Beans]]
- relates_to [[Morning Routine]]
- inspired_by [[Japanese Coffee Culture]]
- documented_in [[Coffee Journal]]
```

## 与 VS Code 一起使用
要一键安装，请点击下面的其中一个安装按钮...

[![通过 UV 在 VS Code 中安装](/mcp-assets/ff0c64ea4d3a42e6aeccd71c5a5b6a57.svg)](https://insiders.vscode.dev/redirect/mcp/install?name=basic-memory&config=%7B%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22basic-memory%22%2C%22mcp%22%5D%7D) [![通过 UV 在 VS Code Insiders 中安装](/mcp-assets/805d41193c5fff3f82290b52ad64e24d.svg)](https://insiders.vscode.dev/redirect/mcp/install?name=basic-memory&config=%7B%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22basic-memory%22%2C%22mcp%22%5D%7D&quality=insiders)

您可以使用 Basic Memory 与 VS Code 轻松地在编码时检索和存储信息。点击上面的安装按钮进行一键设置，或者按照以下手动安装说明操作。

### 手动安装

将以下 JSON 块添加到您的 VS Code 用户设置（JSON）文件中。您可以通过按下 `Ctrl + Shift + P` 并键入 `Preferences: Open User Settings (JSON)` 来完成此操作。

```json
{
  "mcp": {
    "servers": {
      "basic-memory": {
        "command": "uvx",
        "args": ["basic-memory", "mcp"]
      }
    }
  }
}
```

或者，您可以将其添加到工作区中的 `.vscode/mcp.json` 文件中。这将允许您与其他人共享配置。

```json
{
  "servers": {
    "basic-memory": {
      "command": "uvx",
      "args": ["basic-memory", "mcp"]
    }
  }
}
```

## 与 Claude 桌面版一起使用

Basic Memory 是使用 MCP（模型上下文协议）构建的，并且支持 Claude 桌面应用程序 ([https://claude.ai/](https://claude.ai/)):

1. 配置 Claude 桌面版以使用 Basic Memory：

编辑您的 MCP 配置文件（通常位于 OS X 的 `~/Library/Application Support/Claude/claude_desktop_config.json`）：

```json
{
  "mcpServers": {
    "basic-memory": {
      "command": "uvx",
      "args": [
        "basic-memory",
        "mcp"
      ]
    }
  }
}
```

如果您想使用特定项目（请参阅 多个项目），更新您的 Claude 桌面版配置：

```json
{
  "mcpServers": {
    "basic-memory": {
      "command": "uvx",
      "args": [
        "basic-memory",
        "mcp",
        "--project",
        "your-project-name"
      ]
    }
  }
}
```

2. 同步您的知识：

如果您进行了手动编辑，Basic Memory 将实时同步项目中的文件。

3. 在 Claude 桌面版中，LLM 现在可以使用这些工具：

```
write_note(title, content, folder, tags) - Create or update notes
read_note(identifier, page, page_size) - Read notes by title or permalink
build_context(url, depth, timeframe) - Navigate knowledge graph via memory:// URLs
search_notes(query, page, page_size) - Search across your knowledge base
recent_activity(type, depth, timeframe) - Find recently updated information
canvas(nodes, edges, title, folder) - Generate knowledge visualizations
```

5. 可尝试的示例提示：

```
"Create a note about our project architecture decisions"
"Find information about JWT authentication in my notes"
"Create a canvas visualization of my project components"
"Read my notes on the authentication system"
"What have I been working on in the past week?"
```

## 更多信息

查看 [文档](https://memory.basicmachines.co/) 了解更多信息，包括：

- [完整用户指南](https://memory.basicmachines.co/docs/user-guide)
- [CLI 工具](https://memory.basicmachines.co/docs/cli-reference)
- [管理多个项目](https://memory.basicmachines.co/docs/cli-reference#project)
- [从 OpenAI/Claude 项目导入数据](https://memory.basicmachines.co/docs/cli-reference#import)

## 许可证

AGPL-3.0

欢迎贡献。有关本地设置项目和提交 PR 的信息，请参阅 [贡献指南](https://github.com/basicmachines-co/basic-memory/blob/HEAD/CONTRIBUTING.md)。

## 星标历史

请注意，上述翻译保留了原始 Markdown 结构及代码块内容不变。对于具体的代码块内容（如 `#8`, `#9` 等），请根据实际情况替换为相应的中文或保持英文原样，因为这些可能是特定的占位符或示例代码。

 

   
   
   

 

由 Basic Machines 用 ♥️ 构建

**官方网站：** [https://github.com/basicmachines-co/basic-memory](https://github.com/basicmachines-co/basic-memory)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`memory`, `files`
- 标签：`knowledge and memory`, `note taking`, `file systems`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`basic-memory mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/basicmachines-co-basic-memory.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
