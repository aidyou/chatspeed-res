---
title: "GitLab 项目管理服务器"
description: "GitLab MCP服务器（具有活动跟踪和群组项目列表功能） 该服务器基于原始的GitLab MCP服务器，并增强了群组项目列表和活动跟踪功能。"
---

# GitLab 项目管理服务器

GitLab MCP服务器（具有活动跟踪和群组项目列表功能） 该服务器基于原始的GitLab MCP服务器，并增强了群组项目列表和活动跟踪功能。

# GitLab MCP 服务器

一个用于 GitLab 集成的 Model Context Protocol (MCP) 服务器，提供与 GitLab 仓库、问题、合并请求、维基等交互的工具。

## 功能

- 支持 stdio 和 SSE 传输
- 使用 MCP SDK 的严格 TypeScript 类型定义
- 全面的 GitLab API 集成
- 仓库操作（搜索、创建、分叉）
- 文件操作（读取、创建、更新）
- 分支操作（创建）
- 问题管理（创建、列出、筛选）
- 合并请求处理（创建、列出、筛选）
- 组项目列表
- 项目事件检索
- 提交历史访问
- 成员管理（列出项目和组成员）
- 完整的维基管理：
  - 项目维基支持（列出、获取、创建、编辑、删除页面）
  - 组维基支持（列出、获取、创建、编辑、删除页面）
  - 维基附件处理
  - 多种维基格式（markdown、rdoc、asciidoc、org）

## 安装

### 从 npm 安装（推荐）

```bash
npm install @yoda.digital/gitlab-mcp-server
```

### 从源码安装

```bash
# Clone the repository
git clone https://github.com/yourusername/mcp-gitlab-server.git
cd mcp-gitlab-server

# Install dependencies
npm install

# Build the project
npm run build
```

## 配置

### 环境变量

直接运行时，服务器需要以下环境变量：

- `GITLAB_PERSONAL_ACCESS_TOKEN`（必需）：您的 GitLab 个人访问令牌
- `GITLAB_API_URL`（可选）：GitLab API URL（默认为 'https://gitlab.com/api/v4'）
- `PORT`（可选）：用于 SSE 传输的端口（默认为 3000）
- `USE_SSE`（可选）：设置为 'true' 以使用 SSE 传输而不是 stdio（默认为 'false'）

### MCP 设置配置

您可以将 GitLab MCP 服务器添加到您的 MCP 设置文件中（例如 `cline_mcp_settings.json` 或 `claude_desktop_config.json`）：

```json
{
  "mcpServers": {
    "gitlab": {
      "command": "npx",
      "args": ["-y", "@yoda.digital/gitlab-mcp-server"],
      "env": {
        "GITLAB_PERSONAL_ACCESS_TOKEN": "your_token_here",
        "GITLAB_API_URL": "https://gitlab.com/api/v4"
      },
      "alwaysAllow": [],
      "disabled": false
    }
  }
}
```

## 使用

### 使用 stdio 传输运行（默认）

```bash
# Set your GitLab personal access token
export GITLAB_PERSONAL_ACCESS_TOKEN=your_token_here

# Run the server
npm start
```

### 使用 SSE 传输运行

```bash
# Set your GitLab personal access token and enable SSE
export GITLAB_PERSONAL_ACCESS_TOKEN=your_token_here
export USE_SSE=true
export PORT=3000  # Optional, defaults to 3000

# Run the server
npm start
```

### 使用 npx 运行

```bash
# Run directly with npx
GITLAB_PERSONAL_ACCESS_TOKEN=your_token_here npx @yoda.digital/gitlab-mcp-server
```

## 可用工具

服务器提供以下工具：

### 仓库操作

- `search_repositories`: 搜索 GitLab 项目

```json
  {
    "search": "project-name",
    "page": 1,
    "per_page": 20
  }
```

- `create_repository`: 创建一个新的 GitLab 项目

```json
  {
    "name": "new-project",
    "description": "A new project",
    "visibility": "private",
    "initialize_with_readme": true
  }
```

- `fork_repository`: 分叉一个 GitLab 项目

```json
  {
    "project_id": "username/project",
    "namespace": "target-namespace"
  }
```

