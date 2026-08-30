---
title: "Microsoft SQL Server 桥接服务"
description: "一个易于使用的桥梁，让像 Claude 和 Cursor IDE 这样的 AI 助手能够直接查询和探索 Microsoft SQL Server 数据库。无需编码经验！"
---

# Microsoft SQL Server 桥接服务

一个易于使用的桥梁，让像 Claude 和 Cursor IDE 这样的 AI 助手能够直接查询和探索 Microsoft SQL Server 数据库。无需编码经验！

# MS SQL MCP Server 1.1

一个易于使用的桥梁，让像 Claude 这样的 AI 助手可以直接查询和探索 Microsoft SQL Server 数据库。无需编码经验！

## 这个工具能做什么？

这个工具允许 AI 助手：
1. **发现**您 SQL Server 数据库中的表
2. **查看**表结构（列、数据类型等）
3. **执行**安全的只读 SQL 查询
4. **生成**从自然语言请求转换而来的 SQL 查询

## 🌟 为什么你需要这个工具

### 桥接数据与 AI 之间的鸿沟
- **无需编码**：无需编写复杂的集成代码，直接让 Claude 和其他 AI 助手访问您的 SQL Server 数据库
- **保持控制**：所有查询默认为只读，确保您的数据安全
- **私有且安全**：数据库凭据保持本地存储，永远不会发送到外部服务

### 实用优势
- **节省数小时的手动工作**：不再需要复制粘贴数据或查询结果以与 AI 共享
- **深入分析**：AI 可以浏览您的整个数据库模式，并提供跨多个表的见解
- **自然语言界面**：用简单的英语询问关于数据的问题
- **解决上下文限制问题**：访问超过常规 AI 上下文窗口的大数据集

### 适合人群
- **数据分析师**：希望在不共享凭证的情况下获得 AI 帮助解释 SQL 数据
- **开发者**：寻找通过自然对话快速探索数据库结构的方法
- **业务分析师**：不需要 SQL 专业知识即可获得洞察
- **数据库管理员**：希望向 AI 工具提供受控访问

## 🚀 快速入门指南

