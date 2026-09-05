---
title: "文档处理工具"
description: "提供全面的文档处理功能，包括读取、转换和操作各种文档格式，具有先进的文本和HTML处理能力。"
---

# 文档处理工具

提供全面的文档处理功能，包括读取、转换和操作各种文档格式，具有先进的文本和HTML处理能力。

# 简单文档处理 MCP 服务器
[Smithery](https://smithery.ai/server/@cablate/mcp-doc-forge)

一个强大的模型上下文协议（MCP）服务器，提供全面的文档处理能力。

## 功能

### 文档阅读器
- 阅读 DOCX、PDF、TXT、HTML、CSV

### 文档转换
- DOCX 转 HTML/PDF
- HTML 转 TXT/Markdown
- PDF 操作（合并、拆分）

### 文本处理
- 多编码转换支持（UTF-8、Big5、GBK）
- 文本格式化和清理
- 文本比较和差异生成
- 按行或分隔符分割文本

### HTML 处理
- HTML 清理和格式化
- 资源提取（图片、链接、视频）
- 保留结构的转换

## 安装

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@cablate/mcp-doc-forge) 自动为 Claude Desktop 安装文档处理服务器：

```bash
npx -y @smithery/cli install @cablate/mcp-doc-forge --client claude
```

### 手动安装
```bash
npm install -g @cablate/mcp-doc-forge
```

## 使用方法

### 命令行界面

```bash
mcp-doc-forge
```

### 与 [Dive Desktop](https://github.com/OpenAgentPlatform/Dive) 一起使用

1. 在 Dive Desktop 中点击“+ 添加 MCP 服务器”
2. 复制并粘贴此配置：

```json
{
  "mcpServers": {
    "searxng": {
      "command": "npx",
      "args": [
        "-y",
        "@cablate/mcp-doc-forge"
      ],
      "enabled": true
    }
  }
}
```

3. 点击“保存”以安装 MCP 服务器

## 许可证

MIT

## 贡献

欢迎社区参与和贡献！以下是贡献方式：

- ⭐️ 如果你觉得项目有用，请给它加星标
- 🐛 提交问题：报告问题或提供建议
- 🔧 创建拉取请求：提交代码改进

## 联系方式

如果你有任何问题或建议，随时联系我们：

- 📧 电子邮件: [reahtuoo310109@gmail.com](mailto:reahtuoo310109@gmail.com)
- 📧 GitHub: [CabLate](https://github.com/cablate/)
- 🤝 合作：欢迎讨论项目合作
- 📚 技术指导：诚挚欢迎建议和技术指导

**官方网站：** [https://github.com/cablate/mcp-doc-forge](https://github.com/cablate/mcp-doc-forge)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`productivity`
- 标签：`other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @cablate/mcp-doc-forge`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/cablate-doc-forge.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
