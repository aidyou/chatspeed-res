---
title: "Cursor MCP 安装器"
description: "用于Cursor IDE的模型上下文协议（MCP）服务器，可简化其他MCP服务器的安装和配置。"
---

# Cursor MCP 安装器

用于Cursor IDE的模型上下文协议（MCP）服务器，可简化其他MCP服务器的安装和配置。

# Cursor MCP 安装程序

   ___         __  __    ___  __            ___   ___ 
  / __\/\ /\  /__\/ _\  /___\/__\  /\/\    / __\ / _ \
 / /  / / \ \/ \//\ \  //  // \// /    \  / /   / /_)/
/ /___\ \_/ / _  \_\ \/ \_// _  \/ /\/\ \/ /___/ ___/ 
\____/ \___/\/ \_/\__/\___/\/ \_/\/    \/\____/\/     
                                                      
  _____    __  __  _____  _      __    __    __  __   
  \_   \/\ \ \/ _\/__   \/_\    / /   / /   /__\/__\  
   / /\/  \/ /\ \   / /\//_\\  / /   / /   /_\ / \//  
/\/ /_/ /\  / _\ \ / / /  _  \/ /___/ /___//__/ _  \  
\____/\_\ \/  \__/ \/  \_/ \_/\____/\____/\__/\/ \_/  

