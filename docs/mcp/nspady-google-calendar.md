---
title: "Google日历管理工具"
description: "让大型语言模型阅读和管理Google日历事件。"
---

# Google日历管理工具

让大型语言模型阅读和管理Google日历事件。

# Google 日历 MCP 服务器

这是一个模型上下文协议 (MCP) 服务器，提供与 Google 日历的集成。它允许 LLMs 通过标准化接口读取、创建、更新和搜索日历事件。

## 示例用法

除了您期望的日历集成的常规功能外，您还可以执行非常动态的多步骤流程，例如：

1. 从截图和图片中添加事件：
```
   根据附加的截图将此事件添加到我的日历中。
```
   支持的图像格式：PNG、JPEG、GIF
   图像可以包含事件详细信息，如日期、时间、地点和描述
   
2. 日历分析：
```
   这周我有哪些不属于我通常例行公事的活动？
```
3. 检查出席情况：
```
   明天哪些活动的参与者尚未接受邀请？
```
4. 自动协调事件：
```
   这里有一些别人提供给我的可用时间。
   查看可用时间并在我的工作日历上创建一个空闲的时间段。
```
5. 提供您的可用性：
```
   请查看我的个人和工作日历，为即将到来的一周提供可用时间。
   选择适合东海岸正常工作时间的时间。会议时间为1小时
```

## 要求

1. Node.js（推荐使用最新 LTS 版本）
2. TypeScript 5.3 或更高版本
3. 启用了 Calendar API 的 Google Cloud 项目
4. OAuth 2.0 凭证（客户端 ID 和客户端密钥）

## Google Cloud 设置

1. 前往 [Google Cloud 控制台](https://console.cloud.google.com)
2. 创建新项目或选择现有项目。
3. 为您的项目启用 [Google 日历 API](https://console.cloud.google.com/apis/library/calendar-json.googleapis.com)。在启用 API 之前，请确保从顶部栏中选择了正确的项目。
4. 创建 OAuth 2.0 凭证：
   - 转到“凭据”
   - 点击“创建凭据”>“OAuth 客户端 ID”
   - 选择应用程序将访问的数据类型为“用户数据”
   - 添加您的应用名称和联系信息
   - 添加以下范围（可选）：
     - `https://www.googleapis.com/auth/calendar.events`（如果需要更广泛的权限，则使用 `https://www.googleapis.com/auth/calendar`）
   - 选择“桌面应用”作为应用程序类型
   - 在 [OAuth 同意屏幕](https://console.cloud.google.com/apis/credentials/consent) 下添加您的电子邮件地址作为测试用户
      - 注意：添加测试用户可能需要几分钟。在测试用户传播完成之前，OAuth 同意不会允许您继续。
      - 关于测试模式的注意事项：当应用处于测试模式时，授权令牌将在1周后过期，并且需要通过运行 `npm run auth` 来刷新。

## 安装

1. 克隆仓库
2. 安装依赖（这也会通过 postinstall 构建 js）:
```bash
   npm install
```
3. 从 Google Cloud Console 的“Credentials”部分下载您的 Google OAuth 凭证，将文件重命名为 `gcp-oauth.keys.json` 并放置在项目的根目录中。
   - 确保文件包含的是“Desktop app”的凭证。
   - 或者，复制提供的模板文件: `cp gcp-oauth.keys.example.json gcp-oauth.keys.json` 并用来自 Google Cloud Console 的凭证填充它。

## 可用脚本

- `npm run build` - 构建 TypeScript 代码（将 `src` 编译到 `build`）
- `npm run typecheck` - 运行 TypeScript 类型检查而不编译
- `npm run start` - 启动已编译的服务器（使用 `node build/index.js`）
- `npm run dev` - 使用 ts-node 在开发模式下启动服务器（监视更改）
- `npm run auth` - 手动启动用于 Google OAuth 流程的身份验证服务器（如果自动流程失败或用于测试时有用）
- `npm test` - 使用 Vitest 运行单元/集成测试套件
- `npm run test:watch` - 以监视模式运行测试
- `npm run coverage` - 运行测试并生成覆盖率报告

## 身份验证

服务器支持自动和手动身份验证流程：

### 自动身份验证（推荐）
1. 将您的 Google OAuth 凭证放在 `gcp-oauth.keys.json` 中。
2. 启动 MCP 服务器：`npm start` 或 `npm run dev`。
3. 如果在 `.gcp-saved-tokens.json` 中找不到有效的身份验证令牌，服务器将自动：
   - 启动一个身份验证服务器（默认端口为 3000-3004）
   - 打开浏览器窗口进行 OAuth 流程
   - 一旦认证成功，安全地将令牌保存到 `.gcp-saved-tokens.json`
   - 关闭身份验证服务器
   - 继续正常的 MCP 服务器操作

服务器会自动管理令牌刷新。

### 手动身份验证
运行 `npm run auth` 仅启动身份验证服务器。通过浏览器进行身份验证，令牌将会被保存。

## 测试

单元和集成测试使用 [Vitest](https://vitest.dev/) 实现。

- 运行测试: `npm test`
- 以监视模式运行测试: `npm run test:watch`
- 生成覆盖率报告: `npm run coverage`

测试通过模拟外部依赖项（如 Google API、文件系统）来确保对服务器逻辑和处理器的隔离测试。

## 安全须知

- 服务器本地运行，并需要 OAuth 认证。
- OAuth 凭证 (`gcp-oauth.keys.json`) 和保存的令牌 (`.gcp-saved-tokens.json`) **绝对不能** 提交到版本控制中。确保它们被添加到了你的 `.gitignore` 文件里。
- 对于生产环境使用，请考虑让您的 OAuth 应用程序通过 Google 验证。

## 与 Claude Desktop 一起使用

1. 将此配置添加到您的 Claude Desktop 配置文件中。例如：`/Users//Library/Application Support/Claude/claude_desktop_config.json`:
```json
   {
     "mcpServers": {
       "google-calendar": {
         "command": "node",
         "args": ["
/build/index.js"]
       }
     }
   }
```
   注意：请将 `
` 替换为您的项目目录的实际路径。

2. 重启 Claude Desktop

## 开发

### 故障排除

1. OAuth 令牌在一周（7天）后过期
   - 如果您的 Google Cloud 应用处于测试模式，令牌每周都会过期。通过运行 `npm run auth` 或重新启动服务器来重新认证。

3. OAuth 令牌错误 / 认证失败
   - 确保项目根目录下存在 `gcp-oauth.keys.json` 文件，并且包含有效的桌面应用程序凭据。
   - 尝试删除 `.gcp-saved-tokens.json` 并重新认证。
   - 检查 Google Cloud 控制台以确保已启用 Calendar API，并且如果应用处于测试模式，则您被列为测试用户。
   - 确认没有其他进程正在使用端口 3000-3004，当认证服务器需要启动时。

4. 构建错误
   - 再次运行 `npm install`。
   - 检查 Node.js 版本。
   - 删除 `build/` 目录并运行 `npm run build`。

## 许可证

MIT

**官方网站：** [https://github.com/nspady/google-calendar-mcp](https://github.com/nspady/google-calendar-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`productivity`
- 标签：`calendar management`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`<absolute-path-to-project-folder>/build/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/nspady-google-calendar.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
