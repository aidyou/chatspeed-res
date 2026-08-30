---
title: "MCP急救医疗规划器"
description: "与Google地图集成，以在紧急情况下定位和评估医疗设施，帮助用户根据医疗需求、紧急程度和设施能力找到合适的医院和诊所。"
---

# MCP急救医疗规划器

与Google地图集成，以在紧急情况下定位和评估医疗设施，帮助用户根据医疗需求、紧急程度和设施能力找到合适的医院和诊所。

# 紧急医疗保险管理 MCP 服务器

[Smithery](https://smithery.ai/server/@manolaz/emergency-medicare-planner-mcp-server)

(@manolaz/emergency-medicare-planner-mcp-server)

这是一个强大的模型上下文协议 (MCP) 服务器，它与 Google 地图集成，用于在紧急情况下定位和评估医疗设施。该服务器帮助用户根据特定的医疗需求、紧急程度和设施能力，在10公里半径内找到合适的医院和诊所。

系统提供实时路线规划、可用性检查以及关于医疗服务的详细信息，帮助患者在紧急医疗情况下做出明智的决定。

**主要功能**：医疗评估的顺序思考 - 根据患者的症状和病史实现逐步临床推理，以更准确地匹配医疗机构。

## 安装与使用

### 通过 Smithery 安装

要自动安装适用于 Claude Desktop 的 Emergency Medicare Planner：

```bash
npx -y @smithery/cli install @manolaz/emergency-medicare-planner-mcp-server --client claude
```

### 手动安装

```bash
# Using npx (recommended)
npx @manolaz/emergency-medicare-planner-mcp-server

# With environment variable for Google Maps API
GOOGLE_MAPS_API_KEY=your_api_key npx @manolaz/emergency-medicare-planner-mcp-server
```

或者全局安装：

```bash
# Install globally
npm install -g @manolaz/emergency-medicare-planner-mcp-server

# Run after global installation
GOOGLE_MAPS_API_KEY=your_api_key emergency-medicare-planner-mcp-server
```

## 组件

### 工具

- **searchMedicalFacilities**
  - 使用 Google Places API 搜索医院、诊所和其他医疗设施
  - 输入：
    - `query` (字符串): 搜索查询（例如，“急诊室”，“儿科诊所”）
    - `location`: 患者位置的纬度和经度
    - `radius` (可选，默认: 10000): 搜索半径（米）
    - `specialtyNeeded` (可选): 需要的医疗专业领域

- **getMedicalFacilityDetails**
  - 获取特定医疗设施的详细信息
  - 输入：
    - `placeId` (字符串): 医疗设施的 Google Place ID
  - 输出：
    - 营业时间、提供的服务、联系信息等

- **calculateRouteToFacility**
  - 计算到达医疗设施的最快路线
  - 输入：
    - `origin`: 患者的当前位置
    - `facilityId`: 目的地设施的 Place ID
    - `transportMode` (可选): 旅行方式（驾车、步行、公共交通、救护车）
    - `avoidTraffic` (可选): 规划避开交通拥堵的路线

- **checkFacilityAvailability**
  - 检查设施是否当前接受患者
  - 输入：
    - `facilityId`: 医疗设施的 Place ID
    - `emergencyLevel`: 医疗情况的紧急程度

## 配置

### 与 Claude Desktop 一起使用

要在 Claude Desktop 应用程序中使用此服务器，请将以下配置添加到您的 `claude_desktop_config.json` 文件的 "mcpServers" 部分：

```json
{
  "mcpServers": {
    "emergency-medicare-planner": {
      "command": "npx",
      "args": ["@manolaz/emergency-medicare-planner-mcp-server"],
      "env": {
        "GOOGLE_MAPS_API_KEY": "your_google_maps_api_key"
      }
    }
  }
}
```

或者，如果您已安装了软件包，可以直接使用 node 命令：

```json
{
  "mcpServers": {
    "emergency-medicare-planner": {
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

- `GOOGLE_MAPS_API_KEY` (必需): 您的 Google Maps API 密钥，需要启用以下 API：
  - Places API
  - Directions API
  - Geocoding API
  - Time Zone API
  - Distance Matrix API

### 测试

```bash
# Run test suite
npm test

# Run with debug logging
DEBUG=emergency-medicare:* npm start
```

## 许可证

此 MCP 服务器根据 MIT 许可证授权。更多详情，请参阅项目仓库中的 LICENSE 文件。

**官方网站：** [https://github.com/manolaz/emergency-medicare-planner-mcp-server](https://github.com/manolaz/emergency-medicare-planner-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`location services`, `search`, `health and wellness`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`@manolaz/emergency-medicare-planner-mcp-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/manolaz-emergency-medicare-planner.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
