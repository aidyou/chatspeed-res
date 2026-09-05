---
title: "Slack"
description: "用于Slack API的MCP服务器，使Claude能够与Slack工作区进行交互。"
---

# Slack

用于Slack API的MCP服务器，使Claude能够与Slack工作区进行交互。

# Slack MCP 服务器

用于 Slack API 的 MCP 服务器，使 Claude 能够与 Slack 工作区进行交互。

## 工具

1. `slack_list_channels`
   - 列出工作区中的公共频道
   - 可选输入：
     - `limit` (数字，默认：100，最大：200)：要返回的最大频道数
     - `cursor` (字符串)：下一页的分页游标
   - 返回：包含频道 ID 和信息的频道列表

2. `slack_post_message`
   - 向 Slack 频道发布新消息
   - 必需输入：
     - `channel_id` (字符串)：要发布的频道 ID
     - `text` (字符串)：要发布的消息文本
   - 返回：消息发布确认和时间戳

3. `slack_reply_to_thread`
   - 回复特定的消息线程
   - 必需输入：
     - `channel_id` (字符串)：包含线程的频道
     - `thread_ts` (字符串)：父消息的时间戳
     - `text` (字符串)：回复文本
   - 返回：回复确认和时间戳

4. `slack_add_reaction`
   - 向消息添加表情符号反应
   - 必需输入：
     - `channel_id` (字符串)：包含消息的频道
     - `timestamp` (字符串)：要反应的消息的时间戳
     - `reaction` (字符串)：不带冒号的表情符号名称
   - 返回：反应确认

5. `slack_get_channel_history`
   - 获取频道中的最近消息
   - 必需输入：
     - `channel_id` (字符串)：频道 ID
   - 可选输入：
     - `limit` (数字，默认：10)：要检索的消息数量
   - 返回：包含消息内容和元数据的消息列表

6. `slack_get_thread_replies`
   - 获取消息线程中的所有回复
   - 必需输入：
     - `channel_id` (字符串)：包含线程的频道
     - `thread_ts` (字符串)：父消息的时间戳
   - 返回：包含回复内容和元数据的回复列表

7. `slack_get_users`
   - 获取带有基本资料信息的工作区用户列表
   - 可选输入：
     - `cursor` (字符串)：下一页的分页游标
     - `limit` (数字，默认：100，最大：200)：要返回的最大用户数
   - 返回：包含基本资料的用户列表

8. `slack_get_user_profile`
   - 获取特定用户的详细资料信息
   - 必需输入：
     - `user_id` (字符串)：用户的 ID
   - 返回：详细的用户资料信息

## 设置

```markdown
```

1. 创建 Slack 应用：
   - 访问 [Slack Apps 页面](https://api.slack.com/apps)
   - 点击“创建新应用”
   - 选择“从头开始”
   - 命名你的应用并选择你的工作区

2. 配置 Bot Token 权限范围：
   导航到“OAuth & Permissions”并添加以下权限范围：
   - `channels:history` - 查看公共频道中的消息和其他内容
   - `channels:read` - 查看基本的频道信息
   - `chat:write` - 以应用的身份发送消息
   - `reactions:write` - 向消息添加表情符号反应
   - `users:read` - 查看用户及其基本信息

4. 将应用安装到工作区：
   - 点击“安装到工作区”并授权该应用
   - 保存以 `xoxb-` 开头的“Bot User OAuth Token”

5. 按照 [此指南](https://slack.com/help/articles/221769328-Locate-your-Slack-URL-or-ID#find-your-workspace-or-org-id) 获取您的团队 ID（以 `T` 开头）

### 与 Claude Desktop 一起使用

将以下内容添加到您的 `claude_desktop_config.json` 中：

#### npx

```json
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-slack"
      ],
      "env": {
        "SLACK_BOT_TOKEN": "xoxb-your-bot-token",
        "SLACK_TEAM_ID": "T01234567"
      }
    }
  }
}
```

#### docker

```json
{
  "mcpServers": {
    "slack": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e",
        "SLACK_BOT_TOKEN",
        "-e",
        "SLACK_TEAM_ID",
        "mcp/slack"
      ],
      "env": {
        "SLACK_BOT_TOKEN": "xoxb-your-bot-token",
        "SLACK_TEAM_ID": "T01234567"
      }
    }
  }
}
```

### 故障排除

如果您遇到权限错误，请验证：
1. 所有必需的权限范围已添加到您的 Slack 应用中
2. 该应用已正确安装到您的工作区
3. 令牌和工作区 ID 已正确复制到配置文件中
4. 该应用已被添加到需要访问的频道中

## 构建

Docker 构建命令：

```bash
docker build -t mcp/slack -f src/slack/Dockerfile .
```

## 许可证

本 MCP 服务器依据 MIT 许可证许可。这意味着您可以自由地使用、修改和分发软件，但需遵守 MIT 许可证的条款和条件。更多详情，请参阅项目仓库中的 LICENSE 文件。

**官方网站：** [https://github.com/modelcontextprotocol/servers/tree/main/src/slack](https://github.com/modelcontextprotocol/servers/tree/main/src/slack)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`communication`
- 标签：`communication`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @modelcontextprotocol/server-slack`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/modelcontextprotocol-slack.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
