---
title: "Tongxiao"
description: "\"Tongxiao\" is a real-time search engine developed by Alibaba Cloud's information query service for large model applications. It retrieves data from publicly available web domains, vertical domain know…"
---

# Tongxiao

"Tongxiao" is a real-time search engine developed by Alibaba Cloud's information query service for large model applications. It retrieves data from publicly available web domains, vertical domain know…

"Tongxiao" is a real-time search engine developed by Alibaba Cloud's information query service for large model applications. It retrieves data from publicly available web domains, vertical domain knowledge bases, and various ecosystem data sources to meet the real-time Q&A data needs of large models.

# Key Features
- *Real-time*: Offers real-time search capabilities by integrating multiple information sources, providing the latest information and data for large models.
- *Accuracy*: Enhances search precision and reduces the workload of model tuning through methods like query rewriting, search condition optimization, summary enhancement, and result ranking.
- *Diversity*: Integrates multiple vertical domain data sources to offer a more comprehensive and personalized search experience, meeting diverse information needs.
- *High Quality*: Combines searches with high-quality industry knowledge bases, providing original search text and processing results (such as removing commercial content, compliance checks, and Markdown format presentation) to deliver highly credible and complete structured query results.

# Application Scenarios
- *Intelligent Customer Service*: Provides real-time knowledge base and Q&A capabilities for intelligent customer service robots, enhancing service efficiency and user experience.
- *Smart Assistant*: Offers real-time information and Q&A services for applications like smart voice assistants and intelligent search engines to enhance user experience and application value.
- *Content Creation*: Supplies real-time materials and inspiration for content creators like news media and social media, improving content creation efficiency and quality.
- *Data Analysis*: Provides real-time data support for applications such as market research and public opinion monitoring to enhance analysis efficiency and insights.

# How to use the "Tongxiao" MCP service
1. Activate Tongxiao API key
    - Activate [AliCloud IQS](https://help.aliyun.com/document_detail/2870227.html?spm=a2c4g.11186623.help-menu-2837261.d_1.adfe3350nzdbvw)
    - Go to the [Console](https://ipaas.console.aliyun.com/api-key) to activate apikey
2. Complete the MCP service configuration.

```
{
  "mcpServers": {
    "tongxiao-common-search": {
      "command": "npx",
      "args": ["-y", "@tongxiao/common-search-mcp-server"],
      "env": {
        "TONGXIAO_API_KEY": "Tongxiao apikey"
      }
    }
  }
}
```

3. For more information, refer to the [Documentation](https://help.aliyun.com/document_detail/2881063.html?spm=a2c4g.11186623.help-menu-2837261.d_3_1.4be16dd4aG7QLH)

**Official site: ** [https://www.npmjs.com/package/@tongxiao/common-search-mcp-server](https://www.npmjs.com/package/@tongxiao/common-search-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `search`
- Tags: `search`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @tongxiao/common-search-mcp-server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/aliyun-tongxiao.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
