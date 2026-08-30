---
title: "小红书一站式自动化MCP（10月17可用）"
description: "小红书mcp服务，\n1. 支持自动发布\n2. 支持搜索笔记\n3. 支持分析笔记内容\n4. 支持多账户管理\n5. 支持预发布（人工审核后发布）\n6. 支持评论特定笔记引流，支持@指定人\n\n支持mcp，api调用"
---

# 小红书一站式自动化MCP（10月17可用）

小红书mcp服务，
1. 支持自动发布
2. 支持搜索笔记
3. 支持分析笔记内容
4. 支持多账户管理
5. 支持预发布（人工审核后发布）
6. 支持评论特定笔记引流，支持@指定人

支持mcp，api调用

# 小红书自动化工具 - 简易使用手册

本手册将指导您快速配置和使用小红书自动化工具。
高级版本支持(已更新到pypi，可直接使用！！！）：

1. 多账号（可管理多个账号，单独隔离，可设置ip隔离）
2. 自动评论笔记引流（支持@人）
3. 可添加预发布，AI自动生成笔记到预发布界面，人工审核后直接发布。

2025.8.21 亲测可用

## 1. 下载谷歌浏览器和浏览器驱动

### 下载谷歌浏览器
1. 访问 [Google Chrome 官网](https://www.google.com/chrome/)
2. 点击"下载Chrome"并安装

### 下载浏览器驱动
1. 打开Chrome浏览器，输入 `chrome://version/` 查看版本号
2. 访问 [ChromeDriver 下载页面](https://chromedriver.chromium.org/downloads)
3. 下载对应版本的 ChromeDriver
4. 将 `chromedriver.exe` 解压到系统PATH路径中（如 `C:\Windows\System32\`）

> **提示**: 确保ChromeDriver版本与Chrome浏览器版本匹配

## 2. 安装Python

### Windows系统
1. 访问 [Python官网](https://www.python.org/downloads/)
2. 下载Python 3.8或更高版本
3. 安装时勾选"Add Python to PATH"

### 验证安装
打开命令提示符（CMD）或PowerShell，输入：
```bash
python --version
```

### 安装uv包管理器
```bash
# Windows PowerShell
curl -LsSf https://astral.sh/uv/install.ps1 | powershell
```

## 3. 运行小红书自动化服务

### 快速启动（推荐）
使用uvx直接运行，无需下载源码：

```bash
# 启动FastAPI服务器
uvx --from xiaohongshu-automation xhs-server
```

### 启动步骤
1. 运行上述命令后，系统会自动下载依赖
2. 服务启动后会打开浏览器窗口
3. **重要**: 需要扫码登录小红书账号
4. 登录成功后，服务将在 `http://localhost:8001` 运行

> **注意**: 首次运行可能需要一些时间下载依赖包

## 4. 添加MCP配置

### 配置AI客户端
如果您使用支持MCP的AI客户端（如Claude Desktop），需要添加以下配置：

#### Claude Desktop配置示例
在Claude Desktop的配置文件中添加：

```json
{
  "mcpServers": {
    "xiaohongshu-automation": {
      "command": "uvx",
      "args": ["--from", "xiaohongshu-automation", "xhs-mcp"],
      "env": {
        "FASTAPI_URL": "http://localhost:8001"
      }
    }
  }
}
```

#### 配置文件位置
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

### 启动MCP服务
在AI客户端配置完成后，MCP服务会自动启动。您也可以手动测试：

```bash
uvx --from xiaohongshu-automation xhs-mcp
```

## ✅ 验证安装

### 检查服务状态
1. 访问 `http://localhost:8001/docs` 查看API文档
2. 在AI客户端中尝试调用小红书相关功能

### 常见问题
- **ChromeDriver错误**: 确保驱动版本与浏览器版本匹配
- **Python错误**: 确保Python已正确安装并添加到PATH
- **网络错误**: 检查网络连接，确保可以访问PyPI

## 🎉 开始使用

配置完成后，您可以在AI客户端中使用以下功能：
- 发布内容到小红书
- 搜索和分析笔记
- 获取和回复评论
- 系统监控和诊断

---

**技术支持**: 如遇问题，请联系微信号：vasst888
高级版本支持(已更新到pypi，可直接使用！！！）：

1. 多账号（可管理多个账号，单独隔离，可设置ip隔离）
2. 自动评论笔记引流（支持@人）
3. 可添加预发布，AI自动生成笔记到预发布界面，人工审核后直接发布。

2025.8.21 亲测可用

演示视频：
96 Vastt.发布了一篇小红书笔记，快来看吧！ 😆 6miBi42Dm1f 😆 http://xhslink.com/m/2IS3575CL6b 复制本条信息，打开【小红书】App查看精彩内容！


此 MCP 服务器仅限研究用途，禁止用于商业目的。

**官方网站：** [https://pypi.org/project/xiaohongshu-automation/](https://pypi.org/project/xiaohongshu-automation/)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`browser`, `media`
- 标签：`browser automation`, `entertainment and media`, `小红书`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx --from xiaohongshu-automation`
- 参数：`xhs-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/alobak-automation-xhs.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
