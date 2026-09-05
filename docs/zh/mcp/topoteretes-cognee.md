---
title: "认知记忆管理平台"
description: "用于AI应用程序和代理的记忆管理器，使用各种图和向量存储，并允许从30多个数据源进行摄入。"
---

# 认知记忆管理平台

用于AI应用程序和代理的记忆管理器，使用各种图和向量存储，并允许从30多个数据源进行摄入。

# cognee MCP 服务器

### 手动安装
这是一个 MCP 服务器项目
=======
1. 克隆 [cognee](https://github.com/topoteretes/cognee) 仓库

2. 安装依赖项

```
brew install uv
```

```jsx
cd cognee-mcp
uv sync --dev --all-extras --reinstall
```

3. 激活虚拟环境：

```jsx
source .venv/bin/activate
```

4. 将新服务器添加到您的 Claude 配置中：

文件应位于这里：~/Library/Application\ Support/Claude/
```
cd ~/Library/Application\ Support/Claude/
```
如果该文件夹中不存在 `claude_desktop_config.json`，则需要创建它。
确保将您的路径和 LLM API 密钥添加到下面的文件中。
使用您选择的编辑器，例如 Nano：
```
nano claude_desktop_config.json
```

```
{
    "mcpServers": {
        "cognee": {
            "command": "/Users/{user}/cognee/.venv/bin/uv",
            "args": [
        "--directory",
        "/Users/{user}/cognee/cognee-mcp",
        "run",
        "cognee"
      ],
      "env": {
        "ENV": "local",
        "TOKENIZERS_PARALLELISM": "false",
        "LLM_API_KEY": "sk-"
      }
        }
    }
}
```

重启您的 Claude 桌面应用。

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/cognee) 自动为 Claude Desktop 安装 Cognee：

```bash
npx -y @smithery/cli install cognee --client claude
```

在 `server.py` 中定义 `cognify` 工具
重启您的 Claude 桌面应用。

要使用调试器，请运行：
```bash
mcp dev src/server.py
```
以超时时间打开检查器：
```
http://localhost:5173?timeout=120000
```

在开发 cognee 时，如果您想应用新的更改，需要执行以下步骤：

1. 在 cognee 文件夹中运行 `poetry lock`
2. 运行 `uv sync --dev --all-extras --reinstall`
3. 运行 `mcp dev src/server.py`

**官方网站：** [https://github.com/topoteretes/cognee/tree/dev/cognee-mcp](https://github.com/topoteretes/cognee/tree/dev/cognee-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`memory`
- 标签：`knowledge and memory`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`/Users/{user}/cognee/.venv/bin/uv`
- 参数：`--directory /Users/{user}/cognee/cognee-mcp run cognee`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/topoteretes-cognee.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
