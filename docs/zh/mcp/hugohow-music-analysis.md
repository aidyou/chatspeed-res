---
title: "MCP音乐分析工具"
description: "MCP将分析本地音频文件。"
---

# MCP音乐分析工具

MCP将分析本地音频文件。

# MCP 音乐分析

此仓库包含一个**模型上下文提供者 (MCP)**，它使用 MCP 和 [librosa](https://librosa.org/) 对本地音频、YouTube 链接或音频链接中的音频进行分析。

## 与 Claude Desktop 一起使用

   alt="alt text" width="40%">
   alt="alt text" width="40%">

## 安装

```bash
# Clone repository
git clone git@github.com:hugohow/mcp-music-analysis.git
cd mcp-music-analysis

# Create virtual environment and install
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e .
```

### 与 Claude Desktop 一起使用

#### 定位配置文件

配置文件的位置取决于您的操作系统：

- **macOS**:
```
  ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

- **Windows**:
```
  %APPDATA%\Claude\claude_desktop_config.json
```

- **Linux**:
```
  ~/.config/Claude/claude_desktop_config.json
```

在 `claude_desktop_config.json` 中添加以下内容：

```json
{
  "mcpServers": {
    "music-analysis": {
      "command": "uvx",
      "args": ["-n", "mcp-music-analysis"]
    }
  }
}
```

## 示例提示

这里是一些示例提示，您可以在服务器运行后在对话或聊天环境中使用。MCP 将理解这些请求并执行相关工具：

```
Can you analyze the beat of /Users/hugohow-choong/Desktop/sample-6s.mp3?
Could you give me the duration of https://download.samplelib.com/mp3/sample-15s.mp3 ?
Please compute the MFCC for this file: /path/to/another_audio.mp3
What are the spectral centroid values for /path/to/music.wav?
I'd like to know the onset times for https://www.youtube.com/watch?v=8HFiFd9vx1c
```

## 待办事项列表

- [x] 添加音频文件下载的 URL
- [x] 添加 YouTube 转换为音频文件
- [ ] 试验多个 Python 环境（测试中）
- [ ] 改进安装指南
- [ ] 集成 Whisper 用于歌词
- [ ] 实现 Docker 解决方案

## 作者

Hugo How-Choong

**官方网站：** [https://github.com/hugohow/mcp-audio-analysis](https://github.com/hugohow/mcp-audio-analysis)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`files`
- 标签：`file systems`, `image and video processing`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`-n mcp-music-analysis`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/hugohow-music-analysis.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