### 第一步：安装先决条件
- 安装 [Node.js](https://nodejs.org/)（版本 14 或更高）
- 访问 Microsoft SQL Server 数据库（本地或 Azure）

### 第二步：克隆并设置
```bash
# Clone this repository
git clone https://github.com/dperussina/mssql-mcp-server.git

# Navigate to the project directory
cd mssql-mcp-server

# Install dependencies
npm install

# Copy the example environment file
cp .env.example .env
```

### 第三步：配置数据库连接
编辑 `.env` 文件，填写您的数据库凭据：
```
DB_USER=your_username
DB_PASSWORD=your_password
DB_SERVER=your_server_name_or_ip
DB_DATABASE=your_database_name
PORT=3333
TRANSPORT=stdio
SERVER_URL=http://localhost:3333
DEBUG=false                     # Set to 'true' for detailed logging (helpful for troubleshooting)
QUERY_RESULTS_PATH=/path/to/query_results  # Directory where query results will be saved as JSON files
```

### 第四步：启动服务器
```bash
# Start with default stdio transport
npm start

# OR start with HTTP/SSE transport for network access
npm run start:sse
```

### 第五步：试用！
```bash
# Run the interactive client
npm run client
```

## 📊 示例用例

请根据实际需求替换 `#0`, `#1`, `#2`, `#3` 中的内容。

1. **无需编写SQL即可探索数据库结构**
```javascript
   mcp_SQL_mcp_discover_database()
```

2. **获取特定表的详细信息**
```javascript
   mcp_SQL_mcp_table_details({ tableName: "Customers" })
```

3. **运行安全查询**
```javascript
   mcp_SQL_mcp_execute_query({ sql: "SELECT TOP 10 * FROM Customers", returnResults: true })
```

4. **按名称模式查找表**
```javascript
   mcp_SQL_mcp_discover_tables({ namePattern: "%user%" })
```

5. **使用分页导航大型结果集**
```javascript
   // 第一页
   mcp_SQL_mcp_execute_query({ 
     sql: "SELECT * FROM Users ORDER BY Username OFFSET 0 ROWS FETCH NEXT 10 ROWS ONLY", 
     returnResults: true 
   })
   
   // 下一页
   mcp_SQL_mcp_execute_query({ 
     sql: "SELECT * FROM Users ORDER BY Username OFFSET 10 ROWS FETCH NEXT 10 ROWS ONLY", 
     returnResults: true 
   })
```

6. **基于游标的分页以获得最佳性能**
```javascript
   // 第一页
   mcp_SQL_mcp_execute_query({ 
     sql: "SELECT TOP 10 * FROM Users ORDER BY Username", 
     returnResults: true 
   })
   
   // 使用最后一个值作为游标获取下一页
   mcp_SQL_mcp_execute_query({ 
     sql: "SELECT TOP 10 * FROM Users WHERE Username > 'last_username' ORDER BY Username", 
     returnResults: true 
   })
```

7. **提出自然语言问题**
```
   "显示上个月订单最多的前5位客户"
```

## 💡 实际应用

### 商业智能
- **销售业绩分析**："显示过去一年的月度销售趋势，并按地区识别表现最好的产品。"
- **客户细分**："根据购买频率、平均订单价值和地理位置分析我们的客户基础。"
- **财务报告**："创建季度损益报告，比较今年与去年的数据。"

### 数据库管理
- **架构优化**："通过检查查询性能数据帮助我识别缺少索引的表。"
- **数据质量审核**："查找所有信息不完整或值无效的客户记录。"
- **使用情况分析**："显示哪些表被最频繁访问以及哪些查询资源消耗最大。"

### 开发
- **API探索**："我正在构建一个API - 帮助我分析数据库架构以设计合适的端点。"
- **查询优化**："审查这个复杂的查询并建议性能改进。"
- **数据库文档**："创建我们数据库结构的全面文档，解释关系。"

## 🖥️ 交互式客户端功能

捆绑的客户端提供了一个易于使用的菜单驱动界面：

1. **列出可用资源** - 查看可获取的信息
2. **列出可用工具** - 查看可以执行的操作
3. **执行 SQL 查询** - 运行只读的 SQL 查询
4. **获取表详情** - 查看任意表的结构
5. **读取数据库模式** - 查看所有表及其关系
6. **生成 SQL 查询** - 将自然语言转换为 SQL

## 🧠 有效的提示与工具使用指南

在通过此 MCP 服务器与 Claude 或其他 AI 助手合作时，您请求的方式对结果有很大影响。以下是如何帮助 AI 有效使用数据库工具的方法：

### 基本工具调用格式

当提示 AI 使用此工具时，请遵循以下结构：

```
Can you use the SQL MCP tools to [your goal]?

For example:
- Check what tables exist in my database
- Query the Customers table and show me the first 10 records
- Find all orders from the past month
```

### 必要的命令和语法

以下是主要工具及其正确的语法：

```javascript
// Discover the database structure
mcp_SQL_mcp_discover_database()

// Get detailed information about a specific table
mcp_SQL_mcp_table_details({ tableName: "YourTableName" })

// Execute a query and return results
mcp_SQL_mcp_execute_query({ 
  sql: "SELECT * FROM YourTable WHERE Condition", 
  returnResults: true 
})

// Find tables by name pattern
mcp_SQL_mcp_discover_tables({ namePattern: "%pattern%" })

// Access saved query results (for large result sets)
mcp_SQL_mcp_get_query_results({ uuid: "provided-uuid-here" })
```

**何时使用每个工具：**
- **数据库发现**：当 AI 不熟悉您的数据库结构时，首先使用此工具。
- **表详情**：在编写查询之前，专注于特定表时使用。
- **查询执行**：当需要检索或分析实际数据时使用。
- **按模式发现表**：当查找与特定领域相关的表时使用。

### 有效的提示模式

#### 分步工作流程
对于复杂的任务，指导 AI 按照一系列步骤进行：

```
I'd like to analyze our sales data. Please:
1. First use mcp_SQL_mcp_discover_tables to find tables related to sales
2. Use mcp_SQL_mcp_table_details to examine the structure of relevant tables
3. Create a query with mcp_SQL_mcp_execute_query that shows monthly sales by product category
```

#### 先结构后查询
```
First, discover what tables exist in my database. Then, look at the structure
of the Customers table. Finally, show me the top 10 customers by total purchase amount.
```

#### 请求解释
```
Query the top 5 underperforming products based on sales vs. forecasts,
and explain your approach to writing this query.
```

### SQL Server 方言注意事项

提醒 AI 关于 SQL Server 的特定语法：

```
Please use SQL Server syntax for pagination:
- For offset/fetch: "OFFSET 10 ROWS FETCH NEXT 10 ROWS ONLY"
- For cursor-based: "WHERE ID > last_id ORDER BY ID"
```

### 纠正工具使用

如果 AI 使用了错误的语法，您可以这样帮助它：

```
That's not quite right. Please use this format for the tool call:
mcp_SQL_mcp_execute_query({ 
  sql: "SELECT * FROM Customers WHERE Region = 'West'",
  returnResults: true
})
```

### 通过提示排除故障

如果 AI 在处理数据库任务时遇到困难，可以尝试以下方法：

1. **更具体地说明表信息**：“在编写该查询之前，请检查 CustomerOrders 表是否存在以及它有哪些列。”

2. **将复杂任务分解为步骤**：“让我们一步一步来。首先，查看 Products 表的结构。然后，检查 Orders 表……”

3. **请求中间结果**：“先在这个表上运行一个简单的查询，以便我们在尝试更复杂的分析之前验证数据格式。”

4. **请求查询解释**：“编写完这个查询后，请解释每一部分的作用，以便我确认它是否符合我的需求。”

## 🔎 高级查询功能

### 表发现与探索

MCP 服务器提供了强大的工具来探索您的数据库结构：

- **基于模式的表发现**：查找匹配特定模式的表
```javascript
  mcp_SQL_mcp_discover_tables({ namePattern: "%order%" })
```

- **模式概览**：按模式获取表的高级视图
```javascript
  mcp_SQL_mcp_execute_query({ 
    sql: "SELECT TABLE_SCHEMA, COUNT(*) AS TableCount FROM INFORMATION_SCHEMA.TABLES GROUP BY TABLE_SCHEMA" 
  })
```

- **列探索**：检查任何表的列元数据
```javascript
  mcp_SQL_mcp_table_details({ tableName: "dbo.Users" })
```

### 分页技术

服务器支持多种分页方法来处理大数据集：

1. **偏移/获取分页**：使用 OFFSET 和 FETCH 的标准 SQL 分页
```javascript
   mcp_SQL_mcp_execute_query({ 
     sql: "SELECT * FROM Users ORDER BY Username OFFSET 0 ROWS FETCH NEXT 10 ROWS ONLY" 
   })
```

2. **基于游标的分页**：对于大数据集更高效
```javascript
   // 获取第一页
   mcp_SQL_mcp_execute_query({ 
     sql: "SELECT TOP 10 * FROM Users ORDER BY Username" 
   })
   
   // 使用最后一个值作为游标获取下一页
   mcp_SQL_mcp_execute_query({ 
     sql: "SELECT TOP 10 * FROM Users WHERE Username > 'last_username' ORDER BY Username" 
   })
```

3. **带数据计数**：在分页数据旁边检索总数
```javascript
   mcp_SQL_mcp_execute_query({ 
     sql: "WITH TotalCount AS (SELECT COUNT(*) AS Total FROM Users) SELECT TOP 10 u.*, t.Total FROM Users u CROSS JOIN TotalCount t ORDER BY Username" 
   })
```

### 复杂连接与关系

通过连接操作探索表之间的关系：

```javascript
mcp_SQL_mcp_execute_query({ 
  sql: "SELECT u.Username, u.Email, r.RoleName FROM Users u JOIN UserRoles ur ON u.Username = ur.Username JOIN Roles r ON ur.RoleId = r.RoleId ORDER BY u.Username"
})
```

### 分析查询

运行聚合和分析查询以获得洞察：

```javascript
mcp_SQL_mcp_execute_query({ 
  sql: "SELECT UserType, COUNT(*) AS UserCount, SUM(CASE WHEN IsActive = 1 THEN 1 ELSE 0 END) AS ActiveUsers FROM Users GROUP BY UserType"
})
```

### 使用 SQL Server 特性

MCP 服务器支持特定于 SQL Server 的特性：

- **公用表表达式 (CTEs)**
- **窗口函数**
- **JSON 操作**
- **层次查询**
- **全文搜索**（当在数据库中配置时）

## 🔗 集成选项

### Claude Desktop 集成

按照以下简单步骤将此工具直接连接到 Claude Desktop：

1. 从 [anthropic.com](https://www.anthropic.com/) 安装 Claude Desktop
2. 编辑 Claude 的配置文件：
   - 位置：`~/Library/Application Support/Claude/claude_desktop_config.json`
   - 添加此配置：

```json
{
    "mcpServers": {
        "mssql": {
            "command": "node",
            "args": [
                "/FULL/PATH/TO/mssql-mcp-server/server.mjs"
            ]
        }
    }
}
```
3. 将 `/FULL/PATH/TO/` 替换为你克隆此仓库的实际路径
4. 重启 Claude Desktop
5. 在 Claude Desktop 中查找工具图标 - 现在你可以直接使用数据库命令了！

### 通过 Cursor IDE 连接

Cursor 是一个由 AI 支持的代码编辑器，可以利用此工具进行高级数据库交互。以下是设置方法：

#### 在 Cursor 中设置

1. 打开 Cursor IDE（如果还没有，请从 [cursor.sh](https://cursor.sh) 下载）
2. 使用 HTTP/SSE 传输启动 MS SQL MCP 服务器：
```bash
   npm run start:sse
```
3. 在 Cursor 中创建一个新的工作区或打开现有项目
4. 进入 Cursor 设置
5. 点击 MCP
6. 添加新的 MCP 服务器
7. 命名你的 MCP 服务器，选择类型：sse
8. 输入服务器 URL 为：localhost:3333/sse（或你正在使用的端口）

#### 在 Cursor 中使用数据库命令

一旦连接成功，您就可以直接在 Cursor 的 AI 聊天中使用 MCP 命令：

1. 让 Cursor 中的 Claude 探索您的数据库：
```
   Can you show me the tables in my database?
```

2. 执行特定查询：
```
   Query the top 10 records from the Customers table
```

3. 生成并运行复杂的查询：
```
   Find all orders from the last month with a value over $1000
```

#### 解决 Cursor 连接问题

- 确保 MS SQL MCP 服务器正在使用 HTTP/SSE 传输方式运行
- 检查端口是否正确，并与 .env 文件中的设置匹配
- 确保防火墙没有阻止连接
- 如果使用不同的 IP/主机名，请在 .env 文件中更新 SERVER_URL

## 🔄 传输方法说明

### 选项 1：stdio 传输（默认）
最适合：直接与 Claude Desktop 或捆绑客户端一起使用
```bash
npm start
```

### 选项 2：HTTP/SSE 传输
最适合：网络访问或与 Web 应用程序一起使用
```bash
npm run start:sse
```

## 🛡️ 安全特性

- **默认为只读**：无数据修改风险
- **私有凭据**：数据库连接详情保存在 `.env` 文件中
- **SQL 注入保护**：内置 SQL 查询验证

## 🔎 新用户故障排除

### "无法连接到数据库"
- 检查 `.env` 文件中的数据库凭据是否正确
- 确保 SQL Server 正在运行并接受连接
- 对于 Azure SQL，验证您的 IP 是否被允许通过防火墙设置

### "模块未找到" 错误
- 再次运行 `npm install` 以确保所有依赖项已安装
- 确保您使用的是 Node.js 版本 14 或更高版本

### "传输错误" 或 "连接被拒绝"
- 对于 HTTP/SSE 传输，验证 .env 中的 PORT 是否可用
- 确保没有防火墙阻止连接

### Claude Desktop 无法连接
- 仔细检查 `claude_desktop_config.json` 中的路径
- 确保您使用的是绝对路径而不是相对路径
- 在更改后完全重启 Claude Desktop

## 📚 了解 SQL Server 基础

如果您是 SQL Server 的新手，这里有一些关键概念：

- **表**：以行和列的形式存储数据
- **架构**：逻辑上对表进行分组（类似文件夹）
- **查询**：用于检索或分析数据的命令
- **视图**：预定义的查询，便于快速访问

这个工具帮助您探索所有这些内容，而无需成为 SQL 专家！

## 🏗️ 架构与核心模块

MS SQL MCP 服务器采用模块化架构构建，以分离关注点，提高可维护性和可扩展性：

### 核心模块

#### `database.mjs` - 数据库连接
- 管理 SQL Server 连接池
- 提供带有重试逻辑和错误处理的查询执行
- 处理数据库连接、事务和配置
- 包括用于清理 SQL 和格式化错误的实用工具

#### `tools.mjs` - 工具注册

- 将所有数据库工具注册到MCP服务器
- 实现工具验证和参数检查
- 为SQL查询、表探索和数据库发现提供核心功能
- 将工具调用映射到数据库操作

#### `resources.mjs` - 数据库资源
- 通过资源端点公开数据库元数据
- 提供模式信息、表列表和过程文档
- 格式化数据库结构信息以便AI使用
- 包含用于数据库探索的发现工具

#### `pagination.mjs` - 结果导航
- 为大型结果集实现基于游标的分页
- 提供生成下一页/上一页游标的实用工具
- 转换SQL查询以支持分页
- 处理SQL Server的OFFSET/FETCH分页语法

#### `errors.mjs` - 错误处理
- 定义不同失败场景下的自定义错误类型
- 实现JSON-RPC错误格式化
- 提供人类可读的错误消息
- 包含全局错误处理中间件

#### `logger.mjs` - 日志系统
- 使用多个传输配置Winston日志记录
- 提供上下文感知的请求日志记录
- 处理日志轮转和格式化
- 捕获未捕获的异常和未处理的拒绝

### 这些模块如何协同工作

1. 当收到工具调用时，MCP服务器将其路由到`tools.mjs`中的适当处理程序
2. 工具处理程序验证参数并构建数据库查询
3. 查询通过`database.mjs`中的函数执行，并可能从`pagination.mjs`中进行分页
4. 结果被格式化并返回给客户端
5. 任何错误都被捕获并通过`errors.mjs`处理
6. 所有操作都通过`logger.mjs`记录

这种架构确保了：
- 清晰的责任分离
- 一致的错误处理
- 全面的日志记录
- 高效的数据库连接管理
- 可扩展的查询执行

## ⚙️ 环境配置说明

`.env`文件控制MS SQL MCP服务器如何连接到您的数据库并运行。以下是每个设置的详细说明：

```
# Database Connection Settings
DB_USER=your_username           # SQL Server username
DB_PASSWORD=your_password       # SQL Server password
DB_SERVER=your_server_name      # Server hostname or IP address (example: localhost, 10.0.0.1, myserver.database.windows.net)
DB_DATABASE=your_database_name  # Name of the database to connect to

# Server Configuration
PORT=3333                       # Port for the HTTP/SSE server to listen on
TRANSPORT=stdio                 # Connection method: 'stdio' (for Claude Desktop) or 'sse' (for network connections)
SERVER_URL=http://localhost:3333 # Base URL when using SSE transport (must match your PORT setting)

# Advanced Settings
DEBUG=false                     # Set to 'true' for detailed logging (helpful for troubleshooting)
QUERY_RESULTS_PATH=/path/to/query_results  # Directory where query results will be saved as JSON files
```

### 连接类型说明

#### stdio传输
- 在直接与Claude Desktop连接时使用
- 通信通过标准输入/输出流进行
- 在`.env`文件中设置`TRANSPORT=stdio`
- 使用`npm start`运行

#### HTTP/SSE传输
- 在通过网络连接（如Cursor IDE）时使用
- 使用Server-Sent Events (SSE)进行实时通信
- 在`.env`文件中设置`TRANSPORT=sse`
- 配置`SERVER_URL`以匹配您的服务器地址
- 使用`npm run start:sse`运行

### SQL Server连接示例

#### 本地SQL Server
```
DB_USER=sa
DB_PASSWORD=YourStrongPassword
DB_SERVER=localhost
DB_DATABASE=AdventureWorks
```

#### Azure SQL数据库
```
DB_USER=azure_admin@myserver
DB_PASSWORD=YourStrongPassword
DB_SERVER=myserver.database.windows.net
DB_DATABASE=AdventureWorks
```

### 查询结果存储

查询结果作为JSON文件保存在`QUERY_RESULTS_PATH`指定的目录中。这可以防止大型结果集压垮对话。您可以：

- 留空以使用项目中的默认 `query-results` 目录
- 设置自定义路径，如 `/Users/username/Documents/query-results`
- 使用工具响应中提供的 UUID 访问保存的结果

## 📝 许可证

ISC

**官方网站：** [https://github.com/dperussina/mssql-mcp-server](https://github.com/dperussina/mssql-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`databases`, `developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`/FULL/PATH/TO/mssql-mcp-server/server.mjs`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/dperussina-mssql.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
