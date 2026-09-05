---
title: "fdp_basic"
description: "Basic network data, including passive DNS resolution data, registration information for domains and IPs, website certificates, and queries to the IOC (Indicators of Compromise) library. The data sourc…"
---

# fdp_basic

Basic network data, including passive DNS resolution data, registration information for domains and IPs, website certificates, and queries to the IOC (Indicators of Compromise) library. The data sourc…

# Basic Network Security Data Query

## About XLab
XLab is a team at Qi'anxin dedicated to large-scale network security research, threat analysis and tracing, and the construction of large-scale multi-dimensional security data platforms.
XLab was one of the earliest teams in China to use large-scale data for security research, security applications, and threat intelligence production. It built the first PassiveDNS system in China, as well as several industry-leading foundational data systems for Netflow, Whois, certificates, IPs, and malware samples.

## Basic Network Security Data
Basic network data, including passive DNS resolution data, registration information for domains and IPs, website certificates, and IOC library queries.

# Tools
1. flint rrset
   * flint rrset data in PassiveDNS
   * flint rrset is used to query Resource Record Sets (RRset) for a specific domain and record type
   * You can query flint rrset records of subdomains using the form *.example.com
   * Returns fqdn, DNS access count, first record time, last record time, DNS rtype, DNS rdata
2. flint rdata
   * flint rdata data in PassiveDNS
   * flint rdata is used to reverse-query the rrset records of DNS responses
   * Returns fqdn, DNS access count, first record time, last record time, DNS rtype, DNS rdata
3. whois history
   * Queries the registration history of a domain or IP
   * Returns the registrant, registrant email, registrar, registry, registration time, current domain status, etc.
4. certdb domain
   * Queries domain certificate information by domain
   * Returns certificate validity period, issue time, fingerprint, subject info, etc.
5. ioc
   * Queries the XLab IOC database
   * Returns entity tag information

# Installation and Usage

## Notes
The current toolset is the **trial version** of basic security data queries. Under high concurrency, the backend will throttle network access frequency.

For high-frequency scenarios, use the official version.

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
                "url": "https://fdp.qianxin.com/mcp/v1/basic/",
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
                    api_key="YOUR-LLM-MODEL-APK-KEY",
                ),
            )
            agent.run("Query the registration information of www.example.com and give a brief summary.")


    if __name__ == "__main__":
        main()

```
4. If you are using Claude Desktop, you can use the `mcp-remote` library for proxy forwarding and configure the HTTP headers during forwarding:
```json
    {
        "mcpServers": {
            "fdp_basic": {
                "command": "npx",
                "args": [
                    "-y",
                    "mcp-remote@latest",
                    "https://fdp.qianxin.com/mcp/v1/basic/",
                    "--header",
                    "fdp-access:xxxx"
                    "--header",
                    "fdp-secret:yyyy"
                ],
            }
        }
    }
```

**Official site: ** [https://blog.xlab.qianxin.com/](https://blog.xlab.qianxin.com/)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `memory`, `data`
- Tags: `research and data`, `developer tools`, `knowledge and memory`, `网络安全`, `威胁情报`, `passivedns`, `dns`, `whois`, `certificate`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y mcp-remote@latest https://fdp.qianxin.com/mcp/v1/basic/`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/dongkitchen-fdp-basic.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
