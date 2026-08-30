---
title: "网络基础数据查询"
description: "网络基础数据，包括passivedns解析数据、域名和IP的注册信息、网站证书、IOC库的查询。\n数据来源于奇安信X实验室被动收集的大网安全研究、威胁分析溯源和大规模多维度安全数据平台。"
---

# 网络基础数据查询

网络基础数据，包括passivedns解析数据、域名和IP的注册信息、网站证书、IOC库的查询。
数据来源于奇安信X实验室被动收集的大网安全研究、威胁分析溯源和大规模多维度安全数据平台。

# 网络基础安全数据查询


## X实验室介绍
X实验室（XLab）是奇安信公司致力于大网安全研究、威胁分析溯源和大规模多维度安全数据平台建设的团队。
X实验室是国内最早利用大规模数据进行安全研究、安全应用和威胁情报生产的团队，建立了国内首个PassiveDNS系统，以及多个业内领先的 Netflow、Whois、证书、IP 和恶意样本等基础数据系统。

## 网络基础安全数据
网络基础数据，包括passivedns解析数据、域名和IP的注册信息、网站证书、IOC库的查询。


# 工具
1. flint rrset
	* PassiveDNS 中的 flint rrset 数据
	* flint rrset 用于查询特定域名和记录类型的资源记录集（Resource Record Set，简称 RRset）
	* 可以使用 *.example.com 的形势查询子域名的 flint rrset 记录
	* 返回 fqdn, DNS access count, first record time, last record time, DNS rtype, DNS rdata
2. flint rdata
	* PassiveDNS中的flint rdata数据
	* flint rdata是用来反向查询DNS响应的rrset记录的数据
	* 返回 fqdn, DNS access count, first record time, last record time, DNS rtype, DNS rdata
3. whois history
	* 查询域名或IP的注册历史信息
	* 返回注册用户、注册邮箱、注册商、注册局、注册时间、当前域名状态等等
4. certdb domain
	* 通过域名查询域名证书信息
	* 返回证书有效期、颁发时间、指纹、主题信息等等
5. ioc
	* 查询X实验室IOC数据库
	* 返回实体的标签信息


# 安装使用

## 说明
当前工具集是基础安全数据查询的_**体验版**_，高并发情况下后端会限制网络访问频率。

在高频场景下，请使用正式版。


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
            agent.run("查询www.example.com的注册信息，并给做一个简短的总结。")


    if __name__ == "__main__":
        main()

```
4. 如果是使用在claude desktop上，可以利用`mcp-remote`库进行代理转发，在转发过程配置http请求头，配置说明：
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

**官方网站：** [https://blog.xlab.qianxin.com/](https://blog.xlab.qianxin.com/)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`memory`, `data`
- 标签：`research and data`, `developer tools`, `knowledge and memory`, `网络安全`, `威胁情报`, `passivedns`, `dns`, `whois`, `certificate`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y mcp-remote@latest https://fdp.qianxin.com/mcp/v1/basic/`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/dongkitchen-fdp-basic.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
