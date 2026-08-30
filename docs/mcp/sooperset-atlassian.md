---
title: "MCP Atlassian工具"
description: "Model Context Protocol (MCP) 服务器适用于 Atlassian Cloud 产品（Confluence 和 Jira）。此集成是专门为 Atlassian Cloud 实例设计的，不支持 Atlassian Server 或 Data Center 部署。"
---

# MCP Atlassian工具

Model Context Protocol (MCP) 服务器适用于 Atlassian Cloud 产品（Confluence 和 Jira）。此集成是专门为 Atlassian Cloud 实例设计的，不支持 Atlassian Server 或 Data Center 部署。

# MCP Atlassian

![PyPI Version](/mcp-assets/70c34732cb7c08d25b33412d96c854c2.svg)
![PyPI - Downloads](/mcp-assets/534c417bc36a0e78ef942b38b8523bb4.svg)
![PePy - Total Downloads](/mcp-assets/31d34999f0b703a47ffbb660990b858b.svg)
![License](/mcp-assets/5816f652aa1f0cc4eedb21a2f733e09e.svg)

用于Atlassian产品（Confluence和Jira）的Model Context Protocol (MCP)服务器。此集成同时支持Confluence & Jira Cloud以及Server/Data Center部署。

### 功能演示
![Jira 演示](/mcp-assets/61dba7a150323888b4ffffc9a9d3734d.gif)

Confluence 演示

![Confluence 演示](/mcp-assets/44e49275d5a90aaad801912c27834211.gif)

### 兼容性

| 产品 | 部署类型 | 支持状态              |
|---------|----------------|-----------------------------|
| **Confluence** | 云端 | ✅ 完全支持           |
| **Confluence** | 服务器/数据中心 | ✅ 支持 (版本7.9+)  |
| **Jira** | 云端 | ✅ 完全支持           |
| **Jira** | 服务器/数据中心 | ✅ 支持 (版本8.14+) |

## 设置指南

### 1. 认证设置

首先，为Confluence & Jira生成必要的认证令牌：

#### 对于云端
1. 前往 https://id.atlassian.com/manage-profile/security/api-tokens
2. 点击 **创建API令牌**，命名它
3. 立即复制令牌

#### 对于服务器/数据中心
1. 进入您的个人资料（头像）→ **个人资料** → **个人访问令牌**
2. 点击 **创建令牌**，命名它，设置过期时间
3. 立即复制令牌

### 2. 安装

选择以下安装方法之一：

```bash
# Using uv (recommended)
brew install uv
uvx mcp-atlassian

# Using pip
pip install mcp-atlassian

# Using Docker
git clone https://github.com/sooperset/mcp-atlassian.git
cd mcp-atlassian
docker build -t mcp/atlassian .
```

### 3. 配置与使用

您可以使用命令行参数来配置MCP服务器。该服务器支持使用Confluence、Jira或两者服务 - 根据您的使用情况仅包含所需的参数。

#### 必需参数

对于云端：
```bash
uvx mcp-atlassian \
  --confluence-url https://your-company.atlassian.net/wiki \
  --confluence-username your.email@company.com \
  --confluence-token your_api_token \
  --jira-url https://your-company.atlassian.net \
  --jira-username your.email@company.com \
  --jira-token your_api_token
```

对于服务器/数据中心：
```bash
uvx mcp-atlassian \
  --confluence-url https://confluence.your-company.com \
  --confluence-personal-token your_token \
  --jira-url https://jira.your-company.com \
  --jira-personal-token your_token
```

> **注意：** 您可以只配置Confluence，只配置Jira，或者同时配置两者。只需包含您要使用的服务的参数即可。例如，如果您只想使用Confluence云端，那么只需要`--confluence-url`、`--confluence-username`和`--confluence-token`。

#### 可选参数

- `--transport`: 选择传输类型 (`stdio` [默认] 或 `sse`)
- `--port`: SSE 传输的端口号 (默认: 8000)
- `--[no-]confluence-ssl-verify`: 切换 Confluence Server/DC 的 SSL 验证
- `--[no-]jira-ssl-verify`: 切换 Jira Server/DC 的 SSL 验证
- `--confluence-spaces-filter`: 逗号分隔的空间键列表，用于过滤 Confluence 搜索结果（例如："DEV,TEAM,DOC"）
- `--jira-projects-filter`: 逗号分隔的项目键列表，用于过滤 Jira 搜索结果（例如："PROJ,DEV,SUPPORT"）
- `--read-only`: 以只读模式运行（禁用所有写操作）
- `--verbose`: 增加日志详细程度（可以多次使用，默认级别为 WARNING）
  - `-v` 或 `--verbose`: 将日志设置为 INFO 级别
  - `-vv` 或 `--verbose --verbose`: 将日志设置为 DEBUG 级别

