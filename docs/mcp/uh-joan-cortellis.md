---
title: "Cortellis药物搜索服务"
description: "启用在Cortellis数据库中搜索药物和探索本体论术语的功能，提供对全面的药物开发状态信息的访问，并以结构化的JSON响应形式呈现。"
---

# Cortellis药物搜索服务

启用在Cortellis数据库中搜索药物和探索本体论术语的功能，提供对全面的药物开发状态信息的访问，并以结构化的JSON响应形式呈现。

# Cortellis MCP 服务器

用于在Cortellis数据库中搜索药物和探索本体术语的MCP服务器。

## 安装

```bash
# Using npm
npm install @uh-joan/cortellis-mcp-server
```

## 快速开始

1. 设置您的环境变量：
```env
CORTELLIS_USERNAME=your_username
CORTELLIS_PASSWORD=your_password
USE_HTTP=true  # Optional: run as HTTP server
PORT=3000      # Optional: specify port for HTTP server
```

2. 运行服务器：
```bash
# As MCP server
npx cortellis-mcp-server

# As HTTP server
USE_HTTP=true PORT=3000 npx cortellis-mcp-server
```

## 工具

请注意，您提供的markdown内容中的代码块(```...```)内部的内容（如`#0`, `#1`, `#2`）没有给出具体的命令或信息。如果这些部分包含特定的命令或配置信息，请提供详细内容以便更准确地翻译。对于保持格式一致性的要求，我已将这些占位符直接保留下来。

1. `search_drugs`
   - Search for drugs in the Cortellis database
   - Optional Inputs:
     - `query` (string) - Raw search query
     - `company` (string) - Company developing the drug
     - `indication` (string) - Active indications (e.g., obesity)
     - `action` (string) - Target specific action (e.g., glucagon)
     - `phase` (string) - Development status:
       - Supports both short and descriptive formats:
         - Short format: S, DR, CU, C1-C3, PR, R, L, OL, NDR, DX, W
         - Descriptive format: "Phase 1 Clinical", "Phase 2 Clinical", "Phase 3 Clinical", "Launched", etc.
       - Supports OR/AND operators: "C2 OR C3" or "Phase 2 Clinical OR Phase 3 Clinical"
       - Examples:
         - `phase: "C3"` (short format)
         - `phase: "C2 OR C3"` (short format)
         - `phase: "Phase 2 Clinical OR Phase 3 Clinical"` (descriptive format)
         - `phase: "C2 AND C3"` (using AND operator)
       - Status codes:
         - S: Suspended
         - DR: Discovery/Preclinical
         - CU: Clinical (unknown phase)
         - C1-C3: Phase 1-3 Clinical
         - PR: Pre-registration
         - R: Registered
         - L: Launched
         - OL: Outlicensed
         - NDR: No Development Reported
         - DX: Discontinued
         - W: Withdrawn
     - `phase_terminated` (string) - Last phase before NDR/DX
       - Supports same formats and operators as `phase`
       - Examples:
         - `phase_terminated: "C2 OR CR"` (short format)
         - `phase_terminated: "C2"` (short format)
         - `phase_terminated: "Phase 2 Clinical"` (descriptive format)
         - `phase_terminated: "C2 OR C3"` (multiple phases)
     - `technology` (string) - Drug technology (e.g., small molecule)
     - `drug_name` (string) - Name of the drug
     - `country` (string) - Country of development
     - `offset` (number) - For pagination
   - Returns: JSON response with drug information and development status

2. `explore_ontology`
   - Explore taxonomy terms in the Cortellis database
   - Optional Inputs (at least one required):
     - `term` (string) - Generic search term
     - `category` (string) - Category to search within
     - `action` (string) - Target specific action
     - `indication` (string) - Disease/condition
     - `company` (string) - Company name
     - `drug_name` (string) - Drug name
     - `target` (string) - Drug target
     - `technology` (string) - Drug technology
   - Returns: JSON response with matching taxonomy terms

3. `get_drug`
   - Return the entire drug record with all available fields for a given identifier
   - Required Input:
     - `id` (string) - Drug Identifier
   - Returns: JSON response with complete drug record

4. `get_drug_swot`
   - Return SWOT analysis complementing chosen drug record
   - Required Input:
     - `id` (string) - Drug Identifier
   - Returns: JSON response with SWOT analysis for the drug

5. `get_drug_financial`
   - Return financial commentary and data (actual sales and consensus forecast)
   - Required Input:
     - `id` (string) - Drug Identifier
   - Returns: JSON response with financial data and commentary

6. `get_company`
   - Return the entire company record with all available fields for a given identifier
   - Required Input:
     - `id` (string) - Company Identifier
   - Returns: JSON response with complete company record

