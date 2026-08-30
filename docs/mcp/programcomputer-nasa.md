---
title: "NASA-MCP服务器"
description: "一种模型上下文协议服务器，为人工智能模型提供标准化接口，以与NASA的大量数据源进行交互，包括每日天文图片（APOD）、火星漫游车照片、卫星图像和太空天气数据。"
---

# NASA-MCP服务器

一种模型上下文协议服务器，为人工智能模型提供标准化接口，以与NASA的大量数据源进行交互，包括每日天文图片（APOD）、火星漫游车照片、卫星图像和太空天气数据。

# NASA MCP 服务器

这是一个为NASA API设计的模型上下文协议（MCP）服务器，提供了标准化接口以便AI模型能够与NASA庞大的数据源进行交互。该服务器实现了官方的模型上下文协议规范。

特别感谢MCP社区的支持和指导！

## 特性

* 通过单一、一致的接口访问20多个NASA数据源
* 针对AI消费优化的标准数据格式
* 自动参数验证和错误处理
* NASA API密钥的速率限制管理
* 全面的文档和示例
* 支持多种NASA图像格式
* 为LLM兼容性进行的数据转换和格式化
* 跨平台支持（Windows, macOS, Linux）

## 免责声明

**此项目与美国国家航空航天局（NASA）或其子公司及其附属机构无关，也未得到它们的认可或关联。** 这是一个独立实现，用于访问NASA公开可用的API。所使用的全部NASA数据都是公开可获取的，并受NASA数据使用政策约束。

## 安装

### 使用 npx 运行

```bash
env NASA_API_KEY=YOUR_API_KEY npx -y @programcomputer/nasa-mcp-server
```

您也可以将API密钥作为命令行参数传递：

```bash
npx -y @programcomputer/nasa-mcp-server --nasa-api-key=YOUR_API_KEY
```

### 使用 SuperGateway 实现服务器发送事件 (SSE)

