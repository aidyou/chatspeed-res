---
title: "Figma MCP 服务器"
description: "一个集成了Figma API的模型上下文协议服务器，允许与Figma文件、评论、组件、项目和webhook管理进行交互。"
---

# Figma MCP 服务器

一个集成了Figma API的模型上下文协议服务器，允许与Figma文件、评论、组件、项目和webhook管理进行交互。

# Figma MCP 服务器

这是一个模型上下文协议（MCP）服务器，它通过与Figma的API集成，允许您与Figma文件、评论、组件等进行交互。

## 功能

- **文件操作**
  - 获取文件信息
  - 获取文件版本历史
  - 获取文件中的组件
  
- **评论管理**
  - 列出文件中的评论
  - 添加新评论
  - 删除评论
  
- **项目与团队功能**
  - 列出团队项目
  - 获取项目文件
  - 获取已发布的样式
  
- **Webhook 管理**
  - 创建webhook
  - 列出现有webhook
  - 删除webhook

## 安装

1. 克隆仓库
2. 安装依赖项：
```bash
npm install
```
3. 构建服务器：
```bash
npm run build
```

## 配置

在您的MCP设置文件中使用Figma访问令牌配置服务器：

```json
{
  "mcpServers": {
    "figma": {
      "command": "node",
      "args": ["path/to/figma-server/build/index.js"],
      "env": {
        "FIGMA_ACCESS_TOKEN": "your-access-token-here"
      },
      "disabled": false,
      "alwaysAllow": []
    }
  }
}
```

## 可用工具

### 文件操作

#### get_file
获取关于Figma文件的信息
```json
{
  "file_key": "string"
}
```

#### get_file_versions
获取文件的版本历史
```json
{
  "file_key": "string"
}
```

#### get_file_components
获取文件中的组件
```json
{
  "file_key": "string"
}
```

### 评论管理

#### get_file_comments
从文件中获取评论
```json
{
  "file_key": "string"
}
```

#### post_comment
向文件发布评论
```json
{
  "file_key": "string",
  "message": "string"
}
```

#### delete_comment
从文件中删除评论
```json
{
  "file_key": "string",
  "comment_id": "string"
}
```

### 项目与团队操作

#### get_team_projects
获取团队的项目
```json
{
  "team_id": "string"
}
```

#### get_project_files
获取项目中的文件
```json
{
  "project_id": "string"
}
```

#### get_component_styles
获取已发布的样式
```json
{
  "team_id": "string"
}
```

### Webhook 管理

#### create_webhook
创建一个webhook
```json
{
  "team_id": "string",
  "event_type": "string",
  "callback_url": "string"
}
```

#### get_webhooks
列出webhook
```json
{
  "team_id": "string"
}
```

#### delete_webhook
删除一个webhook
```json
{
  "webhook_id": "string"
}
```

## 使用示例

```typescript
// Example using the MCP tool to get file information

figma
get_file

{
  "file_key": "your-file-key"
}

```

## 许可证

MIT

## 贡献指南

1. Fork 本仓库
2. 创建你的特性分支
3. 提交更改
4. 推送到该分支
5. 创建一个新的Pull Request

**官方网站：** [https://github.com/deepsuthar496/figma-mcp-server](https://github.com/deepsuthar496/figma-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`art and culture`, `developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`path/to/figma-server/build/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/deepsuthar496-figma.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
