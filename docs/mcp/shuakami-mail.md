---
title: "mcp-mail"
description: "An MCP-based email tool that enables AI models to access email services through standardized interfaces, allowing AI assistants to perform various email operations like sending emails, reading inboxes…"
---

# mcp-mail

An MCP-based email tool that enables AI models to access email services through standardized interfaces, allowing AI assistants to perform various email operations like sending emails, reading inboxes…

# Mail MCP Tool

[![ISC License](/mcp-assets/c0f97d58722d396df536af21aec4c5f9.svg)](https://opensource.org/licenses/ISC)
[![Node.js](/mcp-assets/8c67e9c4c130e734f4648fb076a7355b.svg)](https://nodejs.org/)
[![TypeScript](/mcp-assets/722312b2deefe5976cd4c92516fa3afb.svg)](https://www.typescriptlang.org/)
[![Mail](/mcp-assets/fd7c9ae04250a10869facd4a0383c766.svg)](https://github.com/shuakami/mcp-mail)

[English Version (https://github.com/shuakami/mcp-mail/blob/HEAD/README-EN.md)](https://github.com/shuakami/mcp-mail/blob/HEAD/README-EN.md)

## What is this

This is an email tool based on MCP (Model Context Protocol) that lets AI models access email services through a standardized interface.

In short, it allows AI assistants to perform various email operations - such as sending emails, reading the inbox, and handling attachments - without requiring users to manually write complex API calls or switch to an email client.

Supported features (click to expand)

- **Email sending**: plain-text emails, HTML emails, emails with attachments, mass emails
- **Email receiving and querying**: get folder lists, list emails, advanced search, get email details
- **Email management**: mark as read/unread, delete emails, move emails
- **Attachment management**: view attachment lists, download attachments, view attachment contents
- **Contact management**: get contact lists, search contacts

Feature highlights (click to expand)

Here are some core features of the Mail MCP tool:

- **Advanced search**: supports complex search by multiple folders, keywords, date ranges, senders, recipients, etc.
- **Smart contact management**: automatically extracts contact information from email history, including contact frequency analysis
- **Content range control**: view large emails in segments to avoid loading too much content
- **Multiple email formats**: supports sending and displaying plain-text and HTML emails
- **Attachment handling**: intelligently identifies attachment types and supports previews of different attachment types such as text and images
- **Safe and reliable**: all email operations are processed locally; sensitive information is not forwarded through third-party servers

With simple natural-language instructions, the AI can help you with all of the above, without manually writing API calls or performing complex operations in an email client.

## Quick Start

### 0. Environment preparation

If you have never used Node.js before (click to expand)

1. Install Node.js and npm
   - Visit the [Node.js official website](https://nodejs.org/)
   - Download and install the LTS (Long Term Support) version
   - Select the default options during installation; the installer will install both Node.js and npm

2. Verify the installation
   - After installation, open Command Prompt (CMD) or PowerShell
   - Run the following commands to confirm the installation:
```bash
     node --version
     npm --version
```
   - If version numbers are displayed, the installation succeeded

3. Install Git (if not already installed)
   - Visit the [Git official website](https://git-scm.com/)
   - Download and install Git
   - Use the default options during installation

4. Install Python 3.11 or higher (required)
   - Visit the [Python official website](https://www.python.org/downloads/)
   - Download and install Python 3.11 or higher
   - **Important**: make sure to check the "Add Python to PATH" option during installation
   - After installation, **restart your computer** to make sure the environment variables take effect

### 1. Clone and install

```bash
git clone https://github.com/shuakami/mcp-mail.git
cd mcp-mail
npm install
npm run build
```

### 2. Build the project

```bash
npm run build
```

### 3. Add to the Cursor MCP configuration

Configure MCP according to your operating system:

Windows configuration (click to expand)

1. In Cursor, open or create the MCP config file: `C:\Users\YOUR_USERNAME\.cursor\mcp.json`
   - Note: replace `YOUR_USERNAME` with your Windows username

2. Add or modify the configuration as follows:

```json
{
  "mcpServers": {
    "mail-mcp": {
      "command": "pythonw",
      "args": [
        "C:/Users/YOUR_USERNAME/mcp-mail/bridging_mail_mcp.py"
      ],
      "env": {
        "SMTP_HOST": "smtp.qq.com",
        "SMTP_PORT": "465",
        "SMTP_SECURE": "true",
        "SMTP_USER": "your.email@qq.com",
        "SMTP_PASS": "your-app-specific-password",
        "IMAP_HOST": "imap.qq.com",
        "IMAP_PORT": "993",
        "IMAP_SECURE": "true",
        "IMAP_USER": "your.email@qq.com",
        "IMAP_PASS": "your-app-specific-password",
        "DEFAULT_FROM_NAME": "Your Name",
        "DEFAULT_FROM_EMAIL": "your.email@qq.com"
      }
    }
  }
}
```

> **Please note**:
> - Replace `YOUR_USERNAME` with your Windows username
> - Make sure the path points to the directory where you cloned or extracted the project
> - The path should reflect the actual location of the project files
> - **Do not delete the cloned or extracted folder**; this will cause MCP to stop working

macOS configuration (click to expand)

1. In Cursor, open or create the MCP config file: `/Users/YOUR_USERNAME/.cursor/mcp.json`
   - Note: replace `YOUR_USERNAME` with your macOS username

2. Add or modify the configuration as follows:

```json
{
  "mcpServers": {
    "mail-mcp": {
      "command": "pythonw3",
      "args": [
        "/Users/YOUR_USERNAME/mcp-mail/bridging_mail_mcp.py"
      ]
    }
  }
}
```

> **Please note**:
> - Replace `YOUR_USERNAME` with your macOS username
> - Make sure the path points to the directory where you cloned or extracted the project
> - The path should reflect the actual location of the project files
> - **Do not delete the cloned or extracted folder**; this will cause MCP to stop working

Linux configuration (click to expand)

1. In Cursor, open or create the MCP config file: `/home/YOUR_USERNAME/.cursor/mcp.json`
   - Note: replace `YOUR_USERNAME` with your Linux username

2. Add or modify the configuration as follows:

```json
{
  "mcpServers": {
    "mail-mcp": {
      "command": "python3",
      "args": [
        "/home/YOUR_USERNAME/mcp-mail/bridging_mail_mcp.py"
      ]
    }
  }
}
```

> **Please note**:
> - Replace `YOUR_USERNAME` with your Linux username
> - Make sure the path points to the directory where you cloned or extracted the project
> - The path should reflect the actual location of the project files
> - **Do not delete the cloned or extracted folder**; this will cause MCP to stop working

### 4. Start the service

After configuring, restart the Cursor editor; it will start the MCP service automatically. Then you can start using it.

Usage examples (click to expand)

You can ask the AI to do things like:
- "List my email folders"
- "Show the latest 5 emails in the inbox"
- "Send an email with the subject 'test email' to example@example.com"
- "Search for emails containing the keyword 'invoice'"
- "View the details of email with UID 1234"
- "Download attachments from an email"

## How it works

Technical implementation details (click to expand)

This tool is implemented based on the **MCP (Model Context Protocol)** standard, acting as a bridge between AI models and email services. It uses **nodemailer** and **node-imap** as the underlying email clients and **Zod** for request validation and type checking.

Main technical components include:
- **SMTP client**: handles all email sending, supporting HTML content and attachments
- **IMAP client**: connects to the mail server to fetch email lists, details, and attachments
- **Email parser**: uses **mailparser** to parse complex email formats
- **Content processing**: intelligently handles HTML and plain-text content, with segmented loading for large emails
- **Contact extraction**: automatically extracts and organizes contact information from email history

Each email operation is wrapped as a standardized MCP tool that receives structured parameters and returns formatted results. All data is processed to ensure it is presented in a human-readable format, so AI models can easily understand the content structure of emails.

## License

ISC

---

If this project helps you, feel free to give it a Star. <3

**Official site: ** [https://github.com/shuakami/mcp-mail](https://github.com/shuakami/mcp-mail)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `communication`
- Tags: `communication`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `pythonw`
- Args: `C:/Users/YOUR_USERNAME/mcp-mail/bridging_mail_mcp.py`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/shuakami-mail.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
