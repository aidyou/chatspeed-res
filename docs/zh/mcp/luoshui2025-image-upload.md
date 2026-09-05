---
title: "图像上传MCP服务"
description: "一个基于模型上下文协议 (MCP) 的图像上传服务，支持将图像文件上传到指定图床并返回可访问的 URL 链接。"
---

# 图像上传MCP服务

一个基于模型上下文协议 (MCP) 的图像上传服务，支持将图像文件上传到指定图床并返回可访问的 URL 链接。

# 图像上传 MCP 服务 (Image Upload MCP Service)

一个基于模型上下文协议 (MCP) 的图像上传服务，支持将图像文件上传到指定图床并返回可访问的 URL 链接。

## 🚀 功能特性

- ✅ **多格式支持**: 支持 JPG, JPEG, PNG, GIF, BMP, WebP, SVG, TIFF 等主流图像格式
- ✅ **批量上传**: 支持同时上传多个图像文件
- ✅ **文件验证**: 自动检查文件格式、大小和有效性
- ✅ **错误处理**: 提供详细的错误信息和上传状态反馈
- ✅ **安全限制**: 文件大小限制为 10MB，防止滥用
- ✅ **友好界面**: 使用 emoji 和格式化输出提供清晰的用户体验

## 🛠️ 安装和配置

### 1. 环境要求

- Python 3.12+
- uv 包管理器

### 2. 环境变量配置

为了保护您的个人信息，本服务使用环境变量来配置敏感信息：

#### 方法一：使用配置助手脚本（推荐）

```bash
# 运行交互式配置脚本
uv run setup_env.py

# 或检查当前配置
uv run setup_env.py check
```

#### 方法二：手动创建 .env 文件

1. 复制示例配置文件：
```bash
cp .env.example .env
```

2. 编辑 `.env` 文件，填入您的实际配置：
```env
# 图床 API 基础 URL (可选，默认值如下)
IMGBED_API_BASE=https://imgbed.deepseeking.app

# 图床授权码 (必需，请填写您的实际授权码)
IMGBED_AUTH_CODE=your_actual_auth_code_here
```

#### 方法三：设置系统环境变量

```bash
# Linux/macOS
export IMGBED_AUTH_CODE="your_actual_auth_code_here"
export IMGBED_API_BASE="https://imgbed.deepseeking.app"  # 可选

# Windows
set IMGBED_AUTH_CODE=your_actual_auth_code_here
set IMGBED_API_BASE=https://imgbed.deepseeking.app
```

### 3. 项目初始化

项目已经配置好依赖项，您只需运行：

```bash
# 验证安装和配置
uv run setup_env.py check

# 启动服务（用于测试）
uv run image_upload.py
```

### 4. 在 Cursor 中配置 MCP 服务

在 Cursor 的 MCP 配置中添加以下内容：

```json
{
    "mcpServers": {
        "image-upload": {
            "command": "uv",
            "args": [
                "--directory",
                "/Users/luoshui/Documents/Cursor/MCP/image-upload-mcp",
                "run",
                "image_upload.py"
            ]
        }
    }
}
```

> **注意**: 请将路径 `/Users/luoshui/Documents/Cursor/MCP/image-upload-mcp` 替换为您的实际项目路径。

## 📋 可用工具

### 1. `upload_image` - 单文件上传

上传单个图像文件到图床服务器。

**参数:**
- `file_path` (string): 要上传的图像文件的完整路径

**示例:**
```
请上传我桌面上的 screenshot.png 文件
```

### 2. `upload_multiple_images` - 批量上传

批量上传多个图像文件。

**参数:**
- `file_paths` (list[string]): 要上传的图像文件路径列表

**示例:**
```
请批量上传以下文件：
- ~/Pictures/photo1.jpg
- ~/Pictures/photo2.png
- ~/Pictures/photo3.gif
```

### 3. `check_image_info` - 文件信息检查

检查图像文件的基本信息，验证是否可以上传。

**参数:**
- `file_path` (string): 要检查的图像文件路径

