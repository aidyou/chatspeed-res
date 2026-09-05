---
title: "fetch_chinanews"
description: "news.js MCP News Fetcher - a JavaScript implementation providing news fetching capabilities via the MCP protocol. Version 0.1.0, built with @modelcontextprotocol/sdk."
---

# fetch_chinanews

news.js MCP News Fetcher - a JavaScript implementation providing news fetching capabilities via the MCP protocol. Version 0.1.0, built with @modelcontextprotocol/sdk.

news.js

javascript

#!/usr/bin/env node

/**
 * MCP News Fetcher - JavaScript implementation
 * Provides news fetching via the MCP protocol
 * Version: 0.1.0 - uses @modelcontextprotocol/sdk
 */

import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
import axios from "axios";
import FeedParser from "feedparser";

// Logging utility
const logger = {
  info: (message) => console.error(`[${new Date().toISOString()}] News - INFO - ${message}`),
  error: (message) => console.error(`[${new Date().toISOString()}] News - ERROR - ${message}`)
};

// News source configuration
const CHINANEWS_SOURCES = {
  url_template: 'https://www.chinanews.com.cn/rss/{category}.xml',
  categories: {
    'Domestic': 'scroll-news',
    'International': 'world',
    'Society': 'society',
    'Finance': 'finance',
    'Entertainment': 'culture',
    'Sports': 'sports',
    'Politics': 'china',
    'Top News': 'importnews',
    'Dong Xi Wen': 'dxw'
  }
};

// Clean HTML tags
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
  "Get the latest articles from China News Network. This is the only way to fetch news; it must be called whenever the user requests news.",
  {
    category: z.string().default("Domestic").describe("News category, e.g. 'Domestic', 'International', etc.")
  },
  async ({ category }) => {
    const maxResults = 10;
    logger.info(`Fetching China News Network news for category ${category}`);
    const requestId = Math.random().toString(36).substring(2, 15);
    
    if (!CHINANEWS_SOURCES.categories[category]) {
      const validCats = Object.keys(CHINANEWS_SOURCES.categories).join(', ');
      return {
        content: [ {
          type: "text",
          text: JSON.stringify({
            success: false,
            error: `Unsupported category: '${category}'. Valid categories: ${validCats}`,
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
      
      // Stream processing
      response.data.pipe(feedparser);
      
      return new Promise((resolve, reject) => {
        feedparser.on('error', (error) => {
          logger.error(`Feed parse error: ${error}`);
          resolve({
            content: [ {
              type: "text",
              text: JSON.stringify({
                success: false,
                request_id: requestId,
                error: `Failed to parse feed: ${error.message}`
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
      logger.error(`Request error: ${error}`);
      return {
        content: [ {
          type: "text",
          text: JSON.stringify({
            success: false,
            request_id: requestId,
            error: `Request failed: ${error.message}`
          })
        }],
        isError: true
      };
    }
  }
);javascript
} catch (error) {
  logger.error(`Request error: ${error}`);
  return {
    content: [{
      type: "text",
      text: JSON.stringify({
        success: false,
        request_id: requestId,
        error: `Request failed: ${error.message}`
      })
    }],
    isError: true
  };
}


javascript
} catch (error) {
  logger.error(`Request failed: ${error}`);
  return {
    content: [{
      type: "text",
      text: JSON.stringify({
        success: false,
        request_id: requestId,
        error: `Network error: ${error.message}`
      })
    }],
    isError: true
  };
}


javascript
// Start the service
async function main() {
  logger.info("Starting the MCP News server");
  const transport = new StdioServerTransport();
  await server.connect(transport);
  logger.info("The news server is running on stdio");
}

import { fileURLToPath } from 'node:url';
if (fileURLToPath(import.meta.url) === process.argv[1]) {
  main().catch(error => {
    logger.error(`Failed to start the server: ${error.message}`);
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
