---
title: "dingtalk-mcp"
description: "DingTalk MCP Server. Features: DingTalk address book, department management, bot message sending/DING, corporate culture honors, to-dos, calendar, check-in, work notifications, app management, service…"
---

# dingtalk-mcp

DingTalk MCP Server. Features: DingTalk address book, department management, bot message sending/DING, corporate culture honors, to-dos, calendar, check-in, work notifications, app management, service…

# DingTalk MCP Server

## Features
- DingTalk address book
- DingTalk department management
- DingTalk bot message sending/DING
- DingTalk corporate culture honors
- DingTalk to-dos
- DingTalk calendar
- DingTalk check-in
- DingTalk work notifications
- DingTalk app management
- DingTalk service window
- DingTalk project management
- DingTalk reports

## How to use
```json
{
   "mcpServers": {
      "dingtalk-mcp": {
         "command": "npx",
         "args": [
            "-y",
            "dingtalk-mcp@latest"
         ],
         "env": {
            "DINGTALK_Client_ID": "your dingtalk client id",
            "DINGTALK_Client_Secret": "your dingtalk client secret",
           "ACTIVE_PROFILES": "dingtalk-contacts,dingtalk-calendar"
         }
      }
   }
}
```
### Environment variable description
1. DINGTALK_Client_ID
2. DINGTALK_Client_Secret
3. ACTIVE_PROFILES: which DingTalk MCP services to activate, comma-separated; if ALL, activate everything. Optional set:

| ProfileId                   | Description        | Permission                                       |
|-----------------------------|--------------------|--------------------------------------------------|
| dingtalk-contacts           | DingTalk address book, activated by default | qyapi_addresslist_search   qyapi_get_member |
| dingtalk-department         | DingTalk department management | qyapi_get_department_list qyapi_get_department_member |
| dingtalk-robot-send-message | DingTalk bot message sending/DING, activated by default | requires in-enterprise bot message permission Premium.Ding.Write |
| dingtalk-honor              | DingTalk corporate culture honors | OrgCulture.Honor.Read |
| dingtalk-tasks              | DingTalk to-dos | Todo.Todo.Write Todo.Todo.Read |
| dingtalk-calendar           | DingTalk calendar | Calendar.Event.Write Calendar.Event.Read Calendar.EventSchedule.Read |
| dingtalk-checkin            | DingTalk check-in | qyapi_checkin_read |
| dingtalk-notice             | DingTalk work notifications | |
| dingtalk-app-manage         | DingTalk app management | qyapi_microapp_manage qyapi_get_microapp_list |
| dingtalk-service-window     | DingTalk service window | OfficialAccount.Message.Send OfficialAccount.Contact.Read OfficialAccount.Account.Read |
| dingtalk-teambition         | DingTalk project management | Project.Project.Write.All Project.Project.Read.All Project.Task.Write.All Project.Task.Read.All |
| dingtalk-report             | DingTalk reports | qyapi_report_statistics qyapi_report_manage qyapi_report_query |

4. ROBOT_CODE: the bot code used to send messages/DING
5. ROBOT_ACCESS_TOKEN: the group custom bot ACCESS_TOKEN, used to send messages with a custom bot
6. DINGTALK_AGENT_ID: used to send work notifications

### How to get the DingTalk Client ID and Client Secret
1. [Become a DingTalk developer](https://open.dingtalk.com/document/orgapp/obtain-developer-permissions)
2. [Create an app](https://open.dingtalk.com/document/orgapp/create-an-application)
3. Go to the app detail page - Credentials & Basic Info, and get the Client ID and Client Secret
4. [Add permissions](https://open.dingtalk.com/document/orgapp/add-api-permission), adding the relevant permission points based on the enabled MCP services

### How to get ROBOT_CODE
1. See [How to create a bot](https://open.dingtalk.com/document/orgapp/the-creation-and-installation-of-the-application-robot-in-the)

## Support

- Help docs: https://open.dingtalk.com/document/ai-dev/dingtalk-server-api-mcp-overview
- DingTalk Open Platform: https://open.dingtalk.com
- MCP protocol: https://modelcontextprotocol.io
- Welcome to join the DingTalk MCP community group
  ![Welcome to join the DingTalk MCP community group](/mcp-assets/716fc6db3a69b27b109dea933f579009.png)

**Official site: ** [https://github.com/open-dingtalk/dingtalk-mcp](https://github.com/open-dingtalk/dingtalk-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `communication`
- Tags: `communication`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y dingtalk-mcp@latest`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/open-dingtalk-dingtalk.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
