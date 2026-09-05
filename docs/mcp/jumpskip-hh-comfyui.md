---
title: "hh-mcp-comfyui"
description: "This is a ComfyUI image generation service based on the Model Context Protocol (MCP), which generates images by calling the local ComfyUI instance through an API."
---

# hh-mcp-comfyui

This is a ComfyUI image generation service based on the Model Context Protocol (MCP), which generates images by calling the local ComfyUI instance through an API.

# ComfyUI MCP Service

![English](/mcp-assets/61f5c8da326274e25c6808773dea795f.svg)

![Python 3.12+](/mcp-assets/5142151145d2dd1ac338bb460f878742.svg)
![License](/mcp-assets/5816f652aa1f0cc4eedb21a2f733e09e.svg)

This is a ComfyUI image generation service based on the Model Context Protocol (MCP), which generates images by calling the local ComfyUI instance through API.

## Features

- Provides image generation services via the MCP protocol, enabling natural language to generate images freely
- Supports dynamic replacement of prompts and dimensions in workflows
- Automatically loads workflow files from the workflows directory as resources

## Changelog
- [2025-06-29] Support for kontext image editing workflows

- [2025-05-11] Support for dynamically configuring the workflow file directory
- [2025-05-09] Added Docker build method, supports Python 3.12+
- [2025-05-07] Added pip build method
- [2025-05-06] Changed project directory `src/hh` to `src/hh_mcp_comfyui`, added uvx build method
- [2025-04-26] Added image-to-image and background removal sample workflows and support for image-to-image tools
- [2025-04-20] Added text-to-image generation tool

## Effects

- **Usage in Cherry Studio**

- **Usage in Cline**

## Installation Dependencies

**1. Ensure Python 3.12+ is installed**

**2. Use uv to manage the Python environment:**
- Install uv:
  bash
  # On macOS and Linux.
  $ curl -LsSf https://astral.sh/uv/install.sh | sh

  # On Windows.
  $ powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

  # Update uv (not required):
  $ uv self update
  

## Test Running the Service

- **uvx Method**
  bash
  $ uvx hh-mcp-comfyui

  INFO:hh_mcp_comfyui.server:Scanning for workflows in: C:\Users\tianw\AppData\Local\uv\cache\archive-v0\dp4MTo0f1qL0DdYF_BYCL\Lib\site-packages\hh_mcp_comfyui\workflows
  INFO:hh_mcp_comfyui.server:Starting ComfyUI MCP Server...
  
- **pip Method**
  bash
  $ pip install hh_mcp_comfyui
  
  $ python -m hh_mcp_comfyui

  INFO:hh_mcp_comfyui.server:Scanning for workflows in: F:\Python\Python313\Lib\site-packages\hh_mcp_comfyui\workflows
  INFO:hh_mcp_comfyui.server:Starting ComfyUI MCP Server...
  
**The above messages indicate that the service has started successfully.**

