---
title: "tomtom位置服务"
description: "TomTom开源的位置服务MCP TomTom的MCP（Map and Content Platform）是一个开源项目，旨在提供一系列位置相关的服务。该项目允许开发者利用TomTom的数据和服务来构建自己的应用程序。 特性 - 地图渲染：使用矢量瓦片技术，支持自定义样式。 - 搜索与地理编码：快速准确地查找地址和地点。 - 路线规划：提供多种交通方式下的最优路径计算。 - 实时交通信息：获取最新…"
---

# tomtom位置服务

TomTom开源的位置服务MCP TomTom的MCP（Map and Content Platform）是一个开源项目，旨在提供一系列位置相关的服务。该项目允许开发者利用TomTom的数据和服务来构建自己的应用程序。 特性 - 地图渲染：使用矢量瓦片技术，支持自定义样式。 - 搜索与地理编码：快速准确地查找地址和地点。 - 路线规划：提供多种交通方式下的最优路径计算。 - 实时交通信息：获取最新…

---

# TomTom MCP 服务器

**TomTom MCP Server** 通过提供对 TomTom 位置服务的无缝访问，简化了地理空间开发。这些服务包括搜索、路线规划、交通和静态地图数据。它能够将精确的地理位置数据轻松集成到 AI 工作流和开发环境中。

---

## 快速开始

### 先决条件
- Node.js 22 或更高版本
- TomTom API 密钥

