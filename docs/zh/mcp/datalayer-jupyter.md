---
title: "Jupyter MCP 服务"
description: "通过模型上下文协议启用与 Jupyter 笔记本的交互，支持在 JupyterLab 环境中执行代码和插入 markdown。"
---

# Jupyter MCP 服务

通过模型上下文协议启用与 Jupyter 笔记本的交互，支持在 JupyterLab 环境中执行代码和插入 markdown。

[![Datalayer](/mcp-assets/ebffabe66603ffc5befd3fb0a80b406d.svg)](https://datalayer.io)

[![成为赞助商](/mcp-assets/ac64e82bf123c4e77c9539d7abadcb39.svg)](https://github.com/sponsors/datalayer)

# 🪐 ✨ Jupyter MCP 服务器

[![Github Actions 状态](/mcp-assets/a360cf14c31b446d557b2bc79fbedc72.svg)](https://github.com/datalayer/jupyter-mcp-server/actions/workflows/build.yml)
[![PyPI - 版本](/mcp-assets/8ef09b6c2110dbd088df1d98fe6006ab.svg)](https://pypi.org/project/jupyter-mcp-server)
[Smithery](https://smithery.ai/server/@datalayer/jupyter-mcp-server)

Jupyter MCP 服务器是一个 [模型上下文协议](https://modelcontextprotocol.io) (MCP) 服务器实现，它提供了与运行在任何 JupyterLab 中的 📓 Jupyter 笔记本的交互（也适用于你的 💻 本地 JupyterLab）。

![Jupyter MCP 服务器](/mcp-assets/57180397b99671dab65bd45b4840f2ce.gif)

## 启动 JupyterLab

确保你已经安装了以下内容。协作包是必需的，因为通过 [Jupyter 实时协作](https://jupyterlab.readthedocs.io/en/stable/user/rtc.html)，可以在笔记本上看到所做的修改。

```bash
pip install jupyterlab jupyter-collaboration ipykernel
pip uninstall -y pycrdt datalayer_pycrdt
pip install datalayer_pycrdt
```

然后，使用以下命令启动 JupyterLab。

```bash
jupyter lab --port 8888 --IdentityProvider.token MY_TOKEN --ip 0.0.0.0
```

你也可以运行 `make jupyterlab`。

> [!注意]
>
> `--ip` 设置为 `0.0.0.0` 以便允许在 Docker 容器中运行的 MCP 服务器访问你的本地 JupyterLab。

## 与 Claude 桌面版一起使用

Claude 桌面版可以从 [这个页面](https://claude.ai/download) 下载 macOS 和 Windows 版本。

对于 Linux，我们成功使用了基于 nix 的 [非官方构建脚本](https://github.com/k3d3/claude-desktop-linux-flake)。

```bash
# ⚠️ UNOFFICIAL
# You can also run `make claude-linux`
NIXPKGS_ALLOW_UNFREE=1 nix run github:k3d3/claude-desktop-linux-flake \
  --impure \
  --extra-experimental-features flakes \
  --extra-experimental-features nix-command
```

要与 Claude 桌面版一起使用，请将以下内容添加到你的 `claude_desktop_config.json` 中（更多详情请参阅 [MCP 文档网站](https://modelcontextprotocol.io/quickstart/user#2-add-the-filesystem-mcp-server)）。

> [!重要]
>
> 确保 `SERVER_URL` 和 `TOKEN` 的端口与 `jupyter lab` 命令中使用的相匹配。
>
> `NOTEBOOK_PATH` 应该相对于启动 JupyterLab 的目录。

### macOS 和 Windows 上的 Claude 配置

```json
{
  "mcpServers": {
    "jupyter": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e",
        "SERVER_URL",
        "-e",
        "TOKEN",
        "-e",
        "NOTEBOOK_PATH",
        "datalayer/jupyter-mcp-server:latest"
      ],
      "env": {
        "SERVER_URL": "http://host.docker.internal:8888",
        "TOKEN": "MY_TOKEN",
        "NOTEBOOK_PATH": "notebook.ipynb"
      }
    }
  }
}
```

### Linux 上的 Claude 配置

```bash
CLAUDE_CONFIG=${HOME}/.config/Claude/claude_desktop_config.json
cat  $CLAUDE_CONFIG
{
  "mcpServers": {
    "jupyter": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e",
        "SERVER_URL",
        "-e",
        "TOKEN",
        "-e",
        "NOTEBOOK_PATH",
        "--network=host",
        "datalayer/jupyter-mcp-server:latest"
      ],
      "env": {
        "SERVER_URL": "http://localhost:8888",
        "TOKEN": "MY_TOKEN",
        "NOTEBOOK_PATH": "notebook.ipynb"
      }
    }
  }
}
EOF
cat $CLAUDE_CONFIG
```

## 组件

### 工具

服务器目前提供 3 个工具：

1. `add_execute_code_cell`

- 在 Jupyter 笔记本中添加并执行一个代码单元格。
- 输入：
  - `cell_content`（字符串）：要执行的代码。
- 返回：单元格输出。

2. `add_markdown_cell`

- 在 Jupyter 笔记本中添加一个 Markdown 单元格。
- 输入：
  - `cell_content`（字符串）：Markdown 内容。
- 返回：成功消息。

3. `download_earth_data_granules`

   ⚠️ 我们计划在未来将此工具迁移到单独的仓库，因为它特定于地理空间分析。

- 在 Jupyter 笔记本中添加一个代码单元格，用于从 NASA Earth Data 下载地球数据颗粒。
- 输入：
  - `folder_name` (字符串)：用于保存数据的本地文件夹名称。
  - `short_name` (字符串)：要下载的地球数据集的简称。
  - `count` (整数)：要下载的数据颗粒数量。
  - `temporal` (元组)：(可选) 时间范围，格式为 (date_from, date_to)。
  - `bounding_box` (元组)：(可选) 边界框，格式为 (lower_left_lon, lower_left_lat, upper_right_lon, upper_right_lat)。
- 返回：单元格输出。

## 构建

您可以从源代码构建 Docker 镜像。

```bash
make build-docker
```

## 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@datalayer/jupyter-mcp-server) 自动安装适用于 Claude Desktop 的 Jupyter MCP Server：

```bash
npx -y @smithery/cli install @datalayer/jupyter-mcp-server --client claude
```

**官方网站：** [https://github.com/datalayer/jupyter-mcp-server](https://github.com/datalayer/jupyter-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`docker`
- 参数：`run -i --rm -e ROOM_URL -e ROOM_TOKEN -e ROOM_ID -e RUNTIME_URL -e RUNTIME_TOKEN datalayer/jupyter-mcp-server:latest`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/datalayer-jupyter.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
