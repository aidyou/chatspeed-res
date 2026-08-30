---
title: "Markdown 转换器"
description: "一种将各种文件格式（PDF、文档、图像、音频、网页内容）转换为Markdown的文档转换服务器，具有改进的多语言和UTF-8支持。"
---

# Markdown 转换器

一种将各种文件格式（PDF、文档、图像、音频、网页内容）转换为Markdown的文档转换服务器，具有改进的多语言和UTF-8支持。

# Markdownify MCP Server - UTF-8 增强版

这是 [原始的 Markdownify MCP 项目](https://github.com/cursor-ai/markdownify-mcp) 的增强版本，改进了对 UTF-8 编码的支持，并优化了多语言内容的处理。

[中文文档](https://github.com/JDJR2024/markdownify-mcp-utf8/blob/HEAD/README-CN.md)

## 增强功能

- 添加了全面的 UTF-8 编码支持
- 优化了多语言内容的处理
- 修复了 Windows 系统上的编码问题
- 改进了错误处理机制

## 与原项目的主要区别

1. 增强的编码支持：
   - 在所有操作中完全支持 UTF-8
   - 正确处理中文、日文、韩文及其他非 ASCII 字符
   - 修复了特定于 Windows 的编码问题（cmd.exe 和 PowerShell 兼容性）

2. 改进的错误处理：
   - 提供英文和中文的详细错误信息
   - 更好的网络问题异常处理
   - 转换失败时的优雅回退机制

3. 扩展的功能：
   - 支持批量处理多个文件
   - 增强了 YouTube 视频字幕的处理
   - 从各种文件格式中改进了元数据提取
   - 更好地保留了文档格式

4. 性能优化：
   - 优化了大文件转换时的内存使用
   - 加快了多语言内容的处理速度
   - 减少了依赖冲突

5. 更好的开发体验：
   - 全面的调试选项
   - 详细的日志系统
   - 针对不同环境的配置支持
   - 英文和中文的清晰文档

## 功能

支持将各种文件类型转换为 Markdown：
- PDF 文件
- 图像（带元数据）
- 音频（带转录）
- Word 文档（DOCX）
- Excel 电子表格（XLSX）
- PowerPoint 演示文稿（PPTX）
- 网络内容：
  - YouTube 视频字幕
  - 搜索结果
  - 一般网页
- 已有的 Markdown 文件

## 快速开始

1. 克隆此仓库：
```bash
   git clone https://github.com/JDJR2024/markdownify-mcp-utf8.git
   cd markdownify-mcp-utf8
```

2. 安装依赖项：
```bash
   pnpm install
```
   注意：这也会安装 `uv` 及相关的 Python 依赖项。

3. 构建项目：
```bash
   pnpm run build
```

4. 启动服务器：
```bash
   pnpm start
```

## 系统要求

- Node.js 16.0 或更高版本
- Python 3.8 或更高版本
- pnpm 包管理器
- Git

## 详细安装指南

### 1. 环境设置

1. 安装 Node.js:
   - 从 [Node.js 官方网站](https://nodejs.org/) 下载
   - 验证安装: `node --version`

2. 安装 pnpm:
```bash
   npm install -g pnpm
   pnpm --version
```

3. 安装 Python:
   - 从 [Python 官方网站](https://www.python.org/downloads/) 下载
   - 确保在安装过程中将 Python 添加到 PATH
   - 验证安装: `python --version`

4. (仅限 Windows) 配置 UTF-8 支持:
```bash
   # 设置系统范围的 UTF-8
   setx PYTHONIOENCODING UTF-8
   # 设置当前会话的 UTF-8
   set PYTHONIOENCODING=UTF-8
   # 在命令提示符中启用 UTF-8
   chcp 65001
```

### 项目设置

1. 克隆仓库:
```bash
   git clone https://github.com/JDJR2024/markdownify-mcp-utf8.git
   cd markdownify-mcp-utf8
```

2. 创建并激活 Python 虚拟环境:
```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # Linux/macOS
   python3 -m venv .venv
   source .venv/bin/activate
```

3. 安装项目依赖:
```bash
   # 安装 Node.js 依赖
   pnpm install

   # 安装 Python 依赖（将由 setup.sh 处理）
   ./setup.sh
```

4. 构建项目:
```bash
   pnpm run build
```

### 验证

1. 启动服务器:
```bash
   pnpm start
```

2. 测试安装:
```bash
   # 转换网页
   python convert_utf8.py "https://example.com"

   # 转换本地文件
   python convert_utf8.py "path/to/your/file.docx"
```

## 使用指南

### 基本使用

1. 转换网页:
```bash
   python convert_utf8.py "https://example.com"
```
   转换后的 Markdown 将保存为 `converted_result.md`

2. 转换本地文件:
```bash
   # 转换 DOCX
   python convert_utf8.py "document.docx"

   # 转换 PDF
   python convert_utf8.py "document.pdf"

   # 转换 PowerPoint
   python convert_utf8.py "presentation.pptx"

   # 转换 Excel
   python convert_utf8.py "spreadsheet.xlsx"
```

3. 转换 YouTube 视频:
```bash
   python convert_utf8.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

### 高级使用

1. 环境变量:
```bash
   # 设置自定义 UV 路径
   export UV_PATH="/custom/path/to/uv"

   # 设置自定义输出目录
   export MARKDOWN_OUTPUT_DIR="/custom/output/path"
```

2. 批量处理:
   创建一个批处理文件（例如 `convert_batch.txt`），包含 URL 或文件路径:
```text
   https://example1.com
   https://example2.com
   file1.docx
   file2.pdf
```
   然后运行:
```bash
   while read -r line; do python convert_utf8.py "$line"; done < convert_batch.txt
```

### 故障排除

1. 常见问题:
   - 如果看到编码错误，请确保正确设置了 UTF-8
   - 对于 Windows 上的权限问题，请以管理员身份运行
   - 对于 Python 路径问题，请确保已激活虚拟环境

2. 调试:
```bash
   # 启用调试输出
   export DEBUG=true
   python convert_utf8.py "your_file.docx"
```

## 使用

### 命令行

将网页转换为 Markdown：
```bash
python convert_utf8.py "https://example.com"
```

转换本地文件：
```bash
python convert_utf8.py "path/to/your/file.docx"
```

### 桌面应用程序集成

要将此服务器与桌面应用程序集成，请在您的应用程序的服务器配置中添加以下内容：

```js
{
  "mcpServers": {
    "markdownify": {
      "command": "node",
      "args": [
        "{ABSOLUTE_PATH}/dist/index.js"
      ],
      "env": {
        "UV_PATH": "/path/to/uv"
      }
    }
  }
}
```

## 故障排除

1. 编码问题
   - 如果遇到字符编码问题，请确保 `PYTHONIOENCODING` 环境变量设置为 `utf-8`
   - Windows 用户可能需要运行 `chcp 65001` 以启用 UTF-8 支持

2. 权限问题
   - 确保您有足够的文件读/写权限
   - 在 Windows 上，您可能需要以管理员身份运行

## 致谢

本项目基于 Zach Caceres 的原始工作。感谢原作者的杰出贡献。

## 许可证

本项目继续使用 MIT 许可证。详情请参阅 [LICENSE](https://github.com/JDJR2024/markdownify-mcp-utf8/blob/HEAD/LICENSE) 文件。

## 贡献

欢迎贡献！在提交 Pull Request 之前，请：
1. 确保您的代码遵循项目的编码标准
2. 添加必要的测试和文档
3. 更新 README 中的相关部分

## 联系方式

对于问题或建议：
1. 提交 Issue: https://github.com/JDJR2024/markdownify-mcp-utf8/issues
2. 创建 Pull Request: https://github.com/JDJR2024/markdownify-mcp-utf8/pulls
3. 电子邮件: jdidndosmmxmx@gmail.com

**官方网站：** [https://github.com/JDJR2024/markdownify-mcp-utf8](https://github.com/JDJR2024/markdownify-mcp-utf8)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`files`
- 标签：`file systems`, `developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`{ABSOLUTE_PATH}/dist/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/jdjr2024-markdownify-utf8.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
