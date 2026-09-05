---
title: "热闻社媒服务"
description: "一个模型上下文协议服务器，提供来自主要中文社交平台和新闻网站的实时热门话题。"
---

# 热闻社媒服务

一个模型上下文协议服务器，提供来自主要中文社交平台和新闻网站的实时热门话题。

# HotNews MCP Server

一个提供来自中国主要社交平台和新闻网站实时热点话题的模型上下文协议（MCP）服务器。

## 特性

- 来自9个中国主要平台的实时热点
- 兼容MCP协议
- 与AI模型轻松集成
- 支持Markdown格式输出及可点击链接
- 热度指数支持（在可用的情况下）

## 支持的平台

1. 知乎热榜 (Zhihu Hot List)
2. 36氪热榜 (36Kr Hot List)
3. 百度热点 (Baidu Hot Discussion)
4. B站热榜 (Bilibili Hot List)
5. 微博热搜 (Weibo Hot Search)
6. 抖音热点 (Douyin Hot List)
7. 虎扑热榜 (Hupu Hot List)
8. 豆瓣热榜 (Douban Hot List)
9. IT新闻 (IT News)

> API来源，本项目使用`api.vvhan.com`服务来获取热点数据。

## 可用工具
- `get_hot_news`
  - `sources` - 必需参数：平台ID列表
- 使用示例：
  - `get_hot_news([3])` : 仅获取百度热点讨论
  - `get_hot_news([1,3,7])` : 获取知乎、百度和虎扑的热门榜单
  - `get_hot_news([1,2,3,4])` : 获取知乎、36氪、百度和B站的热门榜单

## 安装

### NPX

```json
{
  "mcpServers": {
    "mcp-server-hotnews": {
      "command": "npx",
      "args": [
        "-y",
        "@wopal/mcp-server-hotnews"
      ]
    }
  }
}
```

### Docker 
（Docker镜像尚未上传至Docker Hub，需要自行构建。）

```json
{
  "mcpServers": {
    "mcp-server-hotnews": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "wopal/mcp-server-hotnews"
      ]
    }
  }
}
```

## 开发

```bash
# Install dependencies
npm install

# Watch mode
npm run watch

# Build
npm run build

# Test URLs
npm run test:urls
```

Docker 构建:

```bash
docker build -t wopal/mcp-server-hotnews:latest -f Dockerfile .
```

## 许可证

此MCP服务器根据MIT许可证发布。这意味着您可以自由地使用、修改和分发该软件，但需遵守MIT许可证的条款和条件。更多详情，请参见项目仓库中的LICENSE文件。

**官方网站：** [https://github.com/wopal-cn/mcp-hotnews-server](https://github.com/wopal-cn/mcp-hotnews-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`
- 标签：`social media`, `search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @wopal/mcp-server-hotnews`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/wopal-cn-hotnews.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
