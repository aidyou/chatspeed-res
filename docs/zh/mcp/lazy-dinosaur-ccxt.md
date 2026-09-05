---
title: "CCXT-MCP"
description: "允许AI模型通过Model Context协议与加密货币交易所API交互的服务器，提供对100多家交易所及其交易功能的访问。"
---

# CCXT-MCP

允许AI模型通过Model Context协议与加密货币交易所API交互的服务器，提供对100多家交易所及其交易功能的访问。

# CCXT MCP 服务器

[![npm 版本](/mcp-assets/bd2769ecb427064450e03819af05aed2.svg)](https://www.npmjs.com/package/@lazydino/ccxt-mcp)
[![npm 下载量](/mcp-assets/eaac4374b03e037e3ead64cc14258ebb.svg)](https://www.npmjs.com/package/@lazydino/ccxt-mcp)
[![GitHub 星标](/mcp-assets/d8445d529be7383c056ef87b71b3fd86.svg)](https://github.com/lazy-dinosaur/ccxt-mcp/stargazers)
[![许可证: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)

[韩语版本 (Korean version)](https://github.com/lazy-dinosaur/ccxt-mcp/blob/HEAD/README.ko.md)

CCXT MCP 服务器是一个允许 AI 模型通过 [Model Context Protocol (MCP)](https://github.com/anthropics/anthropic-cookbook/tree/main/model-context-protocol) 与加密货币交易所 API 进行交互的服务器。该服务器使用 [CCXT 库](https://github.com/ccxt/ccxt) 提供对超过 100 个加密货币交易所及其交易功能的访问。

## 🚀 快速开始

```bash
# Install the package globally
npm install -g @lazydino/ccxt-mcp

# Run with default settings
ccxt-mcp

# or run without installation
npx @lazydino/ccxt-mcp
```

## 安装和使用

### 全局安装

```bash
# Install the package globally
npm install -g @lazydino/ccxt-mcp
```

### 使用 npx 运行

你可以直接运行而无需安装：

```bash
# Using default settings
npx @lazydino/ccxt-mcp

# Using custom configuration file
npx @lazydino/ccxt-mcp --config /path/to/config.json
```

查看帮助：

```bash
npx @lazydino/ccxt-mcp --help
```

## 配置

### 在 Claude Desktop 中注册 MCP 服务器

1. **打开 Claude Desktop 设置**：

   - 前往 Claude Desktop 应用中的设置菜单
   - 找到 "MCP Servers" 部分

2. **添加新的 MCP 服务器**：

   - 点击 "Add Server" 按钮
   - 服务器名称: `ccxt-mcp`
   - 命令: `npx @lazydino/ccxt-mcp`
   - 额外参数（可选）: `--config /path/to/config.json`

3. **保存并测试服务器**：
   - 保存设置
   - 使用 "Test Connection" 按钮测试连接

### 配置方法 - 两个选项

#### 选项 1：直接在 Claude Desktop 设置中包含账户信息（基本方法）

此方法将 CCXT 账户信息直接包含在 Claude Desktop 设置文件 (claude_desktop_config.json) 中：

```json
{
  "mcpServers": {
    "ccxt-mcp": {
      "command": "npx",
      "args": ["-y", "@lazydino/ccxt-mcp"],
      "accounts": [
        {
          "name": "bybit_main",
          "exchangeId": "bybit",
          "apiKey": "YOUR_API_KEY",
          "secret": "YOUR_SECRET_KEY",
          "defaultType": "spot"
        },
        {
          "name": "bybit_futures",
          "exchangeId": "bybit",
          "apiKey": "YOUR_API_KEY",
          "secret": "YOUR_SECRET_KEY",
          "defaultType": "swap"
        }
      ]
    }
  }
}
```

使用这种方法，你不需要单独的配置文件。所有设置都集成到了 Claude Desktop 配置文件中。

#### 选项 2：使用单独的配置文件（高级方法）

为了将账户信息分离到一个单独的配置文件中，请按如下步骤设置：

1. **创建一个单独的配置文件**（例如，`ccxt-accounts.json`）：

```json
{
  "accounts": [
    {
      "name": "bybit_main",
      "exchangeId": "bybit",
      "apiKey": "YOUR_API_KEY",
      "secret": "YOUR_SECRET_KEY",
      "defaultType": "spot"
    },
    {
      "name": "bybit_futures",
      "exchangeId": "bybit",
      "apiKey": "YOUR_API_KEY",
      "secret": "YOUR_SECRET_KEY",
      "defaultType": "swap"
    }
  ]
}
```

2. **在 Claude Desktop 设置中指定配置文件路径**：

```json
{
  "mcpServers": {
    "ccxt-mcp": {
      "command": "npx",
      "args": [
        "-y",
        "@lazydino/ccxt-mcp",
        "--config",
        "/path/to/ccxt-accounts.json"
      ]
    }
  }
}
```

> **使用单独配置文件的原因**：
>
> - 防止递归引用问题
> - 分离敏感信息如 API 密钥
> - 更容易进行多环境配置（开发、测试、生产）
> - 改进配置文件的版本控制

## 主要特性

- **市场信息检索**：

  - 列出交易所
  - 按交易所查看市场信息
  - 获取特定符号的价格信息
  - 查看特定符号的订单簿信息
  - 搜索历史OHLCV数据

- **交易功能**：

  - 创建市价/限价订单
  - 取消订单并检查状态
  - 查看账户余额
  - 检查交易历史

- **交易分析**：

  - 日/周/月表现分析
  - 胜率计算（最近7天、30天、所有时间）
  - 平均盈亏比（R倍数）
  - 最大连亏/连赢系列分析
  - 资产变动跟踪
  - 综合绩效指标
  - 交易模式识别
  - 基于周期的回报计算

- **仓位管理**：

  - 资金比例交易（例如，使用账户资金的5%进入）
  - 期货市场杠杆设置（1-100倍）
  - 动态仓位大小（基于波动性）
  - 分割买入/卖出策略实施

- **风险管理**：
  - 基于技术指标的止损设置（例如，5分钟图表上10根蜡烛中的最低点）
  - 基于波动性的止损/止盈（ATR倍数）
  - 最大允许损失限额（日/周）
  - 动态止盈设置（追踪利润）

## 工作原理

```
User  AI Model(Claude/GPT)  MCP Protocol  CCXT MCP Server  Cryptocurrency Exchange API
```

1. **用户**：提出如“告诉我比特币的价格”或“在我的币安账户上购买以太坊”这样的请求。
2. **AI模型**：理解用户请求，并确定使用哪些MCP工具/资源。
3. **MCP协议**：AI与CCXT MCP服务器之间的标准化通信。
4. **CCXT MCP服务器**：使用CCXT库与加密货币交易所API进行通信。
5. **交易所API**：提供实际数据并执行交易订单。

## 与AI模型结合使用

当注册了Claude Desktop后，您可以向AI模型发出以下类型的请求：

### 注意事项和推荐提示

在使用AI模型时，请考虑以下注意事项，并使用以下提示以实现有效的交易：

```
Your goal is to execute trades using the ccxt tools as much as possible
Cautions:
- Accurately identify whether it's a futures market or spot market before proceeding with trades
- If there's no instruction about percentage of capital or amount to use, always calculate and execute trades using the entire available capital
```

**注意事项：**

- AI模型有时会将期货交易与现货交易混淆。
- 如果没有明确的交易资本规模指导，AI可能会感到困惑。
- 使用上述提示有助于清晰地传达您的交易意图。

### 基本查询示例

```
Check and compare the current Bitcoin price on binance and coinbase.
```

### 高级交易查询示例

**仓位管理**

```
Open a long position on BTC/USDT futures market in my Bybit account (bybit_futures) with 5% of capital using 10x leverage.
Enter based on moving average crossover strategy and set stop loss at the lowest point among the 12 most recent 5-minute candles.
```

**性能分析**

```
Analyze my Binance account (bybit_main) trading records for the last 7 days and show me the win rate, average profit, and maximum consecutive losses.
```

**详细的交易分析**

```
Analyze my trading performance on the bybit_futures account for BTC/USDT over the last 30 days. Calculate win rate, profit factor, and identify any patterns in my winning trades.
```

```
Show me the monthly returns for my bybit_main account over the past 90 days and identify my best and worst trading months.
```

```
Analyze my consecutive wins and losses on my bybit_futures account and tell me if I have any psychological patterns affecting my trading after losses.
```

## 开发

### 从源码构建

```bash
# Clone repository
git clone https://github.com/lazy-dinosaur/ccxt-mcp.git

# Navigate to project directory
cd ccxt-mcp

# Install dependencies
npm install

# Build
npm run build
```

## 🤝 贡献

欢迎贡献！请随时提交Pull Request。

## 📄 许可证

根据MIT许可证分发。有关更多信息，请参阅LICENSE文件。

## ❤️ 支持

如果您觉得这个项目有用，请考虑在GitHub上给它一个⭐️！

**官方网站：** [https://github.com/lazy-dinosaur/ccxt-mcp](https://github.com/lazy-dinosaur/ccxt-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`finance`
- 标签：`finance`, `cloud platforms`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @lazydino/ccxt-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/lazy-dinosaur-ccxt.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
