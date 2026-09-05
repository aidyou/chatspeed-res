---
title: "MCP股票数据服务"
description: "通过为AI助手提供的模型上下文协议（MCP）服务器，实时访问全球股市数据，包括当前价格、历史图表和公司财务信息。"
---

# MCP股票数据服务

通过为AI助手提供的模型上下文协议（MCP）服务器，实时访问全球股市数据，包括当前价格、历史图表和公司财务信息。

# 全球MCP股票服务器

用于全球股市数据和分析的Model Context Protocol (MCP) 服务器

## 概述

此项目提供了一个MCP服务器，用于访问股市数据。它使得AI助手能够实时访问股价、图表数据、公司信息等。

## MCP（模型上下文协议）是什么？

模型上下文协议（MCP）是一种标准化的方法，允许应用程序向大规模语言模型（LLM）提供上下文。详情请参阅 [Model Context Protocol 网站](https://modelcontextprotocol.github.io/)。

## 功能

- 获取实时股价信息
- 股价历史数据与图表
- 支持主要股市指标
- 公司信息与财务数据
- 使用TypeScript实现并严格类型检查

# 用户指南

## 前提条件

- Node.js 18 或更高版本
- npm 或 yarn

## 安装方法

1. 克隆仓库:

```bash
   git clone https://github.com/sakura-ku/grobal_mcp_stock_server.git
   cd grobal_mcp_stock_server
```

2. 安装依赖项:

```bash
   npm install
```

3. 构建并运行服务器:

```bash
   npm run build
   npm start
```

## 使用方法

### 1. 设置环境变量

首先，设置必要的环境变量。创建一个`.env`文件或复制现有的`.env.example`文件：

```bash
# Windows PowerShellの場合
Copy-Item .env.example .env

# UNIX系システムの場合
cp .env.example .env
```

编辑`.env`文件以配置所需的API密钥：

```
# 基本設定
PORT=3000
HOST=localhost
NODE_ENV=development

# Polygon.io APIキー (株価データ取得用)
POLYGON_API_KEY=your_polygon_api_key_here

# その他のAPIキー...
```

### 2. 运行服务器

在开发模式下启动服务器：

```bash
npm run dev
```

在生产模式下启动服务器：

```bash
npm run build
npm run start:prod
```

### 3. API使用方式

#### 直接从浏览器访问

服务器启动后，可以通过以下URL直接从浏览器访问股价数据：

```
http://localhost:3000/api/stock/price?symbol=AAPL
```

#### 使用cURL的示例

可以从命令行使用cURL获取数据：

```bash
# 株価データの取得
curl "http://localhost:3000/api/stock/price?symbol=AAPL"

# 株価履歴データの取得（過去30日間）
curl "http://localhost:3000/api/stock/history?symbol=AAPL&days=30"
```

#### 从程序中使用的示例

从Node.js应用程序中使用的例子：

```javascript
// 株価データを取得する関数
async function getStockPrice(symbol) {
  const response = await fetch(`http://localhost:3000/api/stock/price?symbol=${symbol}`);
  const data = await response.json();
  return data;
}

// 使用例
getStockPrice('AAPL').then(data => {
  console.log(`現在の${data.symbol}の株価: ${data.price} ${data.currency}`);
});
```

### 4. 与AI助手集成

有关如何与Claude、GPT-4等AI助手集成的信息，请参见“与MCP客户端协作”部分。

#### Claude使用示例

Claude提示的例子：

```
株価を調べてください。
テスラ（TSLA）の現在の株価と、過去1週間の動向を教えてください。
```

#### AI助手响应示例

```
テスラ（TSLA）の株価情報は以下の通りです：

現在の株価: $248.42 USD
前日比: +$5.21 (+2.14%)
取引量: 3,421,532株

過去1週間の動向:
- 7日前: $230.15
- 6日前: $232.05
- 5日前: $235.87
- 4日前: $239.14
- 3日前: $242.33
- 2日前: $243.21
- 1日前: $248.42

