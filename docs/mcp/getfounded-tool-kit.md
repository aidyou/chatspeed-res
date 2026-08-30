---
title: "MCP工具箱"
description: "一个用于Claude AI助手的模块化服务器实现，集成了工具，使Claude能够执行操作并访问外部资源，如文件系统、网络搜索、浏览器自动化、金融数据和文档生成。"
---

# MCP工具箱

一个用于Claude AI助手的模块化服务器实现，集成了工具，使Claude能够执行操作并访问外部资源，如文件系统、网络搜索、浏览器自动化、金融数据和文档生成。

# MCP 工具包

一个用于构建高精度垂直AI代理的模块化服务器实现。旨在用于构建高精度垂直AI代理，但也可以部署以获得通用工具功能。

使用的代码比单独使用Python MCP SDK少>=50%。

[![PyPI version](/mcp-assets/29b82074e1c665297b984aede3621407.svg)](https://pypi.org/project/mcptoolkit/)
[![Python versions](/mcp-assets/c339bb8884144390a05d18bfc55005e9.svg)](https://pypi.org/project/mcptoolkit/)
[![License](/mcp-assets/5816f652aa1f0cc4eedb21a2f733e09e.svg)](https://github.com/getfounded/mcp-tool-kit/blob/main/LICENSE)

### 该方法的优点

- **减少Claude的认知负担**：Claude不需要考虑工具调用的顺序
- **封装领域知识**：代理可以包含关于如何在特定垂直领域中良好执行任务的领域特定逻辑
- **简化错误处理**：代理可以在内部处理错误和重试，无需Claude参与
- **支持复杂工作流**：通过单个工具调用难以协调的多步骤过程
- **保持对话流畅**：用户不会暴露于底层系统的复杂性

### 示例场景
以下是一个具体的Claude调用垂直代理的例子：

```
User: "I need a comprehensive analysis of the electric vehicle market for a presentation tomorrow."

Claude: [recognizes this requires multiple tools and domain expertise]

Claude: "I'll help you with that comprehensive EV market analysis. I'll need to gather the latest market data, news, and trends. This will take a moment..."

[Behind the scenes, Claude calls a MarketAnalysisAgent]

Claude -> MarketAnalysisAgent.analyze_market(
    sector="electric vehicles",
    include_news=True,
    include_market_data=True,
    create_presentation=True
)

[The agent orchestrates multiple tool calls using your toolkit]
- news_search for recent EV news
- brave_web_search for market data
- sequential_thinking for analysis
- write_file to save the report
- ppt_create_presentation to generate slides

[Agent returns results to Claude]

Claude: "I've analyzed the electric vehicle market for you. Here are the key findings:
1. Tesla continues to lead with 65% market share in North America
2. BYD has overtaken VW in global sales volume
3. Battery technology breakthroughs are accelerating adoption

I've also created a presentation with detailed charts and data. You can find it saved as 'EV_Market_Analysis.pptx' in your working directory."
```

## 概述

MCP统一服务器为Claude提供了一个与各种外部系统和工具交互的统一接口，包括：

- **文件系统操作**：读取、写入和操作文件
- **时间工具**：获取不同时区的当前时间，进行时区转换
- **序列思考**：一种动态和反思性的问题解决工具
- **Brave搜索**：网络和本地搜索能力
- **浏览器自动化**：通过Playwright完全控制浏览器
- **世界银行API**：访问经济和发展数据
- **新闻API**：访问全球新闻来源和文章
- **PowerPoint**：创建和操作PowerPoint演示文稿
- **Excel**：创建和操作Excel电子表格
- **Yahoo Finance**：股票市场和金融数据
- **FRED**：联邦储备经济数据
- **代理能力**：创建并部署执行复杂任务的自主代理
- **以及更多专门工具**

## 共有123种工具可用

## 快速入门指南：使用默认工具部署您的第一个MCP服务器
注意：确保您已下载git ([https://git-scm.com/downloads](https://git-scm.com/downloads)) 和 Docker ([https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)) 并且它们正在运行。您还必须确保git可执行文件已添加到路径中（本README末尾有说明）。

## Docker 部署（推荐且最稳定）
1) 克隆仓库：
```git
clone https://github.com/getfounded/mcp-tool-kit.git
cd mcp-tool-kit
```
2) 然后您可以使用Docker的两种方式之一：
选项1 - 使用docker-compose：
```
docker-compose up
```
选项2 - 直接使用Docker命令：
```
docker run -p 8000:8000 -v ~/documents:/app/documents getfounded/mcp-tool-kit:latest
```

该仓库包含一个示例Claude桌面配置文件 (`claude_desktop_config.json`)，您可以使用它：

```json
{
  "mcpServers": {
    "unified": {
      "command": "docker",
      "args": [
        "exec",
        "-i",
        "mcp-tool-kit-mcp-server",
        "python",
        "-u",
        "mcp_unified_server.py"
      ],
      "useStdio": true
    }
  }
}
```
### 故障排查 Docker
如果您在运行 Docker 时遇到错误，很可能是因为 Claude 桌面配置文件中的镜像名称不正确。一个常见的解决方法是使用以下 JSON 进行配置：

```json
{
  "mcpServers": {
    "unified": {
      "command": "docker",
      "args": [
        "exec",
        "-i",
        "mcp-tool-kit-mcp-server-1",
        "python",
        "-u",
        "mcp_unified_server.py"
      ],
      "useStdio": true
    }
  }
}
```

## 通过 pip 安装
```bash
# Simple installation
pip install mcptoolkit

# Launch the server with default configuration
mcptoolkit-server
```

本地服务器基本配置：

```json
{
  "tools": [
    {
      "name": "MCP Toolkit",
      "url": "http://localhost:8000"
    }
  ],
  "settings": {
    "allowed_directories": ["~/Documents", "~/Downloads"],
    "default_tools": ["MCP Toolkit"]
  }
}
```

## 配置 Claude Desktop 以访问您的服务器

1. 打开 Claude Desktop 应用程序
2. 转到 文件 > 设置 > 开发者 > 编辑配置
3. 添加 'claude_desktop_configuration.json' 文件
4. 保存配置
5. 重启 MCP 服务器并集成您的新工具
6. 重启并打开 Claude Desktop 应用程序（对于 Windows 用户，您必须使用任务管理器结束所有 Claude 实例的任务）

您可以在 Claude 桌面应用程序中导入此配置，或者将其作为参考来创建自己的配置。

现在，您可以立即访问强大的功能，包括文件操作、网络搜索、时间工具等——无需任何 API 密钥或复杂的设置。

## 设置环境变量

克隆仓库后，您有两种方法可以配置环境变量：

### 选项 1：交互式设置脚本

运行设置脚本，该脚本将引导您完成环境变量的设置：

```bash
python setup_env.py
```

此脚本将在仓库中创建一个包含您的配置的 `.env` 文件。

### 选项 2：手动配置

或者，您可以在仓库根目录下手动创建一个 `.env` 文件，并包含以下变量：

```
# API Keys for external services
BRAVE_API_KEY=your_brave_api_key
NEWS_API_KEY=your_news_api_key
FRED_API_KEY=your_fred_api_key

# Application configuration
STREAMLIT_APPS_DIR=/path/to/streamlit/apps
MCP_FILESYSTEM_DIRS=/path/to/allowed/dir1,/path/to/allowed/dir2
MCP_LOG_LEVEL=info
```
### 示例 Claude 提示

设置完成后，您可以使用如下提示让 Claude 使用这些工具：

- "搜索最新的 AI 研究论文并总结其发现。"
- "创建一个关于气候变化的 PowerPoint 演示文稿，共三页。"
- "使用 weather_checker 代理告诉我东京当前的天气状况。"
- "你能使用 quick_lookup 代理研究量子计算的进步吗？"
- "下载我的 QuickBooks 发票数据并分析我们上个季度的收入。"
- "在我的 Shopify 商店中使用这些详细信息和定价设置一个产品。"
- "使用 Yahoo Finance 获取特斯拉的当前股价和历史数据。"
- "使用 FRED 经济数据分析过去五年的通货膨胀趋势。"
- "使用浏览器自动化填写 [网站 URL] 的表单。"
- "读取我下载文件夹中名为 'project_notes.txt' 的文本文件。"
- "获取有关技术的最新新闻头条。"

## 可用工具

### 文件系统工具
```

- `read_file`: 读取文件内容
- `read_multiple_files`: 同时读取多个文件
- `write_file`: 创建或覆盖文件
- `edit_file`: 对文件进行基于行的编辑
- `create_directory`: 创建新目录
- `list_directory`: 获取目录内容
- `directory_tree`: 获取递归树视图
- `move_file`: 移动或重命名文件/目录
- `search_files`: 搜索匹配模式的文件
- `get_file_info`: 获取文件元数据
- `list_allowed_directories`: 列出允许访问的目录

- **Browser_Automation:**
  - `playwright_launch_browser`: 启动新的浏览器实例
  - `playwright_navigate`: 导航到指定 URL
  - `playwright_screenshot`: 截图
  - `playwright_click`: 点击元素
  - `playwright_fill`: 填充输入字段
  - `playwright_evaluate`: 执行 JavaScript
  - `playwright_get_content`: 获取页面的 HTML 内容

### Agent Tools
- `run_agent`: 使用参数执行已注册的代理
- `list_agents`: 列出所有可用代理及其元数据

### Financial Data Tools
- **Yahoo Finance:**
  - `yfinance`: 获取股票报价和历史数据
  - `yfinance_get_quote`: 获取当前股票报价
  - `yfinance_get_history`: 获取历史股票数据
  - `yfinance_get_info`: 获取详细的公司信息
  - `yfinance_get_options`: 获取期权链数据
  - `yfinance_get_recommendations`: 获取分析师推荐

- **FRED (Federal Reserve Economic Data):**
  - `fred_get_series`: 获取经济数据系列
  - `fred_get_series_info`: 获取关于数据系列的元数据
  - `fred_search`: 搜索经济数据系列
  - `fred_get_category`: 按类别浏览数据
  - `fred_get_releases`: 获取经济数据发布
  - `fred_get_sources`: 获取数据来源

### Time Tools
- `get_current_time`: 获取指定时区的当前时间
- `convert_time`: 在不同时区之间转换时间

### Sequential Thinking
- `sequentialthinking`: 通过逐步思考过程分解复杂问题的工具

### Brave Search
- `brave_web_search`: 执行网络搜索
- `brave_local_search`: 搜索本地商家和地点

### World Bank API
- `worldbank_get_indicator`: 获取国家的指标数据

### News API
- `news_top_headlines`: 获取头条新闻
- `news_search`: 搜索新闻文章
- `news_sources`: 列出可用的新闻来源

### PowerPoint Tools
- `ppt_create_presentation`: 创建新的 PowerPoint 演示文稿
- `ppt_open_presentation`: 打开现有的演示文稿
- `ppt_save_presentation`: 保存演示文稿
- `ppt_add_slide`: 添加新幻灯片
- `ppt_add_text`: 向幻灯片添加文本
- `ppt_add_image`: 向幻灯片添加图片
- `ppt_add_chart`: 向幻灯片添加图表
- `ppt_add_table`: 向幻灯片添加表格
- `ppt_analyze_presentation`: 分析演示文稿结构
- `ppt_enhance_presentation`: 提出改进意见
- `ppt_generate_presentation`: 从文本生成演示文稿
- `ppt_command`: 处理自然语言命令

对于可用工具的完整列表，请参阅文档或浏览 tools 目录。
对于可用工具的完整列表，请参阅文档或浏览 tools 目录。

### 添加新的工具模块

1. 在 `tools` 目录中创建一个新文件（例如 `my_tool.py`）
2. 遵循现有的模块模式：
   - 创建服务类
   - 定义工具函数
   - 实现注册函数
3. 更新 `mcp_unified_server.py` 以导入并注册您的新模块

### 扩展现有工具模块

1. 向服务类中添加新方法
2. 添加新的工具函数
3. 更新注册函数以包含您的新工具

### 使用 Docker 进行开发

您可以使用 Docker 进行开发，以确保环境的一致性：

```
#10
```

这会将您的本地仓库挂载到容器中，因此对代码的更改会立即反映出来（对大多数文件有效）。

## 哲学视角：人机认知伙伴关系

MCP 工具包代表了我们在构想人类智能与 AI 系统之间关系方面的范式转变。它不仅仅将 AI 视为任务自动化的工具，而是建立了一种认知伙伴关系，在这种关系中，人类的战略思维与 AI 的操作能力在深层次上互相补充。

代理架构体现了一种变革性的愿景：AI 系统能够独立地解释上下文、在限定参数内做出决策，并执行复杂的行动序列——同时保持人类的监督和战略方向。这不仅代表了一项技术进步，而且是一种全新的人机协作模型。

在这个不断发展的认知领域中，最成功的实现将是那些深思熟虑地平衡技术潜力与人类能力的项目，创造出增强而非取代人类决策和创造力的接口。

## 故障排除

- **模块未加载**：检查导入路径和依赖项
- **API 密钥错误**：验证 `.env` 文件中的 API 密钥
- **权限错误**：检查 `MCP_FILESYSTEM_DIRS` 中允许的目录
- **连接错误**：确保服务器正在运行并且端口可访问
- **代理未检测到**：验证代理文件位于正确的目录中并且遵循所需格式
- **路径问题**：确保按照以下说明将 git 添加到 PATH 中

#要在 Windows 上将 Git 添加到 PATH，请执行以下步骤：

1) 查找 Git 安装位置：确定系统上 Git 的安装路径。对于标准的 Git 安装，常见路径包括 `C:\Program Files\Git\bin\git.exe` 和 `C:\Program Files\Git\cmd`；如果你是通过 GitHub for Windows 或 GitHub Desktop 安装的 Git，则可能是 `C:\Users\\AppData\Local\GitHub\PortableGit_\bin` 和 `C:\Users\\AppData\Local\GitHub\PortableGit_\cmd`。

2) 编辑环境变量：通过控制面板或在开始菜单中搜索“编辑系统环境变量”来打开“编辑环境变量”应用程序。在“系统变量”部分找到“Path”变量，点击“编辑...”，然后添加 Git 可执行文件和命令文件的路径。确保分隔路径的分号前后没有空格。

3) 保存更改：添加 Git 路径后，点击“确定”以保存更改。关闭并重新打开任何命令提示符窗口以应用新的 PATH 设置。

4) 验证安装：打开命令提示符并运行 `git --version` 来验证 Git 是否可以从命令行访问。

## 许可证

MCP Unified Server 使用 MIT 许可证。

## 致谢

本项目使用了多个开源库和 API：
- MCP SDK 用于 Claude AI 助手
- NewsAPI 用于新闻访问
- Brave Search API 用于网页搜索
- World Bank API 用于经济数据
- python-pptx 用于 PowerPoint 操作
- XlsxWriter 用于 Excel 电子表格
```

**官方网站：** [https://github.com/getfounded/mcp-tool-kit](https://github.com/getfounded/mcp-tool-kit)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`, `browser`, `files`
- 标签：`file systems`, `browser automation`, `developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`docker`
- 参数：`exec -i mcp-server python mcp_server_v2.py`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/getfounded-tool-kit.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
