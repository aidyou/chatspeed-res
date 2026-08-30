---
title: "MCP-Weather天气工具"
description: "通过使用AccuWeather API提供每小时天气预报，使用户能够获取当前天气状况以及针对特定地点的详细12小时预报。"
---

# MCP-Weather天气工具

通过使用AccuWeather API提供每小时天气预报，使用户能够获取当前天气状况以及针对特定地点的详细12小时预报。

# MCP 天气服务器

一个简单的MCP服务器，使用AccuWeather API提供每小时天气预报。

## 设置

1. 使用 `uv` 安装依赖项：
```bash
uv venv
uv sync
```

2. 创建一个包含您的AccuWeather API密钥的 `.env` 文件：
```
ACCUWEATHER_API_KEY=your_api_key_here
```

您可以通过在[AccuWeather API](https://developer.accuweather.com/)注册来获取API密钥。

## 运行服务器

```json
{
    "mcpServers": {
        "weather": {
            "command": "uvx",
            "args": ["--from", "git+https://github.com/adhikasp/mcp-weather.git", "mcp-weather"],
            "env": {
                "ACCUWEATHER_API_KEY": "your_api_key_here"
            }
        }
    }
}
```

## API 使用

### 获取每小时天气预报

响应：
```json
{
    "location": "Jakarta",
    "location_key": "208971",
    "country": "Indonesia",
    "current_conditions": {
        "temperature": {
            "value": 32.2,
            "unit": "C"
        },
        "weather_text": "Partly sunny",
        "relative_humidity": 75,
        "precipitation": false,
        "observation_time": "2024-01-01T12:00:00+07:00"
    },
    "hourly_forecast": [
        {
            "relative_time": "+1 hour",
            "temperature": {
                "value": 32.2,
                "unit": "C"
            },
            "weather_text": "Partly sunny",
            "precipitation_probability": 40,
            "precipitation_type": "Rain",
            "precipitation_intensity": "Light"
        }
    ]
}
```

该API提供：
- 当前天气状况，包括温度、天气描述、湿度和降水状态
- 12小时预报，每小时数据包括：
  - 从当前时间开始的相对时间
  - 摄氏温度
  - 天气描述
  - 降水概率、类型和强度

**官方网站：** [https://github.com/adhikasp/mcp-weather](https://github.com/adhikasp/mcp-weather)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`location services`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`--from git+https://github.com/adhikasp/mcp-weather.git mcp-weather`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/adhikasp-weather.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
