---
title: "图片视频生成"
description: "集成阿里云百炼平台通义万相模型实现文生图和文生视频功能"
---

# 图片视频生成

集成阿里云百炼平台通义万相模型实现文生图和文生视频功能

# Media Generator MCP Server

集成阿里云百炼平台通义万相模型实现文生图和文生视频功能。

## 功能

### 1. 生成图片 (`generate_image`)

根据文本描述生成图片。

**参数：**
- `prompt` (必填): 图片文本描述
- `negative_prompt` (可选): 不希望在图片中出现的内容描述
- `size` (可选): 图片尺寸，可选值：
  - 1024*1024 (默认)
  - 720*1280
  - 1280*720
  - 768*1152
  - 1152*768
  - 512*512
  - 1440*1440
- `n` (可选): 生成图片数量，1-4，默认1
- `seed` (可选): 随机种子，用于生成可重复的结果
- `prompt_extend` (可选): 是否启用提示词智能改写，默认true
- `watermark` (可选): 是否添加AI生成水印，默认false

### 2. 生成视频 (`generate_video`)

根据文本描述生成视频。

**参数：**
- `prompt` (必填): 视频文本描述
- `negative_prompt` (可选): 不希望在视频中出现的内内容描述
- `size` (可选): 视频分辨率，可选值：
  - 1920*1080 (默认，1080P横屏)
  - 1080*1920 (1080P竖屏)
  - 1440*1440 (1080P方形)
  - 1632*1248 (1080P 4:3)
  - 1248*1632 (1080P 3:4)
  - 1280*720 (720P横屏)
  - 720*1280 (720P竖屏)
  - 960*960 (720P方形)
  - 1088*832 (720P 4:3)
  - 832*1088 (720P 3:4)
  - 832*480 (480P横屏)
  - 480*832 (480P竖屏)
  - 624*624 (480P方形)
- `model` (可选): 视频模型，可选值：
  - wan2.2-t2v-plus (默认)
  - wanx2.1-t2v-turbo
  - wanx2.1-t2v-plus
- `seed` (可选): 随机种子，用于生成可重复的结果
- `prompt_extend` (可选): 是否启用提示词智能改写，默认true
- `watermark` (可选): 是否添加AI生成水印，默认false


## 示例

### 生成图片
生成一张猫的图片：
```json
{
  "prompt": "一只可爱的橘猫坐在窗台上晒太阳",
  "size": "1024*1024"
}
```

### 生成视频
生成一只小猫在月光下奔跑的视频：
```json
{
  "prompt": "一只小猫在月光下奔跑，水墨画风格，背景是古色古香的中式庭院",
  "size": "1920*1080",
  "model": "wan2.2-t2v-plus"
}
```

## MCP服务配置

### Claude Desktop 配置
在 `claude_desktop_config.json` 中添加：

```json
{
  "mcpServers": {
    "media-gen": {
      "command": "npx",
      "args": ["-y", "media-gen-mcp"],
      "env": {
        "DASHSCOPE_API_KEY": "你的DashScope_API密钥"
      }
    }
  }
}
```

### Cursor 配置
在 `.cursor/mcp.json` 中添加：

```json
{
  "mcpServers": {
    "media-gen": {
      "command": "npx",
      "args": ["-y", "media-gen-mcp"],
      "env": {
        "DASHSCOPE_API_KEY": "你的DashScope_API密钥"
      }
    }
  }
}
```

### VS Code 配置
在 `settings.json` 中添加：

```json
{
  "mcp": {
    "servers": {
      "media-gen": {
        "command": "npx",
        "args": ["-y", "media-gen-mcp"],
        "env": {
          "DASHSCOPE_API_KEY": "你的DashScope_API密钥"
        }
      }
    }
  }
}
```

### HTTP模式使用
如需通过HTTP使用，先运行：
```bash
npm run build
npm start stream
```

然后配置MCP客户端连接到 `http://localhost:8080`

**官方网站：** [https://github.com/weiwei162/MediaGenMCP.git](https://github.com/weiwei162/MediaGenMCP.git)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y media-gen-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/weiwei162-mediagenmcp.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
