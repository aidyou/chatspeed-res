---
title: "飞影数字人"
description: "一种模型上下文协议服务器，能够为广泛使用的数字形象快速且免费地创建口型同步视频，同时支持音频和文本输入以生成同步的口型动作。"
---

# 飞影数字人

一种模型上下文协议服务器，能够为广泛使用的数字形象快速且免费地创建口型同步视频，同时支持音频和文本输入以生成同步的口型动作。

# Flyworks MCP：免费且快速的零镜头口型同步工具

  

    

  

  

    

  

### 概述

Flyworks MCP 是一个模型上下文协议（MCP）服务器，提供了一个方便的接口来与 Flyworks API 进行交互。它为各种数字头像（包括逼真和卡通风格）提供了快速且免费的口型同步视频创建。

### 演示

输入头像视频（素材）：

   

带有 TTS 语音的音频片段，内容为 `我是一个飞影数字人。欢迎来到 Flyworks MCP 服务器演示。此工具可为各种数字头像（包括逼真和卡通风格）提供快速且免费的口型同步视频创建。`：

生成的口型同步视频：

### 特性

- 使用数字头像视频和音频作为输入来创建口型同步视频
- 更多功能即将推出...

### 要求

- Python 3.8+
- 依赖项：`httpx`, `mcp[cli]`

### 安装

1. 克隆此仓库：
```bash
   git clone https://github.com/yourusername/flyworks-mcp.git
   cd flyworks-mcp
```

2. 安装依赖项：
```bash
   pip install httpx "mcp[cli]>=1.6.0"
```
   
   或者使用 `uv`：
```bash
   uv pip install httpx "mcp[cli]>=1.6.0"
```

   为了避免在服务器启动时出现超时问题，我们建议预先安装所有依赖项：
```bash
   pip install pygments pydantic-core httpx "mcp[cli]>=1.6.0"
```

### 配置

将您的 Flyworks API 令牌设置为环境变量：

```bash
# Linux/macOS
export FLYWORKS_API_TOKEN="your_token_here"

# Windows (Command Prompt)
set FLYWORKS_API_TOKEN=your_token_here

# Windows (PowerShell)
$env:FLYWORKS_API_TOKEN="your_token_here"
```

或者，您也可以创建一个 `.env` 文件。

> **注意：** 我们提供的试用访问权限使用令牌 `2aeda3bcefac46a3`。但请注意，该免费访问的日配额是有限的。此外，生成的视频将会被加上水印，并且限制为 45 秒以内。如需完全访问，请联系 bd@flyworks.ai 获取您的令牌。

### 使用方法

#### 运行服务器

直接运行 `server.py` 文件：

```bash
python server.py
```

#### 与 Claude 或其他 MCP 客户端集成

##### 在 Claude 桌面版中使用

由于原文档中的 #0 和 #1 处未提供具体命令，翻译中保留了这些占位符。如果需要具体的命令，请根据实际文档内容进行补充。

1. 使用 `mcp` 工具安装服务器：
```bash
   mcp install /path/to/server.py
```

2. 在 Claude Desktop 的配置文件中添加服务器配置：
   编辑 `claude_desktop_config.json` 文件并添加以下内容：

```json
   {
     "mcpServers": {
       "flyworks": {
         "command": "python",
         "args": ["/path/to/server.py"],
         "env": {
           "FLYWORKS_API_TOKEN": "your_api_token_here"
         }
       }
     }
   }
```

##### 在 Cursor 中使用

将以下内容添加到 Cursor MCP 配置中：

```json
{
  "mcpServers": {
    "flyworks": {
      "command": "python",
      "args": ["/path/to/server.py"],
      "env": {
        "FLYWORKS_API_TOKEN": "your_api_token_here"
      }
    }
  }
}
```

### 工具描述

#### 1. 创建口型同步视频 (`create_lipsync_video`)

创建一个数字虚拟人物的口型同步视频。输入是一个数字虚拟人物的视频和一个音频文件，输出是一个与音频长度相同的口型同步视频。

**参数**:
- `video_url`: 视频文件 URL，对于基于视频的创作是必需的，支持 mp4, mov 格式
- `audio_url`: 音频文件 URL，对于基于音频的创作是必需的，支持 mp3, m4a, wav 格式

**返回**:
- `job_id`: 视频创作任务的 ID

#### 2. 检查任务状态 (`inspect_job_status`)

查询视频创作的状态。如果成功，则返回可下载的视频 URL。

**参数**:
- `job_id`: 任务 ID，必需。在创建作品时返回。

**响应参数**:
- `message`: 字符串，失败时返回的错误消息
- `code`: 整数，失败时的错误代码
- `status`: 整数，任务状态，1: 等待中，2: 处理中，3: 完成，4: 失败
- `video_Url`: URL，生成的视频的 URL。这是一个临时 URL，请及时保存。URL 包含查询参数，在下载时请确保兼容性。
- `duration`: 整数，视频的持续时间（秒）
- `request_id`: 字符串，请求码

### 注意事项

- 任务处理可能需要一些时间，请耐心等待
- 视频文件 URL 是临时的，请及时下载并保存

### 相关链接

- [Flyworks AI 开放平台文档](https://api.lingverse.co/hifly.html)
- [模型上下文协议 (MCP) 文档](https://modelcontextprotocol.io/llms-full.txt)
- [Python MCP SDK](https://github.com/modelcontextprotocol/python-sdk)

**官方网站：** [https://github.com/Flyworks-AI/flyworks-mcp](https://github.com/Flyworks-AI/flyworks-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`entertainment and media`, `multimedia-processing`, `speech-processing`, `audio-processing`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`flyworks-mcp -y`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/flyworks-ai-flyworks.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
