---
title: "OceanBase MCP 服务器"
description: "一个模型上下文协议 (MCP) 服务器，用于实现与 OceanBase 数据库的安全交互。该服务器允许 AI 助手通过受控接口列出表格、读取数据并执行 SQL 查询，从而使数据库的探索和分析更加安全、结构化。"
---

# OceanBase MCP 服务器

一个模型上下文协议 (MCP) 服务器，用于实现与 OceanBase 数据库的安全交互。该服务器允许 AI 助手通过受控接口列出表格、读取数据并执行 SQL 查询，从而使数据库的探索和分析更加安全、结构化。

# OceanBase MCP服务器

一个模型上下文协议（MCP）服务器，用于实现与OceanBase数据库的安全交互。该服务器允许AI助手通过受控接口列出表格、读取数据和执行SQL查询，使数据库探索和分析更安全、更有结构。

## 功能

- 将可用的OceanBase表列为资源
- 读取表格内容
- 执行SQL查询并进行适当的错误处理
- 通过环境变量实现安全的数据库访问
- 全面的日志记录

## 配置

设置以下环境变量：

```bash
OB_HOST=localhost     # 数据库主机
OB_PORT=2881         # 可选：数据库端口（如果未指定，默认为2881）
OB_USER=your_username
OB_PASSWORD=your_password
OB_DATABASE=your_database
```

## 使用

### 与Claude桌面一起使用

将以下内容添加到你的`claude_desktop_config.json`中：

```json
{
  "mcpServers": {
    "oceanbase": {
      "command": "uv",
      "args": [
        "--directory", 
        "path/to/mcp-oceanbase",
        "run",
        "oceanbase_mcp_server"
      ],
      "env": {
        "OB_HOST": "localhost",
        "OB_PORT": "2881",
        "OB_USER": "your_username",
        "OB_PASSWORD": "your_password",
        "OB_DATABASE": "your_database"
      }
    }
  }
}
```

### 作为独立服务器使用

```bash
# 安装依赖
pip install -r requirements.txt

# 运行服务器
python -m oceanbase_mcp_server
```

## 安装与开发

```bash
# 克隆仓库
git clone https://github.com/yourusername/mcp-oceanbase.git
cd mcp-oceanbase

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # 在Windows上使用`venv\Scripts\activate`

# 复制并修改.env
cp .env.template .env

# 安装开发依赖
pip install -r requirements-dev.txt

# 运行测试
pytest
```

## 安全考虑

- 切勿提交环境变量或凭证
- 使用具有最低权限的数据库用户
- 考虑在生产环境中实施查询白名单
- 监控并记录所有数据库操作

## 安全最佳实践

此MCP服务器需要数据库访问才能运行。为了安全：

1. **创建一个专用的OceanBase用户**，赋予最低权限
2. **切勿使用root凭证**或管理账户
3. **限制数据库访问**仅限必要操作
4. **启用日志记录**以用于审计目的
5. **定期进行数据库访问的安全审查**

请参阅OceanBase安全配置指南以获取关于以下方面的详细说明：
- 创建一个受限的OceanBase用户
- 设置适当的权限
- 监控数据库访问
- 安全最佳实践

⚠️ 重要：在配置数据库访问时，始终遵循最低权限原则。

## 许可证

Apache许可证 - 请参阅LICENSE文件了解详细信息。

## 贡献

1. Fork仓库
2. 创建功能分支（`git checkout -b feature/amazing-feature`）
3. 提交更改（`git commit -m 'Add some amazing feature'`）
4. 推送到分支（`git push origin feature/amazing-feature`）
5. 打开一个Pull Request

**官方网站：** [https://github.com/oceanbase/mcp-oceanbase](https://github.com/oceanbase/mcp-oceanbase)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`research and data`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`oceanbase_mcp_server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/oceanbase-oceanbase.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
