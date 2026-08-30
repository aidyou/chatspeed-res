---
title: "mcp-file-preview HTML预览分析工具"
description: "提供HTML文件的预览和分析功能。该服务器能够捕获本地HTML文件的全页截图并分析其结构。"
---

# mcp-file-preview HTML预览分析工具

提供HTML文件的预览和分析功能。该服务器能够捕获本地HTML文件的全页截图并分析其结构。

# MCP 文件预览服务器

一个提供 HTML 文件预览和分析功能的模型上下文协议 (MCP) 服务器。该服务器能够捕获本地 HTML 文件的全页面截图并分析其结构。

## 功能

- **文件预览**：捕获带有适当 CSS 样式的 HTML 文件全页面截图
- **内容分析**：分析 HTML 结构（标题、段落、图片、链接）
- **本地文件支持**：处理本地文件路径和资源
- **截图管理**：将截图保存到专用目录

## 安装

1. 克隆仓库：
```bash
git clone https://github.com/your-username/mcp-file-preview.git
cd mcp-file-preview
```

2. 安装依赖项：
```bash
npm install
```

3. 构建项目：
```bash
npm run build
```

## 配置

将服务器添加到您的 Claude 或 Cline MCP 设置中：

### Claude 桌面应用程序
添加到 `~/Library/Application Support/Claude/claude_desktop_config.json`：
```json
{
  "mcpServers": {
    "file-preview": {
      "command": "node",
      "args": ["/path/to/mcp-file-preview/build/index.js"]
    }
  }
}
```

### Cline VSCode 扩展
添加到 VSCode 的 MCP 设置中：
```json
{
  "mcpServers": {
    "file-preview": {
      "command": "node",
      "args": ["/path/to/mcp-file-preview/build/index.js"]
    }
  }
}
```

## 使用

服务器提供了两个主要工具：

### preview_file
捕获截图并返回 HTML 内容：
```typescript

file-preview
preview_file

{
  "filePath": "/path/to/file.html",
  "width": 1024,  // optional
  "height": 768   // optional
}

```

截图将保存在项目文件夹中的 `screenshots/` 目录下。

### analyze_content
分析 HTML 结构：
```typescript

file-preview
analyze_content

{
  "filePath": "/path/to/file.html"
}

```

返回以下各项的计数：
- 标题
- 段落
- 图片
- 链接

## 开发

1. 安装依赖项：
```bash
npm install @modelcontextprotocol/sdk puppeteer typescript @types/node @types/puppeteer
```

2. 在 `src/` 中进行修改
3. 构建：
```bash
npm run build
```
4. 本地测试：
```bash
npm run dev
```

## 实现细节

服务器使用 MCP SDK 的 Server 类进行适当的初始化：

```typescript
this.server = new Server(
  // Metadata object
  {
    name: 'file-preview-server',
    version: '0.1.0'
  },
  // Options object with capabilities
  {
    capabilities: {
      tools: {
        preview_file: {
          description: 'Preview local HTML file and capture screenshot',
          inputSchema: {
            // ... schema definition
          }
        }
      }
    }
  }
);
```

要点：
- 服务器构造函数接受单独的元数据和选项对象
- 工具在 capabilities.tools 中声明
- 每个工具需要描述和 inputSchema
- 截图保存到本地 `screenshots/` 目录

## 调试

1. 使用 MCP Inspector：
```bash
npx @modelcontextprotocol/inspector
```

2. 连接方式：
   - 传输类型：STDIO
   - 命令：node
   - 参数：/path/to/build/index.js

3. 如果工具未出现在下拉菜单中，请检查 Claude OS 日志

## 贡献

请阅读 [CONTRIBUTING.md](https://github.com/seanivore/mcp-file-preview/blob/HEAD/CONTRIBUTING.md) 以了解我们的行为准则以及提交拉取请求的流程。

## 许可证

该项目根据 MIT 许可证获得许可 - 有关详细信息，请参阅 [LICENSE](https://github.com/seanivore/mcp-file-preview/blob/HEAD/LICENSE) 文件。

**官方网站：** [https://github.com/seanivore/mcp-file-preview](https://github.com/seanivore/mcp-file-preview)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`files`
- 标签：`file systems`, `browser automation`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`/path/to/mcp-file-preview/build/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/seanivore-file-preview.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
