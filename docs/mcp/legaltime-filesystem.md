---
title: "Legaltime文件系统工具"
description: "实现用于文件系统操作的模型上下文协议的 Node.js 服务器，允许 Claude 在指定位置读取、写入和操作文件及目录。"
---

# Legaltime文件系统工具

实现用于文件系统操作的模型上下文协议的 Node.js 服务器，允许 Claude 在指定位置读取、写入和操作文件及目录。

# 文件系统 MCP 服务器

Node.js 服务器实现用于文件系统操作的模型上下文协议 (MCP)。

## 功能

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
  - 以 UTF-8 编码读取整个文件的内容

- **read_multiple_files**
  - 同时读取多个文件
  - 输入: `paths` (字符串数组)
  - 读取失败不会停止整个操作

- **write_file**
  - 创建新文件或覆盖现有文件（使用时需谨慎）
  - 输入:
    - `path` (字符串): 文件位置
    - `content` (字符串): 文件内容

- **edit_file**
  - 使用高级模式匹配和格式化进行选择性编辑
  - 特性:
    - 基于行和多行内容匹配
    - 保留缩进的空白字符规范化
    - 带置信度评分的模糊匹配
    - 多个同时编辑，正确定位
    - 识别并保留缩进风格
    - 带上下文的 Git 风格差异输出
    - 通过干运行模式预览更改
    - 通过置信度评分调试失败的匹配
  - 输入:
    - `path` (字符串): 要编辑的文件
    - `edits` (数组): 编辑操作列表
      - `oldText` (字符串): 要搜索的文本（可以是子字符串）
      - `newText` (字符串): 替换为的文本
    - `dryRun` (布尔值): 不应用更改的情况下预览更改（默认: false）
    - `options` (对象): 可选的格式设置
      - `preserveIndentation` (布尔值): 保持现有缩进（默认: true）
      - `normalizeWhitespace` (布尔值): 在保持结构的同时规范化空格（默认: true）
      - `partialMatch` (布尔值): 启用模糊匹配（默认: true）
  - 返回详细的差异和匹配信息用于干运行，否则应用更改
  - 最佳实践: 总是先使用 dryRun 预览更改，然后再应用它们

- **create_directory**
  - 创建新目录或确保其存在
  - 输入: `path` (字符串)
  - 如需要则创建父目录
  - 如果目录已存在则静默成功

- **list_directory**
  - 列出目录内容，并带有 [FILE] 或 [DIR] 前缀
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
    - `excludePatterns` (字符串数组): 排除任何模式。支持 Glob 格式。
  - 匹配不区分大小写
  - 返回匹配项的完整路径

- **get_file_info**
  - 获取文件/目录的详细元数据
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
    - 该服务器可以读/写的目录

## 与 Claude Desktop 一起使用
将以下内容添加到您的 `claude_desktop_config.json` 中：

```json
{
  // 这里添加配置内容
}
```

注意：您可以通过将目录挂载到 `/projects` 来为服务器提供沙箱目录。添加 `ro` 标志将使服务器对该目录只读。

### Docker
注意：默认情况下，所有目录都必须挂载到 `/projects`。

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "--mount", "type=bind,src=/Users/username/Desktop,dst=/projects/Desktop",
        "--mount", "type=bind,src=/path/to/other/allowed/dir,dst=/projects/other/allowed/dir,ro",
        "--mount", "type=bind,src=/path/to/file.txt,dst=/projects/path/to/file.txt",
        "mcp/filesystem",
        "/projects"
      ]
    }
  }
}
```

### NPX

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/username/Desktop",
        "/path/to/other/allowed/dir"
      ]
    }
  }
}
```

## 构建

Docker 构建：

```bash
docker build -t mcp/filesystem -f src/filesystem/Dockerfile .
```

## 许可证

此 MCP 服务器根据 MIT 许可证授权。这意味着您可以自由使用、修改和分发该软件，但须遵守 MIT 许可证的条款和条件。更多详情，请参阅项目仓库中的 LICENSE 文件。

**官方网站：** [https://github.com/Legaltime/filesystem](https://github.com/Legaltime/filesystem)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`files`
- 标签：`file systems`, `developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @modelcontextprotocol/server-filesystem /Users/username/Desktop /path/to/other/allowed/dir`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/legaltime-filesystem.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
