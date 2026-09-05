---
title: "Google日历MCP"
description: "一种集成了Google日历与Claude桌面端的模型上下文协议服务器，允许用户通过自然语言管理日历事件（查看、创建、更新、删除）。"
---

# Google日历MCP

一种集成了Google日历与Claude桌面端的模型上下文协议服务器，允许用户通过自然语言管理日历事件（查看、创建、更新、删除）。

# Google Calendar MCP 服务器

> **🔔 版本更新通知 🔔**  
> 版本 1.0.1 包含了对 Node.js v20.9.0+ 与 'open' 包的兼容性修复，该包在版本 10+ 中已完全转为 ESM。版本 1.0.0 标志着我们首次生产就绪的发布，包含了全面的代码重构和国际化支持。

![Version](/mcp-assets/4ff787f9c6d99002a67c5b61c7a4d89c.svg)
![License](/mcp-assets/5816f652aa1f0cc4eedb21a2f733e09e.svg)
![Security](/mcp-assets/bd906b87ff78e7328bf1a546d50817db.svg)
![Tests](/mcp-assets/3cf9e89b5fce77ff6e478ce0e7400072.svg)

  

## 项目概述

Google Calendar MCP 服务器是一个实现了 MCP（模型上下文协议）的服务器，它使得 Google 日历能够与 Claude 桌面版集成。该项目让 Claude 能够与用户的 Google 日历交互，通过自然语言处理来显示、创建、更新和删除日历事件。

### 核心功能

- **Google 日历集成**: 在 Claude 桌面版和 Google 日历 API 之间提供了一个桥梁
- **MCP 实现**: 遵循 AI 助手工具集成的 Model Context Protocol 规范
- **OAuth2 认证**: 安全地处理 Google API 的认证流程
- **事件管理**: 支持全面的日历事件操作（获取、创建、更新、删除）
- **颜色支持**: 使用 colorId 参数设置和更新事件颜色的能力
- **标准输入输出传输**: 使用标准输入/输出与 Claude 桌面版进行通信

## 技术架构

该项目使用了：

- **TypeScript**: 用于类型安全的代码开发
- **MCP SDK**: 使用 `@modelcontextprotocol/sdk` 与 Claude 桌面版集成
- **Google API**: 使用 `googleapis` 访问 Google 日历 API
- **Zod**: 对请求/响应数据实现模式验证
- **基于环境的配置**: 使用 dotenv 进行配置管理
- **Helmet.js**: 用于安全头
- **AES-256-GCM**: 用于令牌加密
- **Jest**: 用于单元测试和覆盖率
- **GitHub Actions**: 用于 CI/CD

## 主要组件

1. **MCP 服务器**: 核心服务器实现，负责与 Claude 桌面版的通信
2. **Google 日历工具**: 日历操作（检索、创建、更新、删除）
3. **认证处理器**: 管理与 Google API 的 OAuth2 流程
4. **模式验证**: 确保所有操作中的数据完整性
5. **令牌管理器**: 安全处理认证令牌

## 可用工具

此 MCP 服务器提供了以下工具以与 Google 日历交互：

### 1. getEvents

使用多种过滤选项检索日历事件。

**参数:**

- `calendarId` (optional): 日历ID（如果省略，则使用主日历）
- `timeMin` (optional): 事件检索的开始时间（ISO 8601格式，例如："2025-03-01T00:00:00Z"）
- `timeMax` (optional): 事件检索的结束时间（ISO 8601格式）
- `maxResults` (optional): 要检索的最大事件数量（默认：10）
- `orderBy` (optional): 排序顺序（"startTime" 或 "updated"）

### 2. createEvent

创建一个新的日历事件。

**参数：**
- `calendarId` (optional): 日历ID（如果省略，则使用主日历）
- `event`: 包含以下内容的事件详情对象：
  - `summary` (required): 事件标题
  - `description` (optional): 事件描述
  - `location` (optional): 事件地点
  - `start`: 开始时间对象，包含：
    - `dateTime` (optional): ISO 8601格式（例如："2025-03-15T09:00:00+09:00"）
    - `date` (optional): 全天事件的YYYY-MM-DD格式
    - `timeZone` (optional): 时区（例如："Asia/Tokyo"）
  - `end`: 结束时间对象（与开始时间相同格式）
  - `attendees` (optional): 参与者数组，包含电子邮件和可选的displayName
  - `colorId` (optional): 事件颜色ID（1-11）

### 3. updateEvent

更新现有的日历事件。

**参数：**
- `calendarId` (optional): 日历ID（如果省略，则使用主日历）
- `eventId` (required): 要更新的事件ID
- `event`: 包含要更新字段的事件详情对象（与createEvent相同的结构，所有字段都是可选的）

