---
title: "Outlook日历管理器"
description: "Outlook日历MCP使克劳德能够直接管理Windows系统上的Microsoft Outlook日历，提供了一种注重隐私的解决方案，可将所有数据保留在本地。用户可以查看事件、创建会议、查找空闲时间段以及管理多个日历，而无需让数据离开他们的机器。"
---

# Outlook日历管理器

Outlook日历MCP使克劳德能够直接管理Windows系统上的Microsoft Outlook日历，提供了一种注重隐私的解决方案，可将所有数据保留在本地。用户可以查看事件、创建会议、查找空闲时间段以及管理多个日历，而无需让数据离开他们的机器。

# Outlook 日历 MCP 工具

这是一个模型上下文协议（MCP）服务器，允许 Claude 访问和管理您的本地 Microsoft Outlook 日历（仅限 Windows）。

[![License: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)

## 功能

- **查看日历事件**：列出指定日期范围内的事件，查看事件详情，检查参与者状态
- **管理日历事件**：创建新的事件和会议，更新现有事件
- **日历智能**：查找可用时间以安排会议，确定最佳会议时间
- **多日历支持**：访问您 Outlook 配置文件中的不同日历

## 前提条件

- Windows 操作系统
- 安装了 Microsoft Outlook 桌面客户端
- Node.js (版本 14.x 或更高)
- npm (随 Node.js 一起提供)

## 安装

### 选项 1：从 npm 安装

```bash
npm install -g outlook-calendar-mcp
```

您也可以直接使用 npx 运行而无需安装：

```bash
npx outlook-calendar-mcp
```

### 选项 2：从源代码安装

1. 克隆此仓库或下载源代码
2. 安装依赖项：

```bash
npm install
```

3. 运行服务器：

```bash
npm start
```

## MCP 服务器配置

要将此工具与 Claude 一起使用，需要将其添加到您的 MCP 设置配置文件中。

### 对于 Claude 桌面应用程序

在您的 Claude 桌面配置文件（位于 `%APPDATA%\Claude\claude_desktop_config.json`）中添加以下内容：

#### 如果通过 npm 全局安装：

```json
{
  "mcpServers": {
    "outlook-calendar": {
      "command": "outlook-calendar-mcp",
      "args": [],
      "env": {}
    }
  }
}
```

#### 使用 npx（不安装）：

```json
{
  "mcpServers": {
    "outlook-calendar": {
      "command": "npx",
      "args": ["-y", "outlook-calendar-mcp"],
      "env": {}
    }
  }
}
```

#### 如果从源代码安装：

```json
{
  "mcpServers": {
    "outlook-calendar": {
      "command": "node",
      "args": ["path/to/outlook-calendar-mcp/src/index.js"],
      "env": {}
    }
  }
}
```

### 对于 Claude VSCode 扩展

在您的 Claude VSCode 扩展 MCP 设置文件（位于 `%APPDATA%\Code\User\globalStorage\saoudrizwan.claude-dev\settings\cline_mcp_settings.json`）中添加以下内容：

#### 如果通过 npm 全局安装：

```json
{
  "mcpServers": {
    "outlook-calendar": {
      "command": "outlook-calendar-mcp",
      "args": [],
      "env": {}
    }
  }
}
```

#### 使用 npx（不安装）：

```json
{
  "mcpServers": {
    "outlook-calendar": {
      "command": "npx",
      "args": ["-y", "outlook-calendar-mcp"],
      "env": {}
    }
  }
}
```

#### 如果从源代码安装：

```json
{
  "mcpServers": {
    "outlook-calendar": {
      "command": "node",
      "args": ["path/to/outlook-calendar-mcp/src/index.js"],
      "env": {}
    }
  }
}
```

对于源代码安装，请将 `path/to/outlook-calendar-mcp` 替换为您实际安装此工具的路径。

## 使用

配置完成后，Claude 将可以访问以下工具：

### 列出日历事件

```
list_events
- startDate: Start date in MM/DD/YYYY format
- endDate: End date in MM/DD/YYYY format (optional)
- calendar: Calendar name (optional)
```

示例："列出我下周的日历事件"

### 创建日历事件

```
create_event
- subject: Event subject/title
- startDate: Start date in MM/DD/YYYY format
- startTime: Start time in HH:MM AM/PM format
- endDate: End date in MM/DD/YYYY format (optional)
- endTime: End time in HH:MM AM/PM format (optional)
- location: Event location (optional)
- body: Event description (optional)
- isMeeting: Whether this is a meeting with attendees (optional)
- attendees: Semicolon-separated list of attendee email addresses (optional)
- calendar: Calendar name (optional)
```

示例："周五下午 2 点与 John 关于项目提案的会议"

### 查找空闲时间段

```
find_free_slots
- startDate: Start date in MM/DD/YYYY format
- endDate: End date in MM/DD/YYYY format (optional)
- duration: Duration in minutes (optional)
- workDayStart: Work day start hour (0-23) (optional)
- workDayEnd: Work day end hour (0-23) (optional)
- calendar: Calendar name (optional)
```

示例："这周我什么时候有空进行 1 小时的会议？"

### 获取参与者状态

```
get_attendee_status
- eventId: Event ID
- calendar: Calendar name (optional)
```

示例："谁还没有回复我的团队会议邀请？"

> **重要提示**：当使用需要事件 ID 的操作（如 update_event, delete_event, get_attendee_status）时，必须使用 list_events 响应中的 `id` 字段。这是 Outlook 用来标识事件的唯一 EntryID。

### 更新日历事件

```
update_event
- eventId: Event ID to update
- subject: New event subject/title (optional)
- startDate: New start date in MM/DD/YYYY format (optional)
- startTime: New start time in HH:MM AM/PM format (optional)
- endDate: New end date in MM/DD/YYYY format (optional)
- endTime: New end time in HH:MM AM/PM format (optional)
- location: New event location (optional)
- body: New event description (optional)
- calendar: Calendar name (optional)
```

示例："将我明天的团队会议时间从下午 2 点改为下午 3 点"

### 获取日历

```
get_calendars
```

示例："显示我可用的日历"

## 安全注意事项

- 首次使用时，Outlook 可能会显示安全提示以允许脚本访问
- 该工具仅访问您的本地 Outlook 客户端，并不会将日历数据发送到外部服务器
- 所有日历操作都在您的计算机上本地执行

## 故障排除

- **Outlook 安全提示**：如果您看到 Outlook 的安全提示，您需要允许脚本访问您的 Outlook 数据
- **脚本执行策略**：如果遇到脚本执行错误，可能需要调整您的 PowerShell 执行策略
- **路径问题**：请确保 MCP 配置文件中的路径指向工具的正确位置

## 贡献

我们欢迎对 Outlook Calendar MCP 工具做出贡献！请参阅我们的[贡献指南](https://github.com/merajmehrabi/Outlook_Calendar_MCP/blob/HEAD/CONTRIBUTING.md)以了解如何开始。

通过参与此项目，您同意遵守我们的[行为准则](https://github.com/merajmehrabi/Outlook_Calendar_MCP/blob/HEAD/CODE_OF_CONDUCT.md)。

## 许可证

此项目根据 MIT 许可证许可 - 详情请参见[LICENSE](https://github.com/merajmehrabi/Outlook_Calendar_MCP/blob/HEAD/LICENSE)文件。

**官方网站：** [https://github.com/merajmehrabi/Outlook_Calendar_MCP](https://github.com/merajmehrabi/Outlook_Calendar_MCP)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`productivity`
- 标签：`calendar management`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y outlook-calendar-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/merajmehrabi-outlook-calendar.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
