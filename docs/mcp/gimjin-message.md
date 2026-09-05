---
title: "message-mcp"
description: "Desktop notifications, personalized sounds, ntfy mobile app notifications, email notifications, and API push - reducing the anxiety of waiting for AI tasks so you can comfortably enjoy a cup of coffee…"
---

# message-mcp

Desktop notifications, personalized sounds, ntfy mobile app notifications, email notifications, and API push - reducing the anxiety of waiting for AI tasks so you can comfortably enjoy a cup of coffee…

# Message MCP

Desktop notifications, personalized sounds, ntfy mobile app notifications, email notifications, and API push to reduce the anxiety of waiting for AI tasks, so you can comfortably enjoy a cup of coffee.

## Improve AI usage efficiency and free up more time

When waiting for AI to finish a task, do you wish you could work on something else at the same time? Now you can rest easy and handle other tasks while the AI executes long-running tasks.

**Message MCP makes your AI collaboration more efficient!**

```text
: Make a Tetris web game and notify me when done.
: I will start making the Tetris game
   ...
: Message MCP executed, message sent.
```

> TIP
>
> - In the client settings, **allow MCP to run automatically**.
> - Add a "notify me when done" hint in **User Rules** or **Rule Files** to avoid manually repeating the prompt.

### Quick Install

[Install in Cursor](https://cursor.com/install-mcp?name=message-mcp&config=eyJjb21tYW5kIjogIm5weCIsImFyZ3MiOiBbIm1lc3NhZ2UtbWNwQGxhdGVzdCJdfQ==) [Open in VS Code](https://insiders.vscode.dev/redirect?url=vscode:mcp/install?{%22name%22:%22message-mcp%22,%22command%22:%22npx%22,%22args%22:[%22message-mcp@latest%22]}) [Open in VS Code](https://insiders.vscode.dev/redirect?url=vscode-insiders:mcp/install?{%22name%22:%22message-mcp%22,%22command%22:%22npx%22,%22args%22:[%22message-mcp@latest%22]}) [Smithery](https://smithery.ai/server/@gimjin/message-mcp)

> Cloud installation (e.g. Dify and other SaaS services) is supported via smithery.ai, and local one-click deployment is also available. Since Message MCP actually runs in the smithery.ai cloud, desktop notifications are not supported there. End-to-end encryption is used throughout to keep data secure. [Learn more](https://smithery.ai/docs/getting_started/quickstart_connect#one-click-connect-to-smithery-servers)

### Standard Installation

#### MacOS, Linux, WSL2

```json
{
  "mcpServers": {
    "message-mcp": {
      "command": "npx",
      "args": ["-y", "message-mcp@latest"]
    }
  }
}
```

#### Windows

```json
{
  "mcpServers": {
    "message-mcp": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "message-mcp@latest"]
    }
  }
}
```

### Optional Configuration

#### Customize desktop notifications

```json
{
  "mcpServers": {
    "message-mcp": {
      "command": "npx",
      "args": ["-y", "message-mcp@latest"],
      "env": {
        "DISABLE_DESKTOP": "true",
        "SOUND_PATH": "/path/to/your/sound.mp3"
      }
    }
  }
}
```

> - Desktop notifications are enabled by default
> - The default sound is provided by zapsplat. If you don't like it, you can download and configure your own at [zapsplat.com](https://zapsplat.com/).

#### ntfy mobile notifications

Install the app: [App Store](https://apps.apple.com/us/app/ntfy/id1625396347), [Google Play](https://play.google.com/store/apps/details?id=io.heckel.ntfy), [F-Droid](https://f-droid.org/en/packages/io.heckel.ntfy/)

```json
{
  "mcpServers": {
    "message-mcp": {
      "command": "npx",
      "args": ["-y", "message-mcp@latest"],
      "env": {
        "NTFY_TOPIC": "your-unique-topic"
      }
    }
  }
}
```

#### Email notifications

```json
{
  "mcpServers": {
    "message-mcp": {
      "command": "npx",
      "args": ["-y", "message-mcp@latest"],
      "env": {
        "SMTP_HOST": "smtp.gmail.com",
        "SMTP_PORT": "587",
        "SMTP_SECURE": "false",
        "SMTP_USER": "user@gmail.com",
        "SMTP_PASS": "your_password"
      }
    }
  }
}
```

#### API notifications

```json
{
  "mcpServers": {
    "message-mcp": {
      "command": "npx",
      "args": ["-y", "message-mcp@latest"],
      "env": {
        "API_URL": "https://httpbin.org/post",
        "API_METHOD": "POST", // POST, PUT, PATCH
        "API_HEADERS": "{\"Authorization\": \"Bearer token\"}"
      }
    }
  }
}
```

```javascript
fetch(API_URL, {
  method: API_METHOD,
  headers: {
    'Content-Type': 'application/json'
    ...JSON.parse(API_HEADERS)
  },
  body: JSON.stringify({
    title: notifyTitle,
    message: notifyMessage,
  }),
})
```

## System Requirements

- Node.js: 18 or higher
- macOS: native notifications require >= 10.8
- Linux: needs notify-osd or libnotify-bin installed (included by default on Ubuntu)
- Windows: >= 8, or enable Windows Notifications & Actions > Get notifications from apps and other senders

#### WSL2 (Ubuntu) has no notification sound

```bash
sudo apt install -y pulseaudio mpg123
```

#### WSL2 environment lacks OS notifications

```bash
sudo find / -type f -name "snoretoast-*.exe" 2>/dev/null
/path/to/.../node_modules/snoretoast-x64.exe
/path/to/.../node_modules/snoretoast-x86.exe

chmod +x /path/to/.../node_modules/snoretoast-*.exe
```

---

If this project helps you, please give it a Star so more people can see it!

**Official site: ** [https://github.com/gimjin/message-mcp](https://github.com/gimjin/message-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `developer tools`, `browser automation`, `other`, `productivity`, `automation`, `message`, `notification`, `notify`, `cursor`, `copilot`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y message-mcp@latest --shttp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/gimjin-message.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
