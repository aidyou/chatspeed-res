---
title: "新闻标题情感分析"
description: "分析来自美国主要出版物的新闻标题的情感，使用标准和自然语言日期输入，从而洞察公众情感趋势。"
---

# 新闻标题情感分析

分析来自美国主要出版物的新闻标题的情感，使用标准和自然语言日期输入，从而洞察公众情感趋势。

# 标题情绪分析 MCP 服务器

一个模型上下文协议服务器，用于分析美国主要出版物新闻标题的情绪。该服务器提供了基于日期的标准接口和自然语言日期解析功能，以便更易于使用。

## 功能

- 每次请求最多分析100个标题
- 美国主要新闻来源的标题均衡分布
- 情绪评分范围为0-10（0=最负面，10=最正面）
- 自然语言日期解析（例如，“昨天”，“上周五”）
- 详细的来源分布信息
- 结果中包含示例标题

## 前提条件

- Node.js v16或更高版本
- NewsAPI密钥（在https://newsapi.org获取）

## 安装

1. 克隆仓库：
```bash
git clone https://github.com/fred-em/headline-vibes.git
cd headline-vibes
```

2. 安装依赖项：
```bash
npm install
```

3. 构建服务器：
```bash
npm run build
```

4. 在MCP设置文件中配置您的NewsAPI密钥：
```json
{
  "mcpServers": {
    "headline-vibes": {
      "command": "node",
      "args": ["/path/to/headline-vibes/build/index.mjs"],
      "env": {
        "NEWS_API_KEY": "your-api-key-here"
      },
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

## 可用工具

### analyze_headlines
使用自然语言日期输入或特定日期来分析情绪。

示例用法：
```typescript
// Using natural language
{
  "name": "analyze_headlines",
  "arguments": {
    "input": "yesterday"
  }
}

// Or using specific dates
{
  "name": "analyze_headlines",
  "arguments": {
    "input": "2025-02-11"
  }
}
```

输入示例：
- "last Friday"
- "3 days ago"
- "March 10th"
- "two weeks ago"
- "2025-02-11"（也支持YYYY-MM-DD格式）

## 响应格式

工具返回结果的格式如下：
```json
{
  "score": "6.50",              // Normalized sentiment score (0-10)
  "synopsis": "Overall positive sentiment in today's headlines",
  "headlines_analyzed": 100,    // Number of headlines analyzed
  "sources_analyzed": 12,       // Number of unique sources
  "source_distribution": {      // Distribution of headlines by source
    "Reuters": 10,
    "Associated Press": 8,
    "CNN": 9,
    // ... etc
  },
  "sample_headlines": [         // Up to 5 sample headlines
    "Example headline 1",
    "Example headline 2",
    // ... etc
  ]
}
```

## 新闻来源

服务器从以下美国主要新闻来源获取标题：
- 美联社
- 路透社
- CNN
- Fox News
- NBC News
- ABC News
- 华尔街日报
- 华盛顿邮报
- USA Today
- 彭博社
- Business Insider
- Time

## 错误处理

对于常见问题，服务器提供了清晰的错误消息：
- 无效的日期格式
- 无法解析的自然语言查询
- 指定日期未找到任何标题
- 来自NewsAPI的API错误

## 开发

在开发过程中以监视模式运行服务器：
```bash
npm run watch
```

## 许可证

MIT

**官方网站：** [https://github.com/fred-em/headline-vibes](https://github.com/fred-em/headline-vibes)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`research and data`, `search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`/path/to/headline-vibes/build/index.mjs`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/fred-em-headline-vibes.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
