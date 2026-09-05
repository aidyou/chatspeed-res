---
title: "fdp_domain"
description: "A tool for querying domain-related data in network foundational data. This includes associated domains, domain rankings, domain web page data, and domain-related data from the Libra foundational data…"
---

# fdp_domain

A tool for querying domain-related data in network foundational data. This includes associated domains, domain rankings, domain web page data, and domain-related data from the Libra foundational data…

# Domain-Related Basic Data Query

## Introduction to X Lab
X Lab (XLab) is a team at Qianxin dedicated to large-scale network security research, threat analysis and tracing, and the construction of a large-scale, multi-dimensional security data platform. 
X Lab was one of the first teams in China to utilize large-scale data for security research, security applications, and threat intelligence production. They established the country's first PassiveDNS system, as well as leading foundational data systems for Netflow, Whois, certificates, IP addresses, and malicious samples.

## Domain-Related Basic Data
This toolset is for querying domain-related data within network foundational data. It includes co-occurring domains, domain rankings, domain webpage data, and domain-related data from the Libra basic data platform.

# Tools
1. codomain
   * Codomain, also known as co-occurring domains, refers to domains that appear alongside an FQDN before or after a request, i.e., a co-occurrence list.
   * Returns associated domains, domain labels, the number of times they co-occur with the queried domain, and descriptions of the associated domains.
2. float_fqdn
   * A ranking of domain popularity calculated based on PassiveDNS data.
   * Returns the calculation date, score, and rank based on the score. The score ranges from 0 to 10, with higher scores indicating greater domain popularity.
3. webdb
   * Queries web content associated with a domain.
   * Returns relevant web content, including the title, page content, HTTP response codes, and tags for the page.
4. libra
   * Libra is a domain analysis system by Qianxin's X Lab, which correlates domain-related cybersecurity data: PassiveDNS data, whois data, certificate data, web data, and associated sandbox sample data. Based on these correlated data, it can determine the basic status of the domain.
   * Returns domain-related PassiveDNS data, whois data, certificate data, web data, and sandbox sample data.

# Installation and Usage

## Notes
The current toolset is a **trial version** for basic security data queries. In high-concurrency scenarios, the backend will limit the frequency of network access.

For high-frequency use cases, please use the official version.

## MCP Service Link
The link to Qianxin X Lab's remote MCP service is `https://fdp.qianxin.com/mcp/v1/domain/`

## Official Version Installation Instructions
1. The official version provides a streamable HTTP access method.
2. When using the tools, you need to provide the `fdp-access` and `fdp-secret` HTTP headers.
   * To obtain access credentials, please contact Qianxin X Lab.
3. When writing agent code, include `fdp-access` and `fdp-secret` in the HTTP headers when calling the MCP tool. Here’s an example using smolagents:
   python
   from smolagents import ToolCollection
   from smolagents.agents import ToolCallingAgent
   from smolagents.models import OpenAIServerModel

   def main():
       with ToolCollection.from_mcp(
           {
               "url": "https://fdp.qianxin.com/mcp/v1/domain/",
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
           agent.run("Query the related domains of www.example.com, and judge the possible business of the queried domain based on the data of the related domains.")

   if __name__ == "__main__":
       main()
   
4. If using this on Claude Desktop, you can use the `mcp-remote` library for proxy forwarding. During the forwarding process, configure the HTTP headers as follows:
   json
   {
       "mcpServers": {
           "fdp_domain": {
               "command": "npx",
               "args": [
                   "-y",
                   "mcp-remote@latest",
                   "https://fdp.qianxin.com/mcp/v1/domain/",
                   "--header",
                   "fdp-access:xxxx",
                   "--header",
                   "fdp-secret:yyyy"
               ],
           }
       }
   }Sure, please provide the Chinese technical document that you would like to be translated.

**Official site: ** [https://blog.xlab.qianxin.com/](https://blog.xlab.qianxin.com/)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `communication`, `data`
- Tags: `communication`, `developer tools`, `research and data`, `codomain`, `data analysis`, `network security`, `网络安全`, `威胁情报`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y mcp-remote@latest https://fdp.qianxin.com/mcp/v1/domain/`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/dongkitchen-fdp-domain.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
