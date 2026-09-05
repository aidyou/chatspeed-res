---
title: "google-news-trends"
description: "一个MCP服务器，从Google News和Google Trends的RSS端点抽取数据，可选地使用LLM/NLP进行提炼，并输出结构化的结果。"
---

# google-news-trends

一个MCP服务器，从Google News和Google Trends的RSS端点抽取数据，可选地使用LLM/NLP进行提炼，并输出结构化的结果。

# Google News Trends MCP

一个从Google News和Google Trends RSS端点抓取数据的MCP服务器，可选地使用LLM/NLP进行提炼，并输出结构化结果。

## 特性

- 根据关键词、位置、主题爬取Google News RSS源的文章
- 从Google News获取头条新闻
- 根据地理输入从Google Trends捕获热门搜索词
- 插入LLM/NLP流水线以浓缩文章内容并提取关键概念

## 安装

### 使用uv/uvx（推荐）

当使用[`uv`](https://docs.astral.sh/uv/)时不需要特定安装。我们将使用[`uvx`](https://docs.astral.sh/uv/guides/tools/)直接运行*google-news-trends-mcp*。

### 使用PIP

```bash

pip install google-news-trends-mcp

```
安装后，可以使用以下命令作为脚本运行：

```bash

python -m google_news_trends_mcp

```
## 配置

### 为Claude.app配置

在您的Claude设置中添加：

使用uvx

```json

{

  "mcpServers": {

    "google-news-trends": {

      "command": "uvx",

      "args": ["google-news-trends-mcp@latest"]

    }

  }

}

```

使用pip安装

```json

{

  "mcpServers": {

    "google-news-trends": {

      "command": "python",

      "args": ["-m", "google_news_trends_mcp"]

    }

  }

}

```

### 为VS Code配置

使用uvx

```json

{

  "mcp": {

    "servers": {

      "google-news-trends": {

        "command": "uvx",

        "args": ["google-news-trends-mcp@latest"]

      }

    }

  }

}

```

使用pip安装

```json

{

  "mcp": {

    "servers": {

      "google-news-trends": {

        "command": "python",

        "args": ["-m", "google_news_trends_mcp"]

      }

    }

  }

}

```

## 工具

可用的MCP工具有：

| 工具名称                | 描述                                                        |
|--------------------------|--------------------------------------------------------------------|
| **get_news_by_keyword**  | 使用特定关键词搜索新闻。                           |
| **get_news_by_location** | 检索与某个特定位置相关的新闻。                   |
| **get_news_by_topic**    | 根据选定的主题获取新闻。                                  |
| **get_top_news**         | 从Google News获取头条新闻故事。                       |
| **get_trending_keywords**| 返回指定地点的Google Trends热门关键词。|

所有与新闻相关的工具都有选项可以通过LLM采样（如果支持）或NLP来总结文章文本。

## 命令行界面
所有工具都可以通过`uv`从命令行访问

```bash

uv run google-news-trends

Usage: google-news-trends [OPTIONS] COMMAND [ARGS]...

  Find and download news articles using Google News.

Options:

  --help  Show this message and exit.

Commands:

  keyword   Find articles by keyword using Google News.

  location  Find articles by location using Google News.

  top       Get top news stories from Google News.

  topic     Find articles by topic using Google News.

  trending  Returns google trends for a specific geo location.

```
## 调试

```bash

npx @modelcontextprotocol/inspector uvx google-news-trends-mcp

```
要在本地安装的项目内运行

```bash

cd path/to/google/news/tends/mcp

npx @modelcontextprotocol/inspector uv run google-news-trends-mcp

```
## 测试

```bash

cd path/to/google/news/tends/mcp

python -m pytest

```

**官方网站：** [https://github.com/jmanek/google-news-trends-mcp](https://github.com/jmanek/google-news-trends-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`research and data`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`google-news-trends-mcp@latest`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/jiayiz-google-news-trends.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
