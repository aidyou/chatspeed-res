---
title: "旅行规划器 MCP 服务端"
description: "通过与Google Maps和旅行规划服务交互，使大型语言模型能够执行与旅行相关的任务，包括地点搜索、地点详情和旅行时间计算。"
---

# 旅行规划器 MCP 服务端

通过与Google Maps和旅行规划服务交互，使大型语言模型能够执行与旅行相关的任务，包括地点搜索、地点详情和旅行时间计算。

# 旅行规划 MCP 服务器 (@gongrzhe/server-travelplanner-mcp)
[Smithery](https://smithery.ai/server/@GongRzhe/TRAVEL-PLANNER-MCP-Server)

这是一个用于与 Google 地图和旅行规划服务交互的旅行规划模型上下文协议 (MCP) 服务器实现。该服务器使 LLM 能够执行与旅行相关的任务，如地点搜索、地点详情查询和旅行时间计算。

  

## 安装与使用
### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@GongRzhe/TRAVEL-PLANNER-MCP-Server) 自动为 Claude Desktop 安装旅行规划器：

```bash
npx -y @smithery/cli install @GongRzhe/TRAVEL-PLANNER-MCP-Server --client claude
```

### 手动安装
```bash
# Using npx (recommended)
npx @gongrzhe/server-travelplanner-mcp

# With environment variable for Google Maps API
GOOGLE_MAPS_API_KEY=your_api_key npx @gongrzhe/server-travelplanner-mcp
```

或者全局安装：

```bash
# Install globally
npm install -g @gongrzhe/server-travelplanner-mcp

# Run after global installation
GOOGLE_MAPS_API_KEY=your_api_key @gongrzhe/server-travelplanner-mcp
```

## 组件

### 工具

- **searchPlaces**
  - 使用 Google Places API 搜索地点
  - 输入：
    - `query` (字符串): 地点搜索查询
    - `location` (可选): 用于偏置结果的纬度和经度
    - `radius` (可选): 搜索半径（米）

- **getPlaceDetails**
  - 获取特定地点的详细信息
  - 输入：
    - `placeId` (字符串): 用于检索详情的 Google Place ID

- **calculateRoute**
  - 计算两个地点之间的路线
  - 输入：
    - `origin` (字符串): 出发地
    - `destination` (字符串): 目的地
    - `mode` (可选): 旅行模式（驾车、步行、骑自行车、公共交通）

- **getTimeZone**
  - 获取地点的时区信息
  - 输入：
    - `location`: 纬度和经度坐标
    - `timestamp` (可选): 用于时区计算的时间戳

## 配置

### 与 Claude Desktop 一起使用

要将此服务器与 Claude Desktop 应用程序一起使用，请在您的 `claude_desktop_config.json` 文件的 "mcpServers" 部分添加以下配置：

```json
{
  "mcpServers": {
    "travel-planner": {
      "command": "npx",
      "args": ["@gongrzhe/server-travelplanner-mcp"],
      "env": {
        "GOOGLE_MAPS_API_KEY": "your_google_maps_api_key"
      }
    }
  }
}
```

或者，如果您已安装了包，可以直接使用节点命令：

```json
{
  "mcpServers": {
    "travel-planner": {
      "command": "node",
      "args": ["path/to/dist/index.js"],
      "env": {
        "GOOGLE_MAPS_API_KEY": "your_google_maps_api_key"
      }
    }
  }
}
```

## 开发

### 从源代码构建

1. 克隆仓库
2. 安装依赖项：
```bash
   npm install
```
3. 构建项目：
```bash
   npm run build
```

### 环境变量

- `GOOGLE_MAPS_API_KEY` (必需): 您的 Google 地图 API 密钥，并启用以下 API：
  - Places API
  - Directions API
  - Geocoding API
  - Time Zone API

## 许可证

此 MCP 服务器采用 MIT 许可证。有关更多详细信息，请参阅项目存储库中的 LICENSE 文件。

**官方网站：** [https://github.com/GongRzhe/TRAVEL-PLANNER-MCP-Server](https://github.com/GongRzhe/TRAVEL-PLANNER-MCP-Server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`travel and transportation`, `location services`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`@gongrzhe/server-travelplanner-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/gongrzhe-travel-planner.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
