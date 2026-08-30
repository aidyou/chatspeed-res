---
title: "国立博物馆艺术品平台"
description: "允许您搜索艺术品、检索特定艺术品的详细信息、访问艺术品的图像瓦片，并探索来自国立博物馆的用户创建的收藏。"
---

# 国立博物馆艺术品平台

允许您搜索艺术品、检索特定艺术品的详细信息、访问艺术品的图像瓦片，并探索来自国立博物馆的用户创建的收藏。

# Rijksmuseum MCP 服务器

一个模型上下文协议（MCP）服务器，通过自然语言交互提供对Rijksmuseum藏品的访问。该服务器使AI模型能够探索、分析并与来自Rijksmuseum的艺术作品和藏品进行互动。

## 功能

该服务器提供了几种与Rijksmuseum藏品互动的工具：

### 1. 搜索艺术品 (`search_artwork`)
使用各种标准搜索和筛选艺术品，包括：
- 基于文本的搜索
- 艺术家姓名
- 艺术品类别
- 材料和技术
- 时期
- 颜色
- 等等

### 2. 艺术品详情 (`get_artwork_details`)
检索特定艺术品的全面信息，包括：
- 基本详情（标题、艺术家、日期）
- 物理属性
- 历史背景
- 视觉信息
- 策展信息
- 展览历史

### 3. 高分辨率图像 (`get_artwork_image`)
访问具有深度缩放能力的高分辨率图像数据：
- 多级缩放
- 基于瓦片的图像加载
- 完全分辨率支持
- 位置信息

### 4. 用户收藏集 (`get_user_sets` & `get_user_set_details`)
探索用户创建的收藏集：
- 浏览精选集合
- 查看主题分组
- 分析收藏模式
- 访问详细的集合信息

### 5. 图像查看 (`open_image_in_browser`)
直接在浏览器中打开艺术品图像以详细查看。

### 6. 艺术家时间线 (`get_artist_timeline`)
生成艺术家作品的时间顺序时间线：
- 追踪艺术发展
- 分析时期和风格
- 研究职业进展

## 示例用例

这里是一些您可以向AI询问的示例查询：

### 艺术品发现
```
"Show me all paintings by Rembrandt from the 1640s"
"Find artworks that prominently feature the color blue"
"What are the most famous masterpieces in the collection?"
"Search for still life paintings from the Dutch Golden Age"
```

### 艺术品分析
```
"Tell me everything about The Night Watch"
"What are the dimensions and materials used in Van Gogh's Self Portrait?"
"Show me high-resolution details of the brushwork in Vermeer's The Milkmaid"
"Compare the colors used in different versions of The Potato Eaters"
```

### 艺术家研究
```
"Create a timeline of Rembrandt's self-portraits"
"How did Van Gogh's use of color evolve throughout his career?"
"Show me all works by Frans Hals in chronological order"
"What techniques did Jan Steen use in his paintings?"
```

### 主题探索
```
"Find all artworks depicting biblical scenes"
"Show me paintings of Amsterdam in the 17th century"
"What artworks feature flowers or still life arrangements?"
"Find portraits that include musical instruments"
```

### 收藏分析
```
"Show me the most popular user-curated collections"
"Find sets that focus on landscape paintings"
"What are the recent additions to the museum's collection?"
"Show me collections featuring works from multiple artists"
```

### 视觉细节
```
"Let me examine the details in the background of The Night Watch"
"Show me a close-up of the jewelry in Girl with a Pearl Earring"
"Can you display the highest resolution version of The Jewish Bride?"
"I want to study the facial expressions in The Syndics"
```

## 开始使用

您可以通过两种方式安装此服务器：

### 1. 使用Claude桌面版及NPM包
更新您的Claude配置文件 (`~/Library/Application Support/Claude/claude_desktop_config.json`)：

```json
{
  "mcpServers": {
    "rijksmuseum-server": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-server-rijksmuseum"
      ],
      "env": {
        "RIJKSMUSEUM_API_KEY": "your_api_key_here"
      }
    }
  }
}
```
您可以从[Rijksmuseum API门户](https://data.rijksmuseum.nl/docs/api/)获取API密钥。

### 2. 从源代码安装

1. 克隆此仓库
2. 安装依赖项：
```bash
   npm install
```
3. 复制示例环境文件：
```bash
   cp .env.example .env
```
4. 在 `.env` 文件中添加您的 Rijksmuseum API 密钥：
```
   RIJKSMUSEUM_API_KEY=your_api_key_here
```
5. 然后更新您的 Claude 配置文件：
```json
   {
     "mcpServers": {
       "rijksmuseum-server": {
         "command": "node",
         "args": [
           "/path/to/rijksmuseum-server/build/index.js"
         ],
         "env": {
           "RIJKSMUSEUM_API_KEY": "your_api_key_here"
         }
       }
     }
   }
```

请确保：
- 将 `/path/to/rijksmuseum-server` 替换为您实际的安装路径
- 在 `env` 部分添加您的 Rijksmuseum API 密钥

更新配置后，重启 Claude Desktop 以使更改生效。

## 配置

可以通过环境变量来配置服务器：
- `RIJKSMUSEUM_API_KEY`: 您的 Rijksmuseum API 密钥（必需）
- `PORT`: 服务器端口（默认：3000）
- `LOG_LEVEL`: 日志级别（默认：'info'）

## API 文档

有关此服务器使用的 Rijksmuseum API 端点的详细信息，请访问：
[Rijksmuseum API 文档](https://data.rijksmuseum.nl/object-metadata/api/)

## 贡献

欢迎贡献！请随时提交拉取请求或创建问题报告 bug 和功能请求。

## 许可证

本项目采用 MIT 许可证 - 详情请参阅 LICENSE 文件。

**官方网站：** [https://github.com/r-huijts/rijksmuseum-mcp](https://github.com/r-huijts/rijksmuseum-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`, `media`
- 标签：`search`, `image and video processing`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y mcp-server-rijksmuseum`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/r-huijts-rijksmuseum.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
