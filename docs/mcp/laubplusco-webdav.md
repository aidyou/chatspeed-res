---
title: "MCP WebDAV 服务"
description: "一种模型上下文协议（MCP）服务器，它使 Claude Desktop 和其他 MCP 客户端能够通过自然语言命令与 WebDAV 文件系统进行 CRUD 操作交互。"
---

# MCP WebDAV 服务

一种模型上下文协议（MCP）服务器，它使 Claude Desktop 和其他 MCP 客户端能够通过自然语言命令与 WebDAV 文件系统进行 CRUD 操作交互。

# WebDAV MCP 服务器

一个模型上下文协议（MCP）服务器，支持通过基本身份验证对WebDAV端点进行CRUD操作。此服务器使Claude Desktop和其他MCP客户端能够通过自然语言命令与WebDAV文件系统交互。

## 功能

- 连接到任意带有可选身份验证的WebDAV服务器
- 对文件和目录执行CRUD操作
- 将文件操作作为MCP资源和工具公开
- 通过stdio传输（用于Claude Desktop集成）或HTTP/SSE传输运行
- 通过可选的基本身份验证实现安全访问
- 支持使用bcrypt加密密码进行MCP服务器身份验证（由于协议限制，WebDAV密码必须是明文）
- 连接池以提高与WebDAV服务器的性能
- 使用Zod进行配置验证
- 结构化日志记录以便更好地进行故障排除

## 前提条件

- Node.js 18 或更高版本
- npm 或 yarn
- WebDAV 服务器（用于实际文件操作）

## 安装

### 选项 1：从npm包安装

```bash
# Global installation
npm install -g webdav-mcp-server

# Or with npx
npx webdav-mcp-server
```

### 选项 2：从源代码克隆并构建

```bash
# Clone repository
git clone https://github.com/yourusername/webdav-mcp-server.git
cd webdav-mcp-server

# Install dependencies
npm install

# Build the application
npm run build
```

### 选项 3：Docker

```bash
# Build the Docker image
docker build -t webdav-mcp-server .

# Run the container without authentication
docker run -p 3000:3000 \
  -e WEBDAV_ROOT_URL=http://your-webdav-server \
  -e WEBDAV_ROOT_PATH=/webdav \
  webdav-mcp-server
  
# Run the container with authentication for both WebDAV and MCP server
docker run -p 3000:3000 \
  -e WEBDAV_ROOT_URL=http://your-webdav-server \
  -e WEBDAV_ROOT_PATH=/webdav \
  -e WEBDAV_AUTH_ENABLED=true \
  -e WEBDAV_USERNAME=admin \
  -e WEBDAV_PASSWORD=password \
  -e AUTH_ENABLED=true \
  -e AUTH_USERNAME=user \
  -e AUTH_PASSWORD=pass \
  webdav-mcp-server
```

## 配置

在根目录下创建一个`.env`文件，并设置以下变量：

```env
# WebDAV configuration
WEBDAV_ROOT_URL=http://localhost:4080
WEBDAV_ROOT_PATH=/webdav

# WebDAV authentication (optional)
WEBDAV_AUTH_ENABLED=true
WEBDAV_USERNAME=admin

# WebDAV password must be plain text (required when auth enabled)
# The WebDAV protocol requires sending the actual password to the server
WEBDAV_PASSWORD=password

# Server configuration (for HTTP mode)
SERVER_PORT=3000

# Authentication configuration for MCP server (optional)
AUTH_ENABLED=true
AUTH_USERNAME=user
AUTH_PASSWORD=pass
AUTH_REALM=MCP WebDAV Server

# Auth password for MCP server can be a bcrypt hash (unlike WebDAV passwords)
# AUTH_PASSWORD={bcrypt}$2y$10$CyLKnUwn9fqqKQFEbxpZFuE9mzWR/x8t6TE7.CgAN0oT8I/5jKJBy
```

### 为MCP服务器认证使用加密密码

为了增强MCP服务器的安全性（而不是WebDAV连接），您可以使用bcrypt加密密码而非明文存储：

1. 生成bcrypt哈希：
```bash
   # 使用内置工具
   npm run generate-hash -- yourpassword
   
   # 或者使用npx
   npx webdav-mcp-generate-hash yourpassword
```

2. 将哈希添加到您的.env文件中，并加上{bcrypt}前缀：
```
   AUTH_PASSWORD={bcrypt}$2y$10$CyLKnUwn9fqqKQFEbxpZFuE9mzWR/x8t6TE7.CgAN0oT8I/5jKJBy
```

