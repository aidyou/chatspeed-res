---
title: "Sketchfab模型平台"
description: "允许通过克劳德或光标与Sketchfab的3D模型平台进行交互，使用户能够直接从人工智能界面搜索、查看详细信息和下载3D模型。"
---

# Sketchfab模型平台

允许通过克劳德或光标与Sketchfab的3D模型平台进行交互，使用户能够直接从人工智能界面搜索、查看详细信息和下载3D模型。

# Sketchfab MCP 服务器

一个用于与 Sketchfab 的 3D 模型平台交互的模型上下文协议 (MCP) 服务器。此 MCP 允许您通过 Claude 或 Cursor 直接搜索、查看详细信息和下载 Sketchfab 上的 3D 模型。

## 功能

- **搜索 3D 模型**：使用关键字、标签和类别在 Sketchfab 上查找模型
- **查看模型详细信息**：获取关于特定模型的全面信息
- **下载模型**：以各种格式（gltf, glb, usdz, source）下载模型

## 前提条件

- Node.js 18 或更高版本
- 一个 Sketchfab API 密钥（用于身份验证）

## 安装

1. 克隆此仓库
2. 安装依赖项：
```
   npm install
```
3. 构建项目：
```
   npm run build
```

## 使用

### 运行 MCP 服务器

```
npm start
```

要提供您的 Sketchfab API 密钥，请使用 `--api-key` 参数：

```
node build/index.js --api-key YOUR_API_KEY
```

或者，您可以设置 `SKETCHFAB_API_KEY` 环境变量：

```
export SKETCHFAB_API_KEY=YOUR_API_KEY
npm start
```

### 可用工具

#### 1. sketchfab-search

根据关键词和过滤器在 Sketchfab 上搜索 3D 模型。

参数：
- `query`（可选）：文本搜索查询（例如："car", "house", "character"）
- `tags`（可选）：按特定标签过滤（例如：["animated", "rigged", "pbr"]）
- `categories`（可选）：按类别过滤（例如：["characters", "architecture", "vehicles"]）
- `downloadable`（可选）：设置为 true 以仅显示可下载的模型
- `limit`（可选）：返回的最大结果数量（1-24，默认值：10）

#### 2. sketchfab-model-details

获取有关特定 Sketchfab 模型的详细信息。

参数：
- `modelId`：Sketchfab 模型的唯一 ID

#### 3. sketchfab-download

从 Sketchfab 下载 3D 模型。

参数：
- `modelId`：要下载的 Sketchfab 模型的唯一 ID
- `format`（可选）：下载模型的首选格式（gltf, glb, usdz, source）
- `outputPath`（可选）：保存下载文件的本地目录或文件路径

## 与 Cursor 一起使用

1. 转到 Cursor 设置 -> MCP -> 添加新的 MCP 服务器
2. 配置您的 MCP：
   - 名称：Sketchfab MCP
   - 类型：command
   - 命令：`node /path/to/build/index.js --api-key YOUR_API_KEY`

## 与 Claude Desktop 一起使用

将以下 MCP 配置添加到您的 Claude Desktop 配置中：

```json
{
  "mcpServers": {
    "sketchfab": {
      "command": "node",
      "args": ["/path/to/build/index.js", "--api-key", "YOUR_API_KEY"]
    }
  }
}
```

## 环境变量

您可以设置以下环境变量：

- `SKETCHFAB_API_KEY`：您的 Sketchfab API 密钥（作为传递 `--api-key` 参数的替代方案）

## 许可证

ISC

**官方网站：** [https://github.com/gregkop/sketchfab-mcp-server](https://github.com/gregkop/sketchfab-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`art and culture`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`/path/to/build/index.js --api-key YOUR_API_KEY`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/gregkop-sketchfab.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
