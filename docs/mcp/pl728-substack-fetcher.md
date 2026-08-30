---
title: "Substack抓取器 - 金融版"
description: "启用从 Adam Mancini 在 Substack 上的 Trade Companion 获取和阅读订阅者专属内容的功能，使克劳德能够访问并讨论最新的金融交易文章。"
---

# Substack抓取器 - 金融版

启用从 Adam Mancini 在 Substack 上的 Trade Companion 获取和阅读订阅者专属内容的功能，使克劳德能够访问并讨论最新的金融交易文章。

# Substack 读者

一个用于从 Adam Mancini 在 Substack 上的 Trade Companion 获取和阅读文章的工具。

## 设置

### 先决条件

1. Python 3.8+
2. uv 包管理器
3. Claude AI 助手

### 安装

1. 如果你还没有安装 uv 包管理器，请先安装：
```bash
   curl -sSf https://install.ultraviolet.dev | sh
```

2. 创建并激活虚拟环境：
```bash
   uv venv
   source .venv/bin/activate  # 在 Windows 上: .venv\Scripts\activate
```

3. 使用 `pyproject.toml` 文件安装依赖项：
```bash
   uv pip install -e .
```

### 设置 Substack 认证

为了访问仅限订阅者的内容，你需要提供你的 Substack cookie：

1. 为你的浏览器安装 Cookie-Editor 扩展程序：
   - [Chrome 网上应用店](https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm)
   - [Firefox 插件](https://addons.mozilla.org/en-US/firefox/addon/cookie-editor/)

2. 登录到你的 Substack 账户 [tradecompanion.substack.com](https://tradecompanion.substack.com)

3. 点击 Cookie-Editor 扩展程序图标

4. 点击“导出”并选择“导出为 JSON”（这会将 cookie 复制到剪贴板）

5. 在此项目的根目录下创建一个名为 `substack_cookies.json` 的文件

6. 将复制的 cookie 粘贴到此文件中并保存

## 与 Claude 配合使用

此工具设计用于与 Claude AI 助手配合使用。要设置它：

1. 通过在 Claude 配置文件中添加以下内容来配置 Claude 以使用此 MCP 服务器：

```json
{
  "mcpServers": {
    "substack_reader": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/substack_reader",
        "run",
        "substack_reader.py"
      ]
    }
  },
  "globalShortcut": "Ctrl+Space"
}
```

将 `/path/to/substack_reader` 替换为实际的 substack_reader 目录路径。

2. 当正确配置后，Claude 在启动时会自动连接到此 MCP 服务器。

3. 然后你可以要求 Claude 获取最新的 Trade Companion 文章。

## 功能

- 获取 Adam Mancini 发布的最新 Trade Companion 文章
- 以纯文本格式提取文章内容
- 保留标题、段落和列表项
- 排除 "My Trade Methodology Fundamentals" 文章

## 隐私说明

你的 Substack cookie 存储在本地的 `substack_cookies.json` 文件中，并且仅用于向 Substack 进行身份验证请求。它们不会被发送到任何其他地方或以任何形式暴露。

**官方网站：** [https://github.com/pl728/substack-fetcher-mcp](https://github.com/pl728/substack-fetcher-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`finance`, `data`
- 标签：`finance`, `browser automation`, `research and data`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`--directory /path/to/substack_reader run substack_reader.py`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/pl728-substack-fetcher.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
