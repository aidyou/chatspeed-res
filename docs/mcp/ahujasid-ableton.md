---
title: "Ableton"
description: "通过模型上下文协议将Ableton Live与Claude AI连接起来，通过允许Claude直接与Ableton Live会话交互和控制，实现人工智能辅助的音乐制作。"
---

# Ableton

通过模型上下文协议将Ableton Live与Claude AI连接起来，通过允许Claude直接与Ableton Live会话交互和控制，实现人工智能辅助的音乐制作。

# AbletonMCP - Ableton Live Model Context Protocol 集成
[Smithery](https://smithery.ai/server/@ahujasid/ableton-mcp)

AbletonMCP 通过 Model Context Protocol (MCP) 将 Ableton Live 连接到 Claude AI，使 Claude 能够直接与 Ableton Live 交互并控制它。此集成支持提示辅助的音乐制作、音轨创建和 Live 会话操作。

### 加入社区

提供反馈、获取灵感并在 MCP 上进行构建：[Discord](https://discord.gg/3ZrMyGKnaU)。由 [Siddharth](https://x.com/sidahuj) 制作

## 功能

- **双向通信**：通过基于套接字的服务器将 Claude AI 连接到 Ableton Live
- **音轨操作**：创建、修改和操作 MIDI 和音频轨道
- **乐器和效果选择**：Claude 可以访问并从 Ableton 的库中加载正确的乐器、效果和声音
- **剪辑创建**：创建并编辑带有音符的 MIDI 剪辑
- **会话控制**：开始和停止播放、触发剪辑以及控制传输

## 组件

系统由两个主要组件组成：

1. **Ableton 远程脚本** (`Ableton_Remote_Script/__init__.py`)：一个用于 Ableton Live 的 MIDI 远程脚本，创建一个套接字服务器来接收和执行命令
2. **MCP 服务器** (`server.py`)：一个实现 Model Context Protocol 并连接到 Ableton 远程脚本的 Python 服务器

## 安装

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@ahujasid/ableton-mcp) 自动安装 Claude Desktop 的 Ableton Live 集成：

```bash
npx -y @smithery/cli install @ahujasid/ableton-mcp --client claude
```

### 先决条件

- Ableton Live 10 或更新版本
- Python 3.8 或更新版本
- [uv 包管理器](https://astral.sh/uv)

如果你使用的是 Mac，请这样安装 uv：
```
brew install uv
```

否则，请从 [uv 的官方网站][[https://docs.astral.sh/uv/getting-started/installation/]](https://docs.astral.sh/uv/getting-started/installation/]) 安装

⚠️ 在安装 UV 之前请勿继续

### Claude for Desktop 集成

[按照设置说明视频进行操作](https://youtu.be/iJWJqyVuPS8)

1. 前往 Claude > 设置 > 开发者 > 编辑配置 > claude_desktop_config.json 添加以下内容：

```json
{
    "mcpServers": {
        "AbletonMCP": {
            "command": "uvx",
            "args": [
                "ableton-mcp"
            ]
        }
    }
}
```

### Cursor 集成

通过 uvx 运行 ableton-mcp 而不永久安装。前往 Cursor 设置 > MCP 并粘贴此命令：

```
uvx ableton-mcp
```

⚠️ 仅运行一个 MCP 服务器实例（在 Cursor 或 Claude Desktop 中择一），不要同时运行两者

### 安装 Ableton 远程脚本

[按照设置说明视频进行操作](https://youtu.be/iJWJqyVuPS8)

1. 从该仓库下载 `AbletonMCP_Remote_Script/__init__.py` 文件

2. 将文件夹复制到 Ableton 的 MIDI Remote Scripts 目录。不同操作系统和版本的路径可能有所不同。**以下路径之一应该有效，您可能需要查找一下**：

   **对于 macOS:**
   - 方法 1：前往应用程序 > 右键点击 Ableton Live 应用程序 → 显示包内容 → 导航至：
     `Contents/App-Resources/MIDI Remote Scripts/`
   - 方法 2：如果在第一种方法中找不到，请使用直接路径（将 XX 替换为您的版本号）：
     `/Users/[用户名]/Library/Preferences/Ableton/Live XX/User Remote Scripts`

   **对于 Windows:**
   - 方法 1:
     C:\Users\[用户名]\AppData\Roaming\Ableton\Live x.x.x\Preferences\User Remote Scripts
   - 方法 2:
     `C:\ProgramData\Ableton\Live XX\Resources\MIDI Remote Scripts\`
   - 方法 3:
     `C:\Program Files\Ableton\Live XX\Resources\MIDI Remote Scripts\`
   *注意：将 XX 替换为您的 Ableton 版本号（例如，10, 11, 12）*

4. 在 Remote Scripts 目录中创建一个名为 'AbletonMCP' 的文件夹，并将下载的 `__init__.py` 文件粘贴进去

3. 启动 Ableton Live

4. 前往设置/偏好设置 → Link, Tempo & MIDI

5. 在 Control Surface 下拉菜单中选择 "AbletonMCP"

6. 将输入和输出设置为 "None"

## 使用说明

### 开始连接

1. 确保 Ableton Remote Script 已加载到 Ableton Live 中
2. 确保 MCP 服务器已在 Claude Desktop 或 Cursor 中配置
3. 当您与 Claude 交互时，连接应自动建立

### 与 Claude 一起使用

一旦在 Claude 上设置了配置文件，并且远程脚本正在 Ableton 中运行，您将看到带有 Ableton MCP 工具的锤子图标。

## 功能

- 获取会话和轨道信息
- 创建和修改 MIDI 和音频轨道
- 创建、编辑和触发片段
- 控制播放
- 从 Ableton 浏览器加载乐器和效果
- 向 MIDI 片段添加音符
- 更改节奏和其他会话参数

## 示例命令

这里是一些您可以要求 Claude 执行的示例命令：

- "创建一个 80 年代合成波曲目" [演示](https://youtu.be/VH9g66e42XA)
- "创建一个 Metro Boomin 风格的嘻哈节拍"
- "创建一个新的带有合成贝斯乐器的 MIDI 轨道"
- "给我的鼓添加混响"
- "创建一个包含简单旋律的 4 小节 MIDI 片段"
- "获取当前 Ableton 会话的信息"
- "将 808 鼓机架加载到所选轨道"
- "向轨道 1 中的片段添加爵士和弦进行"
- "将速度设置为 120 BPM"
- "播放轨道 2 中的片段"

## 故障排除

- **连接问题**：确保已加载 Ableton Remote Script，并且已在 Claude 上配置了 MCP 服务器
- **超时错误**：尝试简化您的请求或将它们分解成更小的步骤
- **重启试试？**：如果您仍然遇到连接错误，请尝试重新启动 Claude 和 Ableton Live

## 技术细节

### 通信协议

系统通过TCP套接字使用基于简单JSON的协议：

- 命令以包含`type`和可选`params`的JSON对象形式发送
- 响应是以包含`status`以及`result`或`message`的JSON对象形式返回

### 限制与安全考虑

- 创建复杂的音乐编排可能需要分解成更小的步骤
- 该工具设计为与Ableton的默认设备和浏览器项目一起工作
- 在进行大量实验之前，请务必保存您的工作

## 贡献

欢迎贡献！请随时提交Pull Request。

## 免责声明

这是一个第三方集成，并非由Ableton制作。

**官方网站：** [https://github.com/ahujasid/ableton-mcp](https://github.com/ahujasid/ableton-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`entertainment and media`, `os automation`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`ableton-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/ahujasid-ableton.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
