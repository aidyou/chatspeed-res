---
title: "Figma MCP API工具"
description: "语言类型：英语 翻译结果：具有完整API功能的Figma MCP"
---

# Figma MCP API工具

语言类型：英语 翻译结果：具有完整API功能的Figma MCP

# Figma MCP 服务器

[thirdstrandstudio.com](https://thirdstrandstudio.com)

[Smithery](https://smithery.ai/server/@thirdstrandstudio/mcp-figma)

用于与 Figma API 交互的 MCP 服务器。此服务器通过模型上下文协议提供了一整套 Figma API 方法。在处理大型 Figma 文件时，您可能需要告诉它使用 depth = 1 进行 figma_get_file 操作，然后根据需要增加。

![image](/mcp-assets/80684fd100ae09b9de617675bbf68cda.png)

## 工具

该服务器将所有 Figma API 方法实现为 MCP 工具：

### 用户方法
1. `figma_get_me` - 获取当前用户

### 文件方法
2. `figma_get_file` - 通过键获取 Figma 文件
3. `figma_get_file_nodes` - 从 Figma 文件中获取特定节点
4. `figma_get_images` - 从 Figma 文件中渲染图像
5. `figma_get_image_fills` - 获取 Figma 文件中的图像填充
6. `figma_get_file_versions` - 获取 Figma 文件的版本历史记录

### 评论方法
7. `figma_get_comments` - 获取 Figma 文件中的评论
8. `figma_post_comment` - 向 Figma 文件添加评论
9. `figma_delete_comment` - 从 Figma 文件中删除评论
10. `figma_get_comment_reactions` - 获取评论的反应
11. `figma_post_comment_reaction` - 向评论添加反应
12. `figma_delete_comment_reaction` - 从评论中删除反应

### 团队和项目方法
13. `figma_get_team_projects` - 获取团队中的项目
14. `figma_get_project_files` - 获取项目中的文件

### 组件方法
15. `figma_get_team_components` - 获取团队中的组件
16. `figma_get_file_components` - 获取文件中的组件
17. `figma_get_component` - 通过键获取组件
18. `figma_get_team_component_sets` - 获取团队中的组件集
19. `figma_get_file_component_sets` - 获取文件中的组件集
20. `figma_get_component_set` - 通过键获取组件集

### 样式方法
21. `figma_get_team_styles` - 获取团队中的样式
22. `figma_get_file_styles` - 获取文件中的样式
23. `figma_get_style` - 通过键获取样式

### Webhook 方法（V2 API）
24. `figma_post_webhook` - 创建 Webhook
25. `figma_get_webhook` - 通过 ID 获取 Webhook
26. `figma_update_webhook` - 更新 Webhook
27. `figma_delete_webhook` - 删除 Webhook
28. `figma_get_team_webhooks` - 获取团队的 Webhook

### 库分析方法
29. `figma_get_library_analytics_component_usages` - 获取库分析组件使用数据
30. `figma_get_library_analytics_style_usages` - 获取库分析样式使用数据
31. `figma_get_library_analytics_variable_usages` - 获取库分析变量使用数据

## 安装

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/embed/@thirdstrandstudio/mcp-figma) 自动安装适用于 Claude Desktop 的 mcp-figma：

```bash
npx @smithery/cli@latest install @thirdstrandstudio/mcp-figma --client claude
```

### 前提条件
- Node.js (v16 或更高版本)
- npm 或 yarn

### 安装包

```bash
# Clone the repository
git clone https://github.com/thirdstrandstudio/mcp-figma.git
cd mcp-figma

# Install dependencies
npm install

# Build the package
npm run build
```

## 设置

要使用此MCP服务器，您需要设置您的Figma API令牌。您可以通过以下三种方式之一来完成此操作：

### 1. 环境变量

在项目根目录下创建一个`.env`文件或直接设置环境变量：

```
FIGMA_API_KEY=your_figma_api_key
```

### 2. 命令行参数

启动服务器时，您可以将您的Figma API令牌作为命令行参数传递：

```bash
# Using the long form
node dist/index.js --figma-token YOUR_FIGMA_TOKEN

# Or using the short form
node dist/index.js -ft YOUR_FIGMA_TOKEN
```

### 与Claude Desktop一起使用

将以下内容添加到您的`claude_desktop_config.json`中：

#### 使用npx
```json
{
  "mcpServers": {
    "figma": {
      "command": "npx",
      "args": ["@thirdstrandstudio/mcp-figma", "--figma-token", "your_figma_api_key"]
    }
  }
}
```

#### 直接使用Node.js（带环境变量）
```json
{
  "mcpServers": {
    "figma": {
      "command": "node",
      "args": ["/path/to/mcp-figma/dist/index.js"],  
      "env": {
        "FIGMA_API_KEY": "your_figma_api_key"
      }
    }
  }
}
```

#### 直接使用Node.js（带命令行参数）
```json
{
  "mcpServers": {
    "figma": {
      "command": "node",
      "args": ["/path/to/mcp-figma/dist/index.js", "--figma-token", "your_figma_api_key"]
    }
  }
}
```

请将`/path/to/mcp-figma`替换为实际的存储库路径。

## 示例

### 获取Figma文件

```javascript
// Get a Figma file
const result = await callTool("figma_get_file", { 
  fileKey: "abcXYZ123"
});
```

### 从文件获取评论

```javascript
// Get comments from a file
const comments = await callTool("figma_get_comments", { 
  fileKey: "abcXYZ123",
  as_md: true 
});
```

### 创建Webhook

```javascript
// Create a webhook
const webhook = await callTool("figma_post_webhook", {
  event_type: "FILE_UPDATE",
  team_id: "12345",
  endpoint: "https://example.com/webhook",
  passcode: "your_passcode_here",
  description: "File update webhook"
});
```

## 开发

```bash
# Install dependencies
npm install

# Start the server in development mode
npm start

# Build the server
npm run build

# Run with a Figma API token
npm start -- --figma-token YOUR_FIGMA_TOKEN
```

## 许可证

此MCP服务器根据MIT许可证发布。这意味着您可以在遵守MIT许可证条款和条件的前提下自由地使用、修改和分发该软件。更多详情，请参阅项目仓库中的LICENSE文件。

**官方网站：** [https://github.com/JayArrowz/mcp-figma](https://github.com/JayArrowz/mcp-figma)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`art and culture`, `developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`@thirdstrandstudio/mcp-figma --figma-token your_figma_api_key`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/thirdstrandstudio-figma.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
