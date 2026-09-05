---
title: "MemoryOperatingSystem"
description: "MemOS Memory Management Assistant Service Overview MemOS Memory Management is a powerful plugin that allows users to access the memory addition and search functions of MemOS. It can store and retrieve…"
---

# MemoryOperatingSystem

MemOS Memory Management Assistant Service Overview MemOS Memory Management is a powerful plugin that allows users to access the memory addition and search functions of MemOS. It can store and retrieve…

# MemOS Memory Management Assistant

## Service Overview

MemOS Memory Management is a powerful plugin that allows users to access the memory addition and search functions of MemOS. It can store and retrieve conversation content, providing efficient memory management services to enhance the consistency and personalization level of user-AI interactions.

## Links
- MemOS Official Website: https://memos.openmem.net/cn/
- MemOS Github: https://github.com/MemTensor/MemOS

## Tool Introduction
- **search_memory**: This tool is used to query the user's memory data, returning the most relevant snippets. It supports real-time retrieval during user-AI conversations and global searches across the entire memory. It can be used for creating user profiles or supporting personalized recommendations. Parameters required include conversation ID, user ID, and query text, with an option to set the number of returned memory items.
- **add_message**: This tool allows the batch import of one or more messages into the MemOS memory storage database, making them retrievable in future conversations. It supports chat history management, user behavior tracking, and personalized interactions. When using this tool, you need to specify the conversation ID, message content, sender role, conversation time, and user ID.
- **delete_memory**: This tool is used to delete specific memories based on their IDs. You need to provide a list of user IDs and a list of memory IDs to be deleted.
- **add_feedback**: This tool is used to submit user feedback to the MemOS system. Required parameters include the user identifier, session unique identifier, and the specific content of the feedback. Additionally, optional parameters such as Agent ID, App ID, feedback time, whether public access is allowed, and a list of knowledge base IDs for writing are supported.
- **get_user_profile**: This tool is used to obtain a full-dimensional memory profile of the user, returning factual memories, preference information, and tool usage traces. It is suitable for identity-related questions like "Who am I?" and "What are my preferences?". You can set whether to include preferences, tool traces, and pagination parameters (page number and items per page).
- **create_knowledge_base**: This tool is used to create a knowledge base container, facilitating the management of documents by project or domain. You need to provide the name of the knowledge base, and optionally, a description.
- **remove_knowledge_base**: This tool is used to remove no longer needed knowledge bases and their associated content.
- **add_kb_document**: This tool is used to upload documents to a specified knowledge base. It supports local file paths, public URLs, or Base64 encoded content. You need to provide the knowledge base ID and a list of files; each file item can include content, filename, and MIME type in the case of local files.
- **get_kb_documents**: This tool is used to batch retrieve knowledge base document information based on a list of file IDs. You need to provide a list of file IDs.
- **delete_kb_documents**: This tool is used to precisely delete documents from a knowledge base by file ID. You need to provide a list of file IDs.

## Usage

### Configuration
json
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