## Usage
> **Ensure that the local ComfyUI instance is running (default address: http://127.0.0.1:8188) [ComfyUI installation link](https://github.com/comfyanonymous/ComfyUI.git)**

### Usage with Clients like Cherry Studio, Cline, Cursor, etc.

  uvx MCP Service Configuration

  bash
  {
    "mcpServers": {
      "hh-mcp-comfyui": {
        "command": "uvx",
        "args": [
          "hh-mcp-comfyui@latest"
        ],
        "env": {
          "COMFYUI_API_BASE": "http://127.0.0.1:8188",
          "COMFYUI_WORKFLOWS_DIR": "/path/hh-mcp-comfyui/workflows"
        }
      }
    }
  }
  
  

  pip MCP Service Configuration

  **First, run the following command in the terminal: `pip install hh_mcp_comfyui`**

  bash
  {
    "mcpServers": {
      "hh-mcp-comfyui": {
        "command": "python",
        "args": [
          "-m",
          "hh_mcp_comfyui"
        ],
        "env": {
          "COMFYUI_API_BASE": "http://127.0.0.1:8188",
          "COMFYUI_WORKFLOWS_DIR": "/path/hh-mcp-comfyui/workflows"
        }
      }
    }
  }
  

  Docker MCP Service Configuration

  **Prerequisite: Docker is installed**

  bash
  {
    "mcpServers": {
      "hh-mcp-comfyui": {
        "command": "docker",
        "args": [
            "run",
            "--net=host",
            "-v",
            "/path/hh-mcp-comfyui/workflows:/app/workflows",
            "-i",
            "--rm",
            "zjf2671/hh-mcp-comfyui:latest"
        ],
        "env": {
          "COMFYUI_API_BASE": "http://127.0.0.1:8188"
        }
      }
    }
  }
    

## Sample Workflow Copy to the Specified Workflow Directory:

  (**Note**: Use the following uvx or pip method to find the location of your installed workflow directory, add the sample workflow, and then restart your MCP service)
- **uvx**
  bash
  $ uvx hh-mcp-comfyui
  
  
- **pip**

   bash
  # First, install dependencies
  $ pip install hh_mcp_comfyui
  $ python -m hh_mcp_comfyui
  
  

## Testing

> **Use MCP Inspector to Test the Server Tool**

- **uvx Method**
  bash
  $ npx @modelcontextprotocol/inspector uvx hh-mcp-comfyui
   
- **pip Method**
  bash
  $ pip install hh_mcp_comfyui
  $ npx @modelcontextprotocol/inspector python -m hh_mcp_comfyui
   
- **Docker Method**
    bash
    $ npx @modelcontextprotocol/inspector docker run --net=host -i --rm zjf2671/hh-mcp-comfyui
     
Then click to connect as shown in the image for debugging:

## Usage Notes (Especially for Those Who Have Not Used ComfyUI Before)

- The default workflow is `t2image_bizyair_flux`
- The default image size is 1024x1024
- When the service starts, it will automatically load all JSON workflow files in the workflows directory
- If you are using the **sample workflow** from this project, you need to download a plugin in ComfyUI. For detailed instructions, please refer to: [Sample Workflow Plugin Installation Tutorial](https://ziitefe2yxn.feishu.cn/wiki/PlSmwBbBWiA0iDkc07scb4EEnHc)
- If you are using a local ComfyUI workflow, first ensure that your workflow can run normally in ComfyUI, then export it in JSON format (API) and place it in your local `/path/hh_mcp_comfyui/workflows` directory

## Adding New Workflows

1. Place the workflow JSON file in the `/path/hh_mcp_comfyui/workflows` directory
  
    For uvx and pip startup methods, please refer to the usage instructions above under **"Copy Sample Workflow to the Specified Workflow Directory"**

2. Restart the service to automatically load the new workflow

## Development

### Project Structure

plaintext
.
├── .gitignore
├── .python-version
├── pyproject.toml
├── README.md
├── uv.lock
├── example/              # Example workflow directory
│   └── workflows/
│       ├── i2image_bizyair_sdxl.json
│       ├── t2image_bizyair_flux.json
│       ├── i2image_cogview4.json
│       └── t2image_sd1.5.json
├── src/                  # Source code directory
│   └── hh_mcp_comfyui/
│       ├── comfyui_client.py    # ComfyUI client implementation
│       ├── server.py            # MCP service main file
│       └── workflows/           # Workflow files directory

### Initialize the Project Development Environment:

  bash
  # Clone the repository.
  $ git clone https://github.com/zjf2671/hh-mcp-comfyui.git

  $ cd hh-mcp-comfyui

  # Initialize venv
  $ uv venv

  # Activate the virtual environment.
  $ .venv\Scripts\activate

  # Install dependencies.
  $ uv lock
  Resolved 30 packages in 1ms

  # Sync dependencies.
  $ uv sync
  Resolved 30 packages in 2.54s
  Audited 29 package in 0.02ms
  

### Check if the Service is Running Normally

  bash
  $ uv --directory YOUR_LOCAL_INSTALL_DIR/hh-mcp-comfyui run hh-mcp-comfyui

  INFO:__main__:Scanning for workflows in: D:\cygitproject\hh-mcp-comfyui\src\hh_mcp_comfyui\workflows
  INFO:__main__:Registered resource: workflow://t2image_bizyair_flux -> t2image_bizyair_flux.json
  INFO:__main__:Starting ComfyUI MCP Server...
  

### Use MCP Inspector to Test the Server Tool

  bash
  $ npx @modelcontextprotocol/inspector uv --directory YOUR_LOCAL_INSTALL_DIR/hh-mcp-comfyui run hh-mcp-comfyui
  

### MCP Configuration

  json
  {
    "mcpServers": {
      "hh-mcp-comfyui": {
        "command": "uv",
        "args": [
          "--directory",
          "project absolute path (e.g., D:/hh-mcp-comfyui)",
          "run",
          "hh-mcp-comfyui"
        ],
        "env": {
          "COMFYUI_API_BASE": "http://127.0.0.1:8188",
          "COMFYUI_WORKFLOWS_DIR": "/path/hh-mcp-comfyui/workflows"
        }
      }
    }
  }## Contribution

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---
## If you have any questions, you can contact me through the official account:

*

*

👆 Scan to follow and discover more fun stuff!

---

**Official site: ** [https://github.com/zjf2671/hh-mcp-comfyui.git](https://github.com/zjf2671/hh-mcp-comfyui.git)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `other`, `entertainment and media`, `comfyui`, `图像生成`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `hh-mcp-comfyui@latest`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/jumpskip-hh-comfyui.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
