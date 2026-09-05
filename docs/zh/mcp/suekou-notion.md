---
title: "Notion MCP"
description: "用于Notion API的MCP服务器，使Claude能够与Notion工作区进行交互。"
---

# Notion MCP

用于Notion API的MCP服务器，使Claude能够与Notion工作区进行交互。

# Notion MCP 服务器

Notion API 的 MCP 服务器，使 Claude 能够与 Notion 工作区进行交互。

## 设置

以下文章中详细解释了上述步骤：

- 英文版：https://dev.to/suekou/operating-notion-via-claude-desktop-using-mcp-c0h
- 日文版：https://qiita.com/suekou/items/44c864583f5e3e6325d9

1. **创建 Notion 集成**：

   - 访问 [Notion 您的集成页面](https://www.notion.so/profile/integrations)。
   - 点击“新建集成”。
   - 为您的集成命名并选择适当的权限（例如，“读取内容”，“更新内容”）。

2. **获取密钥**：

   - 从您的集成中复制“内部集成令牌”。
   - 此令牌将用于身份验证。

3. **将集成添加到您的工作区**：

   - 在 Notion 中打开您希望集成访问的页面或数据库。
   - 点击右上角的“...”按钮。
   - 点击“连接”按钮，并选择您在上面第 1 步中创建的集成。

4. **配置 Claude 桌面**：
   将以下内容添加到您的 `claude_desktop_config.json` 文件中：

```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "@suekou/mcp-notion-server"],
      "env": {
        "NOTION_API_TOKEN": "your-integration-token"
      }
    }
  }
}
```

或

```json
{
  "mcpServers": {
    "notion": {
      "command": "node",
      "args": ["your-built-file-path"],
      "env": {
        "NOTION_API_TOKEN": "your-integration-token"
      }
    }
  }
}
```

## 环境变量

- `NOTION_API_TOKEN`（必需）：您的 Notion API 集成令牌。
- `NOTION_MARKDOWN_CONVERSION`：设置为 "true" 以启用实验性的 Markdown 转换。这可以在查看内容时显著减少 token 消耗，但在尝试编辑页面内容时可能会出现问题。

## 高级配置

### Markdown 转换

默认情况下，所有响应都以 JSON 格式返回。您可以启用实验性的 Markdown 转换以减少 token 消耗：

```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "@suekou/mcp-notion-server"],
      "env": {
        "NOTION_API_TOKEN": "your-integration-token",
        "NOTION_MARKDOWN_CONVERSION": true
      }
    }
  }
}
```

或

```json
{
  "mcpServers": {
    "notion": {
      "command": "node",
      "args": ["your-built-file-path"],
      "env": {
        "NOTION_API_TOKEN": "your-integration-token",
        "NOTION_MARKDOWN_CONVERSION": true
      }
    }
  }
}
```

当 `NOTION_MARKDOWN_CONVERSION` 设置为 `"true"` 时，响应将转换为 Markdown 格式（当 `format` 参数设置为 `"markdown"` 时），使其更易于阅读，并显著减少 token 消耗。但是，由于此功能是实验性的，在尝试编辑页面内容时可能会出现问题，因为原始结构在转换过程中会丢失。

您可以通过在工具调用中将 `format` 参数设置为 `"json"` 或 `"markdown"` 来逐个请求控制格式：

- 使用 `"markdown"` 可以在仅查看内容时提高可读性
- 使用 `"json"` 当您需要修改返回的内容时

## 故障排除

如果您遇到权限错误：

1. 确保集成具有所需的权限。
2. 确认该集成已被邀请到相关的页面或数据库。
3. 确认在 `claude_desktop_config.json` 中正确设置了令牌和配置。

## 工具

所有工具都支持以下可选参数：

- `format` (字符串, "json" 或 "markdown", 默认: "markdown"): 控制响应格式。使用 "markdown" 以获得人类可读的输出，使用 "json" 以便程序化访问原始数据结构。注意：Markdown 转换仅在 `NOTION_MARKDOWN_CONVERSION` 环境变量设置为 "true" 时有效。

1. `notion_append_block_children`

   - Append child blocks to a parent block.
   - Required inputs:
     - `block_id` (string): The ID of the parent block.
     - `children` (array): Array of block objects to append.
   - Returns: Information about the appended blocks.

2. `notion_retrieve_block`

   - Retrieve information about a specific block.
   - Required inputs:
     - `block_id` (string): The ID of the block to retrieve.
   - Returns: Detailed information about the block.

3. `notion_retrieve_block_children`

   - Retrieve the children of a specific block.
   - Required inputs:
     - `block_id` (string): The ID of the parent block.
   - Optional inputs:
     - `start_cursor` (string): Cursor for the next page of results.
     - `page_size` (number, default: 100, max: 100): Number of blocks to retrieve.
   - Returns: List of child blocks.

4. `notion_delete_block`

   - Delete a specific block.
   - Required inputs:
     - `block_id` (string): The ID of the block to delete.
   - Returns: Confirmation of the deletion.

5. `notion_retrieve_page`

   - Retrieve information about a specific page.
   - Required inputs:
     - `page_id` (string): The ID of the page to retrieve.
   - Returns: Detailed information about the page.

6. `notion_update_page_properties`

   - Update properties of a page.
   - Required inputs:
     - `page_id` (string): The ID of the page to update.
     - `properties` (object): Properties to update.
   - Returns: Information about the updated page.

7. `notion_create_database`

   - Create a new database.
   - Required inputs:
     - `parent` (object): Parent object of the database.
     - `title` (array): Title of the database as a rich text array.
     - `properties` (object): Property schema of the database.
   - Returns: Information about the created database.

8. `notion_query_database`

   - Query a database.
   - Required inputs:
     - `database_id` (string): The ID of the database to query.
   - Optional inputs:
     - `filter` (object): Filter conditions.
     - `sorts` (array): Sorting conditions.
     - `start_cursor` (string): Cursor for the next page of results.
     - `page_size` (number, default: 100, max: 100): Number of results to retrieve.
   - Returns: List of results from the query.

9. `notion_retrieve_database`

   - Retrieve information about a specific database.
   - Required inputs:
     - `database_id` (string): The ID of the database to retrieve.
   - Returns: Detailed information about the database.

10. `notion_update_database`

    - Update information about a database.
    - Required inputs:
      - `database_id` (string): The ID of the database to update.
    - Optional inputs:
      - `title` (array): New title for the database.
      - `description` (array): New description for the database.
      - `properties` (object): Updated property schema.
    - Returns: Information about the updated database.

11. `notion_create_database_item`

    - Create a new item in a Notion database.
    - Required inputs:
      - `database_id` (string): The ID of the database to add the item to.
      - `properties` (object): The properties of the new item. These should match the database schema.
    - Returns: Information about the newly created item.

12. `notion_search`

    - Search pages or databases by title.
    - Optional inputs:
      - `query` (string): Text to search for in page or database titles.
      - `filter` (object): Criteria to limit results to either only pages or only databases.
      - `sort` (object): Criteria to sort the results
      - `start_cursor` (string): Pagination start cursor.
      - `page_size` (number, default: 100, max: 100): Number of results to retrieve.
    - Returns: List of matching pages or databases.

13. `notion_list_all_users`

    - List all users in the Notion workspace.
    - Note: This function requires upgrading to the Notion Enterprise plan and using an Organization API key to avoid permission errors.
    - Optional inputs:
      - start_cursor (string): Pagination start cursor for listing users.
      - page_size (number, max: 100): Number of users to retrieve.
    - Returns: A paginated list of all users in the workspace.

14. `notion_retrieve_user`

    - Retrieve a specific user by user_id in Notion.
    - Note: This function requires upgrading to the Notion Enterprise plan and using an Organization API key to avoid permission errors.
    - Required inputs:
      - user_id (string): The ID of the user to retrieve.
    - Returns: Detailed information about the specified user.

15. `notion_retrieve_bot_user`

    - Retrieve the bot user associated with the current token in Notion.
    - Returns: Information about the bot user, including details of the person who authorized the integration.

16. `notion_create_comment`

    - Create a comment in Notion.
    - Requires the integration to have 'insert comment' capabilities.
    - Either specify a `parent` object with a `page_id` or a `discussion_id`, but not both.
    - Required inputs:
      - `rich_text` (array): Array of rich text objects representing the comment content.
    - Optional inputs:
      - `parent` (object): Must include `page_id` if used.
      - `discussion_id` (string): An existing discussion thread ID.
    - Returns: Information about the created comment.

17. `notion_retrieve_comments`
    - Retrieve a list of unresolved comments from a Notion page or block.
    - Requires the integration to have 'read comment' capabilities.
    - Required inputs:
      - `block_id` (string): The ID of the block or page whose comments you want to retrieve.
    - Optional inputs:
      - `start_cursor` (string): Pagination start cursor.
      - `page_size` (number, max: 100): Number of comments to retrieve.
    - Returns: A paginated list of comments associated with the specified block or page.

## 许可

此 MCP 服务器依据 MIT 许可证进行授权。这意味着您可以在遵守 MIT 许可证的条款和条件的前提下自由使用、修改和分发该软件。更多详情，请参阅项目仓库中的 LICENSE 文件。

**官方网站：** [https://github.com/suekou/mcp-notion-server](https://github.com/suekou/mcp-notion-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`note taking`, `developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @suekou/mcp-notion-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/suekou-notion.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
