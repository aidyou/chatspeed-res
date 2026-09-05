---
title: "memory-plus"
description: "🧠 Memory-Plus 是一种轻量级的本地 RAG（检索增强生成）内存存储，适用于 MCP 代理。可以轻松地在会话之间记录、检索、更新、删除和可视化持久化的“记忆”——非常适合与多个 AI 编码工具（如 Windsurf、Cursor 或 Copilot）一起工作的开发者，或者任何希望他们的 AI 能真正记住他们的人。"
---

# memory-plus

🧠 Memory-Plus 是一种轻量级的本地 RAG（检索增强生成）内存存储，适用于 MCP 代理。可以轻松地在会话之间记录、检索、更新、删除和可视化持久化的“记忆”——非常适合与多个 AI 编码工具（如 Windsurf、Cursor 或 Copilot）一起工作的开发者，或者任何希望他们的 AI 能真正记住他们的人。

# Memory-Plus

一个轻量级的本地检索增强生成（RAG）内存存储，用于MCP代理。Memory-Plus允许您的代理在运行过程中记录、检索、更新和可视化持久的“记忆”——包括笔记、想法和会话上下文。

> 🏆 在[Infosys剑桥AI中心黑客松](https://infosys-cam-ai-centre.github.io/Infosys-Cambridge-Hackathon/)中获得**第一名**！

## 主要功能

* **记录记忆**：保存用户数据、想法和重要上下文。
* **检索记忆**：通过关键词或主题搜索过去的条目。
* **最近记忆**：快速获取最后 *N* 项。
* **更新记忆**：无缝追加或修改现有条目。
* **可视化记忆**：揭示关系的交互式图集群。
* **文件导入** (*自v0.1.2起*)：直接将文档摄入内存。
* **删除记忆** (*自v0.1.2起*)：移除不需要的条目。
* **记忆的记忆** (*自v0.1.4起*)：现在我们使用`资源`来教导您的AI何时（以及何时不）回忆过去的互动。
* **记忆版本控制** (*自v0.1.4起*)：当记忆被更新时，我们会保留旧版本以提供完整的记录历史。

---

![alt text](/mcp-assets/346961ce5284e34085dbbb87c6d340a6.png)

## 安装

### 1. 先决条件

**Google API密钥**
从[Google AI Studio](https://aistudio.google.com/apikey)获取并设置为环境中的`GOOGLE_API_KEY`。
> 注意，我们将仅使用此API密钥的`Gemini嵌入API`，因此对您来说是**完全免费**的！

设置Google API密钥示例

```bash
  # macOS/Linux
  export GOOGLE_API_KEY=""

  # Windows (PowerShell)
  setx GOOGLE_API_KEY ""
```

**UV运行时**
用于提供MCP插件。

安装UV运行时

```bash
pip install uv
```

或者通过shell脚本安装：

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### VS Code一键设置

点击下面的徽章以自动在VS Code中安装和配置Memory-Plus：

[![VS Code一键安装](/mcp-assets/ff0c64ea4d3a42e6aeccd71c5a5b6a57.svg)](https://insiders.vscode.dev/redirect/mcp/install?name=memory-plus&config=%7B%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22-q%22%2C%22memory-plus%40latest%22%5D%7D)

这将在您的`settings.json`中添加以下内容：

```json
  {
    "mcpServers": {
      //...,  您的其他MCP服务器
      "memory-plus": {
        "command": "uvx",
        "args": [
          "-q",
          "memory-plus@latest"
        ],
      }
    }
  }
```

对于`cursor`，转到`文件 -> 首选项 -> 光标设置 -> MCP`并添加上述配置。
如果您没有将`GOOGLE_API_KEY`添加到您的秘密/环境变量中，可以添加：
```json
"env": {
        "GOOGLE_API_KEY": ""
      }
```
就在`memory-plus`字典中的`args`数组之后。

对于`Cline`，在您的`cline_mcp_settings.json`中添加以下内容：
```json
{
  "mcpServers": {
    //...,  您的其他MCP服务器
    "memory-plus": {
      "disabled": false,
      "timeout": 300,
      "command": "uvx",
      "args": [
        "-q",
        "memory-plus@latest"
      ],
      "env": {
        "GOOGLE_API_KEY": "${{ secrets.GOOGLE_API_KEY }}"
      },
      "transportType": "stdio"
    }
  }
}
```

对于其他IDE，它应该与上述内容大致相同。

## 本地测试和开发

使用MCP检查器，您可以本地测试memory-plus服务器。

```bash
git clone https://github.com/Yuchen20/Memory-Plus.git
cd Memory-Plus
npx @modelcontextprotocol/inspector fastmcp run run .\memory_plus\mcp.py
```

或者，如果您更喜欢在实际聊天会话中使用此MCP。`agent.py`中有一个模板聊天机器人。

```bash
# 克隆仓库
git clone https://github.com/Yuchen20/Memory-Plus.git
cd Memory-Plus

# 安装依赖
pip install uv
uv pip install fast-agent-mcp
uv run fast-agent setup
```
用您自己的API密钥设置`fastagent.config.yaml`和`fastagent.secrets.yaml`。
```bash
# 运行代理
uv run agent_memory.py
```

## 路线图
- [x] 内存更新
- [x] 改进记忆记录的提示工程
- [x] 更好的记忆图可视化
- [x] 文件导入
- [ ] 远程备份！
- [ ] 内存管理的Web UI

> 如果您有任何功能请求，请随时通过添加新问题或在[功能请求](https://voltaic-shell-9af.notion.site/1f84e395c1d18059849ce844fcbba903?pvs=105)中添加新条目来提出。

## 许可证

本项目根据**Apache License 2.0**授权。详情请参阅[LICENSE](https://github.com/Yuchen20/Memory-Plus/blob/HEAD/LICENSE)。

## 常见问题解答

### 1. 为什么memory-plus无法工作？
- memory-plus有几个依赖项，首次下载可能较慢。通常需要大约1分钟来获取所有所需的内容。
- 一旦依赖项安装完成，后续使用将会快得多。
- 如果遇到其他问题，请随时在仓库中开启新问题。

### 2. 如何在真实的聊天会话中使用memory-plus？
- 只需将MCP JSON文件添加到您的MCP设置中。
- 添加后，memory-plus将在需要时自动激活。

**官方网站：** [https://github.com/Yuchen20/Memory-Plus](https://github.com/Yuchen20/Memory-Plus)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`memory`
- 标签：`knowledge and memory`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`-q memory-plus@latest`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/yuchen20-memory-plus.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
