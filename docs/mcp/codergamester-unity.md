---
title: "mcp-unity"
description: "An implementation of the Model Context Protocol for Unity Editor, allowing AI assistants to interact with Unity projects through tools for executing menu items, selecting objects, managing packages, r…"
---

# mcp-unity

An implementation of the Model Context Protocol for Unity Editor, allowing AI assistants to interact with Unity projects through tools for executing menu items, selecting objects, managing packages, r…

# MCP Unity Editor (Game Engine)

[![](/mcp-assets/d4184d72d7bf151a0d8778c272bd9a4f.svg 'MCP Enabled')](https://modelcontextprotocol.io/introduction)
[![](/mcp-assets/9b700283d756a88564d8b5b453be0905.svg 'Unity')](https://unity.com/releases/editor/archive)
[![](/mcp-assets/148c8c2430c0ccd90f9e06f3c3ea5e04.svg 'Node.js')](https://nodejs.org/en/download/)

[Smithery](https://smithery.ai/server/@CoderGamester/mcp-unity)
[![](/mcp-assets/4d6facd625d9b6e2a16ce8e07e00105a.svg 'Stars')](https://github.com/CoderGamester/mcp-unity/stargazers)
[![](/mcp-assets/001aa60de15e858c5fc854b03602f104.svg 'Forks')](https://github.com/CoderGamester/mcp-unity/network/members)
[![](/mcp-assets/8f9cfbb56c5a2696e6809907d3b704ae.svg 'Last Commit')](https://github.com/CoderGamester/mcp-unity/commits/main)
[![](/mcp-assets/3936e2c22a65da85cb0bf816374d21f8.svg 'MIT License')](https://opensource.org/licenses/MIT)

  

```
                              ,/(/.   *(/,                                  
                          */(((((/.   *((((((*.                             
                     .*((((((((((/.   *((((((((((/.                         
                 ./((((((((((((((/    *((((((((((((((/,                     
             ,/(((((((((((((/*.           */(((((((((((((/*.                
            ,%%#((/((((((*                    ,/(((((/(#&@@(                
            ,%%##%%##((((((/*.             ,/((((/(#&@@@@@@(                
            ,%%######%%##((/(((/*.    .*/(((//(%@@@@@@@@@@@(                
            ,%%####%#(%%#%%##((/((((((((//#&@@@@@@&@@@@@@@@(                
            ,%%####%(    /#%#%%%##(//(#@@@@@@@%,   #@@@@@@@(                
            ,%%####%(        *#%###%@@@@@@(        #@@@@@@@(                
            ,%%####%(           #%#%@@@@,          #@@@@@@@(                
            ,%%##%%%(           #%#%@@@@,          #@@@@@@@(                
            ,%%%#*              #%#%@@@@,             *%@@@(                
            .,      ,/##*.      #%#%@@@@,     ./&@#*      *`                
                ,/#%#####%%#/,  #%#%@@@@, ,/&@@@@@@@@@&.                    
                 `*#########%%%%###%@@@@@@@@@@@@@@@@@@&*´                   
                    `*%%###########%@@@@@@@@@@@@@@&*´                        
                        `*%%%######%@@@@@@@@@@&*´                            
                            `*#%%##%@@@@@&*´                                 
                               `*%#%@&*´                                     
                                                       
     ███╗   ███╗ ██████╗██████╗         ██╗   ██╗███╗   ██╗██╗████████╗██╗   ██╗
     ████╗ ████║██╔════╝██╔══██╗        ██║   ██║████╗  ██║██║╚══██╔══╝╚██╗ ██╔╝
     ██╔████╔██║██║     ██████╔╝        ██║   ██║██╔██╗ ██║██║   ██║    ╚████╔╝ 
     ██║╚██╔╝██║██║     ██╔═══╝         ██║   ██║██║╚██╗██║██║   ██║     ╚██╔╝  
     ██║ ╚═╝ ██║╚██████╗██║             ╚██████╔╝██║ ╚████║██║   ██║      ██║   
     ╚═╝     ╚═╝ ╚═════╝╚═╝              ╚═════╝ ╚═╝  ╚═══╝╚═╝   ╚═╝      ╚═╝   
```

MCP Unity is an implementation of the Model Context Protocol for Unity Editor, allowing AI assistants to interact with your Unity projects. This package provides a bridge between Unity and a Node.js server that implements the MCP protocol, enabling AI agents like Claude, Windsurf, and Cursor to execute operations within the Unity Editor.

## Features
This MCP currently provides the following 
tools
:

- 
**execute_menu_item**
: Executes Unity menu items (functions tagged with the MenuItem attribute)
- 
**select_gameobject**
: Selects game objects in the Unity hierarchy by path or instance ID
- 
**update_component**
: Updates component fields on a GameObject or adds it to the GameObject if it does not contain the component
- 
**add_package**
: Installs new packages in the Unity Package Manager
- 
**run_tests**
: Runs tests using the Unity Test Runner
- 
**notify_message**
: Displays messages in the Unity Editor

This MCP currently provides the following 
resources
:

- 
**get_menu_items**
: Retrieves a list of all available menu items in the Unity Editor to facilitate 
**execute_menu_item**
 tool
- 
**get_hierarchy**
: Retrieves a list of all game objects in the Unity hierarchy
- 
**get_gameobject**
: Retrieves detailed information about a specific GameObject by instance ID, including all GameObject components with it's serialized properties and fields
- 
**get_console_logs**
: Retrieves a list of all logs from the Unity console
- 
**get_packages**
: Retrieves information about installed and available packages from the Unity Package Manager
- 
**get_assets**
: Retrieves information about assets in the Unity Asset Database
- 
**get_tests**
: Retrieves information about tests in the Unity Test Runner

## Requirements
- Unity 2022.3 or later - to [install the server](#install-server)
- Node.js 18 or later - to [start the server](#start-server)
- npm 9 or later - to [debug the server](#debug-server)

## 

Installation

Installing this MCP Unity Server is a multi-step process:

### Step 1: Install Unity MCP Server package via Unity Package Manager
1. Open the Unity Package Manager (Window > Package Manager)
2. Click the "+" button in the top-left corner
3. Select "Add package from git URL..."
4. Enter: `https://github.com/CoderGamester/mcp-unity.git`
5. Click "Add"

### Step 2: Install Node.js 
> To run MCP Unity server, you'll need to have Node.js 18 or later installed on your computer:

Windows

1. Visit the [Node.js download page](https://nodejs.org/en/download/)
2. Download the Windows Installer (.msi) for the LTS version (recommended)
3. Run the installer and follow the installation wizard
4. Verify the installation by opening PowerShell and running:
```bash
   node --version
```

macOS

1. Visit the [Node.js download page](https://nodejs.org/en/download/)
2. Download the macOS Installer (.pkg) for the LTS version (recommended)
3. Run the installer and follow the installation wizard
4. Alternatively, if you have Homebrew installed, you can run:
```bash
   brew install node@18
```
5. Verify the installation by opening Terminal and running:
```bash
   node --version
```

### Step 3: Configure AI LLM Client

Option 1: Configure using Unity Editor

1. Open the Unity Editor
2. Navigate to Tools > MCP Unity > Server Window
3. Click on the "Configure" button for your AI LLM client as shown in the image below

4. Confirm the configuration installation with the given popup

Option 2: Configure via Smithery

To install MCP Unity via [Smithery](https://smithery.ai/server/@CoderGamester/mcp-unity):

```
Currently not available
```

Option 3: Configure Manually

Open the MCP configuration file of your AI client (e.g. claude_desktop_config.json in Claude Desktop) and copy the following text:

> Replace `ABSOLUTE/PATH/TO` with the absolute path to your MCP Unity installation or just copy the text from the Unity Editor MCP Server window (Tools > MCP Unity > Server Window).

```json
{
   "mcpServers": {
   "mcp-unity": {
      "command": "node",
      "args": [
         "ABSOLUTE/PATH/TO/mcp-unity/Server/build/index.js"
      ],
      "env": {
         "UNITY_PORT": "8090"
      }
   }
   }
}
```

## 

Start Unity Editor MCP Server
1. Open the Unity Editor
2. Navigate to Tools > MCP Unity > Server Window
3. Click "Start Server" to start the WebSocket server
4. Open Claude Desktop or your AI Coding IDE (e.g. Cursor IDE, Windsurf IDE, etc.) and start executing Unity tools
   

> When the AI client connects to the WebSocket server, it will automatically show in the green box in the window

## Optional: Set WebSocket Port
By default, the WebSocket server runs on port 8090. You can change this port in two ways:

Option 1: Using the Unity Editor

1. Open the Unity Editor
2. Navigate to Tools > MCP Unity > Server Window
3. Change the "WebSocket Port" value to your desired port number
4. Unity will setup the system environment variable UNITY_PORT to the new port number
5. Restart the Node.js server
6. Click again on "Start Server" to reconnect the Unity Editor web socket to the Node.js MCP Server

Option 2: Using the terminal

1. Set the UNITY_PORT environment variable in the terminal
   - Powershell
```powershell
   $env:UNITY_PORT = "8090"
```
   - Command Prompt/Terminal
```cmd
   set UNITY_PORT=8090
```
2. Restart the Node.js server
3. Click again on "Start Server" to reconnect the Unity Editor web socket to the Node.js MCP Server

## 

Debugging the Server

Building the Node.js Server

The MCP Unity server is built using Node.js . It requires to compile the TypeScript code to JavaScript in the `build` directory.
To build the server, open a terminal and:

1. Navigate to the Server directory:
```bash
   cd ABSOLUTE/PATH/TO/mcp-unity/Server
```

2. Install dependencies:
```bash
   npm install
```

3. Build the server:
```bash
   npm run build
```

4. Run the server:
```bash
   node build/index.js
```

   

Debugging with MCP Inspector

Debug the server with [@modelcontextprotocol/inspector](https://github.com/modelcontextprotocol/inspector):
   - Powershell
```powershell
   $env:UNITY_PORT=8090; npx @modelcontextprotocol/inspector node Server/build/index.js
```
   - Command Prompt/Terminal
```cmd
   set UNITY_PORT=8090 && npx @modelcontextprotocol/inspector node Server/build/index.js
```

Don't forget to shutdown the server with `Ctrl + C` before closing the terminal or debugging it with the [MCP Inspector](https://github.com/modelcontextprotocol/inspector).

Enable Console Logs

1. Enable logging on your terminal or into a log.txt file:
   - Powershell
```powershell
   $env:LOGGING = "true"
   $env:LOGGING_FILE = "true"
```
   - Command Prompt/Terminal
```cmd
   set LOGGING=true
   set LOGGING_FILE=true
```

## Troubleshooting

Connection Issues

- Ensure the WebSocket server is running (check the Server Window in Unity)
- Check if there are any firewall restrictions blocking the connection
- Make sure the port number is correct (default is 8080)
- Change the port number in the Unity Editor MCP Server window. (Tools > MCP Unity > Server Window)

Server Not Starting

- Check the Unity Console for error messages
- Ensure Node.js is properly installed and accessible in your PATH
- Verify that all dependencies are installed in the Server directory

Menu Items Not Executing

- Ensure the menu item path is correct (case-sensitive)
- Check if the menu item requires confirmation
- Verify that the menu item is available in the current context

## Support & Feedback

If you have any questions or need support, please open an [issue](https://github.com/CoderGamester/mcp-unity/issues) on this repository.

Alternative you can reach out on:
- [![](/mcp-assets/b6f093496278e747d7449e7eb9b6142c.svg 'LinkedIn')](https://www.linkedin.com/in/miguel-tomas/)
- Discord: gamester7178

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue with your request.

**Commit your changes** following the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) format.

## License

This project is under [MIT License](https://github.com/codergamester/mcp-unity/blob/HEAD/LICENSE.md)

**Official site: ** [https://github.com/codergamester/mcp-unity](https://github.com/codergamester/mcp-unity)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `developer tools`, `virtualization`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `node`
- Args: `ABSOLUTE/PATH/TO/mcp-unity/Server/build/index.js`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/codergamester-unity.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
