---
title: "成都线下活动MCP"
description: "一个基于 Model Context Protocol (MCP) 的服务端（Server），用于抓取并解析成都青年之家的最新活动信息。（后续会扩宽范围）"
---

# 成都线下活动MCP

一个基于 Model Context Protocol (MCP) 的服务端（Server），用于抓取并解析成都青年之家的最新活动信息。（后续会扩宽范围）

# MCP Server · 成都青年之家活动抓取器

一个基于 [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) 的服务端（Server），
用于抓取并解析 [成都青年之家](https://cdyouth.cdcyl.org.cn/jgc/) 的最新活动信息。

本项目提供一个 MCP Tool：`fetch_chengdu_youth_activities`  

---

## ✨ 功能特性

- 🔍 **抓取活动信息**：从 `https://cdyouth.cdcyl.org.cn/jgc/` 获取最新活动。
- 📝 **自动解析**：活动标题、标签、时间、地点、状态、浏览量、图片等。
- 📦 **MCP Tool 接口**：可直接在兼容 MCP 的客户端（如 Anthropic MCP Inspector）中使用。
- 🔄 **SSE Transport**：基于 Server-Sent Events 实现（兼容旧版 MCP 客户端）。
- 🧩 **结构化输出**：返回 JSON 数组，同时包含可读文本。

---

## 📦 安装与运行

### 1. 克隆仓库
```bash
git clone https://github.com//mcp-chengdu-youth-activities.git
cd mcp-chengdu-youth-activities
```

**官方网站：** [https://github.com/fsyj123/mcp-chengdu-youth-activities](https://github.com/fsyj123/mcp-chengdu-youth-activities)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`art and culture`, `娱乐`, `生活`, `线下活动`, `成都`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`mcp-cd-youth`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/fsyj123-youth-activities.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