過去1週間で約8%の上昇トレンドを示しています。特に直近3日間で価格の上昇が加速しています。
```

## 可用工具

### 获取股价信息 (get_stock_price)

获取指定股票代码的当前股价及相关信息。

**参数:**
- `symbol` (string): 股票代码（例如: AAPL, MSFT, GOOGL）

**返回值:**
- 股价信息（价格、变动、货币等）

## 与MCP客户端协作

要在客户端（如Claude, Claude Desktop, 其他支持MCP的应用程序）中使用此MCP服务器，需要创建一个mcp.json文件来定义MCP服务器。

### mcp.json定义示例

下面是一个使用本服务器的mcp.json定义示例。将此配置添加到MCP客户端中，即可访问股价信息：

```json
{
  "servers": [
    {
      "id": "global-stock-server",
      "url": "http://localhost:3000",
      "description": "株式市場データと分析のためのMCPサーバー",
      "tools": [
        {
          "name": "get_stock_price",
          "description": "指定された株式銘柄の現在の株価と関連情報を取得します",
          "parameters": {
            "type": "object",
            "required": ["symbol"],
            "properties": {
              "symbol": {
                "type": "string",
                "description": "株式銘柄コード（例: AAPL, MSFT, GOOGL）"
              }
            }
          }
        }
      ]
    }
  ]
}
```

### 在MCP客户端中的设置方法

1. 将上述mcp.json定义保存至任意位置
2. 打开MCP客户端（如Claude Desktop）的设置界面
3. 在MCP设置部分选择“添加服务器”或“导入”选项
4. 选择已保存的mcp.json文件或将内容复制粘贴
5. 保存设置并重启客户端

这样，在MCP客户端的提示或聊天中就可以使用股价信息工具了。

### Cursor IDE中的设置方法

在Cursor IDE中，通过向settings.json文件添加MCP服务器设置，可以使AI助手能够使用这些工具。

#### 设置步骤

1. 打开Cursor设置：
   - Windows/Linux: `Ctrl+,`
   - macOS: `Cmd+,`

2. 选择"Cursor Settings"并编辑settings.json文件

3. 在`mcpServers`部分添加以下设置:

##### 作为本地项目运行（推荐）

该项目假设您将在本地进行开发和运行。使用npm脚本来运行是最可靠的方法：

```json
{
  "mcpServers": {
    "global-stock-server": {
      "command": "npm",
      "args": ["run", "start"],
      "cwd": "/path/to/grobal_mcp_stock_server",
      "env": {
        "PORT": "3000",
        "HOST": "localhost",
        "NODE_ENV": "production",
        "STOCK_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

在开发模式下运行时:

```json
{
  "mcpServers": {
    "global-stock-server": {
      "command": "npm",
      "args": ["run", "dev"],
      "cwd": "/path/to/grobal_mcp_stock_server",
      "env": {
        "PORT": "3000",
        "HOST": "localhost",
        "NODE_ENV": "development",
        "STOCK_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

##### 从GitHub Packages安装的方法

这个MCP服务器通过GitHub Packages作为私有npm注册表发布。按照以下步骤进行安装：

1. 创建或编辑`.npmrc`文件以进行身份验证设置：

```
@sakura-ku:registry=https://npm.pkg.github.com
//npm.pkg.github.com/:_authToken=${NPM_TOKEN}
```

2. 将GitHub个人访问令牌设置为环境变量`NPM_TOKEN`：

```bash
# Windowsの場合
$env:NPM_TOKEN="your_github_token"

# macOS/Linuxの場合
export NPM_TOKEN="your_github_token"
```

3. 安装包：

```bash
npm install @sakura-ku/grobal-mcp-stock-server
```

4. Cursor IDE中的设置示例：

```json
{
  "mcpServers": {
    "global-stock-server": {
      "command": "npx",
      "args": ["@sakura-ku/grobal-mcp-stock-server"],
      "env": {
        "PORT": "3000",
        "HOST": "localhost",
        "STOCK_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

更多详细设置方法请参考管理私有npm注册表。

#### 故障排除

对于具体的故障排除建议，请参照相关文档或联系技术支持。

- **服务器无法启动时**:
  - 移动到项目目录手动执行命令，检查错误
  - 确认依赖项已正确安装（运行 `npm install`）
  - 检查 TypeScript 版本是否匹配

- **找不到工具时**:
  - 确认服务器是否正常启动
  - 检查日志输出中注册的工具名称
  - 如有必要，使用 `npm run dev` 以调试模式启动服务器

# 开发者指南

## 项目结构

```
grobal_mcp_stock_server/
├── build/                # コンパイルされたJavaScriptファイル
├── src/
│   ├── __tests__/        # 統合テストとテストユーティリティ
│   ├── config/           # 設定ファイル
│   ├── data/             # データモデルとストレージ
│   ├── errors/           # カスタムエラークラス
│   ├── services/         # 外部APIとの連携サービス
│   ├── tools/            # MCPツール実装
│   │   └── __tests__/    # ツールユニットテスト
│   ├── types/            # TypeScript型定義
│   └── index.ts          # メインサーバーエントリーポイント
├── package.json          # プロジェクト設定
├── tsconfig.json         # TypeScript設定
└── README.md             # プロジェクトドキュメント
```

## 设置开发环境

1. 安装开发依赖:
```bash
   npm install
```

2. 在开发模式下启动服务器:
```bash
   npm run dev
```

## 开发工作流程

- 以监视模式启动 TypeScript 编译器: `npm run dev`
- 执行代码静态分析: `npm run lint`
- 自动修复静态分析问题: `npm run lint:fix`
- 运行测试: `npm test`

## 可用脚本

在 package.json 中定义的脚本详细说明:

### 构建脚本
- `build`: 编译 TypeScript 代码并输出到 dist 目录
- `build:dev`: 为开发环境构建，包含源映射
- `build:prod`: 为生产环境构建，不包含源映射
- `clean`: 删除 dist 目录进行清理
- `prebuild`: 在构建前自动执行 clean 脚本

### 服务器启动脚本
- `start`: 启动已编译的服务器
- `start:dev`: 以开发环境配置启动服务器
- `start:prod`: 以生产环境配置启动服务器
- `dev`: 开发模式，监视源代码更改，并自动重建和重启

### 代码质量控制脚本
- `lint`: 使用 ESLint 对 TypeScript 代码进行静态分析
- `lint:fix`: 使用 ESLint 自动修正代码问题

### 测试脚本
- `test`: 使用 Jest 运行所有测试
- `test:watch`: 以监视模式运行测试，在文件变更时重新运行
- `test:coverage`: 生成测试覆盖率报告
- `test:ci`: 以 CI 环境配置运行测试
- `test:unit`: 仅运行单元测试
- `test:integration`: 仅运行集成测试
- `test:services`: 仅运行服务测试
- `test:debug`: 以调试模式运行测试

### 部署与打包
- `deploy:staging`: 部署到预发布环境
- `deploy:production`: 部署到生产环境
- `publish:package`: 将包发布到 npm 注册表
- `prepare:package`: 在打包前执行生产构建并创建 tarball
- `prepublishOnly`: 在发布包之前执行生产构建

## 许可证

ISC

## 贡献

如果您有兴趣为这个项目做贡献，请发送拉取请求。

**官方网站：** [https://github.com/sakura-ku/grobal_mcp_stock_server](https://github.com/sakura-ku/grobal_mcp_stock_server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`finance`
- 标签：`finance`, `search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npm`
- 参数：`run dev`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/sakura-ku-grobal-stock.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
