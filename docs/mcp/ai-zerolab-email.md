---
title: "mcp-email-server"
description: "Provides IMAP and SMTP capabilities, enabling developers to manage email services with seamless integration and automated workflows."
---

# mcp-email-server

Provides IMAP and SMTP capabilities, enabling developers to manage email services with seamless integration and automated workflows.

# mcp-email-server

[![Release](/mcp-assets/44568dba424b415d971809a279ce2b35.svg)](https://img.shields.io/github/v/release/ai-zerolab/mcp-email-server)
[![Build status](/mcp-assets/abc15660130701393306443a8e2a39cb.svg)](https://github.com/ai-zerolab/mcp-email-server/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](/mcp-assets/56374751c0b5213655ce0d5025025dc6.svg)](https://codecov.io/gh/ai-zerolab/mcp-email-server)
[![Commit activity](/mcp-assets/c488edaf3f16a47fb518204f08a6584b.svg)](https://img.shields.io/github/commit-activity/m/ai-zerolab/mcp-email-server)
[![License](/mcp-assets/3558c36785ba77f4575ce643a3a48f2a.svg)](https://img.shields.io/github/license/ai-zerolab/mcp-email-server)
[Smithery](https://smithery.ai/server/@ai-zerolab/mcp-email-server)

IMAP and SMTP via MCP Server

- **Github repository**: 
- **Documentation** 

## Installation

### Manual Installation

We recommend using [uv](https://github.com/astral-sh/uv) to manage your environment.

Try `uvx mcp-email-server@latest ui` to config, and use following configuration for mcp client:

```json
{
  "mcpServers": {
    "zerolib-email": {
      "command": "uvx",
      "args": ["mcp-email-server@latest", "stdio"]
    }
  }
}
```

This package is available on PyPI, so you can install it using `pip install mcp-email-server`

After that, configure your email server using the ui: `mcp-email-server ui`

Then you can try it in [Claude Desktop](https://claude.ai/download). If you want to intergrate it with other mcp client, run `$which mcp-email-server` for the path and configure it in your client like:

```json
{
  "mcpServers": {
    "zerolib-email": {
      "command": "{{ ENTRYPOINT }}",
      "args": ["stdio"]
    }
  }
}
```

If `docker` is avaliable, you can try use docker image, but you may need to config it in your client using `tools` via `MCP`. The default config path is `~/.config/zerolib/mcp_email_server/config.toml`

```json
{
  "mcpServers": {
    "zerolib-email": {
      "command": "docker",
      "args": ["run", "-it", "ghcr.io/ai-zerolab/mcp-email-server:latest"]
    }
  }
}
```

### Installing via Smithery

To install Email Server for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@ai-zerolab/mcp-email-server):

```bash
npx -y @smithery/cli install @ai-zerolab/mcp-email-server --client claude
```

## Development

This project is managed using [uv](https://github.com/ai-zerolab/uv).

Try `make install` to install the virtual environment and install the pre-commit hooks.

Use `uv run mcp-email-server` for local development.

## Releasing a new version

- Create an API Token on [PyPI](https://pypi.org/).
- Add the API Token to your projects secrets with the name `PYPI_TOKEN` by visiting [this page](https://github.com/ai-zerolab/mcp-email-server/settings/secrets/actions/new).
- Create a [new release](https://github.com/ai-zerolab/mcp-email-server/releases/new) on Github.
- Create a new tag in the form `*.*.*`.

For more details, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/cicd/#how-to-trigger-a-release).

**Official site: ** [https://github.com/ai-zerolab/mcp-email-server](https://github.com/ai-zerolab/mcp-email-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `communication`
- Tags: `communication`, `developer tools`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `mcp-email-server@latest stdio`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/ai-zerolab-email.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
