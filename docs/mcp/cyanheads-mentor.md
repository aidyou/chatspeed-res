---
title: "智码师"
description: "通过Deepseek API为大型语言模型代理提供人工智能驱动的代码审查、设计评论、写作反馈和头脑风暴指导，从而在各种开发和战略规划任务中提升输出效果。"
---

# 智码师

通过Deepseek API为大型语言模型代理提供人工智能驱动的代码审查、设计评论、写作反馈和头脑风暴指导，从而在各种开发和战略规划任务中提升输出效果。

# mentor-mcp-server

[![TypeScript](/mcp-assets/49904649f602ceb829cc76dcf6be1703.svg)](https://www.typescriptlang.org/)
[![Model Context Protocol](/mcp-assets/69961a4849edddd35de5143c0035e099.svg)](https://modelcontextprotocol.io/)
[![Version](/mcp-assets/b3bf466f985d1cb8019f262681fdd935.svg)]()
[![License](/mcp-assets/fa73b4786cfc281bb30f39f895ada091.svg)](https://opensource.org/licenses/Apache-2.0)
[![Status](/mcp-assets/9a22554be918edafcc71c8bd0058366d.svg)]()
[![GitHub](/mcp-assets/fe6113458dd9b6cc2f99e34f47b5a356.svg)](https://github.com/cyanheads/mentor-mcp-server)

一个 Model Context Protocol 服务器，通过 AI 驱动的 Deepseek-Reasoning (R1) 导师功能为 LLM 代理提供第二意见，包括代码审查、设计批评、写作反馈和创意头脑风暴等功能。通过 Deepseek API，让您的 LLM 代理获得专家级的第二意见和可操作的见解。

## Model Context Protocol

Model Context Protocol (MCP) 支持以下实体之间的通信：

- **客户端**：Claude Desktop、IDEs 和其他兼容 MCP 的客户端
- **服务器**：用于任务管理和自动化的工具和资源
- **LLM 代理**：利用服务器能力的 AI 模型

## 目录

- [特性](#特性)
- [安装](#安装)
- [配置](#配置)
- [工具](#工具)
- [示例](#示例)
- [开发](#开发)
- [项目结构](#项目结构)
- [许可证](#许可证)

## 特性

### 代码分析
- 全面的代码审查
- 错误检测与预防
- 代码风格和最佳实践评估
- 性能优化建议
- 安全漏洞评估

### 设计与架构
- UI/UX 设计批评
- 架构图分析
- 设计模式推荐
- 可访问性评估
- 一致性检查

### 内容增强
- 写作反馈与改进
- 语法和风格分析
- 文档审查
- 内容清晰度评估
- 结构性建议

### 战略规划
- 功能增强头脑风暴
- 方法上的第二意见
- 创新建议
- 可行性分析
- 用户价值评估

## 安装

```bash
# Clone the repository
git clone git@github.com:cyanheads/mentor-mcp-server.git
cd mentor-mcp-server

# Install dependencies
npm install

# Build the project
npm run build
```

## 配置

在您的 MCP 客户端设置中添加：

```json
{
  "mcpServers": {
    "mentor": {
      "command": "node",
      "args": ["build/index.js"],
      "env": {
        "DEEPSEEK_API_KEY": "your_api_key",
        "DEEPSEEK_MODEL": "deepseek-reasoner",
        "DEEPSEEK_MAX_TOKENS": "8192",
        "DEEPSEEK_MAX_RETRIES": "3",
        "DEEPSEEK_TIMEOUT": "30000"
      }
    }
  }
}
```

### 环境变量

| 变量 | 是否必需 | 默认值 | 描述 |
|----------|----------|---------|-------------|
| DEEPSEEK_API_KEY | 是 | - | 您的 Deepseek API 密钥 |
| DEEPSEEK_MODEL | 是 | deepseek-reasoner | Deepseek 模型名称 |
| DEEPSEEK_MAX_TOKENS | 否 | 8192 | 每次请求的最大令牌数 |
| DEEPSEEK_MAX_RETRIES | 否 | 3 | 重试次数 |
| DEEPSEEK_TIMEOUT | 否 | 30000 | 请求超时时间（毫秒） |

## 工具

### 代码审查
```xml

mentor-mcp-server
code_review

{
  "file_path": "src/app.ts",
  "language": "typescript"
}

```

### 设计批评
```xml

mentor-mcp-server
design_critique

{
  "design_document": "path/to/design.fig",
  "design_type": "web UI"
}

```

### 写作反馈
```xml

mentor-mcp-server
writing_feedback

{
  "text": "Documentation content...",
  "writing_type": "documentation"
}

```

### 功能增强
```xml

mentor-mcp-server
brainstorm_enhancements

{
  "concept": "User authentication system"
}

```

## 示例

每个工具的使用方法和输出详细示例可以在 [examples](https://github.com/cyanheads/mentor-mcp-server/tree/HEAD/examples) 目录中找到：

- [第二意见示例](https://github.com/cyanheads/mentor-mcp-server/blob/HEAD/examples/second-opinion.md) - 认证系统需求分析
- [代码审查示例](https://github.com/cyanheads/mentor-mcp-server/blob/HEAD/examples/code-review.md) - 详细的 TypeScript 代码审查，包含安全性和性能方面的见解
- [设计评论示例](https://github.com/cyanheads/mentor-mcp-server/blob/HEAD/examples/design-critique.md) - 仪表板设计的全面 UI/UX 反馈
- [写作反馈示例](https://github.com/cyanheads/mentor-mcp-server/blob/HEAD/examples/writing-feedback.md) - 文档改进建议
- [头脑风暴增强示例](https://github.com/cyanheads/mentor-mcp-server/blob/HEAD/examples/brainstorm-enhancements.md) - 功能构思及实现细节

每个示例都包括请求格式和示例响应，展示了工具的功能和输出结构。

## 开发

```bash
# Build TypeScript code
npm run build

# Start the server
npm run start

# Development with watch mode
npm run dev

# Clean build artifacts
npm run clean
```

## 项目结构

```
src/
├── api/         # API integration modules
├── tools/       # Tool implementations
│   ├── second-opinion/
│   ├── code-review/
│   ├── design-critique/
│   ├── writing-feedback/
│   └── brainstorm-enhancements/
├── types/       # TypeScript type definitions
├── utils/       # Utility functions
├── config.ts    # Server configuration
├── index.ts     # Entry point
└── server.ts    # Main server implementation
```

## 许可证

Apache License 2.0。有关更多信息，请参阅 [LICENSE](https://github.com/cyanheads/mentor-mcp-server/blob/HEAD/LICENSE)。

---

使用模型上下文协议构建

**官方网站：** [https://github.com/cyanheads/mentor-mcp-server](https://github.com/cyanheads/mentor-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`developer tools`, `research and data`, `cloud platforms`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`build/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/cyanheads-mentor.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
