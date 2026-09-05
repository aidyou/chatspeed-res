---
title: "TuriX-Computer-Use-Agent"
description: "TuriX · Desktop Actions, Driven by AI Talk to your computer, watch it work. Watch our demo and download MCP service, we fully open‑source at GitHub. 📞 Contact & Community Contact us with email: contac…"
---

# TuriX-Computer-Use-Agent

TuriX · Desktop Actions, Driven by AI Talk to your computer, watch it work. Watch our demo and download MCP service, we fully open‑source at GitHub. 📞 Contact & Community Contact us with email: contac…

TuriX · Desktop Actions, Driven by AI

Talk to your computer, watch it work.

Watch our demo and download MCP service, we fully open‑source at [GitHub](https://github.com/TurixAI/TuriX-CUA/tree/mac_mcp).
　
## 📞 Contact & Community

Contact us with email: contact@turix.ai

If you are interested in our service, welcome to join our wechat group.![QRcode](/mcp-assets/36c9a922c3d018dcb69e44be7ccb8e29.jpg)

TuriX lets your powerful AI models take real, hands‑on actions directly on your desktop. 
It ships with a **state‑of‑the‑art computer‑use agent** (passes > 68 % of our internal OSWorld‑style test set) yet stays 100 % open‑source and cost‑free for personal & research use.  

Prefer your own model? **Change in `config.json` and go.**

## Table of Contents
- [📞 Contact & Community](#-contact--community)
- [🚀 Quick‑Start (macOS 15)](#-quickstart-macos-15)
   - [1. Create a Python 3.12 Environment](#2-create-a-python-312-environment)
   - [2. Grant macOS Permissions](#3-grant-macos-permissions)
      - [2.1 Accessibility](#31-accessibility)
      - [2.2 Safari Automation](#32-safari-automation)
   - [3. MCP Support](#5-mcp-support)

## 🚀 Quick‑Start (macOS 15)

### 1. Create a Python 3.12 Environment
Firstly Clone the repository and run:
```bash
conda create -n turix_env python=3.12
conda activate turix_env        # requires conda ≥ 22.9
pip install -r requirements.txt
```

### 2. Grant macOS Permissions

#### 2.1 Accessibility
1. Open **System Settings ▸ Privacy & Security ▸ Accessibility**  
2. Click **＋**, then add **Terminal** and **Visual Studio Code** ANY IDE you use
3. If the agent still fails, also add **/usr/bin/python3**

#### 2.2 Safari Automation
1. **Safari ▸ Settings ▸ Advanced** → enable **Show features for web developers**  
2. In the new **Develop** menu, enable  
    * **Allow Remote Automation**  
    * **Allow JavaScript from Apple Events**  

##### Trigger the Permission Dialogs (run once per shell)
```
# macOS Terminal
osascript -e 'tell application "Safari" \
to do JavaScript "alert(\"Triggering accessibility request\")" in document 1'

# VS Code integrated terminal (repeat to grant VS Code)
osascript -e 'tell application "Safari" \
to do JavaScript "alert(\"Triggering accessibility request\")" in document 1'
```

> **Click "Allow" on every dialog** so the agent can drive Safari.

### 3. MCP Support

TuriX support [Model Context Protocol](https://modelcontextprotocol.io/overview). You can use Claude for Desktop to call TuriX as a MCP Server with the following configuration(assume you have turix_env conda env): 
```json
{
  "mcpServers": {
    "mcp_agent": {
      "command": "/ABSOLUTE/PATH/TO/YOUR/CONDA/ENV/bin/python",
      "args": [
        "/ABSOLUTE/PATH/TO/FOLDER/TuriX-CUA/src/mcp/mcp_server.py"
      ],
      "env": {
        "LLM_PROVIDER": "turix",
        "LLM_MODEL":   "turix-model",
        "LLM_TEMP":    "0",
        "OPENAI_API_KEY":  "YOUR_KEY_HERE",
        "OPENAI_API_BASE": "YOUR_BASE_URL",
        "MCP_TIMEOUT_SEC": "600"
      }
    }
  }
}
```
You can also setup your llm model by change the env in the json file. MCP_TIMEOUT_SEC is the time limit, if the task running time larger than the setting value, the task will be terminated.

If you wanna terminate the agent while running, press cmd+shift+2.

**Official site: ** [https://github.com/TurixAI/TuriX-CUA/tree/mac_mcp](https://github.com/TurixAI/TuriX-CUA/tree/mac_mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `browser`
- Tags: `other`, `browser automation`, `computer-use-agent`, `computer-automation`, `电脑自动化`

## MCP Configuration

- Transport: `stdio`
- Command: `/ABSOLUTE/PATH/TO/YOUR/CONDA/ENV/bin/python`
- Args: `/ABSOLUTE/PATH/TO/FOLDER/TuriX-CUA/src/mcp/mcp_server.py`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/dennisyk348-turix-computer-use-agent.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
