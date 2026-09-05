---
title: "AniList MCP管理服务器"
description: "语言类型：英语 翻译结果：AniList MCP服务器，用于访问AniList API数据"
---

# AniList MCP管理服务器

语言类型：英语 翻译结果：AniList MCP服务器，用于访问AniList API数据

# AniList MCP 服务器
[Smithery](https://smithery.ai/server/@yuna0x0/anilist-mcp)

这是一个与 AniList API 接口的 Model Context Protocol (MCP) 服务器，允许 LLM 客户端访问和互动来自 AniList 的动画、漫画、角色、工作人员和用户数据。

## 功能

- 搜索动画、漫画、角色、工作人员和工作室
- 获取特定动画、漫画、角色和工作人员成员的详细信息
- 访问用户资料和列表
- 支持高级过滤选项
- 获取类型和媒体标签

## 前提条件

- Node.js 18+

## 与 Claude Desktop（或其他 MCP 客户端）一起使用

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@yuna0x0/anilist-mcp) 自动为 Claude Desktop 安装 AniList MCP 服务器：

```bash
npx -y @smithery/cli install @yuna0x0/anilist-mcp --client claude

# For other MCP clients, use the following command:
# List available clients
npx -y @smithery/cli list clients
# Install to other clients
npx -y @smithery/cli install @yuna0x0/anilist-mcp --client 
```

### 通过 mcp-get 安装

```bash
npx @michaellatman/mcp-get@latest install anilist-mcp
```

### 手动安装

1. 将此服务器添加到您的 `claude_desktop_config.json` 中：

```json
{
  "mcpServers": {
    "anilist": {
      "command": "npx",
      "args": ["-y", "anilist-mcp"],
      "env": {
        "ANILIST_TOKEN": "your_api_token"
      }
    }
  }
}
```

如果您不打算使用需要登录的操作的 AniList 令牌，则可以完全删除 `env` 对象。

2. 重启 Claude Desktop
3. 使用工具与 AniList 交互

## 环境变量

- `ANILIST_TOKEN`: (可选) AniList API 令牌（仅在需要登录的操作时需要）

### 获取 AniList API 令牌（可选）

要获取 API 令牌，请按照以下步骤操作：

