---
title: "MySQL MCP服务"
description: "通过JSON命令启用与MySQL数据库的交互，支持只读查询、写查询的测试执行以及通过Docker进行的表信息检索。"
---

# MySQL MCP服务

通过JSON命令启用与MySQL数据库的交互，支持只读查询、写查询的测试执行以及通过Docker进行的表信息检索。

# MySQL MCP 服务器

一个用于与 MySQL 数据库交互的 MCP 服务器。

该服务器支持执行只读查询（query）和最终会被回滚的写查询（test_execute）。

  

## 设置

### 环境变量

将以下环境变量添加到 `~/.mcp/.env` 文件中：

```
MYSQL_HOST=host.docker.internal  # Hostname to access host services from Docker container
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=your_password
```

> **注意**：`host.docker.internal` 是一个特殊的 DNS 名称，用于从 Docker 容器访问主机服务。
> 当连接到运行在您主机上的 MySQL 服务器时，请使用此设置。
> 如果连接到其他 MySQL 服务器，请更改为主机名。

### mcp.json 配置

```json
{
  "mcpServers": {
    "mysql": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "--add-host=host.docker.internal:host-gateway",
        "--env-file",
        "/Users/username/.mcp/.env",
        "ghcr.io/xiangma9712/mcp/mysql"
      ]
    }
  }
}
```

## 使用方法

### 启动服务器

```sh
docker run -i --rm --add-host=host.docker.internal:host-gateway --env-file ~/.mcp/.env ghcr.io/xiangma9712/mcp/mysql
```

> **注意**：如果您使用 OrbStack，`host.docker.internal` 会自动支持，因此可以省略 `--add-host` 选项。
> 虽然 Docker Desktop 通常也会自动支持这一点，但为了更好的可靠性，建议添加 `--add-host` 选项。

### 可用命令

#### 1. 执行只读查询

```json
{
  "type": "query",
  "payload": {
    "sql": "SELECT * FROM your_table"
  }
}
```

响应：
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "name": "example"
    }
  ]
}
```

#### 2. 测试查询执行

```json
{
  "type": "test_execute",
  "payload": {
    "sql": "UPDATE your_table SET name = 'updated' WHERE id = 1"
  }
}
```

响应：
```json
{
  "success": true,
  "data": "The UPDATE SQL query can be executed."
}
```

#### 3. 列出表

```json
{
  "type": "list_tables"
}
```

响应：
```json
{
  "success": true,
  "data": ["table1", "table2", "table3"]
}
```

#### 4. 描述表

```json
{
  "type": "describe_table",
  "payload": {
    "table": "your_table"
  }
}
```

响应：
```json
{
  "success": true,
  "data": [
    {
      "Field": "id",
      "Type": "int(11)",
      "Null": "NO",
      "Key": "PRI",
      "Default": null,
      "Extra": ""
    },
    {
      "Field": "name",
      "Type": "varchar(255)",
      "Null": "YES",
      "Key": "",
      "Default": null,
      "Extra": ""
    }
  ]
}
```

## 实现细节

- 用 TypeScript 实现
- 使用 mysql2 包
- 作为 Docker 容器运行
- 通过标准输入接收 JSON 命令
- 通过标准输出返回 JSON 响应
- 使用 `host.docker.internal` 连接到主机 MySQL（兼容 OrbStack 和 Docker Desktop）

## 安全注意事项

- 使用环境变量管理敏感信息
- SQL 注入预防是实施者的责任
- 生产环境中需要正确的网络配置
- 连接到主机服务时需要适当的防火墙设置

**官方网站：** [https://github.com/xiangma9712/mysql-mcp-server](https://github.com/xiangma9712/mysql-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`databases`, `developer tools`, `virtualization`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`docker`
- 参数：`run -i --rm --add-host=host.docker.internal:host-gateway --env-file /Users/username/.mcp/.env ghcr.io/xiangma9712/mcp/mysql`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/xiangma9712-mysql.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
