---
title: "MemOS 记忆操作系统"
description: "MemOS记忆管理助手 服务简介 MemOS记忆管理是一款强大的插件，它允许用户访问MemOS记忆的添加和搜索功能，能够存取对话内容，为用户提供高效的记忆管理服务，助力于提升用户与AI对话的一致性和个性化水平。 链接 - MemOS官网：https://memos.openmem.net/cn/ - MemOS Github：https://github.com/MemTensor/MemOS 工…"
---

# MemOS 记忆操作系统

MemOS记忆管理助手 服务简介 MemOS记忆管理是一款强大的插件，它允许用户访问MemOS记忆的添加和搜索功能，能够存取对话内容，为用户提供高效的记忆管理服务，助力于提升用户与AI对话的一致性和个性化水平。 链接 - MemOS官网：https://memos.openmem.net/cn/ - MemOS Github：https://github.com/MemTensor/MemOS 工…

# MemOS记忆管理助手

## 服务简介

MemOS记忆管理是一款强大的插件，它允许用户访问MemOS记忆的添加和搜索功能，能够存取对话内容，为用户提供高效的记忆管理服务，助力于提升用户与AI对话的一致性和个性化水平。

## 链接
- MemOS官网：https://memos.openmem.net/cn/
- MemOS Github：https://github.com/MemTensor/MemOS

## 工具介绍
- search_memory：该工具用于查询用户的记忆数据，可返回与输入最相关的片段。支持在用户与AI对话期间实时检索内存，也能在整个内存中进行全局搜索，可用于创建用户配置文件或支持个性化推荐，查询时需提供对话ID、用户ID、查询文本等参数，还可设置返回的记忆项数量。
- add_message：此工具可将一条或多条消息批量导入到MemOS记忆存储数据库，方便在未来对话中检索，从而支持聊天历史管理、用户行为跟踪和个性化交互，使用时需指定对话ID、消息内容、发送者角色、对话时间和用户ID等信息。
- delete_memory：该工具用于根据 ID 删除特定的记忆。使用时需提供将要删除记忆的用户 ID 列表以及要删除的记忆 ID 列表。
- add_feedback：该工具用于向 MemOS 系统提交用户反馈。使用时需提供用户标识符、会话唯一标识符和反馈的具体内容。此外，还支持提供 Agent ID、App ID、反馈时间、是否允许公开访问以及允许写入的知识库 ID 列表等可选参数。
- get_user_profile：该工具用于获取用户的全维度记忆画像，返回事实记忆、偏好信息以及工具使用轨迹。适用于“我是谁”“我的偏好是什么”等身份类问题。使用时可设置是否包含偏好、是否包含工具轨迹，以及分页参数（页码与每页数量）。
- create_knowledge_base：该工具用于创建知识库容器，便于按项目或领域管理文档。使用时需提供知识库名称，并可选填写知识库描述。
- remove_knowledge_base：该工具用于移除不再需要的知识库及其关联内容
- add_kb_document：该工具用于向指定知识库上传文档。支持本地文件路径、公网 URL 或 Base64 数据内容。使用时需提供知识库 ID 与文件列表；文件项可包含内容、文件名，以及本地文件场景下的 MIME 类型
- get_kb_documents：该工具用于根据文件 ID 列表批量获取知识库文档信息。使用时需提供文件 ID 列表。
- delete_kb_documents：该工具用于从知识库中按文件 ID 精准删除文档。使用时需提供文件 ID 列表。

## 使用方式

### 配置
```json
{
  "mcpServers": {
    "memos-api-mcp": {
      "timeout": 60,
      "type": "stdio",
      "command": "npx",
      "args": [
        "-y",
        "@memtensor/memos-api-mcp@latest"
      ],
      "env": {
        "MEMOS_API_KEY": "mpg-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "MEMOS_USER_ID": "your-user-id",
        "MEMOS_CHANNEL": "MODELSCOPE"
      }
    }
  }
}
```

