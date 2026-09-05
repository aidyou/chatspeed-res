---
title: "MCP交易分析平台"
description: "MCP Trader Server 对股票进行综合技术分析，提供趋势、动量指标、波动率指标和成交量分析的见解，以支持股票交易决策。"
---

# MCP交易分析平台

MCP Trader Server 对股票进行综合技术分析，提供趋势、动量指标、波动率指标和成交量分析的见解，以支持股票交易决策。

# MCP 交易者服务器

[Smithery](https://smithery.ai/server/mcp-trader)

一个面向股票交易者的模型上下文协议（MCP）服务器。

## 功能

### 工具

该服务器为股票分析和交易提供了以下工具：

- **analyze-stock**: 对给定的股票代码进行技术分析

  - 必需参数: `symbol` (字符串, 例如 "NVDA")
  - 返回全面的技术分析，包括：
    - 移动平均趋势 (20, 50, 200 日简单移动平均线)
    - 动量指标 (RSI, MACD)
    - 波动率指标 (ATR, ADRP)
    - 成交量分析

- **relative-strength**: 计算相对于基准的股票相对强度

  - 必需参数: `symbol` (字符串, 例如 "AAPL")
  - 可选参数: `benchmark` (字符串, 默认: "SPY")
  - 返回多个时间段（21, 63, 126, 252 天）的相对强度指标
  - 包括股票与基准之间的表现比较

- **volume-profile**: 按价格分析成交量分布

  - 必需参数: `symbol` (字符串, 例如 "MSFT")
  - 可选参数: `lookback_days` (整数, 默认: 60)
  - 返回成交量分布分析，包括：
    - 控制点 (POC) - 成交量最高的价格水平
    - 价值区域 (70% 的成交量范围)
    - 成交量最高的价格水平

- **detect-patterns**: 在价格数据中识别图表模式

  - 必需参数: `symbol` (字符串, 例如 "AMZN")
  - 返回检测到的图表模式及其置信度和价格目标

- **position-size**: 根据风险参数计算最优仓位大小

  - 必需参数:
    - `symbol` (字符串, 例如 "TSLA")
    - `stop_price` (数字)
    - `risk_amount` (数字)
    - `account_size` (数字)
  - 可选参数: `price` (数字, 默认: 当前价格)
  - 返回推荐的仓位大小、美元风险和潜在盈利目标

- **suggest-stops**: 基于技术分析建议止损水平
  - 必需参数: `symbol` (字符串, 例如 "META")
  - 返回基于以下条件的多个止损建议：
    - ATR 基准止损 (1x, 2x, 3x ATR)
    - 百分比基准止损 (2%, 5%, 8%)
    - 技术水平 (移动平均线, 最近的摆动低点)

### 技术分析能力

该服务器利用了多个专门的分析模块：

- **技术分析**: 核心技术指标和趋势分析

  - 移动平均线 (SMA 20, 50, 200)
  - 动量指标 (RSI, MACD)
  - 波动率指标 (ATR, 平均每日波动百分比)
  - 成交量分析 (20日平均成交量)

- **相对强度**: 比较表现分析

  - 多时间框架相对强度评分 (21, 63, 126, 252天)
  - 与基准指数的表现比较
  - 超额/不足表现分类

- **成交量分布**: 高级成交量分析

  - 价格水平成交量分布
  - 控制点 (POC) 识别
  - 价值区域计算 (70% 的成交量)

- **模式识别**: 图表模式检测

  - 支撑/阻力水平
  - 常见图表模式 (头肩顶、双重顶/底等)
  - 检测到的模式的信心评分

- **风险分析**: 仓位大小和风险管理
  - 基于风险的仓位大小
  - 多种止损策略
  - R倍数盈利目标计算

### 数据来源

服务器使用 [Tiingo API](https://api.tiingo.com/) 获取市场数据：

- 历史每日OHLCV数据
- 用于准确回测的调整后价格
- 默认最多一年的历史数据

## 设置

### 先决条件

- Python 3.11+
- [uv](https://github.com/astral-sh/uv)
- [ta-lib](https://ta-lib.org/install/)
- [Tiingo API Key](https://api.tiingo.com/)

### 环境变量

创建一个 `.env` 文件：

```bash
TIINGO_API_KEY=your_api_key_here
```

### 通过Smithery安装

要通过 [Smithery](https://smithery.ai/server/mcp-trader) 自动安装Trader for Claude Desktop：

```bash
npx -y @smithery/cli install mcp-trader --client claude
```

这将执行以下操作：

1. 安装MCP Trader服务器
2. 使用您的Tiingo API密钥进行配置
3. 设置Claude Desktop集成

#### Smithery配置

服务器包含一个 `smithery.yaml` 配置文件，定义了：

- 必需的配置参数 (Tiingo API密钥)
- 启动MCP服务器的命令函数
- 与Claude Desktop的集成

您可以通过编辑 `smithery.yaml` 文件来自定义Smithery配置。

### 安装

```bash
uv venv --python 3.11
source .venv/bin/activate # On Windows: .venv\Scripts\activate
uv sync
```

### Docker部署

项目包含一个用于容器化部署的Dockerfile：

```bash
# Build the Docker image
docker build -t mcp-trader .

# Run the container with your API key
docker run -e TIINGO_API_KEY=your_api_key_here -p 8000:8000 mcp-trader
```

要以HTTP服务器模式运行容器：

```bash
docker run -e TIINGO_API_KEY=your_api_key_here -p 8000:8000 mcp-trader uv run mcp-trader --http
```

## 配置

### Claude Desktop应用程序

在MacOS上: `~/Library/Application\ Support/Claude/claude_desktop_config.json`

在Windows上: `%APPDATA%/Claude/claude_desktop_config.json`

开发配置：

```json
{
  "mcpServers": {
    "stock-analyzer": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/mcp-trader",
        "run",
        "mcp-trader"
      ]
      "env": {
        "TIINGO_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

## 开发

### 构建和运行

```bash
uv build
uv run mcp-trader
```

### HTTP服务器模式

服务器也可以作为独立的HTTP服务器运行，以便测试或与其他应用程序集成：

```bash
uv run mcp-trader --http
```

这将在 [http://localhost:8000](http://localhost:8000) 上启动一个HTTP服务器，并提供以下端点：

- **GET /list-tools**: 返回可用工具及其架构的列表
- **POST /call-tool**: 使用提供的参数执行工具
  - 请求体格式：
```json
    {
      "name": "analyze-stock",
      "arguments": {
        "symbol": "AAPL"
      }
    }
```
  - 返回一个内容项数组（文本、图片等）

### 调试

使用 MCP Inspector 进行调试：

```bash
npx @modelcontextprotocol/inspector uv --directory /path/to/mcp-trader run mcp-trader
```

## 示例用法

在 Claude Desktop 中：

```
Analyze the technical setup for NVDA
```

服务器将返回技术分析摘要，包括趋势状态、动量指标和关键指标。

## 依赖项

请参阅 pyproject.toml 获取完整的依赖项列表：

```
- aiohttp >=3.11.11
- mcp >=1.2.0
- numpy ==1.26.4
- pandas >=2.2.3
- pandas-ta >=0.3.14b0
- python-dotenv >=1.0.1
- setuptools >=75.8.0
- ta-lib >=0.6.0
```

## 贡献

欢迎为 MCP Trader 做贡献！以下是一些你可以贡献的方式：

- **添加新工具**：实现额外的技术分析工具或交易策略
- **改进现有工具**：提高当前工具的准确性或性能
- **添加数据源**：集成额外的市场数据提供商
- **文档**：改进文档或添加示例
- **修复错误**：修复问题或改进错误处理

### 开发工作流程

1. 叉分仓库
2. 创建功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交你的更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 打开一个 Pull Request

## 未来计划

MCP Trader 项目有多个计划中的增强功能：

- **投资组合分析**：用于分析和优化投资组合的工具
- **回测**：在历史数据上测试交易策略的能力
- **情绪分析**：与新闻和社交媒体情绪数据的集成
- **期权分析**：用于分析期权策略和定价的工具
- **实时数据**：支持实时市场数据流
- **自定义策略**：实现和测试自定义交易策略的框架
- **警报**：价格和技术指标警报的通知系统

## 进一步阅读

通过这些详细的博客文章了解更多关于此项目的信息：

- [使用 MCP 构建股票分析服务器，第 1 部分](https://sethhobson.com/2025/01/building-a-stock-analysis-server-with-mcp-part-1/) - 初始设置、架构和核心技术分析功能
- [使用 MCP 构建股票分析服务器，第 2 部分](https://sethhobson.com/2025/03/building-a-stock-analysis-server-with-mcp-part-2/) - 相对强度、成交量、模式识别、风险分析

**官方网站：** [https://github.com/wshobson/mcp-trader](https://github.com/wshobson/mcp-trader)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`finance`, `data`
- 标签：`finance`, `research and data`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`--directory /absolute/path/to/mcp-trader run mcp-trader`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/wshobson-trader.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
