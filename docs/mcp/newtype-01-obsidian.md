---
title: "obsidian-mcp"
description: "This project implements a Model Context Protocol (MCP) server for connecting AI models with Obsidian knowledge bases. Through this server, AI models can directly access and manipulate Obsidian notes…"
---

# obsidian-mcp

This project implements a Model Context Protocol (MCP) server for connecting AI models with Obsidian knowledge bases. Through this server, AI models can directly access and manipulate Obsidian notes…

# Obsidian MCP (Model Context Protocol) Server

This project implements a Model Context Protocol (MCP) server that connects AI models with Obsidian knowledge bases. Through this server, AI models can directly access and manipulate Obsidian notes, including reading, creating, updating, and deleting notes, as well as managing folder structures.

## Features

- Seamless integration with Obsidian knowledge bases
- Support for reading, creating, updating, and deleting notes
- Support for creating, renaming, moving, and deleting folders
- Full-text search support
- Compliant with the Model Context Protocol specification

## Prerequisites

- Node.js (v16 or higher)
- Obsidian desktop app
- Obsidian Local REST API plugin (needs to be installed in Obsidian)

## Installation

1. Clone this repository:

```bash
git clone https://github.com/newtype-01/obsidian-mcp.git
cd obsidian-mcp
```

2. Install dependencies:

```bash
npm install
```

3. Build the project:

```bash
npm run build
```

## Configuration

The server is configured through environment variables:

- `OBSIDIAN_VAULT_PATH`: the path to the Obsidian knowledge base
- `OBSIDIAN_API_TOKEN`: the API token of the Obsidian Local REST API plugin
- `OBSIDIAN_API_PORT`: the port of the Obsidian Local REST API plugin (default 27123)

You can set the environment variables as follows:

1. Copy the `.env.example` file to `.env` and edit the values:

```bash
cp .env.example .env
```

2. Edit the `.env` file and fill in your actual configuration:

```
OBSIDIAN_VAULT_PATH=/path/to/your/vault
OBSIDIAN_API_TOKEN=your_api_token_here
OBSIDIAN_API_PORT=27123
```

**Note:** the `.env` file contains sensitive information and has been added to `.gitignore`, so it will not be committed to the version control system.

## Usage

1. Make sure Obsidian is running, and the Local REST API plugin is installed and configured

2. Start the MCP server:

```bash
npm start
```

3. The server communicates with AI models through standard input/output

## Testing

The project includes a test script to verify the server functionality:

```bash
node test-mcp.js
```

## Supported Tools

The MCP server provides the following tools:

- `list_notes`: list all notes in the knowledge base
- `read_note`: read the content of a specified note
- `create_note`: create a new note
- `update_note`: update an existing note
- `search_vault`: search for content in the knowledge base
- `delete_note`: delete a note
- `manage_folder`: manage folders (create, rename, move, delete)

## Development

- Use `npm run dev` to run the server in development mode
- The source code is in the `src` directory

## License

ISC

## Contributing

Pull Requests and Issues are welcome!

## Related Projects

- [Model Context Protocol](https://github.com/anthropics/model-context-protocol)
- [Obsidian Local REST API](https://github.com/coddingtonbear/obsidian-local-rest-api)

**Official site: ** [https://github.com/newtype-01/obsidian-mcp](https://github.com/newtype-01/obsidian-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `memory`, `files`
- Tags: `note taking`, `knowledge and memory`, `file systems`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `@huangyihe/obsidian-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/newtype-01-obsidian.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
