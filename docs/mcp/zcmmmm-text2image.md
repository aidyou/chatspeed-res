---
title: "文字转图片"
description: "一个提供文本转图像功能的模型上下文协议服务器，可将任何文本转换为美观的图像格式。"
---

# 文字转图片

一个提供文本转图像功能的模型上下文协议服务器，可将任何文本转换为美观的图像格式。

# TextImage 服务

一个提供文本转图片功能的模型上下文协议服务器，可将任意文本转换为美观的图片格式。

## 功能

- 将文本转换为1080x1080尺寸的图片
- 自动计算文字大小和居中位置
- 支持自定义字体
- 生成图片可直接保存或显示

## 安装
```bash
pip install -r requirements.txt
```

## 使用方法
### 作为命令行工具
```bash
python src/text2image/text2image.py
```

### 在 Claude 桌面版中
添加到您的 Claude 桌面配置 (claude_desktop_config.json)：
```json
{
  "mcpServers": {
    "text2image": {
      "command": "uv",
      "args": [
        "--directory", "/absolute/path/to/text2image",
        "run", "text2image.py"
      ]
    }
  }
}
```

## 可用工具
### text_to_image
将文本转换为图片

**参数**:
- `text` (字符串, 必填): 要转换为图片的文本
- `text_color` (字符串, 可选): 文字颜色，Hex格式，默认"#000000"
- `bg_color` (字符串, 可选): 背景颜色，Hex格式，默认"#FFFFFF"
- `width` (整数, 可选): 图片宽度，默认1080
- `height` (整数, 可选): 图片高度，默认1080
- `font_size` (整数, 可选): 字体大小，默认80
- `font_path` (字符串, 可选): 字体文件路径，默认'simhei.ttf'
- `texture` (字符串, 可选): 背景材质图片路径
- `output_path` (字符串, 可选): 图片保存路径，未指定时默认保存为"output.png"
- `corner_radius` (整数, 可选): 图片圆角半径，默认为0（直角）

**JSON示例请求**:
```json
{
  "text": "示例
文本(可自带换行符控制换行位置)",
  "text_color": "#FF0000",
  "bg_color": "#FFFFFF",
  "width": 800,
  "height": 600,
  "font_size": 60,
  "font_path": "arial.ttf",
  "texture": "background.jpg",
  "output_path": "custom_output.png"
}
```

**返回值**:
- PIL.Image.Image: 生成的图片对象

## 开发
```bash
# 安装依赖
pip install -r requirements.txt

# 运行服务
python src/text2image/text2image.py
```

## 许可证
MIT 许可证

## 贡献
欢迎贡献！请随时提交 Pull Request。
  "mcpServers": # TextImage 服务

**官方网站：** [https://gitee.com/zcmmmm/text2image-mcp-server](https://gitee.com/zcmmmm/text2image-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`entertainment and media`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`--directory /absolute/path/to/text2image run text2image.py`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/zcmmmm-text2image.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
