---
title: "mogutongxue-mcp-server"
description: "About what I want to achieve on a Windows computer: 'Xiao Ai, open Kuwo Music' and 'Xiao Ai, cut the song'. - Implement 'Mogutongxue, open Kuwo Music' and 'Mogutongxue, cut the song'. Implementation…"
---

# mogutongxue-mcp-server

About what I want to achieve on a Windows computer: 'Xiao Ai, open Kuwo Music' and 'Xiao Ai, cut the song'. - Implement 'Mogutongxue, open Kuwo Music' and 'Mogutongxue, cut the song'. Implementation…

# mogutongxue-mcp-server

About what I want to achieve on a Windows computer: "Xiao Ai, open Kuwo Music" and "Xiao Ai, cut the song".

## Demo video:
https://www.bilibili.com/video/av114929751298782/

## Purpose:

Implements two things: "Mogutongxue, open Kuwo Music" and "Mogutongxue, cut the song"

```
GET http://localhost:8001/chat/option/call?
    query=Xiao Ai, my commonly used software is all in the rj folder on the C drive, open Kuwo Music

GET http://localhost:8001/chat/option/call?
    query=Xiao Ai, cut the song
```

Implementation: Java runs CMD commands and Java simulates keyboard key presses

```java
// The two lines that actually do the work
// Run cmd
new ProcessBuilder("cmd", "/c", "start", "\"\"", "\"" + filePath + "\"").start();

// Simulate a key press
robot.keyPress(keyCode);
```

## Deployment:

1. Download the source code or git clone

2. Run the code (I ran it with IDEA lol). You probably need Maven and JDK 21 installed locally, then mvn run (roughly, I'm a Java newbie)

3. Add the MCP

##### JSON format:

```json
{
  "mcpServers": {
    "mogutongxue": {
      "url": "http://localhost:8083/sse"
    }
  }
}
```

##### Custom add:

Type: sse

url: http://localhost:8083/sse

4. Modify the code a bit (I thought about developing a visual UI, but it felt like too much trouble, so I didn't)

Modify the following location

...\mogutongxue-mcp\mogutongxue-api\src\main\resources\config.json

Refer to 'cut the song' and write the shortcut key function you want the MCP to implement.

Everything else can stay as is, of course you can also add other things.

5. That's all, best regards

## Afterword:

A Java beginner here, just writing this for fun. I hope it gives the experts a little inspiration, and I hope one day we can really control computers with natural language

**Official site: ** [https://github.com/mogu520999/mogutongxue](https://github.com/mogu520999/mogutongxue)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `files`, `communication`, `media`
- Tags: `communication`, `entertainment and media`, `file systems`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/mogu520999-mogutongxue.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
