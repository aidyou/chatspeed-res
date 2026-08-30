---
title: "Redis MCP代理服务器"
description: "官方的 Redis MCP 服务器是一种为代理应用程序设计的自然语言接口，用于高效管理和搜索 Redis 中的数据。"
---

# Redis MCP代理服务器

官方的 Redis MCP 服务器是一种为代理应用程序设计的自然语言接口，用于高效管理和搜索 Redis 中的数据。

# Redis MCP 服务器
[Smithery](https://smithery.ai/server/@redis/mcp-redis)

  

## 概述
Redis MCP 服务器是一个**自然语言接口**，旨在为代理应用程序高效管理和搜索 Redis 中的数据。它与**MCP（模型内容协议）客户端**无缝集成，使 AI 驱动的工作流能够与 Redis 中的结构化和非结构化数据进行交互。使用此 MCP 服务器，您可以提出以下问题：

- "将整个对话存储在流中"
- "缓存此项目"
- "存储带有过期时间的会话"
- "索引并搜索此向量"

## 功能
- **自然语言查询**：允许 AI 代理使用自然语言查询和更新 Redis。
- **无缝 MCP 集成**：与任何**MCP 客户端**配合使用，实现顺畅的通信。
- **全面支持 Redis**：处理**哈希、列表、集合、有序集合、流**等。
- **搜索与过滤**：支持在 Redis 中高效检索和搜索数据。
- **可扩展且轻量级**：专为**高性能**数据操作设计。

## 工具

此 MCP 服务器提供了管理存储在 Redis 中的数据的工具。

- `string` 工具用于设置、获取带过期时间的字符串。适用于存储简单的配置值、会话数据或缓存响应。
- `hash` 工具用于在一个键内存储字段-值对。哈希可以存储向量嵌入。适用于表示具有多个属性的对象、用户资料或产品信息，其中可以单独访问字段。
- `list` 工具提供常见的追加和弹出项操作。适用于队列、消息代理或维护最近的操作列表。
- `set` 工具用于添加、移除和列出集合成员。适用于跟踪唯一的值，如用户 ID 或标签，并执行集合操作，如交集。
- `sorted set` 工具用于管理例如排行榜、优先级队列或基于分数排序的时间分析数据。
- `pub/sub` 功能用于向频道发布消息并订阅接收消息。适用于实时通知、聊天应用或向多个客户端分发更新。
- `streams` 工具用于向数据流添加、读取和删除。适用于事件溯源、活动源或传感器数据日志，支持消费者组。
- `JSON` 工具用于在 Redis 中存储、检索和操作 JSON 文档。适用于复杂的嵌套数据结构、文档数据库或路径访问的配置管理。

其他工具。

- `query engine` 工具用于管理向量索引和执行向量搜索
- `server management` 工具用于检索有关数据库的信息

## 安装

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@redis/mcp-redis) 自动安装 Claude Desktop 的 Redis MCP 服务器：

```bash
npx -y @smithery/cli install @redis/mcp-redis --client claude
```

### 手动安装
```sh
# Clone the repository
git clone https://github.com/redis/mcp-redis.git
cd mcp-redis

# Install dependencies using uv
uv venv
source .venv/bin/activate
uv sync
```

## 配置

要配置此 Redis MCP 服务器，请考虑以下环境变量：

| 名称                    | 描述                                               | 默认值 |
|-------------------------|-----------------------------------------------------------|---------------|
| `REDIS_HOST`            | Redis IP 或主机名                                      | `"127.0.0.1"` |
| `REDIS_PORT`            | Redis 端口                                                | `6379`        |
| `REDIS_USERNAME`        | 默认数据库用户名                                 | `"default"`   |
| `REDIS_PWD`             | 默认数据库密码                                 | ""            |
| `REDIS_SSL`             | 启用或禁用 SSL/TLS                               | `False`       |
| `REDIS_CA_PATH`         | 用于验证服务器的 CA 证书                       | None          |
| `REDIS_SSL_KEYFILE`     | 客户端认证的私钥文件                           | None          |
| `REDIS_SSL_CERTFILE`    | 客户端认证的证书文件                           | None          |
| `REDIS_CERT_REQS`       | 客户端是否应验证服务器的证书 | `"required"`  |
| `REDIS_CA_CERTS`        | 受信任的 CA 证书文件路径                  | None          |
| `REDIS_CLUSTER_MODE`    | 启用 Redis 集群模式                                 | `False`       |

## 与 OpenAI Agents SDK 的集成

将此 MCP 服务器与 OpenAI Agents SDK 集成。阅读[文档](https://openai.github.io/openai-agents-python/mcp/)以了解更多关于 SDK 与 MCP 集成的信息。

安装 Python SDK。

```commandline
pip install openai-agents
```

配置 OpenAI 令牌：

```commandline
export OPENAI_API_KEY=""
```

并运行 [应用程序](https://github.com/redis/mcp-redis/blob/HEAD/examples/redis_assistant.py)。

```commandline
python3.13 redis_assistant.py 
```

您可以使用 [OpenAI 控制台](https://platform.openai.com/traces/)来排查您的代理工作流问题。

## 与 Claude 桌面版的集成
您可以配置 Claude 桌面版以使用此 MCP 服务器。

1. 指定您的 Redis 凭据和 TLS 配置
2. 获取您的 `uv` 命令完整路径（例如 `which uv`）
3. 编辑 `claude_desktop_config.json` 配置文件 
   - 在 MacOS 上，位于 `~/Library/Application\ Support/Claude/`

```commandline
{
    "mcpServers": {
        "redis": {
            "command": "",
            "args": [
                "--directory",
                "",
                "run",
                "src/main.py"
            ],
            "env": {
                "REDIS_HOST": "",
                "REDIS_PORT": "",
                "REDIS_PSW": "",
                "REDIS_SSL": True|False,
                "REDIS_CA_PATH": "",
                "REDIS_CLUSTER_MODE": True|False
            }
        }
    }
}
```

您可以通过跟踪日志文件来排查问题。

```commandline
tail -f ~/Library/Logs/Claude/mcp-server-redis.log
```

## 测试

您可以使用 [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector) 对此 MCP 服务器进行可视化调试。

```sh
npx @modelcontextprotocol/inspector uv run src/main.py
```

## 示例用例
- **AI 助手**：使 LLM 能够在 Redis 中获取、存储和处理数据。
- **聊天机器人 & 虚拟代理**：检索会话数据、管理队列以及个性化响应。
- **数据搜索 & 分析**：查询 Redis 以获得**实时洞察和快速查找**。
- **事件处理**：使用 **Redis Streams** 管理事件流。

## 贡献
1. Fork 仓库
2. 创建一个新的分支 (`feature-branch`)
3. 提交您的更改
4. 将更改推送到您的分支并提交 PR！

## 许可证

此项目采用 **MIT 许可证**。

## 联系
如遇问题或需要支持，请通过 [GitHub Issues](https://github.com/redis/mcp-redis/issues) 联系我们。

**官方网站：** [https://github.com/redis/mcp-redis](https://github.com/redis/mcp-redis)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`memory`
- 标签：`databases`, `knowledge and memory`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`docker`
- 参数：`run --rm --name redis-mcp-server -i -e REDIS_HOST=<redis_hostname> -e REDIS_PORT=<redis_port> -e REDIS_USERNAME=<redis_username> -e REDIS_PWD=<redis_password> mcp-redis`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/redis-redis.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
