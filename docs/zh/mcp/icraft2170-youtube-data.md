---
title: "YouTube数据MCP服务"
description: "启用AI语言模型通过标准化接口与YouTube内容交互，提供检索视频信息、字幕、频道分析和趋势分析的工具。"
---

# YouTube数据MCP服务

启用AI语言模型通过标准化接口与YouTube内容交互，提供检索视频信息、字幕、频道分析和趋势分析的工具。

# YouTube MCP 服务器
[Smithery](https://smithery.ai/server/@icraft2170/youtube-data-mcp-server)

这是一个利用 YouTube 数据 API 实现的模型上下文协议 (MCP) 服务器。它允许 AI 语言模型通过标准化接口与 YouTube 内容进行交互。

## 主要功能

### 视频信息
* 获取详细的视频信息（标题、描述、时长、统计）
* 根据关键词搜索视频
* 基于特定视频获取相关视频
* 计算并分析视频互动比率

### 字幕/字幕管理
* 支持多语言的视频字幕检索
* 指定字幕的语言偏好
* 访问带时间戳的字幕以便精确内容引用

### 频道分析
* 查看详细频道统计数据（订阅者数、观看次数、视频数量）
* 获取频道内表现最佳的视频
* 分析频道的增长和互动指标

### 趋势分析
* 按地区和类别查看热门视频
* 比较多个视频的表现指标
* 发现特定类别中的流行内容

## 可用工具

该服务器提供了以下 MCP 工具：

| 工具名称 | 描述 | 必需参数 |
|-----------|-------------|---------------------|
| `getVideoDetails` | 获取关于多个 YouTube 视频的详细信息，包括元数据、统计和内容详情 | `videoIds` (数组) |
| `searchVideos` | 根据查询字符串搜索视频 | `query`, `maxResults` (可选) |
| `getTranscripts` | 为多个视频检索字幕 | `videoIds` (数组), `lang` (可选) |
| `getRelatedVideos` | 基于 YouTube 的推荐算法获取与特定视频相关的视频 | `videoId`, `maxResults` (可选) |
| `getChannelStatistics` | 获取多个频道的详细指标，包括订阅者数量、观看次数和视频数量 | `channelIds` (数组) |
| `getChannelTopVideos` | 获取特定频道中观看次数最多的视频 | `channelId`, `maxResults` (可选) |
| `getVideoEngagementRatio` | 计算多个视频的互动指标（观看次数、点赞数、评论数及互动率） | `videoIds` (数组) |
| `getTrendingVideos` | 按地区和类别获取当前流行的视频 | `regionCode` (可选), `categoryId` (可选), `maxResults` (可选) |
| `compareVideos` | 比较多个视频之间的统计数据 | `videoIds` (数组) |

## 安装

### 通过 Smithery 自动安装

通过 [Smithery](https://smithery.ai/server/@icraft2170/youtube-data-mcp-server) 自动为 Claude Desktop 安装 YouTube MCP 服务器：

```bash
npx -y @smithery/cli install @icraft2170/youtube-data-mcp-server --client claude
```

### 手动安装
```bash
# Install from npm
npm install youtube-data-mcp-server

# Or clone repository
git clone https://github.com/icraft2170/youtube-data-mcp-server.git
cd youtube-data-mcp-server
npm install
```

## 环境配置
设置以下环境变量：
* `YOUTUBE_API_KEY`: YouTube 数据 API 密钥（必需）
* `YOUTUBE_TRANSCRIPT_LANG`: 默认字幕语言（可选，默认: 'ko'）

## MCP 客户端配置
将以下内容添加到您的 Claude Desktop 配置文件中：

```json
{
  "mcpServers": {
    "youtube": {
      "command": "npx",
      "args": ["-y", "youtube-data-mcp-server"],
      "env": {
        "YOUTUBE_API_KEY": "YOUR_API_KEY_HERE",
        "YOUTUBE_TRANSCRIPT_LANG": "ko"
      }
    }
  }
}
```

## YouTube API 设置

1. 访问 Google Cloud 控制台
2. 创建一个新项目或选择一个现有项目
3. 启用 YouTube Data API v3
4. 创建 API 凭证（API 密钥）
5. 在您的环境配置中使用生成的 API 密钥

## 开发

```bash
# Install dependencies
npm install

# Run in development mode
npm run dev

# Build
npm run build
```

## 网络配置

服务器对外暴露以下端口用于通信：
- HTTP: 3000
- gRPC: 3001

## 系统要求
- Node.js 18.0.0 或更高版本

## 安全注意事项
- 始终确保您的 API 密钥安全，不要将其提交到版本控制系统
- 通过环境变量或配置文件管理您的 API 密钥
- 为您的 API 密钥设置使用限制，以防止未经授权的使用

## 许可证
本项目根据 MIT 许可证发布。详情请参阅 LICENSE 文件。

**官方网站：** [https://github.com/icraft2170/youtube-data-mcp-server](https://github.com/icraft2170/youtube-data-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`entertainment and media`, `search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y youtube-data-mcp-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/icraft2170-youtube-data.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
