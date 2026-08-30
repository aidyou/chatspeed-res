---
title: "Spotify音乐管理"
description: "通过Spotify Web API启用与Spotify音乐目录的交互，支持搜索、艺人信息获取、播放列表管理和自动令牌处理。"
---

# Spotify音乐管理

通过Spotify Web API启用与Spotify音乐目录的交互，支持搜索、艺人信息获取、播放列表管理和自动令牌处理。

# ArtistLens

[Smithery](https://smithery.ai/server/@superseoworld/artistlens)
[![npm version](/mcp-assets/5b2f6860f196533871b70e560b2a8000.svg)](https://www.npmjs.com/package/@thomaswawra/artistlens)

一个强大的模型上下文协议（MCP）服务器，提供对Spotify Web API的访问。ArtistLens使您能够无缝地与Spotify的音乐目录进行交互，包括搜索曲目、专辑和艺术家，以及访问特定艺术家的信息，如热门曲目和相关艺术家。

**当前版本:** 0.4.12

## 安装

### 通过Smithery安装

要通过[Smithery](https://smithery.ai/server/@superseoworld/artistlens)自动为Claude Desktop安装ArtistLens：

```bash
npx -y @smithery/cli install @superseoworld/artistlens --client claude
```

### 手动安装

您可以全局安装该软件包：

```bash
npm install -g @thomaswawra/artistlens
```

或者直接使用npx运行：

```bash
npx -y @thomaswawra/artistlens
```

## 配置

添加到您的MCP设置文件中（例如，`claude_desktop_config.json`或`cline_mcp_settings.json`）：

```json
{
  "mcpServers": {
    "spotify": {
      "command": "npx",
      "args": ["-y", "@thomaswawra/artistlens"],
      "env": {
        "SPOTIFY_CLIENT_ID": "your_client_id",
        "SPOTIFY_CLIENT_SECRET": "your_client_secret"
      },
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

您需要提供您的Spotify API凭证：
1. 前往[Spotify开发者仪表板](https://developer.spotify.com/dashboard)
2. 创建一个新的应用程序
3. 获取您的客户端ID和客户端密钥
4. 将它们按照上述方式添加到配置中

## 功能

- 搜索曲目、专辑、艺术家和播放列表
- 获取艺术家信息，包括热门曲目和相关艺术家
- 获取专辑信息和曲目
- 访问新发行和推荐
- 获取带有市场特定内容和章节的有声书信息
- 注意：有声书端点可能需要额外的身份验证或市场特定访问权限
- 获取并修改播放列表信息（名称、描述、公开/私密状态）
- 支持分页访问播放列表曲目和项目
- 同时支持Spotify ID和URI
- 自动令牌管理，采用客户端凭据流
- 全面的功能测试套件
- 代码组织良好，职责分离明确

## 可用工具

- `get_access_token`: 获取有效的 Spotify 访问令牌
- `search`: 搜索曲目、专辑、艺术家或播放列表
- `get_artist`: 获取艺术家信息
- `get_artist_top_tracks`: 获取艺术家的热门曲目
- `get_artist_related_artists`: 获取与给定艺术家相似的艺术家
- `get_artist_albums`: 获取艺术家的专辑
- `get_album`: 获取专辑信息
- `get_album_tracks`: 获取专辑中的曲目
- `get_track`: 获取曲目信息
- `get_available_genres`: 获取用于推荐的可用流派列表
- `get_new_releases`: 获取新发行的专辑
- `get_recommendations`: 基于种子曲目、艺术家或流派获取曲目推荐
- `get_audiobook`: 获取有声书信息，可选市场参数
- `get_multiple_audiobooks`: 获取多个有声书的信息（最多50个）
- `get_audiobook_chapters`: 获取有声书章节，支持分页（每次请求1-50章）
- `get_playlist`: 获取由 Spotify 用户拥有的播放列表
- `get_playlist_tracks`: 获取播放列表中曲目的完整详情（每次请求1-100首曲目）
- `get_playlist_items`: 获取播放列表中项目的完整详情（每次请求1-100个项目）
- `modify_playlist`: 更改播放列表详情（名称、描述、公开/私有状态、协作状态）
- `add_tracks_to_playlist`: 向播放列表添加一个或多个曲目，可选位置
- `remove_tracks_from_playlist`: 从播放列表中移除一个或多个曲目，可选位置和快照ID
- `get_current_user_playlists`: 获取当前 Spotify 用户拥有或关注的播放列表列表（每次请求1-50个播放列表）
- `get_featured_playlists`: 获取带有特定类别的 Spotify 推荐播放列表列表，可选语言环境和支持分页
- `get_category_playlists`: 获取带有特定类别的 Spotify 播放列表列表

## 更新

要更新到最新版本：

```bash
# If installed globally
npm update -g @thomaswawra/artistlens

# If using npx, it will automatically use the latest version
npx -y @thomaswawra/artistlens
```

## 开发

该项目是开源的，可在 GitHub 上找到：[https://github.com/superseoworld/artistlens](https://github.com/superseoworld/artistlens)。

### 项目结构

代码库组织成以下目录：
- `src/handlers/`: 包含不同 Spotify API 端点的处理器类
- `src/types/`: 请求和响应对象的 TypeScript 接口
- `src/utils/`: 用于 API 通信的实用函数和类
- `src/__tests__/`: 所有功能的 Jest 测试文件

### 测试

该项目使用 Jest 进行测试。要运行测试：

```bash
npm test
```

在开发期间以监视模式运行测试：

```bash
npm run test:watch
```

### 贡献

要贡献代码，请遵循以下步骤：
1. 叉取仓库
2. 创建你的特性分支 (`git checkout -b feature/amazing-feature`)
3. 为你的更改添加测试
4. 提交你的更改 (`git commit -m 'Add some amazing feature'`)
5. 将更改推送到分支 (`git push origin feature/amazing-feature`)
6. 打开拉取请求

## 许可证

MIT 许可证

[Smithery](https://smithery.ai/server/@superseoworld/artistlens)

**官方网站：** [https://github.com/superseoworld/mcp-spotify](https://github.com/superseoworld/mcp-spotify)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`entertainment and media`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @thomaswawra/artistlens`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/superseoworld-spotify.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
