---
title: "北大法宝法律智能检索MCP服务"
description: "这是北大法宝提供的用于法律法规智能检索的MCP服务。使用文本嵌入，进行语义检索。"
---

# 北大法宝法律智能检索MCP服务

这是北大法宝提供的用于法律法规智能检索的MCP服务。使用文本嵌入，进行语义检索。

# 北大法宝法律智能检索MCP服务

这是[北大法宝](https://www.pkulaw.com/)提供的用于法律法规智能检索的MCP服务。

标签：搜索工具

北大法宝——让法律更智能。


## 工具

法律法规智能检索MCP服务提供了如下工具：
- `get_article`: 通过包含法规名称和法条条号的文本，获取法条内容和对应的法规全称
- `search_article`: 通过对文本进行语义检索，获取匹配的法条内容和对应的法规名称


## MCP客户端使用

当前页面右侧的【服务配置信息】，选择【Streamable HTTP】或【sse】，【鉴权类型】选择“无鉴权”，选择【有效期】，点击【连接】，生成服务配置。

在MCP客户端（比如CherryStudio）里，使用生成的配置添加法律法规智能检索MCP服务。

在大模型对话的工具栏，首先启用智能检索MCP服务，然后输入类似以下的内容，调用MCP服务完成回答：
- 请给出的《民事诉讼法》第7条的具体内容，不要做任何修改。
- 法律中关于危险货物的定义是什么？

如果MCP客户端没有调用MCP服务，在输入开头加入“请使用工具回答”提示使用：
- 请使用工具回答，法律中关于危险货物的定义是什么？

## 联系

有问题请联系: .

**官方网站：** [https://pypi.org/project/pkulaw-mcp-proxy/@latest](https://pypi.org/project/pkulaw-mcp-proxy/@latest)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`
- 标签：`search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`pkulaw-mcp-proxy --name pkulaw-mcp-law-search --backend-url https://apim-gateway.pkulaw.com/mcp-law-search-service --backend-token c5d14fd3-1c46-3bba-9fa7-64be73cc97ad`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/pkulaw-pkulaw-law-search.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
