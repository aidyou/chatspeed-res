---
title: "MCPHyperTerminal"
description: "MCP Hyper Terminal MCP Hyper Terminal is a terminal extension tool specifically designed for AI IDE development scenarios. It addresses the shortcomings of AI IDEs when calling external tools, support…"
---

# MCPHyperTerminal

MCP Hyper Terminal MCP Hyper Terminal is a terminal extension tool specifically designed for AI IDE development scenarios. It addresses the shortcomings of AI IDEs when calling external tools, support…

# MCP Hyper Terminal

**MCP Hyper Terminal** is a terminal extension tool specifically designed for AI IDE development scenarios.  
It addresses the shortcomings of AI IDEs when calling external tools, supporting command execution, Git operations, custom commands, and can run almost any terminal script.  
Currently, it supports **macOS** and **Linux** users.

---

## ✨ Features

- 🔧 **Command Execution**: Run terminal commands directly within the IDE  
- 🌀 **Git Integration**: Supports common Git operations (commit, pull, push, etc.)  
- ⚙️ **Custom Commands**: Freely configure shortcut commands to meet personalized needs  
- 📜 **Script Execution**: Can run any Shell / Bash script  
- 🖥️ **Cross-Platform**: Supports macOS and Linux  

---

## 🚀 Use Cases

- Quickly call external tools during AI IDE development  
- Execute Git workflows without leaving the editor  
- Automate project scripts (build, test, deploy)  
- Replace the limited terminal calling capabilities built into the IDE  

---

## ⚙️ Configuring MCP Service

Add the following content to your IDE's configuration file to enable **MCP Hyper Terminal**:

json
{
  "mcpServers": {
    "MCPHyperTerminal": {
      "timeout": 10000,
      "type": "stdio",
      "command": "npx",
      "args": [
        "-y",
        "@mcpshell/command"
      ]
    }
  }
}

**Official site: ** [https://www.npmjs.com/package/@mcpshell/command](https://www.npmjs.com/package/@mcpshell/command)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `files`
- Tags: `developer tools`, `file systems`, `超级终端`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @mcpshell/command`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/aeryking-mcphyperterminal.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
