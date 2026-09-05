---
title: "source-sage-mcp-server"
description: "A TypeScript-based server that visualizes project directory structures in Markdown format, automatically documenting file contents with syntax highlighting and supporting customizable exclusion patter…"
---

# source-sage-mcp-server

A TypeScript-based server that visualizes project directory structures in Markdown format, automatically documenting file contents with syntax highlighting and supporting customizable exclusion patter…

# SourceSage MCP

## Overview

SourceSage is an MCP server that visualizes a project's directory structure in a beautiful Markdown format. Implemented in TypeScript, it offers advanced customization and flexible exclusion pattern support. It also automatically documents the contents of each file, making it easy to grasp the overall picture of a project.

## Key Features

- Outputs the directory structure in Markdown format
- Beautiful tree structure display (ASCII art)
- Automatic documentation of file contents (with language-specific syntax highlighting)
- Flexible exclusion patterns (.SourceSageignore)
- Modern implementation with ES2022 and the Node16 module system
- High reliability through strict type checking

## Tech Stack

- TypeScript (ES2022 target)
- Model Context Protocol SDK (v0.6.0)
- Node.js (Node16 module system)
- glob (v11.0.0) - file pattern matching
- ignore (v6.0.2) - flexible file exclusion

## Project Structure

```plaintext
source-sage/
├── assets/
│   └── header.svg          # Project header image
├── src/
│   └── index.ts           # Main server implementation
├── build/                 # Compiled JavaScript files
├── .gitignore            # Git exclusion settings
├── .SourceSageignore     # SourceSage-specific exclusion settings
├── package.json          # Project settings and dependencies
├── README.md            # Project documentation
└── tsconfig.json        # TypeScript settings
```

## TypeScript Configuration

```json
{
  "compilerOptions": {
    "target": "ES2022",        // Leverage the latest ECMAScript features
    "module": "Node16",        // Use Node.js 16's latest module system
    "moduleResolution": "Node16",
    "outDir": "./build",      // Output directory for compiled files
    "rootDir": "./src",       // Root directory of source files
    "strict": true,           // Enable strict type checking
    "esModuleInterop": true,  // Ensure interoperability with CommonJS modules
    "skipLibCheck": true,     // Skip checking of type definition files
    "forceConsistentCasingInFileNames": true  // Strictly manage file name casing
  }
}
```

## Installation

### Install from npm
```bash
npm install -g @sunwood-ai-labs/source-sage-mcp-server
```

### Build from source
```bash
git clone https://github.com/sunwood-ai-labs/source-sage-mcp-server.git
cd source-sage-mcp-server
npm install
npm run build
```

## Usage

### Configure as an MCP server

1. Add the following to the MCP config file:

```json
{
  "mcpServers": {
    "source-sage": {
      "command": "node",
      "args": ["C:/path/to/source-sage/build/index.js"]
    }
  }
}
```

### Available Tools

#### generate_structure

Generates the project's directory structure and creates a detailed document that includes file contents.

```typescript
interface GenerateStructureArgs {
  // Path of the directory whose structure will be generated (required)
  // Always specify an absolute path
  path: string;
  // Path of the .SourceSageignore file (optional)
  // If specified, use an absolute path
  ignorePath?: string;
}
```

### Usage example

```typescript
// Use with an absolute path (recommended)
const result = await mcpClient.callTool('source-sage', 'generate_structure', {
  path: 'C:/Users/your-name/path/to/your-project',
  ignorePath: 'C:/Users/your-name/path/to/your-project/.SourceSageignore'
});
```

### Output sample

Example output of actual project structure:

```plaintext
# Project: source-sage

## Directory Structure

OS: win32
Directory: C:\Users\your-name\source-sage

└─ source-sage/
   ├─ src/
   │  └─ index.ts          # Main implementation of the MCP server
   ├─ package.json         # Project dependencies and settings
   ├─ README.md           # Detailed project description
   └─ tsconfig.json       # TypeScript compilation settings
```

This output includes the following information:

- Project name and OS info
- Directory tree structure
- Role and description of each file
- Exclusion of unnecessary files via .SourceSageignore

## Configuring .SourceSageignore

Create a `.SourceSageignore` file in the project root and write the patterns you want to exclude. The following exclusion patterns are included by default:

```plaintext
# Version control system related
.git
.gitignore

# Cache files
__pycache__
.pytest_cache
**/__pycache__/**
*.pyc

# Build / distribution related
build
dist
*.egg-info

# Temp files / output
output
output.md
test_output
.SourceSageAssets
.SourceSageAssetsDemo

# Assets
*.png
*.svg
assets

# Other
LICENSE
example
folder
package-lock.json
```

## Output Example

```plaintext
  # Project: my-project

  ## Directory Structure

  OS: win32
  Directory: C:\path\to\my-project

  └─ my-project/
    ├─ src/
    │  ├─ index.ts
    │  └─ utils/
    │     └─ helper.ts
    └─ package.json

  ## File Contents

  ### `src/index.ts`
  **Type**: TypeScript Source File

```

## Developer Information

### Key implementation details

- **Server Class**: the `SourceSageServer` class provides the core functionality of the MCP server
- **Tree Building**:
  - The `buildTree` method recursively parses the directory structure
  - Sorts directories and files appropriately for display
- **File Filtering**:
  - Uses the `ignore` package for flexible file exclusion
  - Supports rich default exclusion patterns and custom settings
- **Content Generation**:
  - Provides appropriate syntax highlighting based on file type
  - Offers additional information based on file type
- **Async Processing**:
  - Uses the `glob` package for efficient file scanning
  - Supports large projects through asynchronous processing

### Setting up the development environment

```bash
# Clone the repository
git clone https://github.com/sunwood-ai-labs/source-sage-mcp-server.git

# Install dependencies
npm install

# Build for development
npm run build

# Start the development server
npm run inspector
```

### Available npm scripts

- `npm run build`: compiles TypeScript and sets execute permissions
- `npm run prepare`: automatic build on install
- `npm run watch`: automatic compilation during development
- `npm run inspector`: launch the MCP inspector

## Contributing

1. Fork this repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add an amazing feature'`)
4. Push the branch (`git push origin feature/amazing-feature`)
5. Create a Pull Request

## License

MIT License - see the LICENSE file for details.

## Related Links

- [npm package](https://www.npmjs.com/package/@sunwood-ai-labs/source-sage-mcp-server)
- [GitHub repository](https://github.com/sunwood-ai-labs/source-sage-mcp-server)
- [Bug reports](https://github.com/sunwood-ai-labs/source-sage-mcp-server/issues)

## Maintainers

- Sunwood AI Labs Team

---

Made with <3 by Sunwood AI Labs

**Official site: ** [https://github.com/Sunwood-ai-labs/source-sage-mcp-server](https://github.com/Sunwood-ai-labs/source-sage-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `files`
- Tags: `developer tools`, `file systems`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `node`
- Args: `C:/path/to/source-sage/build/index.js`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/sunwood-ai-labs-source-sage.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
