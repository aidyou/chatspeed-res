---
title: "MCP文件管理服务器"
description: "一个MCP服务器，允许克劳德AI在指定的允许路径内执行文件系统操作，包括读取、写入、列出、移动文件和搜索目录。"
---

# MCP文件管理服务器

一个MCP服务器，允许克劳德AI在指定的允许路径内执行文件系统操作，包括读取、写入、列出、移动文件和搜索目录。

# 文件系统 MCP 服务器

一个为 Claude AI 提供文件系统操作的模型上下文协议 (MCP) 服务器。

## 功能

此 MCP 服务器提供以下文件系统操作：

1. **read_file**: 读取文件的完整内容
   - 输入: `path` (字符串)
   - 以 UTF-8 编码读取整个文件内容

2. **read_multiple_files**: 同时读取多个文件
   - 输入: `paths` (字符串数组)
   - 失败的读取不会停止整个操作

3. **write_file**: 创建新文件或覆盖现有文件
   - 输入:
     - `path` (字符串): 文件位置
     - `content` (字符串): 文件内容

4. **create_directory**: 创建新目录或确保其存在
   - 输入: `path` (字符串)
   - 如果需要，创建父目录
   - 如果目录已存在，则静默成功

5. **list_directory**: 列出目录内容，并带有 [FILE] 或 [DIR] 前缀
   - 输入: `path` (字符串)

6. **move_file**: 移动或重命名文件和目录
   - 输入:
     - `source` (字符串)
     - `destination` (字符串)
   - 如果目标已存在则失败

7. **search_files**: 递归搜索文件/目录
   - 输入:
     - `path` (字符串): 起始目录
     - `pattern` (字符串): 搜索模式
   - 匹配不区分大小写
   - 返回匹配项的完整路径

8. **get_file_info**: 获取详细的文件/目录元数据
   - 输入: `path` (字符串)
   - 返回:
     - 大小
     - 创建时间
     - 修改时间
     - 访问时间
     - 类型 (文件/目录)
     - 权限

9. **list_allowed_directories**: 列出服务器允许访问的所有目录
   - 不需要输入
   - 返回服务器可以从中读取/写入的目录

## 安全性

服务器仅允许在通过命令行参数指定的目录内进行操作。

## 安装

1. 克隆此仓库
2. 安装依赖: `npm install`
3. 构建项目: `npm run build`

## 使用

使用一个或多个允许的目录运行服务器：

```bash
node build/index.js /path/to/allowed/dir1 /path/to/allowed/dir2
```

## MCP 配置

将服务器添加到您的 MCP 配置文件中：

```json
{
  "mcpServers": {
    "filesystem-server": {
      "command": "node",
      "args": [
        "/path/to/filesystem-server/build/index.js",
        "/path/to/allowed/dir1",
        "/path/to/allowed/dir2"
      ],
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

## 许可证

ISC

**官方网站：** [https://github.com/ai-yliu/filesystem-mcp-server](https://github.com/ai-yliu/filesystem-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`files`
- 标签：`file systems`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`/path/to/filesystem-server/build/index.js /path/to/allowed/dir1 /path/to/allowed/dir2`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/ai-yliu-filesystem.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
