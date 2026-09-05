---
title: "通晓"
description: "通晓是阿里云信息查询服务为大模型应用打造的实时搜索引擎，通过网络公开域、垂域知识库以及多种生态数据源检索，满足大模型实时问答的数据需求。"
---

# 通晓

通晓是阿里云信息查询服务为大模型应用打造的实时搜索引擎，通过网络公开域、垂域知识库以及多种生态数据源检索，满足大模型实时问答的数据需求。

通晓 是阿里云信息查询服务为大模型应用打造的实时搜索引擎，通过网络公开域、垂域知识库以及多种生态数据源检索，满足大模型实时问答的数据需求。

# 通晓 MCP 服务的关键特性
- *实时*：集成多个信息源的实时搜索功能，为大模型提供最新的信息和数据。
- *准确性*：通过Query改写、搜索条件优化、摘要增强、结果精排等方法，提高搜索精准度，降低模型调优工作量。
- *多样性*：集成多个垂域数据源，提供更全面、个性化的搜索体验，满足多样化信息需求。
- *高质量*：结合高质量的行业知识库进行搜索，提供搜索原文，并对结果进行处理（如去除商业化内容、合规性检查和Markdown格式呈现），以提供高可信度和高完整度的结构化查询结果。

# 应用场景
- *智能客服*： 为智能客服机器人提供实时知识库和问答能力，提升客服效率和用户体验。
- *智能助手*： 为智能语音助手、智能搜索引擎等应用提供实时信息和问答服务，增强用户体验和应用价值。
- *内容创作*： 为新闻媒体、自媒体等内容创作者提供实时素材和灵感，提升内容创作效率和质量。
- *数据分析*： 为市场调研、舆情监测等数据分析应用提供实时数据支持，提升分析效率和洞察力。

# 如何使用 ‘通晓’ MCP 服务？
1. 开通通晓 apikey
    - 开通 [阿里云信息查询服务](https://help.aliyun.com/document_detail/2870227.html?spm=a2c4g.11186623.help-menu-2837261.d_1.adfe3350nzdbvw)
    - 前往 [控制台](https://ipaas.console.aliyun.com/api-key) 开通 apikey
2. 完成 mcp 服务配置

```
{
  "mcpServers": {
    "tongxiao-common-search": {
      "command": "npx",
      "args": ["-y", "@tongxiao/common-search-mcp-server"],
      "env": {
        "TONGXIAO_API_KEY": "通晓 apikey"
      }
    }
  }
}
```

3. 更多信息参考[文档](https://help.aliyun.com/document_detail/2881063.html?spm=a2c4g.11186623.help-menu-2837261.d_3_1.4be16dd4aG7QLH)

**官方网站：** [https://www.npmjs.com/package/@tongxiao/common-search-mcp-server](https://www.npmjs.com/package/@tongxiao/common-search-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`
- 标签：`search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @tongxiao/common-search-mcp-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/aliyun-tongxiao.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
