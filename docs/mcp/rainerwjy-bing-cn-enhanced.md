---
title: "bing必应搜索增强版"
description: "一个基于MCP（模型上下文协议）的中文必应搜索工具，可以直接通过Claude等支持MCP的AI来搜索必应并获取网页内容，无需API密钥。"
---

# bing必应搜索增强版

一个基于MCP（模型上下文协议）的中文必应搜索工具，可以直接通过Claude等支持MCP的AI来搜索必应并获取网页内容，无需API密钥。

# Bing CN MCP Enhanced

一个基于 MCP (Model Context Protocol) 的中文必应搜索工具，可以直接通过 Claude 或其他支持 MCP 的 AI 来搜索必应并获取网页内容。
解决了市面上BingMcp搜索工具都存在的因为反扒机制而返回随机数据的问题。但因为modelscope.cn托管不支持playwright，所以只能用stdio方案。

## 特点
- 使用页面解析方式完成bing查询和内容快速获取
- 修复其他bing 查询的各类bug，尤其是bing如果识别你是个机器人会随机给数据，导致搜索失败问题
- 持续维护 有问题提gh issues 
- 无需 API 密钥，直接爬取必应搜索结果
- 轻量级，易于安装和使用
- 支持 Claude 等 AI 工具调用

## 安装
背后依托playwright， 开始的时候会自己下载
所以请保持使用的机器有网络

### 全局安装

```bash
npm install -g bing-cn-mcp-enhanced
```

### 或者直接通过 npx 运行

```bash
npx bing-cn-mcp-enhanced
```

## 使用方法

### 启动服务器

```bash
bing-cn-mcp-enhanced
```

或者使用 npx：

```bash
npx bing-cn-mcp-enhanced
```

### 在支持 MCP 的环境中使用

在支持 MCP 的环境（如 Cursor）中，配置 MCP 服务器来使用它：

1. 找到 MCP 配置文件（例如 `.cursor/mcp.json`）
2. 添加服务器配置：

```json
{
  "mcpServers": {
    "EnhancedBing": {
      "args": [
        "bing-cn-mcp-enhanced"
      ],
      "command": "npx"
    }
  }
}
```
Windows用户的配置

```json
{
  "mcpServers": {
    "EnhancedBing": {
        "command": "cmd",
        "args": [
          "/c",
          "npx",
          "bing-cn-mcp-enhanced"
      ]
    }
  }
}
```

3. 现在你可以在 Claude 中使用 `mcp__bing_search` 和 `mcp__fetch_webpage` 工具了

4. 你也可以使用 Lynxe 来使用这个工具  [Lynxe github](https://github.com/spring-ai-alibaba/Lynxe)

### 查看日志

MCP 服务器的日志输出到 stderr。如果你想将日志保存到文件以便查看，可以通过修改 MCP 配置来实现：

Lynxe则可以在后台日志直接看到

## 作者

Lynxe

## 许可证

MIT

**官方网站：** [https://github.com/Lynxe-public/bing-mcp-cn-enhanced](https://github.com/Lynxe-public/bing-mcp-cn-enhanced)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`
- 标签：`search`, `bing mcp 持续维护 增强`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`bing-cn-mcp-enhanced`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/rainerwjy-bing-cn-enhanced.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
