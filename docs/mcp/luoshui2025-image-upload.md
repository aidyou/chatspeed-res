---
title: "image-upload-mcp"
description: "A model context protocol (MCP) based image upload service that supports uploading image files to a specified image hosting service and returns an accessible URL link."
---

# image-upload-mcp

A model context protocol (MCP) based image upload service that supports uploading image files to a specified image hosting service and returns an accessible URL link.

# Image Upload MCP Service

An image upload service based on the Model Context Protocol (MCP) that supports uploading image files to a specified image hosting service and returns accessible URL links.

## 🚀 Features

- ✅ **Multi-format Support**: Supports mainstream image formats such as JPG, JPEG, PNG, GIF, BMP, WebP, SVG, TIFF
- ✅ **Batch Upload**: Supports uploading multiple image files simultaneously
- ✅ **File Validation**: Automatically checks file format, size, and validity
- ✅ **Error Handling**: Provides detailed error messages and upload status feedback
- ✅ **Security Limits**: File size limit is 10MB to prevent abuse
- ✅ **User-friendly Interface**: Uses emojis and formatted output for a clear user experience

## 🛠️ Installation and Configuration

### 1. Environment Requirements

- Python 3.12+
- uv package manager

### 2. Environment Variable Configuration

To protect your personal information, this service uses environment variables to configure sensitive information:

#### Method One: Using the Configuration Helper Script (Recommended)

```bash

# 运行交互式配置脚本

uv run setup_env.py

# 或检查当前配置

uv run setup_env.py check

```
#### Method Two: Manually Create .env File

1. Copy the example configuration file:
```bash
cp .env.example .env
```
2. Edit the `.env` file and fill in your actual configurations:
```env
# 图床 API 基础 URL (可选，默认值如下)
IMGBED_API_BASE=https://imgbed.deepseeking.app

# 图床授权码 (必需，请填写您的实际授权码)
IMGBED_AUTH_CODE=your_actual_auth_code_here
```
#### Method Three: Set System Environment Variables

```bash

# Linux/macOS

export IMGBED_AUTH_CODE="your_actual_auth_code_here"

export IMGBED_API_BASE="https://imgbed.deepseeking.app"  # 可选

# Windows

set IMGBED_AUTH_CODE=your_actual_auth_code_here

set IMGBED_API_BASE=https://imgbed.deepseeking.app

```
### 3. Project Initialization

The project has already been set up with its dependencies; you just need to run:

```bash

# 验证安装和配置

uv run setup_env.py check

# 启动服务（用于测试）

uv run image_upload.py

```
### 4. Configure MCP Service in Cursor

Add the following content to the MCP configuration in Cursor:

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
> **Note**: Please replace the path `/Users/luoshui/Documents/Cursor/MCP/image-upload-mcp` with your actual project path.

## 📋 Available Tools

### 1. `upload_image` - Single File Upload

Uploads a single image file to the image hosting server.

**Parameters:**
- `file_path` (string): The full path of the image file to be uploaded

**Example:**
```
请上传我桌面上的 screenshot.png 文件
```
### 2. `upload_multiple_images` - Batch Upload

Uploads multiple image files in batch.

**Parameters:**
- `file_paths` (list[string]): A list of paths to the image files to be uploaded

**Example:**
```
请批量上传以下文件：
- ~/Pictures/photo1.jpg
- ~/Pictures/photo2.png
- ~/Pictures/photo3.gif
```
### 3. `check_image_info` - File Information Check

Checks the basic information of an image file to verify if it can be uploaded.

**Parameters:**
- `file_path` (string): The path of the image file to be checked

**Example:**
```
请检查 ~/Downloads/image.jpg 文件是否可以上传
```
## 📝 Usage Examples

### Basic Upload

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
### Batch Upload

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
### File Check

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
## 🔧 Technical Details

### Supported Image Formats

- `.jpg`, `.jpeg` - JPEG images
- `.png` - PNG images
- `.gif` - GIF animations
- `.bmp` - Windows bitmap
- `.webp` - Google WebP format
- `.svg` - Scalable Vector Graphics
- `.tiff`, `.tif` - TIFF images

### File Restrictions

- **Maximum File Size**: 10MB
- **Concurrent Uploads**: Supports batch uploads but processes each file sequentially
- **Timeout Setting**: 60 seconds timeout for each upload request

### API Integration

This service uses the following image hosting API:

- **Upload Endpoint**: `https://imgbed.deepseeking.app/upload?authCode={authCode}`
- **Base Access URL**: `https://imgbed.deepseeking.app`
- **Request Method**: POST (multipart/form-data)
- **Authentication Method**: authCode in the URL parameters

## 🐛 Error Handling

The service provides detailed error messages:

| Error Type | Description | Solution |
|------------|-------------|----------|
| File Not Found | The specified file path is invalid | Check if the file path is correct |
| Unsupported Format | The file format is not in the supported list | Convert to a supported format |
| File Too Large | The file exceeds the 10MB limit | Compress the image or choose a smaller file |
| Network Error | Network anomaly during the upload process | Check the network connection and retry |
| Server Error | Abnormal response from the image hosting server | Retry later or contact the service provider |

## 🔒 Security Considerations

- File size limits to prevent abuse
- Strict format validation to prevent malicious file uploads
- Network request timeouts to prevent long-term blocking
- Detailed error logs for troubleshooting

## 📞 Technical Support

If you encounter any issues, please check:

1. ✅ Whether the file path is correct
2. ✅ Whether the file format is supported
3. ✅ Whether the file size is within the limit
4. ✅ Whether the network connection is normal
5. ✅ Whether the MCP service configuration is correct

---

**Developer**: Built using the FastMCP framework**Version**: 1.0.0  
**Protocol**: MCP (Model Context Protocol)  
**Transport Method**: stdio

**Official site: ** [https://github.com/luoshui-coder/image-upload-mcp.git](https://github.com/luoshui-coder/image-upload-mcp.git)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `files`
- Tags: `file systems`, `entertainment and media`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uv`
- Args: `--directory /Users/luoshui/Documents/Cursor/MCP/image-upload-mcp run image_upload.py`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/luoshui2025-image-upload.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
