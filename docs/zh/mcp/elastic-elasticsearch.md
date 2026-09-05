---
title: "Elasticsearch"
description: "将Claude和其他MCP客户端连接到Elasticsearch数据，允许用户通过自然语言对话与其Elasticsearch索引进行交互。"
---

# Elasticsearch

将Claude和其他MCP客户端连接到Elasticsearch数据，允许用户通过自然语言对话与其Elasticsearch索引进行交互。

# Elasticsearch MCP 服务器

通过模型上下文协议 (MCP) 直接从任何 MCP 客户端（如 Claude Desktop）连接到您的 Elasticsearch 数据。

此服务器使用 Model Context Protocol 将代理连接到您的 Elasticsearch 数据。它允许您通过自然语言对话与您的 Elasticsearch 索引进行交互。

  

## 可用工具

* `list_indices`: 列出所有可用的 Elasticsearch 索引
* `get_mappings`: 获取特定 Elasticsearch 索引的字段映射
* `search`: 使用提供的查询 DSL 执行 Elasticsearch 搜索
* `get_shards`: 获取所有或特定索引的分片信息

## 前提条件

* 一个 Elasticsearch 实例
* Elasticsearch 身份验证凭据（API 密钥或用户名/密码）
* MCP 客户端（例如 Claude Desktop）

## 演示

[https://github.com/user-attachments/assets/5dd292e1-a728-4ca7-8f01-1380d1bebe0c](https://github.com/user-attachments/assets/5dd292e1-a728-4ca7-8f01-1380d1bebe0c)

## 安装与设置

### 使用已发布的 NPM 包

> [!TIP]
> 使用 Elasticsearch MCP 服务器最简单的方法是通过已发布的 npm 包。

1. **配置 MCP 客户端**
   - 打开您的 MCP 客户端。请参阅 [MCP 客户端列表](https://modelcontextprotocol.io/clients)，这里我们正在配置 Claude Desktop。
   - 转到 **设置 > 开发者 > MCP 服务器**
   - 单击 `编辑配置` 并添加一个新的 MCP 服务器，配置如下：

```json
   {
     "mcpServers": {
       "elasticsearch-mcp-server": {
         "command": "npx",
         "args": [
           "-y",
           "@elastic/mcp-server-elasticsearch"
         ],
         "env": {
           "ES_URL": "your-elasticsearch-url",
           "ES_API_KEY": "your-api-key"
         }
       }
     }
   }
```

2. **开始对话**
   - 在您的 MCP 客户端中打开一个新的对话
   - MCP 服务器应自动连接
   - 现在您可以询问关于您的 Elasticsearch 数据的问题了

### 配置选项

Elasticsearch MCP 服务器支持配置选项以连接到您的 Elasticsearch：

> [!NOTE]
> 您必须提供 API 密钥或同时提供用户名和密码进行身份验证。

| 环境变量 | 描述 | 是否必需 |
|---------------------|-------------|----------|
| `ES_URL` | 您的 Elasticsearch 实例 URL | 是 |
| `ES_API_KEY` | 用于身份验证的 Elasticsearch API 密钥 | 否 |
| `ES_USERNAME` | 用于基本身份验证的 Elasticsearch 用户名 | 否 |
| `ES_PASSWORD` | 用于基本身份验证的 Elasticsearch 密码 | 否 |
| `ES_CA_CERT` | 自定义 CA 证书路径，用于 Elasticsearch SSL/TLS | 否 |

### 本地开发

> [!NOTE]
> 如果您想要修改或扩展 MCP 服务器，请遵循以下本地开发步骤。

1. **使用正确的 Node.js 版本**
```bash
   nvm use
```

2. **安装依赖项**
```bash
   npm install
```

3. **构建项目**
```bash
   npm run build
```

4. **在 Claude Desktop App 中本地运行**
   - 打开 **Claude Desktop App**
   - 进入 **设置 > 开发者 > MCP 服务器**
   - 点击 `编辑配置` 并添加一个新的 MCP 服务器，配置如下：

```json
   {
     "mcpServers": {
       "elasticsearch-mcp-server-local": {
         "command": "node",
         "args": [
           "/path/to/your/project/dist/index.js"
         ],
         "env": {
           "ES_URL": "your-elasticsearch-url",
           "ES_API_KEY": "your-api-key"
         }
       }
     }
   }
```

5. **使用 MCP 检查器进行调试**
```bash
   ES_URL=your-elasticsearch-url ES_API_KEY=your-api-key npm run inspector
```

   这将启动 MCP 检查器，允许您调试和分析请求。您应该会看到：

```bash
   Starting MCP inspector...
   Proxy server listening on port 3000

   🔍 MCP Inspector is up and running at http://localhost:5173 🚀
```

## 贡献

我们欢迎社区的贡献！有关如何贡献的详细信息，请参阅 [贡献指南](https://github.com/elastic/mcp-server-elasticsearch/blob/HEAD/docs/CONTRIBUTING.md)。

## 示例问题

> [!TIP]
> 以下是一些您可以使用 MCP 客户端尝试的自然语言查询。

* "我的 Elasticsearch 集群中有哪些索引？"
* "显示 'products' 索引的字段映射。"
* "查找上个月超过 $500 的所有订单。"
* "哪些产品获得了最多的五星评价？"

## 工作原理

1. MCP 客户端分析您的请求并确定需要哪些 Elasticsearch 操作。
2. MCP 服务器执行这些操作（列出索引、获取映射、执行搜索）。
3. MCP 客户端处理结果并以用户友好的格式呈现。

## 安全最佳实践

> [!WARNING]
> 避免使用集群管理员权限。创建具有有限范围的专用 API 密钥，并在索引级别应用细粒度的访问控制，以防止未经授权的数据访问。

您可以创建一个具有最小权限的专用 Elasticsearch API 密钥来控制对数据的访问：

```
POST /_security/api_key
{
  "name": "es-mcp-server-access",
  "role_descriptors": {
    "mcp_server_role": {
      "cluster": [
        "monitor"
      ],
      "indices": [
        {
          "names": [
            "index-1",
            "index-2",
            "index-pattern-*"
          ],
          "privileges": [
            "read",
            "view_index_metadata"
          ]
        }
      ]
    }
  }
}
```

## 许可证

该项目根据 Apache License 2.0 许可。

## 故障排除

* 确保您的 MCP 配置正确。
* 验证您的 Elasticsearch URL 是否可以从您的机器访问。
* 检查您的身份验证凭据（API 密钥或用户名/密码）是否具有必要的权限。
* 如果使用带有自定义 CA 的 SSL/TLS，请验证证书路径是否正确且文件可读。
* 查看终端输出中的错误消息。

如果您遇到问题，请随时在 GitHub 仓库中打开一个 issue。

**官方网站：** [https://github.com/elastic/mcp-server-elasticsearch](https://github.com/elastic/mcp-server-elasticsearch)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`
- 标签：`search`, `databases`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @elastic/mcp-server-elasticsearch`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/elastic-elasticsearch.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
