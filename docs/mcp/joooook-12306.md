---
title: "12306-MCP车票查询工具"
description: "基于Model Context Protocol (MCP) 的12306购票搜索服务器。提供了简单的API接口，允许大模型利用接口搜索12306购票信息。"
---

# 12306-MCP车票查询工具

基于Model Context Protocol (MCP) 的12306购票搜索服务器。提供了简单的API接口，允许大模型利用接口搜索12306购票信息。

# 
12306-mcp

[![](/mcp-assets/8cfea57fe4719c70863f9befc43e677b.svg)](https://github.com/Joooook)
[![](/mcp-assets/ce110b7037df2e4b88c9448a33b493a2.svg)](https://space.bilibili.com/3546386788255839)
![](/mcp-assets/96ffefbbfecc39ee03d1721d869ccee7.svg)
![](/mcp-assets/359abbb9d66235e1cdeda1302553d105.svg)
![](/mcp-assets/05585de86f37e025c044e88e2f7adf72.svg)
![](/mcp-assets/15cf1d71dd338c329dde81052ed36c85.svg)

A 12306 ticket search server based on the Model Context Protocol (MCP). The server provides a simple API interface that allows users to search for 12306 tickets.

基于 Model Context Protocol (MCP) 的12306购票搜索服务器。提供了简单的API接口，允许大模型利用接口搜索12306购票信息。

## 
🚩Features

 

| 功能描述                         | 状态     |
|------------------------------|--------|
| 查询12306购票信息              | ✅ 已完成  |
| 过滤列车信息                   | ✅ 已完成  |
| 过站查询                      | ✅ 已完成 |
| 中转查询                      | ✅ 已完成 |
| 其余接口，欢迎提feature         | 🚧 计划内 |

 
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
npx -y 12306-mcp --port [端口号]
~~~

### MCP sever configuration

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

- [服务原理详解](https://github.com/Joooook/12306-mcp/blob/HEAD/docs/principle.md)  12306-MCP服务的工作原理
- [架构图](https://github.com/Joooook/12306-mcp/blob/HEAD/docs/architecture.md)  12306-MCP服务的架构图
   ![12306-MCP 服务架构图](/mcp-assets/988e65867be3fab84b3ccebc94ff4831.png)

## 
👉️Reference

- [modelcontextprotocol/modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol)
- [modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk)

## 
💭Murmurs

本项目仅用于学习，欢迎催更。

## 
🎫Badges

 

  

[![MseeP.ai Security Assessment Badge](/mcp-assets/9fe1de54ede043ff29b14fd59df7c35a.png)](https://mseep.ai/app/joooook-12306-mcp)

## 
☕️Donate

请我喝杯奶茶吧。

**官方网站：** [https://github.com/Joooook/12306-mcp](https://github.com/Joooook/12306-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`
- 标签：`travel and transportation`, `search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y 12306-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/joooook-12306.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
