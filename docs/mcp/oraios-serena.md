---
title: "serena"
description: "A fully featured coding agent that uses symbolic operations (enabled by language servers) and works well even in large code bases. Essentially a free to use alternative to Cursor and Windsurf Agents…"
---

# serena

A fully featured coding agent that uses symbolic operations (enabled by language servers) and works well even in large code bases. Essentially a free to use alternative to Cursor and Windsurf Agents…

style="width:500px">
   style="width:500px">

* :rocket: Serena is a powerful **coding agent toolkit** capable of turning an LLM into a fully-featured agent that works **directly on your codebase**.
* :wrench: Serena provides essential **semantic code retrieval and editing tools** that are akin to an IDE's capabilities, extracting code entities at the symbol level and exploiting relational structure.
* :free: Serena is **free & open-source**, enhancing the capabilities of LLMs you already have access to free of charge.

### Demonstration

Here is a demonstration of Serena implementing a small feature for itself (a better log GUI) with Claude Desktop.
Note how Serena's tools enable Claude to find and edit the right symbols.

https://github.com/user-attachments/assets/6eaa9aa1-610d-4723-a2d6-bf1e487ba753

### LLM Integration

Serena provides the necessary [tools](#full-list-of-tools) for coding workflows, but an LLM is required to do the actual work,
orchestrating tool use.

Serena can be integrated with an LLM in several ways:
 * by using the **model context protocol (MCP)**.  
   Serena provides an MCP server which integrates with 
     * Claude Desktop, 
     * IDEs like VSCode, Cursor or IntelliJ,
     * Extensions like Cline or Roo Code
     * Goose (for a nice CLI experience)
     * and many others, including [the ChatGPT app soon](https://x.com/OpenAIDevs/status/1904957755829481737)
 * by using **Agno – the model-agnostic agent framework**.  
   Serena's Agno-based agent allows you to turn virtually any LLM into a coding agent, whether it's provided by Google, OpenAI or Anthropic (with a paid API key)
   or a free model provided by Ollama, Together or Anyscale.
 * by incorporating Serena's tools into an agent framework of your choice.  
   Serena's tool implementation is decoupled from the framework-specific code and can thus easily be adapted to any agent framework.

### Programming Language Support & Semantic Analysis Capabilities

Serena's semantic code analysis capabilities build on **language servers** using the widely implemented
language server protocol (LSP). The LSP provides a set of versatile code querying
and editing functionalities based on symbolic understanding of the code. 
Equipped with these capabilities, Serena discovers and edits code just like a seasoned developer 
making use of an IDE's capabilities would.
Serena can efficiently find the right context and do the right thing even in very large and
complex projects! So not only is it free and open-source, it frequently achieves better results 
than existing solutions that charge a premium.

Language servers provide support for a wide range of programming languages.
With Serena, we provide 
 * direct, out-of-the-box support for:
     * Python 
     * Java (_Note_: startup is slow, initial startup especially so)
     * TypeScript
 * indirect support (may require some code changes/manual installation) for:
     * Ruby (untested)
     * Go (untested)
     * C# (untested)
     * Rust (untested)
     * Kotlin (untested)
     * Dart (untested)
     * C/C++ (untested)
     
   These languages are supported by the language server library [multilspy](https://github.com/microsoft/multilspy), which Serena uses under the hood.
   But we did not explicitly test whether the support for these languages actually works.
       
Further languages can, in principle, easily be supported by providing a shallow adapter for a new language server
implementation.

## Table of Contents

- [What Can I Use Serena For?](#what-can-i-use-serena-for)
- [Free Coding Agents with Serena](#free-coding-agents-with-serena)
- [Quick Start](#quick-start)
  * [Setup and Configuration](#setup-and-configuration)
  * [MCP Server (Claude Desktop)](#mcp-server-claude-desktop)
  * [Other MCP Clients - Cline, Roo-Code, Cursor, Windsurf etc.](#other-mcp-clients---cline-roo-code-cursor-windsurf-etc)
  * [Goose](#goose)
  * [Agno Agent](#agno-agent)
  * [Other Agent Frameworks](#other-agent-frameworks)
- [Serena's Tools and Configuration](#serenas-tools-and-configuration)
- [Comparison with Other Coding Agents](#comparison-with-other-coding-agents)
  * [Subscription-Based Coding Agents](#subscription-based-coding-agents)
  * [API-Based Coding Agents](#api-based-coding-agents)
  * [Other MCP-Based Coding Agents](#other-mcp-based-coding-agents)
- [Onboarding and Memories](#onboarding-and-memories)
- [Combination with Other MCP Servers](#combination-with-other-mcp-servers)
- [Recommendations on Using Serena](#recommendations-on-using-serena)
  * [Which Model to Choose?](#which-model-to-choose)
  * [Onboarding](#onboarding)
  * [Before Editing Code](#before-editing-code)
  * [Potential Issues in Code Editing](#potential-issues-in-code-editing)
  * [Running Out of Context](#running-out-of-context)
  * [Controlling Tool Execution](#controlling-tool-execution)
  * [Structuring Your Codebase](#structuring-your-codebase)
  * [Logging, Linting, and Testing](#logging-linting-and-testing)
  * [General Advice](#general-advice)
- [Troubleshooting](#troubleshooting)
  * [Serena Logging](#serena-logging)
- [Acknowledgements](#acknowledgements)
- [Customizing Serena](#customizing-serena)
- [Full List of Tools](#full-list-of-tools)

## What Can I Use Serena For?

You can use Serena for any coding tasks – whether it is focussed on analysis, planning, 
designing new components or refactoring existing ones.
Since Serena's tools allow an LLM to close the cognitive perception-action loop, 
agents based on Serena can autonomously carry out coding tasks from start to finish – 
from the initial analysis to the implementation, testing and, finally, the version
control system commit.

Serena can read, write and execute code, read logs and the terminal output.
While we do not necessarily encourage it, "vibe coding" is certainly possible, and if you 
want to almost feel like "the code no longer exists",
you may find Serena even more adequate for vibing than an agent inside an IDE
(since you will have a separate GUI that really lets you forget).

## Free Coding Agents with Serena

Even the free tier of Anthropic's Claude has support for MCP Servers, so you can use Serena with Claude for free.
Presumably, the same will soon be possible with ChatGPT Desktop once support for MCP servers is added.  
Through Agno, you furthermore have the option to use Serena with a free/open-weights model.

Serena is [Oraios AI](https://oraios-ai.de/)'s contribution to the developer community.  
We use it ourselves on a regular basis.

We got tired of having to pay multiple
IDE-based subscriptions (such as Windsurf or Cursor) that forced us to keep purchasing tokens on top of the chat subscription costs we already had.
The substantial API costs incurred by tools like Claude Code, Cline, Aider and other API-based tools are similarly unattractive.
We thus built Serena with the prospect of being able to cancel most other subscriptions.

## Quick Start

Serena can be used in various ways, below you will find instructions for selected integrations.

- If you just want to turn Claude into a free-to-use coding agent, we recommend using Serena through Claude Desktop.
- If you want to use Gemini or any other model and you want a GUI experience, you should use [Agno](#agno-agent). On macOS you can also use the GUI of [goose](#goose).
- If you prefer using Serena through a CLI, you can use [goose](#goose). There again almost any model is possible.
- If you want to use Serena integrated in your IDE, see the section on [other MCP clients](#other-mcp-clients---cline-roo-code-cursor-windsurf-etc).

### Setup and Configuration

1. Install `uv` (instructions [here](https://docs.astral.sh/uv/getting-started/installation/))
2. Clone the repository to `/path/to/serena`.
3. Copy `serena_config.template.yml` to `serena_config.yml` and adjust settings.
4. Copy `myproject.template.yml` to `myproject.yml` and adjust the settings specific to your project.
   (Add one such file for each project you want Serena to work on.)
5. If you want Serena to dynamically switch between projects, add the list of all project files
   created in the previous step to the `projects` list in `serena_config.yml`.

> ⚠️ **Note:** Serena is under active development. We are continuously adding features, improving stability and the UX.
> As a result, configuration may change in a breaking manner. If you have an invalid configuration,
> the MCP server or Serena-based Agent may fail to start (investigate the MCP logs in the former case).
> Check the [changelog](https://github.com/oraios/serena/blob/HEAD/CHANGELOG.md)
> and the configuration templates when updating Serena, adapting your configurations accordingly.

After the initial setup, continue with one of the sections below, depending on how you
want to use Serena.

### MCP Server (Claude Desktop)

1. Create a configuration file for your project, say `myproject.yml` based on the template in myproject.template.yml.
2. Configure the MCP server in your client.  
   For [Claude Desktop](https://claude.ai/download) (available for Windows and macOS), go to File / Settings / Developer / MCP Servers / Edit Config,
   which will let you open the JSON file `claude_desktop_config.json`. Add the following (with adjusted paths) to enable Serena:

```json
   {
       "mcpServers": {
           "serena": {
               "command": "/abs/path/to/uv",
               "args": ["run", "--directory", "/abs/path/to/serena", "serena-mcp-server", "--project-file", "/abs/path/to/myproject.yml"]
           }
       }
   }
```
   
   :info: passing the project file is optional if you have set `enable_project_activation` in your configuration,
   as this setting will allow you to simply instruct Claude to activate the project you want to work on.

   If you are using paths containing backslashes for paths on Windows 
   (note that you can also just use forward slashes), be sure to escape them correctly (`\`).

That's it! Save the config and then restart Claude Desktop. 

Note: on Windows and macOS there are official Claude Desktop applications by Anthropic, for Linux there is an [open-source
community version](https://github.com/aaddrick/claude-desktop-debian).

⚠️ Be sure to fully quit the Claude Desktop application, as closing Claude will just minimize it to the system tray – at least on Windows.  

After restarting, you should see Serena's tools in your chat interface (notice the small hammer icon).

⚠️ Tool Names: Claude Desktop (and most MCP Clients) don't resolve the name of the server. So you shouldn't
say something like "use Serena's tools". Instead, you can instruct the LLM to use symbolic tools or to
use a particular tool by referring to its name. Moreover, if you use multiple MCP Servers, you might get
**tool name collisions** which lead to undefined behavior. For example, Serena is currently incompatible with the
[Filesystem MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) due to tool name
collisions.

ℹ️ Note that MCP servers which use stdio as a protocol are somewhat unusual as far as client/server architectures go, as the server
necessarily has to be started by the client in order for communication to take place via the server's standard input/output stream.
In other words, you do not need to start the server yourself. The client application (e.g. Claude Desktop) takes care of this and 
therefore needs to be configured with a launch command.

For more information on MCP servers with Claude Desktop, see [the official quick start guide](https://modelcontextprotocol.io/quickstart/user).

### Other MCP Clients - Cline, Roo-Code, Cursor, Windsurf etc.

Being an MCP Server, Serena can be included in any MCP Client. The same config as above,
maybe with small client-specific modifications should work. Most of the popular
existing coding assistants (IDE extensions or VSCode-like IDEs) accept connecting
to MCP Servers. Including Serena generally boosts their performance
by providing them tools for symbolic operations.

In this case, the billing for the usage continues to be controlled by the client of your choice
(unlike with the Claude Desktop client). But you may still want to use Serena through such an approach,
e.g., for one of the following reasons:

1. You are already using a coding assistant (say Cline or Cursor) and just want to make it more powerful.
2. You are on Linux and don't want to use the [community-created Claude Desktop](https://github.com/aaddrick/claude-desktop-debian)
3. You want tighter integration of Serena into your IDE and don't mind paying for that

The same considerations as in using Serena for Claude Desktop (in particular, tool name collisions) 
also apply here.

When used in an IDE or extension that has inbuilt AI interactions for coding 
(which is, really, all of them), Serena's full set of tools may lead to unwanted interactions with
the clients internal tools that you as the user may have no control over. This holds especially for the editing tools, which you may want to disable for this purpose.
As we are gaining more experience with Serena used within the various popular clients, we will collect and enhance best practices that enable a smooth experience.

### Goose

[goose](https://github.com/block/goose) is a standalone coding agent which has an integration for MCP servers and offers a CLI (and a GUI on macOS). Using goose is currently the simplest way of running Serena through a CLI with an LLM of your choice.

Follow the instructions [here](https://block.github.io/goose/docs/getting-started/installation/) to install it.

After that, use `goose configure` to add an extension. For adding Serena, choose the option `Command-line Extension`, name it `Serena` and add the following as command:

```
/abs/path/to/uv run --directory /abs/path/to/serena serena-mcp-server /optional/abs/path/to/project.yml
```

Since Serena can do all necessary editing and command operations, you should disable the `developer` extension that goose enables by default.
For that execute

```shell
goose configure
```
again, choose the option `Toggle Extensions`, and make sure Serena is enabled selected while `developer` is not.

That's it. Read through the configuration options of goose to see what you can do with it (which is a lot, like setting different levels of permissions for tool execution).

> Goose does not seem to always properly terminate python processes for MCP servers when a session ends. 
> You may want to disable the Serena GUI and/or to manually cleanup any running python processes after finishing your work
> with goose.

### Agno Agent

Agno is a model-agnostic agent framework that allows you to turn Serena into an agent 
(independent of the MCP technology) with a large number of underlying LLMs. Agno is currently
the simplest way of running Serena in a chat GUI with an LLM of your choice 
(unless you are using a Mac, then you might prefer goose, which requires almost no setup).

While Agno is not yet entirely stable, we chose it, because it comes with its own open-source UI, 
making it easy to directly use the agent using a chat interface.  With Agno, Serena is turned into an agent
(so no longer an MCP Server), so it can be used in programmatic ways (for example for benchmarking or within 
your application).

Here's how it works (see also [Agno's documentation](https://docs.agno.com/introduction/playground)):

1. Download the agent-ui code with npx
```shell
   npx create-agent-ui@latest
```
   or, alternatively, clone it manually:
```shell
   git clone https://github.com/agno-agi/agent-ui.git
   cd agent-ui 
   pnpm install 
   pnpm dev
```

2. Install serena with the optional requirements:
```shell
   # You can also only select agno,google or agno,anthropic instead of all-extras
   uv pip install --all-extras -r pyproject.toml -e .
```
   
3. Copy `.env.example` to `.env` and fill in the API keys for the provider(s) you
   intend to use.

5. Start the agno agent app with
```shell
   uv run python scripts/agno_agent.py
```
   By default, the script uses Claude as the model, but you can choose any model
   supported by Agno (which is essentially any existing model).

5. In a new terminal, start the agno UI with
```shell
   cd agent-ui 
   pnpm dev
```
   Connect the UI to the agent you started above and start chatting. You will have
   the same tools as in the MCP server version.

Here is a short demo of Serena performing a small analysis task with the newest Gemini model:

https://github.com/user-attachments/assets/ccfcb968-277d-4ca9-af7f-b84578858c62

⚠️ IMPORTANT: In contrast to the MCP server approach, tool execution in the Agno UI does
not ask for the user's permission. The shell tool is particularly critical, as it can perform arbitrary code execution. 
While we have never encountered any issues with
this in our testing with Claude, allowing this may not be entirely safe. 
You may choose to disable certain tools for your setup in your Serena project's
configuration file (`.yml`).

### Other Agent Frameworks

The Agno agent is particularly nice because of the Agno UI, but it is easy to incorporate Serena into any
agent framework (like [pydantic-ai](https://ai.pydantic.dev/), [langgraph](https://langchain-ai.github.io/langgraph/tutorials/introduction/) or others).

You just have to write an adapter of Serena's tools to the tools in the framework of your choice, like
it was done by us for agno in the [SerenaAgnoToolkit](https://github.com/oraios/serena/blob/HEAD/src/serena/agno.py).

## Serena's Tools and Configuration

Serena combines tools for semantic code retrieval with editing capabilities and shell execution.
Find the complete list of tools [below](#serenas-tools-and-configuration).

The use of all tools is generally recommended, as this allows Serena to provide the most value:
Only by executing shell commands (in particular, tests) can Serena identify and correct mistakes 
autonomously.

However, it should be noted that the `execute_shell_command` tool allows for arbitrary code execution. 
When using Serena as an MCP Server, clients will typically ask the user for permission 
before executing a tool, so as long as the user inspects execution parameters beforehand,
this should not be a problem.
However, if you have concerns, you can choose to disable certain commands in your project's 
.yml configuration file.
If you only want to use Serena purely for analyzing code and suggesting implementations
without modifying the codebase, you can enable read-only mode by setting `read_only: true` in your project configuration file. 
This will automatically disable all editing tools and prevent any modifications to your codebase while still 
allowing all analysis and exploration capabilities.

In general, be sure to back up your work and use a version control system in order to avoid
losing any work.

## Comparison with Other Coding Agents

To our knowledge, Serena is the first fully-featured coding agent where the
entire functionality
is available through an MCP server, thus not requiring API keys or
subscriptions.

### Subscription-Based Coding Agents

The most prominent subscription-based coding agents are parts of IDEs like
Windsurf, Cursor and VSCode.
Serena's functionality is similar to Cursor's Agent, Windsurf's Cascade or
VSCode's
upcoming [agent mode](https://code.visualstudio.com/blogs/2025/02/24/introducing-copilot-agent-mode).

Serena has the advantage of not requiring a subscription.
A potential disadvantage is that it 
is not directly integrated into an IDE, so the inspection of newly written code
is not as seamless.

More technical differences are:
* Serena is not bound to a specific IDE.
  Serena's MCP server can be used with any MCP client (including some IDEs), 
  and the Agno-based agent provides additional ways of applying its functionality.
* Serena is not bound to a specific large language model or API.
* Serena navigates and edits code using a language server, so it has a symbolic
  understanding of the code.
  IDE-based tools often use a R

**Official site: ** [https://github.com/oraios/serena](https://github.com/oraios/serena)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `developer tools`, `version control`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `/abs/path/to/uv`
- Args: `run --directory /abs/path/to/serena serena-mcp-server --project-file /abs/path/to/myproject.yml`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/oraios-serena.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
