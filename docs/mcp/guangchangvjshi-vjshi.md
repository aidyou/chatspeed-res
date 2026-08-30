---
title: "光厂MCP"
description: "您可以在支持MCP协议的AI模型客户端中搜索授权的高清商业视频素材。"
---

# 光厂MCP

您可以在支持MCP协议的AI模型客户端中搜索授权的高清商业视频素材。

# 🎬 光厂 MCP 视频素材搜索工具

## ⚠️ 特别说明
若**译文出现乱码**（魔塔强制翻译导致），请切换到原文（中文），方便阅读

---

## 📖 项目概述
🔍 可以在支持MCP协议的AI模型客户端中搜索正版高清商用视频素材

---

## ✨ 核心功能
🎯 在光厂数千万条正版高清商用视频素材中，为您检索并推荐相关视频素材

### 主要特性：
- 🎥 海量、正版、高清视频素材
- 🏢 商用授权，无版权风险
- 🚀 快速、精准的智能搜索体验
- 📋 结构化输出，便于后续处理

---

## 🚀 快速开始

### 步骤1️⃣：获取API密钥
🔑 前往 [光厂MCP官网](https://open.vjshi.com/mcp) 页面获取服务端密钥

> 💡 **提示**：通过密钥您才能够使用搜索功能

### 步骤2️⃣：完成配置
⚙️ 请将 `YOUR_API_KEY` 替换为您的实际密钥，并将下述配置添加到支持MCP的模型客户端

**支持的客户端：** Claude App、Cherry Studio、Cursor、Cline、Windsurf 等

json
{
  "mcpServers": {
    "vjshi-video-mcp": {
      "command": "npx",
      "args": [
        "-y",
        "@vjshi/vjshi-video-mcp@latest"
      ],
      "env": {
        "VJSHI_API_KEY": "YOUR_API_KEY"
      },
      "disabled": false,
      "isActive": true
    }
  }
}

---

## 📄 许可证
📜 该项目根据 **MIT 许可证** 授权，请参阅 LICENSE 文件获取详细信息。

---

## 🤝 联系我们
如有问题或建议，欢迎访问 [光厂MCP](https://open.vjshi.com/mcp) 获取更多帮助！

**官方网站：** [https://github.com/dioa-design/vjshi-video-mcp](https://github.com/dioa-design/vjshi-video-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`search`, `art and culture`, `entertainment and media`, `光厂`, `vj师网`, `视频素材网`, `高清视频素材下载`, `ae模板下载`, `免费视频素材`, `素材搜索推荐`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @vjshi/vjshi-video-mcp@latest`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/guangchangvjshi-vjshi.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
