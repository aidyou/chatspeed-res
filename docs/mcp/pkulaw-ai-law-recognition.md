---
title: "北大法宝法条识别—法律MCP"
description: "自动从文本中识别并提取法律条文，例如在合同、案件描述或法律文书中，精准定位涉及的具体法律条文（如“《民法典》第585条”），并将文本中的法律问题与对应法条内容关联，提取法规名称的服务。"
---

# 北大法宝法条识别—法律MCP

自动从文本中识别并提取法律条文，例如在合同、案件描述或法律文书中，精准定位涉及的具体法律条文（如“《民法典》第585条”），并将文本中的法律问题与对应法条内容关联，提取法规名称的服务。

# 项目描述
北大法宝法条识别MCP是一个动态的、实时的分析引擎，实现自动从文本中识别并提取法律条文，接受输入文本，运用模型推理和词典精准匹配，实时识别出其中提及的法律名称和具体条文（款、项），并进行标准化验证和推荐。

使用场景： 
1、从文本段落中提取法规名称和条款，例如在合同、案件描述或法律文书中，精准定位涉及的具体法律条文（如“《民法典》第585条”） 
2、将提取的法规名称与法律数据库中的标准名称及条款，进行校验匹配

# 要求
- requires-python = ">=3.10"
- mcp>=1.0.0

# 安装
- pip install mcp_server_law_recognition

# 使用方法
## 示例
    from mcp import ClientSession, StdioServerParameters, types
    from mcp.client.stdio import stdio_client
    server_params = StdioServerParameters(
        command="python",  # 可执行文件
        args=["-m","mcp_server_law_recognition"],  # 可选命令行参数
        env={
            "pkulaw_api_key": "da9629867ee841518***********"
        }  # 可选环境变量
    ) 
    
    async def run():
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(
                read, write
            ) as session:
                # 初始化连接
                await session.initialize()

            tools = await session.list_tools()
            print('tools:',tools)
            result = await session.call_tool("get_law_recognition", arguments={"text": "根据《民法典》第一千二百六十条规定，该法自2021年1月1日起施行，同时废止了《中华人民共和国婚姻法》、《中华人民共和国继承法》、《中华人民共和国民法通则》..."})
            print('result:',result)

    if __name__ == "__main__":
        import asyncio
    
        asyncio.run(run())

# 返回结果
- Text: 模型识别用的原始文本中的名称
- Original: pkulaw 数据库中的标准法规名称
- Full-text: pkulaw 数据库中的法规内容
- source: Pkulaw 网址

# 联系我们
- 申请 APIKEY: fxtj@chinalawinfo.com

**官方网站：** [https://pypi.org/project/mcp-server-law-recognition](https://pypi.org/project/mcp-server-law-recognition)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`python`
- 参数：`-m mcp_server_law_recognition`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/pkulaw-ai-law-recognition.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
