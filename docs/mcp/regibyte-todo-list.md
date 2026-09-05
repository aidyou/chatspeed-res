---
title: "todo-list-mcp"
description: "A Model Context Protocol (MCP) server that provides tools for managing todo items, including creation, updating, completion, deletion, searching, and summarizing tasks."
---

# todo-list-mcp

A Model Context Protocol (MCP) server that provides tools for managing todo items, including creation, updating, completion, deletion, searching, and summarizing tasks.

# Todo List MCP Server

A Model Context Protocol (MCP) server that provides a comprehensive API for managing todo items.

  

> **📚 Learning Resource**: This project is designed as an educational example of MCP implementation. See [GUIDE.md](https://github.com/RegiByte/todo-list-mcp/blob/HEAD/GUIDE.md) for a comprehensive explanation of how the project works and why things are implemented the way they are.

## Features

- **Create todos**: Add new tasks with title and markdown description
- **Update todos**: Modify existing tasks
- **Complete todos**: Mark tasks as done
- **Delete todos**: Remove tasks from the list
- **Search todos**: Find tasks by title or creation date
- **Summarize todos**: Get a quick overview of active tasks

## Tools

This MCP server exposes the following tools:

1. `create-todo`: Create a new todo item
2. `list-todos`: List all todos
3. `get-todo`: Get a specific todo by ID
4. `update-todo`: Update a todo's title or description
5. `complete-todo`: Mark a todo as completed
6. `delete-todo`: Delete a todo
7. `search-todos-by-title`: Search todos by title (case-insensitive partial match)
8. `search-todos-by-date`: Search todos by creation date (format: YYYY-MM-DD)
9. `list-active-todos`: List all non-completed todos
10. `summarize-active-todos`: Generate a summary of all active (non-completed) todos

## Installation

```bash
# Clone the repository
git clone https://github.com/RegiByte/todo-list-mcp.git
cd todo-list-mcp

# Install dependencies
npm install

# Build the project
npm run build
```

## Usage

### Starting the Server

```bash
npm start
```

### Configuring with Claude for Desktop

#### Claude Desktop

Add this to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "todo": {
      "command": "node",
      "args": ["/absolute/path/to/todo-list-mcp/dist/index.js"]
    }
  }
}
```

#### Cursor

- Go to "Cursor Settings" -> MCP
- Add a new MCP server with a "command" type
- Add the absolute path of the server and run it with node
- Example: node /absolute/path/to/todo-list-mcp/dist/index.js

### Example Commands

When using with Claude for Desktop or Cursor, you can try:

- "Create a todo to learn MCP with a description explaining why MCP is useful"
- "List all my active todos"
- "Create a todo for tomorrow's meeting with details about the agenda in markdown"
- "Mark my learning MCP todo as completed"
- "Summarize all my active todos"

## Project Structure

This project follows a clear separation of concerns to make the code easy to understand:

```
src/
├── models/       # Data structures and validation schemas
├── services/     # Business logic and database operations
├── utils/        # Helper functions and formatters
├── config.ts     # Configuration settings
├── client.ts     # Test client for local testing
└── index.ts      # Main entry point with MCP tool definitions
```

## Learning from This Project

This project is designed as an educational resource. To get the most out of it:

1. Read the [GUIDE.md](https://github.com/RegiByte/todo-list-mcp/blob/HEAD/GUIDE.md) for a comprehensive explanation of the design
2. Study the heavily commented source code to understand implementation details
3. Use the test client to see how the server works in practice
4. Experiment with adding your own tools or extending the existing ones

## Development

### Building

```bash
npm run build
```

### Running in Development Mode

```bash
npm run dev
```

## License

MIT

**Official site: ** [https://github.com/RegiByte/todo-list-mcp](https://github.com/RegiByte/todo-list-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `memory`
- Tags: `note taking`, `knowledge and memory`, `other`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `node`
- Args: `/absolute/path/to/todo-list-mcp/dist/index.js`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/regibyte-todo-list.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