1. 转到 [AniList 设置](https://anilist.co/settings/developer)。
2. 单击“创建新客户端”。
3. 使用此 URL 作为您客户端的“重定向 URL”：
```
https://anilist.co/api/v2/oauth/pin
```

4. 单击“保存”
5. 然后转到 https://anilist.co/api/v2/oauth/authorize?client_id={clientID}&response_type=token，将 `{clientID}` 替换为您获得的客户端 ID。它会要求您登录，然后提供给您使用的令牌。
6. 复制生成的令牌，并将其用于您的 `.env` 文件或环境变量中。

## 可用工具

### 杂项工具
- **get_genres**: 获取 AniList 上所有可用的类型
- **get_media_tags**: 获取 AniList 上所有可用的媒体标签
- **get_site_statistics**: 获取过去七天内 AniList 站点统计信息
- **get_studio**: 通过其 AniList ID 或名称获取工作室信息
- **favourite_studio**: [需要登录] 通过其 ID 收藏或取消收藏一个工作室

### 活动工具
- **delete_activity**: [需要登录] 删除当前授权用户的活动帖子
- **get_activity**: 通过其 ID 获取特定的 AniList 活动
- **get_user_activity**: 获取用户的活动
- **post_message_activity**: [需要登录] 发布新的消息活动或更新现有活动
- **post_text_activity**: [需要登录] 发布新的文本活动或更新现有活动

### 列表工具
- **get_user_anime_list**: 获取用户的动画列表
- **get_user_manga_list**: 获取用户的漫画列表
- **add_list_entry**: [需要登录] 向授权用户的列表中添加条目
- **remove_list_entry**: [需要登录] 从授权用户的列表中移除条目
- **update_list_entry**: [需要登录] 更新授权用户列表中的条目

### 媒体工具
- **get_anime**: 通过 AniList ID 获取有关动漫的详细信息
- **get_manga**: 通过 AniList ID 获取有关漫画的详细信息
- **favourite_anime**: [需要登录] 通过 ID 收藏或取消收藏动漫
- **favourite_manga**: [需要登录] 通过 ID 收藏或取消收藏漫画

### 人物工具
- **get_character**: 通过 AniList ID 获取有关角色的信息
- **get_staff**: 通过 AniList ID 获取有关工作人员的信息
- **favourite_character**: [需要登录] 通过 ID 收藏或取消收藏角色
- **favourite_staff**: [需要登录] 通过 ID 收藏或取消收藏工作人员
- **get_todays_birthday_characters**: 获取今天生日的所有角色
- **get_todays_birthday_staff**: 获取今天生日的所有工作人员

### 推荐工具
- **get_recommendation**: 通过其 ID 获取 AniList 推荐
- **get_recommendations_for_media**: 获取特定媒体的 AniList 推荐

### 搜索工具
- **search_activity**: 在 AniList 上搜索活动
- **search_anime**: 使用查询词和过滤器搜索动漫
- **search_manga**: 使用查询词和过滤器搜索漫画
- **search_character**: 根据查询词搜索角色
- **search_staff**: 根据查询词搜索工作人员
- **search_studio**: 根据查询词搜索工作室
- **search_user**: 在 AniList 上搜索用户

### 论坛工具
- **get_thread**: 通过 AniList ID 获取特定的帖子
- **get_thread_comments**: 获取特定帖子的评论
- **delete_thread**: [需要登录] 通过 ID 删除帖子

### 用户工具
- **get_user_profile**: 获取用户的 AniList 个人资料
- **get_user_stats**: 获取用户的 AniList 统计数据
- **get_full_user_info**: 获取用户的完整个人资料和统计数据
- **get_user_recent_activity**: 获取用户的最近活动
- **get_authorized_user**: [需要登录] 获取当前授权用户的个人资料信息
- **follow_user**: [需要登录] 通过 ID 关注或取消关注用户
- **update_user**: [需要登录] 更新用户设置

## 示例用法

### 基本动漫搜索

```
Can you search for anime similar to "Bocchi the Rock!"?
```

### 获取角色信息

```
Can you tell me about the character Hitori Gotou? Use the AniList tools to find information.
```

### 比较工作室作品

```
What anime has Studio Ghibli produced? Can you list their most popular works?
```

## 本地开发

此项目使用 [Bun](https://bun.sh) 作为包管理器。如果您还没有安装它，请先安装。

克隆仓库并安装依赖项：

```bash
git clone https://github.com/yuna0x0/anilist-mcp.git
cd anilist-mcp
bun install
```

### 配置（可选）

1. 通过复制示例创建一个 `.env` 文件：
```bash
cp .env.example .env
```

2. 编辑 `.env` 文件并添加您的 AniList API 令牌：
```
ANILIST_TOKEN=your_api_token
```

## 使用 MCP Inspector 进行调试

您可以使用 MCP Inspector 来测试和调试 AniList MCP 服务器：

```bash
npx @modelcontextprotocol/inspector -e ANILIST_TOKEN=your_api_token npx anilist-mcp

# Use this instead when Local Development
bun run inspector
```

然后在浏览器中打开提供的 URL（通常是 [http://localhost:5173](http://localhost:5173)）以访问 MCP Inspector 界面。从那里，您可以：

1. 连接到正在运行的AniList MCP服务器
2. 浏览可用工具
3. 使用自定义参数运行工具
4. 查看响应

这在将设置连接到Claude或其他AI助手之前进行测试特别有用。

## Docker

从Docker Hub拉取：
```bash
docker pull yuna0x0/anilist-mcp
```

Docker构建（本地开发）：
```bash
docker build -t yuna0x0/anilist-mcp .
```

Docker多平台构建（本地开发）：
```bash
docker buildx build --platform linux/amd64,linux/arm64 -t yuna0x0/anilist-mcp .
```

## 安全须知

此MCP服务器接受您在.env文件中或作为环境变量提供的AniList API令牌。请确保该信息的安全，切勿将其提交到版本控制中。

## 许可证

本项目采用MIT许可证授权 - 详情请参阅[LICENSE](https://github.com/yuna0x0/anilist-mcp/blob/HEAD/LICENSE)文件。

**官方网站：** [https://github.com/yuna0x0/anilist-mcp](https://github.com/yuna0x0/anilist-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`art and culture`, `search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y anilist-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/yuna0x0-anilist.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
