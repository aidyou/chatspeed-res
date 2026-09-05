---
title: "answer-book-mcp"
description: "Book of Answers MCP Service A wisdom answer generation service based on the Model Context Protocol, providing random and philosophical answers to your questions. Source Address - https://github.com/li…"
---

# answer-book-mcp

Book of Answers MCP Service A wisdom answer generation service based on the Model Context Protocol, providing random and philosophical answers to your questions. Source Address - https://github.com/li…

# Book of Answers MCP Service

A wisdom answer generation service based on the Model Context Protocol, providing random and philosophical answers to your questions.

## Source Address
- https://github.com/liuyvan2025-art/answer-book-mcp

## Features

- 🎯 Randomly generate wise answers
- 📊 Query history records and statistics
- 🎨 Support for custom answers
- 💾 Persistent storage configuration

## Inspector

1. Execute: `npx @modelcontextprotocol/inspector uvx answer-book-mcp`

## MCP Server Configuration

json
{
  "mcpServers": {
    "answer-book-mcp": {
      "args": [
        "answer-book-mcp@latest"
      ],
      "command": "uvx"
    }
  }
}

## API Documentation

- `ask_question(question: str)` - Ask a question to get an answer
- `get_recent_history(limit: int)` - Get recent history
- `get_statistics()` - Get usage statistics
- `add_custom_answer(answer_text: str)` - Add a custom answer

## Usage Example
This MCP service can be used through various MCP clients, such as Claude, Cursor, etc.:

python
# Sample conversation
User: Should I accept this job offer?
Book of Answers: Follow the voice of your heart.

User: Will this project succeed?
Book of Answers: The risk is too high, proceed with caution.

User: Show my history
Book of Answers: Display the last 5 query records

**Official site: ** [https://github.com/liuyvan2025-art/answer-book-mcp](https://github.com/liuyvan2025-art/answer-book-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `art and culture`, `mcp`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `answer-book-mcp@latest`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/liuyvan-answer-book.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