**示例:**
```
请检查 ~/Downloads/image.jpg 文件是否可以上传
```

## 📝 使用示例

### 基本上传

```
用户: 请帮我上传桌面上的 avatar.jpg 文件

助手: [使用 upload_image 工具]
✅ 图像上传成功！

原始文件: avatar.jpg
文件大小: 245760 bytes
相对路径: /file/1749257735878_avatar.jpg
完整访问链接: https://imgbed.deepseeking.app/file/1749257735878_avatar.jpg

您可以直接使用上述链接访问上传的图像。
```

### 批量上传

```
用户: 请批量上传我照片文件夹中的所有图片

助手: [使用 upload_multiple_images 工具]
📊 批量上传完成汇总:
总文件数: 3
成功上传: 2
失败上传: 1
成功率: 66.7%

详细结果:
[1] ✅ photo1.jpg: 上传成功
[2] ✅ photo2.png: 上传成功
[3] ❌ photo3.bmp: 文件太大
```

### 文件检查

```
用户: 请检查这个文件是否可以上传：~/Downloads/large_image.png

助手: [使用 check_image_info 工具]
📋 文件信息检查结果:

文件名: large_image.png
文件路径: /Users/username/Downloads/large_image.png
文件大小: 15728640 bytes (15360.0 KB)
文件格式: .png
MIME 类型: image/png

✅ 格式支持: 是
✅ 大小检查: 超出限制 (最大10MB)

🔴 该文件不能上传

支持的格式: .bmp, .gif, .jpg, .jpeg, .png, .svg, .tif, .tiff, .webp
```

## 🔧 技术详情

### 支持的图像格式

- `.jpg`, `.jpeg` - JPEG 图像
- `.png` - PNG 图像
- `.gif` - GIF 动图
- `.bmp` - Windows 位图
- `.webp` - Google WebP 格式
- `.svg` - 可缩放矢量图形
- `.tiff`, `.tif` - TIFF 图像

### 文件限制

- **最大文件大小**: 10MB
- **并发上传**: 支持批量上传，但会按顺序处理每个文件
- **超时设置**: 每个上传请求 60 秒超时

### API 集成

本服务使用以下图床 API：

- **上传接口**: `https://imgbed.deepseeking.app/upload?authCode={authCode}`
- **访问基础URL**: `https://imgbed.deepseeking.app`
- **请求方式**: POST (multipart/form-data)
- **认证方式**: URL 参数中的 authCode

## 🐛 错误处理

服务提供详细的错误信息：

| 错误类型 | 描述 | 解决方案 |
|---------|------|---------|
| 文件不存在 | 指定的文件路径无效 | 检查文件路径是否正确 |
| 格式不支持 | 文件格式不在支持列表中 | 转换为支持的格式 |
| 文件过大 | 文件超过 10MB 限制 | 压缩图像或选择较小的文件 |
| 网络错误 | 上传过程中网络异常 | 检查网络连接并重试 |
| 服务器错误 | 图床服务器响应异常 | 稍后重试或联系服务提供商 |

## 🔒 安全考虑

- 文件大小限制防止滥用
- 严格的格式验证防止恶意文件上传
- 网络请求超时防止长时间阻塞
- 详细的错误日志便于问题排查

## 📞 技术支持

如遇到问题，请检查：

1. ✅ 文件路径是否正确
2. ✅ 文件格式是否支持
3. ✅ 文件大小是否在限制内
4. ✅ 网络连接是否正常
5. ✅ MCP 服务配置是否正确

---

**开发者**: 基于 FastMCP 框架构建  
**版本**: 1.0.0  
**协议**: MCP (Model Context Protocol)  
**传输方式**: stdio

**官方网站：** [https://github.com/luoshui-coder/image-upload-mcp.git](https://github.com/luoshui-coder/image-upload-mcp.git)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`files`
- 标签：`file systems`, `entertainment and media`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`--directory /Users/luoshui/Documents/Cursor/MCP/image-upload-mcp run image_upload.py`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/luoshui2025-image-upload.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
