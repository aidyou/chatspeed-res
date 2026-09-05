---
title: "自动生成口播视频（MCP&Agent挑战赛）"
description: "🛠️ 可用工具 服务器提供以下工具，可供 LLM 或其他客户端直接调用： 数字人与多媒体创作工具 - Avatar Tools (avatartools): - createpersonalavatarbyphoto: 通过单张照片创建个人数字人。 - createpersonalavatarbyvideo: 通过视频文件创建个人数字人。 - Voice Tools (voicetools): -…"
---

# 自动生成口播视频（MCP&Agent挑战赛）

🛠️ 可用工具 服务器提供以下工具，可供 LLM 或其他客户端直接调用： 数字人与多媒体创作工具 - Avatar Tools (avatartools): - createpersonalavatarbyphoto: 通过单张照片创建个人数字人。 - createpersonalavatarbyvideo: 通过视频文件创建个人数字人。 - Voice Tools (voicetools): -…

## 🛠️ 可用工具

服务器提供以下工具，可供 LLM 或其他客户端直接调用：

### 数字人与多媒体创作工具
- **Avatar Tools (`avatar_tools`)**:
  - `create_personal_avatar_by_photo`: 通过单张照片创建个人数字人。
  - `create_personal_avatar_by_video`: 通过视频文件创建个人数字人。
- **Voice Tools (`voice_tools`)**:
  - `create_voice_by_file`: 通过音频文件克隆声音。
  - `create_voice_by_text`: 通过文本创建声音（用于声音定制）。
- **Video Creation Tools (`video_tools`)**:
  - `create_video_by_audio`: 使用指定的数字人和音频文件创作视频。
  - `create_video_by_script`: 使用指定的数字人和文本脚本创作视频。
- **Audio Creation Tools (`audio_tools`)**:
  - `create_audio_by_text`: 将文本转换为语音。
- **File Upload Tools (`upload_tools`)**:
  - `upload_file`: 上传媒体文件（音频、视频）到服务器。

### 网络与内容工具 (`web_tools`)
- `get_baidu_trending`: 获取百度热搜榜。
- `get_36kr_news`: 获取 36氪 最新资讯。
- `get_autohome_news`: 获取汽车之家最新资讯。
- `get_custom_rss`: 从指定的 RSS 源获取内容。
- `crawl_website`: 爬取指定网页的结构化内容。
- `web_search`: 执行网络搜索。

### 查询工具 (`query_tools`)
- `query_task_status`: 查询指定任务的当前状态和结果。
- `query_personal_avatars`: 查询已创建的个人数字人列表。
- `query_personal_voices`: 查询已创建的个人声音列表。
- `query_public_avatars`: 查询公共数字人列表。
- `query_public_voices`: 查询公共声音列表。
- `query_video_templates`: 查询可用的视频模板。

#### 命令行工具

安装后，您可以使用 `auto_video_mcp` 命令行工具来启动服务器：

```bash
# 激活虚拟环境
source .venv/bin/activate

# HTTP 模式 (默认端口 8000)
python -m auto_video_mcp.server --transport http

# 自定义主机和端口
python -m auto_video_mcp.server --transport http --host 0.0.0.0 --port 8080 

# SSE 模式
python -m auto_video_mcp.server --transport sse

# STDIO 模式 (用于 MCP 集成)
python -m auto_video_mcp.server --transport stdio
```

或者使用安装的命令行工具：

```bash
# HTTP 模式 (默认端口 8000)
auto_video_mcp --transport http

# 自定义主机和端口
auto_video_mcp --transport http --host 0.0.0.0 --port 8080 

# SSE 模式
auto_video_mcp --transport sse

# STDIO 模式 (用于 MCP 集成)
auto_video_mcp --transport stdio
```

#### 配置方式

服务器的配置项（如主机、端口等）可以通过以下三种方式设置，优先级从高到低：

1.  **命令行参数**: 启动时直接传入参数，优先级最高。
2.  **配置文件**: 通过 `--config` 参数指定一个 JSON 配置文件。
3.  **环境变量**: 从 `.env` 文件中加载，通常用于存放敏感信息如 API Token。

#### 传输协议 (Transport)

FastMCP 支持多种传输协议，您可以通过不同的子命令选择：