### 4. deleteEvent

删除一个日历事件。

**参数：**
- `calendarId` (optional): 日历ID（如果省略，则使用主日历）
- `eventId` (required): 要删除的事件ID

## 开发指南

在添加新功能、修改代码或修复错误时，请使用`npm version`命令语义化地增加版本号。
同时，请确保您的代码清晰并遵循所有必要的编码规则，如面向对象编程。
版本脚本将在版本更新时自动运行`npm install`，但在提交代码之前，您仍应构建、运行lint和测试代码。

### 代码结构

- **src/**: 源代码目录
  - **auth/**: 认证处理
  - **config/**: 配置设置
  - **mcp/**: MCP服务器实现
  - **tools/**: Google日历工具实现
  - **utils/**: 工具函数和辅助函数

### 最佳实践

- 根据TypeScript的最佳实践进行适当的类型标注
- 保持全面的错误处理
- 确保正确的认证流程
- 保持依赖项最新
- 为所有函数编写清晰的文档
- 实施安全最佳实践
- 遵循OAuth 2.1认证标准
- 对所有输入/输出数据使用模式验证

### 测试

- 为核心功能实现单元测试
- 彻底测试认证流程
- 验证针对Google API的日历操作
- 运行带有覆盖率报告的测试
- 确保包括安全测试

## 部署

此包在 npm 上发布为 `@takumi0706/google-calendar-mcp`：

```bash
npx @takumi0706/google-calendar-mcp@1.0.1
```

### 前提条件

1. 创建一个 Google Cloud 项目并启用 Google Calendar API
2. 在 Google Cloud 控制台中配置 OAuth2 凭证
3. 设置环境变量：

```bash
# Create a .env file with your Google OAuth credentials
GOOGLE_CLIENT_ID=your_client_id
GOOGLE_CLIENT_SECRET=your_client_secret
GOOGLE_REDIRECT_URI=http://localhost:4153/oauth2callback
# Optional: Token encryption key (auto-generated if not provided)
TOKEN_ENCRYPTION_KEY=32-byte-hex-key
# Optional: Auth server port and host (default port: 4153, host: localhost)
AUTH_PORT=4153
AUTH_HOST=localhost
# Optional: MCP server port and host (default port: 3000, host: localhost)
PORT=3000
HOST=localhost
```

### Claude Desktop 配置

将服务器添加到您的 `claude_desktop_config.json` 中：

```json
{
  "mcpServers": {
    "google-calendar": {
      "command": "npx",
      "args": [
        "-y",
        "@takumi0706/google-calendar-mcp"
      ],
      "env": {
        "GOOGLE_CLIENT_ID": "your_client_id",
        "GOOGLE_CLIENT_SECRET": "your_client_secret",
        "GOOGLE_REDIRECT_URI": "http://localhost:4153/oauth2callback"
      }
    }
  }
}
```

## 安全考虑

- **OAuth 令牌**仅存储在内存中（不会存储在基于文件的存储中）
- **敏感凭证**必须作为环境变量提供
- **令牌加密**使用 AES-256-GCM 进行安全存储
- **PKCE 实现**，带有明确的 code_verifier 和 code_challenge 生成
- **状态参数验证**用于 CSRF 保护
- 使用 Helmet.js 应用**安全头**
- **速率限制**以保护 API 端点
- 使用 Zod 模式进行**输入验证**

更多详情，请参阅 [SECURITY.md](https://github.com/takumi0706/google-calendar-mcp/blob/HEAD/SECURITY.md)。

## 维护

- 定期更新以保持与 Google Calendar API 的兼容性
- 版本更新记录在 README.md 中
- 日志存储在用户主目录 `~/.google-calendar-mcp/logs/` 中

## 故障排除

如果您遇到任何问题：

1. 检查主目录中的日志 `~/.google-calendar-mcp/logs/`
2. 确保您的 Google OAuth 凭证配置正确
3. 确保您有足够的权限访问 Google Calendar API
4. 确认您的 Claude Desktop 配置正确

### 常见错误

- **JSON 解析错误**：如果您看到诸如 `Unexpected non-whitespace character after JSON at position 4 (line 1 column 5)` 之类的错误，通常是因为 JSON-RPC 消息格式不正确。此问题已在版本 0.6.7 及更高版本中修复。如果您仍然遇到这些错误，请更新到最新版本。
- **认证错误**：验证您的 Google OAuth 凭证
- **连接错误**：确保只有一个服务器实例在运行
- **断开连接问题**：确保您的服务器正确处理 MCP 消息，而无需自定义 TCP 套接字

## 版本历史

### 版本 1.0.1 更改
- 修复了与 Node.js v20.9.0+ 和 'open' 包（v10+）的兼容性问题
- 将静态导入替换为动态导入，以适应 ESM-only 的 'open' 包
- 改进了 OAuth 认证期间浏览器打开时的错误处理
- 增强了代码注释，以便更好地维护

### 版本 1.0.0 更改
- 主要版本发布，标志着生产就绪
- 全面重构代码，提高可维护性
- 所有消息和注释国际化（从日语翻译成英语）
- 提高代码一致性和可读性
- 改进错误消息，提升用户体验
- 更新文档以反映项目的当前状态
- 标准化整个代码库的编码风格

### 版本 0.8.0 更改

- 增强了 OAuth 认证流程以处理刷新令牌问题
- 添加了 `prompt: 'consent'` 参数，强制 Google 显示同意屏幕并提供新的刷新令牌
- 修改了认证流程，在没有刷新令牌的情况下仅使用访问令牌工作
- 改进了令牌刷新逻辑，以处理没有刷新令牌或刷新令牌无效的情况
- 更新了令牌存储，保存刷新后的访问令牌，以更好地管理令牌
- 修复了令牌刷新逻辑中潜在的无限循环问题

### Version 0.7.0 Changes
- 修复了导致 "Cannot GET /oauth2callback" 错误的 OAuth 回调处理问题
- 添加了从 MCP 服务器自动重定向到 OAuth 服务器进行回调处理的功能
- 改进了与不同 OAuth 重定向 URI 配置的兼容性
- 增强了 OAuth 认证流程中的错误处理
- 更新了文档以反映 OAuth 回调处理的修复

### Version 0.6.9 Changes
- 修复了导致重复认证请求的 OAuth 认证提示问题
- 改进了认证流程，防止多个浏览器窗口打开
- 增强了令牌刷新机制，正确处理过期令牌
- 更新了文档以反映 OAuth 认证的修复

### Version 0.6.8 Changes
- 修复了多个实例运行时的端口冲突问题
- 改进了版本管理系统
- 增强了服务器启动和关闭程序
- 将依赖项更新到最新的兼容版本

### Version 0.6.7 Changes
- 修复了使用 MCP Inspector 时导致错误的关键 JSON 解析 bug
- 改进了日志记录，防止干扰 JSON-RPC 消息
- 在 STDIO 传输中增强了消息处理
- 改进了对格式错误的 JSON 消息的错误处理
- 添加了在使用 npm version 命令更新版本时的自动化 npm 安装过程
- 更新了文档以反映 JSON 解析 bug 的修复和自动化 npm 安装过程

### Version 0.6.6 Changes
- 在 utils/json-parser.ts 中添加了专用的 JSON-RPC 消息解析工具
- 创建了全面的 JSON 解析测试套件以防止回归
- 实现了 10 个测试用例，覆盖各种格式错误的 JSON 场景
- 重构了 server.ts 以使用通用的 JSON 解析工具
- 提高了代码的可维护性和可测试性

### Version 0.6.5 Changes
- 完全重新设计了 JSON-RPC 消息处理，以解决解析错误
- 简化并改进了从消息中提取有效 JSON 的算法
- 修复了 "Unexpected non-whitespace character after JSON at position 4" 错误
- 通过更详细的错误消息增强了错误处理
- 改进了日志记录，以提高诊断和故障排除能力

### Version 0.6.4 Changes

- 进一步改进了 JSON-RPC 消息处理，以更稳健地处理格式错误的消息
- 增强了用于提取 JSON 对象和数组的正则表达式模式，使用非贪婪匹配
- 添加了平衡括号匹配算法，以找到 JSON 对象和数组的正确结束位置
- 修复了正则表达式模式中的 ESLint 警告
- 改进了错误日志记录，以便更好地进行诊断
- 更新了 package.json 和 server.ts 中的版本号

### Version 0.6.3 Changes
- 修复了 JSON-RPC 消息处理，以更稳健地处理格式错误的消息
- 改进了用于提取 JSON 对象的正则表达式模式
- 添加了 JSON 解析的回退机制
- 更新了 server.ts 中的版本号以匹配 package.json

### Version 0.6.2 Changes
- 实现了 HTML 消毒，以防止跨站脚本 (XSS) 漏洞
- 添加了 escapeHtml 工具函数，以安全处理 HTML 响应中的用户控制数据
- 修复了 OAuth 错误处理中的潜在 XSS 漏洞
- 为 HTML 消毒功能添加了全面的测试套件
- 提高了针对注入攻击的整体安全性

### Version 0.6.1 Changes
- 修复了日志记录器配置，确保信息日志输出到 stdout 而不是 stderr
- 更新依赖项以解决过时包警告
- 移除了不必要的 @types/helmet 依赖
- 固定了 eslint 版本，使其与 @typescript-eslint 包兼容
- 提高了整体稳定性和兼容性

### Version 0.6.0 Changes
- 升级版本以保持与最新依赖项的兼容性
- 在传输层实现了 OAuth 2.1 认证
- 添加了对多个请求的 JSON-RPC 批处理支持
- 增强了 PKCE 实现，显式生成 code_verifier 和 code_challenge
- 通过显式状态参数验证增强了 CSRF 保护
- 修复了 TokenManager 清理计时器，以在测试完成后正确释放资源
- 改进了间隔计时器的处理，以防止潜在的内存泄漏
- 增强了资源管理，提高了应用程序稳定性
- 提高了整体稳定性和性能
- 提高了代码质量和可维护性

### Version 0.5.1 Changes
- 小错误修复和稳定性改进
- 文档更新

### Version 0.5.0 Changes
- 为日历事件添加了颜色支持，使用 colorId 参数
- 增强了事件创建和更新功能
- 将 @modelcontextprotocol/sdk 从 1.7.0 升级到 1.8.0
- 将 googleapis 从 133.0.0 升级到 148.0.0
- 将 winston 从 3.11.0 升级到 3.17.0
- 将 zod 从 3.22.4 升级到 3.24.2
- 提高了与最新依赖项的稳定性和兼容性

### Version 0.4.2 Changes
- 改进了工具注册，以正确向客户端公开工具详情
- 通过明确的工具定义增强了服务器能力注册
- 修复了服务器初始化中的操作顺序
- 改进了代码文档和注释

### Version 0.4.1 Changes

- 重构代码架构以提高可维护性
- 实现了 `ToolsManager` 类来封装工具定义
- 通过将功能从 `server.ts` 移动到 `tools.ts` 来改进代码组织
- 删除了未使用的导入和类型定义
- 提高了代码质量和可读性

### Version 0.4.0 更改
- 实现了令牌加密系统（AES-256-GCM）
- 增强了基本的 OAuth 认证流程
- 使用 Helmet.js 添加了安全头
- 为 DDoS 防护实现了速率限制
- 增强了输入验证和错误处理
- 改进了测试覆盖率
- 通过 GitHub Actions 自动化 CI/CD
- 增强了安全文档

### Version 0.3.3 更改
- 移除了基于文件的令牌存储，并改进了内存中的令牌管理
- 修复了各种内存泄漏问题并改进了资源管理
- 增强了稳定性和错误处理

### Version 0.3.2 更改
- 增加了自动打开浏览器进行 Google 日历授权的功能
- 在认证流程中改善了用户体验

### Version 0.3.1 更改
- 更新了服务器版本指示器
- 修复了事件处理中的小错误

### Version 0.2.7 修复
- 修复了 JSON-RPC 消息处理，使其能够处理格式错误的消息
- 通过更强大的解析改进了客户端与服务器之间的消息处理
- 通过更好的上下文信息增强了日志格式
- 添加了调试模式支持，以便对 JSON-RPC 消息进行故障排除

### Version 0.2.6 修复
- 修复了导致解析错误的 JSON-RPC 消息处理
- 移除了导致连接问题的自定义 TCP 套接字服务器
- 为传输错误添加了适当的错误处理
- 改进了客户端与服务器之间消息交换的日志记录

### Version 0.2.0 更改
- 更新为使用最新的 MCP SDK API (v1.8.0+)
- 从 `Server` 类迁移到现代的 `McpServer` 类
- 通过适当类型的工具处理器提高了类型安全性
- 修复了更新操作，以正确处理部分事件更新
- 通过详细的错误消息增强了错误处理
- 优化了处理日历操作时的性能
- 通过直接 API 调用简化了实现

## 开发

要为该项目贡献代码：

```bash
# Clone the repository
git clone https://github.com/takumi0706/google-calendar-mcp.git
cd google-calendar-mcp

# Install dependencies
npm install

# Run in development mode
npm run dev
```

## 测试

要运行测试：

```bash
# Run all tests
npm test

# Run tests with coverage report
npm test -- --coverage
```

## 许可证

MIT

**官方网站：** [https://github.com/takumi0706/google-calendar-mcp](https://github.com/takumi0706/google-calendar-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`productivity`
- 标签：`calendar management`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @takumi0706/google-calendar-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/takumi0706-google-calendar.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
