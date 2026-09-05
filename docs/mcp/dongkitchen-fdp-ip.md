---
title: "fdp_ip"
description: "Network foundational data and IP-related data query tools. Currently, it includes companion IP geolocation queries."
---

# fdp_ip

Network foundational data and IP-related data query tools. Currently, it includes companion IP geolocation queries.

# IP相关基础数据查询


## X实验室介绍
X实验室（XLab）是奇安信公司致力于大网安全研究、威胁分析溯源和大规模多维度安全数据平台建设的团队。
X实验室是国内最早利用大规模数据进行安全研究、安全应用和威胁情报生产的团队，建立了国内首个PassiveDNS系统，以及多个业内领先的 Netflow、Whois、证书、IP 和恶意样本等基础数据系统。

## IP相关基础数据
网络基础数据中和IP相关数据的查询工具。目前包括伴IP地理位置查询。


# 工具
1. ip geo
	* 查询ipv4地理位置、ASN、IP所有者等信息


# 安装使用

## 说明
当前工具集是基础安全数据查询的**体验版**，高并发情况下后端会限制网络访问频率。

在高频场景下，请使用正式版。


## MCP服务链接
奇安信X实验室远端MCP服务的链接是`https://fdp.qianxin.com/mcp/v1/ip/`


## 正式版安装说明
1. 正式版本提供了streamable http的访问方式。
2. 在使用工具时，需要提供fdp-access和fdp-secret这两个http请求头
	* 获取访问凭据，请联系奇安信X实验室
3. 在编写agents代码时，在编写调用连接mcp工具时将fdp-access和fdp-secret增加到http请求头中。以smolagents为例进行说明：
	
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
            agent.run("查询这个ip的信息：8.8.8.8")


    if __name__ == "__main__":
        main()

```
4. 如果是使用在claude desktop上，可以利用`mcp-remote`库进行代理转发，在转发过程配置http请求头，配置说明：
	
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
