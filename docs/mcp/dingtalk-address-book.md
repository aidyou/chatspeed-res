---
title: "Address-Book"
description: "1.什么是钉钉通讯录（应用授权） MCP Server？ 钉钉通讯录（应用授权）是 开放平台官方提供的 MCP，支持获取组织架构信息、查询成员详情、获取部门列表、以及管理成员与部门关系等操作。 2.如何使用钉钉通讯录（应用授权） MCP Server？ 钉钉已为你部署好了云端的钉钉通讯录（应用授权）MCP 服务。你可以直接在对话输入框中添加并使用。 MCP Tool 有： getuserinfo，…"
---

# Address-Book

1.什么是钉钉通讯录（应用授权） MCP Server？ 钉钉通讯录（应用授权）是 开放平台官方提供的 MCP，支持获取组织架构信息、查询成员详情、获取部门列表、以及管理成员与部门关系等操作。 2.如何使用钉钉通讯录（应用授权） MCP Server？ 钉钉已为你部署好了云端的钉钉通讯录（应用授权）MCP 服务。你可以直接在对话输入框中添加并使用。 MCP Tool 有： getuserinfo，…

# DingTalk Address Book (App Authorization) MCP Server

## 1. What is the DingTalk Address Book (App Authorization) MCP Server?

The DingTalk Address Book (App Authorization) is an MCP provided by the official open platform, supporting operations such as obtaining organizational structure information, querying member details, getting department lists, and managing the relationships between members and departments.

## 2. How to Use the DingTalk Address Book (App Authorization) MCP Server?

DingTalk has already deployed the cloud-based DingTalk Address Book (App Authorization) MCP service for you. You can directly add and use it in the conversation input box.

### MCP Tools

- **`get_user_info`**  
  Obtain basic information of a specified user (such as name, employee ID, email, phone number, etc.).

- **`list_departments`**  
  List all departments within the enterprise or the sub-departments of a specified department.

- **`get_department_detail`**  
  Get detailed information about a specified department (including department name, head, number of members, etc.).

- **`list_department_members`**  
  Paginate and obtain all member information under a specified department.

## User Cases

- Query the list of all members and their contact information under the "Technology Department" in the company.
- Obtain detailed information about the employee "Li Si", including the department they belong to, position, and start date.
- List all first-level departments in the corporate organizational structure and display the head of each department.
- Get the total number of members and the list of member names under the "Sales Department" (Department ID: `10086`).

**Official site: ** [https://mcp.dingtalk.com/#/detail?mcpId=2400&detailType=marketMcpDetail](https://mcp.dingtalk.com/#/detail?mcpId=2400&detailType=marketMcpDetail)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `files`
- Tags: `developer tools`, `file systems`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `mcp-server-fetch`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/dingtalk-address-book.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
