---
title: "PromptX"
description: "PromptX provides professional roles, memory management, and knowledge systems for AI applications through the MCP protocol. With a single command, any AI client instantly becomes a professional."
---

# PromptX

PromptX provides professional roles, memory management, and knowledge systems for AI applications through the MCP protocol. With a single command, any AI client instantly becomes a professional.

PromptX - AI-Native Professional Capability Enhancement System

Through the MCP protocol, PromptX provides professional roles, memory management, and knowledge systems for AI applications. With a single line of command, any AI client instantly turns into a professional.

---

### What PromptX Does at a Glance

What can PromptX do? In short, it gives your AI assistant a "brain" and a "memory", and turns you into a creator of AI capabilities.

- **Professional role-playing**: expert roles across different domains, making AI answers more professional and deeper.
- **Long-term memory and knowledge base**: AI remembers key information and your preferences, providing coherent, personalized support across conversations and work.
- **AI role creation workshop**: turn your idea into a professional AI assistant **within 2 minutes** - a stunning leap from user to creator.
- **Easy integration**: enable these powerful features for dozens of mainstream AI apps (such as Claude, Cursor) with just one command.

### What You Get After Configuration

#### 1. Discover and activate professional roles
*Use `promptx_hello` to discover available roles, then `promptx_action` to activate one - your AI instantly becomes a domain expert.*

#### 2. Smart memory
*Use `promptx_remember` to save key information; the AI will proactively use that knowledge in later conversations.*

---

## Project Status

PromptX is currently in its **initial development stage**. We are actively refining features and fixing issues. Until we reach a stable release, you may encounter some usability issues or instability.

**We sincerely ask for your understanding and support!**

### Need Help?

If you run into any issues, please reach us through:

- **Submit an Issue**: [GitHub Issues](https://github.com/Deepractice/PromptX/issues) - describe the problem in detail; we will reply as soon as possible
- **Direct contact**: add the developer's WeChat `deepracticex` for immediate help
- **Email**: `sean@deepracticex.com` for technical support
- **Community group**: scan the QR code below to join our tech chat group

Your feedback is invaluable and helps us improve quality fast!

---

## One-Click Start: Configure in 30 Seconds

Open your config file and paste in the `promptx` configuration below. This is the simplest **zero-config mode** - PromptX handles everything automatically.

```json
{
  "mcpServers": {
    "promptx": {
      "command": "npx",
      "args": [
        "-y",
        "-f",
        "--registry",
        "https://registry.npmjs.org",
        "dpml-prompt@beta",
        "mcp-server"
      ]
    }
  }
}
```

**Configuration notes:**
- `command`: uses npx to run the promptx service
- `args`: startup arguments
  - `-y`: auto-confirm
  - `-f`: force cache refresh
  - `--registry`: specify the registry
  - `https://registry.npmjs.org`: use the official registry
  - `dpml-prompt@beta`: use the stable beta version
  - `mcp-server`: start the server

**That's it!** Save the file, restart your AI app, and PromptX is active.

> **Tip:** the config deliberately uses the official registry `registry.npmjs.org` to avoid install issues caused by non-official mirrors. If installation is slow, use a proxy to speed it up rather than switching mirrors.

**[Complete installation guide](https://github.com/Deepractice/PromptX/wiki/PromptX-MCP-Install)** - detailed configuration and troubleshooting for various clients

### Don't know what MCP is? [Check out the MCP kindergarten tutorial on Bilibili](https://www.bilibili.com/video/BV1HFd6YhErb)

All MCP-protocol AI clients can use PromptX, mainly including: **Claude Desktop**, **Cursor**, **Windsurf**, **Cline**, **Zed**, **Continue** and other mainstream AI coding tools, plus more apps joining all the time.

---

### How It Works

PromptX acts as a "professional capability middleware" between you and the AI app, communicating via the standard [MCP protocol](https://github.com/metacontroller/mcp).

When you call a `promptx_...` tool, the AI app sends the request to PromptX over MCP. The PromptX engine loads the appropriate professional role, retrieves relevant memories, and returns a professionally enhanced result to the AI app, which finally presents it to you.

---

**After configuration, your AI app automatically gets 6 professional tools:**
- `promptx_init`: **System initialization** - prepares the working environment automatically.
- `promptx_hello`: **Role discovery** - browse all available expert roles.
- `promptx_action`: **Role activation** - instantly become an expert in a given domain. **(includes Nvwa, the role-creation advisor)**
- `promptx_learn`: **Knowledge learning** - teach the AI specific knowledge or skills.
- `promptx_recall`: **Memory retrieval** - find historical info from the memory store.
- `promptx_remember`: **Experience saving** - store important info into long-term memory.

---

## Nvwa Creation Workshop - Let Everyone Be an AI Role Designer

#### From Idea to Reality in Just 2 Minutes

Have you ever thought: what if I could customize a professional AI assistant for a specific work scenario? **Nvwa turns that idea into reality.**

> "Every idea deserves its own AI assistant. Technical barriers should not limit the flight of creativity."

#### Core Value Transformation

- **Zero-barrier creation**: describe your needs in natural language - no complex tech required
- **Instant delivery**: from idea to usable role in about 2 minutes
- **Professional quality**: automatically generates professional AI roles that comply with DPML standards
- **Plug and play**: activate and use immediately after creation
- **A sense of ownership**: a brilliant leap from user to creator

#### Example Use Cases

| User Need | Nvwa Generates | Immediately Usable |
|---|---|---|
| "I need an AI assistant that understands Xiaohongshu marketing" | Xiaohongshu marketing expert role | `Activate Xiaohongshu marketing expert` |
| "I want a Python async programming expert" | Python async programming tutor role | `Activate Python async programming tutor` |
| "Give me a UI/UX design consultant" | UI/UX design expert role | `Activate UI/UX design expert` |
| "I need a data analyst assistant" | Data analysis expert role | `Activate data analysis expert` |

#### Experience Nvwa's Creativity - Create Your Own AI Assistant in 4 Steps

```bash
# 1. Activate the Nvwa role-creation advisor
"I want Nvwa to help me create a role"

# 2. Describe your needs (natural language is fine)
"I need a professional [domain] assistant, mainly for [specific scenario]"

# 3. Wait 2 minutes while Nvwa generates your professional role
# Nvwa creates the role file, registers it, and completes a quality check

# 4. Activate and use your own AI assistant right away
"Activate the role that was just created"
```

#### Nvwa's Design Philosophy

- **Boundless creation**: let anyone with an idea create AI assistants, breaking down technical barriers
- **Instant gratification**: meeting the digital age's demand for immediacy
- **Growth guidance**: not just tool use, but guiding users to understand the boundaries of AI capabilities
- **Ecosystem building**: every user-created role can inspire others

---

## Practice Case: Legacy Lands Library

### Project Overview

**Project name:** Legacy Lands Library
**Project URL:** https://github.com/LegacyLands/legacy-lands-library
**About:** legacy-lands-library is a developer tool library for modern Minecraft server plugin development. It aims to provide developers with cross-platform, production-ready infrastructure.

### Organization Info

**Organization:** Legacy Lands
**Website:** https://www.legacylands.cn/
**About:** Legacy Lands is an innovative team focused on building large-scale Minecraft civilization simulation experiences. Participating in the open-source community, it provides elegant, efficient, and reliable solutions for Minecraft server plugin development.

> ### Core Developer's Experience
> "The development experience with PromptX is truly different. Our team uses Claude Code with PromptX, and **one developer wrote more than 11,000 lines of high-quality Java code in just three days.**
>
> The value of this workflow showed fully in real development. PromptX solves many pain points of AI usage, consistently ensuring unified code style and quality, and greatly reducing the learning cost for new members. Best practices that previously required repeated communication and documentation inheritance can now be naturally woven into every generation of code."

### Related Resources

- **AI integration standard & practice guide:** https://github.com/LegacyLands/legacy-lands-library/blob/main/AI_CODE_STANDARDS_ZHCN.md

---

## Star Growth Trend

[![Star History Chart](/mcp-assets/7ff5ea12648cd650854ef8cf69c6f49e.svg)](https://star-history.com/#Deepractice/PromptX&Date)

---

### Contributing & Communication

We welcome any form of contribution and feedback!

- **Branch strategy** - branch management and release process
- **Release process** - version management and release docs

Scan the QR code to join the tech community group:

---

## License

[MIT License](https://github.com/Deepractice/PromptX/blob/HEAD/LICENSE) - making professional AI capabilities accessible to all

**Official site: ** [https://github.com/Deepractice/PromptX](https://github.com/Deepractice/PromptX)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `memory`, `communication`
- Tags: `developer tools`, `knowledge and memory`, `communication`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y -f --registry https://registry.npmjs.org dpml-prompt@beta mcp-server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/deepractice-ai-promptx.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
