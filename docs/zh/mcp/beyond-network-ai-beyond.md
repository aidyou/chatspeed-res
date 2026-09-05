---
title: "超越社交金融模型服务器"
description: "一个可扩展的模型上下文协议服务器，为AI模型提供对社交平台数据（目前是Farcaster）和区块链数据的标准访问。"
---

# 超越社交金融模型服务器

一个可扩展的模型上下文协议服务器，为AI模型提供对社交平台数据（目前是Farcaster）和区块链数据的标准访问。

# Beyond MCP Server

一个可扩展的模型上下文协议服务器，提供对社交平台数据和链上数据的标准化访问。目前支持通过Neynar API访问Farcaster，并为Twitter集成预留了位置。很快将增加更多平台的支持，如Telegram及其链上数据。

## 功能特点

- **MCP合规**：完全实现模型上下文协议规范
- **多平台支持**：设计用于支持多个社交媒体平台
- **可扩展性**：易于添加新的平台提供商
- **格式良好**：针对大语言模型消费优化了上下文格式
- **灵活传输**：支持标准输入输出以及SSE/HTTP传输方式

## 支持的平台

- **Farcaster**：通过Neynar API完整实现
- **Twitter**：占位符（未实现）

## 开始使用

### 前提条件

- Node.js 16+
- Neynar API密钥（用于访问Farcaster）[https://neynar.com/](https://neynar.com/)

### 安装步骤

1. 克隆仓库
```bash
git clone https://github.com/yourusername/beyond-mcp-server.git
cd beyond-mcp-server
```

2. 安装依赖项
```bash
npm install
```

3. 从模板创建.env文件
```bash
cp .env.example .env
# Edit .env with your API keys
```

4. 配置你的环境变量
   - **必需**：在你的.env文件中设置`NEYNAR_API_KEY`
   - 你可以从[https://neynar.com/](https://neynar.com/)获取Neynar API密钥
   - 没有有效的API密钥，Farcaster功能将无法工作

5. 构建并启动服务器
```bash
npm run build
npm start  # For stdio mode (default)
# OR
npm run start:http  # For HTTP/SSE mode
```

## 与Claude桌面版一起使用

1. 构建服务器
```bash
npm run build
```

2. 确保你的.env文件正确配置了你的API密钥
   - 服务器将在以下位置查找.env文件：
     - 当前工作目录
     - 项目根目录
     - 上级目录（最多向上追溯3层）
   - 你也可以直接在系统中设置环境变量

3. 在Claude Desktop配置中添加服务器：
* macOS: ~/Library/Application Support/Claude/claude_desktop_config.json
* Windows: %APPDATA%\Claude\claude_desktop_config.json
  

```json
{
  "mcpServers": {
    "beyond-social": {
      "command": "/usr/local/bin/node",
      "args": [
        "/full/path/to/beyond-mcp-server/dist/index.js",
        "--stdio"
      ]
    }
  }
}
```

4. 或者，你可以直接在Claude Desktop配置中传递API密钥和其他环境变量（**推荐**）：

```json
{
  "mcpServers": {
    "beyond-social": {
      "command": "/usr/local/bin/node",
      "args": [
        "/full/path/to/beyond-mcp-server/dist/index.js",
        "--stdio"
      ],
      "env": {
        "NEYNAR_API_KEY": "YOUR_API_KEY_HERE",
        "ENABLE_FARCASTER": "true",
        "ENABLE_TWITTER": "false"
      }
    }
  }
}
```

5. 重启Claude桌面版

## MCP能力

### 资源

* `social://{platform}/{query}/search` - 在平台上搜索内容
* `social://{platform}/user/{userId}/profile` - 获取用户资料
* `social://{platform}/wallet/{walletAddress}/profile` - 通过钱包地址获取用户资料（仅限 Farcaster）
* `social://{platform}/user/{userId}/balance` - 获取用户的钱包余额（仅限 Farcaster）
  - 接受 FID（数字）或用户名
  - 如果提供的是用户名，则在获取余额前自动转换为 FID
* `social://{platform}/wallet/{walletAddress}/profile` - 通过钱包地址获取用户资料
* `social://{platform}/user/{userId}/content` - 获取用户内容
* `social://{platform}/thread/{threadId}` - 获取对话线程
* `social://{platform}/trending` - 获取热门话题
* `social://{platform}/trending-feed` - 获取支持多提供商的热门动态内容（仅限 Farcaster）
  - 支持的提供商：neynar（默认）、openrank、mbd
  - 参数：timeWindow (1h, 6h, 12h, 24h, 7d, 30d), limit

### 工具

* `search-content` - 在社交平台上搜索内容
* `get-user-profile` - 获取用户的个人资料信息
* `get-user-profile-by-wallet` - 通过钱包地址获取用户资料（仅限 Farcaster）
* `get-user-balance` - 获取用户的钱包余额（仅限 Farcaster）
  - 接受 FID（数字）或用户名
  - 自动处理从用户名到 FID 的转换
* `get-user-content` - 获取特定用户的内容
* `get-thread` - 获取对话线程
* `get-trending-topics` - 获取当前热门话题
* `getTrendingFeed` - 获取支持多提供商的热门动态内容（仅限 Farcaster）
* `get-wallet-profile` - 根据钱包地址获取并分析用户资料

### 提示

* `analyze-thread` - 分析社交媒体线程
* `summarize-user-activity` - 概述用户的活动
* `explore-trending-topics` - 探索平台上的热门话题
* `analyze-search-results` - 分析查询的搜索结果
* `explore-trending-feed` - 跨不同提供商分析热门动态内容
* `get-wallet-profile` - 通过钱包地址获取并分析用户资料
* `check-user-balance` - 分析用户的钱包余额和持有情况
  - 支持 FID 和用户名输入
  - 自动处理用户名到 FID 的解析

## 扩展新提供商

要添加一个新的社交平台提供商：

1. 在 `src/providers/` 中创建一个新目录
2. 实现 `ContentProvider` 接口
3. 在注册表中注册提供商

示例：

```typescript
import { ContentProvider } from '../interfaces/provider';

export class MyPlatformProvider implements ContentProvider {
  public name = 'myplatform';
  public platform = 'myplatform';
  
  // Implement all required methods
}
```

## 开发

### 以开发模式运行

```bash
npm run dev        # stdio mode
npm run dev:http   # HTTP mode
```

### 测试

```bash
npm test
```

### 代码检查

```bash
npm run lint
npm run lint:fix
```

## 许可证

MIT

## 贡献

欢迎贡献！请随时提交 Pull Request。

## 更新日志

   所有对该项目的重要更改都将在此文件中记录。
   
   ### [1.0.0] - 2025年3月10日
   
   #### 新增
   - 初始发布
   - 通过 Neynar API 集成 Farcaster
   - MCP 兼容的服务器实现
   - 支持 stdio 和 HTTP 模式

   ### [1.0.1] - 2025年3月19日

   #### 新增
   - 添加了新工具和资源，用于通过钱包地址获取用户资料
   - 添加了新的测试
     
   ### [1.0.2] - 2025-3-21
   
   #### 新增
   - 增加了通过ID或用户名检索Farcaster用户钱包余额的功能
   - 实现了趋势内容的多提供商支持
   - 通过增加额外的用户详情增强了updateUserProfile功能
   - 添加了全面的测试以确保可靠性和性能
     
   
请注意，日期格式已经根据中文习惯进行了调整（从"2025-Mar-21"改为"2025-3-21"），如果你希望保持原样，请告知我。

**官方网站：** [https://github.com/beyond-network-ai/beyond-mcp-server](https://github.com/beyond-network-ai/beyond-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`finance`
- 标签：`social media`, `finance`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`/usr/local/bin/node`
- 参数：`/full/path/to/beyond-mcp-server/dist/index.js --stdio`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/beyond-network-ai-beyond.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
