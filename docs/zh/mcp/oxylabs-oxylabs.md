---
title: "氧元素网络抓取工具"
description: "一个利用Oxylabs Web Scraper API的爬虫工具，能够灵活选择解析和渲染页面的选项，从而高效地从复杂网站中抓取和处理网页内容。"
---

# 氧元素网络抓取工具

一个利用Oxylabs Web Scraper API的爬虫工具，能够灵活选择解析和渲染页面的选项，从而高效地从复杂网站中抓取和处理网页内容。

# MCP Server for Oxylabs Scraper
[Smithery](https://smithery.ai/server/@oxylabs/oxylabs-mcp)

一个模型上下文协议（MCP）服务器，使像Claude这样的AI助手能够通过Oxylabs强大的网络抓取技术无缝访问网页数据。

## 📖 概览

Oxylabs MCP服务器为AI模型和网络之间提供了一个桥梁。它使它们能够抓取任何URL，渲染JavaScript密集型页面，提取并格式化供AI使用的内容，绕过反抓取措施，并从195多个国家访问地理限制的网络数据。

该实现利用了模型上下文协议（MCP），为AI助手与网页内容交互创建了一种安全、标准化的方式。

## ✨ 主要功能

 从任意站点抓取内容

- 从任意URL提取数据，包括复杂的单页应用程序
- 使用无头浏览器支持完全渲染动态网站
- 选择全JavaScript渲染、仅HTML或不渲染
- 模拟移动设备和桌面视口以实现逼真的渲染

 自动获取适用于AI的数据

- 自动清理并将HTML转换为Markdown以提高可读性
- 对于像Google、Amazon等热门目标使用自动解析器

 绕过封锁和地理限制

- 以高成功率绕过复杂的机器人保护系统
- 即使是最复杂的网站也能可靠地抓取
- 从覆盖195多个国家的代理池中自动轮换IP

 灵活设置和跨平台支持

- 如有需要，可以设置渲染和解析选项
- 将数据直接馈送至AI模型或分析工具
- 支持macOS、Windows和Linux

 内置错误处理和请求管理

- 全面的错误处理和报告
- 智能速率限制和请求管理

## 🔥 示例查询

当你已经使用Claude或其他AI助手设置了MCP服务器后，你可以进行如下请求：

你能抓取
https://www.google.com/search?q=ai
页面吗？

启用解析抓取
https://www.amazon.de/-/en/Smartphone-Contract-Function-Manufacturer-Exclusive/dp/B0CNKD651V
。

启用解析和渲染抓取
https://www.amazon.de/-/en/gp/bestsellers/beauty/ref=zg_bs_nav_beauty_0
。

使用带有渲染功能的网络解锁器抓取
https://www.bestbuy.com/site/top-deals/all-electronics-on-sale/pcmcat1674241939957.c
。

## ✔️ 前提条件

在开始之前，请确保你已具备以下条件：

- **Oxylabs账户**：从[Oxylabs](https://dashboard.oxylabs.io/)获取你的用户名和密码（提供一周免费试用）

### 基本用法（通过Smithery CLI或Cursor）
- **Node.js** (v16+)
- `npx`命令行工具

### 本地/开发环境设置

- **Python 3.12+**
- `uv` 包管理器 – 使用 [此指南](https://docs.astral.sh/uv/getting-started/installation/) 安装

## âï¸ 基本设置说明

### 通过 Smithery 安装（推荐）

通过 [Smithery](https://smithery.ai/server/@oxylabs/oxylabs-mcp) 自动安装 Oxylabs MCP 服务器以用于 Claude Desktop：

```bash
npx -y @smithery/cli install @oxylabs/oxylabs-mcp --client claude
```
---
### 在 Cursor 上运行

> [!IMPORTANT]
> 需要 Cursor 版本 `0.45.6+`

在 Cursor 中配置 Oxylabs：

1. 打开 Cursor **设置**
2. 转到 **功能 > MCP 服务器** 
3. 点击 "**+ 添加新的 MCP 服务器**"
4. 输入以下内容：
   - **名称**: `oxylabs`（或您喜欢的名称）
   - **类型**: `command`
   - **命令**: `npx -y @smithery/cli@latest run @oxylabs/oxylabs-mcp --config "{\"oxylabsUsername\":\"YOUR_USERNAME\",\"oxylabsPassword\":\"YOUR_PASSWORD\"}"`
  
将 `your-username` 和 `your-password` 替换为您的 Oxylabs 凭证。

> [!TIP]
> 如果您使用的是 Windows 并遇到问题，可以尝试以下方法：
> 
> `cmd /c "set OXYLABS_USERNAME=your-username && set OXYLABS_PASSWORD=your-password && npx -y oxylabs-mcp"`

之后，刷新 MCP 服务器列表以查看新工具。Composer Agent 将在适当的时候自动使用 Oxylabs，但您也可以通过描述您的网络抓取需求来明确请求它。通过 `Command+L`（Mac）访问 Composer，在提交按钮旁边的“代理”中选择，并输入您的查询。

---
### 使用 Claude Desktop 设置

启用 **开发者模式**，然后导航到 **Claude → 设置 → 开发者 → 编辑配置**，并按如下方式编辑您的 `claude_desktop_config.json` 文件：

```json
{
  "mcpServers": {
    "oxylabs_scraper": {
      "command": "uvx",
      "args": ["oxylabs-mcp"],
      "env": {
        "OXYLABS_USERNAME": "YOUR_USERNAME_HERE",
        "OXYLABS_PASSWORD": "YOUR_PASSWORD_HERE"
      }
    }
  }
}
```
---

## ð» 本地/开发环境设置说明

### 克隆仓库

```
git clone 
```

### 安装依赖项

安装 MCP 服务器依赖项：

```bash
cd mcp-server-oxylabs

# Create virtual environment and activate it
uv venv

source .venv/bin/activate # MacOS/Linux
# OR
.venv/Scripts/activate # Windows

# Install dependencies
uv sync
```

### 使用 Claude Desktop 设置

启用 **开发者模式**，然后导航到 **Claude → 设置 → 开发者 → 编辑配置**，并按如下方式编辑您的 `claude_desktop_config.json` 文件：

```json
{
  "mcpServers": {
    "oxylabs_scraper": {
      "command": "uv",
      "args": [
        "--directory",
        "/
/oxylabs-mcp",
        "run",
        "oxylabs-mcp"
      ],
      "env": {
        "OXYLABS_USERNAME": "YOUR_USERNAME_HERE",
        "OXYLABS_PASSWORD": "YOUR_PASSWORD_HERE"
      }
    }
  }
}
```
---
### ð 调试

```bash
make run
```
然后在 `http://localhost:5173` 访问 MCP Inspector。您可能需要在检查器中添加用户名和密码作为环境变量，分别为 `OXYLABS_USERNAME` 和 `OXYLABS_PASSWORD`。

## ð§© API 参数

Oxylabs MCP 服务器支持以下参数：

| 参数 | 描述 | 值 |
|-----------|-------------|--------|
| `url` | 要抓取的 URL | 任何有效的 URL |
| `parse` | 启用结构化数据提取 | `True` 或 `False` |
| `render` | 使用无头浏览器渲染 | `html` 或 `None` |

## ð ï¸ 技术细节

该服务器提供两个主要工具：

1. **oxylabs_scraper**: 使用 Oxylabs Web Scraper API 进行常规网站抓取
2. **oxylabs_web_unblocker**: 使用 Oxylabs Web Unblocker 用于难以访问的网站

[Web Scraper API](https://oxylabs.io/products/scraper-api/web) 支持 JavaScript 渲染、解析的结构化数据以及清理后的 HTML（Markdown 格式）。[Web Unblocker](https://oxylabs.io/products/web-unblocker) 提供 JavaScript 渲染和清理后的 HTML，但不返回解析的数据。

---

> [!WARNING]
> 使用 MCP Inspector 受到 MCP 的 Python SDK 中一个持续存在的问题的影响，详情请见：https://github.com/modelcontextprotocol/python-sdk/pull/85。对于 Claude，我们使用了一个分叉版本的 SDK 作为临时解决方案。

## 许可证

本项目根据 [MIT 许可证](https://github.com/oxylabs/oxylabs-mcp/blob/HEAD/LICENSE) 发布。

## 关于 Oxylabs

Oxylabs 成立于 2015 年，是一个市场领先的网络情报收集平台，遵循最高的商业、道德和合规标准，使全球企业能够解锁数据驱动的洞察力。

[![image](/mcp-assets/4b6e75fa8224df241a3e81ec5f39cb87.png)](https://oxylabs.io/)

**官方网站：** [https://github.com/oxylabs/oxylabs-mcp](https://github.com/oxylabs/oxylabs-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`browser`
- 标签：`browser automation`, `search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`oxylabs-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/oxylabs-oxylabs.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