> **注意：** 所有配置选项也可以通过环境变量设置。请参阅仓库中的 `.env.example` 文件以获取可用环境变量的完整列表。

## IDE 集成

### Claude 桌面设置

使用 uvx（推荐）- 云：

```json
{
  "mcpServers": {
    "mcp-atlassian": {
      "command": "uvx",
      "args": [
        "mcp-atlassian",
        "--confluence-url=https://your-company.atlassian.net/wiki",
        "--confluence-username=your.email@company.com",
        "--confluence-token=your_api_token",
        "--jira-url=https://your-company.atlassian.net",
        "--jira-username=your.email@company.com",
        "--jira-token=your_api_token"
      ]
    }
  }
}
```

使用 uvx（推荐）- 服务器/数据中心

```json
{
  "mcpServers": {
    "mcp-atlassian": {
      "command": "uvx",
      "args": [
        "mcp-atlassian",
        "--confluence-url=https://confluence.your-company.com",
        "--confluence-personal-token=your_token",
        "--jira-url=https://jira.your-company.com",
        "--jira-personal-token=your_token"
      ]
    }
  }
}
```

使用 pip

> 注意：以下示例使用的是云配置。对于服务器/数据中心，请使用相应的参数 (--confluence-personal-token, --jira-personal-token)，如上文配置部分所示。

```json
{
  "mcpServers": {
    "mcp-atlassian": {
      "command": "python",
      "args": [
        "-m",
        "mcp-atlassian",
        "--confluence-url=https://your-company.atlassian.net/wiki",
        "--confluence-username=your.email@company.com",
        "--confluence-token=your_api_token",
        "--jira-url=https://your-company.atlassian.net",
        "--jira-username=your.email@company.com",
        "--jira-token=your_api_token"
      ]
    }
  }
}
```

使用 docker

> 注意：以下示例使用的是云配置。对于服务器/数据中心，请使用相应的参数 (--confluence-personal-token, --jira-personal-token)，如上文配置部分所示。

有两种方法来配置 Docker 环境：

1. 直接在配置中使用命令行参数：
```json
{
  "mcpServers": {
    "mcp-atlassian": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "mcp/atlassian",
        "--confluence-url=https://your-company.atlassian.net/wiki",
        "--confluence-username=your.email@company.com",
        "--confluence-token=your_api_token",
        "--jira-url=https://your-company.atlassian.net",
        "--jira-username=your.email@company.com",
        "--jira-token=your_api_token"
      ]
    }
  }
}
```

2. 使用环境文件：
```json
{
  "mcpServers": {
    "mcp-atlassian": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "--env-file",
        "/path/to/your/.env",
        "mcp/atlassian"
      ]
    }
  }
}
```

### Cursor IDE 设置

1. 打开 Cursor 设置
2. 导航到 `功能` > `MCP 服务器`（或直接到 `MCP`）
3. 点击 `+ 添加新的全局 MCP 服务器`

这将创建或编辑 `~/.cursor/mcp.json` 文件，其中包含您的 MCP 服务器配置。

![Cursor MCP 配置](/mcp-assets/7454e87ad13115092aae5c745861c7fb.png)

#### stdio 传输的 JSON 配置

对于云：
```json
{
  "mcpServers": {
    "mcp-atlassian": {
      "command": "uvx",
      "args": [
        "mcp-atlassian",
        "--confluence-url=https://your-company.atlassian.net/wiki",
        "--confluence-username=your.email@company.com",
        "--confluence-token=your_api_token",
        "--jira-url=https://your-company.atlassian.net",
        "--jira-username=your.email@company.com",
        "--jira-token=your_api_token"
      ]
    }
  }
}
```

服务器/数据中心配置

```json
{
  "mcpServers": {
    "mcp-atlassian": {
      "command": "uvx",
      "args": [
        "mcp-atlassian",
        "--confluence-url=https://confluence.your-company.com",
        "--confluence-personal-token=your_token",
        "--jira-url=https://jira.your-company.com",
        "--jira-personal-token=your_token"
      ]
    }
  }
}
```

#### SSE 传输配置

