---
title: "n8n MCP 服务器"
description: "一个MCP服务器，通过模型上下文协议（Model Context Protocol）实现与n8n工作流、执行和设置的安全交互，专为与大型语言模型（LLMs）集成而设计。"
---

# n8n MCP 服务器

一个MCP服务器，通过模型上下文协议（Model Context Protocol）实现与n8n工作流、执行和设置的安全交互，专为与大型语言模型（LLMs）集成而设计。

# n8n MCP 服务器

通过模型上下文协议（Model Context Protocol）提供对 n8n 工作流、执行、凭证等的访问的 MCP 服务器。这允许大型语言模型（LLMs）以安全和标准化的方式与 n8n 实例交互。

## 安装

### 获取您的 n8n API 密钥

1. 登录到您的 n8n 实例
2. 点击左下角的用户图标
3. 转到设置
4. 选择 API
5. 点击“创建 API 密钥”
6. 复制您的 API 密钥（您将无法再次查看它）

### 安装 MCP 服务器

#### 选项 1：从 npm 安装（推荐）

```bash
npm install -g @illuminaresolutions/n8n-mcp-server
```

#### 选项 2：从源代码安装

1. 克隆仓库：
```bash
   git clone https://github.com/illuminaresolutions/n8n-mcp-server.git
   cd n8n-mcp-server
```

2. 安装依赖并构建：
```bash
   npm install
   npm run build
```

3. 在后台启动服务器：
```bash
   nohup npm start > n8n-mcp.log 2>&1 &
```

   停止服务器：
```bash
   pkill -f "node build/index.js"
```

注意：从 npm 安装时，服务器将在您的 PATH 中作为 `n8n-mcp-server` 可用。

## 配置

### Claude 桌面版

1. 打开您的 Claude 桌面配置文件：
```
   ~/Library/Application Support/Claude/claude_desktop_config.json
```

2. 添加 n8n 配置：
```json
   {
     "mcpServers": {
        "n8n": {
         "command": "n8n-mcp-server",
         "env": {
           "N8N_HOST": "https://your-n8n-instance.com",
           "N8N_API_KEY": "your-api-key-here"
         }
       }
     }
   }
```

### Cline (VS Code)

1. 安装服务器（请参阅上面的安装步骤）
2. 打开 VS Code
3. 从左侧边栏打开 Cline 扩展
4. 单击窗格顶部的 'MCP Servers' 图标
5. 滚动到底部并点击 'Configure MCP Servers'
6. 在打开的设置文件中添加以下内容：
```json
   {
     "mcpServers": {
       "n8n": {
         "command": "n8n-mcp-server",
         "env": {
           "N8N_HOST": "https://your-n8n-instance.com",
           "N8N_API_KEY": "your-api-key-here"
         }
       }
     }
   }
```
7. 保存文件
8. 确保 MCP 开关已启用（绿色）且状态指示器为绿色
9. 开始在 Cline 中使用 MCP 命令

### Sage

即将推出！n8n MCP 服务器将可通过以下途径获得：
- Smithery.ai 市场
- 从 Claude 桌面版导入

目前，请使用 Claude 桌面版或 Cline。

## 验证

配置完成后：

1. 重启您的 LLM 应用程序
2. 询问：“列出我的 n8n 工作流”
3. 您应该能看到列出的工作流

如果出现错误：
- 检查您的 n8n 实例是否正在运行
- 验证您的 API 密钥是否有正确的权限
- 确保 N8N_HOST 没有尾随斜杠

## 功能

### 核心功能
- 列出和管理工作流
- 查看工作流详情
- 执行工作流
- 管理凭证
- 处理标签和执行
- 生成安全审计
- 管理工作流标签

### 企业功能
这些功能需要 n8n 企业许可证：

- 项目管理
- 变量管理
- 高级用户管理

## 故障排除

### 常见问题

1. "客户端未初始化"
   - 检查 N8N_HOST 和 N8N_API_KEY 是否设置正确
   - 确保 n8n 实例可访问
   - 验证 API 密钥权限

2. "需要许可证"
   - 您正在尝试使用企业版功能
   - 请升级到 n8n 企业版或仅使用核心功能

3. 连接问题
   - 确认 n8n 实例正在运行
   - 检查 URL 协议 (http/https)
   - 从 N8N_HOST 中移除尾部斜杠

## 安全最佳实践

1. API 密钥管理
   - 使用最低限度的必要权限
   - 定期轮换密钥
   - 永不将密钥提交到版本控制

2. 实例访问
   - 在生产环境中使用 HTTPS
   - 启用 n8n 身份验证
   - 保持 n8n 更新

## 支持

- [GitHub Issues](https://github.com/illuminaresolutions/n8n-mcp-server/issues)
- [n8n 文档](https://docs.n8n.io)

## 许可证

[MIT 许可证](https://github.com/illuminaresolutions/n8n-mcp-server/blob/HEAD/LICENSE)

**官方网站：** [https://github.com/illuminaresolutions/n8n-mcp-server](https://github.com/illuminaresolutions/n8n-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`, `browser`
- 标签：`developer tools`, `os automation`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`n8n-mcp-server`
- 参数：无

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/illuminaresolutions-n8n.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
