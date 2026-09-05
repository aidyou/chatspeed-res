---
title: "MCP工具包服务器"
description: "一种模型上下文协议服务器，为LLM代理提供一套完整的工具集，用于IP地理定位、网络诊断、系统监控、加密操作和二维码生成。"
---

# MCP工具包服务器

一种模型上下文协议服务器，为LLM代理提供一套完整的工具集，用于IP地理定位、网络诊断、系统监控、加密操作和二维码生成。

# toolkit-mcp-server

[![TypeScript](/mcp-assets/338d54970219d624fd3e1e2ec6136758.svg)](https://www.typescriptlang.org/)
[![Model Context Protocol](/mcp-assets/87f72c275fb39706595cd53d5a0896ca.svg)](https://modelcontextprotocol.io/)
[![Version](/mcp-assets/9493ca65d9ece12eec9cbb73eb0990da.svg)]()
[![License](/mcp-assets/fa73b4786cfc281bb30f39f895ada091.svg)](https://opensource.org/licenses/Apache-2.0)
[![Status](/mcp-assets/9a22554be918edafcc71c8bd0058366d.svg)]()
[![GitHub](/mcp-assets/0df68bdbd906a344cad37ec4949bb502.svg)](https://github.com/cyanheads/toolkit-mcp-server)

一个提供系统工具和功能的 Model Context Protocol 服务器，包括 IP 地理定位、网络诊断、系统监控、加密操作和二维码生成等功能。

## Model Context Protocol

Model Context Protocol (MCP) 支持以下实体之间的通信：

- **客户端**：Claude Desktop、IDE 和其他 MCP 兼容的客户端
- **服务器**：用于任务管理和自动化的工具和资源
- **LLM 代理**：利用服务器功能的 AI 模型

## 目录

- [特性](#features)
- [安装](#installation)
- [配置](#configuration)
- [工具](#tools)
- [贡献](#contributing)
- [许可](#license)

## 特性

### 网络与地理定位
- 带智能缓存的 IP 地理定位
- 网络连接测试
- Ping 和 Traceroute 工具
- 公共 IP 检测
- 请求速率限制（每分钟 45 次请求）

### 系统工具
- 获取系统信息
- 资源监控
- 负载平均跟踪
- 网络接口详情

### 安全工具
- 加密哈希生成（MD5, SHA-1, SHA-256, SHA-512）
- 常数时间哈希比较
- UUID 生成

### 生成器工具
- 二维码生成
  - 终端输出
  - SVG 格式
  - Base64 编码图像

## 安装

```bash
# Using npm (recommended)
npm install @cyanheads/toolkit-mcp-server

# Or install from source
git clone git@github.com:cyanheads/toolkit-mcp-server.git
cd toolkit-mcp-server
npm install
npm run build
```

## 配置

将以下内容添加到您的 MCP 客户端设置中：

```json
{
  "mcpServers": {
    "toolkit": {
      "command": "node",
      "args": ["node_modules/@cyanheads/toolkit-mcp-server/build/index.js"],
      "env": {
        "NODE_ENV": "production"
      }
    }
  }
}
```

## 工具

### 网络操作
```typescript
// Get geolocation data
const geo = await mcp.use('toolkit-mcp-server', 'geolocate', {
  query: '8.8.8.8'
});

// Check connectivity
const conn = await mcp.use('toolkit-mcp-server', 'checkConnectivity', {
  host: 'example.com',
  port: 443
});
```

### 系统操作
```typescript
// Get system information
const sysInfo = await mcp.use('toolkit-mcp-server', 'getSystemInfo', {});

// Get load average
const load = await mcp.use('toolkit-mcp-server', 'getLoadAverage', {});
```

### 安全操作
```typescript
// Generate hash
const hash = await mcp.use('toolkit-mcp-server', 'hashData', {
  input: 'test data',
  algorithm: 'sha256'
});

// Generate UUID
const uuid = await mcp.use('toolkit-mcp-server', 'generateUUID', {});
```

### 生成器操作
```typescript
// Generate QR code
const qr = await mcp.use('toolkit-mcp-server', 'generateQRCode', {
  data: 'https://example.com',
  type: 'svg'
});
```

## 贡献

1. 叉分仓库
2. 创建你的功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交你的更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 打开一个 Pull Request

## 许可

Apache License 2.0。有关更多信息，请参阅 [LICENSE](https://github.com/cyanheads/toolkit-mcp-server/blob/HEAD/LICENSE)。

---

使用 Model Context Protocol 构建

**官方网站：** [https://github.com/cyanheads/toolkit-mcp-server](https://github.com/cyanheads/toolkit-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`location services`, `monitoring`, `security and iam`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`node_modules/@cyanheads/toolkit-mcp-server/build/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/cyanheads-toolkit.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
