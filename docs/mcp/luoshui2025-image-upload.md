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

# Run the interactive configuration script

uv run setup_env.py

# Or check the current configuration

uv run setup_env.py check

```
#### Method Two: Manually Create .env File

1. Copy the example configuration file:
```bash
cp .env.example .env
```
2. Edit the `.env` file and fill in your actual configurations:
```env
# Image hosting API base URL (optional, default as below)
IMGBED_API_BASE=https://imgbed.deepseeking.app

# Image hosting auth code (required; fill in your actual auth code)
IMGBED_AUTH_CODE=your_actual_auth_code_here
```
#### Method Three: Set System Environment Variables

```bash

# Linux/macOS

export IMGBED_AUTH_CODE="your_actual_auth_code_here"

export IMGBED_API_BASE="https://imgbed.deepseeking.app"  # optional

# Windows

set IMGBED_AUTH_CODE=your_actual_auth_code_here

set IMGBED_API_BASE=https://imgbed.deepseeking.app

```
### 3. Project Initialization

The project has already been set up with its dependencies; you just need to run:

```bash

# Verify the installation and configuration

uv run setup_env.py check

# Start the service (for testing)

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
Please upload the screenshot.png file on my desktop
```
### 2. `upload_multiple_images` - Batch Upload

Uploads multiple image files in batch.

**Parameters:**
- `file_paths` (list[string]): A list of paths to the image files to be uploaded

**Example:**
```
Please batch upload the following files:
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
Please check whether the ~/Downloads/image.jpg file can be uploaded
```
## 📝 Usage Examples

### Basic Upload

```

User: Please help me upload the avatar.jpg file on my desktop

Assistant: [uses the upload_image tool]

Image uploaded successfully!

Original file: avatar.jpg

File size: 245760 bytes

Relative path: /file/1749257735878_avatar.jpg

Full access link: https://imgbed.deepseeking.app/file/1749257735878_avatar.jpg

You can directly use the link above to access the uploaded image.

```
### Batch Upload

```

User: Please batch upload all images in my photo folder

Assistant: [uses the upload_multiple_images tool]

Batch upload summary:

Total files: 3

Uploaded successfully: 2

Failed uploads: 1

Success rate: 66.7%

Detailed results:

[1] photo1.jpg: upload succeeded

[2] photo2.png: upload succeeded

[3] photo3.bmp: file too large

```
### File Check

```

User: Please check whether this file can be uploaded: ~/Downloads/large_image.png

Assistant: [uses the check_image_info tool]

File info check result:

File name: large_image.png

File path: /Users/username/Downloads/large_image.png

File size: 15728640 bytes (15360.0 KB)

File format: .png

MIME type: image/png

Format supported: Yes

Size check: over the limit (max 10MB)

This file cannot be uploaded

Supported formats: .bmp, .gif, .jpg, .jpeg, .png, .svg, .tif, .tiff, .webp

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