**如何获取 TomTom API 密钥**：
1.  在 [TomTom 开发者门户](https://developer.tomtom.com/) 上创建一个开发者帐户。
2.  在左侧菜单中转到 **API & SDK Keys**。
3.  点击 **红色的 Create Key** 按钮。
4.  选择所有可用的 API 以确保完全访问权限，为您的密钥分配一个名称，然后点击 **Create**。

更多详细信息，请访问 [TomTom API 密钥管理文档](https://developer.tomtom.com/platform/documentation/dashboard/api-key-management)。

### 安装
```bash
# 安装到本地项目
npm install @tomtom-org/tomtom-mcp@latest

# 或者直接运行而无需安装
npx @tomtom-org/tomtom-mcp@latest
```
---

### 配置
使用以下方法之一设置您的 TomTom API 密钥：

```bash
# 选项 1：使用 .env 文件（推荐）
echo "TOMTOM_API_KEY=你的_api_密钥" > .env

# 选项 2：环境变量 (Linux/macOS)
export TOMTOM_API_KEY=你的_api_密钥
# Windows CMD: set TOMTOM_API_KEY=你的_api_密钥
# Windows PowerShell: $env:TOMTOM_API_KEY="你的_api_密钥"

# 选项 3：作为 CLI 参数传递
npx @tomtom-org/tomtom-mcp@latest --key 你的_api_密钥
```
---

### 用法
```bash
# 启动 MCP 服务器
npx @tomtom-org/tomtom-mcp@latest
# 获取帮助
npx @tomtom-org/tomtom-mcp@latest --help
```

---

## 集成指南

TomTom MCP Server 可以轻松集成到各种 AI 开发环境和工具中。

这些指南帮助您将 MCP 服务器与您的工具和环境集成：
- [Claude Desktop 设置](https://github.com/tomtom-international/tomtom-mcp/blob/HEAD/docs/claude-desktop-setup.md) - 配置 Claude Desktop 以使用 TomTom MCP 服务器的说明
- [VS Code 设置](https://github.com/tomtom-international/tomtom-mcp/blob/HEAD/docs/vscode-setup.md) - 在 Visual Studio Code 中设置开发环境
- [Cursor AI 集成](https://github.com/tomtom-international/tomtom-mcp/blob/HEAD/docs/cursor-setup.md) - 将 TomTom MCP 服务器与 Cursor AI 集成的指南
- [WinSurf 集成](https://github.com/tomtom-international/tomtom-mcp/blob/HEAD/docs/windsurf-setup.md) - 配置 WindSurf 使用 TomTom MCP 服务器的说明
- [Smolagents 集成](https://github.com/tomtom-international/tomtom-mcp/blob/HEAD/docs/smolagents/smolagents-setup.md) - 展示如何将 Smolagents AI 代理连接到 TomTom MCP 服务器的示例。

---

## 可用工具

| 工具 | 描述 | 文档 |
|------|-------------|---------------|
| `tomtom-geocode` | 将地址转换为坐标，提供全球覆盖 | https://developer.tomtom.com/geocoding-api/documentation/geocode |
| `tomtom-reverse-geocode` |  根据 GPS 坐标获取地址 | https://developer.tomtom.com/reverse-geocoding-api/documentation/reverse-geocode |
| `tomtom-fuzzy-search` | 智能搜索，支持容错（拼写错误） | https://developer.tomtom.com/search-api/documentation/search-service/fuzzy-search |
| `tomtom-poi-search` | 查找特定的商业类别（兴趣点） | https://developer.tomtom.com/search-api/documentation/search-service/points-of-interest-search |
| `tomtom-nearby` | 发现指定半径内的服务 | https://developer.tomtom.com/search-api/documentation/search-service/nearby-search |
| `tomtom-routing` | 计算位置之间的最优路线 | https://developer.tomtom.com/routing-api/documentation/tomtom-maps/calculate-route |
| `tomtom-waypoint-routing` | 多站点路线规划 | https://developer.tomtom.com/routing-api/documentation/tomtom-maps/calculate-route |
| `tomtom-reachable-range` | 根据时间/距离确定覆盖范围区域 | https://developer.tomtom.com/routing-api/documentation/tomtom-maps/calculate-reachable-range |
| `tomtom-traffic` | 实时交通事件数据 | https://developer.tomtom.com/traffic-api/documentation/traffic-incidents/traffic-incidents-service  |
| `tomtom-static-map` | 生成自定义地图图像 | https://developer.tomtom.com/map-display-api/documentation/raster/static-image |

---
## 贡献与本地开发

### 设置
```bash
git clone  # 克隆代码库（请替换为实际地址）

cd tomtom-mcp # 进入项目目录

npm install # 安装依赖

cp .env.example .env      # 复制环境变量示例文件，并在 .env 中添加您的 API 密钥

npm run build             # 构建 TypeScript 文件

node ./bin/tomtom-mcp.js   # 启动 MCP 服务器
```

### 测试
```bash
npm run build               # 构建 TypeScript
npm test                    # 运行所有测试
npm run test:unit           # 仅运行单元测试
npm run test:comprehensive  # 运行集成测试
```
---

### 测试要求
⚠️ **重要提示**：所有测试都需要在 `.env` 文件中提供有效的 API 密钥，因为它们会进行真实的 API 调用（非模拟）。这将消耗您的 API 配额。

### 项目结构
```
src/
├── tools/             # MCP 工具定义
├── services/          # TomTom API 包装器
├── schemas/           # 验证模式
├── utils/             # 工具函数
└── createServer.ts    # MCP 服务器创建逻辑
└── index.ts           # 主入口点
```
---
## 故障排除

### API 密钥问题
```bash
# Linux/macOS 检查环境变量
echo $TOMTOM_API_KEY
# Windows CMD: echo %TOMTOM_API_KEY%
# Windows PowerShell: echo $env:TOMTOM_API_KEY
```

### 测试失败
```bash
ls -la .env          # 验证 .env 文件是否存在 (Linux/macOS)
# Windows: dir .env
cat .env             # 检查 API 密钥 (Linux/macOS)
# Windows: type .env
```

### 构建问题
```bash
npm run build            # 重新构建
npm cache clean --force  # 清除缓存
```
---

**官方网站：** [https://github.com/tomtom-international/tomtom-mcp.git](https://github.com/tomtom-international/tomtom-mcp.git)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`location services`, `地图服务`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @tomtom-org/tomtom-mcp@latest`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/nanago-tomtom-maps.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