这样，您的MCP服务器密码将被安全地存储。请注意，根据协议要求，WebDAV密码必须始终是明文。

## 使用

### 通过stdio传输运行

这种模式非常适合直接与Claude Desktop集成。

```bash
# If installed globally
webdav-mcp-server

# If using npx
npx webdav-mcp-server

# If built from source
node dist/index.js
```

### 通过HTTP/SSE传输运行

这种模式允许服务器通过HTTP与Server-Sent Events实现实时通信。

```bash
# If installed globally
webdav-mcp-server --http

# If using npx
npx webdav-mcp-server --http

# If built from source
node dist/index.js --http
```

## 使用Docker Compose快速启动

开始使用WebDAV服务器和MCP服务器最简单的方法是使用Docker Compose：

```bash
# Start both WebDAV and MCP servers
cd docker
docker-compose up -d

# This will start:
# - hacdias/webdav server on port 4080 (username: admin, password: admin)
# - MCP server on port 3000 (username: user, password: pass)
```

此设置使用[hacdias/webdav](https://github.com/hacdias/webdav)，这是一个用Go编写的简单且独立的WebDAV服务器。WebDAV服务器的配置存储在`webdav_config.yml`中，您可以修改它来调整权限、添加用户或更改其他设置。

WebDAV服务器将所有文件存储在一个名为`webdav_data`的Docker卷中，该卷在容器重启之间保持持久性。

## WebDAV 服务器配置

`webdav_config.yml`文件配置了Docker Compose设置中使用的hacdias/webdav服务器。以下是您可以自定义的内容：

```yaml
# Server address and port
address: 0.0.0.0
port: 6060

# Root data directory
directory: /data

# Enable/disable CORS
cors:
  enabled: true
  # Additional CORS settings...

# Default permissions (C=Create, R=Read, U=Update, D=Delete)
permissions: CRUD

# User definitions
users:
  - username: admin
    password: admin      # Plain text password
    permissions: CRUD    # Full permissions
  
  - username: reader
    password: reader
    permissions: R       # Read-only permissions
    
  # You can also use bcrypt-encrypted passwords
  - username: secure
    password: "{bcrypt}$2y$10$zEP6oofmXFeHaeMfBNLnP.DO8m.H.Mwhd24/TOX2MWLxAExXi4qgi"
```

对于更高级的配置选项，请参阅 [hacdias/webdav 文档](https://github.com/hacdias/webdav)。

## 测试

要运行测试：

```bash
npm test
```

## 与 Claude Desktop 集成

1. 确保在 Claude Desktop 中启用了 MCP 功能

使用 npx
2. 打开 Claude Desktop 设置并点击编辑配置 (`claude_desktop_config.json`)
3. 添加
```json
{
    "mcpServers": {
        "webdav": {
            "command": "npx",
            "args": [
                "-y",
                "webdav-mcp-server"
            ],
            "env": {
                "WEBDAV_ROOT_URL": "",
                "WEBDAV_ROOT_PATH": "",
                "WEBDAV_USERNAME": "",
                "WEBDAV_PASSWORD": "",
                "WEBDAV_AUTH_ENABLED": "true|false"
            }
        }
    }
}
```

使用 node 和本地构建
2. 克隆此仓库并在 mac/linux 上运行 `setup.sh` 或在 windows 上运行 `setup.bat`
3. 打开 Claude Desktop 设置并点击编辑配置 (`claude_desktop_config.json`)
4. 添加
```json
{
    "mcpServers": {
        "webdav": {
            "command": "node",
            "args": [
                "
/dist/index.js"
            ],
            "env": {
                "WEBDAV_ROOT_URL": "",
                "WEBDAV_ROOT_PATH": "",
                "WEBDAV_USERNAME": "",
                "WEBDAV_PASSWORD": "",
                "WEBDAV_AUTH_ENABLED": "true|false"
            }
        }
    }
}
```

## 可用的 MCP 资源

- `webdav://{path}/list` - 列出目录中的文件
- `webdav://{path}/content` - 获取文件内容
- `webdav://{path}/info` - 获取文件或目录信息

## 可用的 MCP 工具

- `webdav_create_remote_file` - 在远程 WebDAV 服务器上创建新文件
- `webdav_get_remote_file` - 从存储在远程 WebDAV 服务器上的文件中检索内容
- `webdav_update_remote_file` - 更新远程 WebDAV 服务器上的现有文件
- `webdav_delete_remote_item` - 从远程 WebDAV 服务器上删除文件或目录
- `webdav_create_remote_directory` - 在远程 WebDAV 服务器上创建新目录
- `webdav_move_remote_item` - 在远程 WebDAV 服务器上移动或重命名文件/目录
- `webdav_copy_remote_item` - 将文件/目录复制到远程 WebDAV 服务器上的新位置
- `webdav_list_remote_directory` - 列出远程 WebDAV 服务器上的文件和目录

## 可用的 MCP 提示

- `webdav_create_remote_file` - 提示在远程WebDAV服务器上创建新文件
- `webdav_get_remote_file` - 提示从远程WebDAV文件中检索内容
- `webdav_update_remote_file` - 提示更新远程WebDAV服务器上的文件
- `webdav_delete_remote_item` - 提示从远程WebDAV服务器上删除文件/目录
- `webdav_list_remote_directory` - 提示列出远程WebDAV服务器上的目录内容
- `webdav_create_remote_directory` - 提示在远程WebDAV服务器上创建目录
- `webdav_move_remote_item` - 提示在远程WebDAV服务器上移动/重命名文件/目录
- `webdav_copy_remote_item` - 提示在远程WebDAV服务器上复制文件/目录

## Claude 中的示例查询

以下是一些可以在Claude Desktop中使用的示例查询，前提是已经连接了WebDAV MCP服务器：

- "列出我的远程WebDAV服务器上的文件"
- "在我的远程WebDAV服务器上创建一个名为notes.txt的新文本文件，内容为：Hello World"
- "从我的远程WebDAV服务器获取document.txt的内容"
- "使用此新配置更新我远程WebDAV服务器上的config.json"
- "在我的远程WebDAV服务器上创建一个名为projects的目录"
- "将report.docx复制到我的远程WebDAV服务器上的备份位置"
- "在我远程WebDAV服务器上将old_name.txt文件移动并重命名为new_name.txt"
- "从我的远程WebDAV服务器上删除temp.txt"

## 程序化使用

您也可以在自己的项目中以编程方式使用此包：

```javascript
import { startWebDAVServer } from 'webdav-mcp-server';

// For stdio transport without authentication
await startWebDAVServer({
  webdavConfig: {
    rootUrl: 'http://your-webdav-server',
    rootPath: '/webdav',
    authEnabled: false
  },
  useHttp: false
});

// For stdio transport with WebDAV authentication (password must be plain text)
await startWebDAVServer({
  webdavConfig: {
    rootUrl: 'http://your-webdav-server',
    rootPath: '/webdav',
    authEnabled: true,
    username: 'admin',
    password: 'password'
  },
  useHttp: false
});

// With bcrypt hash for MCP server password (HTTP auth only)
await startWebDAVServer({
  webdavConfig: {
    rootUrl: 'http://your-webdav-server',
    rootPath: '/webdav',
    authEnabled: true,
    username: 'admin',
    password: 'password' // WebDAV password must be plain text
  },
  useHttp: true,
  httpConfig: {
    port: 3000,
    auth: {
      enabled: true,
      username: 'user',
      password: '{bcrypt}$2y$10$CyLKnUwn9fqqKQFEbxpZFuE9mzWR/x8t6TE7.CgAN0oT8I/5jKJBy'
    }
  }
});

// For HTTP transport with MCP authentication
await startWebDAVServer({
  webdavConfig: {
    rootUrl: 'http://your-webdav-server',
    rootPath: '/webdav',
    authEnabled: true,
    username: 'admin',
    password: 'password'
  },
  useHttp: true,
  httpConfig: {
    port: 3000,
    auth: {
      enabled: true,
      username: 'user',
      password: 'pass',
      realm: 'MCP WebDAV Server'
    }
  }
});

// For HTTP transport without authentication
await startWebDAVServer({
  webdavConfig: {
    rootUrl: 'http://your-webdav-server',
    rootPath: '/webdav',
    authEnabled: false
  },
  useHttp: true,
  httpConfig: {
    port: 3000,
    auth: {
      enabled: false
    }
  }
});
```

## 许可证

MIT

**官方网站：** [https://github.com/laubplusco/mcp-webdav-server](https://github.com/laubplusco/mcp-webdav-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`files`
- 标签：`file systems`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y webdav-mcp-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/laubplusco-webdav.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
