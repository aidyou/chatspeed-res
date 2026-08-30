---
title: "QWeather气象控制平台"
description: "请提供具体的正文内容，目前的内容“qweather mcp”不足以进行准确的语言识别和翻译。如果这是特定术语或代码，请给予更多上下文信息。"
---

# QWeather气象控制平台

请提供具体的正文内容，目前的内容“qweather mcp”不足以进行准确的语言识别和翻译。如果这是特定术语或代码，请给予更多上下文信息。

# qweather-mcp
[Smithery](https://smithery.ai/server/@overstarry/qweather-mcp)

用于 [QWeather](https://www.qweather.com/) API 的 MCP 服务器。

该项目通过模型上下文协议（MCP）提供天气信息查询功能。

## 使用方法

在这里获取您的 API 密钥 [here](https://console.qweather.com/)。

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@overstarry/qweather-mcp) 自动为 Claude Desktop 安装 qweather-mcp：

```bash
npx -y @smithery/cli install @overstarry/qweather-mcp --client claude
```

### 手动配置

```bash
# stdio server
npx -y qweather-mcp

```

环境变量：

```
QWEATHER_API_BASE=https://api.qweather.com
QWEATHER_API_KEY=
```

### JSON 配置

```json
{
  "mcpServers": {
    "qweather": {
      "command": "npx",
      "args": ["-y", "qweather-mcp"],
      "env": {
        "QWEATHER_API_BASE": "",
        "QWEATHER_API_KEY": ""
      }
    }
  }
}
```

### 可用工具

- `lookup-city`: 根据名称查找城市信息
- `get-weather-now`: 获取某个地点的当前天气

## 许可证

MIT。

**官方网站：** [https://github.com/overstarry/qweather-mcp](https://github.com/overstarry/qweather-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`
- 标签：`search`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y qweather-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/overstarry-qweather.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