+---------------------------------------------+
| 🚀 CURSOR MCP INSTALLER 🚀                 |
| ✨ 轻松魔幻安装MCP服务器 ✨                  |
+---------------------------------------------+

  
一个用于在Cursor IDE中安装和配置其他MCP服务器的模型上下文协议（MCP）服务器。

  
  [![License: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)
  [![npm version](/mcp-assets/29a0b0e56cf9e0b0777f127388314059.svg)](https://www.npmjs.com/package/cursor-mcp-installer-free)
  [![MCP Compatible](/mcp-assets/4d2db09f8c33956073a63b9d84264fc0.svg)](https://github.com/anthropic-labs/model-context-protocol)
  [![Cursor IDE](/mcp-assets/102bff546638934e4bc403af21a70287.svg)](https://cursor.sh)
  [![npm downloads](/mcp-assets/810b2cb940621247fb255926882d4580.svg)](https://www.npmjs.com/package/cursor-mcp-installer-free)
  
  

    

  

> **📢 现已在NPM上可用！** 使用简单的`npm install -g cursor-mcp-installer-free`命令进行安装，或者直接使用`npx cursor-mcp-installer-free`或`uvx cursor-mcp-installer-free`！

> **🔄 最新更新 (v0.1.3):** 改进了所有MCP服务器安装的路径处理、更好的OpenAPI模式检测以及在本地目录中更强大的服务器发现。感谢[@ItzAmirreza](https://github.com/ItzAmirreza)提交了初始安装路径处理问题。详情请参阅CHANGELOG.md。

## 快速入门指南

### 第一步：添加到Cursor配置

选择以下方法之一将MCP Installer添加到您的Cursor配置：

#### 使用npx（最简单 - 不需要安装）

将此内容添加到您的`~/.cursor/mcp.json`文件中（如果不存在则创建它）：

```json
{
  "mcpServers": {
    "MCP Installer": {
      "command": "npx",
      "type": "stdio",
      "args": [
        "cursor-mcp-installer-free@0.1.3",
        "index.mjs"
      ]
    }
  }
}
```

#### 使用npm（全局安装）

```bash
npm install -g cursor-mcp-installer-free@0.1.3
```

然后添加到您的`~/.cursor/mcp.json`：

```json
{
  "mcpServers": {
    "MCP Installer": {
      "command": "cursor-mcp-installer-free",
      "type": "stdio",
      "args": [
        "index.mjs"
      ]
    }
  }
}
```

### 第二步：重启Cursor

关闭并重新打开Cursor以应用配置更改。

### 第三步：使用Claude安装服务器

让Claude为您安装任何MCP服务器：

```
Install the web search MCP server
```

或

```
Install the MCP server for OpenAPI schema exploration with my-schema.yaml
```

### 第四步：安装后的显示

一旦正确安装并重启Cursor，在使用Claude时您将在侧边栏看到可用的MCP Installer：

 alt="MCP Installer Interface" width="500"/>

MCP 安装程序提供了三个主要工具：
- `install_repo_mcp_server`: 从 npm 包或仓库安装 MCP 服务器
- `install_local_mcp_server`: 从本地目录安装 MCP 服务器
- `add_to_cursor_config`: 添加自定义的 MCP 服务器配置

## 功能

- 从 npm 包安装 MCP 服务器
- 从本地目录安装 MCP 服务器
- 为 Cursor 配置 MCP 服务器
- 添加自定义的 MCP 服务器配置

## 前提条件

在使用此工具之前，您需要安装以下软件：

- [Node.js](https://nodejs.org/)（用于 npm 包）
- [Cursor IDE](https://cursor.sh/)

## 安装

有几种方法可以安装和使用 Cursor MCP 安装程序：

### 1. 使用 npm（推荐）

```bash
npm install -g cursor-mcp-installer-free@0.1.3
```

安装完成后，将其添加到您的 Cursor MCP 配置文件中：

```json
{
  "mcpServers": {
    "MCP Installer": {
      "command": "cursor-mcp-installer-free",
      "type": "stdio",
      "args": [
        "index.mjs"
      ]
    }
  }
}
```

### 2. 使用 npx（无需全局安装）

您可以使用 npx 运行包而无需全局安装：

```json
{
  "mcpServers": {
    "MCP Installer": {
      "command": "npx",
      "type": "stdio",
      "args": [
        "cursor-mcp-installer-free@0.1.3",
        "index.mjs"
      ]
    }
  }
}
```

### 3. 直接从 GitHub

克隆仓库并在本地构建：

```bash
# Clone the repository
git clone https://github.com/matthewdcage/cursor-mcp-installer.git
cd cursor-mcp-installer

# Install dependencies and build
npm install
npm run build
```

然后配置 Cursor 以使用您的本地安装：

```json
{
  "mcpServers": {
    "MCP Installer": {
      "command": "node",
      "type": "stdio",
      "args": [
        "/path/to/cursor-mcp-installer/lib/index.mjs"
      ]
    }
  }
}
```

将 `/path/to/cursor-mcp-installer` 替换为您实际克隆仓库的路径。

### Cursor MCP 配置文件在哪里？

Cursor MCP 配置文件位于：

- **macOS/Linux**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`

如果该文件不存在，您可以根据上述任何一种安装方法创建它。

## v0.1.3 版本中的路径处理改进

版本 0.1.3 引入了对 MCP 服务器安装路径处理的重大改进：

### 增强的路径解析
- 正确地规范化相对路径和绝对路径
- 处理包含空格和特殊字符的路径
- 确保不同操作系统之间的一致路径格式

### 更好的模式检测
- 现在扫描所有参数中的模式文件，而不仅仅是第一个
- 支持更多模式文件扩展名 (.yaml, .yml, .json, .openapi)
- 在传递给服务器之前正确地规范化模式文件路径

### 改进的服务器发现
- 增加了对本地目录中常见服务器入口点的检测
- 增强了对基于 Python 的 MCP 服务器的支持
- 对路径相关问题提供更好的错误报告

这些改进使 MCP 安装程序在处理各种类型的服务器安装时更加健壮，特别是在处理自定义文件路径、OpenAPI 模式和本地目录安装时。

## 使用

安装完成后，您可以使用 Claude 或 Cursor 与 MCP 安装程序交互。以下是一些示例提示：

### 从 npm 包安装 MCP 服务器

```
Install the MCP server named mcp-server-fetch
```

### 带参数安装

```
Install the @modelcontextprotocol/server-filesystem package as an MCP server. Use ['/home/user/documents'] for the arguments
```

### 从本地目录安装 MCP 服务器

```
Install the MCP server at /home/user/projects/my-mcp-server
```

### 使用环境变量安装

```
```

**官方网站：** [https://github.com/matthewdcage/cursor-mcp-installer](https://github.com/matthewdcage/cursor-mcp-installer)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `os automation`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`cursor-mcp-installer-free@0.1.3 index.mjs`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/matthewdcage-cursor-installer.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