- `list_group_projects`: 列出特定 GitLab 组中的所有项目
```json
  {
    "group_id": "group-name",
    "archived": false,
    "visibility": "public",
    "include_subgroups": true,
    "page": 1,
    "per_page": 20
  }
```

### 文件操作

- `get_file_contents`: 从 GitLab 项目中获取文件内容

```json
  {
    "project_id": "username/project",
    "file_path": "path/to/file.txt",
    "ref": "main"
  }
```

- `create_or_update_file`: 在 GitLab 项目中创建或更新单个文件

```json
  {
    "project_id": "username/project",
    "file_path": "path/to/file.txt",
    "content": "File content here",
    "commit_message": "Add/update file",
    "branch": "main",
    "previous_path": "old/path/to/file.txt"
  }
```

- `push_files`: 在单次提交中将多个文件推送到 GitLab 项目
```json
  {
    "project_id": "username/project",
    "files": [
      {
        "path": "file1.txt",
        "content": "Content for file 1"
      },
      {
        "path": "file2.txt",
        "content": "Content for file 2"
      }
    ],
    "commit_message": "Add multiple files",
    "branch": "main"
  }
```

### 分支操作

- `create_branch`: 在 GitLab 项目中创建新分支
```json
  {
    "project_id": "username/project",
    "branch": "new-branch",
    "ref": "main"
  }
```

### 问题操作

- `create_issue`: 在 GitLab 项目中创建新问题

```json
  {
    "project_id": "username/project",
    "title": "Issue title",
    "description": "Issue description",
    "assignee_ids": [1, 2],
    "milestone_id": 1,
    "labels": ["bug", "critical"]
  }
```

- `list_issues`: 获取具有过滤条件的 GitLab 项目中的问题
```json
  {
    "project_id": "username/project",
    "state": "opened",
    "labels": "bug,critical",
    "milestone": "v1.0",
    "author_id": 1,
    "assignee_id": 2,
    "search": "keyword",
    "created_after": "2023-01-01T00:00:00Z",
    "created_before": "2023-12-31T23:59:59Z",
    "updated_after": "2023-06-01T00:00:00Z",
    "updated_before": "2023-06-30T23:59:59Z",
    "page": 1,
    "per_page": 20
  }
```

### 合并请求操作

- `create_merge_request`: 在 GitLab 项目中创建新的合并请求

```json
  {
    "project_id": "username/project",
    "title": "Merge request title",
    "description": "Merge request description",
    "source_branch": "feature-branch",
    "target_branch": "main",
    "allow_collaboration": true,
    "draft": false
  }
```

- `list_merge_requests`: 获取具有过滤条件的 GitLab 项目中的合并请求
```json
  {
    "project_id": "username/project",
    "state": "opened",
    "order_by": "created_at",
    "sort": "desc",
    "milestone": "v1.0",
    "labels": "feature,enhancement",
    "created_after": "2023-01-01T00:00:00Z",
    "created_before": "2023-12-31T23:59:59Z",
    "updated_after": "2023-06-01T00:00:00Z",
    "updated_before": "2023-06-30T23:59:59Z",
    "author_id": 1,
    "assignee_id": 2,
    "search": "keyword",
    "source_branch": "feature-branch",
    "target_branch": "main",
    "page": 1,
    "per_page": 20
  }
```

### 项目活动

- `get_project_events`: 获取 GitLab 项目的最近事件/活动

```json
  {
    "project_id": "username/project",
    "action": "pushed",
    "target_type": "issue",
    "before": "2023-12-31T23:59:59Z",
    "after": "2023-01-01T00:00:00Z",
    "sort": "desc",
    "page": 1,
    "per_page": 20
  }
```

- `list_commits`: 获取 GitLab 项目的提交历史
```json
  {
    "project_id": "username/project",
    "sha": "branch-or-commit-sha",
    "path": "path/to/file",
    "since": "2023-01-01T00:00:00Z",
    "until": "2023-12-31T23:59:59Z",
    "all": true,
    "with_stats": true,
    "first_parent": true,
    "page": 1,
    "per_page": 20
  }
```

