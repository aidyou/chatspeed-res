---
title: "Claude实时语音服"
description: "一种模型上下文协议服务器，使像 Claude 这样的人工智能助手能够通过 Twilio 和 OpenAI 的语音模型发起和管理实时语音通话。"
---

# Claude实时语音服

一种模型上下文协议服务器，使像 Claude 这样的人工智能助手能够通过 Twilio 和 OpenAI 的语音模型发起和管理实时语音通话。

# 语音通话 MCP 服务器

这是一个模型上下文协议 (MCP) 服务器，它使 Claude 和其他 AI 助手能够使用 Twilio 和 OpenAI（GPT-4o 实时模型）发起和管理语音通话。

您可以将此作为基础来启动您的 AI 语音通话探索，节省时间并在其基础上开发更多功能。

## 序列图

```mermaid
sequenceDiagram
    participant AI as AI Assistant (e.g., Claude)
    participant MCP as MCP Server
    participant Twilio as Twilio
    participant Phone as Destination Phone
    participant OpenAI as OpenAI
    
    AI->>MCP: 1) Initiate outbound call request 
(POST /calls)
    MCP->>Twilio: 2) Place outbound call via Twilio API
    Twilio->>Phone: 3) Ring the destination phone
    Twilio->>MCP: 4) Call status updates & audio callbacks (webhooks)
    MCP->>OpenAI: 5) Forward real-time audio to OpenaAI's realtime model
    OpenAI->>MCP: 6) Return voice stream
    MCP->>Twilio: 7) Send voice stream
    Twilio->>Phone: 8) Forward voice stream
    Note over Phone: Two-way conversation continues 
until the call ends
```

## 特性

- 通过 Twilio 发起外拨电话 📞
- 使用 GPT-4o 实时模型实时处理通话音频 🎙️
- 通话过程中实时切换语言 🌐
- 针对常见通话场景的预构建提示（如餐厅预订） 🍽️
- 自动使用 ngrok 进行公共 URL 隧道传输 🔄
- 安全处理凭证 🔒

## 为什么选择 MCP？

模型上下文协议 (MCP) 桥接了 AI 助手与现实世界行动之间的鸿沟。通过实现 MCP，这个服务器允许像 Claude 这样的 AI 模型：

1. 代表用户发起实际电话通话
2. 处理并响应实时音频对话
3. 执行需要语音通信的复杂任务

这种开源实现提供了透明性和可定制性，让开发者可以扩展功能的同时保持对其数据和隐私的控制。

## 要求

- Node.js >= 22
  - 如果您需要更新 Node.js，我们建议使用 `nvm`（Node 版本管理器）：
```bash
    nvm install 22
    nvm use 22
```
- 具有 API 凭证的 Twilio 账户
- OpenAI API 密钥
- Ngrok 认证令牌

## 安装

### 手动安装

1. 克隆仓库
```bash
   git clone https://github.com/lukaskai/voice-call-mcp-server.git
   cd voice-call-mcp-server
```

2. 安装依赖并构建
```bash
   npm install
   npm run build
```

## 配置

服务器需要以下环境变量：

- `TWILIO_ACCOUNT_SID`: 您的 Twilio 账户 SID
- `TWILIO_AUTH_TOKEN`: 您的 Twilio 授权令牌
- `TWILIO_NUMBER`: 您的 Twilio 号码
- `OPENAI_API_KEY`: 您的 OpenAI API 密钥
- `NGROK_AUTHTOKEN`: 您的 ngrok 认证令牌
- `RECORD_CALLS`: 设置为 "true" 以录制通话（可选）

### Claude Desktop 配置

要使用 Claude Desktop 与此服务器配合，请在配置文件中添加以下内容：

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "voice-call": {
      "command": "node",
      "args": ["/path/to/your/mcp-new/dist/start-all.cjs"],
      "env": {
        "TWILIO_ACCOUNT_SID": "your_account_sid",
        "TWILIO_AUTH_TOKEN": "your_auth_token",
        "TWILIO_NUMBER": "your_e.164_format_number",
        "OPENAI_API_KEY": "your_openai_api_key",
        "NGROK_AUTHTOKEN": "your_ngrok_authtoken"
      }
    }
  }
}
```

之后，重启 Claude Desktop 以重新加载配置。
如果连接成功，您应该能在 🔨 菜单下看到“语音通话”选项。

## 与 Claude 的示例交互

这里有一些通过 Claude 与服务器自然交互的方式：

1. 简单呼叫：
```
Can you call +1-123-456-7890 and let them know I'll be 15 minutes late for our meeting?
```

2. 餐厅预订：
```
Please call Delicious Restaurant at +1-123-456-7890 and make a reservation for 4 people tonight at 7:30 PM. Please speak in German.
```

3. 预约安排：
```
Please call Expert Dental NYC (+1-123-456-7899) and reschedule my Monday appointment to next Friday between 4–6pm.
```

## 重要说明

1. **电话号码格式**：所有电话号码必须采用E.164格式（例如，+11234567890）
2. **速率限制**：请注意您的Twilio和OpenAI账户的速率限制和费用
3. **语音对话**：AI将实时处理自然对话
4. **通话时长**：请注意通话时长会影响OpenAI API和Twilio的成本
5. **公开暴露**：请注意ngrok隧道会以随机URL的形式公开您的服务器供Twilio访问（尽管受随机密钥保护）

## 故障排除

常见的错误信息及解决方案：

1. "电话号码必须为E.164格式"
   - 确保电话号码以"+"开头，并包含国家代码

2. "无效凭据"
   - 请仔细检查您的TWILIO_ACCOUNT_SID和TWILIO_AUTH_TOKEN。您可以从[Twilio控制台](https://console.twilio.com)复制它们

3. "OpenAI API错误"
   - 验证您的OPENAI_API_KEY是否正确且有足够的信用额度

4. "ngrok隧道启动失败"
   - 确保您的NGROK_AUTHTOKEN有效且未过期

5. "OpenAI实时系统无法检测到语音输入结束，或存在延迟。"
   - 有时，Twilio与接收方网络运营商之间可能存在语音编码问题。尝试使用不同的接收方。

## 贡献

欢迎贡献！我们希望改进的一些领域包括：

- 实现对当前实现之外的多种AI模型的支持
- 添加数据库集成，以便本地存储对话历史并使其可用于AI上下文
- 改进延迟和响应时间，以增强通话体验
- 增强错误处理和恢复机制
- 添加更多针对常见场景的预构建对话模板
- 实施更完善的呼叫监控和分析功能

如果您想做出贡献，请在提交拉取请求前先打开一个问题来讨论您的想法。

## 许可证

本项目根据MIT许可证发布 - 详情请参阅LICENSE文件。

## 安全性

请不要在GitHub的问题或拉取请求中包含任何敏感信息（如电话号码或API凭证）。此服务器处理敏感通信；请负责任地部署它，并确保所有凭证的安全。

## 是时候迎接新使命了吗？

我们正在招聘工程师，在语音AI前沿进行建设——并将其融入下一代电信服务中。

感兴趣吗？前往[careers.popcorn.space](https://careers.popcorn.space/apply)了解更多 🍿 !

**官方网站：** [https://github.com/lukaskai/voice-call-mcp-server](https://github.com/lukaskai/voice-call-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`communication`
- 标签：`communication`, `speech processing`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`/path/to/your/mcp-new/dist/start-all.cjs`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/popcornspace-voice-call.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
