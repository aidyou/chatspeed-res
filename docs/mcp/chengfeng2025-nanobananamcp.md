---
title: "NanoBananaMCP"
description: "Gemini MCP 是一个基于 Google Gemini 2.0 Flash 模型的 MCP（Model Context Protocol）服务器，专门用于图像分析和处理。它可以无缝集成到 Claude Desktop、Cursor 等支持 MCP 协议的 AI 助手中，提供强大的视觉理解能力。 - 多模态分析：支持图片内容理解、场景识别、文字提取等 - 灵活输入：支持本地文件路径、网络 UR…"
---

# NanoBananaMCP

Gemini MCP 是一个基于 Google Gemini 2.0 Flash 模型的 MCP（Model Context Protocol）服务器，专门用于图像分析和处理。它可以无缝集成到 Claude Desktop、Cursor 等支持 MCP 协议的 AI 助手中，提供强大的视觉理解能力。 - 多模态分析：支持图片内容理解、场景识别、文字提取等 - 灵活输入：支持本地文件路径、网络 UR…

# Gemini MCP - 基于 Gemini 的智能图像分析服务

## 项目概述

Gemini MCP 是一个基于 Google Gemini 2.0 Flash 模型的 MCP（Model Context Protocol）服务器，专门用于图像分析和处理。它可以无缝集成到 Claude Desktop、Cursor 等支持 MCP 协议的 AI 助手中，提供强大的视觉理解能力。

## 核心特性

### 🎯 主要功能
- **多模态分析**：支持图片内容理解、场景识别、文字提取等
- **灵活输入**：支持本地文件路径、网络 URL、Base64 编码等多种图片输入方式
- **流式响应**：实时流式输出分析结果，提升用户体验
- **智能存储**：自动保存处理结果和生成的图片

### 🚀 技术优势
- **零依赖安装**：支持 uvx 直接运行，无需预先安装
- **跨平台兼容**：支持 macOS、Windows、Linux 等主流操作系统
- **代理支持**：内置 SOCKS5 代理支持，适应各种网络环境
- **标准协议**：完全符合 MCP 规范，可与任何 MCP 客户端集成

## 快速开始

### API 密钥获取方式

1. **兔子 API**：访问 [兔子API充值平台](https://api.tu-zi.com/topup) 购买兼容官方格式的 API 服务（国内直连，无需梯子，完全兼容 Gemini 官方 API 接口）

### 方式一：使用 uvx 运行（推荐）

无需安装，直接运行：

```bash
# 设置 API 密钥并启动服务
GEMINI_API_KEY=your-api-key uvx gemini-mcp
```

### 方式二：通过 pip 安装

```bash
# 安装包
pip install gemini-mcp

# 运行服务
GEMINI_API_KEY=your-api-key gemini-mcp
```

### 方式三：从源码运行

```bash
# 克隆仓库
git clone https://github.com/chengfeng2025/gemini-mcp-python.git
cd gemini-mcp-python

# 安装依赖
pip install -r requirements.txt

# 运行服务
python -m gemini_mcp
```

## 客户端配置

### Claude Desktop 配置

1. 打开配置文件：
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`

2. 添加以下配置：

```json
{
  "mcpServers": {
    "gemini": {
      "command": "uvx",
      "args": [
        "gemini-mcp"
      ],
      "env": {
        "GEMINI_API_KEY": "API",
        "GEMINI_MCP_OUTPUT_DIR": "指定下载目录,可不填"
      }
    }
  }
}
```

### Cursor 配置

编辑 `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "gemini": {
      "command": "uvx",
      "args": ["gemini-mcp"],
      "env": {
        "GEMINI_API_KEY": "your-api-key"
      }
    }
  }
}
```

## 使用示例

在配置好的 Claude Desktop 或 Cursor 中，你可以：

```
# 分析本地图片
请分析这张图片：/Users/name/Pictures/photo.jpg

# 分析网络图片
描述一下这个图片的内容：https://example.com/image.png

# 提取图片中的文字
提取图片中的所有文字：/path/to/document.png

# 场景理解
这张图片是在什么场景下拍摄的？/path/to/scene.jpg
```

## 高级配置

### 环境变量

| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| `GEMINI_API_KEY` | Gemini API 密钥（必需） | - |
| `OUTPUT_DIR` | 输出文件保存目录 | `./outputs` |
| `ALL_PROXY` | SOCKS5 代理地址 | - |
| `LOG_LEVEL` | 日志级别 | `INFO` |

### 命令行参数

```bash
# 查看所有可用参数
gemini-mcp --help

# 以 HTTP 服务模式运行
gemini-mcp --mode http --port 8080

# 启用调试模式
gemini-mcp --debug

# 指定输出目录
gemini-mcp --output-dir /custom/path
```

## API 参考

### 支持的工具

#### `analyze_image`
分析图片内容并返回描述。

**参数：**
- `image_input`: 图片输入（文件路径、URL 或 Base64）
- `prompt`: 分析提示词（可选）

**示例：**
```python
{
  "tool": "analyze_image",
  "arguments": {
    "image_input": "/path/to/image.jpg",
    "prompt": "描述这张图片中的主要内容"
  }
}
```

## 开发指南

### 本地开发

```bash
# 克隆项目
git clone https://github.com/chengfeng2025/gemini-mcp-python.git
cd gemini-mcp-python

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装开发依赖
pip install -e ".[dev]"

# 运行测试
pytest tests/
```

### 贡献代码

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 故障排除

### 常见问题

**Q: 提示 "API key not found"**
A: 确保已正确设置 `GEMINI_API_KEY` 环境变量。

**Q: 连接超时错误**
A: 检查网络连接，或配置代理：
```bash
ALL_PROXY=socks5://127.0.0.1:1080 gemini-mcp
```

**Q: Claude Desktop 无法识别服务**
A: 重启 Claude Desktop 应用以重新加载配置。

## 项目信息

- **作者**: chengfeng2025
- **许可证**: MIT
- **版本**: 1.0.0
- **更新时间**: 2025年1月
- **GitHub**: [gemini-mcp-python](https://github.com/chengfeng2025/gemini-mcp-python)

## 相关链接

- [MCP 协议规范](https://modelcontextprotocol.io/)
- [Gemini API 文档](https://ai.google.dev/gemini-api/docs)
- [问题反馈](https://github.com/chengfeng2025/gemini-mcp-python/issues)

## 许可证

本项目采用 MIT 许可证。详见 [LICENSE](https://github.com/Ceeon/gemini-mcp/blob/HEAD/LICENSE) 文件。

---

**注意**：使用本项目需要有效的 Gemini API 密钥。

**Official site: ** [https://github.com/Ceeon/gemini-mcp](https://github.com/Ceeon/gemini-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `entertainment and media`, `gemini`, `生图`, `图片`, `google`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `gemini-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/chengfeng2025-nanobananamcp.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