环境变量获取方式：
- `MEMOS_API_KEY`: 在MemOS官网[API控制台](https://memos-dashboard.openmem.net/cn/apikeys/)上注册账号，然后在接口密钥页面新建api-key并复制粘贴在此处。
![在MemOS API控制台上新建api-key](/mcp-assets/eb10846fe2c7ef12ea098d6896444300.png)
- `MEMOS_USER_ID`: 确定性的用户自定义个人标识符。
  - 对于同一用户，该环境变量需要在不同设备/客户端中保持一致；
  - 请不要使用随机值、设备ID或聊天会话ID作为用户标识符；
  - 推荐使用：个人email地址、姓名全称或员工ID作为用户标识符。
- `MEMOS_CHANNEL`: 填写"MODELSCOPE"即可。

### 在Claude Desktop中使用
在Claude Desktop中使用MemOS，需点击左下角头像 -> "Settings" -> "Developer" -> "Edit Config"， 并粘贴[配置](#configuration)到Claude_desktop_config.json文件中，最后重启客户端，观察到memos-api-mcp服务处于running状态即可在聊天中使用。

![在Claude中使用MemOS-验证](/mcp-assets/ad71b0b39f1f68b4a0c7e2337f3d93cf.png)

为了提升使用效果，建议用户在Claude Desktop中使用MemOS时修改作用于所有对话的用户偏好设置，具体方法为点击左下角头像 -> "General", 在"What personal preferences shold Claude consider in responses?"下面的输入框中粘贴如下内容：

```
你是MemOS记忆管理助手，致力于提供高效的记忆管理服务，基于用户过往的对话内容抽取记忆，并通过记忆检索提升用户与AI对话的一致性和个性化水平。在每次回答用户的问题之前，你需要调用memos-api-mcp的search_memory服务，利用恰当的检索词在用户的个人记忆库中搜索和当前话题有关的记忆。在基于这些记忆完成回答后，再调用memos-api-mcp的add_message服务，将当前对话内容摘要记录下来。（请注意，调用add_message这一步是必须进行的，无论用户说了什么或问了什么问题都要记录下来，否则在后续的对话中，search_memory将无法获取到更细致的用户信息，进而导致你不能准确地回答用户问题。）
```

![在Claude Desktop中使用MemOS-修改用户偏好](/mcp-assets/e185e4e389c3dc84af37071daa514570.png)

下面是在Claude Desktop中使用MemOS的示例，用户可借此判断是否已经成功在Claude Desktop中配置MemOS。

![在Claude Desktop中使用MemOS的示例](/mcp-assets/6c74dd7f199a0d59de9d52ef719d5327.png)

### 在Cursor中使用
在Cursor中使用MemOS，需进入"Cursor Settings" -> "Tools & MCP" -> "Add Custom MCP"(或"New MCP Server"), 并在弹出的mcp.json文件编辑页中粘贴[配置](#configuration)，观察到memos-api-mcp处于启动状态，且能够在工具详情页面看到"add_message""search_memory"等若干工具，即可在Cursor聊天面板中使用。

![在Cursor中使用MemOS](/mcp-assets/fce6a250b7f1b069f1fd188756984858.png)

为了提升使用效果，建议用户在Cursor中使用MemOS时修改User Rules，具体方法为进入"Cursor Settings" -> "Rules, Memories, Commands" -> "User Rules" -> "+ Add Rule", 然后将下面的内容复制粘贴后保存：
```
你是MemOS记忆管理助手，致力于提供高效的记忆管理服务，基于用户过往的对话内容抽取记忆，并通过记忆检索提升用户与AI对话的一致性和个性化水平。在每次回答用户的问题之前，你需要调用memos-api-mcp的search_memory服务，利用恰当的检索词在用户的个人记忆库中搜索和当前话题有关的记忆。在基于这些记忆完成回答后，再调用memos-api-mcp的add_message服务，将当前对话内容摘要记录下来。（请注意，调用add_message这一步是必须进行的，无论用户说了什么或问了什么问题都要记录下来，否则在后续的对话中，search_memory将无法获取到更细致的用户信息，进而导致你不能准确地回答用户问题。）
```

![在Cursor中使用MemOS-配置User rules](/mcp-assets/56c5ccbe9a6f0000af97e6af3cb5b95c.png)

下面是在Cursor中使用MemOS的示例，用户可借此判断是否成功在Cursor中配置MemOS。

![在Cursor中使用MemOS-使用示例](/mcp-assets/4e5eb56b559c5a41f224ad6ac10ebd1b.png)

### 在Visual Studio Code或Trae中使用
在VS Code或Trae中使用MemOS，需安装Cline扩展并进行模型配置后，点击Cline面板内部右上角的"MCP Servers"图标 -> "Configure" -> "Configure MCP Servers", 并粘贴[配置](#configuration)到cline_map_settings.json文件中，观察到memos-api-mcp处于启动状态即可在Cline智能体中使用。同时，推荐开启各工具的`Auto-approve`开关，避免智能体每次调用工具前询问，使用更流畅。
![在Cline中使用MemOS-配置流程](/mcp-assets/95c2114645a7c0c4d16363fa69a0b9b9.png)

为了提升使用效果，建议用户在Cline中使用MemOS时修改global rules，具体方法为点击Cline面板左下角的"Manage Cline Rules & Workflows" 图标 -> 点击Global Rules下方右侧的"＋"图标 -> 在输入框内输入rules文件名，如"memos_rules.md" -> 将下面的内容复制粘贴到弹出的编辑器内：
```markdown
# 🧠 MemOS Automatic Memory System — Mandatory Usage

## ⚠️ Always-On (No User Opt-In Required)
This system must run **automatically for every turn**. Do **not** wait for the user to say “use memory”, “use MCP”, or “call a tool”. The **client/orchestrator is responsible** for auto-invoking the tools.

## 🎯 Mandatory 3-Step Workflow (Enforced by Client Each Turn)
\`\`\`
Every user message
  → 1) 🔍 search_memory (AUTO, before answering)
  → 2) 💬 Answer (use only relevant memories; ignore noise)
  → 3) 💾 add_message (AUTO, after answering)
\`\`\`

### 1) 🔍 Search Memory (Auto-invoked BEFORE answering)
- **Trigger**: Must be auto-called **before** generating any answer (including simple greetings).
- **Tool**: `search_memory`

**Relevance rule**: The model must judge relevance and **only use relevant** memories. If results are irrelevant or noisy, **ignore them** and proceed.

### 2) 💬 Answer
Use retrieved memories **only if relevant**. If none are relevant, answer normally.

### 3) 💾 Save Conversation (Auto-invoked AFTER answering)
- **Trigger**: Must be auto-called after producing the final answer on **every turn**.
- **Tool**: `add_message`

**Purpose**: Persist Q&A for future personalization and continuity — even if no memory was used this turn.

## ✅ Non-Negotiable Client Responsibilities
1. **Auto-invoke** `search_memory` before **every** answer and `add_message` after **every** answer.
2. **No user opt-in**: Do not wait for the user to mention memory/tools/MCP.
3. **Stable `conversation_id`** across the thread.
4. **Store both user and assistant** messages every turn.
5. **Sequence** must be strictly: Search → Answer → Save.
```

![在VS Code或Trae中使用MemOS-修改global rules](/mcp-assets/cec16a0e7a2943500c2bf794ad7433dd.png)

下面是在Cline中使用MemOS的示例，用户可借此判断是否成功在Cline中配置了MemOS。
![在Cline中使用MemOS的示例](/mcp-assets/73bf30c01d6323d7f2e64154be8ad4fd.png)

### 在[Chatbox](https://chatboxai.app/zh)中使用
在Chatbox中使用MemOS，需点击左下角"设置" -> "MCP" -> "自定义MCP服务器-添加服务器" -> "添加自定义服务器"，按照下面的配置添加memos-api-mcp服务。
```
名称：MemOS记忆管理助手
类型：本地(stdio)
命令：npx -y @memtensor/memos-api-mcp
环境变量：
MEMOS_API_KEY={{在MemOS官网API控制台申请获取的api_key}}
MEMOS_USER_ID={{自定义的USER_ID}}
```
填写完成后点击"测试"，如果能在对话框最下方看到"add_message""search_memory"等若干工具，则证明配置成功。
![在Chatbox中使用MemOS-验证](/mcp-assets/1455449b1686ed701ccf1c0f91e3f861.png)

为了提升使用效果，建议用户在Chatbox中使用MemOS时修改system_prompt，具体方式为左下角"设置" -> "对话设置" -> "新对话默认设置"，并将prompt修改如下：
```
你是MemOS记忆管理助手，致力于提供高效的记忆管理服务，基于用户过往的对话内容抽取记忆，并通过记忆检索提升用户与AI对话的一致性和个性化水平。在每次回答用户的问题之前，你需要调用memos-api-mcp的search_memory服务，利用恰当的检索词在用户的个人记忆库中搜索和当前话题有关的记忆。在基于这些记忆完成回答后，再调用memos-api-mcp的add_message服务，将当前对话内容摘要记录下来。（请注意，调用add_message这一步是必须进行的，无论用户说了什么或问了什么问题都要记录下来，否则在后续的对话中，search_memory将无法获取到更细致的用户信息，进而导致你不能准确地回答用户问题。）
```

![在Chatbox中使用MemOS时修改system_prompt](/mcp-assets/cffd1eeecf273adffdff7b8d40268ea0.png)

下面是在Chatbox中使用MemOS的示例，用户可借此判断是否已经成功在Chatbox中配置MemOS。
![在Chatbox中使用MemOS-效果示例](/mcp-assets/8b7cb7d71749258889b3e5558746823a.png)


## Q&A
Q：有时会遇到智能体在应当使用工具的场景没有使用的情况？

A：由于使用的底层模型不同，不同智能体对工具使用的熟练程度也存在差别，当出现智能体忘记使用工具的情况时可通过指令引导模型调用相应的工具，或尝试使用其他底层模型。

**官方网站：** [https://memos-docs.openmem.net/cn/open_source/modules/mos/memos_mcp](https://memos-docs.openmem.net/cn/open_source/modules/mos/memos_mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`memory`
- 标签：`knowledge and memory`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @memtensor/memos-api-mcp@latest`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/memtensor-memoryoperatingsystem.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