How to obtain environment variables:
- `MEMOS_API_KEY`: Register an account on the [API Console](https://memos-dashboard.openmem.net/cn/apikeys/) of the MemOS official website, then create a new API key on the interface key page and paste it here.
![Creating a new API key on the MemOS API Console](/mcp-assets/eb10846fe2c7ef12ea098d6896444300.png)
- `MEMOS_USER_ID`: A deterministic, user-defined personal identifier.
  - For the same user, this environment variable needs to remain consistent across different devices/clients;
  - Do not use random values, device IDs, or chat session IDs as user identifiers;
  - Recommended: personal email address, full name, or employee ID as the user identifier.
- `MEMOS_CHANNEL`: Fill in "MODELSCOPE".

### Using in Claude DesktopTo use MemOS in Claude Desktop, click on the avatar at the bottom left -> "Settings" -> "Developer" -> "Edit Config", and paste the [configuration](#configuration) into the Claude_desktop_config.json file. Finally, restart the client and ensure that the memos-api-mcp service is in a running state to start using it in chats.

![Using MemOS in Claude - Verification](/mcp-assets/ad71b0b39f1f68b4a0c7e2337f3d93cf.png)

For better usage, it is recommended that users modify the user preferences applied to all conversations when using MemOS in Claude Desktop. To do this, click on the avatar at the bottom left -> "General", and in the input box under "What personal preferences should Claude consider in responses?", paste the following content:

 
You are a MemOS memory management assistant, dedicated to providing efficient memory management services. Based on the user's past conversation content, you extract memories and enhance the consistency and personalization of the user's interaction with AI through memory retrieval. Before answering the user's questions each time, you need to call the search_memory service of memos-api-mcp, using appropriate search terms to find memories related to the current topic in the user's personal memory library. After completing the response based on these memories, call the add_message service of memos-api-mcp to record a summary of the current conversation. (Please note that calling add_message is mandatory; regardless of what the user says or asks, it must be recorded. Otherwise, in subsequent conversations, search_memory will not be able to obtain more detailed user information, leading to inaccurate answers.)

![Using MemOS in Claude Desktop - Modifying User Preferences](/mcp-assets/e185e4e389c3dc84af37071daa514570.png)

Below is an example of using MemOS in Claude Desktop, which can help users determine if MemOS has been successfully configured in Claude Desktop.

![Example of Using MemOS in Claude Desktop](/mcp-assets/6c74dd7f199a0d59de9d52ef719d5327.png)

### Using in Cursor
To use MemOS in Cursor, go to "Cursor Settings" -> "Tools & MCP" -> "Add Custom MCP" (or "New MCP Server"), and paste the [configuration](#configuration) into the mcp.json file editing page. Ensure that memos-api-mcp is in a started state and that several tools such as "add_message" and "search_memory" are visible on the tool details page, then you can use MemOS in the Cursor chat panel.

![Using MemOS in Cursor](/mcp-assets/fce6a250b7f1b069f1fd188756984858.png)

For better usage, it is recommended that users modify the User Rules when using MemOS in Cursor. To do this, go to "Cursor Settings" -> "Rules, Memories, Commands" -> "User Rules" -> "+ Add Rule", then copy and paste the following content and save:

 
You are a MemOS memory management assistant, dedicated to providing efficient memory management services. Based on the user's past conversation content, you extract memories and enhance the consistency and personalization of the user's interaction with AI through memory retrieval. Before answering the user's questions each time, you need to call the search_memory service of memos-api-mcp, using appropriate search terms to find memories related to the current topic in the user's personal memory library. After completing the response based on these memories, call the add_message service of memos-api-mcp to record a summary of the current conversation. (Please note that calling add_message is mandatory; regardless of what the user says or asks, it must be recorded. Otherwise, in subsequent conversations, search_memory will not be able to obtain more detailed user information, leading to inaccurate answers.)

![Using MemOS in Cursor - Configuring User Rules](/mcp-assets/56c5ccbe9a6f0000af97e6af3cb5b95c.png)

Below is an example of using MemOS in Cursor, which can help users determine if MemOS has been successfully configured in Cursor.

![Using MemOS in Cursor - Usage Example](/mcp-assets/4e5eb56b559c5a41f224ad6ac10ebd1b.png)

### Using in Visual Studio Code or Trae
To use MemOS in VS Code or Trae, install the Cline extension and configure the model. Then, click on the "MCP Servers" icon in the top right corner of the Cline panel -> "Configure" -> "Configure MCP Servers", and paste the [configuration](#configuration) into the cline_map_settings.json file. Ensure that memos-api-mcp is in a started state to use it in the Cline agent. It is also recommended to turn on the `Auto-approve` switch for each tool to avoid the agent asking for permission before each tool call, making the experience smoother.
![Using MemOS in Cline - Configuration Process](/mcp-assets/95c2114645a7c0c4d16363fa69a0b9b9.png)To enhance the usage experience, it is recommended that users modify the global rules when using MemOS in Cline. The specific method is to click on the "Manage Cline Rules & Workflows" icon at the bottom left of the Cline panel -> click on the "+" icon to the right under Global Rules -> enter the name of the rules file in the input box, such as "memos_rules.md" -> copy and paste the following content into the editor that pops up:

# 🧠 MemOS Automatic Memory System — Mandatory Usage

## ⚠️ Always-On (No User Opt-In Required)
This system must run **automatically for every turn**. Do **not** wait for the user to say “use memory”, “use MCP”, or “call a tool”. The **client/orchestrator is responsible** for auto-invoking the tools.

## 🎯 Mandatory 3-Step Workflow (Enforced by Client Each Turn)

Every user message
  → 1) 🔍 search_memory (AUTO, before answering)
  → 2) 💬 Answer (use only relevant memories; ignore noise)
  → 3) 💾 add_message (AUTO, after answering)

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

