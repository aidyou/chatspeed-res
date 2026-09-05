---
title: "12306-mcp"
description: "A 12306 ticket search server based on the Model Context Protocol (MCP). The server provides a simple API interface that allows users to search for 12306 tickets."
---

# 12306-mcp

A 12306 ticket search server based on the Model Context Protocol (MCP). The server provides a simple API interface that allows users to search for 12306 tickets.

# 
12306-mcp

[![](/mcp-assets/8cfea57fe4719c70863f9befc43e677b.svg)](https://github.com/Joooook)
[![](/mcp-assets/ce110b7037df2e4b88c9448a33b493a2.svg)](https://space.bilibili.com/3546386788255839)
![](/mcp-assets/96ffefbbfecc39ee03d1721d869ccee7.svg)
![](/mcp-assets/359abbb9d66235e1cdeda1302553d105.svg)
![](/mcp-assets/05585de86f37e025c044e88e2f7adf72.svg)
![](/mcp-assets/15cf1d71dd338c329dde81052ed36c85.svg)

A 12306 ticket search server based on the Model Context Protocol (MCP). The server provides a simple API interface that allows users to search for 12306 tickets.

## 
🚩Features

 

| Feature Description                    | Status   |
|----------------------------------------|----------|
| Query 12306 ticket information         | ✅ Completed |
| Filter train information               | ✅ Completed |
| Overstation query                      | ✅ Completed |
| Transfer query                         | ✅ Completed |
| Other interfaces, welcome to suggest features | 🚧 Planned |

 
   width=800px/>

 
  

## 
⚙️Installation

~~~bash
git clone https://github.com/Joooook/12306-mcp.git
npm i
~~~

## 
▶️Quick Start

### CLI-stdio
~~~bash
npx -y 12306-mcp
~~~

### CLI-http
~~~bash
npx -y 12306-mcp --port [port_number]
~~~

### MCP server configuration

~~~json
{
    "mcpServers": {
        "12306-mcp": {
            "command": "npx",
            "args": [
                "-y",
                "12306-mcp"
            ]
        }
    }
}

~~~

### Docker-stdio
~~~bash
docker build . -t 12306-mcp
docker run --rm -it 12306-mcp npx 12306-mcp
~~~

### Docker-http
~~~bash
docker build . -t 12306-mcp
docker run -p [your_port]:8080 -d 12306-mcp npx 12306-mcp --port 8080
~~~

## 
📚Documentation

- [Detailed Service Principle](https://github.com/Joooook/12306-mcp/blob/HEAD/docs/principle.md)  Explanation of the working principle of the 12306-MCP service
- [Architecture Diagram](https://github.com/Joooook/12306-mcp/blob/HEAD/docs/architecture.md)  Architecture diagram of the 12306-MCP service
   ![12306-MCP Service Architecture Diagram](/mcp-assets/988e65867be3fab84b3ccebc94ff4831.png)

## 
👉️Reference

- [modelcontextprotocol/modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol)
- [modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk)

## 
💭Murmurs

This project is for learning purposes only. Updates are welcome.

## 
🎫Badges

 

  

[![MseeP.ai Security Assessment Badge](/mcp-assets/9fe1de54ede043ff29b14fd59df7c35a.png)](https://mseep.ai/app/joooook-12306-mcp)

## 
☕️Donate

Buy me a cup of milk tea.

**Official site: ** [https://github.com/Joooook/12306-mcp](https://github.com/Joooook/12306-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `search`
- Tags: `travel and transportation`, `search`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y 12306-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/joooook-12306.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
