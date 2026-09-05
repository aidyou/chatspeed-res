---
title: "Figma智能助手"
description: "一个MCP服务器集成，使Cursor AI能够与Figma通信，允许用户通过自然语言命令以编程方式读取和修改设计。"
---

# Figma智能助手

一个MCP服务器集成，使Cursor AI能够与Figma通信，允许用户通过自然语言命令以编程方式读取和修改设计。

# Cursor 与 Figma MCP 通信

该项目实现了 Cursor AI 和 Figma 之间的 Model Context Protocol (MCP) 集成，允许 Cursor 读取设计并在程序上修改它们。

[https://github.com/user-attachments/assets/129a14d2-ed73-470f-9a4c-2240b2a4885c](https://github.com/user-attachments/assets/129a14d2-ed73-470f-9a4c-2240b2a4885c)

## 项目结构

- `src/talk_to_figma_mcp/` - 用于 Figma 集成的 TypeScript MCP 服务器
- `src/cursor_mcp_plugin/` - 用于与 Cursor 通信的 Figma 插件
- `src/socket.ts` - 促进 MCP 服务器和 Figma 插件之间通信的 WebSocket 服务器

## 开始使用

1. 如果你还没有安装 Bun，请先安装：

```bash
curl -fsSL https://bun.sh/install | bash
```

2. 运行设置脚本，这也会在你的 Cursor 当前项目中安装 MCP

```bash
bun setup
```

3. 启动 WebSocket 服务器

```bash
bun socket
```

4. 启动 MCP 服务器

```bash
bunx cursor-talk-to-figma-mcp
```

5. 安装 [Figma 插件](#figma-plugin)

# 快速视频教程

[LinkedIn post](https://www.linkedin.com/posts/sonnylazuardi_just-wanted-to-share-my-latest-experiment-activity-7307821553654657024-yrh8)

## 手动设置和安装

### MCP 服务器：与 Cursor 的集成

将服务器添加到你的 Cursor MCP 配置文件 `~/.cursor/mcp.json` 中：

```json
{
  "mcpServers": {
    "TalkToFigma": {
      "command": "bunx",
      "args": ["cursor-talk-to-figma-mcp"]
    }
  }
}
```

### WebSocket 服务器

启动 WebSocket 服务器：

```bash
bun socket
```

### Figma 插件

1. 在 Figma 中，转到插件 > 开发 > 新建插件
2. 选择“链接现有插件”
3. 选择 `src/cursor_mcp_plugin/manifest.json` 文件
4. 现在该插件应该可以在你的 Figma 开发插件列表中找到

## Windows + WSL 指南

1. 通过 PowerShell 安装 bun

```bash
powershell -c "irm bun.sh/install.ps1|iex"
```

2. 在 `src/socket.ts` 中取消注释主机名 `0.0.0.0`

```typescript
// uncomment this to allow connections in windows wsl
hostname: "0.0.0.0",
```

3. 启动 websocket

```bash
bun socket
```

## 使用方法

1. 启动 WebSocket 服务器
2. 在 Cursor 中安装 MCP 服务器
3. 打开 Figma 并运行 Cursor MCP 插件
4. 通过使用 `join_channel` 加入频道来连接插件到 WebSocket 服务器
5. 使用 Cursor 通过 MCP 工具与 Figma 通信

## MCP 工具

MCP 服务器提供了以下工具来与 Figma 交互：

### 文档与选择

- `get_document_info` - 获取当前 Figma 文档的信息
- `get_selection` - 获取当前选中的信息
- `get_node_info` - 获取特定节点的详细信息
- `get_nodes_info` - 通过提供一个节点 ID 数组来获取多个节点的详细信息

### 创建元素

- `create_rectangle` - 创建一个新的矩形，指定位置、大小和可选名称
- `create_frame` - 创建一个新的框架，指定位置、大小和可选名称
- `create_text` - 创建一个新的文本节点，并自定义字体属性

### 修改文本内容

- `set_text_content` - 设置现有文本节点的文本内容

### 样式

- `set_fill_color` - 设置节点的填充颜色（RGBA）
- `set_stroke_color` - 设置节点的描边颜色和粗细
- `set_corner_radius` - 设置节点的圆角半径，并可选地控制每个角

### 布局与组织

- `move_node` - 将节点移动到新位置
- `resize_node` - 用新尺寸调整节点大小
- `delete_node` - 删除节点
- `clone_node` - 创建现有节点的副本，并可选地设置位置偏移

### 组件与样式

- `get_styles` - 获取关于本地样式的相关信息
- `get_local_components` - 获取关于本地组件的相关信息
- `get_team_components` - 获取关于团队组件的相关信息
- `create_component_instance` - 创建一个组件实例

### 导出与高级功能

- `export_node_as_image` - 将节点导出为图像（PNG、JPG、SVG 或 PDF）
- `execute_figma_code` - 在 Figma 中执行任意 JavaScript 代码（谨慎使用）

### 连接管理

- `join_channel` - 加入特定频道以与 Figma 通信

## 开发

### 构建 Figma 插件

1. 导航到 Figma 插件目录：

```
   cd src/cursor_mcp_plugin
```

2. 编辑 code.js 和 ui.html 文件

## 最佳实践

在使用 Figma MCP 时：

1. 在发送命令之前始终先加入一个频道
2. 首先使用 `get_document_info` 获取文档概览
3. 在进行修改前，使用 `get_selection` 检查当前选择
4. 根据需要使用适当的创建工具：
   - 使用 `create_frame` 创建容器
   - 使用 `create_rectangle` 创建基本形状
   - 使用 `create_text` 创建文本元素
5. 使用 `get_node_info` 验证更改
6. 尽可能使用组件实例以保持一致性
7. 适当处理错误，因为所有命令都可能抛出异常

## 许可证

MIT

**官方网站：** [https://github.com/sonnylazuardi/cursor-talk-to-figma-mcp](https://github.com/sonnylazuardi/cursor-talk-to-figma-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`art and culture`, `image and video processing`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`bunx`
- 参数：`cursor-talk-to-figma-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/sonnylazuardi-cursor-talk-to-figma.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
