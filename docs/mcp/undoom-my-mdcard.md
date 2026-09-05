---
title: "my_mdcard"
description: "MD2Card MCP Server homepage: https://md2card.cn"
---

# my_mdcard

MD2Card MCP Server homepage: https://md2card.cn

# mycard MCP Server

> Official Website: https://md2card.cn/zh/my/api-keys

## Introduction

mycard is a powerful Markdown to knowledge card conversion tool that can transform ordinary Markdown documents into beautiful knowledge cards, supporting various visual styles and customization options. Whether for social media sharing, study notes, or professional presentations, mycard can meet your needs.

## Installation and Usage

Before you start using it, you need to obtain an API key first. Please visit the [mycard official website](https://md2card.cn/zh?referralCode=github) to apply for your exclusive key.

### Method 1: Using npx (Recommended)

This is the simplest way, no installation required, just run with npx directly:

bash
# Set API key and run
MYCARD_API_KEY="Your API Key" npx mycard-mcp-server

### Method 2: Global Installation

If you need to use it frequently, you can choose to install globally:

bash
# Global installation
npm install -g mycard-mcp-server

# Run the service
MYCARD_API_KEY="Your API Key" mycard-mcp-server

### Method 3: Local Configuration

For developers or users who need custom features:

1. Clone the project locally
2. Find the path of the index.js file
3. Replace this path in your client's MCP configuration file

## Features

### Rich Theme Selection

mycard offers 22 exquisite theme styles to meet different scenario needs:

- **Daily Style**: Apple Notes, Notebook, Minimalist High-end Gray
- **Artistic Style**: Pop Art, Art Deco, Watercolor Art, Traditional Chinese
- **Modern Design**: Glassmorphism, Dreamy Gradient, Dark Tech, Cyberpunk
- **Special Style**: Warm and Soft, Fresh and Natural, Purple Xiaohongshu, Vintage Typewriter, Children's Fairy Tale, Business Briefing, Japanese Magazine, Minimalist Black and White

### Intelligent Features

- **Intelligent Size Adaptation**: Automatically adjusts content layout to ensure perfect display at different sizes
- **Three Content Splitting Modes**: Default automatic splitting, also supports manual control of splitting methods
- **Standardized Interface**: Provides services through the MCP protocol, easy to integrate into various workflows

### Latest Features

- **Directly Read Markdown Files**: Supports reading content directly from file paths, no need to manually copy and paste
- **Custom Card Type/Size**: Supports specifying card type and size directly through the `type` parameter, more flexible

## Usage

mycard provides multiple flexible usage methods, and you can choose the most suitable one according to your needs.

### Method 1: Directly Provide Markdown Content

The most basic usage method, directly passing in Markdown text:

json
{
  "markdown": "# My Knowledge Card\n\nThis is a sample content, supporting all standard **Markdown** syntax.\n\n- List item 1\n- List item 2\n\n> Quoted text is also perfectly supported"
}

### Method 2: Provide Markdown File Path

Suitable for handling existing Markdown files, no need to copy the content:

json
{
  "markdownFile": "/path/to/your/file.md"
}

### Method 3: Customize Card Type and Size

#### Preset Card Types

mycard supports the following preset types, making it easy to quickly create cards for specific scenarios:

| Type | Size | Applicable Scenarios |
|------|------|----------------------|
| Xiaohongshu | 440×586 | Xiaohongshu notes, social media sharing |
| Square | 500×500 | General social media, avatars, thumbnails |
| Mobile Poster | 440×782 | Long-form content for mobile display |
| A4 Paper Print | 595×842 | Printing documents, PDF export |

Usage example:

json
{
  "markdown": "# My Xiaohongshu Note\n\nShare some interesting content...",
  "type": "Xiaohongshu"
}

#### Custom Size

You can also fully customize the card size using the `width` and `height` parameters:

json
{
  "markdown": "# Custom Size Card\n\nFully customized size according to my needs",
  "width": 600,
  "height": 800
}

> **Tip**: For the best results, it is recommended to keep the aspect ratio between 1:1 and 1:2

## Client Configuration

mycard supports integration with various clients through the MCP (Model Control Protocol) protocol. Below are the configuration methods for common clients.

### General MCP Client ConfigurationFor a generic client that supports the MCP protocol, add the following to the configuration file:

json
{
  "mycard-server": {
    "command": "npx",
    "args": ["mycard-mcp-server@latest"],
    "env": {
      "MYCARD_API_KEY": "Your API key"
    }
  }
}

### Cursor Editor Configuration

[Cursor](https://cursor.sh/) is a code editor that supports AI features. You can add the following to its MCP configuration file:

json
{
  "mycard-server": {
    "command": "npx",
    "args": ["-y", "mycard-mcp-server@latest"],
    "env": {
      "MYCARD_API_KEY": "Your API key"
    }
  }
}

### Other Editors and Tools

mycard can be integrated with any tool that supports the MCP protocol, including but not limited to:

- VS Code (via plugins)
- JetBrains series IDEs
- Command-line tools

## Notes

- **API Key**: The MYCARD_API_KEY environment variable is required and will only be checked at runtime. This environment variable is not needed when installing the package.
- **Version Updates**: Using the `@latest` tag ensures you always use the latest version, or you can specify a particular version number.
- **Custom Configuration**: Advanced users can perform deeper customizations by modifying the source code.

## Getting Help

- **Official Documentation**: Visit the [mycard official website](https://md2card.cn) for complete documentation.
- **API Key Application**: Apply for your API key through [this link](https://md2card.cn/zh?referralCode=github).
- **Feedback**: If you have any issues or suggestions, please contact us via the official website.

**Official site: ** [https://github.com/maqi1520/md2card-mcp-server](https://github.com/maqi1520/md2card-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `memory`
- Tags: `knowledge and memory`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y md2card-mcp-server@latest`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/undoom-my-mdcard.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
