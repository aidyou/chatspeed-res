---
title: "提示词增强"
description: "接受简单的关键词、短语或初始简短提示，并将其增强为详细、高质量的提示。此工具通过添加结构、上下文和具体性来提升最低限度的输入，将基本想法转化为有效的提示，并进行优化，以便从 AI 模型中生成更好、更可预测的结果。"
---

# 提示词增强

接受简单的关键词、短语或初始简短提示，并将其增强为详细、高质量的提示。此工具通过添加结构、上下文和具体性来提升最低限度的输入，将基本想法转化为有效的提示，并进行优化，以便从 AI 模型中生成更好、更可预测的结果。

# [PromptPilot](https://promptpilot.online/) 
 - AI 提示生成与增强工具

**PromptPilot** 是一个基于人工智能的网页应用程序，旨在帮助用户为各种生成式AI模型生成和增强提示。它提供了一个快速生成功能以满足简单需求，以及一个独特的对话引导（Masterful Prompt Creator）来创建高质量、详细的提示。此仓库包含了PromptPilot的代码库。

## ✨ 功能
该应用程序专注于两个核心功能：

1.  **🚀 快速提示生成：**
    *   接受用户提供的简单关键词或短语。
    *   利用AI根据输入生成一个或多个基本的、即用型提示。
    *   非常适合需要快速起点的用户。

2.  **🧠 引导式问答提示增强：**
    *   提供一个交互式的聊天界面。
    *   通过一系列由AI引导的问题来指导用户。
    *   帮助用户详细表达并细化他们的需求。
    *   根据引导对话生成全面且高质量的提示。
    *   目标是显著提高AI输出的相关性和质量。

## 🚀 开始使用

### 先决条件
*   Node.js 和 npm（或yarn），用于前端/后端（取决于您的技术栈）
*   Docker 和 Docker Compose（可选，但推荐用于更简单的设置）

### 步骤 1: 克隆仓库
```bash
git clone https://github.com/FelixFoster/mcp-enhance-prompt # 替换为您实际的仓库URL
cd mcp-enhance-prompt
```

### 步骤 2: 安装依赖
进入相关目录并安装依赖。
```bash
npm install
```

### 步骤 4: 构建项目
```bash
npm run build
```

### 步骤 5: 运行应用程序
您有几种运行应用程序的选择：

#### 选项 1: 直接运行
```bash
node build/index.js
```

#### 选项 2: 使用Docker运行
```bash
docker build -t enhance-prompt-server .
docker run -i --rm -e PROMPT_PILOT_API_KEY=your_prompt_pilot_api_key enhance-prompt-server
```

#### 选项 3: 使用npx运行
```bash
PROMPT_PILOT_API_KEY=your_prompt_pilot_api_key npx -y enhance-prompt-server
```

### 步骤 6: 访问应用程序
打开您的网络浏览器并导航到前端应用程序服务的地址（例如，`http://localhost:9593/rest`）。

## 🐛 故障排除
*   **后端日志：** 检查您的后端进程控制台日志中的错误消息。
*   **网络问题：** 确保您的后端在正确的端口上运行，并且没有防火墙问题阻止访问。如果使用Docker，请验证端口映射。
*   **依赖项：** 确保所有项目依赖项已成功安装。

## 🤝 贡献
欢迎贡献！如果您想为PromptPilot做贡献，请遵循以下步骤：
1.  分叉仓库。
2.  创建一个新的分支 (`git checkout -b feature/your-feature`)。
3.  进行更改。
4.  提交更改 (`git commit -am 'feat: Add new feature X'`)。
5.  将分支推送到远程 (`git push origin feature/your-feature`)。
6.  创建一个新的拉取请求 (Pull Request)。

请确保您的代码遵循项目的编码标准，并在适当的地方包含测试。

## 📄 许可证
本项目采用MIT许可证发布 - 详情请参阅 LICENSE 文件。

**官方网站：** [https://github.com/FelixFoster/mcp-enhance-prompt](https://github.com/FelixFoster/mcp-enhance-prompt)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`aigc`, `art and culture`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y enhance-prompt-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/felixfoster-enhance-prompt.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
