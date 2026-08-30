---
title: "股票分析-MCP"
description: "允许 Claude 和其他 MCP 客户端访问 Alpha Vantage API 提供的实时和历史股票市场数据，包括具有可自定义间隔的盘中和每日股票数据。"
---

# 股票分析-MCP

允许 Claude 和其他 MCP 客户端访问 Alpha Vantage API 提供的实时和历史股票市场数据，包括具有可自定义间隔的盘中和每日股票数据。

# Alpha Vantage 股票 MCP 服务器

这是一个 Model Context Protocol (MCP) 服务器，它通过 Alpha Vantage API 提供股票市场数据。它允许 Claude 和其他 MCP 客户端访问实时和历史股票数据。

  

## 功能

- 获取可自定义间隔的日内股票数据
- 获取每日股票数据
- 根据价格变动生成股票警报
- 作为资源访问股票数据

## 先决条件

- Node.js 16 或更高版本
- Alpha Vantage API 密钥（在 [Alpha Vantage](https://www.alphavantage.co/support/#api-key) 免费获取）

## 安装

1. 克隆此仓库
2. 安装依赖项：
```
   npm install
```
3. 在根目录下创建一个 `.env` 文件，并添加您的 Alpha Vantage API 密钥：
```
   ALPHA_VANTAGE_API_KEY=your_api_key_here
```

## 构建和运行

构建 TypeScript 代码：
```
npm run build
```

运行服务器：
```
npm start
```

开发时自动重新加载：
```
npm run dev
```

测试 API 客户端：
```
npm test
```

## 与桌面版 Claude 一起使用

要将此 MCP 服务器与桌面版 Claude 一起使用：

1. 打开桌面版 Claude
2. 转到设置 > 开发者 > 编辑配置
3. 将以下内容添加到您的 `claude_desktop_config.json` 中：

```json
{
  "mcpServers": {
    "alpha-vantage": {
      "command": "node",
      "args": ["/absolute/path/to/dist/index.js"],
      "env": {
        "ALPHA_VANTAGE_API_KEY": "YOUR_API_KEY"
      } 
    }
  }
}
```

将 `/absolute/path/to/dist/index.js` 替换为已构建的 index.js 文件的绝对路径。

4. 重启桌面版 Claude

## 可用工具

### get-stock-data

获取特定符号的日内股票数据。

参数：
- `symbol`（必需）：股票符号（例如 IBM, AAPL）
- `interval`（可选）：数据点之间的时间间隔（1min, 5min, 15min, 30min, 60min）。默认值：5min
- `outputsize`（可选）：返回的数据量（compact：最新 100 个数据点，full：最多 20 年的数据）。默认值：compact

### get-daily-stock-data

获取特定符号的每日股票数据。

参数：
- `symbol`（必需）：股票符号（例如 IBM, AAPL）
- `outputsize`（可选）：返回的数据量（compact：最新 100 个数据点，full：最多 20 年的数据）。默认值：compact

### get-stock-alerts

分析股票数据以根据价格变动生成警报。

参数：
- `symbol`（必需）：股票符号（例如 IBM, AAPL）
- `threshold`（可选）：价格变动警报的百分比阈值。默认值：5

## 可用资源

### stock-data

直接作为资源访问股票数据。

URI 模板：`stock://{symbol}/{interval}`

参数：
- `symbol`：股票符号（例如 IBM, AAPL）
- `interval`：时间间隔（daily, 1min, 5min, 15min, 30min, 60min）。默认值：daily

在 Claude 中的示例用法：
- "你能分析这个股票数据吗：stock://AAPL/daily"
- "你认为这些数据怎么样：stock://MSFT/5min"

## 许可证

MIT

**官方网站：** [https://github.com/ranveer0323/stock-analysis-mcp](https://github.com/ranveer0323/stock-analysis-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`finance`
- 标签：`finance`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`/absolute/path/to/dist/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/ranveer0323-stock-analysis.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
