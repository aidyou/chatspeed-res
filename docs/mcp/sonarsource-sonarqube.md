---
title: "SonarQube MCP 服务器"
description: "SonarQube MCP Server The SonarQube MCP Server is a Model Context Protocol (MCP) server that enables seamless integration with SonarQube Server or Cloud for code quality and security. It also supports the analysis of code"
---

# SonarQube MCP 服务器

SonarQube MCP Server The SonarQube MCP Server is a Model Context Protocol (MCP) server that enables seamless integration with SonarQube Server or Cloud for code quality and security. It also supports the analysis of code

# SonarQube MCP Server

[![Build](https://github.com/SonarSource/sonarqube-mcp-server/actions/workflows/build.yml/badge.svg?branch=master)](https://github.com/SonarSource/sonarqube-mcp-server/actions/workflows/build.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=SonarSource_sonarqube-mcp-server&metric=alert_status&token=364a508a1e77096460f8571d8e66b41c99c95bea)](https://sonarcloud.io/summary/new_code?id=SonarSource_sonarqube-mcp-server)

The SonarQube MCP Server is a Model Context Protocol (MCP) server that enables seamless integration with SonarQube Server or Cloud for code quality and security.
It also supports the analysis of code snippet directly within the agent context.

## Quick setup

Security best practices

> 🔒 **Important**: Your SonarQube token is a sensitive credential. Follow these security practices:

**When using CLI commands:**
- **Avoid hardcoding tokens** in command-line arguments – they get saved in shell history
- **Use environment variables** – set tokens in environment variables before running commands

**When using configuration files:**
- **Never commit tokens** to version control
- **Use environment variable substitution** in config files when possible

### 🚀 Generate your configuration

The fastest way to get started is the **[SonarQube MCP Server Configuration Generator](https://mcp.sonarqube.com/config-generator.html)** – an interactive tool that produces a ready-to-use configuration for your preferred AI agent client.

### Manual setup

If you prefer to configure things yourself, the simplest method is to use our container image at [sonarsource/sonarqube-mcp](https://hub.docker.com/r/sonarsource/sonarqube-mcp/tags). Use `sonarsource/sonarqube-mcp` for automatic updates (with `--pull=always`), or pin to a version tag (e.g., `sonarsource/sonarqube-mcp:1.19.0.2785`) for reproducible deployments. Read below if you want to build it locally.

> **Note:** While the examples below use `docker`, any OCI-compatible container runtime works (e.g., Podman, nerdctl). Simply replace `docker` with your preferred tool.

Antigravity

SonarQube MCP Server is available in the Antigravity MCP Store. Follow these instructions:

1. Open the **Agent Side Panel**
2. Click the three dots (**...**) at the top right and select **MCP Servers**
3. Search for `SonarQube` and select **Install**
4. Provide the required SonarQube User token. You can also provide your organization key for SonarQube Cloud or the SonarQube URL if connecting to SonarQube Server.

For **SonarQube Cloud US**, set the URL to `https://sonarqube.us`.

Alternatively, you can manually configure the server via `mcp_config.json`:

* To connect with SonarQube Cloud:

In the Agent Side Panel, click the three dots (**...**) -> **MCP Store** -> **Manage MCP Servers** -> **View raw config**, and add the following:

```json
{
  "mcpServers": {
    "sonarqube": {
      "command": "docker",
      "args": ["run", "--init", "--pull=always", "-i", "--rm", "-e", "SONARQUBE_TOKEN", "-e", "SONARQUBE_ORG", "sonarsource/sonarqube-mcp"],
      "env": {
        "SONARQUBE_TOKEN": "",
        "SONARQUBE_ORG": ""
      }
    }
  }
}
```

For **SonarQube Cloud US**, manually add `"SONARQUBE_URL": "https://sonarqube.us"` to the `env` section and `"-e", "SONARQUBE_URL"` to the `args` array.

* To connect with SonarQube Server:

```json
{
  "mcpServers": {
    "sonarqube": {
      "command": "docker",
      "args": ["run", "--init", "--pull=always", "-i", "--rm", "-e", "SONARQUBE_TOKEN", "-e", "SONARQUBE_URL", "sonarsource/sonarqube-mcp"],
      "env": {
        "SONARQUBE_TOKEN": "",
        "SONARQUBE_URL": ""
      }
    }
  }
}
```

Claude Code

* To connect with SonarQube Cloud:

```bash
claude mcp add sonarqube \
  --env SONARQUBE_TOKEN=$SONAR_TOKEN \
  --env SONARQUBE_ORG=$SONAR_ORG \
  -- docker run --init --pull=always -i --rm -e SONARQUBE_TOKEN -e SONARQUBE_ORG sonarsource/sonarqube-mcp
```

For **SonarQube Cloud US**, add `--env SONARQUBE_URL=https://sonarqube.us` to the command.

* To connect with SonarQube Server:

```bash
claude mcp add sonarqube \
  --env SONARQUBE_TOKEN=$SONAR_USER_TOKEN \
  --env SONARQUBE_URL=$SONAR_URL \
  -- docker run --init --pull=always -i --rm -e SONARQUBE_TOKEN -e SONARQUBE_URL sonarsource/sonarqube-mcp
```

Codex CLI

Manually edit the configuration file at `~/.codex/config.toml` and add the following configuration:

* To connect with SonarQube Cloud:

```toml
[mcp_servers.sonarqube]
command = "docker"
args = ["run", "--init", "--pull=always", "--rm", "-i", "-e", "SONARQUBE_TOKEN", "-e", "SONARQUBE_ORG", "sonarsource/sonarqube-mcp"]
env = { "SONARQUBE_TOKEN" = "", "SONARQUBE_ORG" = "" }
```

For **SonarQube Cloud US**, add `"SONARQUBE_URL" = "https://sonarqube.us"` to the `env` section and `"-e", "SONARQUBE_URL"` to the `args` array.

* To connect with SonarQube Server:

```toml
[mcp_servers.sonarqube]
command = "docker"
args = ["run", "--init", "--pull=always", "--rm", "-i", "-e", "SONARQUBE_TOKEN", "-e", "SONARQUBE_URL", "sonarsource/sonarqube-mcp"]
env = { "SONARQUBE_TOKEN" = "", "SONARQUBE_URL" = "" }
```

Cursor

* To connect with SonarQube Cloud:

[![Install for SonarQube Cloud](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en-US/install-mcp?name=sonarqube&config=eyJlbnYiOnsiU09OQVJRVUJFX1RPS0VOIjoiWU9VUl9UT0tFTiIsIlNPTkFSUVVCRV9PUkciOiJZT1VSX1NPTkFSUVVCRV9PUkcifSwiY29tbWFuZCI6ImRvY2tlciBydW4gLS1pbml0IC0tcHVsbD1hbHdheXMgLWkgLS1ybSAtZSBTT05BUlFVQkVfVE9LRU4gLWUgU09OQVJRVUJFX09SRyBzb25hcnNvdXJjZS9zb25hcnF1YmUtbWNwIn0%3D)

For **SonarQube Cloud US**, manually add `"SONARQUBE_URL": "https://sonarqube.us"` to the `env` section in your MCP configuration after installation.

* To connect with SonarQube Server:

[![Install for SonarQube Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en-US/install-mcp?name=sonarqube&config=eyJlbnYiOnsiU09OQVJRVUJFX1RPS0VOIjoiWU9VUl9VU0VSX1RPS0VOIiwiU09OQVJRVUJFX1VSTCI6IllPVVJfU09OQVJRVUJFX1VSTCJ9LCJjb21tYW5kIjoiZG9ja2VyIHJ1biAtLWluaXQgLS1wdWxsPWFsd2F5cyAtaSAtLXJtIC1lIFNPTkFSUVVCRV9UT0tFTiAtZSBTT05BUlFVQkVfVVJMIHNvbmFyc291cmNlL3NvbmFycXViZS1tY3AifQ%3D%3D)

Gemini CLI

> **Note:** The Gemini CLI extension has moved to the [sonarqube-agent-plugins](https://github.com/SonarSource/sonarqube-agent-plugins) repository. Please install it from there going forward.

You can install our MCP server extension by using the following command:

```bash
gemini extensions install https://github.com/SonarSource/sonarqube-agent-plugins
```

You will need to set the required environment variables before starting Gemini:

**Environment Variables Required:**

* **For SonarQube Cloud:**
  - `SONARQUBE_TOKEN` - Your SonarQube Cloud token
  - `SONARQUBE_ORG` - Your organization key
  - `SONARQUBE_URL` - (Optional) Set to `https://sonarqube.us` for SonarQube Cloud US

* **For SonarQube Server:**
  - `SONARQUBE_TOKEN` - Your SonarQube Server USER token
  - `SONARQUBE_URL` - Your SonarQube Server URL

Once installed, the extension will be installed under `/.gemini/extensions/sonarqube/gemini-extension.json`.

GitHub Copilot CLI

After starting Copilot CLI, run the following command to add the SonarQube MCP server:

```bash
/mcp add
```

You will have to provide different information about the MCP server, you can use tab to navigate between fields.

* To connect with SonarQube Cloud:

```
Server Name: sonarqube
Server Type: Local (Press 1)
Command: docker
Arguments: run, --init, --pull=always, --rm, -i, -e, SONARQUBE_TOKEN, -e, SONARQUBE_ORG, sonarsource/sonarqube-mcp
Environment Variables: SONARQUBE_TOKEN=,SONARQUBE_ORG=
Tools: *
```

For **SonarQube Cloud US**, add `-e, SONARQUBE_URL` to Arguments and `SONARQUBE_URL=https://sonarqube.us` to Environment Variables.

* To connect with SonarQube Server:

```
Server Name: sonarqube
Server Type: Local (Press 1)
Command: docker
Arguments: run, --init, --pull=always, --rm, -i, -e, SONARQUBE_TOKEN, -e, SONARQUBE_URL, sonarsource/sonarqube-mcp
Environment Variables: SONARQUBE_TOKEN=,SONARQUBE_URL=
Tools: *
```

The configuration file is located at `~/.copilot/mcp-config.json`.

GitHub Copilot coding agent

GitHub Copilot coding agent can leverage the SonarQube MCP server directly in your CI/CD.

To add the secrets to your Copilot environment, follow the Copilot [documentation](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/extend-coding-agent-with-mcp#setting-up-a-copilot-environment-for-copilot-coding-agent). Only secrets with names prefixed with **COPILOT_MCP_** will be available to your MCP configuration.

In your GitHub repository, navigate under **Settings -> Copilot -> Coding agent**, and add the following configuration in the MCP configuration section:

* To connect with SonarQube Cloud:

```
{
  "mcpServers": {
    "sonarqube": {
      "type": "local",
      "command": "docker",
      "args": [
        "run",
        "--init",
        "--pull=always",
        "--rm",
        "-i",
        "-e",
        "SONARQUBE_TOKEN",
        "-e",
        "SONARQUBE_ORG",
        "sonarsource/sonarqube-mcp"
      ],
      "env": {
        "SONARQUBE_TOKEN": "COPILOT_MCP_SONARQUBE_TOKEN",
        "SONARQUBE_ORG": "COPILOT_MCP_SONARQUBE_ORG"
      },
      "tools": ["*"]
    }
  }
}
```

For **SonarQube Cloud US**, add `"-e", "SONARQUBE_URL"` to the `args` array and `"SONARQUBE_URL": "COPILOT_MCP_SONARQUBE_URL"` to the `env` section, then set the secret `COPILOT_MCP_SONARQUBE_URL=https://sonarqube.us`.

* To connect with SonarQube Server:

```
{
  "mcpServers": {
    "sonarqube": {
      "type": "local",
      "command": "docker",
      "args": [
        "run",
        "--init",
        "--pull=always",
        "--rm",
        "-i",
        "-e",
        "SONARQUBE_TOKEN",
        "-e",
        "SONARQUBE_URL",
        "sonarsource/sonarqube-mcp"
      ],
      "env": {
        "SONARQUBE_TOKEN": "COPILOT_MCP_SONARQUBE_USER_TOKEN",
        "SONARQUBE_URL": "COPILOT_MCP_SONARQUBE_URL"
      },
      "tools": ["*"]
    }
  }
}
```

Kiro

Create a `.kiro/settings/mcp.json` file in your workspace directory (or edit if it already exists), add the following configuration:

* To connect with SonarQube Cloud:

```
{
  "mcpServers": {
    "sonarqube": {
      "command": "docker",
      "args": [
        "run",
        "--init",
        "--pull=always",
        "-i",
        "--rm",
        "-e", 
        "SONARQUBE_TOKEN",
        "-e",
        "SONARQUBE_ORG",
        "sonarsource/sonarqube-mcp"
      ],
      "env": {
        "SONARQUBE_TOKEN": "",
        "SONARQUBE_ORG": ""
      },
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

For **SonarQube Cloud US**, add `"-e", "SONARQUBE_URL"` to the `args` array and `"SONARQUBE_URL": "https://sonarqube.us"` to the `env` section.

* To connect with SonarQube Server:

```
{
  "mcpServers": {
    "sonarqube": {
      "command": "docker",
      "args": [
        "run",
        "--init",
        "--pull=always",
        "-i",
        "--rm",
        "-e", 
        "SONARQUBE_TOKEN",
        "-e",
        "SONARQUBE_URL",
        "sonarsource/sonarqube-mcp"
      ],
      "env": {
        "SONARQUBE_TOKEN": "",
        "SONARQUBE_URL": ""
      },
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

    

VS Code

You can use the following buttons to simplify the installation process within VS Code.


For **SonarQube Cloud US**, manually add `"SONARQUBE_URL": "https://sonarqube.us"` to the `env` section in your MCP configuration after installation.


Windsurf

SonarQube MCP Server is available as a Windsurf plugin. Follow these instructions:

1. Open Windsurf **Settings** > **Cascade** > **MCP Servers** and select **Open MCP Marketplace** 
2. Search for `sonarqube` on the Cascade MCP Marketplace
3. Choose the **SonarQube MCP Server** and select **Install**
4. Add the required SonarQube User token. Then add the organization key if you want to connect with SonarQube Cloud, or the SonarQube URL if you want to connect to SonarQube Server or Community Build.

For **SonarQube Cloud US**, set the URL to `https://sonarqube.us`.

Zed

Navigate to the **Extensions** view in Zed and search for **SonarQube MCP Server**.
When installing the extension, you will be prompted to provide the necessary environment variables:

* When using SonarQube Cloud:

```
{
  "sonarqube_token": "YOUR_SONARQUBE_TOKEN",
  "sonarqube_org": "SONARQUBE_ORGANIZATION_KEY",
  "docker_path": "DOCKER_PATH"
}
```

For **SonarQube Cloud US**, add `"sonarqube_url": "https://sonarqube.us"` to the configuration.

* When using SonarQube Server:

```
{
  "sonarqube_token": "YOUR_SONARQUBE_USER_TOKEN",
  "sonarqube_url": "YOUR_SONARQUBE_SERVER_URL",
  "docker_path": "DOCKER_PATH"
}
```

The `docker_path` is the path to a docker executable. Examples:

Linux/macOS: `/usr/bin/docker` or `/usr/local/bin/docker`

Windows: `C:\Program Files\Docker\Docker\resources\bin\docker.exe`

> 💡 **Tip:** We recommend pulling the latest image regularly or before reporting issues to ensure you have the most up-to-date features and fixes.

## Manual installation

You can manually install the SonarQube MCP server by copying the following snippet in the MCP servers configuration file:

* To connect with SonarQube Cloud:

```JSON
{
  "sonarqube": {
    "command": "docker",
    "args": [
      "run",
      "--init",
      "--pull=always",
      "-i",
      "--rm",
      "-e",
      "SONARQUBE_TOKEN",
      "-e",
      "SONARQUBE_ORG",
      "sonarsource/sonarqube-mcp"
    ],
    "env": {
      "SONARQUBE_TOKEN": "",
      "SONARQUBE_ORG": ""
    }
  }
}
```

* To connect with SonarQube Server:

```JSON
{
  "sonarqube": {
    "command": "docker",
    "args": [
      "run",
      "--init",
      "--pull=always",
      "-i",
      "--rm",
      "-e",
      "SONARQUBE_TOKEN",
      "-e",
      "SONARQUBE_URL",
      "sonarsource/sonarqube-mcp"
    ],
    "env": {
      "SONARQUBE_TOKEN": "",
      "SONARQUBE_URL": ""
    }
  }
}
```

## Integration with SonarQube for IDE

The SonarQube MCP Server can integrate with [SonarQube for IDE](https://www.sonarsource.com/products/sonarlint/) to further enhance your development workflow, providing better code analysis and insights directly within your IDE.

Configuration

When using SonarQube for IDE, the `SONARQUBE_IDE_PORT` environment variable should be set with the correct port number. SonarQube for VS Code includes a Quick Install button, which automatically sets the correct port configuration.

For example, with SonarQube Cloud:

```JSON
{
  "sonarqube": {
    "command": "docker",
    "args": [
      "run",
      "--init",
      "--pull=always",
      "-i",
      "--rm",
      "-e",
      "SONARQUBE_TOKEN",
      "-e",
      "SONARQUBE_ORG",
      "-e",
      "SONARQUBE_IDE_PORT",
      "sonarsource/sonarqube-mcp"
    ],
    "env": {
      "SONARQUBE_TOKEN": "",
      "SONARQUBE_ORG": "",
      "SONARQUBE_IDE_PORT": ""
    }
  }
}
```

> When running the MCP server in a container on Linux, the container cannot access the SonarQube for IDE embedded server running on localhost. To allow the container to connect to the SonarQube for IDE server, add the `--network=host` option to your container run command.

## Configuration

Depending on your environment, you should provide specific environment variables.

### Base

You should add the following variable when running the MCP Server:

| Environment variable             | Description                                                                                                                                                                                                                 |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `STORAGE_PATH`                   | Mandatory absolute path to a writable directory where SonarQube MCP Server will store its files (e.g., for creation, updates, and persistence), it is automatically provided when using the container image                 |
| `SONARQUBE_PROJECT_KEY`          | Optional default project key. When set, all tools that require a project key will use this value automatically — the `projectKey` parameter is removed from their schema entirely. Useful when working on a single project. |
| `SONARQUBE_IDE_PORT`             | Optional port number between 64120 and 64130 used to connect SonarQube MCP Server with SonarQube for IDE.                                                                                                                   |
| `SONARQUBE_DEBUG_ENABLED`        | When set to `true`, enables debug logging. Debug logs are written to both the log file and STDERR. Useful for troubleshooting connectivity or configuration issues. Default: `false`.                                       |
| `SONARQUBE_LOG_TO_FILE_DISABLED` | When set to `true`, disables writing logs to disk entirely. No log files will be created under `STORAGE_PATH/logs/`. Useful in containerized or ephemeral environments where file logging is undesirable. Default: `false`. |

### Workspace Mount (Reducing Context Bloat)

By default, analysis tool `analyze_code_snippet` requires the agent to pass the full file content as a `fileContent` argument. For large files or when analyzing many files in a session, this significantly increases context window usage and cost.

**Solution:** mount your project directory into the container at `/app/mcp-workspace`. When this mount is detected, the server reads files directly from disk using the project-relative `filePath` argument — file content never passes through the agent context.

```json
{
  "args": [
    "run", "-i", "--rm", "--init", "--pull=always",
    "-e", "SONARQUBE_TOKEN",
    "-e", "SONARQUBE_ORG",
    "-v", "/path/to/your/project:/app/mcp-workspace",
    "sonarsource/sonarqube-mcp"
  ]
}
```

When the mount is active:
- `run_advanced_code_analysis` becomes available if your organization is entitled to it
- `analyze_code_snippet`: `filePath` is required and `fileContent` is not used — the server resolves the file the same way

### Selective Tool Enablement

By default, only important toolsets are enabled to reduce context overhead. You can enable additional toolsets as needed.

| Environment variable  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**官方网站：** [https://github.com/SonarSource/sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `code quality`, `sonarqube`, `code review`, `official`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`docker`
- 参数：`run --init --pull=always -i --rm -e SONARQUBE_TOKEN -e SONARQUBE_URL sonarsource/sonarqube-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/sonarsource-sonarqube.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
