---
title: "MCP 城市天气查询"
description: "MCP天气查询服务器 基于天行数据API的MCP（模型上下文协议）天气查询服务器，为AI模型提供实时天气信息查询功能。 🌟 功能特性 - 城市搜索: 支持中文和英文城市名称搜索 - 实时天气: 获取当前天气、温度、湿度、风力等详细信息 - 空气质量: 提供AQI指数和空气质量等级 - 生活提示: 根据天气情况提供穿衣和出行建议 - 丰富展示: 使用emoji图标，信息展示直观友好 🛠️ MCP工具…"
---

# MCP 城市天气查询

MCP天气查询服务器 基于天行数据API的MCP（模型上下文协议）天气查询服务器，为AI模型提供实时天气信息查询功能。 🌟 功能特性 - 城市搜索: 支持中文和英文城市名称搜索 - 实时天气: 获取当前天气、温度、湿度、风力等详细信息 - 空气质量: 提供AQI指数和空气质量等级 - 生活提示: 根据天气情况提供穿衣和出行建议 - 丰富展示: 使用emoji图标，信息展示直观友好 🛠️ MCP工具…

# MCP天气查询服务器

基于天行数据API的MCP（模型上下文协议）天气查询服务器，为AI模型提供实时天气信息查询功能。

## 🌟 功能特性

- **城市搜索**: 支持中文和英文城市名称搜索
- **实时天气**: 获取当前天气、温度、湿度、风力等详细信息
- **空气质量**: 提供AQI指数和空气质量等级
- **生活提示**: 根据天气情况提供穿衣和出行建议
- **丰富展示**: 使用emoji图标，信息展示直观友好

## 🛠️ MCP工具函数

### 1. `query_weather(city: str)`
根据城市名称查询天气信息。

**参数:**
- `city`: 城市名称（支持中文和英文，如：广州、北京、shanghai等）

**返回:**
- 格式化的天气信息字符串，包含温度、湿度、风力、空气质量等

**示例:**
```python
result = await query_weather("广州")
# 返回:
# 📍 广东 广州 (2025-06-14 星期六)
# 🌤️ 天气: 阴
# 🌡️ 当前温度: 26.4℃
# 📊 温度范围: 24℃ ~ 30℃
# ...
```

### 2. `search_city_info(city: str)`
搜索城市的详细信息。

**参数:**
- `city`: 城市名称（支持中文和英文）

**返回:**
- 城市详细信息字符串，包含中英文名称、省份、经纬度、城市代码等

**示例:**
```python
result = await search_city_info("广州")
# 返回:
# 🏙️ 城市信息
# 📍 中文名称: 广州
# 🔤 英文名称: guangzhou
# 🗺️ 所属省份: 广东 (guangdong)
# ...
```

## 📦 安装和使用

### 1. 安装依赖
```bash
cd mcp-weather/mcp-server-weather
uv sync
```

### 2. 启动服务器
```bash
# 使用内置API Key
python server.py

# 或使用自定义API Key
python server.py --api_key YOUR_API_KEY
```

### 3. 配置MCP客户端（Cursor集成）
在Cursor的`.cursor/mcp.json`文件中添加如下配置：

```json
{
  "mcpServers": {
    "weather": {
      "command": "uv",
      "args": [
        "--directory",
        "/Users/luoshui/Documents/Cursor/MCP/mcp-weather/mcp-server-weather",
        "run",
        "server.py"
      ],
      "disabled": false,
      "autoApprove": [
        "query_weather",
        "search_city_info"
      ]
    }
  }
}
```

**参数说明：**
- `command`: 使用`uv`作为包管理器运行
- `--directory`: 指定服务目录
- `run server.py`: 启动天气服务
- `autoApprove`: 自动批准工具函数调用，无需手动确认
- `disabled`: 是否禁用该服务

> **注意：** 路径请根据你本地实际情况调整。

### 4. 使用方法
- 在Cursor中直接用自然语言提问天气，如"查询广州天气""北京空气质量如何"等，AI会自动调用MCP工具。
- 支持城市详细信息查询，如"广州的城市代码是多少"。

## 🔧 技术实现

- **API提供商**: 天行数据 (tianapi.com)
- **HTTP客户端**: httpx
- **MCP框架**: FastMCP
- **异步支持**: 完全异步实现，支持并发请求
- **错误处理**: 完善的错误处理和用户友好的错误信息

## 📊 API接口

### 城市搜索接口
- **URL**: `https://apis.tianapi.com/citylookup/index`
- **方法**: GET
- **参数**: `key`, `area`

### 天气查询接口
- **URL**: `https://apis.tianapi.com/tianqi/index`
- **方法**: GET
- **参数**: `key`, `city`, `type`

## 🧪 测试结果

✅ 所有功能测试通过：
- API连接正常
- 城市搜索功能正常
- 天气查询功能正常
- 数据格式化正常
- MCP工具函数正常

## 📝 注意事项

1. **城市名称**: 支持中文城市名称，英文名称支持有限
2. **API限制**: 使用免费API Key，可能有请求频率限制
3. **网络依赖**: 需要稳定的网络连接访问天行数据API
4. **数据准确性**: 天气数据来源于天行数据，准确性依赖于数据提供商

## 🔄 更新日志

- **v0.1.0**: 初始版本，实现基本天气查询功能
- 支持城市搜索和天气查询
- 完善的错误处理和数据格式化
- MCP工具函数集成

## 📄 许可证

本项目遵循MIT许可证。

**官方网站：** [https://github.com/luoshui-coder/mcp-server-weather.git](https://github.com/luoshui-coder/mcp-server-weather.git)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`search`, `location services`, `天气`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`--directory /Users/luoshui/Documents/Cursor/MCP/mcp-weather/mcp-server-weather run server.py`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/luoshui2025-weather.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
