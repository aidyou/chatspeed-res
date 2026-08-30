---
title: "思维导图mcp"
description: "这是一个用于生成思维导图的MCP（模型上下文协议）服务器。它可以根据文本内容自动生成思维导图，并返回可访问的思维导图图片链接。该工具支持CodeBuddy、Cursor等MCP客户端，并基于Coze API提供强大的思维导图生成功能。"
---

# 思维导图mcp

这是一个用于生成思维导图的MCP（模型上下文协议）服务器。它可以根据文本内容自动生成思维导图，并返回可访问的思维导图图片链接。该工具支持CodeBuddy、Cursor等MCP客户端，并基于Coze API提供强大的思维导图生成功能。

# @jiushan93/mind-map-mcp

一个用于生成思维导图的 MCP (Model Context Protocol) 服务器。

## 功能特性

- 🧠 根据文本内容自动生成思维导图
- 🔗 返回可访问的思维导图图片链接
- 🚀 支持 CodeBuddy、Cursor 等 MCP 客户端
- 🌐 基于 Coze API 的强大思维导图生成能力

## 安装

### 通过 NPM 安装

```bash
npm install -g @jiushan93/mind-map-mcp
```

### 通过 npx 直接使用

```bash
npx @jiushan93/mind-map-mcp
```

## 配置

### 在 CodeBuddy 中配置

1. 打开 CodeBuddy 设置
2. 找到 MCP 服务器配置
3. 添加新的服务器：

```json
{
  "mcpServers": {
    "mind-map": {
      "command": "npx",
      "args": ["@jiushan93/mind-map-mcp"]
    }
  }
}
```

### 在 Cursor 中配置

1. 打开 Cursor 设置 (Ctrl/Cmd + ,)
2. 搜索 "MCP"
3. 在 MCP 服务器配置中添加：

```json
{
  "mind-map": {
    "command": "npx",
    "args": ["@jiushan93/mind-map-mcp"]
  }
}
```

## 使用方法

配置完成后，你可以在支持 MCP 的工具中使用以下功能：

### 生成思维导图

```
请帮我生成一个关于"分布式系统架构"的思维导图
```

或者直接调用工具：

```
使用 generate_mindmap 工具，内容为："机器学习的基本概念和应用"
```

## 可用工具

### generate_mindmap

根据输入内容生成思维导图。

**参数：**
- `content` (string, 必需): 要转换为思维导图的内容描述

**返回：**
- 思维导图的图片链接
- 生成状态信息

**示例：**
```json
{
  "content": "深度学习的发展历程和主要技术"
}
```

## 开发

### 本地开发

1. 克隆仓库：
```bash
git clone https://github.com/jiushan-test/Mind-map-mcp.git
cd Mind-map-mcp
```

2. 安装依赖：
```bash
npm install
```

3. 构建项目：
```bash
npm run build
```

4. 启动开发模式：
```bash
npm run dev
```

### 项目结构

```
Mind-map-mcp/
├── src/
│   └── index.ts          # 主要的 MCP 服务器代码
├── dist/                 # 编译后的 JavaScript 文件
├── package.json          # 项目配置
├── tsconfig.json         # TypeScript 配置
└── README.md            # 项目说明
```

## API 说明

本工具使用 Coze API 来生成思维导图。API 详情：

- **端点**: `https://api.coze.cn/v1/workflow/run`
- **方法**: POST
- **认证**: Bearer Token
- **返回**: 思维导图图片链接

## 故障排除

### 常见问题

1. **"未知工具" 错误**
   - 确保 MCP 服务器正确配置
   - 检查工具名称是否正确 (`generate_mindmap`)

2. **API 请求失败**
   - 检查网络连接
   - 确认 API 服务状态

3. **中文编码问题**
   - 本工具已处理中文编码，支持中文内容输入

### 调试模式

启动时会在 stderr 输出调试信息，可以通过查看日志来诊断问题。

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！

## 更新日志

### v1.0.1
- 更新 API 配置
- 更新包名为 @jiushan93/mind-map-mcp
- 更新项目仓库地址

### v1.0.0
- 初始版本发布
- 支持基本的思维导图生成功能
- 支持 CodeBuddy 和 Cursor 集成

**官方网站：** [https://github.com/jiushan-test/Mind-map-mcp](https://github.com/jiushan-test/Mind-map-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`memory`
- 标签：`knowledge and memory`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`@jiushan93/mind-map-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/yspdsh-mind-v1-2.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