### 成员操作

- `list_project_members`: 列出 GitLab 项目的所有成员（包括继承的成员）

```json
  {
    "project_id": "username/project",
    "query": "search term",
    "page": 1,
    "per_page": 20
  }
```

- `list_group_members`: 列出 GitLab 组的所有成员（包括继承的成员）

```json
  {
    "group_id": "group-name",
    "query": "search term",
    "page": 1,
    "per_page": 20
  }
```

### 项目维基操作

- `list_project_wiki_pages`: 列出 GitLab 项目的所有维基页面

```json
  {
    "project_id": "username/project",
    "with_content": false
  }
```

- `get_project_wiki_page`: 获取 GitLab 项目的特定维基页面

```json
  {
    "project_id": "username/project",
    "slug": "page-slug",
    "render_html": false,
    "version": "commit-sha"
  }
```

- `create_project_wiki_page`: 为 GitLab 项目创建新的维基页面

```json
  {
    "project_id": "username/project",
    "title": "Page Title",
    "content": "Wiki page content",
    "format": "markdown"
  }
```

- `edit_project_wiki_page`: 编辑 GitLab 项目的现有维基页面

```json
  {
    "project_id": "username/project",
    "slug": "page-slug",
    "title": "New Page Title",
    "content": "Updated wiki page content",
    "format": "markdown"
  }
```

- `delete_project_wiki_page`: 从 GitLab 项目中删除一个维基页面

```json
  {
    "project_id": "username/project",
    "slug": "page-slug"
  }
```

- `upload_project_wiki_attachment`: 向 GitLab 项目维基上传附件
```json
  {
    "project_id": "username/project",
    "file_path": "path/to/attachment.png",
    "content": "base64-encoded-content",
    "branch": "main"
  }
```

### 组维基操作

- `list_group_wiki_pages`: 列出 GitLab 组的所有 wiki 页面

```json
  {
    "group_id": "group-name",
    "with_content": false
  }
```

- `get_group_wiki_page`: 获取 GitLab 组的特定 wiki 页面

```json
  {
    "group_id": "group-name",
    "slug": "page-slug",
    "render_html": false,
    "version": "commit-sha"
  }
```

- `create_group_wiki_page`: 为 GitLab 组创建新的 wiki 页面

```json
  {
    "group_id": "group-name",
    "title": "Page Title",
    "content": "Wiki page content",
    "format": "markdown"
  }
```

- `edit_group_wiki_page`: 编辑 GitLab 组中已存在的 wiki 页面

```json
  {
    "group_id": "group-name",
    "slug": "page-slug",
    "title": "New Page Title",
    "content": "Updated wiki page content",
    "format": "markdown"
  }
```

- `delete_group_wiki_page`: 从 GitLab 组中删除一个 wiki 页面

```json
  {
    "group_id": "group-name",
    "slug": "page-slug"
  }
```

- `upload_group_wiki_attachment`: 向 GitLab 组的 wiki 上传附件
```json
  {
    "group_id": "group-name",
    "file_path": "path/to/attachment.png",
    "content": "base64-encoded-content",
    "branch": "main"
  }
```

## 开发

### 构建项目

```bash
npm run build
```

### 运行测试

```bash
npm test
```

## 许可证

此项目根据 MIT 许可证发布 - 详情请参阅 [LICENSE](https://github.com/yoda-digital/mcp-gitlab-server/blob/HEAD/LICENSE) 文件。

## 贡献

欢迎贡献！请随时提交 Pull Request。

## 贡献者

感谢所有帮助改进此项目的贡献者：

- [thomasleveil](https://github.com/thomasleveil) - 实现了项目和组的 GitLab 成员列表功能

## NPM 包

该包在 npm 上可用:
[https://www.npmjs.com/package/@yoda.digital/gitlab-mcp-server](https://www.npmjs.com/package/@yoda.digital/gitlab-mcp-server)

**官方网站：** [https://github.com/yoda-digital/mcp-gitlab-server](https://github.com/yoda-digital/mcp-gitlab-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`version control`, `developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @yoda.digital/gitlab-mcp-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/yoda-digital-gitlab.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