7. `search_companies`
   - Search for companies in the Cortellis database
   - Optional Inputs:
     - `query` (string) - Raw search query
     - `company_name` (string) - Company name to search for
     - `hq_country` (string) - Company headquarters country
     - `deals_count` (string) - Count for all distinct deals where company is principal/partner
       - Format: '20' for greater than 20 deals (default behavior)
     - `indications` (string) - Top 10 indication terms
     - `actions` (string) - Top 10 target-based action terms
     - `technologies` (string) - Top 10 technologies terms
     - `company_size` (string) - The size of a company based on market capitalization in billions USD
       - Format: '2' for greater than $2B (default behavior)
     - `status` (string) - Highest status of linked drugs
     - `offset` (number) - For pagination
   - Returns: JSON response with company information

## 特性

- 直接访问 Cortellis 药物数据库
- 全面的药物研发状态搜索
- 本体/分类术语探索
- 详细的药物信息检索
- 药物 SWOT 分析
- 财务数据和预测
- 结构化的 JSON 响应
- 对大量结果集的支持分页

## HTTP API 端点

当以 HTTP 模式运行（USE_HTTP=true）时，以下 REST 端点可用：

1. `POST /search_drugs`
   - 使用可选过滤器搜索药物
   - 请求体：包含搜索参数的 JSON 对象（参见 `search_drugs` 工具输入）

2. `POST /explore_ontology`
   - 搜索分类术语
   - 请求体：包含搜索参数的 JSON 对象（参见 `explore_ontology` 工具输入）

3. `GET /drug/:id`
   - 根据 ID 获取完整的药物记录
   - 参数：
     - `id`: 药物标识符

4. `GET /drug/:id/swot`
   - 获取药物的 SWOT 分析
   - 参数：
     - `id`: 药物标识符

5. `GET /drug/:id/financial`
   - 获取药物的财务数据和预测
   - 参数：
     - `id`: 药物标识符

6. `GET /company/:id`
   - 根据 ID 获取完整的公司记录
   - 参数：
     - `id`: 公司标识符

7. `POST /search_companies`
   - 使用可选过滤器搜索公司
   - 请求体：包含搜索参数的 JSON 对象（参见 `search_companies` 工具输入）

## 设置

### 环境变量
服务器需要 Cortellis API 凭证：

```env
CORTELLIS_USERNAME=your_username
CORTELLIS_PASSWORD=your_password
```

### 在 Claude Desktop 上安装
开始之前，请确保您的桌面上已安装 [Node.js](https://nodejs.org/) 以便使用 `npx`。
1. 转到：设置 > 开发者 > 编辑配置

2. 将以下内容添加到您的 `claude_desktop_config.json` 文件中：

```json
{
  "mcpServers": {
    "cortellis": {
      "command": "npx",
      "args": [
        "-y",
        "@uh-joan/cortellis-mcp-server"
      ],
      "env": {
        "CORTELLIS_USERNAME": "your_username",
        "CORTELLIS_PASSWORD": "your_password"
      }
    }
  }
}
```

3. 重启 Claude Desktop 并开始探索药物开发数据！

## 构建（针对开发者）

```bash
git clone https://github.com/uh-joan/cortellis-mcp-server.git
cd cortellis-mcp-server
npm install
npm run build
```

对于本地开发：
```bash
# Copy example environment file
cp .env.example .env

# Edit .env with your credentials
vim .env  # or use your preferred editor

# Start the server
npm run start
```

## Docker

```bash
docker build -t cortellis-mcp-server .
docker run -i --env-file .env cortellis-mcp-server
```

## 许可证

此 MCP 服务器根据 MIT 许可证授权。

## 免责声明

Cortellis™ 是 Clarivate Analytics 的商业产品和商标。此 MCP 服务器需要有效的 Cortellis API 凭证才能运行。要获取凭证并了解有关 Cortellis 的更多信息，请访问 [Clarivate 的 Cortellis 页面](https://clarivate.com/products/cortellis/)。

此项目与 Clarivate Analytics 无关，也未得到其认可或赞助。所有产品名称、徽标和品牌均为其各自所有者的财产。

## 贡献

欢迎贡献！请随时提交 Pull Request。对于重大更改，请先打开一个问题来讨论您想要进行的更改。

## 版本控制

我们使用 [SemVer](http://semver.org/) 进行版本控制。有关可用版本，请参阅 [此存储库上的标签](https://github.com/uh-joan/cortellis-mcp-server/tags)。

**官方网站：** [https://github.com/uh-joan/mcp-server-cortellis](https://github.com/uh-joan/mcp-server-cortellis)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`research and data`, `databases`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @uh-joan/cortellis-mcp-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/uh-joan-cortellis.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
