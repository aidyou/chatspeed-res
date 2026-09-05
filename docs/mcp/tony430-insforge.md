---
title: "InsForge"
description: "InsForge turns your coding agents into full-stack builders, letting them add backend features like auth, databases, file storage, serverless functions, and LLMs to your apps in seconds."
---

# InsForge

InsForge turns your coding agents into full-stack builders, letting them add backend features like auth, databases, file storage, serverless functions, and LLMs to your apps in seconds.

alt="Insforge Banner">
  

[![MCP Badge](/mcp-assets/ae2b3adc954c277ae2a75d29e41af32b.svg)](https://lobehub.com/mcp/insforge-insforge-mcp)

# Insforge MCP Server

InsForge turns your coding agents into full-stack builders, letting them add backend features like auth, databases, file storage, serverless functions, and LLMs to your apps in seconds.

This repo is Model Context Protocol server for [Insforge](https://github.com/InsForge/insforge).

  

## 📖 Documentation

Please visit the [main Insforge repository](https://github.com/InsForge/insforge) for:

- Installation and setup instructions
- Configuration guide
- Available tools and usage examples
- API documentation
- Contributing guidelines

## 🚀 Quick Start

### Automated Installation (Recommended)

Use the InsForge installer to automatically configure MCP for your client:

```bash
# Claude Code
npx @insforge/install --client claude-code --env API_KEY=your_api_key --env API_BASE_URL=http://localhost:7130

# Cursor
npx @insforge/install --client cursor --env API_KEY=your_api_key --env API_BASE_URL=http://localhost:7130

# Windsurf
npx @insforge/install --client windsurf --env API_KEY=your_api_key --env API_BASE_URL=http://localhost:7130

# Cline
npx @insforge/install --client cline --env API_KEY=your_api_key --env API_BASE_URL=http://localhost:7130

# Roo Code
npx @insforge/install --client roocode --env API_KEY=your_api_key --env API_BASE_URL=http://localhost:7130
# Trae
npx @insforge/install --client trae --env API_KEY=your_api_key --env API_BASE_URL=http://localhost:7130

# Install dev version for testing
npx @insforge/install --client cursor --env API_KEY=your_api_key --env API_BASE_URL=http://localhost:7130 --dev
```

Replace:
- `your_api_key` with your InsForge API key
- `http://localhost:7130` with your InsForge instance URL (optional, defaults to localhost:7130)

### Manual Installation

If you prefer to manually configure your MCP client, add this to your MCP settings file:

```json
{
  "mcpServers": {
    "insforge": {
      "command": "npx",
      "args": [
        "-y",
        "@insforge/mcp@latest"
      ],
      "env": {
        "API_KEY": "your_api_key",
        "API_BASE_URL": "http://localhost:7130"
      }
    }
  }
}
```

For detailed setup instructions, see the [Insforge Documentation](https://docs.insforge.dev).

## 📄 License

Apache License 2.0 - see the [LICENSE](https://github.com/InsForge/insforge-mcp/blob/HEAD/LICENSE) file for details.

---

Part of the [Insforge](https://github.com/InsForge/insforge) project.

**Official site: ** [https://github.com/InsForge/insforge-mcp](https://github.com/InsForge/insforge-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `developer tools`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @insforge/mcp@latest`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/tony430-insforge.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
