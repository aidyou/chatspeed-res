---
title: "MCP G套件服务器"
description: "MCP服务器用于与Google产品交互。"
---

# MCP G套件服务器

MCP服务器用于与Google产品交互。

# mcp-gsuite MCP 服务器

[Smithery](https://smithery.ai/server/mcp-gsuite)
用于与 Google 产品交互的 MCP 服务器。

## 示例提示

目前，此 MCP 服务器支持 Gmail 和日历集成，具有以下功能：

1. 通用
* 多个 Google 帐户

2. Gmail
* 获取您的 Gmail 用户信息
* 使用灵活搜索查询电子邮件（例如，未读、来自特定发件人、日期范围、带有附件）
* 通过 ID 检索完整的电子邮件内容
* 创建带有收件人、主题、正文和抄送选项的新草稿邮件
* 删除草稿邮件
* 回复现有邮件（可以立即发送或保存为草稿）
* 通过其 ID 一次性检索多封邮件。
* 将多封邮件中的附件保存到本地系统。

3. 日历
* 管理多个日历
* 在指定的时间范围内获取日历事件
* 创建日历事件：
  + 标题、开始/结束时间
  + 可选的位置和描述
  + 可选的参与者
  + 自定义时区支持
  + 通知偏好设置
* 删除日历事件

您可以尝试的示例提示：

* 检索我最新的未读消息
* 搜索来自 Scrum Master 的邮件
* 检索所有来自会计部门的邮件
* 查找关于 ABC 的邮件并总结它
* 给 Alice 的最后一封邮件写一个友好的回复，并上传草稿。
* 用感谢信回复 Bob 的邮件。将其保存为草稿

* 我明天的日程安排是什么？
* 检查我的私人账户下周的家庭日程
* 我需要与 Tim 计划下周的一个两小时的活动。建议一些时间段。

## 快速入门

### 安装

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/mcp-gsuite) 自动安装 Claude Desktop 的 mcp-gsuite：

```bash
npx -y @smithery/cli install mcp-gsuite --client claude
```

#### OAuth 2

Google Workspace (G Suite) API 需要 OAuth2 授权。请按照以下步骤设置身份验证：

