---
title: "UnityMCPIntegration"
description: "A server that enables AI assistants to understand and interact with Unity projects in real-time, providing access to scene hierarchy, project settings, and the ability to execute code directly in the…"
---

# UnityMCPIntegration

A server that enables AI assistants to understand and interact with Unity projects in real-time, providing access to scene hierarchy, project settings, and the ability to execute code directly in the…

# 🚀 Advacned Unity MCP Integration 

[![MCP](/mcp-assets/4ac9d1cb3d9e4c6281ed9c3ef4fdeb70.svg)](https://modelcontextprotocol.io/introduction)
[Smithery](https://smithery.ai/server/@quazaai/unitymcpintegration)
[![Unity](/mcp-assets/7f09525df44b518fff9bc7f6d91f242b.svg)](https://unity.com)
[![Node.js](/mcp-assets/86837d3edb1c91af41de4016c858edda.svg)](https://nodejs.org)
[![TypeScript](/mcp-assets/03500effbf23a69c818017a47f3da738.svg)](https://www.typescriptlang.org)
[![WebSockets](/mcp-assets/9f61a0ada231ddbb474fbe97f3d70b4b.svg)](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)

[![Stars](/mcp-assets/f1ac8d13fab3e12d896778ffab59549c.svg)](https://github.com/quazaai/UnityMCPIntegration/stargazers)
[![Forks](/mcp-assets/eac4d6eec7e3b730931b041a26b0af0b.svg)](https://github.com/quazaai/UnityMCPIntegration/network/members)
[![License](/mcp-assets/5816f652aa1f0cc4eedb21a2f733e09e.svg)](https://github.com/quazaai/UnityMCPIntegration/blob/main/LICENSE)

   alt="Unity MCP Inspector" width="400" align="right" style="margin-left: 20px; margin-bottom: 20px;"/>

This package provides a seamless integration between [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) and Unity Editor, allowing AI assistants to understand and interact with your Unity projects in real-time. With this integration, AI assistants can access information about your scene hierarchy, project settings, and execute code directly in the Unity Editor context.

## 📚 Features
- Browse and manipulate project files directly
- Access real-time information about your Unity project
- Understand your scene hierarchy and game objects
- Execute C# code directly in the Unity Editor
- Monitor logs and errors
- Control the Editor's play mode
- Wait For Code Execution

## 🚀 Getting Started

### Prerequisites

- Unity 2021.3 or later
- Node.js 18+ (for running the MCP server)

### Installation

#### 1. Install Unity Package

You have several options to install the Unity package:

**Option A: Package Manager (Git URL)**
1. Open the Unity Package Manager (`Window > Package Manager`)
2. Click the `+` button and select `Add package from git URL...`
3. Enter the repository URL: `https://github.com/quazaai/UnityMCPIntegration.git`
4. Click `Add`

**Option B: Import Custom Package**
1. Clone this repository or [download it as a unityPackage](https://github.com/quazaai/UnityMCPIntegration/releases)
2. In Unity, go to `Assets > Import Package > Custom Package`
3. Select the `UnityMCPIntegration.unitypackage` file

#### 2. Set up the MCP Server

You have two options to run the MCP server:

**Option A: Run the server directly**

1. Navigate to the `mcpServer (likely 
LibraryPackageCachecom.quaza.unitymcp@d2b8f1260bcamcpServer)` directory
2. Install dependencies:
```
   npm install
```
3. Run the server:
```
   node build/index.js
```

**Option B: Add to MCP Host configuration**

Add the server to your MCP Host configuration for Claude Desktop, Custom Implementation etc

```json
{
  "mcpServers": {
    "unity-mcp-server": {
      "command": "node",
      "args": [
        "path-to-project>\Library\PackageCache\com.quaza.unitymcp@d2b8f1260bca\mcpServer\mcpServer\build\index.js"
      ],
      "env": {
        "MCP_WEBSOCKET_PORT": "5010"
      }
    }
  }
}
```
### Demo Video
[Watch video](https://www.youtube.com/watch?v=GxTlahBXs74)

### Installing via Smithery

To install Unity MCP Integration for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@quazaai/unitymcpintegration):

```bash
npx -y @smithery/cli install @quazaai/unitymcpintegration --client claude
```

### 🔧 Usage

#### Debugging and Monitoring

You can open the MCP Debug window in Unity to monitor the connection and test features:

1. Go to `Window > MCP Debug`
2. Use the debug window to:
   - Check connection status
   - Test code execution
   - View logs
   - Monitor events

#### Available Tools

The Unity MCP integration provides several tools to AI assistants:

##### Unity Editor Tools
- **get_editor_state**: Get comprehensive information about the Unity project and editor state
- **get_current_scene_info**: Get detailed information about the current scene
- **get_game_objects_info**: Get information about specific GameObjects in the scene
- **execute_editor_command**: Execute C# code directly in the Unity Editor
- **get_logs**: Retrieve and filter Unity console logs
- **verify_connection**: Check if there's an active connection to Unity Editor

##### Filesystem Tools
- **read_file**: Read contents of a file in your Unity project
- **read_multiple_files**: Read multiple files at once
- **write_file**: Create or overwrite a file with new content
- **edit_file**: Make targeted edits to existing files with diff preview
- **list_directory**: Get a listing of files and folders in a directory
- **directory_tree**: Get a hierarchical view of directories and files
- **search_files**: Find files matching a search pattern
- **get_file_info**: Get metadata about a specific file or directory
- **find_assets_by_type**: Find all assets of a specific type (e.g. Material, Prefab)
- **list_scripts**: Get a listing of all C# scripts in the project

File paths can be absolute or relative to the Unity project's Assets folder. For example, `"Scenes/MyScene.unity"` refers to `
/Assets/Scenes/MyScene.unity`.

## 🛠️ Architecture

The integration consists of two main components:

1. **Unity Plugin (C#)**: Resides in the Unity Editor and provides access to Editor APIs
2. **MCP Server (TypeScript/Node.js)**: Implements the MCP protocol and communicates with the Unity plugin

Communication between them happens via WebSocket, transferring JSON messages for commands and data.

## File System Access

The Unity MCP integration now includes powerful filesystem tools that allow AI assistants to:

- Browse, read, and edit files in your Unity project
- Create new files and directories
- Search for specific files or asset types
- Analyze your project structure
- Make targeted code changes with diff previews

All file operations are restricted to the Unity project directory for security. The system intelligently handles both absolute and relative paths, always resolving them relative to your project's Assets folder for convenience.

Example usages:
- Get a directory listing: `list_directory(path: "Scenes")`
- Read a script file: `read_file(path: "Scripts/Player.cs")`
- Edit a configuration file: `edit_file(path: "Resources/config.json", edits: [{oldText: "value: 10", newText: "value: 20"}], dryRun: true)`
- Find all materials: `find_assets_by_type(assetType: "Material")`

## 👥 Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

### Development Setup

**Unity Side**:
- Open the project in Unity
- Modify the C# scripts in the `UnityMCPConnection/Editor` directory

**Server Side**:
- Navigate to the `mcpServer` directory
- Install dependencies: `npm install`
- Make changes to the TypeScript files in the `src` directory
- Build the server: `npm run build`
- Run the server: `node build/index.js`

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

If you encounter any issues or have questions, please file an issue on the GitHub repository.

**Official site: ** [https://github.com/quazaai/UnityMCPIntegration](https://github.com/quazaai/UnityMCPIntegration)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `files`
- Tags: `developer tools`, `file systems`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `node`
- Args: `path-to-project>\Library\PackageCache\com.quaza.unitymcp@d2b8f1260bca\mcpServer\mcpServer\build\index.js`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/quazaai-unitymcpintegration.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
