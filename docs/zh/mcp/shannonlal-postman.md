---
title: "MCP-Postman API测试工具"
description: "启用通过Newman运行Postman集合，以进行API测试并通过对标准化接口获取详细的结果分析。"
---

# MCP-Postman API测试工具

启用通过Newman运行Postman集合，以进行API测试并通过对标准化接口获取详细的结果分析。

# Postman MCP 服务器
[Smithery](https://smithery.ai/server/mcp-postman)

这是一个 MCP（Model Context Protocol）服务器，它通过 Newman 运行 Postman 集合。此服务器允许 LLMs 通过标准化接口执行 API 测试并获取详细结果。

[Watch video](https://youtu.be/d1WgTqwMsog)

## 功能

- 使用 Newman 运行 Postman 集合
- 支持环境文件
- 支持全局变量
- 详细的测试结果包括：
  - 总体成功/失败状态
  - 测试摘要（总数、通过数、失败数）
  - 详细的失败信息
  - 执行时间

## 安装

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/mcp-postman) 自动安装 Claude 桌面版的 Postman Runner：

```bash
npx -y @smithery/cli install mcp-postman --client claude
```

### 手动安装
```bash
# Clone the repository
git clone 
cd mcp-postman

# Install dependencies
pnpm install

# Build the project
pnpm build
```

## 使用

### 配置

将服务器添加到你的 Claude 桌面配置文件 `~/Library/Application Support/Claude/claude_desktop_config.json` 中：

```json
{
  "mcpServers": {
    "postman-runner": {
      "command": "node",
      "args": ["/absolute/path/to/mcp-postman/build/index.js"]
    }
  }
}
```

### 可用工具

#### run-collection

运行一个 Postman 集合并返回测试结果。

**参数：**

- `collection` (必需): Postman 集合的路径或 URL
- `environment` (可选): 环境文件的路径或 URL
- `globals` (可选): 全局变量文件的路径或 URL
- `iterationCount` (可选): 要运行的迭代次数

**示例响应：**

```json
{
  "success": true,
  "summary": {
    "total": 5,
    "failed": 0,
    "passed": 5
  },
  "failures": [],
  "timings": {
    "started": "2024-03-14T10:00:00.000Z",
    "completed": "2024-03-14T10:00:01.000Z",
    "duration": 1000
  }
}
```

### 在 Claude 中使用示例

你可以通过让 Claude 运行一个 Postman 集合来使用该服务器：

"运行位于 /path/to/collection.json 的 Postman 集合并告诉我所有测试是否通过"

Claude 将会：

1. 使用 run-collection 工具
2. 分析测试结果
3. 提供易于理解的执行摘要

## 开发

### 项目结构

```
src/
  ├── index.ts           # Entry point
  ├── server/
  │   ├── server.ts     # MCP Server implementation
  │   └── types.ts      # Type definitions
  └── newman/
      └── runner.ts     # Newman runner implementation
test/
  ├── server.test.ts    # Server tests
  ├── newman-runner.test.ts  # Runner tests
  └── fixtures/         # Test fixtures
      └── sample-collection.json
```

### 运行测试

```bash
# Run tests
pnpm test

# Run tests with coverage
pnpm test:coverage
```

### 构建

```bash
# Build the project
pnpm build

# Clean build artifacts
pnpm clean
```

## 贡献

1. 分叉仓库
2. 创建你的功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交你的更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 打开一个 Pull Request

## 许可证

ISC

**官方网站：** [https://github.com/shannonlal/mcp-postman](https://github.com/shannonlal/mcp-postman)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`/absolute/path/to/mcp-postman/build/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/shannonlal-postman.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
