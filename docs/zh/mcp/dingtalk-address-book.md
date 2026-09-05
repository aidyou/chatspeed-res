---
title: "通讯录"
description: "1.什么是钉钉通讯录（应用授权） MCP Server？ 钉钉通讯录（应用授权）是 开放平台官方提供的 MCP，支持获取组织架构信息、查询成员详情、获取部门列表、以及管理成员与部门关系等操作。 2.如何使用钉钉通讯录（应用授权） MCP Server？ 钉钉已为你部署好了云端的钉钉通讯录（应用授权）MCP 服务。你可以直接在对话输入框中添加并使用。 MCP Tool 有： getuserinfo，…"
---

# 通讯录

1.什么是钉钉通讯录（应用授权） MCP Server？ 钉钉通讯录（应用授权）是 开放平台官方提供的 MCP，支持获取组织架构信息、查询成员详情、获取部门列表、以及管理成员与部门关系等操作。 2.如何使用钉钉通讯录（应用授权） MCP Server？ 钉钉已为你部署好了云端的钉钉通讯录（应用授权）MCP 服务。你可以直接在对话输入框中添加并使用。 MCP Tool 有： getuserinfo，…

# 钉钉通讯录（应用授权）MCP Server

## 1. 什么是钉钉通讯录（应用授权） MCP Server？

钉钉通讯录（应用授权）是开放平台官方提供的 MCP，支持获取组织架构信息、查询成员详情、获取部门列表，以及管理成员与部门关系等操作。

## 2. 如何使用钉钉通讯录（应用授权） MCP Server？

钉钉已为你部署好了云端的钉钉通讯录（应用授权）MCP 服务。你可以直接在对话输入框中添加并使用。

### MCP Tools

- **`get_user_info`**  
  获取指定用户的基本信息（如姓名、工号、邮箱、手机号等）。

- **`list_departments`**  
  列出企业内所有部门或指定部门的子部门列表。

- **`get_department_detail`**  
  获取指定部门的详细信息（包括部门名称、负责人、成员数量等）。

- **`list_department_members`**  
  分页获取指定部门下的所有成员信息。

## 用户使用案例

- 查询公司 “技术部” 下的所有成员名单及其联系方式。
- 获取员工 “李四” 的详细信息，包括所属部门、职位和入职时间。
- 列出企业组织架构中的所有一级部门，并展示每个部门的负责人。
- 获取 “销售部”（部门 ID: `10086`）下的成员总数及成员姓名列表。

**官方网站：** [https://mcp.dingtalk.com/#/detail?mcpId=2400&detailType=marketMcpDetail](https://mcp.dingtalk.com/#/detail?mcpId=2400&detailType=marketMcpDetail)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`files`
- 标签：`developer tools`, `file systems`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`mcp-server-fetch`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/dingtalk-address-book.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
