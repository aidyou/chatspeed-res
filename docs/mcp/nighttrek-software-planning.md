---
title: "Software-planning-mcp"
description: "Facilitates interactive software development planning by managing tasks, tracking progress, and creating detailed implementation plans through the Model Context Protocol."
---

# Software-planning-mcp

Facilitates interactive software development planning by managing tasks, tracking progress, and creating detailed implementation plans through the Model Context Protocol.

# Software Planning Tool 🚀
[Smithery](https://smithery.ai/server/@NightTrek/Software-planning-mcp)

A Model Context Protocol (MCP) server designed to facilitate software development planning through an interactive, structured approach. This tool helps break down complex software projects into manageable tasks, track implementation progress, and maintain detailed development plans.

  

## Features ✨

- **Interactive Planning Sessions**: Start and manage development planning sessions
- **Todo Management**: Create, update, and track development tasks
- **Complexity Scoring**: Assign complexity scores to tasks for better estimation
- **Code Examples**: Include relevant code snippets in task descriptions
- **Implementation Plans**: Save and manage detailed implementation plans

## Installation 🛠️

### Installing via Smithery

To install Software Planning Tool for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@NightTrek/Software-planning-mcp):

```bash
npx -y @smithery/cli install @NightTrek/Software-planning-mcp --client claude
```

### Manual Installation
1. Clone the repository
2. Install dependencies:
```bash
pnpm install
```
3. Build the project:
```bash
pnpm run build
```
4. Add to your MCP settings configuration (typically located at `~/Library/Application Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`):
```json
{
  "mcpServers": {
    "software-planning-tool": {
      "command": "node",
      "args": [
        "/path/to/software-planning-tool/build/index.js"
      ],
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

## Available Tools 🔧

### start_planning
Start a new planning session with a specific goal.
```typescript
{
  goal: string  // The software development goal to plan
}
```

### add_todo
Add a new todo item to the current plan.
```typescript
{
  title: string,         // Title of the todo item
  description: string,   // Detailed description
  complexity: number,    // Complexity score (0-10)
  codeExample?: string  // Optional code example
}
```

### get_todos
Retrieve all todos in the current plan.
```typescript
// No parameters required
```

### update_todo_status
Update the completion status of a todo item.
```typescript
{
  todoId: string,     // ID of the todo item
  isComplete: boolean // New completion status
}
```

### save_plan
Save the current implementation plan.
```typescript
{
  plan: string  // The implementation plan text
}
```

### remove_todo
Remove a todo item from the current plan.
```typescript
{
  todoId: string  // ID of the todo item to remove
}
```

## Example Usage 📝

Here's a complete example of using the software planning tool:

1. Start a planning session:
```typescript
await client.callTool("software-planning-tool", "start_planning", {
  goal: "Create a React-based dashboard application"
});
```

2. Add a todo item:
```typescript
const todo = await client.callTool("software-planning-tool", "add_todo", {
  title: "Set up project structure",
  description: "Initialize React project with necessary dependencies",
  complexity: 3,
  codeExample: `
npx create-react-app dashboard
cd dashboard
npm install @material-ui/core @material-ui/icons
  `
});
```

3. Update todo status:
```typescript
await client.callTool("software-planning-tool", "update_todo_status", {
  todoId: todo.id,
  isComplete: true
});
```

4. Save the implementation plan:
```typescript
await client.callTool("software-planning-tool", "save_plan", {
  plan: `
# Dashboard Implementation Plan

## Phase 1: Setup (Complexity: 3)
- Initialize React project
- Install dependencies
- Set up routing

## Phase 2: Core Features (Complexity: 5)
- Implement authentication
- Create dashboard layout
- Add data visualization components
  `
});
```

## Development 🔨

### Project Structure
```
software-planning-tool/
  ├── src/
  │   ├── index.ts        # Main server implementation
  │   ├── prompts.ts      # Planning prompts and templates
  │   ├── storage.ts      # Data persistence
  │   └── types.ts        # TypeScript type definitions
  ├── build/              # Compiled JavaScript
  ├── package.json
  └── tsconfig.json
```

### Building
```bash
pnpm run build
```

### Testing
Test all features using the MCP inspector:
```bash
pnpm run inspector
```

## License 📄

MIT

---

Made with ❤️ using the Model Context Protocol

**Official site: ** [https://github.com/NightTrek/Software-planning-mcp](https://github.com/NightTrek/Software-planning-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `developer tools`, `other`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `node`
- Args: `/path/to/software-planning-tool/build/index.js`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/nighttrek-software-planning.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
