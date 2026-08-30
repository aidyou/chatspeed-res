---
title: "Desktop Commander"
description: "Desktop Commander MCP Search, update, manage files and run terminal commands with AI Work with code and text, run processes, and automate tasks, going far beyond other AI editors - while using host client subscriptions i"
---

# Desktop Commander

Desktop Commander MCP Search, update, manage files and run terminal commands with AI Work with code and text, run processes, and automate tasks, going far beyond other AI editors - while using host client subscriptions i

# Desktop Commander MCP
### Search, update, manage files and run terminal commands with AI


[![AgentAudit Verified](https://agentaudit.dev/api/badge/desktop-commander)](https://agentaudit.dev/skills/desktop-commander)
[![Trust Score](https://archestra.ai/mcp-catalog/api/badge/quality/wonderwhy-er/DesktopCommanderMCP)](https://archestra.ai/mcp-catalog/wonderwhy-er__desktopcommandermcp)


Work with code and text, run processes, and automate tasks, going far beyond other AI editors - while using host client subscriptions instead of API token costs.

  

## 🖥️ Try the Desktop Commander App (Beta)

**Want a better experience?** The Desktop Commander App gives you everything the MCP server does, plus:

- **Use any AI model** — Claude, GPT-4.5, Gemini 2.5, or any model you prefer
- **See file changes live** — visual file previews as AI edits your files
- **Add custom MCPs and context** — extend with your own tools, no config files
- **Coming soon** — skills system, dictation, background scheduled tasks, and more

**👉 [Download the App](https://desktopcommander.app/#download)** (macOS & Windows)

> The MCP server below still works great with Claude Desktop and other MCP clients — the app is for those who want a dedicated, polished experience.

## Table of Contents
- [Features](#features)
- [How to install](#how-to-install)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [File Preview UI & Markdown Editor](#file-preview-ui--markdown-editor)
- [Handling Long-Running Commands](#handling-long-running-commands)
- [Work in Progress and TODOs](#roadmap)
- [Sponsors and Supporters](#support-desktop-commander)
- [Website](#website)
- [Media](#media)
- [Testimonials](#testimonials)
- [Frequently Asked Questions](#frequently-asked-questions)
- [Contributing](#contributing)
- [License](#license)

All of your AI development tools in one place.
Desktop Commander puts all dev tools in one chat.
Execute long-running terminal commands on your computer and manage processes through Model Context Protocol (MCP). Built on top of [MCP Filesystem Server](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) to provide additional search and replace file editing capabilities.

## Features

- **Remote AI Control** - Use Desktop Commander from ChatGPT, Claude web, and other AI services via [Remote MCP](https://mcp.desktopcommander.app)
- **File Preview UI** - Visual file previews in Claude Desktop with rendered markdown, inline images, expandable content, built-in markdown editor, and quick "Open in folder" access
- **Enhanced terminal commands with interactive process control**
- **Execute code in memory (Python, Node.js, R) without saving files**
- **Instant data analysis - just ask to analyze CSV/JSON/Excel files**
- **Native Excel file support** - Read, write, edit, and search Excel files (.xlsx, .xls, .xlsm) without external tools
- **PDF support** - Read PDFs with text extraction, create new PDFs from markdown, modify existing PDFs
- **DOCX support** - Read, create, edit, and search Word documents (.docx) with surgical XML editing and markdown-to-DOCX conversion
- **Interact with running processes (SSH, databases, development servers)**
- Execute terminal commands with output streaming
- Command timeout and background execution support
- Process management (list and kill processes)
- Session management for long-running commands
- **Process output pagination** - Read terminal output with offset/length controls to prevent context overflow
- Server configuration management:
  - Get/set configuration values
  - Update multiple settings at once
  - Dynamic configuration changes without server restart
- Full filesystem operations:
  - Read/write files (text, Excel, PDF, DOCX)
  - Create/list directories
  - **Recursive directory listing** with configurable depth and context overflow protection for large folders
  - Move files/directories
  - Search files and content (including Excel content)
  - Get file metadata
  - **Negative offset file reading**: Read from end of files using negative offset values (like Unix tail)
- Code editing capabilities:
  - Surgical text replacements for small changes
  - Full file rewrites for major changes
  - Multiple file support
  - Pattern-based replacements
  - vscode-ripgrep based recursive code or text search in folders
- Comprehensive audit logging:
  - All tool calls are automatically logged
  - Log rotation with 10MB size limit
  - Detailed timestamps and arguments
- Safety guardrails (not a sandbox — see [SECURITY.md](https://github.com/wonderwhy-er/DesktopCommanderMCP/blob/HEAD/SECURITY.md)):
  - Symlink traversal prevention on file operations
  - Command blocklist for accidental execution
  - [Docker isolation](#option-6-docker-installation--auto-updates-no-nodejs-required) for complete isolation

## How to install

### Install in Claude Desktop

Desktop Commander offers multiple installation methods for Claude Desktop.

> **📋 Update & Uninstall Information:** Options 1, 2, 3, 4, and 6 have automatic updates. Option 5 requires manual updates. See below for details.

Option 1: Install through npx ⭐ Auto-Updates (Requires Node.js)

Just run this in terminal:
```
npx @wonderwhy-er/desktop-commander@latest setup
```

For debugging mode (allows Node.js inspector connection):
```
npx @wonderwhy-er/desktop-commander@latest setup --debug
```

**Command line options during setup:**
- `--debug`: Enable debugging mode for Node.js inspector
- `--no-onboarding`: Disable onboarding prompts for new users

Restart Claude if running.

**✅ Auto-Updates:** Yes - automatically updates when you restart Claude  
**🔄 Manual Update:** Run the setup command again  
**🗑️ Uninstall:** Run `npx @wonderwhy-er/desktop-commander@latest remove`

Option 2: Using bash script installer (macOS) ⭐ Auto-Updates (Installs Node.js if needed)

```
curl -fsSL https://raw.githubusercontent.com/wonderwhy-er/DesktopCommanderMCP/refs/heads/main/install.sh | bash
```
This script handles all dependencies and configuration automatically.

**✅ Auto-Updates:** Yes  
**🔄 Manual Update:** Re-run the bash installer command above  
**🗑️ Uninstall:** Run `npx @wonderwhy-er/desktop-commander@latest remove`

Option 3: Installing via Smithery ⭐ Auto-Updates (Requires Node.js)

1. **Visit:** https://smithery.ai/server/@wonderwhy-er/desktop-commander
2. **Login to Smithery** if you haven't already
3. **Select your client** (Claude Desktop) on the right side
4. **Install with the provided key** that appears after selecting your client
5. **Restart Claude Desktop**

**✅ Auto-Updates:** Yes - automatically updates when you restart Claude  
**🔄 Manual Update:** Visit the Smithery page and reinstall  

Option 4: Add to claude_desktop_config manually ⭐ Auto-Updates (Requires Node.js)

Add this entry to your claude_desktop_config.json:

- On Mac: `~/Library/Application Support/Claude/claude_desktop_config.json`
- On Windows: `%APPDATA%\Claude\claude_desktop_config.json`
- On Linux: `~/.config/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "desktop-commander": {
      "command": "npx",
      "args": [
        "-y",
        "@wonderwhy-er/desktop-commander@latest"
      ]
    }
  }
}
```
Restart Claude if running.

**✅ Auto-Updates:** Yes - automatically updates when you restart Claude  
**🔄 Manual Update:** Run the setup command again  
**🗑️ Uninstall:** Run `npx @wonderwhy-er/desktop-commander@latest remove` or remove the entry from your claude_desktop_config.json

Option 5: Checkout locally ❌ Manual Updates (Requires Node.js)

```bash
git clone https://github.com/wonderwhy-er/DesktopCommanderMCP.git
cd DesktopCommanderMCP
npm run setup
```
Restart Claude if running.

The setup command will install dependencies, build the server, and configure Claude's desktop app.

**❌ Auto-Updates:** No - requires manual git updates  
**🔄 Manual Update:** `cd DesktopCommanderMCP && git pull && npm run setup`  
**🗑️ Uninstall:** Run `npx @wonderwhy-er/desktop-commander@latest remove` or remove the cloned directory and MCP server entry from Claude config

Option 6: Docker Installation 🐳 ⭐ Auto-Updates (No Node.js Required)

Perfect for users who want isolation or don't have Node.js installed. Runs in a sandboxed Docker container with a persistent work environment.

**Prerequisites:** [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed **and running**, Claude Desktop app installed.

**macOS/Linux:**
```bash
bash 
Manual Docker Configuration

**Basic setup (no file access):**
```json
{
  "mcpServers": {
    "desktop-commander-in-docker": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "mcp/desktop-commander:latest"]
    }
  }
}
```

**With folder mounting:**
```json
{
  "mcpServers": {
    "desktop-commander-in-docker": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "-v", "/Users/username/Desktop:/mnt/desktop",
        "-v", "/Users/username/Documents:/mnt/documents",
        "mcp/desktop-commander:latest"
      ]
    }
  }
}
```

**Advanced folder mounting:**
```json
{
  "mcpServers": {
    "desktop-commander-in-docker": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "-v", "dc-system:/usr",
        "-v", "dc-home:/root", 
        "-v", "dc-workspace:/workspace",
        "-v", "dc-packages:/var",
        "-v", "/Users/username/Projects:/mnt/Projects",
        "-v", "/Users/username/Downloads:/mnt/Downloads",
        "mcp/desktop-commander:latest"
      ]
    }
  }
}
```

Docker Management Commands

**macOS/Linux:**
```bash
# Check status
bash 

**✅ Auto-Updates:** Yes - `latest` tag automatically gets newer versions  
**🔄 Manual Update:** `docker pull mcp/desktop-commander:latest` then restart Claude  

### Install in Other Clients

Desktop Commander works with any MCP-compatible client. The standard JSON configuration is:

```json
{
  "mcpServers": {
    "desktop-commander": {
      "command": "npx",
      "args": ["-y", "@wonderwhy-er/desktop-commander@latest"]
    }
  }
}
```

Add this to your client's MCP configuration file at the locations below:

Cursor

[![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en-US/install-mcp?name=desktop-commander&config=eyJjb21tYW5kIjoibnB4IiwiYXJncyI6WyIteSIsIkB3b25kZXJ3aHktZXIvZGVza3RvcC1jb21tYW5kZXJAbGF0ZXN0Il19)

[View MCP Server in Directory](https://cursor.directory/mcp/desktop-commander-mcp)

Or add manually to `~/.cursor/mcp.json` (global) or `.cursor/mcp.json` in your project folder (project-specific).

See [Cursor MCP docs](https://docs.cursor.com/context/model-context-protocol) for more info.

Windsurf

Add to `~/.codeium/windsurf/mcp_config.json`. See [Windsurf MCP docs](https://docs.windsurf.com/windsurf/cascade/mcp) for more info.

VS Code / GitHub Copilot

Add to `.vscode/mcp.json` in your project or VS Code User Settings (JSON). Make sure MCP is enabled under Chat > MCP. Works in Agent mode.

See [VS Code MCP docs](https://code.visualstudio.com/docs/copilot/chat/mcp-servers) for more info.

Cline

Configure through the Cline extension settings in VS Code. Open the Cline sidebar, click the MCP Servers icon, and add the JSON configuration above. See [Cline MCP docs](https://docs.cline.bot/mcp/configuring-mcp-servers) for more info.

Roo Code

Add to your Roo Code MCP configuration file. See [Roo Code MCP docs](https://docs.roocode.com/features/mcp/using-mcp-in-roo) for more info.

Claude Code

```sh
claude mcp add --scope user desktop-commander -- npx -y @wonderwhy-er/desktop-commander@latest
```

Remove `--scope user` to install for the current project only. See [Claude Code MCP docs](https://docs.anthropic.com/en/docs/claude-code/mcp) for more info.

Trae

Use the "Add manually" feature and paste the JSON configuration above. See [Trae MCP docs](https://docs.trae.ai/ide/model-context-protocol?_lang=en) for more info.

Kiro

Navigate to `Kiro` > `MCP Servers`, click `+ Add`, and paste the JSON configuration above. See [Kiro MCP docs](https://kiro.dev/docs/mcp/configuration/) for more info.

Codex (OpenAI)

Codex uses TOML configuration. Run this command to add Desktop Commander:

```sh
codex mcp add desktop-commander -- npx -y @wonderwhy-er/desktop-commander@latest
```

Or manually add to `~/.codex/config.toml`:

```toml
[mcp_servers.desktop-commander]
command = "npx"
args = ["-y", "@wonderwhy-er/desktop-commander@latest"]
```

See [Codex MCP docs](https://developers.openai.com/codex/mcp/) for more info.

JetBrains (AI Assistant)

In JetBrains IDEs, go to **Settings → Tools → AI Assistant → Model Context Protocol (MCP)**, click `+` Add, select **As JSON**, and paste the JSON configuration above. See [JetBrains MCP docs](https://www.jetbrains.com/help/ai-assistant/configure-an-mcp-server.html) for more info.

Gemini CLI

Add to `~/.gemini/settings.json`:

```json
{
  "mcpServers": {
    "desktop-commander": {
      "command": "npx",
      "args": ["-y", "@wonderwhy-er/desktop-commander@latest"]
    }
  }
}
```

See [Gemini CLI docs](https://github.com/google-gemini/gemini-cli) for more info.

Augment Code

Press `Cmd/Ctrl+Shift+P`, open the Augment panel, and add a new MCP server named `desktop-commander` with the JSON configuration above. See [Augment Code MCP docs](https://docs.augmentcode.com/setup-augment/mcp) for more info.

Qwen Code

Run this command to add Desktop Commander:

```sh
qwen mcp add desktop-commander -- npx -y @wonderwhy-er/desktop-commander@latest
```

Or add to `.qwen/settings.json` (project) or `~/.qwen/settings.json` (global). See [Qwen Code MCP docs](https://qwenlm.github.io/qwen-code-docs/en/developers/tools/mcp-server/) for more info.

ChatGPT / Claude Web (Remote MCP)

Use Desktop Commander from **ChatGPT**, **Claude web**, and other AI services via Remote MCP — no desktop app required.

**👉 [Get started at mcp.desktopcommander.app](https://mcp.desktopcommander.app)**

How it works:
1. You run a lightweight **Remote Device** on your computer
2. It connects securely to the cloud Remote MCP service
3. Your AI sends commands through the cloud to your device
4. Commands execute locally, results return to your AI
5. **You stay in control** — stop anytime with `Ctrl+C`

### Security

- ✅ Device only runs when you start it
- ✅ Commands execute under your user permissions
- ✅ Secure OAuth authentication and encrypted communication channel

## Updating & Uninstalling Desktop Commander

### Automatic Updates (Options 1, 2, 3, 4 & 6)
**Options 1 (npx), Option 2 (bash installer), 3 (Smithery), 4 (manual config), and 6 (Docker)** automatically update to the latest version whenever you restart Claude. No manual intervention needed.

### Manual Updates (Option 5)
- **Option 5 (local checkout):** `cd DesktopCommanderMCP && git pull && npm run setup`

### Uninstalling Desktop Commander
#### 🤖 Automatic Uninstallation (Recommended)

The easiest way to completely remove Desktop Commander:

```bash
npx @wonderwhy-er/desktop-commander@latest remove
```

This automatic uninstaller will:
- ✅ Remove Desktop Commander from Claude's MCP server configuration
- ✅ Create a backup of your Claude config before making changes
- ✅ Provide guidance for complete package removal
- ✅ Restore from backup if anything goes wrong

#### 🔧 Manual Uninstallation

If the automatic uninstaller doesn't work or you prefer manual removal:

##### Remove from Claude Configuration

1. **Locate your Claude Desktop config file:**
  - **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
  - **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
  - **Linux:** `~/.config/Claude/claude_desktop_config.json`

2. **Edit the config file:**
  - Open the file in a text editor
  - Find and remove the `"desktop-commander"` entry from the `"mcpServers"` section
  - Save the file

  **Example - Remove this section:**
```json
  {
      "desktop-commander": {
        "command": "npx",
        "args": ["@wonderwhy-er/desktop-commander@latest"]
      }
  }
```

Close and restart Claude Desktop to complete the removal.

#### 🆘 Troubleshooting

**If automatic uninstallation fails:**
- Use manual uninstallation as a fallback

**If Claude won't start after uninstalling:**
- Restore the backup config file created by the uninstaller
- Or manually fix the JSON syntax in your claude_desktop_config.json

**Need help?**
- Join our Discord community: https://discord.com/invite/kQ27sNnZr7

## Getting Started

Once Desktop Commander is installed and Claude Desktop is restarted, you're ready to supercharge your Claude experience!

### 🚀 New User Onboarding

Desktop Commander includes intelligent onboarding to help you discover what's possible:

**For New Users:** When you're just getting started (fewer than 10 successful commands), Claude will automatically offer helpful getting-started guidance and practical tutorials after you use Desktop Commander successfully.

**Request Help Anytime:** You can ask for onboarding assistance at any time by simply saying:
- *"Help me get started with Desktop Commander"*
- *"Show me Desktop Commander examples"* 
- *"What can I do with Desktop Commander?"*

Claude will then show you beginner-friendly tutorials and examples, including:
- 📁 Organizing your Downloads folder automatically
- 📊 Analyzing CSV/Excel files with Python
- ⚙️ Setting up GitHub Actions CI/CD
- 🔍 Exploring and understanding codebases
- 🤖 Running interactive development environments

## Usage

The server provides a comprehensive set of tools organized into several categories:

### Available Tools

| Category | Tool | Description |
|----------|------|-------------|
| **Configuration** | `get_config` | Get the complete server configuration as JSON (includes blockedCommands, defaultShell, allowedDirectories, fileReadLineLimit, fileWriteLineLimit, telemetryEnabled) |
| | `set_config_value` | Set a specific configuration value by key. Available settings: 
• `blockedCommands`: Array of shell commands that cannot be executed
• `defaultShell`: Shell to use for commands (e.g., bash, zsh, powershell)
• `allowedDirectories`: Array of filesystem paths the server can access for file operations (⚠️ terminal commands can still access files outside these directories)
• `fileReadLineLimit`: Maximum lines to read at once (default: 1000)
• `fileWriteLineLimit`: Maximum lines to write at once (default: 50)
• `telemetryEnabled`: Enable/disable telemetry (boolean) |
| **Terminal** | `start_process` | Start programs with smart detection of when they're ready for input |
| | `interact_with_process` | Send commands to running programs and get responses |
| | `read_process_output` | Read output from running processes |
| | `force_terminate` | Force terminate a running terminal session |
| | `list_sessions` | List all active terminal sessions |
| | `list_processes` | List all running processes with detailed information |
| | `kill_process` | Terminate a running process by PID |
| **Filesystem** | `read_file` | Read contents from local filesystem, URLs, Excel files (.xlsx, .xls, .xlsm), and PDFs with line/page-based pagination |
| | `read_multiple_files` | Read multiple files simultaneously |
| | `write_file` | Write file contents with options for rewrite or append mode. Supports Excel files (JSON 2D array format). For PDFs, use `write_pdf` |
| | `write_pdf` | Create new PDF files from markdown or modify existing PDFs (insert/delete pages). Supports HTML/CSS styling and SVG graphics |
| | `create_directory` | Create a new directory or ensure it exists |
| | `list_directory` | Get detailed recursive listing of files and directories (supports depth parameter, default depth=2) |
| | `move_file` | Move or rename files and directories |
| | `start_search` | Start streaming search for files by name or content patterns (searches text files and Excel content) |
| | `get_more_search_results` | Get paginated results from active search with offset support |
| | `stop_search` | Stop an active search gracefully |
| | `list_searches` | List all active search sessions 

**官方网站：** [https://github.com/wonderwhy-er/DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`files`
- 标签：`file systems`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`@wonderwhy-er/desktop-commander@0.2.34`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/wonderwhy-er-desktop-commander.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
