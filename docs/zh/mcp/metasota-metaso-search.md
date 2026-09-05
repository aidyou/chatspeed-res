---
title: "秘塔AI搜索"
description: "秘塔AI搜索的MCP服务"
---

# 秘塔AI搜索

秘塔AI搜索的MCP服务

# 秘塔AI搜索的MCP服务

## 简介

秘塔AI搜索的MCP服务是一个基于Model Context Protocol (MCP) 的智能搜索和问答服务，为AI助手提供强大的网络搜索、内容读取和智能问答能力。通过集成本服务，AI助手可以实时获取网络信息，读取网页内容，并基于RAG技术提供准确的智能问答。

## 服务地址

**ModelScope地址**: [https://www.modelscope.cn/mcp/servers/metasota/metaso-search](https://www.modelscope.cn/mcp/servers/metasota/metaso-search)

**API端点**: `https://metaso.cn/api/mcp`

## 功能特性

### 🔍 多维度搜索
- 支持网页、文档、论文、图片、视频、播客等多种内容类型搜索
- 灵活的搜索范围配置
- 可自定义返回结果数量

### 📖 网页内容读取
- 支持任意URL的网页内容提取
- 提供JSON和Markdown两种输出格式
- 智能内容解析和结构化处理

### 💬 智能问答服务
- 基于RAG（检索增强生成）技术
- 多模型支持，默认使用快速模型
- 结合搜索结果提供准确回答

## 工具列表

### 1. metaso_web_search - 网络搜索工具

**功能描述**: 根据关键词搜索网页、文档、论文、图片、视频、播客等内容

**参数说明**:
- `q` (必填, string): 搜索查询关键词
- `scope` (可选, string): 搜索范围，可选值：`webpage`, `document`, `paper`, `image`, `video`, `podcast`
- `includeSummary` (可选, boolean): 通过网页摘要信息提升搜索结果的召回率
- `includeRawContent` (可选, boolean): 抓取所有来源网页原文
- `size` (可选, integer): 返回结果数量，默认为10

**使用示例**:

```json
{
  "q": "人工智能最新发展",
  "scope": "paper",
  "includeSummary": true,
  "size": 5
}
```

### 2. metaso_web_reader - 网页内容读取工具

**功能描述**: 读取指定URL的网页内容

**参数说明**:
- `url` (必填, string): 要读取的URL地址
- `format` (必填, string): 输出格式，可选值：`json`, `markdown`

**使用示例**:

```json
{
  "url": "https://example.com/article",
  "format": "markdown"
}
```

### 3. metaso_chat - 智能问答工具

**功能描述**: 基于RAG的智能问答服务

**参数说明**:
- `message` (必填, string): 用户问题
- `model` (可选, string): 使用的模型，默认为"fast"

**使用示例**:

```json
{
  "message": "请解释一下量子计算的基本原理",
  "model": "fast"
}
```

## 配置方法

### 1. 基础配置

在您的MCP客户端配置文件中添加以下配置：
> 请将YOUR_API_KEY替换为你自己的ApiKey
```json
{
  "mcpServers": {
    "metaso": {
      "url": "https://metaso.cn/api/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}
```

VSCode配置
```json
{
  "servers": {
    "metaso": {
	  "url": "https://metaso.cn/api/mcp",
	  "type": "http",
	  "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  },
  "inputs": []
}
```

### 2. API密钥获取

1. 访问秘塔AI搜索官网
2. 注册并登录账户
3. 访问API控制台[(https://metaso.cn/search-api/api-keys)](https://metaso.cn/search-api/api-keys)中获取API密钥
4. 将密钥替换配置中的 `YOUR_API_KEY`

## 使用场景

### 📚 学术研究
- 搜索最新论文和研究资料
- 获取特定领域的学术文档
- 快速获取研究背景信息

### 📰 信息获取
- 实时新闻和资讯搜索
- 网页内容快速提取
- 多媒体内容发现

### 🤖 AI增强
- 为AI助手提供实时信息检索能力
- 增强对话系统的知识库
- 支持基于最新信息的智能问答

### 💼 商业应用
- 市场调研和竞品分析
- 行业趋势监控
- 客户服务知识库构建

## 技术优势

- **高性能**: 基于秘塔AI搜索的强大搜索引擎
- **多格式支持**: 支持多种内容类型和输出格式
- **RAG技术**: 结合检索和生成，提供准确回答
- **易于集成**: 标准MCP协议，兼容性强
- **灵活配置**: 丰富的参数选项，满足不同需求

## 注意事项

1. **API配额**: 请注意API调用配额限制，合理使用服务。2. **内容合规**: 搜索和获取的内容请遵守相关法律法规。
3. **缓存策略**: 建议实施适当的缓存策略以提高效率。
4. **错误处理**: 请在应用中实现合适的错误处理机制。

## 支持与反馈

如果您在使用过程中遇到问题或有改进建议，欢迎通过以下方式联系我们：

- 官方技术支持邮箱: support-1@metasota.ai
- 官网客服: 19980541467（微信同号）

---

*本服务由秘塔AI搜索团队提供技术支持，致力于为开发者提供优质的AI搜索解决方案。*

**官方网站：** [https://metaso.cn/api/mcp](https://metaso.cn/api/mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `chinese`

## MCP 配置

- 传输方式：`http`
- 启动命令：``
- 参数：无

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/metasota-metaso-search.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
