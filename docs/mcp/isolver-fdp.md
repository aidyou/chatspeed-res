---
title: "fdp-mcp-server"
description: "A toolset provided by Qi'anxin XLab for querying basic cybersecurity data, including information about domains, IPs, and samples. The toolset supports local operation or remote access via URL and requ…"
---

# fdp-mcp-server

A toolset provided by Qi'anxin XLab for querying basic cybersecurity data, including information about domains, IPs, and samples. The toolset supports local operation or remote access via URL and requ…

fdp-mcp-server

> English version: [README.md](https://github.com/qax-xlab/fdp-mcp-server/blob/HEAD/README.md).

MCP tools for basic cybersecurity data provided by Qi'anxin XLab.

# About XLab
XLab is a team at Qi'anxin dedicated to large-scale network security research, threat analysis and tracing, and the construction of large-scale multi-dimensional security data platforms.
XLab was one of the earliest teams in China to use large-scale data for security research, security applications, and threat intelligence production. It built the first PassiveDNS system in China, as well as several industry-leading foundational data systems for Netflow, Whois, certificates, IPs, and malware samples.

# Tool Categories
fdp-mcp-server provides different kinds of tools. Depending on your needs, you can load different tool types by choosing different URLs.

Currently available tools:
1. **Basic cybersecurity data query**: `https://fdp.qianxin.com/mcp/v1/basic/mcp/`. Includes:
    * **flint rrset**: query Resource Record Sets (RRset) for a specific domain and record type
    * **flint rdata**: reverse-query the rrset data of DNS responses
    * **whois history**: query the registration history of a domain or IP
    * **certdb domain**: query domain certificate information by domain
    * **ioc**: query the XLab IOC database
2. **Domain-related basic data query**: `https://fdp.qianxin.com/mcp/v1/domain/mcp/`. Includes:
    * **codomain**: companion domains of a domain and their tag data
    * **float_fqdn**: domain popularity ranking computed from PassiveDNS data
    * **webdb**: query web content associated with a domain
    * **libra**: query data from Qi'anxin XLab's domain analysis system
3. **IP-related basic data query**: `https://fdp.qianxin.com/mcp/v1/ip/mcp/`. Includes:
    * **ip_geo**: query IPv4 geographic location, ASN, IP owner, and other information
4. **Sample-related basic data query**: `https://fdp.qianxin.com/mcp/v1/sample/mcp/`. Includes:
    * **sandbox**: query sample network behavior summary information

# How to Run
## Notes
1. This application is a proxy that converts calls to remote MCP tools into local Stdio-style operation. Therefore, it can be run locally or by directly accessing the remote MCP tool URL.
2. The remote MCP server URL currently only supports the Streamable HTTP access method.
3. The current toolset is the **trial version** of basic security data queries. Under high concurrency, the backend will throttle network access frequency. For high-frequency scenarios, use the official version.
4. For the official version, access the corresponding tool URL directly. You need to provide the two HTTP headers `fdp-access` and `fdp-secret`.
    * To obtain access credentials, contact Qi'anxin XLab.
5. All examples below use the **basic cybersecurity data query** toolset.

## Trial Version Usage
### Run the code locally
1. Clone the code from the repository
2. Run with uv and configure Claude Desktop:
```json
    {
        "mcpServers": {
            "fdp-mcp-server": {
                "command": "uv",
                "args": [
                    "run",
                    "--project",
                    "/PATH/TO/fdp-mcp-server",
                    "fdp-mcp-server",
                    "--url",
                    "https://fdp.qianxin.com/mcp/v1/basic/mcp/"
                ]
            }
        }
    }
```

### Run with a Docker image
1. Clone the code from the repository
2. Build the Docker image: `docker build . fdp-mcp-server:vxx.xx.xx`
3. Configure Claude Desktop
```json
    {
        "mcpServers": {
            "fdp-mcp-server": {
                "command": "docker",
                "args": [
                    "run",
                    "-i",
                    "--rm",
                    "fdp-mcp-server:vxx.xx.xx"
                ]
            }
        }
    }
```

### Run the PyPI package locally
Use uvx and configure Claude Desktop:
```json
{
    "mcpServers": {
        "fdp-mcp-server": {
            "command": "uvx",
            "args": [
                "fdp-mcp-server",
                "--url",
                "https://fdp.qianxin.com/mcp/v1/basic/mcp/"
            ]
        }
    }
}
```

## Official Version Usage
To call the fdp-mcp-server tools from an agent application, you can configure the remote MCP server URL directly on the client and call the tools, providing the two HTTP headers `fdp-access` and `fdp-secret`.
1. When writing agent code, add `fdp-access` and `fdp-secret` to the HTTP headers when connecting to the MCP tools. Using smolagents as an example:
```python
    from smolagents import ToolCollection
    from smolagents.agents import ToolCallingAgent
    from smolagents.models import OpenAIServerModel

    def main():
        with ToolCollection.from_mcp(
            {
                "url": "https://fdp.qianxin.com/mcp/v1/domain/mcp/",
                "transport": "streamable-http",
                "headers": {
                    "fdp-access": "xxxx",
                    "fdp-secret": "yyyy",
                },
            },
            trust_remote_code=True,
        ) as tools:
            agent = ToolCallingAgent(
                tools=[*tools.tools],
                model=OpenAIServerModel(
                    model_id="YOUR-LLM-MODEL-ID",
                    api_base="YOUR-LLM-MODEL-API-URL",
                    api_key="YOUR-LLM-MODEL-API-KEY",
                ),
            )
            agent.run("Query the associated domains of www.example.com, and make a judgment about the possible business of the queried domain based on the associated domain data.")

    if __name__ == "__main__":
        main()
```
2. If you are using Claude Desktop, you can use the `mcp-remote` library for proxy forwarding and configure the HTTP headers during forwarding:
```json
    {
        "mcpServers": {
            "fdp_domain": {
                "command": "npx",
                "args": [
                    "-y",
                    "mcp-remote@latest",
                    "https://fdp.qianxin.com/mcp/v1/domain/mcp/",
                    "--header",
                    "fdp-access:xxxx"
                    "--header",
                    "fdp-secret:yyyy"
                ],
            }
        }
    }
```

**Official site: ** [https://github.com/qax-xlab/fdp-mcp-server](https://github.com/qax-xlab/fdp-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `research and data`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uv`
- Args: `run --project /PATH/TO/fdp-mcp-server fdp-mcp-server --url https://fdp.qianxin.com/mcp/v1/basic/mcp/`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/isolver-fdp.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
