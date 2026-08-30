---
title: "视频分析MCP"
description: "Aigroup Video MCP Aigroup Video MCP 是一个基于阿里云 DashScope 的视频多模态理解 MCP（Model Context Protocol）服务器，提供强大的视频内容分析功能。 🌟 特性 - 🎥 视频内容分析：支持通过 URL 或本地路径分析视频内容 - 🧠 智能摘要：自动生成视频摘要和关键信息 - 🎬 场景识别：识别视频中的主要场景和场景转换 - ✨ 自定义提示词：支持灵活的自定义分析需求 - 🔌 MCP 协议支持：完全兼容 MCP 协议，支持 stdio 和 SSE 模"
---

# 视频分析MCP

Aigroup Video MCP Aigroup Video MCP 是一个基于阿里云 DashScope 的视频多模态理解 MCP（Model Context Protocol）服务器，提供强大的视频内容分析功能。 🌟 特性 - 🎥 视频内容分析：支持通过 URL 或本地路径分析视频内容 - 🧠 智能摘要：自动生成视频摘要和关键信息 - 🎬 场景识别：识别视频中的主要场景和场景转换 - ✨ 自定义提示词：支持灵活的自定义分析需求 - 🔌 MCP 协议支持：完全兼容 MCP 协议，支持 stdio 和 SSE 模

# Aigroup Video MCP

Aigroup Video MCP 是一个基于阿里云 DashScope 的视频多模态理解 MCP（Model Context Protocol）服务器，提供强大的视频内容分析功能。

