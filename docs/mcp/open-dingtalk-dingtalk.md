---
title: "钉钉MCP"
description: "钉钉MCP Server 🚀 功能特性 - 钉钉通讯录 - 钉钉部门管理 - 钉钉机器人发消息/DING - 钉钉企业文化荣誉 - 钉钉待办 - 钉钉日程 - 钉钉签到 - 钉钉工作通知 - 钉钉应用管理 - 钉钉服务窗 - 钉钉项目管理 - 钉钉日志 如何使用 json { \"mcpServers\": { \"dingtalk-mcp\": { \"command\": \"npx\", \"args\": [ \"-y\", \"dingtalk-mcp@latest\" ], \"env\": { \"DINGTALKClientID\":"
---

# 钉钉MCP

钉钉MCP Server 🚀 功能特性 - 钉钉通讯录 - 钉钉部门管理 - 钉钉机器人发消息/DING - 钉钉企业文化荣誉 - 钉钉待办 - 钉钉日程 - 钉钉签到 - 钉钉工作通知 - 钉钉应用管理 - 钉钉服务窗 - 钉钉项目管理 - 钉钉日志 如何使用 json { "mcpServers": { "dingtalk-mcp": { "command": "npx", "args": [ "-y", "dingtalk-mcp@latest" ], "env": { "DINGTALKClientID":

# 钉钉MCP Server

## 🚀 功能特性
- 钉钉通讯录
- 钉钉部门管理
- 钉钉机器人发消息/DING
- 钉钉企业文化荣誉
- 钉钉待办
- 钉钉日程
- 钉钉签到
- 钉钉工作通知
- 钉钉应用管理
- 钉钉服务窗
- 钉钉项目管理
- 钉钉日志

## 如何使用
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
### env环境变量说明
1. DINGTALK_Client_ID
2. DINGTALK_Client_Secret
3. ACTIVE_PROFILES，激活哪些钉钉MCP服务，逗号风格，如果是ALL则激活全部。可选集合

| ProfileId                   | Description        | Permission                                       |
|-----------------------------|--------------------|--------------------------------------------------|
| dingtalk-contacts           | 钉钉通讯录，默认激活         | qyapi_addresslist_search   qyapi_get_member	                      
| dingtalk-department         | 钉钉部门管理             |qyapi_get_department_list	qyapi_get_department_member	
| dingtalk-robot-send-message | 钉钉机器人发消息/DING，默认激活 | 需要企业内机器人发送消息权限 
Premium.Ding.Write	                                  |
| dingtalk-honor              | 钉钉企业文化荣誉           |OrgCulture.Honor.Read	OrgCulture.Honor.Read	
| dingtalk-tasks              | 钉钉待办               | Todo.Todo.Write
Todo.Todo.Read                |
| dingtalk-calendar           | 钉钉日程               |Calendar.Event.Write	Calendar.Event.Read	 Calendar.EventSchedule.Read	
| dingtalk-checkin            | 钉钉签到               |qyapi_checkin_read
| dingtalk-notice             | 钉钉工作通知             |
| dingtalk-app-manage         | 钉钉应用管理             | qyapi_microapp_manage
qyapi_get_microapp_list |
| dingtalk-service-window     | 钉钉服务窗              |    OfficialAccount.Message.Send	OfficialAccount.Contact.Read	OfficialAccount.Account.Read	                                              |
| dingtalk-teambition         | 钉钉项目管理             |  Project.Project.Write.All	Project.Project.Read.All	Project.Task.Write.All	Project.Task.Read.All	                                                |
| dingtalk-report             | 钉钉日志               | qyapi_report_statistics qyapi_report_manage	qyapi_report_query	                        |

4. ROBOT_CODE，用于发消息/DING的机器人Code
5. ROBOT_ACCESS_TOKEN，群自定义机器人ACCESS_TOKEN，用于自定义机器人发消息
6. DINGTALK_AGENT_ID 用于发送工作通知
### 如何获取钉钉Client ID和Client Secret
1. [成为钉钉开发者](https://open.dingtalk.com/document/orgapp/obtain-developer-permissions)
2. [创建应用](https://open.dingtalk.com/document/orgapp/create-an-application)
3. 进入应用详情页-凭证与基础信息，获取Client ID和Client Secret
4. [添加权限](https://open.dingtalk.com/document/orgapp/add-api-permission)，根据启用的MCP服务添加相关权限点
### 如何获取ROBOT_CODE
1. 参考[如何创建机器人](https://open.dingtalk.com/document/orgapp/the-creation-and-installation-of-the-application-robot-in-the)

## 📞 支持

- 帮助文档： https://open.dingtalk.com/document/ai-dev/dingtalk-server-api-mcp-overview
- 钉钉开放平台: https://open.dingtalk.com
- MCP协议: https://modelcontextprotocol.io
- 欢迎加入钉钉MCP交流群
  ![欢迎加入钉钉MCP交流群](/mcp-assets/716fc6db3a69b27b109dea933f579009.png)

**官方网站：** [https://github.com/open-dingtalk/dingtalk-mcp](https://github.com/open-dingtalk/dingtalk-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`communication`
- 标签：`communication`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y dingtalk-mcp@latest`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/open-dingtalk-dingtalk.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
