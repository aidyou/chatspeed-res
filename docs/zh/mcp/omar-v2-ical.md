---
title: "MCP日历"
description: "将macOS的日历管理转变为使用自然语言的对话式体验，使用户可以通过与MCP兼容的客户端无缝创建、管理和更新日历事件。"
---

# MCP日历

将macOS的日历管理转变为使用自然语言的对话式体验，使用户可以通过与MCP兼容的客户端无缝创建、管理和更新日历事件。

# MCP iCal 服务器

🗓️ 适用于 macOS 的自然语言日历管理

[![MIT License](/mcp-assets/6d39e47e35bcced1bb707dfa0b1c276c.svg)](https://choosealicense.com/licenses/mit/)
[![Python 3.12+](/mcp-assets/5142151145d2dd1ac338bb460f878742.svg)](https://www.python.org/downloads/)
[![MCP 兼容](/mcp-assets/07cb9f306431132c74e40e63bcac6450.svg)](https://modelcontextprotocol.io)

## 🌟 概述

使用自然语言来改变您与 macOS 日历的交互方式！mcp-ical 服务器利用 Model Context Protocol (MCP) 将您的日历管理转变为对话体验。

```
You: "What's my schedule for next week?"
Claude: "Let me check that for you..."
[Displays a clean overview of your upcoming week]

You: "Add a lunch meeting with Sarah tomorrow at noon"
Claude: "✨ 📅 Created: Lunch with Sarah Tomorrow, 12:00 PM"
```

## ✨ 功能

### 📅 事件创建
立即将自然语言转换为日历事件！

```
"Schedule a team lunch next Thursday at 1 PM at Bistro Garden"
↓
📎 Created: Team Lunch
   📅 Thursday, 1:00 PM
   📍 Bistro Garden
```

#### 支持的功能：
- 自定义日历选择
- 地点和备注
- 智能提醒
- 重复事件

#### 高级用户示例：
```
🔄 Recurring Events:
"Set up my weekly team sync every Monday at 9 AM with a 15-minute reminder"

📝 Detailed Events:
"Schedule a product review meeting tomorrow from 2-4 PM in the Engineering calendar, 
add notes about reviewing Q1 metrics, and remind me 1 hour before"

📱 Multi-Calendar Support:
"Add a dentist appointment to my Personal calendar for next Wednesday at 3 PM"
```

### 🔍 智能日程管理和可用性
通过自然查询快速访问您的日程：

```
"What's on my calendar for next week?"
↓
📊 Shows your upcoming events with smart formatting

"When am I free to schedule a 2-hour meeting next Tuesday?"
↓
🕒 Available time slots found:
   • Tuesday 10:00 AM - 12:00 PM
   • Tuesday 2:00 PM - 4:00 PM
```

### ✏️ 智能事件更新
自然地修改事件：

```
Before: "Move tomorrow's team meeting to 3 PM instead"
↓
After: ✨ Meeting rescheduled to 3:00 PM
```

#### 更新功能：
- 时间和日期修改
- 日历转移
- 地点更新
- 备注添加
- 提醒调整
- 重复模式更改

### 📊 日历管理
- 查看所有可用的日历
- 智能日历建议
- 当配置了 iCloud 时无缝集成 Google 日历

> 💡 **小贴士**: 因为您可以在自定义日历中创建事件，如果您已将 Google 日历与 iCloud 日历同步，您可以使用此 MCP 服务器在 Google 日历中创建事件！只需在创建/更新事件时指定 Google 日历即可

## 🚀 快速开始

> 💡 **注意**: 虽然这些说明重点介绍了如何使用 Claude for Desktop 设置 MCP 服务器，但此服务器可以与任何 MCP 兼容的客户端一起使用。有关使用不同客户端的更多详细信息，请参阅 [MCP 文档](https://modelcontextprotocol.io/quickstart/client)。

### 前提条件
- [uv 包管理器](https://github.com/astral-sh/uv)
- 配置了 Calendar 应用程序的 macOS
- 一个 MCP 客户端 - 推荐使用 [Claude for desktop](https://claude.ai/download) 

### 安装

虽然此 MCP 服务器可以与任何 MCP 兼容的客户端一起使用，但以下说明是针对 Claude for desktop 的。

1. **克隆和设置**
```bash
# Clone the repository
git clone https://github.com/yourusername/mcp-ical.git
cd mcp-ical

# Install dependencies
uv sync
```

2. **配置 Claude for Desktop**

创建或编辑 `~/Library/Application\ Support/Claude/claude_desktop_config.json`：

```json
{
    "mcpServers": {
        "mcp-ical": {
            "command": "uv",
            "args": [
                "--directory",
                "/ABSOLUTE/PATH/TO/PARENT/FOLDER/mcp-ical",
                "run",
                "mcp-ical"
            ]
        }
    }
}
```

3. **启动 Claude 以访问日历**

> ⚠️ **重要提示**: 必须从终端启动 Claude 才能正确请求日历权限。直接从 Finder 启动不会触发权限提示。

```bash
/Applications/Claude.app/Contents/MacOS/Claude
```

4. **开始使用！**
```
Try: "What's my schedule looking like for next week?"
```

> 🔑 **注意**: 当您首次使用与日历相关的命令时，macOS 将提示您授予日历访问权限。只有按照上述方法从终端启动 Claude 时才会出现此提示。
## 🧪 测试

> ⚠️ **警告**: 测试将创建临时日历和事件。虽然清理是自动的，但请仅在开发环境中运行测试。

```bash
# Install dev dependencies
uv sync --dev

# Run test suite
uv run pytest tests
```

## 🐛 已知问题

### 重复事件
- 非标准重复日程可能无法总是正确设置
- 与俳句相比，使用 Claude 3.5 十四行诗可以获得更好的结果
- 重复全天事件的提醒时间可能会偏差一天

## 🤝 贡献

欢迎提供反馈和贡献！以下是您可以帮助的方式：

1. 叉取仓库
2. 创建您的功能分支
3. 提交您的更改
4. 推送到该分支
5. 打开一个 Pull Request

## 📝 许可证

本项目采用 MIT 许可证 - 详情请参阅 [LICENSE](https://github.com/Omar-V2/mcp-ical/blob/HEAD/LICENSE) 文件。

## 🙏 致谢

- 使用 [Model Context Protocol](https://modelcontextprotocol.io) 构建
- MacOS 日历集成使用 [PyObjC](https://github.com/ronaldoussoren/pyobjc) 构建

**官方网站：** [https://github.com/Omar-V2/mcp-ical](https://github.com/Omar-V2/mcp-ical)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`productivity`
- 标签：`calendar management`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`--directory /ABSOLUTE/PATH/TO/PARENT/FOLDER/mcp-ical run mcp-ical`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/omar-v2-ical.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
