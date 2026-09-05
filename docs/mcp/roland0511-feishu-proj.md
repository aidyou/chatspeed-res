---
title: "mcp-feishu-proj"
description: "A Model Context Protocol server that enables AI assistants to interact with the Feishu project management system, allowing retrieval of project views and work items."
---

# mcp-feishu-proj

A Model Context Protocol server that enables AI assistants to interact with the Feishu project management system, allowing retrieval of project views and work items.

# MCP-Feishu Project Management Tool

A Feishu project management tool based on the MCP (Model Context Protocol), allowing AI assistants to interact with the Feishu project management system via the MCP protocol.

## Project Introduction

This project is an MCP server implementation that wraps the Feishu project management Open API, enabling AI assistants to fetch Feishu project view lists, view details, and more. With this tool, AI assistants can help users manage and query work items in Feishu projects.

## Usage

Add this server to the config file of an MCP-capable client (such as the [Claude Desktop client](https://claude.ai/download), [Cursor](https://www.cursor.com/), [Cline](https://github.com/cline/cline), etc.).

> For more MCP clients, see: https://modelcontextprotocol.io/clients

Taking the Claude Desktop client as an example, edit the `claude_desktop_config.json` file:
- macOS: ~/Library/Application Support/Claude/claude_desktop_config.json
- Windows: %APPDATA%\Claude\claude_desktop_config.json

Add the following configuration to the `mcpServers` field:

```json
{
  "mcpServers": {
    "feishuproj": {
      "command": "uvx",
      "args": ["mcp-feishu-proj@latest","--transport", "stdio"],
      "env": {
        "FS_PROJ_PROJECT_KEY": "your_project_key",
        "FS_PROJ_USER_KEY": "your_user_key",
        "FS_PROJ_PLUGIN_ID": "your_plugin_id",
        "FS_PROJ_PLUGIN_SECRET": "your_plugin_secret"
      }
    }
  }
}
```

## Supported Features ([Contributions Welcome](#contribution-guide))

### Authentication
- [x] Login and authentication flow

### Views
- [x] Get the Feishu project view list
- [x] Get the work item list of a view
- [ ] Create a fixed view
- [ ] Update a fixed view
- [ ] Create a condition view
- [ ] Update a condition view
- [ ] Delete a view

### Work Item Management
- [x] Get work item details
- [x] Get metadata for creating a work item
- [ ] Create a work item
- [ ] Update a work item
- [ ] Batch update work item field values
- [ ] Delete a work item
- [ ] Terminate/restore a work item
- [ ] Get work item operation history

### Work Item Search
- [ ] Get a specified work item list (single space)
- [ ] Get a specified work item list (cross-space)
- [ ] Get a specified work item list (single space, complex parameters)
- [ ] Get a specified work item list (global search)
- [ ] Get a specified list of linked work items

### Attachment Management
- [ ] Add attachments
- [ ] File upload
- [ ] Download attachments
- [ ] Delete attachments

### Space Management
- [ ] Get the space list
- [ ] Get space details
- [ ] Get business line details in a space
- [ ] Get work item types in a space
- [ ] Get team members in a space

### User Management
- [ ] Get user details
- [ ] Search the user list within a tenant
- [ ] Create a custom user group
- [ ] Update user group members
- [ ] Query user group members

### Space Linkages
- [ ] Get the space linkage rule list
- [ ] Get the linked work item instance list under a space linkage
- [ ] Bind linked work item instances of a space linkage
- [ ] Unbind linked work item instances of a space linkage

### Workflows and Nodes
- [ ] Get workflow details
- [ ] Get workflow details (WBS)
- [ ] Update nodes/scheduling
- [ ] Node completion/rollback
- [ ] Status transitions

### Flow Configuration
- [ ] Get the flow template list under a work item
- [ ] Get flow template configuration details
- [ ] Add a flow template
- [ ] Update a flow template
- [ ] Delete a flow template

### Subtasks
- [ ] Get a specified subtask list
- [ ] Get subtask details
- [ ] Create a subtask
- [ ] Update a subtask
- [ ] Subtask completion/rollback
- [ ] Delete a subtask

### Comments
- [ ] Add comments
- [ ] Query comments
- [ ] Update comments
- [ ] Delete comments

### Work Item Timesheets
- [ ] Get the timesheet record list of a work item
- [ ] Create actual hours
- [ ] Update actual hours
- [ ] Delete actual hours

### Review Management
- [ ] Batch query review opinions and conclusions
- [ ] Modify review conclusions and opinions
- [ ] Query review conclusion label values

### Other Features
- [ ] Add bots to a group
- [ ] Get metric chart detail data
- [ ] Get flow role configuration details

## Development Guide

## Development Environment Setup

1. Clone this repository:

```bash
git clone https://github.com/yourusername/mcp-feishu-proj.git
cd mcp-feishu-proj
```

2. Install dependencies (using uv):

```bash
# Install uv (if not already installed)
pip install uv
# Create a virtual environment and install dependencies
uv venv
uv pip install -e .
```

## Configuration

1. Copy the environment variable example file and configure it:

```bash
cp .env.example .env
```

2. Edit the `.env` file and fill in the following required configuration:

```
FS_PROJ_BASE_URL=https://project.feishu.cn/
FS_PROJ_PROJECT_KEY=your_project_key
FS_PROJ_USER_KEY=your_user_key
FS_PROJ_PLUGIN_ID=your_plugin_id
FS_PROJ_PLUGIN_SECRET=your_plugin_secret
```

Where:
- `FS_PROJ_BASE_URL`: base URL of the Feishu project API, default https://project.feishu.cn/
- `FS_PROJ_PROJECT_KEY`: identifier of the Feishu project
- `FS_PROJ_USER_KEY`: user identifier
- `FS_PROJ_PLUGIN_ID`: plugin ID for the Feishu project Open API
- `FS_PROJ_PLUGIN_SECRET`: plugin secret for the Feishu project Open API

### Adding New Features

To add a new Feishu project API feature, follow these steps:

1. Add a new API method in `fsprojclient.py`
2. Register the new MCP tool in `server.py` with the `@mcp.tool` decorator

### Feishu Project Open API Reference

This project includes a Postman collection of the Feishu project Open API in the `docs/open-api-postman` directory. Import the files in that directory into Postman for quick debugging of Feishu project endpoints:

- `postman_environment.json`: Postman environment variables
- `postman_collection.json`: Postman API collection

## Containerized Deployment Guide

### Docker Deployment

This project supports Docker deployment; you can run the MCP Feishu project service in a Docker container.

#### Prerequisites

- Install [Docker](https://docs.docker.com/get-docker/)
- Install [Docker Compose](https://docs.docker.com/compose/install/)

#### Run with Docker Compose

1. Create a `.env` file and set the required environment variables

```bash
cp .env.example .env
```

Then edit the `.env` file and fill in your Feishu project info:

```
FS_PROJ_BASE_URL=https://project.feishu.cn/
FS_PROJ_PROJECT_KEY=your_project_key
FS_PROJ_USER_KEY=your_user_key
FS_PROJ_PLUGIN_ID=your_plugin_id
FS_PROJ_PLUGIN_SECRET=your_plugin_secret
```

2. Start the service with Docker Compose

```bash
docker-compose -f docker/docker-compose.yml up -d
```

This uses the `ghcr.io/astral-sh/uv` image and mounts the project root into the container, running the local code directly for easy development and debugging. Docker Compose automatically loads the `.env` file in the project root as environment variables.

3. View logs

```bash
docker-compose -f docker/docker-compose.yml logs -f
```

4. Stop the service

```bash
docker-compose -f docker/docker-compose.yml down
```

For more details, see the [Docker deployment docs](https://github.com/Roland0511/mcp-feishu-proj/blob/HEAD/docker/docker-README.md).

### Kubernetes Deployment

#### Prerequisites

- A working Kubernetes cluster
- The kubectl CLI installed
- Permission to create Deployments, ConfigMaps, and Secrets

#### Deployment Steps

1. Prepare the Secret

First, create a Secret containing the sensitive information. Since Kubernetes Secrets require base64-encoded values, encode the sensitive info:

```bash
# base64-encode the sensitive information
echo -n "your_project_key" | base64
echo -n "your_user_key" | base64
echo -n "your_plugin_id" | base64
echo -n "your_plugin_secret" | base64
```

Then update the corresponding fields in the `k8s-secret.yaml` file with the generated base64 values.

2. Apply the configurations

Apply the following config files in order:

```bash
# Create the ConfigMap
kubectl apply -f k8s-configmap.yaml

# Create the Secret
kubectl apply -f k8s-secret.yaml

# Create the Deployment
kubectl apply -f k8s-deployment.yaml
```

3. Verify the deployment

Check the deployment status:

```bash
# View Deployment status
kubectl get deployments

# View Pod status
kubectl get pods

# View Pod logs
kubectl logs -f
```

For more details, see the [Kubernetes deployment docs](https://github.com/Roland0511/mcp-feishu-proj/blob/HEAD/k8s/k8s-README.md).

## Contribution Guide

Contributions, bug reports, and improvement suggestions are welcome. Follow these steps:

1. Fork this repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Create a Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Roland0511/mcp-feishu-proj/blob/HEAD/LICENSE) file for details.

**Official site: ** [https://github.com/Roland0511/mcp-feishu-proj](https://github.com/Roland0511/mcp-feishu-proj)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `communication`
- Tags: `communication`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `mcp-feishu-proj@latest --transport stdio`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/roland0511-feishu-proj.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
