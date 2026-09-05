---
title: "fetch_chinanews"
description: "news.js javascript !/usr/bin/env node / MCP News Fetcher - JavaScript 实现 通过MCP协议提供新闻抓取功能 版本: 0.1.0 - 使用@modelcontextprotocol/sdk / import { McpServer } from \"@modelcontextprotocol/sdk/server/mcp.js\"…"
---

# fetch_chinanews

news.js javascript !/usr/bin/env node / MCP News Fetcher - JavaScript 实现 通过MCP协议提供新闻抓取功能 版本: 0.1.0 - 使用@modelcontextprotocol/sdk / import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js"…

news.js

javascript

#!/usr/bin/env node

/**
 * MCP News Fetcher - JavaScript 实现
 * 通过MCP协议提供新闻抓取功能
 * 版本: 0.1.0 - 使用@modelcontextprotocol/sdk
 */

import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
import axios from "axios";
import FeedParser from "feedparser";

// 日志工具
const logger = {
  info: (message) => console.error(`[${new Date().toISOString()}] News - INFO - ${message}`),
  error: (message) => console.error(`[${new Date().toISOString()}] News - ERROR - ${message}`)
};

// 新闻源配置
const CHINANEWS_SOURCES = {
  url_template: 'https://www.chinanews.com.cn/rss/{category}.xml',
  categories: {
    '国内': 'scroll-news',
    '国际': 'world',
    '社会': 'society',
    '财经': 'finance',
    '娱乐': 'culture',
    '体育': 'sports',
    '时政': 'china',
    '要闻': 'importnews',
    '东西问': 'dxw'
  }
};

// 清理HTML标签
function cleanHtml(rawHtml) {
  if (!rawHtml) return "";
  return rawHtml.replace(/]+>|&[a-zA-Z0-9]+;/g, '').trim();
}

const server = new McpServer({
  name: "NewsFetcher",
  version: "0.1.0",
});

server.tool(
  "fetch_chinanews",
  "从中国新闻网获取最新文章。这是获取新闻的唯一方法。当用户请求新闻时必须调用。",
  {
    category: z.string().default("国内").describe("新闻分类，例如：'国内', '国际'等")
  },
  async ({ category }) => {
    const maxResults = 10;
    logger.info(`正在为分类 ${category} 获取中国新闻网新闻`);
    const requestId = Math.random().toString(36).substring(2, 15);
    
    if (!CHINANEWS_SOURCES.categories[category]) {
      const validCats = Object.keys(CHINANEWS_SOURCES.categories).join(', ');
      return {
        content: [ {
          type: "text",
          text: JSON.stringify({
            success: false,
            error: `不支持的分类: '${category}'。有效的分类: ${validCats}`,
            request_id: requestId
          })
        }],
        isError: true
      };
    }
    
    const categoryCode = CHINANEWS_SOURCES.categories[category];
    const url = CHINANEWS_SOURCES.url_template.replace('{category}', categoryCode);
    
    try {
      const response = await axios({
        method: 'get',
        url: url,
        headers: {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        },
        responseType: 'stream'
      });
      
      const feedparser = new FeedParser();
      const newsItems = [];
      
      // 流式处理
      response.data.pipe(feedparser);
      
      return new Promise((resolve, reject) => {
        feedparser.on('error', (error) => {
          logger.error(`Feed解析错误: ${error}`);
          resolve({
            content: [ {
              type: "text",
              text: JSON.stringify({
                success: false,
                request_id: requestId,
                error: `解析Feed失败: ${error.message}`
              })
            }],
            isError: true
          });
        });
        
        feedparser.on('readable', function() {
          let item;
          while ((item = this.read()) && newsItems.length  {
          resolve({
            content: [ {
              type: "text",
              text: JSON.stringify({
                success: true,
                request_id: requestId,
                results: newsItems,
                count: newsItems.length
              })
            }]
          });
        });
      });
    } catch (error) {
      logger.error(`请求错误: ${error}`);
      return {
        content: [ {
          type: "text",
          text: JSON.stringify({
            success: false,
            request_id: requestId,
            error: `请求失败: ${error.message}`
          })
        }],
        isError: true
      };
    }
  }
);javascript
} catch (error) {
  logger.error(`请求错误: ${error}`);
  return {
    content: [{
      type: "text",
      text: JSON.stringify({
        success: false,
        request_id: requestId,
        error: `请求失败: ${error.message}`
      })
    }],
    isError: true
  };
}


javascript
} catch (error) {
  logger.error(`请求失败: ${error}`);
  return {
    content: [{
      type: "text",
      text: JSON.stringify({
        success: false,
        request_id: requestId,
        error: `网络错误: ${error.message}`
      })
    }],
    isError: true
  };
}


javascript
// 启动服务
async function main() {
  logger.info("正在启动MCP News服务器");
  const transport = new StdioServerTransport();
  await server.connect(transport);
  logger.info("新闻服务器正在stdio上运行");
}

import { fileURLToPath } from 'node:url';
if (fileURLToPath(import.meta.url) === process.argv[1]) {
  main().catch(error => {
    logger.error(`服务器启动失败: ${error.message}`);
    process.exit(1);
  });
}

export default server;

**Official site: ** [https://www.chinanews.com.cn](https://www.chinanews.com.cn)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `search`
- Tags: `search`, `other`

## MCP Configuration

- Transport: `stdio`
- Command: `node`
- Args: `./news.js`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/andyilin-fetch-chinanews.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
