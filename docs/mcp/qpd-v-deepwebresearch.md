---
title: "Claude深度网络调研器"
description: "一种模型上下文协议服务器，使克劳德能够进行高级网络研究，具有智能搜索排队、增强的内容提取和深入的研究能力。"
---

# Claude深度网络调研器

一种模型上下文协议服务器，使克劳德能够进行高级网络研究，具有智能搜索排队、增强的内容提取和深入的研究能力。

# MCP 深网研究服务器 (v0.3.0)

[![Node.js 版本](/mcp-assets/6176b88dbd8c31864dcd7185f406cea8.svg)](https://nodejs.org/)
[![TypeScript](/mcp-assets/03500effbf23a69c818017a47f3da738.svg)](https://www.typescriptlang.org/)
[![许可证: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)

一个用于高级网络研究的模型上下文协议 (MCP) 服务器。

## 最新更改

- 添加了用于直接网页内容提取的 `visit_page` 工具
- 优化性能以适应 MCP 超时限制
  * 减少了默认的 `maxDepth` 和 `maxBranching` 参数
  * 提高了页面加载效率
  * 在整个过程中添加了超时检查
  * 增强了针对超时的错误处理

> 该项目是 [mzxrai](https://github.com/mzxrai) 的 [mcp-webresearch](https://github.com/mzxrai/mcp-webresearch) 项目的分支，增加了额外的功能以提高深网研究能力。我们非常感谢原作者的基础工作。

通过智能搜索队列、增强的内容提取和深入的研究功能，将实时信息带入 Claude。

## 功能

- 智能搜索队列系统
  - 批量搜索操作并带有速率限制
  - 队列管理及进度跟踪
  - 错误恢复与自动重试
  - 搜索结果去重

- 增强的内容提取
  - 基于 TF-IDF 的相关性评分
  - 关键词邻近分析
  - 内容部分加权
  - 可读性评分
  - 改进的 HTML 结构解析
  - 结构化数据提取
  - 更好的内容清理与格式化

- 核心功能
  - Google 搜索集成
  - 网页内容提取
  - 研究会话跟踪
  - 改进格式化的 Markdown 转换

## 先决条件

- [Node.js](https://nodejs.org/) >= 18（包含 `npm` 和 `npx`）
- [Claude 桌面应用程序](https://claude.ai/download)

## 安装

### 全局安装（推荐）

```bash
# Install globally using npm
npm install -g mcp-deepwebresearch

# Or using yarn
yarn global add mcp-deepwebresearch

# Or using pnpm
pnpm add -g mcp-deepwebresearch
```

### 本地项目安装

```bash
# Using npm
npm install mcp-deepwebresearch

# Using yarn
yarn add mcp-deepwebresearch

# Using pnpm
pnpm add mcp-deepwebresearch
```

### Claude 桌面应用程序集成

安装包后，在您的 `claude_desktop_config.json` 文件中添加以下条目：

#### Windows
```json
{
  "mcpServers": {
    "deepwebresearch": {
      "command": "mcp-deepwebresearch",
      "args": []
    }
  }
}
```
位置：`%APPDATA%\Claude\claude_desktop_config.json`

#### macOS
```json
{
  "mcpServers": {
    "deepwebresearch": {
      "command": "mcp-deepwebresearch",
      "args": []
    }
  }
}
```
位置：`~/Library/Application Support/Claude/claude_desktop_config.json`

此配置允许 Claude 桌面应用程序在需要时自动启动网络研究 MCP 服务器。

### 首次设置

安装完成后，运行以下命令以安装所需的浏览器依赖项：
```bash
npx playwright install chromium
```

## 使用方法

只需开始与Claude的聊天，并发送一个可以从网络研究中受益的提示。如果您希望使用一个为深入网络研究定制的预构建提示，您可以通过这个包提供的`agentic-research`提示来实现。在Claude Desktop中，通过点击聊天输入框中的回形针图标，然后选择 `Choose an integration` → `deepwebresearch` → `agentic-research` 来访问该提示。

### 工具

1. `deep_research`
   - 执行全面的研究并进行内容分析
   - 参数：
```typescript
     {
       topic: string;
       maxDepth?: number;      // 默认值: 2
       maxBranching?: number;  // 默认值: 3
       timeout?: number;       // 默认值: 55000 (55秒)
       minRelevanceScore?: number;  // 默认值: 0.7
     }
```
   - 返回：
```typescript
     {
       findings: {
         mainTopics: Array;
         keyInsights: Array;
         sources: Array;
       };
       progress: {
         completedSteps: number;
         totalSteps: number;
         processedUrls: number;
       };
       timing: {
         started: string;
         completed?: string;
         duration?: number;
         operations?: {
           parallelSearch?: number;
           deduplication?: number;
           topResultsProcessing?: number;
           remainingResultsProcessing?: number;
           total?: number;
         };
       };
     }
```

2. `parallel_search`
   - 并行执行多个Google搜索，采用智能队列机制
   - 参数：`{ queries: string[], maxParallel?: number }`
   - 注意：为了确保可靠的性能，maxParallel限制为5

3. `visit_page`
   - 访问网页并提取其内容
   - 参数：`{ url: string }`
   - 返回：
```typescript
     {
       url: string;
       title: string;
       content: string;  // Markdown格式的内容
     }
```

### 提示

#### `agentic-research`
这是一个引导式研究提示，帮助Claude进行彻底的网络研究。该提示指导Claude：
- 从广泛的搜索开始，以了解主题概况
- 优先考虑高质量、权威的来源
- 根据发现迭代地精炼研究方向
- 保持您的知情权，并让您能够交互式地指导研究
- 总是引用带有URL的来源

## 配置选项

服务器可以通过环境变量进行配置：

- `MAX_PARALLEL_SEARCHES`: 同时进行的最大搜索数量（默认值: 5）
- `SEARCH_DELAY_MS`: 搜索之间的延迟时间（毫秒）（默认值: 200）
- `MAX_RETRIES`: 失败请求的重试次数（默认值: 3）
- `TIMEOUT_MS`: 请求超时时间（毫秒）（默认值: 55000）
- `LOG_LEVEL`: 日志级别（默认值: 'info'）

## 错误处理

### 常见问题

1. 速率限制
   - 症状："Too many requests" 错误
   - 解决方案：增加 `SEARCH_DELAY_MS` 或减少 `MAX_PARALLEL_SEARCHES`

2. 网络超时
   - 症状："Request timed out" 错误
   - 解决方案：确保请求在 60 秒的 MCP 超时内完成

3. 浏览器问题
   - 症状："Browser failed to launch" 错误
   - 解决方案：确保 Playwright 正确安装 (`npx playwright install`)

### 调试

这是测试版软件。如果您遇到问题：

1. 检查 Claude Desktop 的 MCP 日志：
```bash
   # 在 macOS 上
   tail -n 20 -f ~/Library/Logs/Claude/mcp*.log
   
   # 在 Windows 上
   Get-Content -Path "$env:APPDATA\Claude\logs\mcp*.log" -Tail 20 -Wait
```

2. 启用调试日志记录：
```bash
   export LOG_LEVEL=debug
```

## 开发

### 设置

```bash
# Install dependencies
pnpm install

# Build the project
pnpm build

# Watch for changes
pnpm watch

# Run in development mode
pnpm dev
```

### 测试

```bash
# Run all tests
pnpm test

# Run tests in watch mode
pnpm test:watch

# Run tests with coverage
pnpm test:coverage
```

### 代码质量

```bash
# Run linter
pnpm lint

# Fix linting issues
pnpm lint:fix

# Type check
pnpm type-check
```

## 贡献

1. 分叉仓库
2. 创建您的功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交您的更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 打开一个 Pull Request

### 编码标准

- 遵循 TypeScript 最佳实践
- 维护测试覆盖率高于 80%
- 记录新功能和 API
- 对重大更改更新 CHANGELOG.md
- 遵循语义化版本控制

### 性能考虑

- 尽可能使用批量操作
- 实现适当的错误处理和重试机制
- 考虑大型数据集的内存使用
- 适当缓存结果
- 使用流式处理大内容

## 要求

- Node.js >= 18
- Playwright（作为依赖项自动安装）

## 已验证平台

- [x] macOS
- [x] Windows
- [ ] Linux

## 许可证

MIT

## 致谢

本项目基于 [mzxrai](https://github.com/mzxrai) 的 [mcp-webresearch](https://github.com/mzxrai/mcp-webresearch) 的优秀工作。原始代码库为我们的增强功能和能力提供了基础。

## 作者

[qpd-v](https://github.com/qpd-v)

**官方网站：** [https://github.com/qpd-v/mcp-deepwebresearch](https://github.com/qpd-v/mcp-deepwebresearch)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`browser`
- 标签：`browser automation`, `search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`mcp-deepwebresearch`
- 参数：无

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/qpd-v-deepwebresearch.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
