---
title: "prototype_assistant"
description: "An MCP tool that allows AI to perform prototyping directly based on HTML, enabling quick software prototype construction even without tools like Figma or Axure. Tool Capabilities: - Provides a navigat…"
---

# prototype_assistant

An MCP tool that allows AI to perform prototyping directly based on HTML, enabling quick software prototype construction even without tools like Figma or Axure. Tool Capabilities: - Provides a navigat…

An MCP tool that allows AI to perform prototyping directly based on HTML, enabling quick software prototype construction even without tools like Figma or Axure.

Tool Capabilities:

- Provides a navigation bar.
- Decouples markup from the prototype.
- Supports additional page annotations.

## AI Prompt Suggestions

Before prototyping:

> Requirements:

> Please follow the prototype tool specifications for design.

> Needs: abcd...

During use, if you want to display the prototype, simply enter:

> Show Prototype

Prototype display will start a background process, so **there's no need to input the command multiple times**, as it would start multiple instances.

To stop, you can enter:

> Stop Display

or

> Close Prototype

## Usage Guidelines

- Navigation Bar:
  - Hierarchy Definition: Corresponds one-to-one with the directory structure of the file system where the prototype is located.
  - Prototype Name: Derived from the `data-nav-name` data attribute value of the prototype page tag; if omitted, the filename is used.

- Function Injection: MCP-Prototype injects the following into each HTML page:
  - Tags, pay attention to the correctness of the "reference" path.
  - The `mcp-prototype-inject.js` file, used for displaying markers.

- Markers: Enhance the user's understanding of UI elements by setting the `data-marker` data attribute. This is optional. If the meaning of related UI elements is already very clear, it is not recommended to configure this.

Additional page annotations are used to express content that cannot be conveyed through the prototype pages, such as design philosophy, element drag-and-drop, precautions, etc. The format is markdown, and the filename should be in the form [prototype page filename].annotation.md.

For specific references, see the `src\mcp\tool\getSpec.ts` file.

Tech Stack
nodejs, SvelteKit, Vite, ts

**Official site: ** [https://github.com/llxxbb/mcp-prototype](https://github.com/llxxbb/mcp-prototype)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `developer tools`, `art and culture`, `原型`, `html`, `导航`, `标注`, `标记`, `附加说明`, `设计`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @llxxbb/mcp-prototype`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/llxxbb-prototype-assistant.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
