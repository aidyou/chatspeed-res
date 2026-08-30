---
title: "域名相关基础数据查询"
description: "网络基础数据中和域名相关数据的查询工具。包括伴生域名、域名排名、域名网页数据、Libra基础数据平台的域名关联数据。"
---

# 域名相关基础数据查询

网络基础数据中和域名相关数据的查询工具。包括伴生域名、域名排名、域名网页数据、Libra基础数据平台的域名关联数据。

# 域名相关基础数据查询


## X实验室介绍
X实验室（XLab）是奇安信公司致力于大网安全研究、威胁分析溯源和大规模多维度安全数据平台建设的团队。
X实验室是国内最早利用大规模数据进行安全研究、安全应用和威胁情报生产的团队，建立了国内首个PassiveDNS系统，以及多个业内领先的 Netflow、Whois、证书、IP 和恶意样本等基础数据系统。

## 域名相关基础数据
网络基础数据中和域名相关数据的查询工具。包括伴生域名、域名排名、域名网页数据、Libra基础数据平台的域名关联数据。


# 工具
1. codomain
	* codomain，称作伴生域名，是指与 fqdn 一起在请求前后出现的域名，亦即共现列表。
	* 返回关联的域名、域名标签、和查询域名共同出现次数、关联域名的说明
2. float_fqdn
	* 基于PassiveDNS数据计算得到的域名流行度的排名。
	* 返回计算日期、计算得分、根据分数的排名。分数取值范围从0到10，分数越高表示域名流行度越高。
3. webdb
	* 查询域名关联的网页内容
	* 返回网页相关内容，包括标题、页面内容、HTTP请求的响应码等，同时也包含这个页面的标签。
4. libra
	* Libra是一个奇安信X实验室对针对域名的分析系统，其关联了和域名相关的网络安全的数据：PassiveDNS数据、whois数据、证书数据、网页数据、关联沙箱样本数据等等。根据这些关联的数据可以对这个域名的基本状态做判定。
	* 返回域名相关的PassiveDNS数据、whois数据、证书数据、网页数据、沙箱样本数据等等。


# 安装使用

## 说明
当前工具集是基础安全数据查询的**体验版**，高并发情况下后端会限制网络访问频率。

在高频场景下，请使用正式版。


## MCP服务链接
奇安信X实验室远端MCP服务的链接是`https://fdp.qianxin.com/mcp/v1/domain/`


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
            agent.run("查询www.example.com的关联域名，并给根据关联域名的数据对查询的域名可能的业务做一个判断。")


    if __name__ == "__main__":
        main()

```
4. 如果是使用在claude desktop上，可以利用`mcp-remote`库进行代理转发，在转发过程配置http请求头，配置说明：
```json
	{
	    "mcpServers": {
	        "fdp_domain": {
	            "command": "npx",
	            "args": [
	            	"-y",
	                "mcp-remote@latest",
	                "https://fdp.qianxin.com/mcp/v1/domain/",
	                "--header",
	                "fdp-access:xxxx"
	                "--header",
	                "fdp-secret:yyyy"
	            ],
	        }
	    }
	}
```

**官方网站：** [https://blog.xlab.qianxin.com/](https://blog.xlab.qianxin.com/)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`communication`, `data`
- 标签：`communication`, `developer tools`, `research and data`, `codomain`, `data analysis`, `network security`, `网络安全`, `威胁情报`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y mcp-remote@latest https://fdp.qianxin.com/mcp/v1/domain/`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/dongkitchen-fdp-domain.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