-   **`http` (默认)**: 启动一个基于 Streamable HTTP 的 Web 服务器。这是推荐用于 Web 服务部署的方式。
```bash
    # 使用默认配置 (http://127.0.0.1:8000)
    python -m auto_video_mcp.server --transport http

    # 自定义主机和端口
    python -m auto_video_mcp.server --transport http --host 0.0.0.0 --port 8080
```

-   **`sse`**: 启动一个基于 Server-Sent Events (SSE) 的服务器。这是旧版协议，新项目推荐使用 `http`。
```bash
    python -m auto_video_mcp.server --transport sse
```

-   **`stdio`**: 启动一个基于标准输入/输出的服务器。这主要用于与 MCP 客户端集成。
```bash
    python -m auto_video_mcp.server --transport stdio
```

#### 命令行参数

您可以使用以下参数来配置服务器的运行：

-   `--transport `: 传输协议类型，可选 `http`, `sse`, `stdio`。
-   `--host 
`: 服务器监听的主机地址 (默认为 `127.0.0.1`)。
-   `--port `: 服务器监听的端口 (默认为 `8000`)。
-   `--path `: HTTP 模式下的 URL 路径 (默认为 `/mcp/`)。
-   `--log-level `: 设置日志级别 (`debug`, `info`, `warning`, `error`, `critical`)。
-   `--config `: 指定配置文件路径。

#### 客户端连接配置

##### Cursor IDE 集成

Cursor IDE 支持通过 MCP 协议与飞影数字人服务器集成。有两种主要的连接方式：

**方式一：通过 `stdio` (标准输入/输出)**

这是最直接的集成方式，Cursor 会在需要时自动启动和停止 MCP 服务器进程。

1.  编辑 Cursor 的 MCP 配置文件 (`~/.cursor/mcp.json`):

```json
    {
      "mcpServers": {
        "auto_video_mcp": {
          "command": "uvx",
          "args": ["auto_video_mcp", "--transport", "stdio"],
          "env": {
            "FLYWORKS_API_TOKEN": "你的API令牌"
          }
        }
      }
    }
```

2.  确保 `auto_video_mcp` 已经安装在您的 Python 环境中。

3.  在 Cursor 中选择 "auto_video_mcp" 作为 MCP 服务器。

**方式二：通过 `http` 连接**

如果您已经手动启动了 MCP 服务器（例如，在本地或 Docker 中运行），您可以通过 HTTP 连接到它。

1.  首先，确保服务器正在运行。例如：
```bash
    python -m auto_video_mcp.server --transport http --host 127.0.0.1 --port 8000
```

2.  编辑 Cursor 的 MCP 配置文件 (`~/.cursor/mcp.json`)，添加以下配置：

```json
    {
      "mcpServers": {
        "auto_video_mcp_http": {
          "transport": "http",
          "url": "http://127.0.0.1:8000/mcp/"
        }
      }
    }
```
    > **注意**:
    > - `url` 中的路径 (`/mcp/`) 需要与服务器配置的 `SERVER_PATH` 环境变量保持一致。
    > - 如果服务器运行在不同的主机或端口，请相应地修改 `url`。

3.  在 Cursor 中选择 "auto_video_mcp_http" 作为 MCP 服务器。

##### 远程连接 (HTTP)

如果您需要将服务部署为网络服务，可以使用 HTTP 连接。

1.  **启动服务器**:
```bash
    python -m auto_video_mcp.server --transport http --host 0.0.0.0 --port 8000
```

2.  **配置客户端**:
    在客户端的配置文件中，添加一个指向您服务器 URL 的条目。

```json
    {
      "mcpServers": {
        "auto_video_mcp-remote": {
          "transport": "http",
          "url": "http://your-server-ip:8000/mcp/"
        }
      }
    }
```
    > **注意**: 请将 `your-server-ip` 替换为运行服务器的机器的实际 IP 地址或域名。

完成配置并重启客户端后，即可连接到飞影数字人 MCP 服务器。

**官方网站：** [https://github.com/fancyboi999/auto_video_mcp](https://github.com/fancyboi999/auto_video_mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`entertainment and media`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`auto_video_mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/fancyboi999-auto-video.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
