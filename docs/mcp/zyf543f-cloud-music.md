---
title: "Cloud-Music-MCP"
description: "Netease OpenAPI MCP Server Based on the Netease Cloud Music Development Platform standard API implementation 🎵 Give Your AI Agent the Power of Music This is an advanced Model Context Protocol (MCP) se…"
---

# Cloud-Music-MCP

Netease OpenAPI MCP Server Based on the Netease Cloud Music Development Platform standard API implementation 🎵 Give Your AI Agent the Power of Music This is an advanced Model Context Protocol (MCP) se…

# Netease OpenAPI MCP Server

> Based on the [Netease Cloud Music Development Platform](https://developer.music.163.com/st/developer/) standard API implementation

**🎵 Give Your AI Agent the Power of Music**

This is an advanced Model Context Protocol (MCP) server built on the **Netease Cloud Music OpenAPI**. It breaks through the limitations of traditional automation, allowing AI assistants like Claude and Gemini to control your Netease Cloud Music playback experience in a native, elegant, and efficient way via **native APIs**.

No more cumbersome simulated clicks, but true deep integration—from QR code login to favorite playlists, from daily recommendations to precise searches, everything is under the control of the AI.

---

## ✨ Features

- **🤖 Let the AI Agent Play Music for You**: Control music playback through natural language commands. Just say "play a song for me," and the Agent will take care of everything.
- **🔓 QR Code Login**: Supports secure login using the mobile app. The login status (Cookies) is only saved locally, protecting your privacy.
- **🧠 Personalized Recommendations**: Perfectly integrates with your **Daily Recommendations** and **Playlists** (including "My Favorite Music"). The Agent will play music based on your listening preferences.
- **🔍 Song Search**: Supports searching for songs, artists, or albums by keyword and playing them directly.
- **🚀 High Performance**: Built on `pyncm` (Open API) and `fastmcp`, it is faster and more stable than traditional Selenium UI automation scripts.

## 🛠️ Tool List

The following tools are exposed to the AI Agent by this server:

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| `netease_login` | None | Initiates the QR code login process (simulating the official App). |
| `netease_status` | None | Checks the current login status and user information. |
| `netease_get_daily_recommend` | None | Retrieves the list of today's recommended songs. |
| `netease_my_playlists` | None | Retrieves all of the user's playlists (including created and collected ones). |
| `netease_search` | `keyword`: Keyword (song name/artist) | Searches for songs, artists, or albums by keyword. |
| `netease_play` | `id`: Resource ID
`type`: Type ('song'/'playlist') | Plays the specified song or playlist (automatically invokes the desktop application). |

## 🚀 Installation and Usage

### Prerequisites

- macOS or Windows system
- Netease Cloud Music desktop client (recommended)
- `uv` package manager (recommended) or `pip`

### Installation Steps

```bash

# 1. Clone the project

git clone https://github.com/Code-MonkeyZhang/netease-mcp-server.git

cd netease-mcp-server

# 2. Create a virtual environment and install dependencies

uv venv

source .venv/bin/activate  # macOS/Linux

# .venv\Scripts\activate   # Windows

uv pip install -r requirements.txt

```
### Configuration Guide (settings.json)

Ensure that your MCP configuration file points to the correct virtual environment path. You can also enable logging functionality here through environment variables.

```json

"netease-music-pro": {

  "command": "/path/to/project/.venv/bin/python", // points to the python of the virtual environment

  "args": [

    "src/main.py"

  ],

  "cwd": "/path/to/project",

  "env": {

    "PYTHONPATH": "src", // ensures the modules can be found

    "MCP_LOG_ENABLE": "true" // [optional] enable log recording; logs are saved under logs/

  }

}

```
**Logging Notes:**
*   **Default State**: Logging is disabled by default.
*   **After Enabling**: Logs will be saved in the `logs/` folder at the root of the project in the format `session_YYYYMMDD_HHMMSS.log`.
*   **Note**: All logs are written to files only and **will never** be output to the terminal, to avoid interfering with the MCP protocol.

**Official site: ** [https://github.com/Code-MonkeyZhang/netease-mcp-server](https://github.com/Code-MonkeyZhang/netease-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `entertainment and media`, `娱乐`, `音乐`, `网易云`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `/absolute/path/to/YOUR_PROJECT/.venv/bin/python`
- Args: `src/main.py`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/zyf543f-cloud-music.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
