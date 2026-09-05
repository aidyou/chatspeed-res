---
title: "Cal.com日历管理器"
description: "一种MCP服务器，通过Cal.com的日历API启用日历预约的调度、更新、删除和列出功能。"
---

# Cal.com日历管理器

一种MCP服务器，通过Cal.com的日历API启用日历预约的调度、更新、删除和列出功能。

# Cal.com 日历 MCP 服务器

这是一个与 Cal.com 日历 API 集成的 MCP 服务器实现，提供了预约安排功能。

## 功能

- **添加预约**：使用参与者详细信息安排新的日历预约
- **更新预约**：修改现有预约的详细信息，如时间、备注等
- **删除预约**：取消并移除现有预约
- **列出预约**：查看特定日期范围内的已安排预约

## 工具

- **calcom_add_appointment**
  - 创建新的日历预约
  - 输入参数：
    - `eventTypeId` (数字)：Cal.com 事件类型 ID
    - `startTime` (字符串)：开始时间（ISO 格式 YYYY-MM-DDTHH:mm:ss.sssZ）
    - `endTime` (字符串)：结束时间（ISO 格式 YYYY-MM-DDTHH:mm:ss.sssZ）
    - `name` (字符串)：参与者的姓名
    - `email` (字符串)：参与者的电子邮件
    - `notes` (字符串, 可选)：预约的附加备注

- **calcom_update_appointment**
  - 更新现有的日历预约
  - 输入参数：
    - `bookingId` (数字)：要更新的 Cal.com 预约 ID
    - `startTime` (字符串, 可选)：新的开始时间（ISO 格式）
    - `endTime` (字符串, 可选)：新的结束时间（ISO 格式）
    - `notes` (字符串, 可选)：预约的新备注

- **calcom_delete_appointment**
  - 删除现有的日历预约
  - 输入参数：
    - `bookingId` (数字)：要删除的 Cal.com 预约 ID
    - `reason` (字符串, 可选)：取消原因

- **calcom_list_appointments**
  - 列出指定日期范围内的日历预约
  - 输入参数：
    - `startDate` (字符串)：开始日期（YYYY-MM-DD 格式）
    - `endDate` (字符串)：结束日期（YYYY-MM-DD 格式）

## 配置

### 获取 API 密钥
1. 注册一个 [Cal.com 账户](https://cal.com)
2. 导航到设置 > 开发者 > API 密钥
3. 生成一个新的具有适当权限的 API 密钥

### 与 Claude Desktop 一起使用
将以下内容添加到您的 `claude_desktop_config.json` 中：

### Docker

```json
{
  "mcpServers": {
    "calcom-calendar": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e",
        "CALCOM_API_KEY",
        "mcp/calcom-calendar"
      ],
      "env": {
        "CALCOM_API_KEY": "YOUR_API_KEY_HERE"
      }
    }
  }
}
```

### NPX

```json
{
  "mcpServers": {
    "calcom-calendar": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-calcom-calendar"
      ],
      "env": {
        "CALCOM_API_KEY": "YOUR_API_KEY_HERE"
      }
    }
  }
}
```

## 构建

Docker 构建：

```bash
docker build -t mcp/calcom-calendar:latest -f Dockerfile .
```

## 许可证

此 MCP 服务器根据 MIT 许可证授权。这意味着您可以自由使用、修改和分发该软件，但需遵守 MIT 许可证的条款和条件。有关更多详细信息，请参阅项目存储库中的 LICENSE 文件。

**官方网站：** [https://github.com/mumunha/cal_dot_com_mcpserver](https://github.com/mumunha/cal_dot_com_mcpserver)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`productivity`
- 标签：`calendar management`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @modelcontextprotocol/server-calcom-calendar`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/mumunha-cal-dot-com-mcpserver.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
