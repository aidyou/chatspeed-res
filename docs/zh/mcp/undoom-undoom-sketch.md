---
title: "图片素描mcp"
description: "一个基于 MCP (Model Context Protocol) 的图片素描化服务器，可以将普通图片转换为多种风格的素描效果。支持单张图片转换、批量处理，以及多种自定义参数调节。 项目已发布到 PyPI，可以直接使用： - PyPI: - GitHub: - 🎨 多种素描风格：支持经典、详细、柔和三种不同的素描风格 - 📁 批量处理：支持批量转换文件夹中的所有图片 - 🖼️ 多格式支持：支持 J…"
---

# 图片素描mcp

一个基于 MCP (Model Context Protocol) 的图片素描化服务器，可以将普通图片转换为多种风格的素描效果。支持单张图片转换、批量处理，以及多种自定义参数调节。 项目已发布到 PyPI，可以直接使用： - PyPI: - GitHub: - 🎨 多种素描风格：支持经典、详细、柔和三种不同的素描风格 - 📁 批量处理：支持批量转换文件夹中的所有图片 - 🖼️ 多格式支持：支持 J…

# Undoom Sketch MCP

[![PyPI version](/mcp-assets/60b2ff0fafaa82cb0d264614759d0905.svg)](https://badge.fury.io/py/undoom-sketch-mcp)
[![License: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)

一个基于 MCP (Model Context Protocol) 的图片素描化服务器，可以将普通图片转换为多种风格的素描效果。支持单张图片转换、批量处理，以及多种自定义参数调节。

## 🌟 在线体验

项目已发布到 PyPI，可以直接使用：
- **PyPI**: [undoom-sketch-mcp](https://pypi.org/project/undoom-sketch-mcp/)
- **GitHub**: [undoom-sketch-mcp](https://github.com/kk520879/undoom-sketch-mcp)

## 功能特性

- 🎨 **多种素描风格**：支持经典、详细、柔和三种不同的素描风格
- 📁 **批量处理**：支持批量转换文件夹中的所有图片
- 🖼️ **多格式支持**：支持 JPG、PNG、BMP、GIF、TIFF、WEBP 等常见图片格式
- 🌏 **中文路径支持**：完美支持中文文件名和路径
- ⚙️ **参数可调**：可自定义模糊程度和对比度参数
- 📊 **图片信息查看**：提供图片基本信息和推荐参数

## 安装要求

- Python >= 3.13
- 依赖包：
  - mcp[cli] >= 1.12.3
  - opencv-python >= 4.8.0
  - numpy >= 1.24.0

## 🚀 快速开始

### 方法一：直接使用 uvx（推荐）

```bash

# 使用国内镜像源（推荐）

uvx --index-url https://pypi.tuna.tsinghua.edu.cn/simple undoom-sketch-mcp

# 或使用默认源

uvx undoom-sketch-mcp

```
### 方法二：通过 PyPI 安装

```bash

# 安装包

pip install undoom-sketch-mcp

# 运行服务器

python -m undoom_sketch_mcp

```
### 方法三：从源码安装

```bash

# 克隆项目

git clone https://github.com/kk520879/undoom-sketch-mcp.git

cd undoom-sketch-mcp

# 使用 uv 安装（推荐）

uv sync

# 或使用 pip

pip install -e .

```
## 📖 使用方法

### 作为 MCP 服务器使用

#### 1. 配置 MCP 客户端

创建 `mcp_config.json` 配置文件：

```json

{

  "mcpServers": {

    "undoom-sketch-mcp": {

      "command": "uvx",

      "args": [

        "--index-url",

        "https://pypi.tuna.tsinghua.edu.cn/simple",

        "undoom-sketch-mcp"

      ]

    }

  }

}

```
#### 2. 直接运行服务器

```bash

# 启动 MCP 服务器

python -m undoom_sketch_mcp

# 或使用 uvx

uvx undoom-sketch-mcp

```
### 🛠️ 可用工具

#### 1. convert_image_to_sketch - 单张图片转换

**MCP 调用示例：**
```json
{
  "tool": "convert_image_to_sketch",
  "arguments": {
    "image_path": "D:\\photos\\portrait.jpg",
    "style": "classic",
    "blur_size": 21,
    "contrast": 256.0
  }
}
```
**Python 直接调用：**
```python
from undoom_sketch_mcp.server import convert_image_to_sketch

result = convert_image_to_sketch(
    image_path="D:/photos/portrait.jpg",
    style="classic",
    blur_size=21,
    contrast=256.0
)
print(result)
```
#### 2. batch_convert_images - 批量图片转换

```python

from undoom_sketch_mcp.server import batch_convert_images

result = batch_convert_images(

    folder_path="D:/photos/",

    style="detailed",

    blur_size=21,

    contrast=256.0

)

print(result)

```
#### 3. get_image_info - 获取图片信息

```python

from undoom_sketch_mcp.server import get_image_info

info = get_image_info("D:/photos/image.jpg")

print(info)

```
### 素描风格说明

- **classic**：经典素描风格，平衡的线条和对比度
- **detailed**：详细素描风格，更清晰的线条和细节
- **soft**：柔和素描风格，更柔和的效果，适合风景图

### 参数说明

- `image_path`：图片文件的完整路径（必需）
- `blur_size`：高斯模糊核大小（3-101，必须为奇数，默认21）
- `contrast`：对比度参数（50-500，默认256.0）
- `style`：素描风格（classic/detailed/soft，默认classic）

### 参数建议

- **大图片**（>200万像素）：blur_size=31-51，contrast=200-300
- **中等图片**（50万-200万像素）：blur_size=21-31，contrast=256
- **小图片**（ 10MP | 30秒+ | blur_size=41-51 |

## 🤝 贡献指南

我们欢迎各种形式的贡献！

### 如何贡献

1. Fork 这个仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

### 报告问题

如果你发现了 bug 或有功能建议，请在 [GitHub Issues](https://github.com/kk520879/undoom-sketch-mcp/issues) 中提交。

### 开发环境设置

```bash

# 克隆仓库

git clone https://github.com/kk520879/undoom-sketch-mcp.git

cd undoom-sketch-mcp

# 安装开发依赖

uv sync --dev

# 运行测试

python -m pytest

```
## 📄 许可证

本项目采用 [MIT 许可证](https://github.com/kk520879/undoom-sketch-mcp/blob/HEAD/LICENSE)。

## 🙏 致谢

- [OpenCV](https://opencv.org/) - 强大的计算机视觉库
- [MCP](https://modelcontextprotocol.io/) - 模型上下文协议
- [FastMCP](https://github.com/jlowin/fastmcp) - 快速 MCP 实现

---

**如果这个项目对你有帮助，请给它一个 ⭐ Star！**

**官方网站：** [https://github.com/kk520879/undoom-sketch-mcp](https://github.com/kk520879/undoom-sketch-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`art and culture`, `素描化`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`--index-url https://pypi.tuna.tsinghua.edu.cn/simple undoom-sketch-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/undoom-undoom-sketch.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
