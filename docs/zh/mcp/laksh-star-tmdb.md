---
title: "TMDB电影推荐"
description: "集成电影数据库 (TMDB) API，提供电影信息、搜索功能和推荐。"
---

# TMDB电影推荐

集成电影数据库 (TMDB) API，提供电影信息、搜索功能和推荐。

# TMDB MCP 服务器

[Smithery](https://smithery.ai/server/@Laksh-star/mcp-server-tmdb)
此MCP服务器与The Movie Database (TMDB) API集成，提供电影信息、搜索功能和推荐。

# 先决条件

在安装和运行TMDB MCP服务器之前，请确保已安装并配置以下先决条件：

## 必需软件

- **Node.js**
  - 版本 18.0.0 或更高
  - 从 [Node.js 官方网站](https://nodejs.org/) 下载
  - 验证安装：`node --version`

- **npm (Node 包管理器)**
  - 版本 8.0.0 或更高（随 Node.js 提供）
  - 验证安装：`npm --version`

- **TypeScript**
  - 将作为项目依赖项安装
  - 可以全局安装：`npm install -g typescript`
  - 验证安装：`tsc --version`

## 必需账户和API密钥

- **TMDB 账户**
  - 在 [TMDB](https://www.themoviedb.org/) 注册免费账户
  - 从 TMDB 控制台获取 API 密钥
  - API 访问必须由 TMDB 批准

- **Claude 桌面应用程序**
  - 安装最新版本
  - 有权修改配置文件

## 系统要求

- **操作系统**
  - macOS (10.15 或更高版本)
  - Linux (现代发行版)

- **硬件要求**
  - 最低 4GB RAM
  - 1GB 空闲磁盘空间
  - 稳定的互联网连接

## 开发环境

为了获得最佳开发体验，我们建议：
- 支持 TypeScript 的代码编辑器（例如 VS Code）
- 终端访问
- Git（用于版本控制）

## 功能

### 工具

- **search_movies**
  - 根据标题或关键词搜索电影
  - 输入：`query` (字符串): 搜索查询
  - 返回：包含标题、发行年份、ID、评分和概述的电影列表
  - 示例：搜索关于太空探索的电影

- **get_recommendations**
  - 根据电影 ID 获取电影推荐
  - 输入：`movieId` (字符串): TMDB 电影 ID
  - 返回：前 5 条推荐电影及其详细信息
  - 示例：根据电影 ID 550 (搏击俱乐部) 获取推荐

- **get_trending**
  - 获取指定时间窗口内的热门电影
  - 输入：`timeWindow` (字符串): "day" 或 "week"
  - 返回：前 10 条热门电影及其详细信息
  - 示例：获取今天的热门电影

### 资源

该服务器提供对 TMDB 电影信息的访问：

- **Movies** (`tmdb:///movie/`)
  - 包含以下详细信息的全面电影详情：
    - 标题和发行日期
    - 评分和概述
    - 类型
    - 海报 URL
    - 演员信息（前 5 名演员）
    - 导演
    - 选定的评论
  - 所有数据以 JSON 格式返回

  ## 开始使用

1. 获取 TMDB API 密钥：
   - 在 [TMDB](https://www.themoviedb.org/) 注册
   - 进入您的账户设置
   - 导航到 API 部分
   - 为开发者用途请求一个 API 密钥

2. 克隆并设置项目：
```bash
   git clone [repository-url]
   cd mcp-server-tmdb
   npm install
```

3. 构建服务器：
```bash
   npm run build
```

4. 设置环境变量：
```bash
   export TMDB_API_KEY=your_api_key_here
```

### 与 Claude Desktop 结合使用

要将此服务器与 Claude Desktop 集成，请在应用程序的服务器配置文件（位于 `~/Library/Application Support/Claude/config.json`）中添加以下内容：

```json
{
  "mcpServers": {
    "tmdb": {
      "command": "/full/path/to/dist/index.js",
      "env": {
        "TMDB_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

请将 `/full/path/to` 替换为您项目的实际路径。

## 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@Laksh-star/mcp-server-tmdb) 自动安装适用于 Claude Desktop 的 TMDB 服务器：

```bash
npx -y @smithery/cli install @Laksh-star/mcp-server-tmdb --client claude
```

## 示例用法

一旦服务器与 Claude Desktop 一起运行，您可以使用如下命令：

1. 搜索电影：
```
   "Search for movies about artificial intelligence"
```

2. 获取热门电影：
```
   "What are the trending movies today?"
   "Show me this week's trending movies"
```

3. 获取电影推荐：
```
   "Get movie recommendations based on movie ID 550"
```

4. 获取电影详情：
```
   "Tell me about the movie with ID 550"
```

## 错误处理

该服务器包括全面的错误处理功能，涵盖：
- 无效的 API 密钥
- 网络错误
- 无效的电影 ID
- 格式错误的请求

错误信息将以用户友好的格式通过 Claude Desktop 返回。

## 开发

在开发过程中监视更改：
```bash
npm run watch
```

## 许可证

此 MCP 服务器根据 MIT 许可证发布。详见 LICENSE 文件。

## 贡献

欢迎贡献！请随时提交 Pull Request。

**官方网站：** [https://github.com/Laksh-star/mcp-server-tmdb](https://github.com/Laksh-star/mcp-server-tmdb)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`entertainment and media`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`/full/path/to/dist/index.js`
- 参数：无

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/laksh-star-tmdb.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
