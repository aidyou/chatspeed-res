---
title: "活动搜索助手"
description: "该服务器为AI助手提供了与Eventbrite API交互的工具，允许用户搜索活动、获取活动详情、检索场地信息以及列出活动类别。"
---

# 活动搜索助手

该服务器为AI助手提供了与Eventbrite API交互的工具，允许用户搜索活动、获取活动详情、检索场地信息以及列出活动类别。

# Eventbrite MCP 服务器

这是一个提供与 Eventbrite API 交互工具的 Model Context Protocol (MCP) 服务器。它允许 AI 助手根据各种条件搜索活动、获取活动详细信息、检索场地信息等。

   alt="Eventbrite 服务器 MCP 服务器" />

## 特性

- 根据各种条件（位置、日期、类别等）搜索活动
- 获取特定活动的详细信息
- 检索场地信息
- 获取活动类别的列表

## 安装

### 从 NPM 安装

```bash
npm install -g @ibraheem4/eventbrite-mcp
```

### 从源代码安装

1. 克隆此仓库
2. 安装依赖项：
```bash
   npm install
```
3. 构建项目：
```bash
   npm run build
```

## 开发

### 以开发模式运行

```bash
npm run dev
```

这将监视源文件的变化，重新构建项目，并自动重启服务器。

### 运行 MCP 服务器

你可以使用提供的运行脚本来运行 MCP 服务器：

```bash
./run.sh
```

这将使用 supergateway 启动 MCP 服务器。

### 使用 Inspector 运行

要使用 Inspector 运行 MCP 服务器，可以使用以下命令：

```bash
npm run inspector
```

这将启动 Inspector，它为测试 MCP 服务器提供了一个 Web 界面。Inspector 将在 [http://localhost:5173](http://localhost:5173) 上可用。

### 手动运行

你可以手动运行 MCP 服务器：

```bash
npx -y supergateway --port 1337 --stdio "./build/index.js"
```

或者简单地使用提供的运行脚本：

```bash
./run.sh
```

### 测试

```bash
# Run all tests
npm test

# Run tests in watch mode
npm run test:watch

# Run tests with coverage
npm run test:coverage

# Run integration tests
npm run test:integration

# Test the API directly
npm run test:api
```

## 配置

要使用此 MCP 服务器，你需要：

1. 从 [Eventbrite 开发者门户](https://www.eventbrite.com/platform/api) 获取 Eventbrite API 密钥
2. 通过以下方式之一设置你的 API 密钥：
   - 在项目根目录中创建一个 `.env` 文件（从 `.env.example` 复制）：
```
     EVENTBRITE_API_KEY=your_eventbrite_api_key_here
```
   - 或者作为环境变量提供：
```bash
     export EVENTBRITE_API_KEY=your_eventbrite_api_key_here
```
   - 或者在 MCP 设置文件中配置（见下文）
3. 测试你的 API 密钥：
```bash
   ./test-api-key.js
```
4. 在你的 MCP 设置文件中配置 MCP 服务器

### 对于 Claude 桌面应用程序

在 `~/Library/Application Support/Claude/claude_desktop_config.json` 文件（macOS 上）中添加以下内容：

```json
{
  "mcpServers": {
    "eventbrite": {
      "command": "npx",
      "args": ["-y", "@ibraheem4/eventbrite-mcp"],
      "env": {
        "EVENTBRITE_API_KEY": "your-eventbrite-api-key"
      },
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

### 对于 Claude 开发环境

在 `~/Library/Application Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json` 文件（macOS 上）中添加以下内容：

```json
{
  "mcpServers": {
    "eventbrite": {
      "command": "npx",
      "args": ["-y", "@ibraheem4/eventbrite-mcp"],
      "env": {
        "EVENTBRITE_API_KEY": "your-eventbrite-api-key"
      },
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

### 快速开始

如果你是从源代码安装的，可以使用提供的运行脚本：

```bash
./run.sh
```

这将构建项目并启动 MCP 服务器。

## 可用工具

### search_events

根据各种条件搜索 Eventbrite 活动。

参数：

- `query` (字符串，可选)：事件搜索查询
- `location` (对象，可选)：搜索周围的地点
  - `latitude` (数字，必填)：纬度坐标
  - `longitude` (数字，必填)：经度坐标
  - `within` (字符串，可选)：距离（例如，'10km'，'10mi'）
- `categories` (字符串数组，可选)：按类别ID过滤
- `start_date` (字符串，可选)：开始日期，ISO格式（例如，'2023-01-01T00:00:00Z'）
- `end_date` (字符串，可选)：结束日期，ISO格式（例如，'2023-12-31T23:59:59Z'）
- `price` (字符串，可选)：按'free'或'paid'事件过滤
- `page` (数字，可选)：分页的页码
- `page_size` (数字，可选)：每页的结果数（最大100）

### get_event

获取特定Eventbrite事件的详细信息。

参数：
- `event_id` (字符串，必填)：Eventbrite事件ID

### get_categories

获取Eventbrite事件类别的列表。

无需参数。

### get_venue

获取特定Eventbrite场地的信息。

参数：
- `venue_id` (字符串，必填)：Eventbrite场地ID

## 可用资源

### 事件详情资源

URI模板: `eventbrite://events/{eventId}`

获取特定Eventbrite事件的详细信息。

## 示例用法

配置完成后，您可以要求Claude使用Eventbrite MCP工具：

- "搜索下周末在纽约的音乐活动"
- "获取ID为123456789的Eventbrite事件的详细信息"
- "Eventbrite上有哪些类别的活动？"
- "告诉我ID为987654321的场地信息"

## 许可证

MIT

**官方网站：** [https://github.com/ibraheem4/eventbrite-mcp](https://github.com/ibraheem4/eventbrite-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`entertainment and media`, `social media`, `search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @ibraheem4/eventbrite-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/ibraheem4-eventbrite.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
