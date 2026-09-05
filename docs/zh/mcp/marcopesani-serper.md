---
title: "Serper MCP多参数搜索服务器"
description: "该 Serper MCP 服务器支持搜索和网页抓取，并且兼容 Serper API 引入的所有最新参数，例如位置参数。"
---

# Serper MCP多参数搜索服务器

该 Serper MCP 服务器支持搜索和网页抓取，并且兼容 Serper API 引入的所有最新参数，例如位置参数。

# Serper 搜索和抓取 MCP 服务器
[Smithery](https://smithery.ai/server/@marcopesani/mcp-server-serper)

这是一个基于 TypeScript 的 MCP 服务器，使用 Serper API 提供网络搜索和网页抓取功能。该服务器与 Claude Desktop 集成，以实现强大的网络搜索和内容提取功能。

  

## 功能

### 工具

- `google_search` - 通过 Serper API 进行网络搜索
  - 丰富的搜索结果，包括自然搜索结果、知识图谱、“人们也问”以及相关搜索
  - 支持地区和语言定位
  - 可选参数包括位置、分页、时间过滤器和自动更正
  - 支持高级搜索操作符：
    - `site`: 将结果限制在特定域内
    - `filetype`: 限制为特定文件类型（例如 'pdf', 'doc'）
    - `inurl`: 搜索 URL 中包含某个词的页面
    - `intitle`: 搜索标题中包含某个词的页面
    - `related`: 查找相似网站
    - `cache`: 查看 Google 缓存的特定 URL 版本
    - `before`: 日期之前 (格式：YYYY-MM-DD)
    - `after`: 日期之后 (格式：YYYY-MM-DD)
    - `exact`: 精确短语匹配
    - `exclude`: 从搜索结果中排除的术语
    - `or`: 替代术语 (OR 操作符)
  
- `scrape` - 从网页中提取内容
  - 获取纯文本和可选的 markdown 内容
  - 包括 JSON-LD 和头部元数据
  - 保持文档结构

## 要求

- Node.js >= 18
- Serper API 密钥（设置为 `SERPER_API_KEY` 环境变量）

## 开发

安装依赖项：
```bash
npm install
```

构建服务器：
```bash
npm run build
```

开发时自动重建：
```bash
npm run watch
```

运行测试：
```bash
npm test                  # Run all tests
npm run test:watch       # Run tests in watch mode
npm run test:coverage    # Run tests with coverage
npm run test:integration # Run integration tests
```

### 环境变量

在根目录创建一个 `.env` 文件：

```
SERPER_API_KEY=your_api_key_here
```

### 调试

由于 MCP 服务器通过 stdio 通信，调试可能具有挑战性。我们建议使用 [MCP Inspector](https://github.com/modelcontextprotocol/inspector)，它作为包脚本提供：

```bash
npm run inspector
```

Inspector 将提供一个 URL 以便您在浏览器中访问调试工具。

## 安装

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@marcopesani/mcp-server-serper) 自动为 Claude Desktop 安装 Serper Search and Scrape：

```bash
npx -y @smithery/cli install @marcopesani/mcp-server-serper --client claude
```

### Claude Desktop

在以下位置添加服务器配置：
- MacOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "serper-search": {
      "command": "npx",
      "args": ["-y", "serper-search-scrape-mcp-server"],
      "env": {
        "SERPER_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

### Cline

1. 打开 Cline 扩展设置
2. 打开 "MCP Servers" 标签
3. 点击 "Configure MCP Servers"
4. 添加服务器配置：

```json
{
  "mcpServers": {
    "github.com/marcopesani/mcp-server-serper": {
      "command": "npx",
      "args": ["-y", "serper-search-scrape-mcp-server"],
      "env": {
        "SERPER_API_KEY": "your_api_key_here"
      },
      "disabled": false,
      "autoApprove": ["google_search", "scrape"]
    }
  }
}
```

其他 Cline 配置选项：
- `disabled`: 设置为 `false` 以启用服务器
- `autoApprove`: 不需要每次使用都显式批准的工具列表

### Cursor

1. 打开光标设置
2. 打开“功能”设置
3. 在“MCP 服务器”部分，点击“添加新的 MCP 服务器”
4. 选择一个名称，并将“类型”设置为“命令”
5. 在“命令”字段中，输入以下内容：

```
env SERPER_API_KEY=your_api_key_here npx -y serper-search-scrape-mcp-server
```

### Docker

您也可以使用 Docker 运行服务器。首先，构建镜像：

```bash
docker build -t mcp-server-serper .
```

然后使用您的 Serper API 密钥运行容器：

```bash
docker run -e SERPER_API_KEY=your_api_key_here mcp-server-serper
```

或者，如果您在 `.env` 文件中有环境变量：

```bash
docker run --env-file .env mcp-server-serper
```

对于开发，您可能希望将源代码作为卷挂载：

```bash
docker run -v $(pwd):/app --env-file .env mcp-server-serper
```

注意：请确保将 `your_api_key_here` 替换为您实际的 Serper API 密钥。

**官方网站：** [https://github.com/marcopesani/mcp-server-serper](https://github.com/marcopesani/mcp-server-serper)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`browser`
- 标签：`browser automation`, `search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y serper-search-scrape-mcp-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/marcopesani-serper.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
