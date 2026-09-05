---
title: "NPS国家公园信息助手"
description: "通过NPS API提供关于美国国家公园的实时信息，使用户能够搜索公园、查看详细信息、警报、游客中心、露营地和即将举行的活动。"
---

# NPS国家公园信息助手

通过NPS API提供关于美国国家公园的实时信息，使用户能够搜索公园、查看详细信息、警报、游客中心、露营地和即将举行的活动。

# 国家公园 MCP 服务器
[Smithery](https://smithery.ai/server/@KyrieTangSheng/mcp-server-nationalparks)

为国家公园服务 (NPS) API 提供的 MCP 服务器，提供关于美国国家公园的实时信息，包括公园详情、警报和活动。

## 工具

```markdown
# 国家公园 MCP 服务器


为国家公园服务 (NPS) API 提供的 MCP 服务器，提供关于美国国家公园的实时信息，包括公园详情、警报和活动。

## 工具
```

1. `findParks`
   - Search for national parks based on various criteria
   - Inputs:
     - `stateCode` (optional string): Filter parks by state code (e.g., "CA" for California). Multiple states can be comma-separated (e.g., "CA,OR,WA")
     - `q` (optional string): Search term to filter parks by name or description
     - `limit` (optional number): Maximum number of parks to return (default: 10, max: 50)
     - `start` (optional number): Start position for results (useful for pagination)
     - `activities` (optional string): Filter by available activities (e.g., "hiking,camping")
   - Returns: Matching parks with detailed information

2. `getParkDetails`
   - Get comprehensive information about a specific national park
   - Inputs:
     - `parkCode` (string): The park code of the national park (e.g., "yose" for Yosemite, "grca" for Grand Canyon)
   - Returns: Detailed park information including descriptions, hours, fees, contacts, and activities

3. `getAlerts`
   - Get current alerts for national parks including closures, hazards, and important information
   - Inputs:
     - `parkCode` (optional string): Filter alerts by park code (e.g., "yose" for Yosemite). Multiple parks can be comma-separated (e.g., "yose,grca")
     - `limit` (optional number): Maximum number of alerts to return (default: 10, max: 50)
     - `start` (optional number): Start position for results (useful for pagination)
     - `q` (optional string): Search term to filter alerts by title or description
   - Returns: Current alerts organized by park

4. `getVisitorCenters`
   - Get information about visitor centers and their operating hours
   - Inputs:
     - `parkCode` (optional string): Filter visitor centers by park code (e.g., "yose" for Yosemite). Multiple parks can be comma-separated (e.g., "yose,grca")
     - `limit` (optional number): Maximum number of visitor centers to return (default: 10, max: 50)
     - `start` (optional number): Start position for results (useful for pagination)
     - `q` (optional string): Search term to filter visitor centers by name or description
   - Returns: Visitor center information including location, hours, and contact details

5. `getCampgrounds`
   - Get information about available campgrounds and their amenities
   - Inputs:
     - `parkCode` (optional string): Filter campgrounds by park code (e.g., "yose" for Yosemite). Multiple parks can be comma-separated (e.g., "yose,grca")
     - `limit` (optional number): Maximum number of campgrounds to return (default: 10, max: 50)
     - `start` (optional number): Start position for results (useful for pagination)
     - `q` (optional string): Search term to filter campgrounds by name or description
   - Returns: Campground information including amenities, fees, and reservation details

6. `getEvents`
   - Find upcoming events at parks
   - Inputs:
     - `parkCode` (optional string): Filter events by park code (e.g., "yose" for Yosemite). Multiple parks can be comma-separated (e.g., "yose,grca")
     - `limit` (optional number): Maximum number of events to return (default: 10, max: 50)
     - `start` (optional number): Start position for results (useful for pagination)
     - `dateStart` (optional string): Start date for filtering events (format: YYYY-MM-DD)
     - `dateEnd` (optional string): End date for filtering events (format: YYYY-MM-DD)
     - `q` (optional string): Search term to filter events by title or description
   - Returns: Event information including dates, times, and descriptions

## 设置

### 通过 Smithery 安装

通过 [Smithery](https://smithery.ai/server/@KyrieTangSheng/mcp-server-nationalparks) 自动安装 mcp-server-nationalparks 到 Claude 桌面版：

```bash
npx -y @smithery/cli install @KyrieTangSheng/mcp-server-nationalparks --client claude
```

### NPS API 密钥
1. 从 [国家公园服务开发者门户](https://www.nps.gov/subjects/developer/get-started.htm) 获取一个免费的 API 密钥
2. 安全地存储此密钥，因为它将用于验证请求

### 与 Claude 桌面版一起使用

要与此服务器配合 Claude 桌面版使用，请在 `claude_desktop_config.json` 文件中添加以下内容：

```json
{
  "mcpServers": {
    "nationalparks": {
      "command": "npx",
      "args": ["-y", "mcp-server-nationalparks"],
      "env": {
        "NPS_API_KEY": "YOUR_NPS_API_KEY"
      }
    }
  }
}
```

## 示例用法

### 查找某个州的公园
```
Tell me about national parks in Colorado.
```

### 获取特定公园的详细信息
```
What's the entrance fee for Yellowstone National Park?
```

### 检查警报或关闭情况
```
Are there any closures or alerts at Yosemite right now?
```

### 查找游客中心
```
What visitor centers are available at Grand Canyon National Park?
```

### 寻找露营地
```
Are there any campgrounds with electrical hookups in Zion National Park?
```

### 查找即将举行的活动
```
What events are happening at Acadia National Park next weekend?
```

### 根据活动计划旅行
```
Which national parks in Utah have good hiking trails?
```

## 许可证

该 MCP 服务器根据 MIT 许可证发布。详情请参阅 LICENSE 文件。

## 附录：热门国家公园及其代码

| 公园名称 | 公园代码 |
|-----------|-----------|
| 约塞米蒂 | yose |
| 大峡谷 | grca |
| 黄石 | yell |
| 锡安 | zion |
| 大雾山 | grsm |
| 阿卡迪亚 | acad |
| 奥林匹克 | olym |
| 落基山 | romo |
| 约书亚树 | jotr |
| 巨杉和国王峡谷 | seki |

完整列表请访问 [NPS 网站](https://www.nps.gov/findapark/index.htm)。

**官方网站：** [https://github.com/kyrietangsheng/mcp-server-nationalparks](https://github.com/kyrietangsheng/mcp-server-nationalparks)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`search`, `location services`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y mcp-server-nationalparks`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/kyrietangsheng-nationalparks.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
