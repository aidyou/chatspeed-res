---
title: "meme-mcp"
description: "A simple Model Context Protocol server that allows AI models to generate meme images using the ImgFlip API, enabling users to create memes from text prompts."
---

# meme-mcp

A simple Model Context Protocol server that allows AI models to generate meme images using the ImgFlip API, enabling users to create memes from text prompts.

# Meme MCP Server

A simple Model Context Protocol (MCP) server for generating memes using the ImgFlip API. This server enables AI models and tools to generate meme images from user prompts.

  

## Tools

The server implements the following a single tool called `generateMeme`.

The tool accepts the following parameters:

- `templateNumericId`: The numeric ID of the meme template to use.
- `text0`: The text for the first placeholder.
- `text1`: The text for the second placeholder.

## Usage

You can configure the meme generator server in your client using the [`meme-mcp`](https://www.npmjs.com/package/meme-mcp) NPM package. Here is an example configuration for Claude Desktop (Settings -> Developer -> Edit Config):

```json
{
  "mcpServers": {
    "meme": {
      "command": "npx",
      "args": ["-y", "meme-mcp"],
      "env": {
        "IMGFLIP_USERNAME": "
",
        "IMGFLIP_PASSWORD": "
"
      }
    }
  }
}
```

> Note: you need to create a free account on [ImgFlip](https://imgflip.com/signup) to get your username and password.

### Troubleshooting

Sometimes Claude Desktop fails to find the right version of `npx` (especially if you are using NVM, see this [Issue](https://github.com/modelcontextprotocol/servers/issues/64) for details). In this case, you can manually install `meme-mcp` globally and then use it directly.

```bash
npm install -g meme-mcp
```

You can find the path of your `node` executable by running `which node` in your terminal. After that your configuration should look like this:

```json
{
  "mcpServers": {
    "meme": {
      "command": "/Users//.nvm/versions/node/v20.18.2/bin/node",
      "args": ["/Users//.nvm/versions/node/v20.18.2/lib/node_modules/meme-mcp/dist/index.js"],
      "env": {
        "IMGFLIP_USERNAME": "
",
        "IMGFLIP_PASSWORD": "
"
      }
    }
  }
}
```

## Example

After configuring Claude Desktop, you need to restart it and then you will see the small hammer icon on the bottom right in the chat input. You can then ask Claude to generate a meme for you.

## Author

This project is created for fun by [Vladimir Haltakov](https://haltakov.net). If you find it interesting you can message me on X [@haltakov](https://x.com/haltakov).

**Official site: ** [https://github.com/haltakov/meme-mcp](https://github.com/haltakov/meme-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `image and video processing`, `other`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y meme-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/haltakov-meme.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