[![Python](/mcp-assets/d52fa8fd608496fb7cb57d905d36fafc.svg)](https://python.org)
[![License](/mcp-assets/5816f652aa1f0cc4eedb21a2f733e09e.svg)](https://github.com/jackdark425/aigroup-video-mcp/blob/HEAD/LICENSE)
[![MCP](/mcp-assets/5723e6b7b8950ac8c07587ca6cf6e73a.svg)](https://modelcontextprotocol.io)

## 🌟 特性

- **🎥 视频内容分析**：支持通过 URL 或本地路径分析视频内容
- **🧠 智能摘要**：自动生成视频摘要和关键信息
- **🎬 场景识别**：识别视频中的主要场景和场景转换
- **✨ 自定义提示词**：支持灵活的自定义分析需求
- **🔌 MCP 协议支持**：完全兼容 MCP 协议，支持 stdio 和 SSE 模式
- **⚡ 高性能处理**：基于异步处理，支持并发请求
- **📊 使用统计**：内置使用统计和监控功能
- **🛡️ 安全配置**：支持域名白名单、文件大小限制等安全特性

## 🎯 核心功能

### 视频分析工具

- **analyze_video**: 基础视频内容分析
- **summarize_video**: 视频摘要生成（支持简要、详细、通用三种模式）
- **analyze_video_scenes**: 视频场景分析和转换检测
- **analyze_video_custom**: 自定义提示词视频分析
- **validate_video_source**: 视频源验证和检查

### 系统资源

- **config://system**: 系统配置信息
- **models://available**: 可用模型信息
- **status://system**: 系统状态和健康检查
- **stats://usage**: 使用统计和分析报告

## 🚀 快速开始

### 环境要求

- Python 3.8+
- DashScope API Key

### 安装

```bash
# 克隆项目
git clone https://github.com/jackdark425/aigroup-video-mcp.git
cd aigroup-video-mcp

# 安装依赖
pip install -r requirements.txt

# 或使用 pip 安装
pip install aigroup-video-mcp
```

### 配置

1. 复制环境变量示例文件：

```bash
cp .env.example .env
```

2. 编辑 `.env` 文件，设置你的 DashScope API Key：

```bash
DASHSCOPE_API_KEY=your_dashscope_api_key_here
```

3. 或者直接设置环境变量：

```bash
export DASHSCOPE_API_KEY=your_dashscope_api_key_here
```

### 运行服务器

#### MCP 模式（默认）

```bash
# 使用 stdio 传输模式（推荐用于 MCP 客户端）
python -m aigroup_video_mcp.main serve
```

#### SSE 模式

```bash
# 使用 SSE 传输模式（用于 HTTP 客户端）
python -m aigroup_video_mcp.main serve --transport sse --host 0.0.0.0 --port 3001
```

## 📖 使用示例

### 命令行工具

#### 分析视频文件

```bash
# 基础视频分析
python -m aigroup_video_mcp.main analyze video.mp4

# 使用自定义提示词
python -m aigroup_video_mcp.main analyze video.mp4 --prompt "请分析视频中的人物动作和表情"

# 输出为 JSON 格式
python -m aigroup_video_mcp.main analyze video.mp4 --format json --save-to result.json
```

#### 健康检查

```bash
# 检查服务器健康状态
python -m aigroup_video_mcp.main health

# 查看服务器信息
python -m aigroup_video_mcp.main info

# 验证配置
python -m aigroup_video_mcp.main config
```

### RooCode MCP 客户端集成

如果你正在开发 MCP 客户端，可以通过以下方式集成：
DASHSCOPE_API_KEY直接在环境变量中设置
```json
{
  "mcpServers": {
    "aigroup-video-mcp": {
      "command": "python",
      "args": [
        "-m",
        "aigroup_video_mcp.main",
        "serve"
      ],
      "env": {
        "DASHSCOPE_API_KEY": "${env:DASHSCOPE_API_KEY}"
      },
      "alwaysAllow": [
        "analyze_video",
        "summarize_video",
        "analyze_video_scenes",
        "analyze_video_custom",
        "validate_video_source"
      ],
      "disabled": false
    }
  }
}
```

### Python API

```python
import asyncio
from aigroup_video_mcp.core.analyzer import get_analyzer, create_video_source

async def analyze_video():
    # 创建分析器
    analyzer = get_analyzer(async_mode=True)
    
    # 创建视频源
    video_source = create_video_source("path/to/video.mp4")
    
    # 分析视频
    result = await analyzer.analyze(
        video_source, 
        "请描述这个视频的主要内容"
    )
    
    if result.success:
        print(result.content)
    else:
        print(f"分析失败: {result.error}")

# 运行
asyncio.run(analyze_video())
```

## 🛠️ 工具详细说明

### analyze_video

基础视频内容分析工具。

**参数：**
- `video_path` (必需): 视频文件路径或 URL
- `prompt` (可选): 自定义分析提示词
- `model` (可选): 使用的模型名称
- `temperature` (可选): 文本生成温度 (0.0-2.0)
- `max_tokens` (可选): 最大响应 token 数

**示例：**
```json
{
  "video_path": "https://example.com/video.mp4",
  "prompt": "请分析这个视频的内容，包括主要场景、人物、动作和事件。",
  "temperature": 0.7,
  "max_tokens": 2000
}
```

### summarize_video

视频摘要生成工具。

**参数：**
- `video_path` (必需): 视频文件路径或 URL
- `summary_type` (可选): 摘要类型 (`general`, `detailed`, `brief`)
- `model` (可选): 使用的模型名称
- `temperature` (可选): 文本生成温度
- `max_tokens` (可选): 最大响应 token 数

### analyze_video_scenes

视频场景分析工具。

**参数：**
- `video_path` (必需): 视频文件路径或 URL
- `scene_detection` (可选): 是否检测场景转换
- `detailed_analysis` (可选): 是否提供详细分析
- `model` (可选): 使用的模型名称

### analyze_video_custom

自定义视频分析工具。

**参数：**
- `video_path` (必需): 视频文件路径或 URL
- `custom_prompt` (必需): 自定义分析提示词
- `analysis_focus` (可选): 分析焦点
- `output_format` (可选): 输出格式
- `language` (可选): 输出语言

### validate_video_source

视频源验证工具。

**参数：**
- `video_path` (必需): 视频文件路径或 URL
- `check_accessibility` (可选): 是否检查可访问性
- `check_format` (可选): 是否检查格式兼容性
- `check_size` (可选): 是否检查文件大小
- `detailed_info` (可选): 是否返回详细信息

## 📊 支持的视频格式

- MP4
- AVI
- MOV
- MKV
- WebM
- FLV

## ⚙️ 配置选项

### 环境变量

| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| `DASHSCOPE_API_KEY` | DashScope API 密钥 | *必需* |
| `VIDEO__MAX_FILE_SIZE` | 最大文件大小（字节） | 104857600 (100MB) |
| `VIDEO__MAX_DURATION` | 最大视频时长（秒） | 3600 (1小时) |
| `MCP__MAX_CONCURRENT_REQUESTS` | 最大并发请求数 | 10 |
| `LOG__LEVEL` | 日志级别 | INFO |
| `ENVIRONMENT` | 运行环境 | production |
| `DEBUG` | 调试模式 | false |

### 配置文件

项目支持通过 `.env` 文件进行配置。所有环境变量都可以在配置文件中设置。

## 🔒 安全特性

- **文件大小限制**：防止过大文件上传
- **格式验证**：只支持指定的视频格式
- **域名白名单/黑名单**：控制允许访问的 URL 域名
- **速率限制**：防止 API 滥用
- **输入验证**：严格的参数验证

## 📈 监控和统计

服务器内置了使用统计和监控功能：

- **使用统计**：工具和资源的使用频率
- **性能监控**：响应时间和成功率
- **健康检查**：系统状态和组件健康
- **资源监控**：CPU、内存、磁盘使用情况

访问统计信息：

```bash
# 查看使用统计
curl http://localhost:3001/resources/stats://usage

# 查看系统状态
curl http://localhost:3001/resources/status://system
```

## 🐛 故障排除

### 常见问题

1. **API Key 未设置**
```
   Error: DashScope API key is required
```
   解决方案：设置 `DASHSCOPE_API_KEY` 环境变量

2. **不支持的视频格式**
```
   Error: Unsupported format: xxx
```
   解决方案：转换视频为支持的格式（MP4, AVI, MOV, MKV, WebM, FLV）

3. **文件过大**
```
   Error: File too large
```
   解决方案：压缩视频或调整 `VIDEO__MAX_FILE_SIZE` 配置

4. **网络连接问题**
```
   Error: Failed to connect to DashScope API
```
   解决方案：检查网络连接和 API Key 是否正确

### 调试模式

启用调试模式获取更详细的日志：

```bash
python -m aigroup_video_mcp.main --debug serve
```

## 🤝 贡献

欢迎贡献代码！请遵循以下步骤：

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 📄 许可证

该项目使用 MIT 许可证。详情请参阅 [LICENSE](https://github.com/jackdark425/aigroup-video-mcp/blob/HEAD/LICENSE) 文件。

## 🙏 致谢

- [阿里云 DashScope](https://dashscope.aliyun.com/) - 提供强大的多模态 AI 能力
- [Model Context Protocol](https://modelcontextprotocol.io/) - 提供标准化的模型交互协议
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) - 提供 Python MCP 实现

## 📞 支持

如果你遇到任何问题或有建议，请：

1. 查看 [常见问题](https://github.com/jackdark425/aigroup-video-mcp/blob/HEAD/README.md#故障排除) 部分
2. 提交 [Issue](https://github.com/jackdark425/aigroup-video-mcp/issues)
3. 联系开发团队：jackdark425@gmail.com

---

**Made with ❤️ by Aigroup Team**

**官方网站：** [https://github.com/jackdark425/aigroup-video-mcp](https://github.com/jackdark425/aigroup-video-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`entertainment and media`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`python`
- 参数：`-m aigroup_video_mcp.main serve`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/jack666-aigroup-video.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
