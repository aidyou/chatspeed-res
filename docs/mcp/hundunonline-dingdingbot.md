---
title: "mcp-dingdingbot-server"
description: "DingDing webhook MCP server"
---

# mcp-dingdingbot-server

DingDing webhook MCP server

## 🚀 mcp-dingdingbot-server

An MCP server application that sends various types of messages to the DingDing group robot.

[English](#english) | [Chinese](#chinese)

## English

### Overview

This is an MCP (Message Control Protocol) server application that allows you to send various types of messages to DingDing group robots. It supports text, markdown, image, news, and template card messages, as well as file uploads.

### Features

- Text message support
- Markdown message support
- Image message support
- News message support
- Template card message support
- File upload support
- Signature verification for enhanced security

### Installation

#### Manual Installation
```sh
# clone the repo and build
$ git clone https://github.com/HundunOnline/mcp-dingdingbot-server.git
$ cd mcp-dingdingbot-server && make build
$ sudo ln -s $PWD/dist/mcp-dingdingbot-server_xxx_xxxx /usr/local/bin/mcp-dingdingbot-server

# "$PWD/dist/mcp-dingdingbot-server_xxx_xxxx" replace with the actual binary file name

#You can also download and use the pre-compiled release binary package.
```

### Configuration

```json
{
  "mcpServers": {
    "mcp-dingdingbot-server": {
      "command": "mcp-dingdingbot-server",
      "env": {
        "DINGDING_BOT_WEBHOOK_KEY": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
        "DINGDING_BOT_SIGN_KEY": "SECxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
      }
    }
  }
}
```

## Environment Variables

- `DINGDING_BOT_WEBHOOK_KEY`: The webhook key for the DingDing Bot server. This is required.
- `DINGDING_BOT_SIGN_KEY`: The sign key for DingDing Bot signature verification. This is optional but recommended for enhanced security.

### Usage

- **send_text**

Send a text message to DingDing group

- **send_markdown**

Send a markdown message to DingDing group

- **send_image**

Send an image message to DingDing group

- **send_news**

Send a news message to DingDing group, a news includes title, description, url, picurl

- **send_template_card**

Send a template card message to DingDing group

- **upload_file**

Upload a file to DingDing

### Samples

```prompt

> prompt: Send me a text message on DingDing with the content: This is a test message.
> prompt: Send me a Markdown message on DingDing with the content: # This is a test Markdown message
> prompt: Send me a graphic message on DingDing with the title: This is a graphic message, the description: This is a graphic message, the link: https://github.com/HundunOnline, and the image: https://img-blog.csdnimg.cn/fcc22710385e4edabccf2451d5f64a99.jpeg

> Send me a text message on DingDing with the content: This is a test message.
> Send me a Markdown message on DingDing with the content: # This is a test Markdown message
> Send me a graphic message on DingDing with the title: This is a graphic message, the description: This is a graphic message, the link: https://github.com/HundunOnline, and the image: https://img-blog.csdnimg.cn/fcc22710385e4edabccf2451d5f64a99.jpeg

```

### DingDing Robot

DingDing group robot configuration guide can be referred to:
https://open.dingtalk.com/document/robots/custom-robot-access

> DINGDING_BOT_WEBHOOK_KEY is the robot webhook key
For example：
> https://oapi.dingtalk.com/robot/send?access_token=693axxx6-7aoc-4bc4-97a0-0ec2sifa5aaa 

> "693axxx6-7aoc-4bc4-97a0-0ec2sifa5aaa" is your own DINGDING_BOT_WEBHOOK_KEY
>
> DINGDING_BOT_SIGN_KEY is the signature key for enhanced security

> When enabled in the DingDing robot security settings, you need to provide this key to authenticate requests.
> The signature verification uses HMAC-SHA256 algorithm with the timestamp and secret key.

**Official site: ** [https://github.com/HundunOnline/mcp-dingdingbot-server](https://github.com/HundunOnline/mcp-dingdingbot-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `communication`
- Tags: `communication`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `mcp-dingdingbot-server`
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/hundunonline-dingdingbot.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
