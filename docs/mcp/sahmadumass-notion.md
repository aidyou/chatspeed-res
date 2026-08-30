---
title: "Notion MCP 服务器"
description: "一种模型上下文协议服务器，使克劳德和其他大型语言模型能够与Notion工作区互动，提供搜索、检索、创建和更新页面以及管理数据库等功能。"
---

# Notion MCP 服务器

一种模型上下文协议服务器，使克劳德和其他大型语言模型能够与Notion工作区互动，提供搜索、检索、创建和更新页面以及管理数据库等功能。

# Notion MCP 服务器

一个用于 Notion 集成的模型上下文协议服务器，允许 Claude 和其他大型语言模型与您的 Notion 工作区进行交互。

## 功能

- **搜索 Notion**：在您的整个 Notion 工作区中进行搜索
- **获取页面**：从特定的 Notion 页面检索内容
- **创建页面**：在您的 Notion 工作区中创建新页面
- **更新页面**：使用新内容或标题更新现有页面
- **创建数据库**：使用自定义属性创建新的数据库
- **查询数据库**：通过过滤器和排序来查询数据库
- **更新数据库条目**：更新数据库条目的属性
- **创建数据库行**：向现有的数据库添加具有自定义属性的新行

## 设置

1. **克隆此仓库**

2. **安装依赖**
```bash
   npm install
```

3. **配置您的 Notion API 密钥**
   - 在 [Notion 开发者门户](https://www.notion.so/my-integrations) 中创建一个集成
   - 复制您的 API 密钥
   - 您可以选择：
     - 编辑 `.env` 文件并将 `your_notion_api_key_here` 替换为您的实际 API 密钥，或者
     - 直接在 Claude for Desktop 的配置中传递它（推荐，见下文）

4. **构建服务器**
```bash
   npm run build
```

5. **运行服务器**
```bash
   npm start
```

## 与 Claude for Desktop 一起设置

1. 安装 Claude for Desktop（如果尚未安装）
2. 打开您的 Claude for Desktop 应用程序配置：
   - 在 macOS 上: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - 如果文件不存在，请创建该文件

3. 将 Notion 服务器添加到您的配置中：
```json
   {
     "mcpServers": {
       "notion": {
         "command": "node",
         "args": [
           "/Users/shaheerahmad/Documents/notion-mcp-server/dist/index.js",
           "--notion-api-key=YOUR_ACTUAL_API_KEY_HERE"
         ]
       }
     }
   }
```
   替换：
   - `/Users/shaheerahmad/Documents/notion-mcp-server` 为您的项目目录的完整路径
   - `YOUR_ACTUAL_API_KEY_HERE` 为您的实际 Notion API 密钥

4. 重启 Claude for Desktop

## 使用服务器

一旦连接到 Claude for Desktop，您可以通过向 Claude 提问来使用服务器，例如：

- "在我的 Notion 工作区中搜索会议笔记"
- "获取我的项目规划页面的内容"（您需要页面 ID）
- "在 Notion 中创建一个包含任务列表的新页面"
- "将我的 Notion 页面 ID 为 1aaada269d1b8003adceda69cf7bcd97 的内容更新为 'Here is some new content to add to the page.'"
- "在我的 Notion 页面 ID 为 1aaada269d1b8003adceda69cf7bcd97 中创建一个新的数据库"
- "查询我的 Notion 数据库 ID 为 1aaada269d1b8003adceda69cf7bcd97 中状态为 'Completed' 的项目"

Claude 将根据您的请求自动使用适当的工具。

### 工具使用示例

#### 搜索 Notion
```
Search for "meeting notes" in my Notion workspace
```

#### 获取页面内容
```
Get the content of my Notion page with ID 1aaada269d1b8003adceda69cf7bcd97
```

#### 创建新页面
```
Create a new page in Notion with title "Weekly Report" and content "This week we accomplished the following tasks..."
```

#### 更新现有页面
```
Update my Notion page with ID 1aaada269d1b8003adceda69cf7bcd97 with content "Adding this new information to the page."
```
您还可以更新标题：
```
Update my Notion page with ID 1aaada269d1b8003adceda69cf7bcd97 with title "New Title" and content "New content to add."
```

#### 创建新数据库
```
Create a new database in my Notion page with ID 1aaada269d1b8003adceda69cf7bcd97 with title "Task Tracker" and properties {
  "Task Name": { "title": {} },
  "Status": {
    "select": {
      "options": [
        { "name": "Not Started", "color": "red" },
        { "name": "In Progress", "color": "yellow" },
        { "name": "Completed", "color": "green" }
      ]
    }
  },
  "Priority": {
    "select": {
      "options": [
        { "name": "Low", "color": "blue" },
        { "name": "Medium", "color": "yellow" },
        { "name": "High", "color": "red" }
      ]
    }
  },
  "Due Date": { "date": {} }
}
```

#### 查询数据库
```
Query my Notion database with ID 1aaada269d1b8003adceda69cf7bcd97 with filter {
  "property": "Status",
  "select": {
    "equals": "Completed"
  }
}
```

您还可以添加排序：
```
Query my Notion database with ID 1aaada269d1b8003adceda69cf7bcd97 with sort {
  "property": "Due Date",
  "direction": "ascending"
}
```

#### 更新数据库条目

更新现有数据库条目的属性（数据库中的页面）。

```json
{
  "tool_name": "update-database-entry",
  "tool_params": {
    "pageId": "page_id_of_database_entry",
    "properties": {
      "Status": {
        "select": {
          "name": "Completed"
        }
      },
      "Priority": {
        "select": {
          "name": "High"
        }
      },
      "Due Date": {
        "date": {
          "start": "2023-12-31"
        }
      }
    }
  }
}
```

`properties` 参数应与您的数据库中特定属性类型所期望的 Notion API 结构相匹配。不同的属性类型（文本、选择、日期等）需要不同的格式。

#### 创建数据库行

向现有数据库添加具有自定义属性的新行。

```json
{
  "tool_name": "create-database-row",
  "tool_params": {
    "databaseId": "your_database_id_here",
    "properties": {
      "Name": {
        "title": [
          {
            "text": {
              "content": "New Task"
            }
          }
        ]
      },
      "Status": {
        "select": {
          "name": "Not Started"
        }
      },
      "Priority": {
        "select": {
          "name": "Medium"
        }
      },
      "Due Date": {
        "date": {
          "start": "2023-12-15"
        }
      },
      "Notes": {
        "rich_text": [
          {
            "text": {
              "content": "This is a new task created via the API"
            }
          }
        ]
      }
    }
  }
}
```

`properties` 参数必须包括数据库所需的所有必需属性，并遵循每个属性类型的 Notion API 结构。

## 故障排除

- 如果工具未显示，请检查 Claude for Desktop 的日志：
```bash
  tail -n 20 -f ~/Library/Logs/Claude/mcp*.log
```

- 确保您的 Notion API 密钥设置正确，并且您的集成已被授予访问您想要交互的页面的权限。

- 如果在日志中看到 "Unexpected token" 错误，很可能是 console.log 语句干扰了 MCP 协议。此版本的服务器已更新以避免这些问题。

## 未来改进

- 添加数据库查询功能
- 实现更好的内容格式化
- 增加对更多块类型的支持

**官方网站：** [https://github.com/SAhmadUmass/notion-mcp-server](https://github.com/SAhmadUmass/notion-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`memory`
- 标签：`note taking`, `databases`, `knowledge and memory`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`/Users/shaheerahmad/Documents/notion-mcp-server/dist/index.js --notion-api-key=YOUR_ACTUAL_API_KEY_HERE`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/sahmadumass-notion.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
