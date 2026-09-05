---
title: "CloudMusic_Auto_Player"
description: "NetEase Cloud Music Auto Player, supporting all shortcut key operations, song search and playback, custom playlist playback, daily recommendations, and roaming features."
---

# CloudMusic_Auto_Player

NetEase Cloud Music Auto Player, supporting all shortcut key operations, song search and playback, custom playlist playback, daily recommendations, and roaming features.

# NetEase Cloud Music MCP Controller

An intelligent NetEase Cloud Music MCP controller providing global hotkey support, single-song search & play, playlist search & play, custom playlist management, daily recommendations, and private roaming.

## Key Features

### Basic Controls
- **Launch NetEase Cloud Music**: Quick launch via URL scheme, with optional auto-minimize
- **Playback control**: Play/pause, previous/next track, volume adjustment
- **UI control**: Toggle mini mode, show/hide lyrics
- **Interactions**: Like the current song with one click

### Music Search & Playback
- **Song search & play**: Search by song name or "song name + artist" and play
- **Playlist search & play**: Search and play a specified playlist
- **Built-in playlists**: Quick access to official charts like the Rising Chart, New Song Chart, and Hot Song Chart
- **Private radar**: Play personalized recommendation playlists

### Playlist Management
- **Custom playlist management**: Add, remove, and list user-defined playlists
- **Playlist config files**: Manage playlists in bulk via JSON files
- **Built-in playlist integration**: Quick access to official hot charts

### Advanced Features
- **Daily recommendations**: Auto-play NetEase Cloud Music's daily recommended playlist
- **Private roaming**: Start NetEase Cloud Music private roaming
- **Global hotkeys**: Global hotkey control without switching to the music app; keys are customizable

### Global Hotkey Support

#### Windows default hotkeys
- `Ctrl+Alt+P`: play/pause
- `Ctrl+Alt+Left`: previous track
- `Ctrl+Alt+Right`: next track
- `Ctrl+Alt+Up/Down`: volume up/down
- `Ctrl+Alt+M`: toggle mini mode
- `Ctrl+Alt+L`: like current song
- `Ctrl+Alt+D`: show/hide lyrics

#### macOS default hotkeys
- `command+option+P`: play/pause
- `command+option+Left`: previous track
- `command+option+Right`: next track
- `command+option+Up/Down`: volume up/down
- `command+option+M`: toggle mini mode
- `command+option+L`: like current song
- `command+option+D`: show/hide lyrics

> Hotkeys can be customized in the `custom_hotkeys` section of `src/config/hotkeys.json`

## Environment Requirements

