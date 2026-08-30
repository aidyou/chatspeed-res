---
title: "AI简历助手"
description: "一个通过分析你的编程项目、自动提取技能并生成专业描述来更新你的JSON简历，从而增强AI助手功能的服务器。"
---

# AI简历助手

一个通过分析你的编程项目、自动提取技能并生成专业描述来更新你的JSON简历，从而增强AI助手功能的服务器。

# JSON Resume MCP 服务器

[![npm 版本](/mcp-assets/021165c1d98f342a44b4b4c516a3a7d8.svg)](https://www.npmjs.com/package/@jsonresume/mcp)
[![许可证: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)
[![GitHub 问题](/mcp-assets/246bdfaf8869026642f59da7103dfd04.svg)](https://github.com/jsonresume/mcp/issues)
[Smithery](https://smithery.ai/server/@jsonresume/mcp)

**通过分析您的编码项目，使用 AI 自动更新简历**

[安装](#installation) • [功能](#features) • [使用方法](#usage) • [配置](#configuration) • [贡献](#contributing) • [测试](#testing)

## 什么是 JSON Resume MCP 服务器？

这是一个 [模型上下文协议 (MCP)](https://modelcontextprotocol.ai) 服务器，它增强了 AI 助手的能力，使其能够通过分析您的编码项目来更新您的 [JSON 简历](https://jsonresume.org)。MCP 服务器提供了工具，使像 [Windsurf](https://www.windsurf.io/) 或 [Cursor](https://cursor.sh/) 中的 AI 助手能够：

1. 检查您是否已有 JSON 简历
2. 分析您的代码库以了解您的技术技能和项目
3. 使用当前项目的详细信息增强您的简历

有了这个工具，您可以简单地要求您的 AI 助手“用我当前的项目增强我的简历”，它会自动分析您的代码，提取相关的技能和项目细节，并相应地更新您的简历。

视频演示：[https://x.com/ajaxdavis/status/1896953226282594381](https://x.com/ajaxdavis/status/1896953226282594381)

## 功能

- **简历增强**：自动分析您的代码库并将项目详情添加到您的简历中
- **GitHub 集成**：从 GitHub Gists 获取并更新您的简历
- **AI 支持**：使用 OpenAI 生成专业的项目和技能描述
- **TypeScript/Zod 验证**：确保您的简历遵循 JSON 简历标准
- **JSON 简历生态系统**：与 [JSON 简历注册表](https://registry.jsonresume.org) 兼容

## 安装

### 前提条件

- 带有个人访问令牌（具有 gist 范围）的 GitHub 账户
- OpenAI API 密钥
- Node.js 18+
- 支持 MCP 的 IDE（Windsurf 或 Cursor）

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@jsonresume/mcp) 自动为 Claude Desktop 安装 mcp：

```bash
npx -y @smithery/cli install @jsonresume/mcp --client claude
```

### 通过 NPM 安装

```bash
npm install -g @jsonresume/mcp
```

### 在 Windsurf 或 Cursor 中安装

将以下内容添加到您的 Windsurf 或 Cursor 配置中：

#### Windsurf

打开设置 → MCP 服务器并添加：

```json
{
  "jsonresume": {
    "command": "npx",
    "args": ["-y", "@jsonresume/mcp"],
    "env": {
      "GITHUB_TOKEN": "your-github-token",
      "OPENAI_API_KEY": "your-openai-api-key",
      "GITHUB_USERNAME": "your-github-username"
    }
  }
}
```

#### Cursor

添加到您的 `~/.cursor/mcp_config.json` 文件中：

```json
{
  "mcpServers": {
    "jsonresume": {
      "command": "npx",
      "args": ["-y", "@jsonresume/mcp"],
      "env": {
        "GITHUB_TOKEN": "your-github-token",
        "OPENAI_API_KEY": "your-openai-api-key",
        "GITHUB_USERNAME": "your-github-username"
      }
    }
  }
}
```

## 使用方法

一旦安装并配置好，您可以使用以下命令与您的 AI 助手交互：

### 使用当前项目增强您的简历

询问您的 AI 助手：
```
"Can you enhance my resume with details from my current project?"
```

助手将会：

1. 在 GitHub 上找到你现有的简历（如果需要的话可以创建一个新的）
2. 分析你当前项目的代码库
3. 生成对你项目和技能的专业描述
4. 用新信息更新你的简历
5. 将更改保存回 GitHub
6. 提供一个链接以查看更新后的简历

### 检查您的简历状态

询问您的 AI 助手：
```
"Can you check if I have a JSON Resume?"
```

助手会检查您是否有现有的简历并显示其详细信息。

### 分析您的代码库

询问您的 AI 助手：
```
"What technologies am I using in this project?"
```

助手将分析您的代码库，并提供关于语言、技术及最近提交的见解。

## 配置

MCP 服务器需要以下环境变量：

| 变量 | 描述 |
|----------|-------------|
| `GITHUB_TOKEN` | 您具有 gist 权限的 GitHub 个人访问令牌 |
| `GITHUB_USERNAME` | 您的 GitHub 用户名 |
| `OPENAI_API_KEY` | 您的 OpenAI API 密钥 |

## 开发

要在开发模式下运行服务器：

1. 克隆仓库：
```bash
git clone https://github.com/jsonresume/mcp.git
cd mcp
```

2. 安装依赖项：
```bash
npm install
```

3. 以开发模式运行：
```bash
npm run dev
```

这将以调试工具启动 MCP 服务器。

## 贡献

欢迎贡献！以下是您可以如何贡献的方法：

1. Fork 仓库
2. 创建功能分支：`git checkout -b feature/amazing-feature`
3. 提交您的更改：`git commit -m 'Add some amazing feature'`
4. 推送到该分支：`git push origin feature/amazing-feature`
5. 打开一个 Pull Request

请确保您的代码遵循现有的风格并且包含了适当的测试。

## 测试

MCP 服务器包含多个测试脚本来帮助调试和验证功能。

### 运行测试

所有测试脚本都位于 `tests/` 目录中。

在运行测试之前，请设置您的环境变量：
```bash
export GITHUB_TOKEN=your_github_token
export OPENAI_API_KEY=your_openai_api_key
export GITHUB_USERNAME=your_github_username
```

#### 检查 OpenAI API 密钥

验证您的 OpenAI API 密钥是否正常工作：
```bash
npx tsx tests/check-openai.ts
```

#### 模拟简历增强

使用模拟数据测试简历增强功能（不调用 API）：
```bash
npx tsx tests/debug-mock.ts
```

#### 完整简历增强测试

通过实时 API 调用来测试完整的简历增强过程：
```bash
npx tsx tests/debug-enhance.ts
```

#### MCP 协议测试

测试 MCP 服务器协议通信：
```bash
node tests/test-mcp.js
```

### 添加到 package.json

为了方便，您可以将这些测试命令添加到您的 package.json 中：
```json
"scripts": {
  "test:openai": "tsx tests/check-openai.ts",
  "test:mock": "tsx tests/debug-mock.ts",
  "test:enhance": "tsx tests/debug-enhance.ts",
  "test:mcp": "node tests/test-mcp.js"
}
```

然后通过 `npm run test:mock` 等方式运行它们。

## 许可证

此项目根据 MIT 许可证许可 - 有关详细信息，请参阅 [LICENSE](https://github.com/jsonresume/mcp/blob/HEAD/LICENSE) 文件。

## 致谢

- [JSON Resume](https://jsonresume.org) 提供了简历标准
- [Model Context Protocol](https://modelcontextprotocol.ai) 使能够集成 AI 工具
- [OpenAI](https://openai.com) 为 AI 简历增强提供了动力

**官方网站：** [https://github.com/jsonresume/mcp](https://github.com/jsonresume/mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`version control`, `developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @jsonresume/mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/jsonresume-mcp.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
