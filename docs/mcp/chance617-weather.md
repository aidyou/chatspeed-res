---
title: "天气查询"
description: "MCP 天气查询服务 这是一个基于MCP (Minimalist Chat Protocol) 的天气查询服务，允许用户通过简单的命令查询不同城市的天气信息。 功能特点 - 支持查询全球主要城市的天气信息 - 提供温度、天气状况、湿度和风速等详细信息 - 使用异步处理提高响应速度 - 完善的错误处理机制 - 支持模拟数据模式，无需API密钥即可测试 安装要求 - Python 3.13 或更高版本 - 依赖包： - httpx = 0.28.1 - mcp = 1.11.0 使用方法 1. 确保已安装所有依赖： p"
---

# 天气查询

MCP 天气查询服务 这是一个基于MCP (Minimalist Chat Protocol) 的天气查询服务，允许用户通过简单的命令查询不同城市的天气信息。 功能特点 - 支持查询全球主要城市的天气信息 - 提供温度、天气状况、湿度和风速等详细信息 - 使用异步处理提高响应速度 - 完善的错误处理机制 - 支持模拟数据模式，无需API密钥即可测试 安装要求 - Python 3.13 或更高版本 - 依赖包： - httpx = 0.28.1 - mcp = 1.11.0 使用方法 1. 确保已安装所有依赖： p

# MCP 天气查询服务

这是一个基于MCP (Minimalist Chat Protocol) 的天气查询服务，允许用户通过简单的命令查询不同城市的天气信息。

## 功能特点

- 支持查询全球主要城市的天气信息
- 提供温度、天气状况、湿度和风速等详细信息
- 使用异步处理提高响应速度
- 完善的错误处理机制
- 支持模拟数据模式，无需API密钥即可测试

## 安装要求

- Python 3.13 或更高版本
- 依赖包：
  - httpx >= 0.28.1
  - mcp >= 1.11.0

## 使用方法

1. 确保已安装所有依赖：
```
   pip install -r requirements.txt
```
   或使用项目配置：
```
   pip install -e .
```

2. 在OpenWeatherMap API配置部分填入你的API密钥（可选）：
```python
   OPENWEATHER_API_KEY = "你的API密钥"  # 替换为你的OpenWeatherMap API密钥
```
   如果不设置API密钥，服务将使用模拟数据。

3. 运行服务器：
```
   python main.py
```

4. 使用以下命令查询天气：
```
   /weather 城市名
```
   例如：`/weather 北京`

## 获取OpenWeatherMap API密钥

1. 访问 [OpenWeatherMap官网](https://openweathermap.org/) 并注册账号
2. 登录后，进入API密钥页面
3. 创建一个新的API密钥
4. 将获取的API密钥复制到代码中的`OPENWEATHER_API_KEY`变量

## 开发说明

- `main.py` - 主程序文件，包含MCP服务器和天气查询功能
- 使用FastMCP框架处理请求和响应
- 通过OpenWeatherMap API获取天气数据
- 支持模拟数据模式，便于开发和测试

## 注意事项

- 免费的OpenWeatherMap API有请求次数限制，请合理使用
- 如果不设置API密钥，服务将使用模拟数据

**官方网站：** [https://www.modelscope.cn/studios/chance617/Weather](https://www.modelscope.cn/studios/chance617/Weather)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`productivity`
- 标签：`calendar management`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`--directory D:\MCP\MCP_Minimalist_Development\example run main.py`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/chance617-weather.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