### General requirements
- **Python**: 3.10+
- **NetEase Cloud Music client**: installed and working
- **uv**: modern Python package manager ([installation guide](https://docs.astral.sh/uv/getting-started/installation/))

### Platform requirements
- **Windows 10/11**: full feature support
  - Global hotkey control
  - Music search & play
  - Daily recommendations
  - Private roaming
  - Bundled ChromeDriver (Windows x64)
- **macOS 10.15+**: basic feature support
  - Global hotkey control
  - Music search & play
  - Daily recommendations (not supported)
  - Private roaming (not supported)

## Installation Guide

### 1. Install uv (if not already installed)
```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Clone the project and install dependencies
```bash
git clone https://github.com/xiduan/CloudMusic_Auto_Player.git
cd CloudMusic_Auto_Player
uv sync
```

### 3. macOS notes
The macOS version only supports basic features (global hotkeys, music search & play); daily recommendations and private roaming are not supported.

### Main dependencies
- `fastmcp>=2.0.0`: MCP server framework
- `pyautogui>=0.9.54`: cross-platform global hotkey support
- `pywin32>=306`: Windows system integration (Windows only)
- `psutil>=5.9.0`: process management
- `selenium>=4.0.0`: web automation (daily recommendations/roaming)
- `requests>=2.28.0`: HTTP request library

## Configuration Guide

### 1. MCP client config

Add the following to your MCP client config file:

#### Option 1: Use uvx (recommended)

Use the published PyPI package directly - no need to download the source:

```json
{
  "mcpServers": {
    "cloudmusic-auto-player": {
      "command": "uvx",
      "args": ["cloudmusic-auto-player==1.0.2"],
      "env": {
        "NETEASE_MUSIC_PATH": "C:\\Program Files (x86)\\Netease\\CloudMusic\\cloudmusic.exe",
        "CHROMEDRIVER_PATH": "C:\\path\\to\\chromedriver.exe"
      }
    }
  }
}
```

**Platform-specific configuration examples:**

**Windows config:**
```json
{
  "mcpServers": {
    "cloudmusic-auto-player": {
      "command": "uvx",
      "args": ["cloudmusic-auto-player==1.0.2"],
      "env": {
        "NETEASE_MUSIC_PATH": "C:\\Program Files (x86)\\Netease\\CloudMusic\\cloudmusic.exe",
        "CHROMEDRIVER_PATH": "C:\\path\\to\\chromedriver.exe"
      }
    }
  }
}
```

**macOS config:**
```json
{
  "mcpServers": {
    "cloudmusic-auto-player": {
      "command": "uvx",
      "args": ["cloudmusic-auto-player==1.0.2"],
      "env": {
        "NETEASE_MUSIC_PATH": "/Applications/NeteaseMusic.app/Contents/MacOS/NeteaseMusic"
      }
    }
  }
}
```

> **Note**: macOS does not support daily recommendations or private roaming, so `CHROMEDRIVER_PATH` is not needed.

#### Option 2: Run from a local project

If you need to modify the source or develop locally, download the project and use:

```json
{
  "mcpServers": {
    "auto-music-player": {
      "command": "uv",
      "args": [
        "run",
        "--project",
        "/path/to/CloudMusic_Auto_Player",
        "src/server.py"
      ],
      "cwd": "/path/to/CloudMusic_Auto_Player",
      "env": {
        "NETEASE_MUSIC_PATH": "/path/to/netease/music/executable",
        "CHROMEDRIVER_PATH": "/path/to/chromedriver"
      }
    }
  }
}
```

**Windows local project example:**
```json
{
  "mcpServers": {
    "auto-music-player": {
      "command": "uv",
      "args": [
        "run",
        "--project", 
        "C:\\Users\\YourName\\CloudMusic_Auto_Player",
        "src/server.py"
      ],
      "cwd": "C:\\Users\\YourName\\CloudMusic_Auto_Player",
      "env": {
        "NETEASE_MUSIC_PATH": "C:\\Program Files (x86)\\Netease\\CloudMusic\\cloudmusic.exe",
        "CHROMEDRIVER_PATH": "C:\\Users\\YourName\\CloudMusic_Auto_Player\\src\\chromedriver\\win64\\chromedriver.exe"
      }
    }
  }
}
```

**macOS local project example:**
```json
{
  "mcpServers": {
    "auto-music-player": {
      "command": "uv",
      "args": [
        "run",
        "python",
        "/Users/YourName/CloudMusic_Auto_Player/src/server.py"
      ],
      "cwd": "/Users/YourName/CloudMusic_Auto_Player",
      "env": {
        "NETEASE_MUSIC_PATH": "/Applications/NeteaseMusic.app/Contents/MacOS/NeteaseMusic"
      }
    }
  }
}
```

> **Important**:
> - Replace the paths with your actual paths
> - Backslashes in Windows paths must be escaped as `\\`
> - macOS does not support daily recommendations or private roaming
> - After configuration, call `get_netease_config()` to verify the environment variables are set correctly

### 2. Custom playlists

#### Upload a custom playlist
You can upload a custom playlist via MCP by providing the playlist name and ID (a description is optional) (recommended)
Or edit the `playlists.json` file in the project root:

```json
{
  "systemPlaylists": {
    "Rising Chart": {"id": "19723756", "name": "Rising Chart", "description": "Official NetEase rising chart"},
    "New Song Chart": {"id": "3779629", "name": "New Song Chart", "description": "Official NetEase new song chart"},
    "Hot Song Chart": {"id": "3778678", "name": "Hot Song Chart", "description": "Official NetEase hot song chart"}
  },
  "userPlaylists": {
    "My Favorites": {"id": "123456789", "name": "My Favorite Playlist", "description": "Personal favorites"},
    "Work Music": {"id": "987654321", "name": "Work Playlist", "description": "Music for working"}
  }
}
```

**How to get a playlist ID:**
1. Open the playlist in the NetEase Cloud Music web or desktop client
2. Get the playlist ID from the URL (e.g. `https://music.163.com/#/playlist?id=123456789` -> `123456789`)
3. Add the playlist info to the `userPlaylists` section

## Usage

> All the methods below are recommended to be called via the MCP tools from an agent using natural language.

### Basic playback controls

```python
# Launch NetEase Cloud Music
launch_netease_music(minimize_window=True)

# Playback control
control_playback(action="play_pause")  # play/pause
control_playback(action="next")        # next track
control_playback(action="previous")    # previous track

# Volume control
control_volume(action="volume_up")     # volume up
control_volume(action="volume_down")   # volume down

# UI control
toggle_mini_mode()  # toggle mini mode
toggle_lyrics()     # toggle lyrics display
like_current_song() # like the current song
```

### Music search & play

```python
# Search and play a song
search_and_play(query="Daoxiang Jay Chou", minimize_window=True)

# Play a built-in playlist
search_and_play_playlist(playlist_name="Rising Chart", minimize_window=True)

# Play a custom playlist
search_and_play_playlist(playlist_name="My Favorites", minimize_window=True)
```

### Advanced features

```python
# Play daily recommendations (requires the NetEase Cloud Music path to be configured)
play_daily_recommend()

# Start private roaming (requires the NetEase Cloud Music path to be configured)
play_roaming()

# Get controller info and feature list
get_controller_info()

# Get current config (verify environment variables)
get_netease_config()
```

### Verifying the configuration

After configuration, we strongly recommend verifying it with:

```python
# Verify environment variables and paths
get_netease_config()
```

This tool returns:
- Whether the NetEase Cloud Music path is configured
- Whether the ChromeDriver path is configured
- Whether each filesystem path exists
- Whether the conditions for daily recommendations are met

**Example output:**
```json
{
  "success": true,
  "config": {
    "netease_music_path": "your-configured-netease-music-path",
    "path_status": "valid",
    "chromedriver_path": "your-configured-chromedriver-path",
    "chromedriver_status": "exists",
    "platform": "windows"
  },
  "ready_for_daily_recommend": true
}
```

### Playlist management

```python
# List all playlists
manage_custom_playlists(action="list")

# Add a playlist
manage_custom_playlists(
    action="add", 
    playlist_name="New Playlist", 
    playlist_id="123456789", 
    description="Playlist description"
)

# Remove a playlist
manage_custom_playlists(action="remove", playlist_name="Old Playlist")
```

## Notes

### Important reminders
1. **Platform differences**: macOS only supports basic features; daily recommendations and private roaming are not supported
2. **NetEase Cloud Music path**: Windows users must configure the client path (via the `NETEASE_MUSIC_PATH` environment variable) before using daily recommendations and private roaming
3. **ChromeDriver requirement**: Windows daily recommendations and roaming require ChromeDriver; the project bundles the Windows version
4. **VIP limits**: Private roaming may require a NetEase Cloud Music VIP membership
5. **Network**: Search and playback need a stable network connection
6. **Config verification**: After configuring, call `get_netease_config()` to verify the environment variables

### Troubleshooting
- **Hotkeys don't respond**: make sure `pyautogui` is installed and no other program is using the hotkeys
- **NetEase Cloud Music fails to launch**: check that the URL scheme is registered correctly; try reinstalling NetEase Cloud Music
- **Daily recommendations won't play**: confirm the NetEase Cloud Music path is correct and you are logged in
- **Search issues**: check the network connection and confirm the NetEase Cloud Music API is accessible

### Compatibility

#### Supported operating systems
- **Windows 10/11**: full feature support
  - Global hotkeys
  - Music search & play
  - Daily recommendations
  - Private roaming
  - Bundled ChromeDriver

- **macOS 10.15+**: basic feature support
  - Global hotkeys
  - Music search & play
  - Daily recommendations (not supported)
  - Private roaming (not supported)

#### Client requirements
- Requires the NetEase Cloud Music desktop client (the UWP version is not supported)
- We recommend the latest NetEase Cloud Music client for best compatibility
- macOS users are recommended to download the desktop version from the official website

## Project Structure

```
auto_music/
├── src/
│   ├── server.py              # MCP server main program
│   └── chromedriver/          # ChromeDriver binaries
│       └── win64/
├── config.json                # MCP client config example
├── netease_config.json        # NetEase Cloud Music config
├── playlists.json             # Playlist config
└── README.md                  # Project docs
```

## Support

- **Repository**: https://github.com/SpongeBaby-124/CloudMusic_Auto_Player
- **Issues**: file them on GitHub Issues
- **Email**: lxd4094@foxmail.com

## License

This project is open source under the MIT License.

## Changelog

### v1.0.2
- Added uvvx configuration option

---

**Enjoy the music, control made simple!**

**Official site: ** [https://github.com/SpongeBaby-124/CloudMusic_Auto_Player](https://github.com/SpongeBaby-124/CloudMusic_Auto_Player)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `entertainment and media`, `音乐自动播放`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `cloudmusic-auto-player==1.0.2`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/lixiande-cloudmusic-auto-player.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