1. 创建 OAuth2 凭据：
   - 转到 [Google Cloud 控制台](https://console.cloud.google.com/)
   - 创建新项目或选择现有项目
   - 为您的项目启用 Gmail API 和 Google Calendar API
   - 转到“凭据”→“创建凭据”→“OAuth 客户端 ID”
   - 选择“桌面应用程序”或“Web 应用程序”作为应用程序类型
   - 使用所需信息配置 OAuth 同意屏幕
   - 添加授权重定向 URI（包括 `http://localhost:4100/code` 用于本地开发）

2. 所需的 OAuth2 范围：
   

```json
   [
     "openid",
     "https://mail.google.com/",
     "https://www.googleapis.com/auth/calendar",
     "https://www.googleapis.com/auth/userinfo.email"
   ]
```

3. 然后在工作目录中使用客户端创建一个 `.gauth.json` 文件

```json
{
    "web": {
        "client_id": "$your_client_id",
        "client_secret": "$your_client_secret",
        "redirect_uris": ["http://localhost:4100/code"],
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token"
    }
}
```

4. 创建一个包含帐户信息的 `.accounts.json` 文件

```json
{
    "accounts": [
        {
            "email": "alice@bob.com",
            "account_type": "personal",
            "extra_info": "Additional info that you want to tell Claude: E.g. 'Contains Family Calendar'"
        }
    ]
}
```

您可以指定多个帐户。确保它们在您的 Google Auth 应用中有访问权限。`extra_info` 字段特别有用，因为您可以在此处添加希望告诉 AI 关于该帐户的信息（例如，它是否有特定的日程）。

注意：当你首次为特定账户执行其中一个工具时，会打开一个浏览器，将你重定向到 Google 并要求你输入凭证、权限范围等。成功登录后，它会将凭证存储在一个名为 `.oauth.{email}.json` 的本地文件中。一旦授权完成，刷新令牌将会被使用。

#### Claude 桌面版

在 MacOS 上: `~/Library/Application\ Support/Claude/claude_desktop_config.json`

在 Windows 上: `%APPDATA%/Claude/claude_desktop_config.json`

  开发/未发布服务器配置
  

```json
{
  "mcpServers": {
    "mcp-gsuite": {
      "command": "uv",
      "args": [
        "--directory",
        "/mcp-gsuite",
        "run",
        "mcp-gsuite"
      ]
    }
  }
}
```

注意：你也可以使用 `uv run mcp-gsuite --accounts-file /path/to/custom/.accounts.json` 来指定不同的账户文件，或者使用 `--credentials-dir /path/to/custom/credentials` 来指定不同的凭证目录。

```json
{
  "mcpServers": {
    "mcp-gsuite": {
      "command": "uv",
      "args": [
        "--directory",
        "/mcp-gsuite",
        "run",
        "mcp-gsuite",
        "--accounts-file",
        "/path/to/custom/.accounts.json",
        "--credentials-dir",
        "/path/to/custom/credentials"
      ]
    }
  }
}
```

  已发布服务器配置
  

```json
{
  "mcpServers": {
    "mcp-gsuite": {
      "command": "uvx",
      "args": [
        "mcp-gsuite",
        "--accounts-file",
        "/path/to/custom/.accounts.json",
        "--credentials-dir",
        "/path/to/custom/credentials"
      ]
    }
  }
}
```

### 配置选项

MCP 服务器可以通过几个命令行选项来指定用于认证和账户信息的自定义路径：

* `--gauth-file`: 指定包含 OAuth2 客户端配置的 `.gauth.json` 文件的路径。默认值为 `./.gauth.json`。
* `--accounts-file`: 指定包含有关 Google 账户信息的 `.accounts.json` 文件的路径。默认值为 `./.accounts.json`。
* `--credentials-dir`: 指定成功认证后存储 OAuth 凭证的目录。默认值为当前工作目录下的每个账户子目录 `.oauth.{email}.json`。

这些选项允许灵活管理不同环境或多个凭证集和账户集，特别适用于开发和测试场景。

示例用法：

```bash
uv run mcp-gsuite --gauth-file /path/to/custom/.gauth.json --accounts-file /path/to/custom/.accounts.json --credentials-dir /path/to/custom/credentials
```

这种配置对于运行具有不同配置的多个服务器实例，或者部署到默认路径不适用的环境中非常有用。

## 开发

### 构建与发布

准备分发包：

1. 同步依赖并更新锁文件：

```bash
uv sync
```

2. 构建包分发：

```bash
uv build
```

这将在 `dist/` 目录下创建源码和 wheel 分发包。

3. 发布到 PyPI：

```bash
uv publish
```

注意：你需要通过环境变量或命令标志设置 PyPI 凭证：
* 令牌: `--token` 或 `UV_PUBLISH_TOKEN`
* 或用户名/密码: `--username`/`UV_PUBLISH_USERNAME` 和 `--password`/`UV_PUBLISH_PASSWORD`

### 调试

由于 MCP 服务器通过标准输入输出运行，调试可能会有挑战。为了获得最佳调试体验，我们强烈建议使用 [MCP Inspector](https://github.com/modelcontextprotocol/inspector)。

你可以通过 [ `npm` ](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) 使用此命令启动 MCP Inspector：

```bash
npx @modelcontextprotocol/inspector uv --directory /path/to/mcp-gsuite run mcp-gsuite
```

启动后，Inspector 将显示一个 URL，你可以在浏览器中访问该 URL 开始调试。

你还可以使用以下命令查看服务器日志：

```bash
tail -n 20 -f ~/Library/Logs/Claude/mcp-server-mcp-gsuite.log
```

**官方网站：** [https://github.com/MarkusPfundstein/mcp-gsuite](https://github.com/MarkusPfundstein/mcp-gsuite)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`productivity`
- 标签：`communication`, `calendar management`, `cloud storage`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`mcp-gsuite --accounts-file /path/to/custom/.accounts.json --credentials-dir /path/to/custom/credentials`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/markuspfundstein-gsuite.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
