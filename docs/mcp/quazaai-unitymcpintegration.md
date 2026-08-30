---
title: "Unity AI桥接服务"
description: "一种服务器，它使人工智能助手能够实时理解并与Unity项目互动，提供对场景层次结构、项目设置的访问，并能够在Unity编辑器中直接执行代码。"
---

# Unity AI桥接服务

一种服务器，它使人工智能助手能够实时理解并与Unity项目互动，提供对场景层次结构、项目设置的访问，并能够在Unity编辑器中直接执行代码。

# 🚀 高级 Unity MCP 集成

[![MCP](/mcp-assets/4ac9d1cb3d9e4c6281ed9c3ef4fdeb70.svg)](https://modelcontextprotocol.io/introduction)
[Smithery](https://smithery.ai/server/@quazaai/unitymcpintegration)
[![Unity](/mcp-assets/7f09525df44b518fff9bc7f6d91f242b.svg)](https://unity.com)
[![Node.js](/mcp-assets/86837d3edb1c91af41de4016c858edda.svg)](https://nodejs.org)
[![TypeScript](/mcp-assets/03500effbf23a69c818017a47f3da738.svg)](https://www.typescriptlang.org)
[![WebSockets](/mcp-assets/9f61a0ada231ddbb474fbe97f3d70b4b.svg)](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)

[![Stars](/mcp-assets/f1ac8d13fab3e12d896778ffab59549c.svg)](https://github.com/quazaai/UnityMCPIntegration/stargazers)
[![Forks](/mcp-assets/eac4d6eec7e3b730931b041a26b0af0b.svg)](https://github.com/quazaai/UnityMCPIntegration/network/members)
[![License](/mcp-assets/5816f652aa1f0cc4eedb21a2f733e09e.svg)](https://github.com/quazaai/UnityMCPIntegration/blob/main/LICENSE)

   alt="Unity MCP 检视器" width="400" align="right" style="margin-left: 20px; margin-bottom: 20px;"/>

此包提供了 [模型上下文协议 (MCP)](https://modelcontextprotocol.io/) 与 Unity 编辑器之间的无缝集成，使 AI 助手能够实时理解和交互您的 Unity 项目。通过这种集成，AI 助手可以访问关于您的场景层次结构、项目设置的信息，并直接在 Unity 编辑器环境中执行代码。

## 📚 特性
- 直接浏览和操作项目文件
- 访问有关您的 Unity 项目的实时信息
- 理解您的场景层次结构和游戏对象
- 直接在 Unity 编辑器中执行 C# 代码
- 监控日志和错误
- 控制编辑器的播放模式
- 等待代码执行

## 🚀 入门指南

### 前提条件

- Unity 2021.3 或更高版本
- Node.js 18+（用于运行 MCP 服务器）

### 安装

#### 1. 安装 Unity 包

您有几种选项来安装 Unity 包：

**选项 A：包管理器（Git URL）**
1. 打开 Unity 包管理器 (`Window > Package Manager`)
2. 单击 `+` 按钮并选择 `Add package from git URL...`
3. 输入仓库 URL: `https://github.com/quazaai/UnityMCPIntegration.git`
4. 单击 `Add`

**选项 B：导入自定义包**
1. 克隆此仓库或 [下载为 unityPackage](https://github.com/quazaai/UnityMCPIntegration/releases)
2. 在 Unity 中，转到 `Assets > Import Package > Custom Package`
3. 选择 `UnityMCPIntegration.unitypackage` 文件

#### 2. 设置 MCP 服务器

您有两种选项来运行 MCP 服务器：

**选项 A：直接运行服务器**

1. 导航到 `mcpServer (可能位于 
\Library\PackageCache\com.quaza.unitymcp@d2b8f1260bca\mcpServer\)` 目录
2. 安装依赖项：
```
   npm install
```
3. 运行服务器：
```
   node build/index.js
```

**选项 B：添加到 MCP 主机配置**

将服务器添加到您的 MCP 主机配置中，适用于 Claude Desktop、自定义实现等

```json
{
  "mcpServers": {
    "unity-mcp-server": {
      "command": "node",
      "args": [
        "path-to-project>\\Library\\PackageCache\\com.quaza.unitymcp@d2b8f1260bca\\mcpServer\\mcpServer\\build\\index.js"
      ],
      "env": {
        "MCP_WEBSOCKET_PORT": "5010"
      }
    }
  }
}
```
### 演示视频

[Watch video](https://www.youtube.com/watch?v=GxTlahBXs74)

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@quazaai/unitymcpintegration) 自动安装 Unity MCP Integration for Claude Desktop：

```bash
npx -y @smithery/cli install @quazaai/unitymcpintegration --client claude
```

### 🔧 使用方法

#### 调试和监控

您可以在 Unity 中打开 MCP 调试窗口来监控连接并测试功能：

1. 转到 `Window > MCP Debug`
2. 使用调试窗口：
   - 检查连接状态
   - 测试代码执行
   - 查看日志
   - 监控事件

#### 可用工具

Unity MCP 集成提供了多种工具给 AI 助手使用：

##### Unity 编辑器工具
- **get_editor_state**: 获取有关 Unity 项目和编辑器状态的全面信息
- **get_current_scene_info**: 获取当前场景的详细信息
- **get_game_objects_info**: 获取场景中特定 GameObject 的信息
- **execute_editor_command**: 在 Unity 编辑器中直接执行 C# 代码
- **get_logs**: 检索并过滤 Unity 控制台日志
- **verify_connection**: 检查是否与 Unity 编辑器有活动连接

##### 文件系统工具
- **read_file**: 读取 Unity 项目中文件的内容
- **read_multiple_files**: 一次性读取多个文件
- **write_file**: 创建或覆盖带有新内容的文件
- **edit_file**: 对现有文件进行有针对性的编辑，并提供差异预览
- **list_directory**: 列出目录中的文件和文件夹
- **directory_tree**: 获取目录和文件的分层视图
- **search_files**: 查找匹配搜索模式的文件
- **get_file_info**: 获取特定文件或目录的元数据
- **find_assets_by_type**: 查找所有特定类型的资源（例如 Material, Prefab）
- **list_scripts**: 获取项目中所有 C# 脚本的列表

文件路径可以是绝对路径，也可以是相对于 Unity 项目 Assets 文件夹的相对路径。例如，`"Scenes/MyScene.unity"` 指的是 `
/Assets/Scenes/MyScene.unity`。

## 🛠️ 架构

该集成由两个主要组件组成：

1. **Unity 插件 (C#)**: 位于 Unity 编辑器中，提供对编辑器 API 的访问
2. **MCP 服务器 (TypeScript/Node.js)**: 实现 MCP 协议并与 Unity 插件通信

它们之间的通信通过 WebSocket 进行，传输 JSON 消息以执行命令和数据交换。

## 文件系统访问

Unity MCP 集成现在包括强大的文件系统工具，允许 AI 助手：

- 浏览、读取和编辑 Unity 项目中的文件
- 创建新的文件和目录
- 搜索特定文件或资源类型
- 分析项目结构
- 通过差异预览进行有针对性的代码更改

所有文件操作都限制在 Unity 项目目录内以确保安全。系统智能地处理绝对路径和相对路径，始终将它们解析为相对于项目的 Assets 文件夹，以便于使用。

示例用法：

- 获取目录列表：`list_directory(path: "Scenes")`
- 读取脚本文件：`read_file(path: "Scripts/Player.cs")`
- 编辑配置文件：`edit_file(path: "Resources/config.json", edits: [{oldText: "value: 10", newText: "value: 20"}], dryRun: true)`
- 查找所有材质：`find_assets_by_type(assetType: "Material")`

## 👥 贡献

欢迎贡献！以下是如何贡献的方法：

1. 叉出仓库
2. 创建一个功能分支 (`git checkout -b feature/amazing-feature`)
3. 进行你的更改
4. 提交你的更改 (`git commit -m 'Add some amazing feature'`)
5. 推送到该分支 (`git push origin feature/amazing-feature`)
6. 打开一个拉取请求

### 开发设置

**Unity 端**：
- 在 Unity 中打开项目
- 修改 `UnityMCPConnection/Editor` 目录下的 C# 脚本

**服务器端**：
- 导航到 `mcpServer` 目录
- 安装依赖项：`npm install`
- 对 `src` 目录下的 TypeScript 文件进行修改
- 构建服务器：`npm run build`
- 运行服务器：`node build/index.js`

## 📄 许可证

此项目根据 MIT 许可证发布 - 详情请参阅 LICENSE 文件。

## 📞 支持

如果您遇到任何问题或有疑问，请在 GitHub 仓库中提交一个问题。

**官方网站：** [https://github.com/quazaai/UnityMCPIntegration](https://github.com/quazaai/UnityMCPIntegration)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`files`
- 标签：`developer tools`, `file systems`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`path-to-project>\Library\PackageCache\com.quaza.unitymcp@d2b8f1260bca\mcpServer\mcpServer\build\index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/quazaai-unitymcpintegration.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
