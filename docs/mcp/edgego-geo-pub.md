---
title: "MCP地理发布"
description: "将 EdgeOne 页面功能与大型语言模型集成，通过模型上下文协议（MCP）获取和利用用户地理定位信息。"
---

# MCP地理发布

将 EdgeOne 页面功能与大型语言模型集成，通过模型上下文协议（MCP）获取和利用用户地理定位信息。

# MCP与Pages Functions：地理位置演示

该项目展示了如何使用EdgeOne Pages Functions来获取用户的地理位置信息，并通过MCP（模型上下文协议）将其与大型语言模型集成。

## 演示

![](/mcp-assets/67f6315167cad0d50116e51ef937c048.gif)

## 部署

[![使用EdgeOne Pages部署](/mcp-assets/0e43c38e86c821a6cca6f1708caf1c7c.svg)](https://edgeone.ai/pages/new?template=mcp-geo)

更多模板: [EdgeOne Pages](https://edgeone.ai/pages/templates)

## 组件

### 1. EdgeOne Pages Functions: 地理位置

项目包含一个EdgeOne Pages Function，用于检索用户地理位置信息：

* 使用EdgeOne请求上下文访问地理位置数据
* 以JSON格式返回位置信息
* 位于 `functions/get_geo.ts`

### 2. MCP服务器集成

MCP服务器组件为大型语言模型提供了访问地理位置数据的接口：

* 实现了模型上下文协议 (MCP)
* 提供了一个`get_geolocation`工具，可供AI模型使用
* 使用EdgeOne Pages Function来获取地理位置数据
* 位于 `mcp-server/index.ts`

## MCP配置

要将MCP服务器与大型语言模型一起使用，请添加以下配置：

json
{
  "mcpServers": {
    "edgeone-geo-mcp-server": {
      "command": "tsx",
      "args": ["path/to/mcp-server/index.ts"]
    }
  }
}

## 了解更多

* [EdgeOne Pages](https://edgeone.ai/products/pages)
* [EdgeOne Pages Functions 文档](https://edgeone.ai/document/162227908259442688)
* [模型上下文协议 (MCP)](https://modelcontextprotocol.github.io) - 了解如何将AI模型与外部工具和服务集成

**官方网站：** [https://github.com/edgego/mcp-geo-pub](https://github.com/edgego/mcp-geo-pub)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`location services`, `rag systems`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`tsx`
- 参数：`path/to/mcp-server/index.ts`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/edgego-geo-pub.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
