---
title: "实时天气MCP服务器"
description: "一个通过OpenWeatherMap API提供实时天气信息（包括温度、湿度、风速和日出/日落时间）的MCP服务器。"
---

# 实时天气MCP服务器

一个通过OpenWeatherMap API提供实时天气信息（包括温度、湿度、风速和日出/日落时间）的MCP服务器。

# Weather MCP Server

[Smithery](https://smithery.ai/server/@CodeByWaqas/weather-mcp-server)

这是一个使用 OpenWeatherMap API 提供天气信息的现代代码协议（MCP）服务器。

## 特性

- 实时天气数据检索
- 温度采用公制单位
- 详细的天气信息包括：
  - 温度
  - 湿度
  - 风速
  - 日出/日落时间
  - 天气描述

## 前提条件

- Python 3.12 或更高版本
- OpenWeatherMap API 密钥

## 安装

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@CodeByWaqas/weather-mcp-server) 自动为 Claude Desktop 安装 Weather MCP Server：

```bash
npx -y @smithery/cli install @CodeByWaqas/weather-mcp-server --client claude
```

### 手动安装
1. 克隆仓库
2. 创建虚拟环境：
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```
3. 安装依赖项：
```bash
pip install -e .
```

## 设置说明

### 使用 Claude Desktop 设置
```json
# claude_desktop_config.json
# Can find location through:
# Claude -> Settings -> Developer -> Edit Config
{
  "mcpServers": {
      "mcp-weather-project": {
          "command": "uv",
          "args": [
              "--directory",
              "/
/weather-mcp-server/src/resources",
              "run",
              "server.py"
          ],
          "env": {
            "WEATHER_API_KEY": "YOUR_API_KEY"
          }
      }
  }
}
```
## 本地/开发设置说明
### 克隆仓库
`git clone https://github.com/CodeByWaqas/weather-mcp-server`
### 安装依赖项
安装 MCP 服务器依赖项：
```bash
cd weather-mcp-server

# Create virtual environment and activate it
uv venv

source .venv/bin/activate # MacOS/Linux
# OR
.venv/Scripts/activate # Windows

# Install dependencies
uv add "mcp[cli]" python-dotenv requests httpx
```

## 配置

1. 将 `src/resources/env.example` 复制到 `src/resources/.env`
2. 在 `.env` 文件中添加您的 OpenWeatherMap API 密钥：
```
WEATHER_API_KEY=your_api_key_here
```

## 使用

运行 Claude Desktop 并使用 LLM 检索天气信息

## 许可证

该项目根据 MIT 许可证授权 - 请参阅 LICENSE 文件获取详细信息。

**官方网站：** [https://github.com/CodeByWaqas/weather-mcp-server](https://github.com/CodeByWaqas/weather-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`
- 标签：`search`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`--directory /<absolute-path>/weather-mcp-server/src/resources run server.py`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/codebywaqas-weather.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
