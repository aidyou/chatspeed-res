---
title: "知识记忆图谱"
description: "该MCP服务器通过利用本地知识图谱来记忆用户在多次交互中的信息，从而为聊天应用提供持久内存集成。"
---

# 知识记忆图谱

该MCP服务器通过利用本地知识图谱来记忆用户在多次交互中的信息，从而为聊天应用提供持久内存集成。

forked [https://github.com/modelcontextprotocol/servers/tree/main](https://github.com/modelcontextprotocol/servers/tree/main)

# 知识图谱内存服务器
这是一个使用本地知识图谱实现的持久化内存的基本示例。这使得Claude能够在多次聊天中记住用户的信息。

## 核心概念

### 实体
实体是知识图谱中的主要节点。每个实体包含：
- 一个唯一的名称（标识符）
- 一个实体类型（例如，“人”、“组织”、“事件”）
- 一系列观察结果

示例：
```json
{
  "name": "John_Smith",
  "entityType": "person",
  "observations": ["Speaks fluent Spanish"]
}
```

### 关系
关系定义了实体之间的有向连接。它们总是以主动语态存储，并描述实体之间如何互动或关联。

示例：
```json
{
  "from": "John_Smith",
  "to": "Anthropic",
  "relationType": "works_at"
}
```

### 观察
观察是对实体的离散信息片段。它们：

- 以字符串形式存储
- 附属于特定的实体
- 可以独立添加或移除
- 应该是原子性的（每个观察一个事实）

示例：
```json
{
  "entityName": "John_Smith",
  "observations": [
    "Speaks fluent Spanish",
    "Graduated in 2019",
    "Prefers morning meetings"
  ]
}
```

## API

### 工具

- **create_entities**
  - 在知识图谱中创建多个新实体
  - 输入: `entities` (对象数组)
    - 每个对象包含:
      - `name` (字符串): 实体标识符
      - `entityType` (字符串): 类型分类
      - `observations` (字符串数组): 关联的观察
  - 忽略已存在名称的实体

- **create_relations**
  - 在实体之间创建多个新的关系
  - 输入: `relations` (对象数组)
    - 每个对象包含:
      - `from` (字符串): 源实体名称
      - `to` (字符串): 目标实体名称
      - `relationType` (字符串): 主动语态的关系类型
  - 跳过重复的关系

- **add_observations**
  - 向现有实体添加新的观察
  - 输入: `observations` (对象数组)
    - 每个对象包含:
      - `entityName` (字符串): 目标实体
      - `contents` (字符串数组): 要添加的新观察
  - 返回每个实体添加的观察
  - 如果实体不存在则失败

- **delete_entities**
  - 删除实体及其关系
  - 输入: `entityNames` (字符串数组)
  - 级联删除相关关系
  - 如果实体不存在则静默操作

- **delete_observations**
  - 从实体中删除特定的观察
  - 输入: `deletions` (对象数组)
    - 每个对象包含:
      - `entityName` (字符串): 目标实体
      - `observations` (字符串数组): 要删除的观察
  - 如果观察不存在则静默操作

- **delete_relations**
  - 从图中删除特定的关系
  - 输入: `relations` (对象数组)
    - 每个对象包含:
      - `from` (字符串): 源实体名称
      - `to` (字符串): 目标实体名称
      - `relationType` (字符串): 关系类型
  - 如果关系不存在则静默操作

- **read_graph**
  - 读取整个知识图谱
  - 不需要输入
  - 返回带有所有实体和关系的完整图结构

- **search_nodes**
  - 基于一个或多个关键词搜索节点
  - 输入: `query` (字符串)
    - 用空格分隔的关键词（例如："budget utility"）
    - 多个关键词被视为OR条件
  - 搜索范围:
    - 实体名称
    - 实体类型
    - 子域
    - 观察内容
  - 匹配行为:
    - 不区分大小写
    - 部分单词匹配
    - 任何关键词可以匹配任何字段
    - 返回与任意关键词匹配的实体
  - 返回匹配的实体及其关系
  - 示例查询:
    - 单个关键词: "budget"
    - 多个关键词: "budget utility"
    - 带特殊字符: "budget & utility"

- **open_nodes**
  - 通过名称检索特定节点
  - 输入: `names` (字符串数组)
  - 返回:
    - 请求的实体
    - 请求实体之间的关系
  - 静默跳过不存在的节点

# 使用 Claude Desktop

### 设置

将以下内容添加到你的 claude_desktop_config.json 文件中:

#### Docker

```json
{
  "mcpServers": {
    "memory": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "mcp/memory"]
    }
  }
}
```

#### NPX
```json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-memory"
      ]
    }
  }
}
```

#### 带自定义设置的 NPX

```json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-memory"
      ],
      "env": {
        "MEMORY_FILE_PATH": "/path/to/custom/memory.json"
      }
    }
  }
}
```

服务器可以通过以下环境变量进行配置：

```json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-memory"
      ],
      "env": {
        "MEMORY_FILE_PATH": "/path/to/custom/memory.json"
      }
    }
  }
}
```

- `MEMORY_FILE_PATH`: 存储内存的 JSON 文件路径（默认：服务器目录下的 `memory.json`）

### 系统提示

使用内存的提示取决于用例。更改提示将有助于模型确定创建记忆的频率和类型。

这是一个用于聊天个性化的示例提示。您可以在 [Claude.ai 项目](https://www.anthropic.com/news/projects) 的“自定义指令”字段中使用此提示。

```
Follow these steps for each interaction:

1. User Identification:
   - You should assume that you are interacting with default_user
   - If you have not identified default_user, proactively try to do so.

2. Memory Retrieval:
   - Always begin your chat by saying only "Remembering..." and retrieve all relevant information from your knowledge graph
   - Always refer to your knowledge graph as your "memory"
   - When searching your memory, you can use multiple keywords to find related information
   - Example searches:
     * Single concept: "programming"
     * Related concepts: "programming python"
     * Specific domain with role: "work engineer"

3. Memory Creation:
   - While conversing with the user, be attentive to any new information that falls into these categories:
     a) Basic Identity (age, gender, location, job title, education level, etc.)
     b) Behaviors (interests, habits, etc.)
     c) Preferences (communication style, preferred language, etc.)
     d) Goals (goals, targets, aspirations, etc.)
     e) Relationships (personal and professional relationships up to 3 degrees of separation)
   - When storing information, use specific and descriptive keywords that will help in future searches

4. Memory Update:
   - If any new information was gathered during the interaction, update your memory as follows:
     a) Create entities for recurring organizations, people, and significant events
     b) Connect them to the current entities using relations
     c) Store facts about them as observations
     d) Use clear and searchable terms in entity names and observations to facilitate future retrieval
```

## 构建

Docker:

```sh
docker build -t mcp/memory -f src/memory/Dockerfile . 
```

## 许可证

该 MCP 服务器根据 MIT 许可证授权。这意味着您可以自由使用、修改和分发该软件，但需遵守 MIT 许可证的条款和条件。有关更多详细信息，请参阅项目仓库中的 LICENSE 文件。

**官方网站：** [https://github.com/yodakeisuke/mcp-memory-domain-knowledge](https://github.com/yodakeisuke/mcp-memory-domain-knowledge)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`memory`
- 标签：`knowledge and memory`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @modelcontextprotocol/server-memory`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/yodakeisuke-memory-domain-knowledge.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