对于 SSE 传输，首先启动服务器：
```bash
uvx mcp-atlassian --transport sse --port 9000
```

然后在 Cursor 中进行配置：
```json
{
  "mcpServers": {
    "mcp-atlassian-sse": {
      "url": "http://localhost:9000/sse",
      "env": {
        "CONFLUENCE_URL": "https://your-company.atlassian.net/wiki",
        "CONFLUENCE_USERNAME": "your.email@company.com",
        "CONFLUENCE_API_TOKEN": "your_api_token",
        "JIRA_URL": "https://your-company.atlassian.net",
        "JIRA_USERNAME": "your.email@company.com",
        "JIRA_API_TOKEN": "your_api_token"
      }
    }
  }
}
```

## 资源

> **注意：** MCP 服务器仅显示用户基于其贡献和分配而实际交互的 Confluence 空间和 Jira 项目。

- `confluence://{space_key}`: 访问 Confluence 空间
- `jira://{project_key}`: 访问 Jira 项目

## 可用工具

| 工具 | 描述 |
|------|-------------|
| `confluence_search` | 使用 CQL 搜索 Confluence 内容 |
| `confluence_get_page` | 获取特定 Confluence 页面的内容 |
| `confluence_get_page_children` | 获取特定 Confluence 页面的子页面 |
| `confluence_get_page_ancestors` | 获取特定 Confluence 页面的父页面 |
| `confluence_get_comments` | 获取特定 Confluence 页面的评论 |
| `confluence_create_page` | 创建新的 Confluence 页面 |
| `confluence_update_page` | 更新现有的 Confluence 页面 |
| `confluence_delete_page` | 删除现有的 Confluence 页面 |
| `jira_get_issue` | 获取特定 Jira 问题的详细信息 |
| `jira_search` | 使用 JQL 搜索 Jira 问题 |
| `jira_get_project_issues` | 获取特定 Jira 项目的所有问题 |
| `jira_create_issue` | 在 Jira 中创建新问题 |
| `jira_update_issue` | 更新现有的 Jira 问题 |
| `jira_delete_issue` | 删除现有的 Jira 问题 |
| `jira_get_transitions` | 获取 Jira 问题可用的状态转换 |
| `jira_transition_issue` | 将 Jira 问题转换到新状态 |
| `jira_add_worklog` | 向 Jira 问题添加工作日志条目 |
| `jira_get_worklog` | 获取 Jira 问题的工作日志条目 |
| `jira_link_to_epic` | 将问题链接到 Epic |
| `jira_get_epic_issues` | 获取链接到特定 Epic 的所有问题 |

## 开发与调试

### 本地开发设置

如果你已经克隆了仓库并希望运行本地版本：

对于云：
```json
{
  "mcpServers": {
    "mcp-atlassian": {
      "command": "uv",
      "args": [
        "--directory", "/path/to/your/mcp-atlassian",
        "run", "mcp-atlassian",
        "--confluence-url=https://your-domain.atlassian.net/wiki",
        "--confluence-username=your.email@domain.com",
        "--confluence-token=your_api_token",
        "--jira-url=https://your-domain.atlassian.net",
        "--jira-username=your.email@domain.com",
        "--jira-token=your_api_token"
      ]
    }
  }
}
```

### 调试工具

```bash
# Using MCP Inspector
# For installed package
npx @modelcontextprotocol/inspector uvx mcp-atlassian ...

# For local development version
npx @modelcontextprotocol/inspector uv --directory /path/to/your/mcp-atlassian run mcp-atlassian ...

# View logs
tail -n 20 -f ~/Library/Logs/Claude/mcp*.log
```

## 安全

- 永不分享 API 令牌
- 保持 .env 文件的安全性和私密性
- 请参阅 [SECURITY.md](https://github.com/sooperset/mcp-atlassian/blob/HEAD/SECURITY.md) 以获取最佳实践

## 许可证

根据 MIT 许可 - 详见 [LICENSE](https://github.com/sooperset/mcp-atlassian/blob/HEAD/LICENSE) 文件。这不是 Atlassian 的官方产品。

**官方网站：** [https://github.com/sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`communication`
- 标签：`communication`, `developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`mcp-atlassian --confluence-url=https://your-company.atlassian.net/wiki --confluence-username=your.email@company.com --confluence-token=your_api_token --jira-url=https://your-company.atlassian.net --jira-username=your.email@company.com --jira-token=your_api_token`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/sooperset-atlassian.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
