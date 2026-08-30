---
title: "人生教练Agent（by AI产品自由）"
description: "人生教练Agent，探讨生活决策"
---

# 人生教练Agent（by AI产品自由）

人生教练Agent，探讨生活决策

# 人生教练 MCP 项目

一个基于 Model Context Protocol (MCP) 的智能人生教练系统，提供 12 位知名人生教练的专业提示词和智能对话功能。

## 功能特性

- **智能人生教练对话** - 12 位知名人生教练提供专业建议
- **多角度思考** - 支持多位教练同时分析问题
- **动态教练选择** - 根据问题类型智能匹配最合适的教练

## 可用教练

| 教练 | 专长领域 | 适用场景 |
|------|----------|----------|
| 李笑来 | 认知科学应用 | 个人成长、学习方法 |
| 苏格拉底 | 启发式对话 | 思辨、哲学思考 |
| 杰伊·福雷斯特 | 系统动力学 | 系统思维、反馈机制 |
| 镜像的我 | 个人记忆分析 | 自我对话、反思 |
| 思辨之神 | 逆向思考 | 逻辑分析、漏洞发现 |
| 大卫·休谟 | 真相拷问 | 深度思考、批判性思维 |
| 问题的考古学家 | 问题本质挖掘 | 复杂问题分析 |
| 炼金士 | 情绪转化 | 负面情绪处理 |
| 史蒂夫·乔布斯 | 产品思维 | 用户体验、完美主义 |
| 查理芒格 | 多元思维 | 投资思维、智慧决策 |
| CBT心理学家 | 认知行为疗法 | 心理健康、情绪调节 |
| 埃隆·马斯克 | 第一性原理 | 创新思维、颠覆式思考 |

## 快速开始

### 1. 安装

**通过 npm 安装（推荐）**
```bash
npm install -g lifecoach-mcp-server
```

**从源码安装**
```bash
cd mcp-server
npm install
npm start
```

### 2. 配置 Claude Desktop

在 Claude Desktop 设置中添加 MCP 服务器：

**全局安装配置：**
```json
{
  "mcpServers": {
    "lifecoach": {
      "command": "lifecoach-mcp-server"
    }
  }
}
```

**配置文件位置：**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%/Claude/claude_desktop_config.json`

### 3. 开始使用

在 Claude Desktop 中说：
- "启动人生教练"
- "我想要李笑来的建议"
- "搜索关于思维相关的教练"

## 项目结构

```
人生教练mcp/
├── mcp-server/           # MCP 服务器（npm: lifecoach-mcp-server）
├── worker/              # Cloudflare Worker API
├── config/              # 配置文档
└── README.md           # 项目文档
```

## 技术架构

```
用户 → Claude Desktop → MCP Server → Cloudflare Worker → Supabase
```

## API 工具

### start_lifecoach
启动人生教练对话模式

### get_lifecoach
获取特定教练信息
```json
{
  "name": "get_lifecoach",
  "arguments": {
    "name": "李笑来"
  }
}
```

### list_lifecoaches
获取所有教练列表

### search_lifecoach
搜索匹配的教练
```json
{
  "name": "search_lifecoach",
  "arguments": {
    "keyword": "思维"
  }
}
```

## 许可证

MIT License

**官方网站：** [https://www.npmjs.com/package/lifecoach-mcp-server](https://www.npmjs.com/package/lifecoach-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`communication`
- 标签：`communication`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y lifecoach-mcp-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/chengfeng2025-lifecoach.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
