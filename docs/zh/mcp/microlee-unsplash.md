---
title: "unsplash图片浏览"
description: "Unsplash MCP Server 一个基于 Model Context Protocol 的 Unsplash 工具服务器，提供搜索、照片详情、随机照片、集合、主题、用户等 15 个工具。 功能列表 照片相关工具 (Photos) - searchphotos - 按关键词搜索 Unsplash 照片，支持分页、排序、颜色筛选和方向筛选 - getphoto - 根据照片 ID 获取单张照片…"
---

# unsplash图片浏览

Unsplash MCP Server 一个基于 Model Context Protocol 的 Unsplash 工具服务器，提供搜索、照片详情、随机照片、集合、主题、用户等 15 个工具。 功能列表 照片相关工具 (Photos) - searchphotos - 按关键词搜索 Unsplash 照片，支持分页、排序、颜色筛选和方向筛选 - getphoto - 根据照片 ID 获取单张照片…

# Unsplash MCP Server

一个基于 Model Context Protocol 的 Unsplash 工具服务器，提供搜索、照片详情、随机照片、集合、主题、用户等 15 个工具。

## 功能列表

### 照片相关工具 (Photos)
- **search_photos** - 按关键词搜索 Unsplash 照片，支持分页、排序、颜色筛选和方向筛选
- **get_photo** - 根据照片 ID 获取单张照片的详细信息，包括作者、尺寸、下载链接等
- **list_photos** - 列出 Unsplash 最新、最热门或最旧的照片列表，支持分页
- **get_random_photo** - 获取随机照片，可按关键词、集合、主题、用户等条件筛选
- **track_download** - 追踪照片下载事件（Unsplash API 要求），在用户下载照片时必须调用

### 集合相关工具 (Collections)
- **list_collections** - 列出 Unsplash 上的照片集合，支持分页浏览
- **get_collection** - 根据集合 ID 获取集合的详细信息，包括标题、描述、照片数量等
- **get_collection_photos** - 获取指定集合中的所有照片，支持分页和方向筛选

### 主题相关工具 (Topics)
- **list_topics** - 列出 Unsplash 上的所有主题分类，支持按最新、最旧或位置排序
- **get_topic** - 根据主题 ID 或 slug 获取主题的详细信息
- **get_topic_photos** - 获取指定主题下的照片，支持分页、排序和方向筛选

### 用户相关工具 (Users)
- **get_user** - 根据用户名获取 Unsplash 用户的公开信息，包括简介、作品数量等
- **get_user_photos** - 获取指定用户上传的所有照片，支持分页、排序和方向筛选
- **get_user_likes** - 获取指定用户点赞（喜欢）的照片列表，支持分页、排序和方向筛选
- **get_user_collections** - 获取指定用户创建的照片集合列表，支持分页

## 安装与构建
```bash
npm install
npm run build
```

## 运行
```bash
UNSPLASH_ACCESS_KEY=your_key node build/index.js
```

## MCP 配置示例
```json
{
    "mcpServers": {
        "unsplash": {
            "command": "npx",
            "args": [
                "-y",
                "@microlee666/unsplash-mcp-server"
            ],
            "env": {
                "UNSPLASH_ACCESS_KEY": ""
            },
            "disabled": false,
            "alwaysAllow": [],
            "disabledTools": []
        }
    }
}
```

## 发布到 npm
需先登录 npm 并确保包名未被占用：
```bash
npm login
npm publish --registry https://registry.npmjs.org
```

**官方网站：** [https://unsplash.com/](https://unsplash.com/)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`search`, `art and culture`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @microlee666/unsplash-mcp-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/microlee-unsplash.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
