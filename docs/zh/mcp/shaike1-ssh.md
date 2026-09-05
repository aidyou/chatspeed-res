---
title: "MCP SSH服务器"
description: "针对模型上下文协议的安全SSH服务器实现， enables远程命令执行和文件操作，同时支持基于密码和密钥的身份验证。"
---

# MCP SSH服务器

针对模型上下文协议的安全SSH服务器实现， enables远程命令执行和文件操作，同时支持基于密码和密钥的身份验证。

# MCP SSH 服务器

一个强大的 SSH 服务器实现，用于模型上下文协议 (MCP)。该服务器通过 SSH 协议启用安全的远程命令执行和文件操作，支持基于密码和密钥的身份验证。

## 特性

- ✨ 安全的 SSH 连接管理
- 🔑 基于密码和密钥的身份验证
- 💻 远程命令执行
- 📁 文件操作（上传/下载）
- 📊 文件传输进度跟踪
- 🔐 权限管理
- 📂 目录操作
- 🚀 批量文件传输
- 📝 详细日志记录

## 安装

1. 安装软件包：
```bash
npm install mcp-ssh
```

2. 添加到你的 Claude 桌面配置 (`claude_desktop_config.json`) 中：
```json
{
  "mcpServers": {
    "ssh": {
      "command": "node",
      "args": ["%APPDATA%/npm/node_modules/mcp-ssh/dist/server.js"],
      "env": {
        "SSH_PORT": "8889",
        "SSH_LOG_LEVEL": "info"
      }
    }
  }
}

```

## 使用方法

### 密码认证
```powershell
$body = @{
    id = "test"
    host = "example.com"
    port = 22
    username = "user"
    password = "pass123"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8889/connect" -Method Post -Body $body -ContentType "application/json"
```

### 密钥认证
```powershell
$body = @{
    id = "test"
    host = "example.com"
    port = 22
    username = "user"
    privateKey = Get-Content ~/.ssh/id_rsa | Out-String
    passphrase = "optional-key-passphrase"  # if your key is protected
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8889/connect" -Method Post -Body $body -ContentType "application/json"
```

### 执行命令
```powershell
$execBody = @{
    id = "test"
    command = "ls -la"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8889/exec" -Method Post -Body $execBody -ContentType "application/json"
```

### 文件操作
```powershell
# Upload file
$uploadForm = @{
    file = Get-Item -Path "localfile.txt"
    remotePath = "/remote/path/file.txt"
}
Invoke-RestMethod -Uri "http://localhost:8889/upload/test" -Method Post -Form $uploadForm

# Download file
Invoke-RestMethod -Uri "http://localhost:8889/download/test?remotePath=/remote/path/file.txt" -Method Get -OutFile "downloaded.txt"
```

### 目录操作
```powershell
# List directory
Invoke-RestMethod -Uri "http://localhost:8889/ls/test?path=/remote/path" -Method Get

# Get connection status
Invoke-RestMethod -Uri "http://localhost:8889/status/test" -Method Get
```

## 开发

1. 克隆仓库：
```bash
git clone https://github.com/shaike1/mcp-server-ssh.git
cd mcp-server-ssh
```

2. 安装依赖项：
```bash
npm install
```

3. 构建：
```bash
npm run build
```

4. 启动服务器：
```bash
npm start
```

## 环境变量

- `SSH_PORT`: 服务器端口（默认：8889）
- `SSH_LOG_LEVEL`: 日志级别（默认：info）

## 贡献

1. 叉分仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 打开拉取请求

## 许可证

MIT

**官方网站：** [https://github.com/shaike1/mcp-server-ssh](https://github.com/shaike1/mcp-server-ssh)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`files`
- 标签：`file systems`, `os automation`, `security and iam`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`%APPDATA%/npm/node_modules/mcp-ssh/dist/server.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/shaike1-ssh.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
