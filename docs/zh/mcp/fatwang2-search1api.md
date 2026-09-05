---
title: "Search1API-MCP 搜索爬取服务器"
description: "一个使用Search1API提供搜索和爬取功能的模型上下文协议（MCP）服务器。"
---

# Search1API-MCP 搜索爬取服务器

一个使用Search1API提供搜索和爬取功能的模型上下文协议（MCP）服务器。

# Search1API MCP 服务器

[中文文档](https://github.com/fatwang2/search1api-mcp/blob/HEAD/README_zh.md)

一个使用 Search1API 提供搜索和爬取功能的模型上下文协议 (MCP) 服务器。

## 先决条件

- Node.js >= 18.0.0
- 有效的 Search1API API 密钥（请参阅下面的**设置指南**以了解如何获取和配置）

## 安装（独立/通用）

1. **克隆仓库：**
```bash
    git clone https://github.com/fatwang2/search1api-mcp.git
    cd search1api-mcp
```

2. **配置 API 密钥：** 在构建之前，您需要提供您的 Search1API 密钥。请参阅下面的**设置指南**部分，了解不同的方法（例如，使用 `.env` 文件或环境变量）。

3. **安装依赖并构建：**
```bash
    npm install
    npm run build
```
    *注意：如果使用项目的 `.env` 文件方法来配置 API 密钥，请确保在执行此步骤之前该文件已经存在。*

## 使用（独立/通用）

确保您的 API 密钥已配置（请参阅**设置指南**）。

启动服务器：
```bash
npm start
```

然后服务器将准备好接受来自 MCP 客户端的连接。

## 设置指南

### 1. 获取 Search1API 密钥

1. 在 [Search1API](https://www.search1api.com/) 注册
2. 从您的仪表板中获取您的 API 密钥。

### 2. 配置 API 密钥

您需要让服务器能够访问您的 API 密钥。请选择以下**一种**方法：

**方法 A：项目 `.env` 文件（推荐用于独立或 LibreChat）**

如果您正在与当前版本的 LibreChat 集成，则需要使用此方法（请参见下面的具体部分）。

1. 在 `search1api-mcp` 项目的根目录下创建一个名为 `.env` 的文件：
```bash
    # 在 search1api-mcp 目录中
    echo "SEARCH1API_KEY=your_api_key_here" > .env
```
2. 将 `your_api_key_here` 替换为您的实际密钥。
3. 确保在运行 `npm install && npm run build` 之前该文件已经存在。

**方法 B：环境变量（仅限独立）**

在启动服务器之前设置 `SEARCH1API_KEY` 环境变量。

```bash
export SEARCH1API_KEY="your_api_key_here"
npm start
```

**方法 C：MCP 客户端配置（高级）**

某些 MCP 客户端允许在其配置中直接指定环境变量。这对于像 Cursor、VS Code 扩展等客户端非常有用。

```json
{
  "mcpServers": {
    "search1api": {
      "command": "npx",
      "args": [
        "-y",
        "search1api-mcp"
      ],
      "env": {
        "SEARCH1API_KEY": "YOUR_SEARCH1API_KEY"
      }
    }
  }
}
```

**LibreChat 用户注意事项：** 由于 LibreChat 当前的限制，方法 A（项目 `.env` 文件）是**必需**的方法。请参阅下面的专用集成部分以获取完整说明。

## 与 LibreChat 集成（Docker）

本节详细介绍了通过 Docker 与 LibreChat 集成所需的步骤。

**概述：**

1. 将此服务器的仓库克隆到 LibreChat `docker-compose.yml` 可访问的位置。
2. 使用**项目 `.env` 文件方法**在此服务器目录内配置所需的 API 密钥。
3. 构建此服务器。
4. 通过编辑 `librechat.yaml` 告诉 LibreChat 如何运行此服务器。
5. 确保通过 Docker 卷绑定使构建的服务器代码在 LibreChat 容器内可用。
6. 重启 LibreChat。

**逐步操作：**

1.  **Clone the Repository:**
    Navigate to the directory on your host machine where you manage external services for LibreChat (this is often alongside your `docker-compose.yml`). A common location is a dedicated `mcp-server` directory.
```bash
    # Example: Navigate to where docker-compose.yml lives, then into mcp-server
    cd /path/to/your/librechat/setup/mcp-server
    git clone https://github.com/fatwang2/search1api-mcp.git
```

2.  **Navigate into the Server Directory:**
```bash
    cd search1api-mcp
```

3.  **Configure API Key (Project `.env` File Method - Required for LibreChat):**
```bash
    # Create the .env file
    echo "SEARCH1API_KEY=your_api_key_here" > .env
    # IMPORTANT: Replace 'your_api_key_here' with your actual Search1API key
```

4.  **Install Dependencies and Build:**
    This step compiles the server code into the `build` directory.
```bash
    npm install
    npm run build
```

5.  **Configure `librechat.yaml`:**
    Edit your main `librechat.yaml` file to tell LibreChat how to execute this MCP server. Add an entry under `mcp_servers`:
```yaml
    # In your main librechat.yaml
    mcp_servers:
      # You can add other MCP servers here too
      search1api:
        # Optional: Display name for the server in LibreChat UI
        # name: Search1API Tools

        # Command tells LibreChat to use 'node'
        command: node

        # Args specify the script for 'node' to run *inside the container*
        args:
          - /app/mcp-server/search1api-mcp/build/index.js
```
    *   The `args` path (`/app/...`) is the location *inside* the LibreChat API container where the built server will be accessed (thanks to the volume bind in the next step).

6.  **Configure Docker Volume Bind:**
    Edit your `docker-compose.yml` (or more likely, your `docker-compose.override.yml`) to map the `search1api-mcp` directory from your host machine into the LibreChat API container. Find the `volumes:` section for the `api:` service:
```yaml
    # In your docker-compose.yml or docker-compose.override.yml
    services:
      api:
        # ... other service config ...
        volumes:
          # ... other volumes likely exist here ...

          # Add this volume bind:
          - ./mcp-server/search1api-mcp:/app/mcp-server/search1api-mcp
```
    *   **Host Path (`./mcp-server/search1api-mcp`):** This is the path on your host machine *relative* to where your `docker-compose.yml` file is located. Adjust it if you cloned the repo elsewhere.
    *   **Container Path (`:/app/mcp-server/search1api-mcp`):** This is the path *inside* the container. It **must match** the directory structure used in the `librechat.yaml` `args` path.

7.  **Restart LibreChat:**
    Apply the changes by rebuilding (if you modified `docker-compose.yml`) and restarting your LibreChat stack.
```bash
    docker compose down && docker compose up -d --build
    # Or: docker compose restart api (if only librechat.yaml changed)
```

现在，Search1API 服务器应该作为工具提供者在 LibreChat 中可用。

## 功能

- 网页搜索功能
- 新闻搜索功能
- 网页内容提取
- 网站站点地图提取
- 使用 DeepSeek R1 进行深度思考和复杂问题解决
- 与 Claude Desktop、Cursor、Windsurf、Cline 及其他 MCP 客户端无缝集成

## 工具

### 1. 搜索工具
- 名称: `search`
- 描述: 使用 Search1API 进行网页搜索
- 参数:
  * `query` (必需): 自然语言的搜索查询。请具体且简洁以获得更好的结果
  * `max_results` (可选, 默认: 10): 返回的结果数量
  * `search_service` (可选, 默认: "google"): 使用的搜索服务 (google, bing, duckduckgo, yahoo, x, reddit, github, youtube, arxiv, wechat, bilibili, imdb, wikipedia)
  * `crawl_results` (可选, 默认: 0): 需要爬取完整网页内容的结果数量
  * `include_sites` (可选): 要包含在搜索中的网站列表
  * `exclude_sites` (可选): 要从搜索中排除的网站列表
  * `time_range` (可选): 搜索结果的时间范围 ("day", "month", "year")

### 2. 新闻工具
- 名称: `news`
- 描述: 使用 Search1API 搜索新闻文章
- 参数:
  * `query` (必需): 自然语言的搜索查询。请具体且简洁以获得更好的结果
  * `max_results` (可选, 默认: 10): 返回的结果数量
  * `search_service` (可选, 默认: "bing"): 使用的搜索服务 (google, bing, duckduckgo, yahoo, hackernews)
  * `crawl_results` (可选, 默认: 0): 需要爬取完整网页内容的结果数量
  * `include_sites` (可选): 要包含在搜索中的网站列表
  * `exclude_sites` (可选): 要从搜索中排除的网站列表
  * `time_range` (可选): 搜索结果的时间范围 ("day", "month", "year")

### 3. 爬虫工具
- 名称: `crawl`
- 描述: 使用 Search1API 从 URL 提取内容
- 参数:
  * `url` (必需): 要爬取的 URL

### 4. 站点地图工具
- 名称: `sitemap`
- 描述: 从 URL 获取所有相关链接
- 参数:
  * `url` (必需): 要获取站点地图的 URL

### 5. 推理工具
- 名称: `reasoning`
- 描述: 一个用于深度思考和复杂问题解决的工具，具有快速的 deepseek r1 模型和网络搜索能力（您可以在 search1api 网站上更改到任何其他模型，但速度无法保证）
- 参数:
  * `content` (必需): 需要深度思考的问题或难题

### 6. 热门话题工具
- 名称: `trending`
- 描述: 从热门平台获取热门话题
- 参数:
  * `search_service` (必需): 指定要从中获取热门话题的平台 (github, hackernews)
  * `max_results` (可选, 默认: 10): 返回的最大热门条目数

## 版本历史

- v0.2.0: 为LibreChat集成添加了回退的`.env`支持，并更新了依赖项。
- v0.1.8: 添加了X(Twitter)和Reddit搜索服务
- v0.1.7: 添加了GitHub和Hacker News的趋势工具
- v0.1.6: 添加了维基百科搜索服务
- v0.1.5: 添加了新的搜索参数（include_sites, exclude_sites, time_range）和新的搜索服务（arxiv, wechat, bilibili, imdb）
- v0.1.4: 添加了带有deepseek r1的推理工具，并更新了Cursor和Windsurf配置指南
- v0.1.3: 添加了新闻搜索功能
- v0.1.2: 添加了站点地图功能
- v0.1.1: 添加了网络爬虫功能
- v0.1.0: 初始版本，包含搜索功能

## 许可证

本项目采用MIT许可证 - 详情请参阅LICENSE文件。

**官方网站：** [https://github.com/fatwang2/search1api-mcp](https://github.com/fatwang2/search1api-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`browser`
- 标签：`browser automation`, `search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y search1api-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/fatwang2-search1api.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
