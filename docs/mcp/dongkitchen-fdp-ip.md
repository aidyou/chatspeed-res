---
title: "fdp_ip"
description: "Network foundational data and IP-related data query tools. Currently, it includes companion IP geolocation queries."
---

# fdp_ip

Network foundational data and IP-related data query tools. Currently, it includes companion IP geolocation queries.

# IP-related Basic Data Query

## About XLab
XLab is a team at Qi'anxin dedicated to large-scale network security research, threat analysis and tracing, and the construction of large-scale multi-dimensional security data platforms.
XLab was one of the earliest teams in China to use large-scale data for security research, security applications, and threat intelligence production. It built the first PassiveDNS system in China, as well as several industry-leading foundational data systems for Netflow, Whois, certificates, IPs, and malware samples.

## IP-related Basic Data
Query tools for IP-related data in the basic network data set. Currently includes IP geolocation queries.

# Tools
1. ip geo
   * Queries IPv4 geolocation, ASN, IP owner, and other information

# Installation and Usage

## Notes
The current toolset is the **trial version** of basic security data queries. Under high concurrency, the backend will throttle network access frequency.

For high-frequency scenarios, use the official version.

## MCP service link
Qi'anxin XLab's remote MCP service link is `https://fdp.qianxin.com/mcp/v1/ip/`

## Official version installation
1. The official version provides streamable HTTP access.
2. When using the tools, you need to provide the two HTTP headers `fdp-access` and `fdp-secret`.
   * To obtain access credentials, contact Qi'anxin XLab.
3. When writing agent code, add `fdp-access` and `fdp-secret` to the HTTP headers when connecting to the MCP tools. Using smolagents as an example:

```python
    from smolagents import ToolCollection
    from smolagents.agents import ToolCallingAgent
    from smolagents.models import OpenAIServerModel


    def main():
        with ToolCollection.from_mcp(
            {
                "url": "https://fdp.qianxin.com/mcp/v1/ip/",
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
            agent.run("Query the information of this IP: 8.8.8.8")


    if __name__ == "__main__":
        main()

```
4. If you are using Claude Desktop, you can use the `mcp-remote` library for proxy forwarding and configure the HTTP headers during forwarding:

```json
    {
        "mcpServers": {
            "fdp_ip": {
                "command": "npx",
                "args": [
                    "-y",
                    "mcp-remote@latest",
                    "https://fdp.qianxin.com/mcp/v1/ip/",
                    "--header",
                    "fdp-access:xxxx"
                    "--header",
                    "fdp-secret:yyyy"
                ],
            }
        }
    }
```

**Official site: ** [https://blog.xlab.qianxin-inc.cn](https://blog.xlab.qianxin-inc.cn)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `communication`, `data`
- Tags: `communication`, `developer tools`, `research and data`, `ip`, `网络安全`, `威胁情报`, `network security`, `data analysis`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y mcp-remote@latest https://fdp.qianxin.com/mcp/v1/ip/`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/dongkitchen-fdp-ip.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