您可以使用[SuperGateway](https://github.com/supercorp-ai/supergateway)来实现服务器发送事件(SSE)。

**NASA-MCP-server 的开发者不推荐 SuperGateway 仓库。提供此信息是为了让那些希望自行决定实现SSE功能的人参考。**

### 手动安装

```bash
# Clone the repository
git clone https://github.com/ProgramComputer/NASA-MCP-server.git

# Install dependencies
cd NASA-MCP-server
npm install

# Run with your API key
NASA_API_KEY=YOUR_API_KEY npm start
```

### 在 Cursor 上运行

配置 Cursor 🖥️ 注意：需要Cursor版本0.45.6+。

要在Cursor中配置NASA MCP Server:

在您的Cursor配置目录中创建或编辑一个 `mcp.json` 文件，内容如下：

```json
{
  "mcpServers": {
    "nasa-mcp": {
      "command": "npx",
      "args": ["-y", "@programcomputer/nasa-mcp-server"],
      "env": {
        "NASA_API_KEY": "your-api-key"
      }
    }
  }
}
```

将 `your-api-key` 替换为您从 [https://api.nasa.gov/](https://api.nasa.gov/) 获取的NASA API密钥。

添加配置后，重启Cursor以查看新的NASA工具。作曲家代理将在适当的情况下自动使用NASA MCP处理与空间相关的查询。

## 环境变量

可以通过以下环境变量配置服务器：

| 变量 | 描述 | 默认值 |
|----------|-------------|---------|
| `NASA_API_KEY` | 您的NASA API密钥（在 api.nasa.gov 获取） | `DEMO_KEY`（有限使用） |
| `PORT` | 服务器运行端口 | `3000` |
| `LOG_LEVEL` | 日志级别（debug, info, warn, error） | `info` |
| `CACHE_DURATION` | 缓存时长（秒） | `3600`（1小时） |
| `RATE_LIMIT` | 每小时最大请求数 | 根据API密钥 |

## 包含的NASA API

此MCP服务器集成了以下NASA API：

1. **NASA 开放 API** (api.nasa.gov):
   - APOD（每日天文图片）
   - EPIC（地球多色成像相机）
   - DONKI（空间天气通知、知识和信息数据库）
   - Insight（火星天气服务）
   - 火星探测车照片
   - NEO（近地天体网络服务）
   - EONET（地球观测自然事件追踪器）
   - TLE（两行轨道数据）
   - NASA 图像和视频库
   - 系外行星档案
   - NASA 声音 API（测试版）
   - POWER（全球能源资源预测）

2. **JPL 太阳系动力学 API** (ssd-api.jpl.nasa.gov):
   - SBDB（小天体数据库）
   - SBDB 近距离接近数据
   - 火流星数据
   - Scout API

3. **地球数据 API**:
   - GIBS（全球图像浏览服务）
   - CMR（通用元数据存储库）- 增强了高级搜索功能
   - EPIC（地球多色成像相机）
   - FIRMS（资源管理系统火灾信息）

## API 方法

每个 NASA API 都通过标准化的 MCP 方法公开：

### APOD（每日天文图片）

```json
{
  "method": "nasa/apod",
  "params": {
    "date": "2023-01-01", // Optional: YYYY-MM-DD format
    "count": 5, // Optional: Return a specified number of random images
    "thumbs": true // Optional: Return URL of video thumbnail
  }
}
```

### 火星探测车照片

```json
{
  "method": "nasa/mars-rover",
  "params": {
    "rover": "curiosity", // Required: "curiosity", "opportunity", or "spirit"
    "sol": 1000, // Either sol or earth_date is required
    "earth_date": "2023-01-01", // YYYY-MM-DD format
    "camera": "FHAZ" // Optional: Filter by camera type
  }
}
```

### 近地天体

```json
{
  "method": "nasa/neo",
  "params": {
    "start_date": "2023-01-01", // Required: YYYY-MM-DD format
    "end_date": "2023-01-07" // Required: YYYY-MM-DD format (max 7 days from start)
  }
}
```

### GIBS（全球图像浏览服务）

```json
{
  "method": "nasa/gibs",
  "params": {
    "layer": "MODIS_Terra_CorrectedReflectance_TrueColor", // Required: Layer ID
    "date": "2023-01-01", // Required: YYYY-MM-DD format
    "format": "png" // Optional: "png" or "jpg"
  }
}
```

### POWER（全球能源资源预测）

```json
{
  "method": "nasa/power",
  "params": {
    "parameters": "T2M,PRECTOTCORR,WS10M", // Required: Comma-separated list
    "community": "re", // Required: Community identifier
    "latitude": 40.7128, // Required: Latitude
    "longitude": -74.0060, // Required: Longitude
    "start": "20220101", // Required: Start date (YYYYMMDD)
    "end": "20220107" // Required: End date (YYYYMMDD)
  }
}
```

有关所有可用方法和参数的完整文档，请参阅 `/docs` 目录中的 API 参考。

## 日志系统

服务器包括全面的日志记录：

* 操作状态和进度
* 性能指标
* 速率限制跟踪
* 错误条件
* 请求验证

示例日志消息：

```
[INFO] NASA MCP Server initialized successfully
[INFO] Processing APOD request for date: 2023-01-01
[INFO] Fetching Mars Rover data for Curiosity, sol 1000
[WARNING] Rate limit threshold reached (80%)
[ERROR] Invalid parameter: 'date' must be in YYYY-MM-DD format
```

## 安全考虑

此 MCP 服务器遵循 Model Context Protocol 规范，实施了最佳安全实践：

* 使用 Zod 模式进行输入验证和清理
* 不执行任意代码
* 防止命令注入
* 正确处理错误以防止信息泄露
* 对 API 请求进行速率限制和超时控制
* 没有可以在会话间被利用的持久状态

## 开发

```bash
# Clone the repository
git clone https://github.com/ProgramComputer/NASA-MCP-server.git

# Install dependencies
npm install

# Copy the example environment file and update with your API keys
cp .env.example .env

# Build the TypeScript code
npm run build

# Start the development server
npm run dev

# Run tests
npm test
```

## 使用 MCP Inspector 测试

NASA MCP 服务器包含一个脚本，帮助您使用 MCP Inspector 测试 API：

```bash
# Run the provided test script
./scripts/test-with-inspector.sh
```

这将：
1. 构建项目以确保包含最新更改
2. 启动运行 NASA MCP 服务器的 MCP Inspector
3. 允许您交互式测试所有 NASA API

### 示例测试请求

仓库中包含了每个 API 的示例测试请求，您可以将其复制并粘贴到 MCP Inspector 中：

```bash
# View the example test requests
cat docs/inspector-test-examples.md
```

有关详细示例，请参阅 [Inspector 测试示例](https://github.com/programcomputer/nasa-mcp-server/blob/HEAD/docs/inspector-test-examples.md) 文档。

## MCP 客户端使用

此服务器遵循官方 Model Context Protocol。以下是如何使用 MCP SDK 的示例：

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { HttpClientTransport } from "@modelcontextprotocol/sdk/client/http.js";

const transport = new HttpClientTransport({
  url: "http://localhost:3000",
});

const client = new Client({
  name: "mcp-client",
  version: "1.0.0",
});

await client.connect(transport);

// Example: Get today's Astronomy Picture of the Day
const apodResult = await client.request({
  method: "nasa/apod", 
  params: {}
});

// Example: Get Mars Rover photos
const marsRoverResult = await client.request({
  method: "nasa/mars-rover",
  params: { rover: "curiosity", sol: 1000 }
});

// Example: Search for Near Earth Objects
const neoResults = await client.request({
  method: "nasa/neo",
  params: {
    start_date: '2023-01-01',
    end_date: '2023-01-07'
  }
});

// Example: Get satellite imagery from GIBS
const satelliteImage = await client.request({
  method: "nasa/gibs",
  params: {
    layer: 'MODIS_Terra_CorrectedReflectance_TrueColor',
    date: '2023-01-01'
  }
});

// Example: Use the new POWER API
const powerData = await client.request({
  method: "nasa/power",
  params: {
    parameters: "T2M,PRECTOTCORR,WS10M",
    community: "re",
    latitude: 40.7128,
    longitude: -74.0060,
    start: "20220101",
    end: "20220107"
  }
});
```

## 贡献

1. 分叉仓库
2. 创建您的功能分支
3. 运行测试：`npm test`
4. 提交拉取请求

## 许可证

ISC 许可证 - 详情请参阅 LICENSE 文件

**官方网站：** [https://github.com/programcomputer/nasa-mcp-server](https://github.com/programcomputer/nasa-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`research and data`, `search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @programcomputer/nasa-mcp-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/programcomputer-nasa.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
