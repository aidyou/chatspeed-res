---
title: "MCP文件系统服务器"
description: "用于文件系统操作的Go语言服务器，实现了模型上下文协议（MCP）。"
---

# MCP文件系统服务器

用于文件系统操作的Go语言服务器，实现了模型上下文协议（MCP）。

[Smithery](https://smithery.ai/server/@mark3labs/mcp-filesystem-server)

# 文件系统 MCP 服务器

实现用于文件系统操作的模型上下文协议 (MCP) 的 Go 语言服务器。

## 特性

- 读写文件
- 创建/列出/删除目录
- 移动文件/目录
- 搜索文件
- 获取文件元数据

**注意**：服务器仅允许在通过 `args` 指定的目录内进行操作。

## API

### 资源

- `file://system`: 文件系统操作接口

### 工具

- **read_file**
  - 读取文件的全部内容
  - 输入: `path` (字符串)
  - 使用 UTF-8 编码读取整个文件的内容

- **read_multiple_files**
  - 同时读取多个文件
  - 输入: `paths` (字符串数组)
  - 单个文件读取失败不会停止整个操作

- **write_file**
  - 创建新文件或覆盖现有文件（使用此功能时需谨慎）
  - 输入:
    - `path` (字符串): 文件位置
    - `content` (字符串): 文件内容

- **create_directory**
  - 创建新目录或确保其存在
  - 输入: `path` (字符串)
  - 如需要则创建父目录
  - 如果目录已存在，则静默成功

- **list_directory**
  - 列出带有 [FILE] 或 [DIR] 前缀的目录内容
  - 输入: `path` (字符串)

- **move_file**
  - 移动或重命名文件和目录
  - 输入:
    - `source` (字符串)
    - `destination` (字符串)
  - 如果目标已存在则失败

- **search_files**
  - 递归搜索文件/目录
  - 输入:
    - `path` (字符串): 起始目录
    - `pattern` (字符串): 搜索模式
  - 不区分大小写的匹配
  - 返回匹配项的完整路径

- **get_file_info**
  - 获取详细的文件/目录元数据
  - 输入: `path` (字符串)
  - 返回:
    - 大小
    - 创建时间
    - 修改时间
    - 访问时间
    - 类型 (文件/目录)
    - 权限

- **list_allowed_directories**
  - 列出服务器允许访问的所有目录
  - 无需输入
  - 返回:
    - 该服务器可以从中读取/写入的目录

## 与 Claude Desktop 一起使用
安装服务器
```bash
go install github.com/mark3labs/mcp-filesystem-server
```

将以下内容添加到您的 `claude_desktop_config.json` 中：
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "mcp-filesystem-server",
      "args": [
        "/Users/username/Desktop",
        "/path/to/other/allowed/dir"
      ]
    }
  }
}
```

## 许可证

本 MCP 服务器根据 MIT 许可证授权。这意味着您可以在遵守 MIT 许可证条款和条件的前提下自由使用、修改和分发软件。有关更多详细信息，请参阅项目存储库中的 LICENSE 文件。

**官方网站：** [https://github.com/mark3labs/mcp-filesystem-server](https://github.com/mark3labs/mcp-filesystem-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`files`
- 标签：`file systems`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`mcp-filesystem-server`
- 参数：`/Users/username/Desktop /path/to/other/allowed/dir`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/mark3labs-filesystem.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
