---
title: "Hacker News模型上下文协议"
description: "为LLM客户端添加了强大的Hacker News集成，允许用户通过模型上下文协议访问故事、评论、用户资料和搜索功能。"
---

# Hacker News模型上下文协议

为LLM客户端添加了强大的Hacker News集成，允许用户通过模型上下文协议访问故事、评论、用户资料和搜索功能。

# Hacker News MCP 服务器

[Smithery](https://smithery.ai/server/@devabdultech/hn-mcp)
官方 Hacker News MCP 服务器 - 为 Cursor、Claude 和其他 LLM 客户端添加强大的 Hacker News 集成。通过模型上下文协议访问故事、评论、用户资料和搜索功能。

  

## 功能

- 使用 Algolia 的 HN 搜索 API 搜索故事和评论
- 按类型获取故事（热门、最新、最佳、提问、展示、工作）
- 获取带有评论的单个故事
- 获取评论树和用户讨论
- 获取用户资料和提交
- 实时访问 Hacker News 数据

## 设置

### 在 Claude 桌面版上运行

将以下内容添加到你的 `claude_desktop_config.json` 文件中：

```json
{
  "mcpServers": {
    "hackernews": {
      "command": "npx",
      "args": ["-y", "@devabdultech/hn-mcp-server"]
    }
  }
}
```

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@devabdultech/hn-mcp) 自动安装 Hacker News MCP 服务器用于 Claude 桌面版，请使用以下命令：

```bash
npx -y @smithery/cli install @devabdultech/hn-mcp --client claude
```

## 工具

1. `search`
   * 使用 Algolia 的搜索 API 在 Hacker News 上搜索故事和评论
   * 输入：
         * `query` (字符串): 搜索查询
         * `type` (可选字符串): 按类型过滤 ('story' 或 'comment')
         * `page` (可选数字): 分页的页码
         * `hitsPerPage` (可选数字): 每页的结果数量（最大 100）
   * 返回: 包含故事和评论的搜索结果

2. `getStories`
   * 按类型获取多个故事（热门、最新、最佳、提问、展示、工作）
   * 输入：
         * `type` (字符串): 要获取的故事类型 ('top', 'new', 'best', 'ask', 'show', 'job')
         * `limit` (可选数字): 要获取的故事数量（最大 100）
   * 返回: 故事对象数组

3. `getStoryWithComments`
   * 获取一个带有评论线程的故事
   * 输入：
         * `id` (数字): 故事 ID
   * 返回: 包含嵌套评论的故事详情

4. `getCommentTree`
   * 获取故事的完整评论树
   * 输入：
         * `storyId` (数字): 故事 ID
   * 返回: 层次化的评论树结构

5. `getUser`
   * 获取用户的个人资料信息
   * 输入：
         * `id` (字符串): 用户名
   * 返回: 用户个人资料详情，包括业力值、创建日期和关于文本

6. `getUserSubmissions`
   * 获取用户的提交（故事和评论）
   * 输入：
         * `id` (字符串): 用户名
   * 返回: 用户提交的故事和评论数组

### 贡献

1. 叉取仓库
2. 创建你的特性分支
3. 提交你的更改
4. 推送到该分支
5. 创建一个新的拉取请求

## 许可证

此 MCP 服务器根据 MIT 许可证授权。详见 LICENSE 文件。

## 关于

此 MCP 服务器由 [devabdultech](https://github.com/devabdultech) 构建并维护。它使用官方的 Hacker News API 和 Algolia 搜索 API，通过模型上下文协议提供对 Hacker News 数据的全面访问。

**官方网站：** [https://github.com/devabdultech/hn-mcp](https://github.com/devabdultech/hn-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`browser`
- 标签：`browser automation`, `search`, `social media`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @devabdultech/hn-mcp-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/devabdultech-hn.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
