---
title: "lanhu_mcp"
description: "让所有 AI 助手共享团队知识，打破 AI IDE 孤岛 lanhumcp | 蓝湖mcp | lanhu-mcp | 蓝湖AI助手 | Lanhu AI Integration | 简体中文 • • • --- 一个功能强大的 服务器，专为 AI 编程时代设计，完美支持蓝湖（Lanhu）设计协作平台。"
---

# lanhu_mcp

让所有 AI 助手共享团队知识，打破 AI IDE 孤岛 lanhumcp | 蓝湖mcp | lanhu-mcp | 蓝湖AI助手 | Lanhu AI Integration | 简体中文 • • • --- 一个功能强大的 服务器，专为 AI 编程时代设计，完美支持蓝湖（Lanhu）设计协作平台。

# 🎨 Lanhu MCP Server | Lanhu MCP Server

**Enable all AI assistants to share team knowledge, breaking the AI IDE silos**

**lanhumcp | lanhu-mcp | Lanhu AI Assistant | Lanhu AI Integration**

[![License: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](/mcp-assets/405b7b46d001e379991916d79670861b.svg)](https://www.python.org/downloads/)
[![MCP](/mcp-assets/dea21ef1b755e12c928a6fd915869854.svg)](https://modelcontextprotocol.io/)
[![FastMCP](/mcp-assets/62e03a3653b5d2a2e895382a3c0492f1.svg)](https://github.com/jlowin/fastmcp)
[![PRs Welcome](/mcp-assets/3a842c6d5613289cab55f6aa03bd7913.svg)](https://github.com/dsphper/lanhu-mcp/blob/HEAD/CONTRIBUTING.md)
[![GitHub Stars](/mcp-assets/16deb8e3fbd721640cf361c659029595.svg)](https://github.com/dsphper/lanhu-mcp/stargazers)
[![GitHub Issues](/mcp-assets/4e7573d76ec265100cb0896089de7a40.svg)](https://github.com/dsphper/lanhu-mcp/issues)
[![GitHub Release](/mcp-assets/089fede281ea337871e95583ebe72473.svg)](https://github.com/dsphper/lanhu-mcp/releases)
![Code of Conduct](/mcp-assets/b5d660e0196c9344304a881319d6b500.svg)

[English](https://github.com/dsphper/lanhu-mcp/blob/HEAD/README_EN.md) | Simplified Chinese

[Quick Start](#-quick-start) • [Key Features](#-key-features) • [Usage Guide](#-usage-guide) • [Contribution Guide](https://github.com/dsphper/lanhu-mcp/blob/HEAD/CONTRIBUTING.md)

---

## 🌟 Project Highlights

A powerful [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server, designed for the AI programming era, perfectly supporting the Lanhu (Lanhu) design collaboration platform.

🔥 **Core Innovations**:
- 📋 **Intelligent Requirement Analysis**: Automatically extracts Axure prototypes, three analysis modes (Development/Testing/Exploration), requirement analysis accuracy >95%
- 💬 **Team Knowledge Base**: Breaks down AI IDE silos, allowing all AI assistants to share the knowledge base and context
- 🎨 **UI Design Support**: Automatically downloads design drafts, intelligently extracts slices, and semantically names them
- ⚡ **Performance Optimization**: Intelligent caching based on version numbers, incremental updates, and concurrent processing

🎯 **Use Cases**:
- ✅ Cursor + Lanhu: Allows Cursor AI to directly read Lanhu requirement documents and design drafts
- ✅ Windsurf + Lanhu: Windsurf Cascade AI directly reads Lanhu requirement documents and design drafts
- ✅ Claude Code + Lanhu: Claude AI directly reads Lanhu requirement documents and design drafts
- ✅ Trae + Lanhu: Trae AI directly reads Lanhu requirement documents and design drafts
- ✅ Tongyi Lingma + Lanhu: Tongyi Lingma AI directly reads Lanhu requirement documents and design drafts
- ✅ Cline + Lanhu: Cline AI directly reads Lanhu requirement documents and design drafts
- ✅ Any AI development tool that supports the MCP protocol

🎯 **Pain Points Solved**:
- ❌ **Old World**: Each developer's AI works independently, repeatedly analyzing requirements, unable to share experiences
- ✅ **New World**: All AIs connect to the same knowledge hub, requirements are analyzed once and reused by everyone, and experience is permanently preserved

---
## 📑 Table of Contents

- [Key Features](#-key-features)
- [Quick Start](#-quick-start)
- [Team Message Board: Breaking the Last Mile in AI Collaboration](#-team-message-board-breaking-the-last-mile-in-ai-collaboration)
- [Usage Guide](#-usage-guide)
- [List of Available Tools](#-list-of-available-tools)
- [System Architecture](#-system-architecture)
- [Project Structure](#-project-structure)
- [Advanced Configuration](#-advanced-configuration)
- [Performance Metrics](#-performance-metrics)
- [Frequently Asked Questions](#-frequently-asked-questions)
- [Security Notes](#-security-notes)
- [Contribution Guide](#-contribution-guide)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)
- [Contact Information](#-contact-information)
- [Roadmap](#-roadmap)

---

## ✨ Key Features

### 📋 Requirement Document Analysis
- **Intelligent Document Extraction**: Automatically downloads and parses all pages, resources, and interactions from Axure prototypes
- **Three Analysis Modes**:
  - 🔧 **Development Perspective**: Detailed field rules, business logic, global flowcharts
  - 🧪 **Testing Perspective**: Test scenarios, test cases, boundary values, validation rules
  - 🚀 **Rapid Exploration**: Overview of core functionalities, module dependencies, review highlights
- **Four-Stage Workflow**: Global Scan → Group Analysis → Reverse Verification → Generate Deliverables
- **Zero Omission Guarantee**: Systematic analysis process driven by TODOs

### 🎨 UI Design Support
- **Design Draft Viewing**: Batch download and display of UI design images
- **Slice Extraction**: Automatic identification and export of design slices and icon resources
- **Intelligent Naming**: Automatically generates semantic file names based on layer paths

### 💬 Team Collaboration Message Board - Breaking Down AI IDE Silos> 🌟 **Core Innovation**: Enable every developer's AI assistant to share team knowledge and context

**Problem Background**:
- Each developer's AI IDE (Cursor, Windsurf) is independent and cannot share context.
- The pitfalls encountered by Developer A are unknown to Developer B's AI.
- The results of requirement analysis cannot be passed on to the tester's AI.
- Team knowledge is fragmented across various chat windows and cannot be consolidated.

**Innovative Solution**:
- 🔗 **Unified Knowledge Base**: All AI assistants connect to the same MCP server, sharing bulletin board data.
- 🧠 **Context Transfer**: Requirements analyzed by the development AI can be directly queried and used by the testing AI.
- 💡 **Knowledge Accumulation**: Pitfalls, experiences, and best practices are permanently saved as "knowledge base" entries.
- 📋 **Task Collaboration**: Use "task" type messages to have the AI help with code and database queries.
- 📨 **@Mention Mechanism**: Supports Feishu notifications, integrating AI collaboration with human communication.
- 👥 **Collaboration Tracking**: Automatically records which AI has accessed which documents, ensuring team transparency.

### ⚡ Performance Optimization
- **Smart Caching**: Permanent caching mechanism based on document version numbers.
- **Incremental Updates**: Only download changed resources.
- **Concurrent Processing**: Supports batch page screenshots and resource downloads.

## 🚀 Quick Start

> ⚠️ **Important Note: Must use an AI model that supports visual features!**
>
> This project requires the AI model to have **image recognition and analysis capabilities**. We recommend using the following mainstream visual models in 2026:
> - 🤖 **Claude** (Anthropic)
> - 🌟 **GPT** (OpenAI)
> - 💎 **Gemini** (Google)
> - 🚀 **Kimi** (Dark Side of the Moon)
> - 🎯 **Qwen** (Alibaba)
> - 🧠 **DeepSeek** (DeepSeek)
>
> Pure text models (such as GPT-3.5, Claude Instant, etc.) are not supported.

---

> 💡 **New User?** Just tell the AI "Help me clone and install the https://github.com/dsphper/lanhu-mcp project," and the AI will guide you through all the steps!

### Method One: Let the AI Help You Install (Recommended)

Directly tell the AI in Cursor:
plaintext
```
"帮我克隆并安装 https://github.com/dsphper/lanhu-mcp 项目"
```
The AI will automatically complete: Cloning the project → Installing dependencies → Guiding you to get the Cookie → Configuring and starting the service

📖 Reference Documents: [AI Installation Guide](https://github.com/dsphper/lanhu-mcp/blob/HEAD/ai-install-guide.md) • [Cookie Acquisition Tutorial](https://github.com/dsphper/lanhu-mcp/blob/HEAD/GET-COOKIE-TUTORIAL.md)

---

### Method Two: Manual Installation

**2.1 Docker Deployment (Recommended)**

Advantages: Environment isolation, one-click deployment, easy management

plaintext
```bash
# 1. 克隆项目
git clone https://github.com/dsphper/lanhu-mcp.git
cd lanhu-mcp

# 2. 配置环境（会引导你输入 Cookie）
bash setup-env.sh        # Linux/Mac
# 或
setup-env.bat           # Windows

# 3. 启动服务
docker-compose up -d
```
> 💡 `setup-env.sh` will interactively guide you to obtain and configure the Lanhu Cookie, generating the `.env` file automatically.

📖 Detailed Documentation: [Docker Deployment Guide](https://github.com/dsphper/lanhu-mcp/blob/HEAD/DEPLOY.md)

**2.2 Running from Source Code**

Prerequisites: Python 3.10+

plaintext
```bash
# 1. 克隆项目
git clone https://github.com/dsphper/lanhu-mcp.git
cd lanhu-mcp

# 2. 一键安装（推荐，会引导你配置 Cookie）
bash easy-install.sh        # Linux/Mac
# 或
easy-install.bat           # Windows
```
> 💡 `easy-install.sh` will automatically install dependencies, guide you to get the Cookie, and configure the environment.

Or manual installation (not recommended)

plaintext
```bash
# 安装依赖
pip install -r requirements.txt
playwright install chromium

# 手动配置（见下方"配置"部分）
```

### Configuration (Required for Running from Source Code)

1. **Set Lanhu Cookie** (Required)

plaintext
```bash
export LANHU_COOKIE="your_lanhu_cookie_here"
```
> 💡 To get the Cookie: Log in to the Lanhu web version, open the browser developer tools, and copy the Cookie from the request headers.

2. **Configure Feishu Bot** (Optional)

**Method One: Environment Variables (Recommended, supports Docker)**
plaintext
```bash
export FEISHU_WEBHOOK_URL="https://open.feishu.cn/open-apis/bot/v2/hook/your-webhook-url"
```
**Method Two: Modify the Code**
Modify in `lanhu_mcp_server.py`:
plaintext
```python
DEFAULT_FEISHU_WEBHOOK = "https://open.feishu.cn/open-apis/bot/v2/hook/your-webhook-url"
```
3. **Configure User Information Mapping** (Optional)

Update the `FEISHU_USER_ID_MAP` dictionary to support @mention functionality.

4. **Other Environment Variables** (Optional)

plaintext
```bash
# 服务器配置
export SERVER_HOST="0.0.0.0"       # 服务器监听地址
export SERVER_PORT=8000            # 服务器端口

# 数据存储
export DATA_DIR="./data"           # 数据存储目录

# 性能调优
export HTTP_TIMEOUT=30             # HTTP请求超时时间（秒）
export VIEWPORT_WIDTH=1920         # 浏览器视口宽度
export VIEWPORT_HEIGHT=1080        # 浏览器视口高度

# 调试选项
export DEBUG="false"               # 调试模式（true/false）
```
> 📝 For a full list of environment variables, refer to the `config.example.env` file.

### Run the Service

**Running from Source Code:**
plaintext
```bash
python lanhu_mcp_server.py
```
**Running with Docker:**
plaintext
```bash
docker-compose up -d              # 启动
docker-compose logs -f            # 查看日志
docker-compose down              # 停止
```
The server will start at `http://localhost:8000/mcp`

### Connect to AI Client

Configure in the AI client that supports MCP (e.g., Claude Code, Cursor, Windsurf):

**Cursor Configuration Example:**
plaintext
```json
{
  "mcpServers": {
    "lanhu": {
      "url": "http://localhost:8000/mcp?role=test&name=123"
    }
  }
}
```
> 📌 URL Parameter Explanation:
> - `role`: User role (backend/frontend/testing/product, etc.)
> - `name`: User name (for collaboration tracking and @mentions)

## 🎯 Team Bulletin Board: Breaking the Last Mile in AI Collaboration

### Why Do We Need a Team Bulletin Board?

In the era of AI programming, each developer has their own AI assistant (Cursor, Windsurf, Claude Code). However, this brings a **serious problem**:

plaintext
PLACEHOLDER_CODE_11**Every AI is doing repetitive work, unable to reuse the analysis results of other AIs!**

### How Does the Team Message Board Solve This?

**Design Philosophy: Let all AI assistants connect to the same "brain"**

```

          ┌─────────────────────────────┐

          │   Lanhu MCP Server          │

          │   (统一知识中枢)             │

          │                             │

          │  📊 需求分析结果             │

          │  🐛 开发踩坑记录             │

          │  📋 测试用例模板             │

          │  💡 技术决策文档             │

          └──────────┬──────────────────┘

                     │

        ┌────────────┼────────────┐

        │            │            │

   ┌────▼───┐   ┌───▼────┐   ┌──▼─────┐

   │后端 AI │   │前端 AI │   │测试 AI │

   │(小王)  │   │(小张)  │   │(小李)  │

   └────────┘   └────────┘   └────────┘

     Cursor      Windsurf     Claude

```
### Core Use Cases

#### Scenario 1: Sharing Requirement Analysis Results

**After the backend AI (Xiao Wang) completes the requirement analysis:**
```
@测试小李 @前端小张 我已经分析完"用户登录"需求，关键信息：
- 手机号必填，11位数字
- 密码6-20位，必须包含字母+数字
- 验证码4位纯数字，5分钟有效
- 错误3次锁定30分钟

[消息类型：knowledge]
```
**When the testing AI (Xiao Li) queries:**
```
AI: 查询所有关于"登录"的知识库消息
→ 立即获取小王 AI 的分析结果，无需重新看需求！
```
#### Scenario 2: Recording Development Pitfalls

**When the backend AI (Xiao Wang) encounters a pitfall:**
```
【知识库】Redis连接超时问题已解决

问题：生产环境 Redis 频繁超时
原因：连接池配置不当，maxIdle 设置过小
解决：调整为 maxTotal=20, maxIdle=10

[消息类型：knowledge]
```
**When other development AIs encounter the same issue:**
```
AI: 搜索"Redis 超时"相关的知识库
→ 找到解决方案，避免重复踩坑！
```
#### Scenario 3: Cross-Role Task Collaboration

**When the product AI initiates a query task:**
```
@后端小王 请帮我查一下数据库中 user 表有多少条测试数据？

[消息类型：task]  // ⚠️ 安全限制：只能查询，不能修改
```
**When the backend AI (Xiao Wang) sees the notification:**
```
AI: 有人 @我了，查看详情
→ 执行 SELECT COUNT(*) FROM user WHERE status='test'
→ 回复留言：共有 1234 条测试数据
```
#### Scenario 4: Broadcasting Urgent Issues

**When the operations AI discovers a production issue:**
```
🚨 紧急：生产环境支付接口异常，请立即排查！

时间：2026-01-15 14:30
现象：支付成功率从 99% 降至 60%
影响：约 200 笔订单受影响

@所有人

[消息类型：urgent]
→ 自动发送飞书通知给所有人
```
### Message Type Design

| Type | Purpose | Search Strategy | Lifecycle |
|------|---------|-----------------|-----------|
| 📢 **normal** | General notifications | Decays over time | Archived after 7 days |
| 📋 **task** | Query tasks (security restriction: read-only) | Archived upon completion | Task lifecycle |
| ❓ **question** | Questions requiring answers | Pinned until answered | Archived after answering |
| 🚨 **urgent** | Urgent notifications | Forced push | Downgraded after 24 hours |
| 💡 **knowledge** | **Knowledge base (core)** | **Permanently searchable** | **Permanently stored** |

### Security Mechanisms

**Security restrictions for task type (task):**
```python
✅ 允许的查询操作：
- 查询代码位置、代码逻辑
- 查询数据库表结构、数据
- 查询测试方法、覆盖率
- 查询 TODO、注释

❌ 禁止的危险操作：
- 修改代码
- 删除文件
- 执行命令
- 提交代码
```
### Search and Filtering

**Smart search (to prevent context overflow):**
```python
# 场景 1：查询所有测试相关的知识库
lanhu_say_list(
    url='all',  # 全局搜索
    filter_type='knowledge',
    search_regex='测试|test|单元测试',
    limit=20
)

# 场景 2：查询某个项目的紧急消息
lanhu_say_list(
    url='项目URL',
    filter_type='urgent',
    limit=10
)

# 场景 3：查找未解决的问题
lanhu_say_list(
    url='all',
    filter_type='question',
    search_regex='待解决|pending'
)
```
### Collaborator Tracking

**Automatically record team member access history:**
```python
lanhu_get_members(url='项目URL')

返回结果：
{
  "collaborators": [
    {
      "name": "小王",
      "role": "后端",
      "first_seen": "2026-01-10 09:00:00",
      "last_seen": "2026-01-15 16:30:00"
    },
    {
      "name": "小李",
      "role": "测试",
      "first_seen": "2026-01-12 10:00:00",
      "last_seen": "2026-01-15 14:00:00"
    }
  ]
}

💡 用途：
- 了解哪些同事的 AI 看过这个需求
- 发现潜在的协作伙伴
- 团队透明化
```
### Feishu Notification Integration

**Bridge AI collaboration with human communication:**

```python

# AI 自动发送飞书通知（当 @某人时）

lanhu_say(

    url='项目URL',

    summary='需要你帮忙review代码',

    content='登录模块的密码加密逻辑，麻烦看一下',

    mentions=['小王', '小张']  # 必须是真实姓名

)

# 飞书群收到：

┌──────────────────────────────────┐

│ 📢 蓝湖协作通知                   │

│                                  │

│ 👤 发布者：小李（测试）           │

│ 📨 提醒：@小王 @小张              │

│ 🏷️ 类型：normal                  │

│ 📁 项目：用户中心改版             │

│ 📄 文档：登录注册模块             │

│                                  │

│ 📝 内容：                        │

│ 登录模块的密码加密逻辑，麻烦看一下 │

│                                  │

│ 🔗 查看需求文档                   │

└──────────────────────────────────┘

```
### Technical Advantages

1. **Zero learning cost**: AI handles everything, developers only need to converse naturally
2. **Real-time synchronization**: All AI assistants connected to the same data source
3. **Global search**: Cross-project knowledge base queries
4. **Version association**: Messages automatically linked to document version numbers
5. **Complete metadata**: Automatically records 10 standard fields such as project, document, and author
6. **Intelligent filtering**: Supports regex search, type filtering, and quantity limits (to prevent token overflow)

---

## 📖 User Guide

### Requirement Document Analysis Workflow

**1. Get page list**
```
请帮我看看这个需求文档：
https://lanhuapp.com/web/#/item/project/product?tid=xxx&pid=xxx&docId=xxx
```
**2. AI automatically performs four-stage analysis**
- ✅ STAGE 1: Global text scan to establish overall understanding
- ✅ STAGE 2: Detailed group analysis (based on selected mode)
- ✅ STAGE 3: Reverse validation to ensure no omissions
- ✅ STAGE 4: Generate deliverable documents (requirement document/test plan/review PPT)

**3. Obtain deliverables**
- Developer perspective: Detailed requirement document + global business process diagram
- Tester perspective: Test plan + test case list + field validation table
- Quick exploration: Review document + module dependency diagram + discussion points

### Viewing UI Design Drafts

```

请帮我看看这个设计稿：

https://lanhuapp.com/web/#/item/project/stage?tid=xxx&pid=xxx

```
### Slicing and Downloading

```

帮我下载"首页设计"的所有切图

```
AI will automatically:
1. Detect project type (React/Vue/Flutter, etc.)
2. Choose the appropriate output directory
3. Generate semantic file names
4. Batch download slices

### Team Messaging

**Post a message:**
```
@张三 @李四 这个登录页面的密码校验规则需要确认一下
```
**View messages:**
```
查看所有 @我的消息
```
**Filter and query:**
```
查看所有关于"测试"的知识库类型留言
```
## 🛠️ Available Tools List

| Tool Name | Function Description | Usage Scenario |
|-----------|----------------------|----------------|
| `lanhu_resolve_invite_link` | Resolve invitation link | When user provides a shared link |
| `lanhu_get_pages` | Get prototype page list | Must be called before analyzing requirement documents |
| `lanhu_get_ai_analyze_page_result` | Analyze prototype page content | Extract requirement details |
| `lanhu_get_designs` | Get UI design list | Must be called before viewing design drafts |
| `lanhu_get_ai_analyze_design_result` | Analyze UI designs | View design drafts |
| `lanhu_get_design_slices` | Get slice information | Download icons and materials |
| `lanhu_say` | Post a message | Team collaboration, @ mentions |
| `lanhu_say_list` | View message list | Query historical messages |
| `lanhu_say_detail` | View message details | View full content |
| `lanhu_say_edit` | Edit a message | Modify published messages |
| `lanhu_say_delete` | Delete a message | Remove messages || `lanhu_get_members` | View Collaborators | View Team Members |

## 🏗️ System Architecture

```

┌─────────────────────────────────────────────────────────────────┐

│                         AI 客户端层                              │

│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐       │

│  │ Cursor   │  │ Windsurf │  │  Claude  │  │   ...    │       │

│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘       │

│       │             │              │             │              │

│       └─────────────┴──────────────┴─────────────┘              │

└───────────────────────────┬─────────────────────────────────────┘

                            │ MCP Protocol (HTTP)

                            │

┌───────────────────────────▼─────────────────────────────────────┐

│                    Lanhu MCP Server                              │

│                                                                  │

│  ┌────────────────────────────────────────────────────────┐    │

│  │              FastMCP 服务框架                           │    │

│  │  ┌──────────┐  ┌──────────┐  ┌───────────────────┐   │    │

│  │  │ Tool API │  │ Resource │  │  Context Provider  │   │    │

│  │  └────┬─────┘  └────┬─────┘  └─────────┬─────────┘   │    │

│  └───────┼─────────────┼──────────────────┼─────────────┘    │

│          │             │                  │                    │

│  ┌───────▼─────────────▼──────────────────▼─────────────┐    │

│  │              核心业务逻辑层                            │    │

│  │                                                        │    │

│  │  ┌─────────────
```

**Official site: ** [https://github.com/dsphper/lanhu-mcp](https://github.com/dsphper/lanhu-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `developer tools`, `chinese`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/aiunite-lanhu.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
