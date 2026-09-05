---
title: "提示工坊"
description: "通过简化的SOLID架构，启用提示词的创建、管理和模板化，允许用户按类别组织提示词并在运行时填充模板。"
---

# 提示工坊

通过简化的SOLID架构，启用提示词的创建、管理和模板化，允许用户按类别组织提示词并在运行时填充模板。

# MCP 提示服务器

一个用于管理提示和模板并具备项目编排能力的MCP服务器。是Model Context Protocol生态系统的一部分。

  

此服务器提供了一种简单的方式来存储、检索和应用AI提示模板，使您更容易在AI应用程序中保持一致的提示模式。

## 目录
- [特性](#特性)
- [安装](#安装)
- [配置](#配置)
- [使用方法](#使用方法)
  - [与Claude一起使用](#与claude一起使用)
  - [可用工具](#可用工具)
  - [API使用示例](#api使用示例)
  - [管理提示](#管理提示)
  - [在您的工作流中使用提示](#在您的工作流中使用提示)
- [提示格式](#提示格式)
- [多格式提示支持](#多格式提示支持)
  - [格式转换](#格式转换)
  - [应用模板](#应用模板)
  - [提取变量](#提取变量)
  - [从不同格式创建](#从不同格式创建)
  - [与存储适配器集成](#与存储适配器集成)
- [存储适配器](#存储适配器)
  - [PostgreSQL设置](#postgresql设置)
- [Docker部署](#docker部署)
  - [Docker Compose编排](#docker-compose编排)
    - [简易部署](#简易部署)
    - [PostgreSQL部署](#postgresql部署)
    - [开发环境](#开发环境)
    - [测试环境](#测试环境)
    - [Docker管理脚本](#docker管理脚本)
    - [自定义配置](#自定义配置)
- [开发](#开发)
  - [开发工作流程](#开发工作流程)
  - [开发命令](#开发命令)
  - [构建过程](#构建过程)
  - [测试](#测试)
  - [目录结构](#目录结构)
- [发布流程](#发布流程)
- [变更日志](#变更日志)
- [最佳实践](#最佳实践)
- [许可证](#许可证)

## 特性

- 存储和检索提示
- 创建和使用带有变量的模板
- 通过标签过滤列出提示
- 向模板应用变量
- 多个存储后端（文件系统、PostgreSQL 和 MDC 格式）
- 易于与Claude及其他AI助手配合使用
- 项目编排功能
- 健康检查端点

## 安装

### 使用 npx (推荐)

```bash
npx -y @sparesparrow/mcp-prompts
```

### 全局安装

```bash
npm install -g @sparesparrow/mcp-prompts
```

### 使用 Docker

```bash
docker run -p 3003:3003 -v ~/mcp/data:/app/data sparesparrow/mcp-prompts:latest
```

### 验证安装

安装后，您可以按照以下步骤验证服务器是否正常工作：

1. 打开Claude桌面版
2. 在聊天输入框中键入"/"以查看来自服务器的提示是否出现
3. 测试一个简单的工具调用：
```
   use_mcp_tool({
     server_name: "prompt-manager",
     tool_name: "list_prompts",
     arguments: {}
   });
```

## 配置

服务器可以通过环境变量进行配置：

| 环境变量 | 描述 | 默认值 |
|----------------------|-------------|---------|
| SERVER_NAME | 服务器名称 | MCP Prompts Server |
| SERVER_VERSION | 服务器版本 | package.json 版本 |
| STORAGE_TYPE | 存储类型：'file', 'postgres' 或 'mdc' | file |
| PROMPTS_DIR | 存储提示的目录 | ~/mcp/data/prompts |
| BACKUPS_DIR | 备份目录 | ~/mcp/data/backups |
| PORT | HTTP 服务器端口 | 3003 |
| LOG_LEVEL | 日志级别 | info |
| HTTP_SERVER | 启用 HTTP 服务器 | false |
| HOST | HTTP 服务器主机 | 0.0.0.0 |

### PostgreSQL 设置（如果 STORAGE_TYPE=postgres，则需要）

| 环境变量 | 描述 | 默认值 |
|----------------------|-------------|---------|
| PG_HOST | PostgreSQL 主机 | localhost |
| PG_PORT | PostgreSQL 端口 | 5432 |
| PG_DATABASE | PostgreSQL 数据库名 | mcp_prompts |
| PG_USER | PostgreSQL 用户名 | postgres |
| PG_PASSWORD | PostgreSQL 密码 | |
| PG_SSL | 使用 SSL 连接 PostgreSQL | false |
| POSTGRES_CONNECTION_STRING | 完整的 PostgreSQL 连接字符串（覆盖单独设置） | |

### MDC 设置（如果 STORAGE_TYPE=mdc，则需要）

| 环境变量 | 描述 | 默认值 |
|----------------------|-------------|---------|
| MDC_RULES_DIR | MDC 规则目录 | ./.cursor/rules |

## 使用方法

### 与 Claude 一起使用

在 Claude 3 桌面应用程序中，您可以在 `claude_desktop_config.json` 中配置 MCP 提示服务器：

```json
{
  "mcpServers": {
    "prompts": {
      "command": "npx",
      "args": [
        "-y",
        "@sparesparrow/mcp-prompts"
      ],
      "env": {
        "STORAGE_TYPE": "file",
        "PROMPTS_DIR": "/path/to/your/prompts/directory",
        "LOG_LEVEL": "debug"
      }
    }
  }
}
```

### 可用工具

MCP 提示服务器提供以下工具：

- `add_prompt`: 添加新提示
- `get_prompt`: 通过 ID 获取提示
- `update_prompt`: 更新现有提示
- `list_prompts`: 列出所有提示
- `delete_prompt`: 通过 ID 删除提示
- `apply_template`: 应用变量到提示模板

### API 使用示例

#### 列出可用提示

要查看可用的提示：

```
use_mcp_tool({
  server_name: "prompt-manager",
  tool_name: "list_prompts",
  arguments: {}
});
```

按标签过滤：

```
use_mcp_tool({
  server_name: "prompt-manager",
  tool_name: "list_prompts",
  arguments: {
    tags: ["development"]
  }
});
```

#### 获取特定提示

通过 ID 检索特定提示：

```
use_mcp_tool({
  server_name: "prompt-manager",
  tool_name: "get_prompt",
  arguments: {
    id: "development-workflow"
  }
});
```

#### 使用模板提示

应用变量到模板提示：

```
use_mcp_tool({
  server_name: "prompt-manager",
  tool_name: "apply_template",
  arguments: {
    id: "development-system-prompt",
    variables: {
      "project_type": "web frontend",
      "language": "JavaScript/React",
      "project_name": "TaskManager",
      "project_goal": "create a task management application with drag-and-drop functionality",
      "technical_context": "Using React 18, TypeScript, and Material UI"
    }
  }
});
```

### 管理提示

#### 添加新提示

添加新提示：

```
use_mcp_tool({
  server_name: "prompt-manager",
  tool_name: "add_prompt",
  arguments: {
    name: "Bug Report Template",
    description: "Template for submitting bug reports",
    content: "## Bug Report\n\n### Description\n{{description}}\n\n### Steps to Reproduce\n{{steps}}\n\n### Expected Behavior\n{{expected}}\n\n### Actual Behavior\n{{actual}}\n\n### Environment\n{{environment}}",
    isTemplate: true,
    variables: ["description", "steps", "expected", "actual", "environment"],
    tags: ["bug", "template", "documentation"]
  }
});
```

#### 编辑现有提示

编辑现有提示：

```
use_mcp_tool({
  server_name: "prompt-manager",
  tool_name: "edit_prompt",
  arguments: {
    id: "development-workflow",
    content: "Updated workflow content here...",
    tags: ["development", "workflow", "python", "updated"]
  }
});
```

### 在您的工作流中使用提示

#### 开发工作流示例

当开始开发一个新功能时：

1. 请求开发系统提示模板
2. 用项目详细信息填充模板
3. 使用生成的系统提示来指导 Claude 的帮助

#### 代码审查示例

当审查代码时：

1. 请求代码审查模板
2. 提供待审查的代码
3. Claude 将提供结构化的审查

## 提示格式

提示具有以下结构：

```json
{
  "id": "unique-id",
  "name": "Prompt Name",
  "description": "Optional description",
  "content": "The prompt content with {{variables}}",
  "tags": ["tag1", "tag2"],
  "isTemplate": true,
  "variables": ["variable1", "variable2"],
  "metadata": {
    "author": "Your Name",
    "version": "1.0.0"
  }
}
```

## 多格式提示支持

MCP 提示服务器包括一个强大的 `MutablePrompt` 接口，允许提示在多种格式之间转换：

- **JSON 格式**: 服务器使用的标准内部格式
- **MDC 格式**: 游标规则 Markdown 格式（.mdc 文件）
- **PGAI 格式**: 支持嵌入的 PostgreSQL AI 格式
- **模板格式**: 带有变量占位符的动态格式

### 格式之间的转换

MutablePrompt 接口提供了在这些格式之间转换提示的方法：

```typescript
// Create a mutable prompt
const factory = new MutablePromptFactoryImpl();
const prompt = factory.create({
  name: "API Design Guide",
  description: "Template for designing RESTful APIs",
  content: "# API Design for {{service_name}}\n\n## Endpoints\n\n{{endpoints}}\n\n## Authentication\n\n{{auth_method}}",
  isTemplate: true,
  variables: ["service_name", "endpoints", "auth_method"],
  tags: ["api", "design", "rest", "glob:*.md"]
});

// Convert to MDC format
const mdcContent = prompt.toMdc({
  includeVariables: true
});

// Convert to PGAI format with embeddings
const pgaiData = prompt.toPgai({
  generateEmbeddings: true,
  collection: "prompts",
  vectorConfig: {
    dimension: 1536,
    metric: "cosine"
  }
});

// Convert to template format with dollar-style variables
const templateContent = prompt.toTemplate({
  delimiterStyle: "dollar"
});
```

### 应用模板

您可以轻松地将变量应用于模板提示：

```typescript
const result = prompt.applyVariables({
  service_name: "User Management API",
  endpoints: "GET /users, POST /users, GET /users/{id}, PUT /users/{id}, DELETE /users/{id}",
  auth_method: "JWT Bearer Token"
});
```

### 提取变量

从模板内容中提取变量：

```typescript
const variables = prompt.extractVariables();
// Returns ["service_name", "endpoints", "auth_method"]
```

### 从不同格式创建

您还可以从各种格式创建提示：

```typescript
// From MDC format
const mdcContent = `---
description: Template for code reviews
globs: ["*.js", "*.ts"]
---

# Code Review Template

## Context
{{context}}

## Patterns
{{patterns}}

## Variables

- \`context\`: Description of the code being reviewed
- \`patterns\`: Common patterns to look for
`;

const promptFromMdc = factory.fromMdc(mdcContent);

// From PGAI format
const pgaiData = {
  id: "api-design",
  name: "API Design Guide",
  content: "# API Design Guide\n\nUse this guide...",
  metadata: {
    description: "Comprehensive API design guide",
    tags: ["api", "rest"],
    isTemplate: false
  }
};

const promptFromPgai = factory.fromPgai(pgaiData);
```

### 与存储适配器集成

MutablePrompt 接口与现有的存储适配器无缝协作：

```typescript
// Save a prompt in MDC format
const mdcPrompt = factory.fromMdc(mdcContent);
await fileAdapter.savePrompt(mdcPrompt);

// Save a prompt to PostgreSQL with PGAI format
const pgaiPrompt = factory.fromPgai(pgaiData);
await postgresAdapter.savePrompt(pgaiPrompt);
```

这种灵活的格式处理支持以下功能：

1. **跨平台兼容性**：在不同的工具和平台上使用提示
2. **向量搜索**：使用 PGAI 格式进行语义搜索
3. **IDE 集成**：直接兼容游标规则
4. **模板系统**：导出模板以供多种编程语言使用

## 存储适配器

服务器支持三种类型的存储适配器：

1. **文件适配器**：将提示作为单独的 JSON 文件存储在目录中。
2. **PostgreSQL 适配器**：将提示存储在 PostgreSQL 数据库中。
3. **MDC 适配器**：将提示存储为游标规则 MDC 格式。

存储类型可以通过 `STORAGE_TYPE` 环境变量进行配置：

```
STORAGE_TYPE=file      # Default
STORAGE_TYPE=postgres  # Requires PostgreSQL configuration
STORAGE_TYPE=mdc       # For Cursor Rules format
```

### PostgreSQL 设置

当使用 PostgreSQL 存储时，配置以下环境变量：

```
PG_HOST=localhost
PG_PORT=5432
PG_DATABASE=mcp_prompts
PG_USER=postgres
PG_PASSWORD=your_password
PG_SSL=false
```

或者，可以使用连接字符串：

```
POSTGRES_CONNECTION_STRING=postgresql://user:password@host:port/database
```

## Docker 部署

### Docker Compose 编排

MCP 提示服务器提供了多种 Docker Compose 配置，适用于不同的部署场景：

#### 简单部署
```bash
docker compose up -d
```
这将使用文件存储在端口 3003 上部署 MCP 提示服务器。

#### PostgreSQL 部署
```bash
docker compose -f docker-compose.postgres.yml up -d
```
这将部署：
- 一个 PostgreSQL 数据库服务器
- 配置为使用 PostgreSQL 的 MCP 提示服务器
- 用于数据库管理的 Adminer，在 http://localhost:8080

#### 开发环境
```bash
docker compose -f docker-compose.dev.yml up -d
```
这设置了一个带有热重载的开发环境。它从您的本地目录挂载源代码，并包含 Adminer。

#### 测试环境
```bash
docker compose -f docker-compose.test.yml up --build
```
这创建了一个专用的测试环境，包括：
- 一个带有测试数据的临时 PostgreSQL 实例
- 一个隔离的测试运行容器，执行所有测试
- 测试结果保存在 ./test-results 目录中

#### Docker 管理脚本

为了简化 Docker Compose 操作，请使用提供的管理脚本：

```bash
# Start development environment
./scripts/docker-manage.sh start dev

# Run tests in Docker
./scripts/docker-manage.sh test

# View logs from production environment
./scripts/docker-manage.sh logs prod

# Clean up test environment
./scripts/docker-manage.sh clean test

# Show help
./scripts/docker-manage.sh help
```

管理脚本支持以下命令：

- `start`: 启动 Docker 容器
- `stop`: 停止 Docker 容器
- `restart`: 重启 Docker 容器
- `logs`: 显示容器日志
- `clean`: 删除容器、网络和卷
- `build`: 构建 Docker 镜像
- `test`: 在 Docker 容器中运行测试

以及以下环境：
- `dev`: 开发环境（默认）
- `test`: 测试环境
- `prod`: 生产环境

#### 自定义配置
你可以通过扩展基础配置来创建自己的自定义 Docker Compose 配置：

```yaml
# custom-compose.yml
version: '3.8'

include:
  - docker-compose.yml

services:
  mcp-prompts:
    environment:
      - CUSTOM_ENV=value
```

然后通过以下命令运行它：
```bash
docker compose -f custom-compose.yml up -d
```

## 开发

### 开发工作流

#### 设置开发环境

1. **克隆仓库**
```bash
   git clone https://github.com/user/mcp-prompt-manager.git
   cd mcp-prompt-manager
```

2. **安装依赖**
```bash
   npm install
```

3. **设置环境变量**
   创建一个包含必要配置的 `.env` 文件。

### 开发命令

- **启动带有热重载的开发服务器**
```bash
  npm run dev
```

- **构建项目**
```bash
  npm run build
```

- **运行单元测试**
```bash
  npm test
```

- **运行集成测试**
```bash
  npm run test:integration
```

- **测试构建过程**
```bash
  npm run test:build
```

- **测试 Docker 构建**
```bash
  npm run test:docker
```

- **构建 Docker 镜像**
```bash
  npm run docker:build
```

### 构建过程

构建过程包括以下几个重要步骤：

1. **TypeScript 编译**
```bash
   npm run build
```

2. **使入口点可执行**
```bash
   chmod +x dist/index.js
```

### 测试

运行测试：

```bash
npm test
```

运行 MCP 检查器进行测试：

```bash
npm run test:inspector
```

#### 全面的测试脚本

对于更高级的测试选项，可以使用提供的测试脚本：

```bash
# Run all tests (unit and integration)
./scripts/run-tests.sh

# Run only unit tests
./scripts/run-tests.sh --unit

# Run only integration tests
./scripts/run-tests.sh --integration

# Generate test coverage report
./scripts/run-tests.sh --coverage

# Run tests in Docker
./scripts/run-tests.sh --docker

# Clean up Docker resources after testing
./scripts/run-tests.sh --docker --clean
```

#### Docker 容器健康测试

要测试 Docker 容器的健康状况：

```bash
# Run the Docker health check tests
TEST_DOCKER_HEALTH=true npm test -- tests/integration/docker-health.integration.test.ts
```

此测试验证当 MCP-Prompts 服务器在 Docker 容器中运行时，健康检查端点是否正常工作。

### 目录结构

项目遵循结构化的组织方式，以保持清晰的关注点分离：

```
mcp-prompt-manager/
âââ .github/workflows/    # CI/CD workflow configurations
âââ dist/                 # Built files
âââ src/                  # Source code
â   âââ adapters.ts       # Storage adapters
â   âââ interfaces.ts     # Core types and interfaces
â   âââ index.ts          # Main entry point
âââ scripts/              # Maintenance and utility scripts
âââ package.json          # Project metadata and scripts
âââ README.md             # Project documentation
```

## 发布流程

### 发布前检查清单

- 所有 TypeScript 错误已解决
- 代码 linting 无错误
- 代码根据项目标准正确格式化
- 单元测试通过
- 集成测试通过
- 构建测试通过
- Docker 构建测试通过
- 包安装测试通过
- README 更新为最新功能和变更
- CHANGELOG 更新所有值得注意的变更

### 版本更新

- 根据语义化版本更新 `package.json` 中的版本
- 确保依赖项是最新的
- 更新文档中的任何版本引用

### 发布

- 为新版本创建一个 git 标签
- 将更改和标签推送到 GitHub
- 发布到 npm (`npm publish`)
- 构建并推送 Docker 镜像

### 发布后验证

- 验证从 npm 的安装
- 验证包可以通过 npx 运行
- 验证 Docker 镜像按预期工作
- 验证与 Claude Desktop 的集成

## 更新日志

### [1.2.20] - 2025-03-14
- 自动版本号增加

### [1.2.19] - 2024-03-16
#### 修复
- 修复了 PostgresAdapter 实现中的 TypeScript 错误
- 增强了 savePrompt 方法以正确返回创建的提示
- 在 PostgresAdapter 中添加了 updatePrompt 方法
- 修复了 StorageAdapter 接口，以包含 listPrompts 和 clearAll 方法
- 改进了 database-tools.ts 中 clearAll 方法的错误处理
- 通过更详细的信息增强了健康检查端点

#### 新增
- 为健康检查端点添加了更好的文档和错误处理

### [1.2.18] - 2024-03-14
#### 新增
- 添加了带有健康检查端点的 HTTP 服务器
- 添加了 Docker 容器健康检查
- 添加了对 Node.js 18-23+ 的 ESM 模块兼容性
- 通过更好的错误处理增强了数据库工具

#### 更改
- 通过多阶段构建改进了 Docker 构建过程
- 简化了配置管理
- 优化了 PostgreSQL 适配器连接处理
- 将依赖项更新到最新版本

#### 修复
- 修复了在某些文件系统上文件适配器的问题
- 改进了错误消息以便更好地调试
- 修复了模板变量提取问题

### [1.2.0] - 2025-03-14
#### 更改
- 重新组织代码库结构以提高可维护性
- 将 Docker 相关文件移至 `docker/` 目录
- 将构建脚本移至 `scripts/build/` 目录
- 将测试脚本移至 `scripts/test/` 目录
- 更新 GitHub 工作流以使用新的文件路径
- 更新 Docker Compose 配置以使用新的文件路径
- 添加了全面的开发文档

#### 新增
- 创建了包含详细说明的开发文档
- 创建了用于发布准备的发布检查清单
- 添加了 CHANGELOG.md 以跟踪更改

#### 移除
- 移除了重复和冗余的文件
- 移除了不完整的脚本

### [1.1.0] - 2024-03-01
#### 新增
- PGAI 向量搜索用于语义提示发现
- 对 PostgreSQL 中嵌入的支持
- 通过专业模板改进提示集合
- 批处理能力用于提示集合

#### 更改
- 增强了提示处理管道
- 通过更多选项改进了命令行界面
- 更好的错误处理和验证

### [1.0.0] - 2024-02-15
#### 新增
- MCP 提示服务器的初始发布
- 基本的提示管理功能（添加、编辑、获取、列表、删除）
- 模板变量替换
- 基于标签的组织
- 基于文件的存储
- 导入/导出功能
- MCP 协议兼容性

## 最佳实践

1. **使用标签组织**: 使用标签对您的提示进行分类，以便更轻松地检索
2. **使用模板**: 创建可重用的带有变量的模板以保持一致的提示
3. **包含元数据**: 添加作者、版本等元数据以便更好地组织
4. **定期备份**: 如果管理关键提示，请使用备份功能
5. **优化大型集合**: 在检索大型提示集合时使用分页
6. **使用一致的命名**: 为提示清晰且一致地命名以便于发现
7. **有效使用标签**: 根据目的、项目或上下文使用标签组织提示
8. **将可重用的提示模板化**: 为经常使用的提示创建带有变量的模板
9. **定期更新**: 随着需求的变化保持您的提示是最新的
10. **与团队共享**: 与您的团队共享有效的提示，以确保一致的交互

## 许可证

MIT

**官方网站：** [https://github.com/sparesparrow/mcp-prompts](https://github.com/sparesparrow/mcp-prompts)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`memory`
- 标签：`knowledge and memory`, `developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @sparesparrow/mcp-prompts`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/sparesparrow-prompts.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
