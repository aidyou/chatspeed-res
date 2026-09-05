---
title: "dida365-mcp-servers"
description: "Implementing Log CRUD Based on the Official Documentation of TickTick Introduction This guide will walk you through how to implement basic log operations (Create, Read, Update, Delete) using the offic…"
---

# dida365-mcp-servers

Implementing Log CRUD Based on the Official Documentation of TickTick Introduction This guide will walk you through how to implement basic log operations (Create, Read, Update, Delete) using the offic…

# Dida365 MCP Service

This is a Model Context Protocol (MCP) server developed for TickTick/Dida365, written in TypeScript. This service allows AI assistants to interact with the Dida365 API through a standardized interface.

## Features

- Create, read, update, and delete tasks
- Manage projects and project lists
- Support task priority and due dates
- Securely configure API Token via environment variables
- Complete TypeScript type support
- Error handling and API response validation

## Quick Start

### Using MCP (Node version)

#### Get the token from the Dida official docs

[OpenAPI - API Doc](https://developer.dida365.com/docs/index.html#/openapi?id=get-access-token)

#### Download

```
npm i dida365-mcp-servers
```

##### Configure the JSON file

```json
    "dida365": {
      "command": "node",
      "args": [
 			//your download path; example: C:\nvm4w\nodejs\node_modules\dida365-mcp-servers\dist
      ],
      "env": {
        "DIDA365_TOKEN": your TOKEN
      }
    }
```

### Using locally

### 1. Install dependencies

```bash
npm install
```

### 2. Configure environment variables

Copy the example environment file:

```bash
cp .env.example .env
```

Edit the `.env` file and add your Dida365 API Token:

```bash
DIDA365_TOKEN=Bearer your_token_here
```

### 3. Get the API Token

1. Visit the [Dida365 Open Platform](https://developer.dida365.com/)
2. Log in to your Dida365 account
3. Create a new app
4. Get the Access Token
5. Add the token to the `.env` file

### 4. Build and run

Development mode:

```bash
npm run dev
```

Production mode:

```bash
npm run build
npm start
```

## Available Tools

### Task management

#### `create_task` - create a new task

- **Parameters**:
  - `title` (string, required): task title
  - `projectId` (string, required): project ID
  - `content` (string): task content description
  - `dueDate` (string): due date (ISO 8601 format)
  - `priority` (number): priority (0-5)

#### `get_task_by_projectId_and_taskId` - get a task by project ID and task ID

- **Parameters**:
  - `projectId` (string, required): project ID
  - `taskId` (string, required): task ID

#### `get_tasks_by_projectId` - get the task list in a project by project ID

- **Parameters**:
  - `projectId` (string, required): project ID

#### `update_task` - update a task

- **Parameters**:
  - `taskId` (string, required): task ID
  - `title` (string): task title
  - `content` (string): task content
  - `dueDate` (string): due date
  - `priority` (number): priority
  - `status` (number): task status (0: incomplete, 1: completed)

#### `delete_task` - delete a task

- **Parameters**:
  - `taskId` (string, required): task ID
  - `projectId` (string, required): project ID

#### `complete_task` - complete a task

- **Parameters**:
  - `taskId` (string, required): task ID
  - `projectId` (string, required): project ID

### Project management

#### `get_projects` - get the project list

- **Parameters**: none

#### `get_project_by_projectId` - get a project by project ID

- **Parameters**:
  - `projectId` (string, required): project ID

#### `create_project` - create a new project

- **Parameters**:
  - `name` (string, required): project name
  - `color` (string): project color, e.g. "#F18181"
  - `sortOrder` (integer): sort value, default 0
  - `viewMode` (string): view mode ("list", "kanban", "timeline")
  - `kind` (string): project type ("TASK", "NOTE")

#### `update_project_by_projectID` - update a project by project ID

- **Parameters**:
  - `projectId` (string, required): project ID
  - `name` (string): project name
  - `color` (string): project color
  - `sortOrder` (integer): sort value, default 0
  - `viewMode` (string): view mode ("list", "kanban", "timeline")
  - `kind` (string): project type ("TASK", "NOTE")

#### `update_project_by_projectID` - delete a project by project ID

- **Parameters**:
  - `projectId` (string, required): project ID

## Available Resources

### `dida365://tasks`

Get a JSON overview of all tasks

### `dida365://projects`

Get a JSON overview of all projects

## Project Structure

```
├── src/
│   └── index.ts          # Main server file
├── dist/                 # Compiled output directory
├── .env.example          # Example environment variables
├── package.json          # Project config
├── tsconfig.json         # TypeScript config
└── README.md             # Project docs
```

## API Interface

This service uses the official Dida365 API:

- Base URL: `https://api.dida365.com/open/v1`
- Authentication: Bearer Token
- Request format: JSON
- Official docs: https://developer.dida365.com/api#/openap

## Error Handling

The service includes complete error handling:

- Returns detailed error messages when API calls fail
- Network error and timeout handling
- Parameter validation and type checking
- Token validation

## Development Notes

## Contributing

Issues and Pull Requests are welcome!

**Official site: ** [https://github.com/ZH1754629545/dida365-mcp-servers](https://github.com/ZH1754629545/dida365-mcp-servers)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `productivity`
- Tags: `calendar management`, `滴答清单`

## MCP Configuration

- Transport: `stdio`
- Command: `node`
- Args: `yourPath`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/hirito-dida365.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