![Using MemOS in VS Code or Trae - Modify Global Rules](/mcp-assets/cec16a0e7a2943500c2bf794ad7433dd.png)

Below is an example of using MemOS in Cline, which users can use to determine if they have successfully configured MemOS in Cline.
![Example of Using MemOS in Cline](/mcp-assets/73bf30c01d6323d7f2e64154be8ad4fd.png)

### Using in [Chatbox](https://chatboxai.app/zh)
To use MemOS in Chatbox, click on "Settings" at the bottom left -> "MCP" -> "Customize MCP Server - Add Server" -> "Add Custom Server", and add the memos-api-mcp service according to the configuration below.

Name: MemOS Memory Management Assistant
Type: Local (stdio)
Command: npx -y @memtensor/memos-api-mcp
Environment Variables:
MEMOS_API_KEY=`{{API key obtained from the MemOS official website API console}}`
MEMOS_USER_ID=`{{Custom USER_ID}}`

After filling out, click "Test". If you see several tools including "add_message" and "search_memory" at the very bottom of the dialog box, it indicates successful configuration.
![Using MemOS in Chatbox - Verification](/mcp-assets/1455449b1686ed701ccf1c0f91e3f861.png)

To enhance the usage experience, it is recommended that users modify the system_prompt when using MemOS in Chatbox. The specific way is to go to "Settings" at the bottom left -> "Conversation Settings" -> "Default Settings for New Conversations", and modify the prompt as follows:

You are the MemOS Memory Management Assistant, dedicated to providing efficient memory management services. Based on the user's past conversation content, extract memories and improve the consistency and personalization level of the user's dialogue with AI through memory retrieval. Before answering the user's questions each time, you need to call the search_memory service of memos-api-mcp, using appropriate search terms to find memories related to the current topic in the user's personal memory library. After completing the response based on these memories, call the add_message service of memos-api-mcp to record a summary of the current conversation. (Please note that calling add_message is a mandatory step, regardless of what the user says or asks, it must be recorded. Otherwise, in subsequent conversations, search_memory will not be able to obtain more detailed user information, leading to inaccurate answers.)![Modifying system_prompt when using MemOS in Chatbox](/mcp-assets/cffd1eeecf273adffdff7b8d40268ea0.png)

Below is an example of using MemOS in Chatbox, which users can use to determine if MemOS has been successfully configured in Chatbox.
![Example of using MemOS in Chatbox - Effect Demonstration](/mcp-assets/8b7cb7d71749258889b3e5558746823a.png)

## Q&A
Q: Sometimes, the agent does not use the tool when it should. What can be done?

A: Due to the differences in the underlying models used, different agents may vary in their proficiency with using tools. If an agent forgets to use a tool, you can guide the model to call the appropriate tool through instructions, or try using a different underlying model.

**Official site: ** [https://memos-docs.openmem.net/cn/open_source/modules/mos/memos_mcp](https://memos-docs.openmem.net/cn/open_source/modules/mos/memos_mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `memory`
- Tags: `knowledge and memory`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @memtensor/memos-api-mcp@latest`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/memtensor-memoryoperatingsystem.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
