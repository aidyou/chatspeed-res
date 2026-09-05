---
title: "Neo4j连接器"
description: "该服务器启用了Neo4j数据库和Claude Desktop之间的交互，允许用户执行Cypher查询、创建节点以及在数据库中建立关系。"
---

# Neo4j连接器

该服务器启用了Neo4j数据库和Claude Desktop之间的交互，允许用户执行Cypher查询、创建节点以及在数据库中建立关系。

# MCP Neo4j 服务器
[Smithery](https://smithery.ai/server/@alanse/mcp-neo4j-server)

一个MCP服务器，提供Neo4j图形数据库与Claude桌面之间的集成，通过自然语言交互实现图形数据库操作。

## 快速开始

你可以直接使用npx运行此MCP服务器：

```bash
npx @alanse/mcp-neo4j
```

或者将其添加到你的Claude桌面配置中：

```json
{
  "mcpServers": {
    "neo4j": {
      "command": "npx",
      "args": ["@alanse/mcp-neo4j-server"],
      "env": {
        "NEO4J_URI": "bolt://localhost:7687",
        "NEO4J_USERNAME": "neo4j",
        "NEO4J_PASSWORD": "your-password"
      }
    }
  }
}
```

## 功能

该服务器提供了与Neo4j数据库交互的工具：

### 工具

- `execute_query`：在Neo4j数据库上执行Cypher查询
  - 支持所有类型的Cypher查询（读取、创建、更新、删除）
  - 以结构化格式返回查询结果
  - 可传递参数以防止注入攻击

- `create_node`：在图形数据库中创建新节点
  - 指定节点标签和属性
  - 返回带有内部ID的创建节点
  - 支持所有Neo4j数据类型作为属性

- `create_relationship`：在两个现有节点之间创建关系
  - 定义关系类型和方向
  - 向关系添加属性
  - 需要源节点和目标节点的ID

## 安装

### 通过Smithery安装

要通过[Smithery](https://smithery.ai/server/@alanse/mcp-neo4j-server)自动为Claude桌面安装MCP Neo4j服务器：

```bash
npx -y @smithery/cli install @alanse/mcp-neo4j-server --client claude
```

### 开发环境

1. 克隆仓库：
```bash
git clone https://github.com/da-okazaki/mcp-neo4j-server.git
cd mcp-neo4j-server
```

2. 安装依赖项：
```bash
npm install
```

3. 构建项目：
```bash
npm run build
```

## 配置

服务器需要以下环境变量：

- `NEO4J_URI`：Neo4j数据库URI（默认：bolt://localhost:7687）
- `NEO4J_USERNAME`：Neo4j用户名（默认：neo4j）
- `NEO4J_PASSWORD`：Neo4j密码（必需）

## 使用示例

这里是如何使用自然语言与Neo4j数据库进行交互的一些例子：

### 查询数据

你可以问这样的问题：
- "显示销售部门的所有员工"
- "找到最老的前5名客户"
- "谁在过去一个月内购买了超过3种产品？"

示例：
```
User: "Show me all employees in the Sales department"

Claude: Let me query the database for Sales department employees.

[Executes query internally: MATCH (e:Employee)-[:WORKS_IN]->(d:Department {name: 'Sales'}) RETURN e.name, e.position]

Result:
- John Smith (Sales Manager)
- Sarah Johnson (Sales Representative)
- Mike Brown (Account Executive)
```

### 创建数据

你可以给出这样的指示：
- "添加一个名叫John Doe的新人员，年龄30岁"
- "创建一个名为'Premium Coffee'的产品，价格$24.99"
- "添加一个名为'研究与发展'的新部门"

示例：
```
User: "Add a new person named John Doe who is 30 years old"

Claude: I'll create a new Person node with the provided information.

[Creates node internally with label 'Person' and properties {name: 'John Doe', age: 30}]

Result: Created new person node with ID: 123
```

### 创建关系

你可以请求这样的关系：
- "让John Doe成为Jane Smith的朋友"
- "将产品A设置为产品B的组成部分"
- "指派John Doe到销售部门"

示例：
```
User: "Make John Doe friends with Jane Smith"

Claude: I'll create a friendship relationship between these two people.

[Creates relationship internally: MATCH (a:Person {name: 'John Doe'}), (b:Person {name: 'Jane Smith'})
CREATE (a)-[:FRIENDS_WITH {since: '2024-01-05'}]->(b)]

Result: Created friendship relationship between John Doe and Jane Smith
```

### 复杂操作

你可以用自然语言执行更复杂的操作：
- "找到居住在纽约的客户所购买的所有产品"
- "显示John Doe朋友的朋友"
- "计算每个部门员工的平均年龄"

示例：
```
User: "Find all products purchased by customers who live in New York"

Claude: I'll query the database for this information.

[Executes query internally:
MATCH (c:Customer {city: 'New York'})-[:PURCHASED]->(p:Product)
RETURN c.name, collect(p.name) as products]

Result:
- Alice Wilson: [Premium Coffee, Tea Set, Cookies]
- Bob Miller: [Premium Coffee, Water Bottle]
```

## 测试

运行测试套件：

```bash
npm test
```

## 许可证

MIT

**官方网站：** [https://github.com/da-okazaki/mcp-neo4j-server](https://github.com/da-okazaki/mcp-neo4j-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`, `development`
- 标签：`databases`, `developer tools`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`@alanse/mcp-neo4j-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/da-okazaki-neo4j.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
