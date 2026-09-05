---
title: "多平台商品搜索"
description: "一个服务器，它通过BigGo的价格比较API，实现跨多个电子商务平台搜索产品、追踪价格历史以及比较产品规格的功能。"
---

# 多平台商品搜索

一个服务器，它通过BigGo的价格比较API，实现跨多个电子商务平台搜索产品、追踪价格历史以及比较产品规格的功能。

# BigGo MCP Server
![PyPI - Python Version](/mcp-assets/258e22dc90f89c4f02fa44bf71fd6b43.svg)
[![PyPI - Version](/mcp-assets/06285530e460209b944272ca02a84852.svg)](https://pypi.org/project/BigGo-MCP-Server/)
![PyPI - License](/mcp-assets/eb08a39e4af3626c2d0c50dd4a992374.svg)

## 介绍
BigGo MCP Server 利用了来自专业比价网站 BigGo 的 API。

## 特性
> 支持 `stdio` 和 `SSE` 传输

- **产品发现**：在多个电子商务平台（如 Amazon、Aliexpress、Ebay、淘宝、Shopee 等）上搜索产品。
- **价格历史追踪**：通过提供产品 URL 或相关术语来追踪产品价格历史。
- **规格比较 [从 v0.1.28 及以上版本禁用]**：根据产品的规格进行比较，从基本信息到更复杂的技术规格。

## 安装
### 前提条件
1. Python >= 3.10
2. [uvx 包管理器 (随 uv 一起提供)](https://docs.astral.sh/uv/getting-started/installation/)
3. 用于规格搜索的 BigGo 认证 (`client_id` 和 `client_secret`)。

#### 如何获取 BigGo 认证？
  - 如果你还没有 BigGo 账户，请[注册](https://account.biggo.com/?url=https%3A%2F%2Fbiggo.com%2F&lang=en&source=web&type=biggo3&method=register)一个。
  - 前往 [BigGo 认证页面](https://account.biggo.com/setting/token)
  - 点击“生成认证”按钮
  - 
  - 复制 `client_id` 和 `client_secret`
  - 将它们用于 MCP 服务器配置中 (`BIGGO_MCP_SERVER_CLIENT_ID` 和 `BIGGO_MCP_SERVER_CLIENT_SECRET`)

### 安装配置
```json
{
  "mcpServers": {
    "biggo-mcp-server": {
      "command": "uvx",
      "args": [ "BigGo-MCP-Server@latest"],
      "env": {
        "BIGGO_MCP_SERVER_CLIENT_ID": "CLIENT_ID",
        "BIGGO_MCP_SERVER_CLIENT_SECRET": "CLIENT_SECRET",
        "BIGGO_MCP_SERVER_REGION": "REGION"
      }
    }
  }
}
```
> 对于特定版本使用 `BigGo-MCP-Server@VERSION`，例如：`BigGo-MCP-Server@0.1.1`

## 环境变量
| 变量                         | 描述               | 默认值 | 选项                                    |
| -------------------------------- | ------------------------- | ------- | ------------------------------------------ |
| `BIGGO_MCP_SERVER_CLIENT_ID`     | 客户端 ID                 | 无    | 规格搜索必需                              |
| `BIGGO_MCP_SERVER_CLIENT_SECRET` | 客户端密钥             | 无    | 规格搜索必需                              |
| `BIGGO_MCP_SERVER_REGION`        | 产品搜索区域       | TW      | US, TW, JP, HK, SG, MY, IN, PH, TH, VN, ID |
| `BIGGO_MCP_SERVER_SSE_PORT`      | SSE 服务器端口       | 9876    | 任何可用端口号                            |
| `BIGGO_MCP_SERVER_SERVER_TYPE`   | 服务器传输类型     | stdio   | stdio, sse                                 |

> 默认 SSE URL: http://localhost:9876/sse

## 可用工具

- `product_search`: 使用 BigGo 搜索 API 进行产品搜索
- `price_history_graph`: 可视化产品价格历史的链接
- `price_history_with_history_id`: 使用产品搜索结果中的历史 ID
- `price_history_with_url`: 通过产品 URL 跟踪价格历史
- `spec_indexes`: 列出可用于产品规格的 Elasticsearch 索引
- `spec_mapping`: 显示带有示例文档的 Elasticsearch 索引映射
- `spec_search`: 从 Elasticsearch 查询产品规格
- `get_current_region`: 获取当前区域

## 常见问题解答
### 如何触发工具使用？
对于**产品发现**相关的：
```
Look for Nike running shoes
```
对于**价格历史跟踪**相关的：
```
Show me the price history of this product: https://some-product-url
```
对于**规格比较**相关的：
```
Find me phones with 16GB RAM and 1TB storage
```
```
Please show me diving watches that can withstand the most water pressure
```

## 构建
更多详情请参阅 [build.md](https://github.com/funmula-corp/biggo-mcp-server/blob/HEAD/docs/build.md)。

## 许可证
本项目采用 MIT 许可证。详情请参阅 [LICENSE](https://github.com/funmula-corp/biggo-mcp-server/blob/HEAD/LICENSE) 文件。

**官方网站：** [https://github.com/funmula-corp/biggo-mcp-server](https://github.com/funmula-corp/biggo-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`
- 标签：`ecommerce and retail`, `search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`BigGo-MCP-Server@latest`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/funmula-corp-biggo.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
