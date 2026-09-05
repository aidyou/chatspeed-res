---
title: "智能组件生成器"
description: "一个由人工智能驱动的工具，可以从自然语言描述生成现代UI组件，并与流行的IDE集成，以简化UI开发工作流程。"
---

# 智能组件生成器

一个由人工智能驱动的工具，可以从自然语言描述生成现代UI组件，并与流行的IDE集成，以简化UI开发工作流程。

# 21st.dev 魔法 AI 代理

![MCP Banner](/mcp-assets/d0328c1bb049425c730a656daf1fd834.png)

Magic 组件平台（MCP）是一个强大的 AI 驱动工具，它通过自然语言描述帮助开发者即时创建美观、现代的 UI 组件。它可以无缝集成到流行的 IDE 中，并为 UI 开发提供了一个简化的流程。

## 🌟 功能

- **AI 驱动的 UI 生成**：通过自然语言描述来创建 UI 组件
- **多 IDE 支持**：
  - [Cursor](https://cursor.com) IDE 集成
  - [Windsurf](https://windsurf.ai) 支持
  - [VSCode + Cline](https://cline.bot) 集成（测试版）
- **现代组件库**：访问由 [21st.dev](https://21st.dev) 启发的大量预制且可定制的组件
- **实时预览**：在创建过程中即时查看您的组件
- **TypeScript 支持**：完整的 TypeScript 支持以实现类型安全开发
- **SVGL 集成**：访问大量的专业品牌资产和徽标
- **组件增强**：使用高级功能和动画改进现有组件（即将推出）

## 🎯 工作原理

1. **告诉代理您需要什么**

   - 在您的 AI 代理聊天中，只需键入 `/ui` 并描述您正在寻找的组件
   - 示例：`/ui 创建一个具有响应式设计的现代导航栏`

2. **让魔法为您创造**

   - 您的 IDE 提示您使用 Magic
   - Magic 即时构建出一个精美的 UI 组件
   - 组件灵感来自 21st.dev 的库

3. **无缝集成**
   - 组件自动添加到您的项目中
   - 立即开始使用您的新 UI 组件
   - 所有组件都是完全可定制的

## 🚀 入门指南

### 前提条件

- Node.js（推荐最新 LTS 版本）
- 支持的 IDE 之一：
  - Cursor
  - Windsurf
  - VSCode（带有 Cline 扩展）

### 安装

1. **生成 API 密钥**

   - 访问 [21st.dev Magic 控制台](https://21st.dev/magic/console)
   - 生成一个新的 API 密钥

2. **选择安装方法**

#### 方法 1：CLI 安装（推荐）

一条命令即可为您的 IDE 安装和配置 MCP：

```bash
npx @21st-dev/cli@latest install  --api-key 
```

支持的客户端：cursor, windsurf, cline, claude

#### 方法 2：手动配置

如果您偏好手动设置，请将以下内容添加到您的 IDE 的 MCP 配置文件中：

```json
{
  "mcpServers": {
    "@21st-dev/magic": {
      "command": "npx",
      "args": ["-y", "@21st-dev/magic@latest", "API_KEY=\"your-api-key\""]
    }
  }
}
```

配置文件位置：

- Cursor: `~/.cursor/mcp.json`
- Windsurf: `~/.codeium/windsurf/mcp_config.json`
- Cline: `~/.cline/mcp_config.json`
- Claude: `~/.claude/mcp_config.json`

## ❓ 常见问题解答

### Magic AI 代理如何处理我的代码库？

Magic AI 代理仅写入或修改与其生成的组件相关的文件。它遵循您的项目的代码风格和结构，并无缝集成到现有的代码库中，不会影响应用程序的其他部分。

### 我可以自定义生成的组件吗？

当然！所有生成的组件都是完全可编辑的，并且附带结构良好的代码。您可以像修改代码库中的其他 React 组件一样修改样式、功能和行为。

### 如果我用完了生成次数怎么办？

如果您超过了每月的生成限制，系统会提示您升级计划。您可以随时升级以继续生成组件。您现有的组件将继续保持完全功能。

### 新组件多久会被添加到 21st.dev 的库中？

作者可以随时将组件发布到 21st.dev，Magic Agent 将立即访问这些组件。这意味着您将始终能够访问社区提供的最新组件和设计模式。

### 组件复杂性有限制吗？

Magic AI Agent 可以处理各种复杂度的组件，从简单的按钮到复杂的交互表单。但是，为了获得最佳效果，我们建议将非常复杂的 UI 分解为更小、更易于管理的组件。

## 🛠️ 开发

### 项目结构

```
mcp/
├── app/
│   └── components/     # Core UI components
├── types/             # TypeScript type definitions
├── lib/              # Utility functions
└── public/           # Static assets
```

### 关键组件

- `IdeInstructions`: 不同 IDE 的设置说明
- `ApiKeySection`: API 密钥管理界面
- `WelcomeOnboarding`: 新用户的引导流程

## 🤝 贡献

我们欢迎贡献！请加入我们的 [Discord 社区](https://discord.gg/Qx4rFunHfm) 并提供反馈以帮助改进 Magic Agent。源代码可在 [GitHub](https://github.com/serafimcloud/21st) 上找到。

## 👥 社区与支持

- [Discord 社区](https://discord.gg/Qx4rFunHfm) - 加入我们的活跃社区
- [Twitter](https://x.com/serafimcloud) - 关注我们获取更新

## ⚠️ 测试版通知

Magic Agent 目前处于测试阶段。在此期间，所有功能都是免费的。感谢您的反馈和支持，我们将继续改进平台。

## 📝 许可证

MIT 许可证

## 🙏 致谢

- 感谢我们的测试用户和社区成员
- 特别感谢 Cursor、Windsurf 和 Cline 团队的合作
- 与 [21st.dev](https://21st.dev) 集成以获取组件灵感
- [SVGL](https://svgl.app) 提供的徽标和品牌资产集成

---

欲了解更多信息，请加入我们的 [Discord 社区](https://discord.gg/Qx4rFunHfm) 或访问 [21st.dev/magic](https://21st.dev/magic)。

**官方网站：** [https://github.com/21st-dev/magic-mcp](https://github.com/21st-dev/magic-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `image and video processing`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @21st-dev/magic@latest API_KEY="your-api-key"`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/21st-dev-magic.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
