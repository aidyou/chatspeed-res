---
title: "飞行雷达24实时航班追踪"
description: "一个基于Claude桌面的MCP服务器，它可以帮助您使用Flightradar24数据实时跟踪航班。非常适合航空爱好者、旅行规划师或任何对头顶航班好奇的人！"
---

# 飞行雷达24实时航班追踪

一个基于Claude桌面的MCP服务器，它可以帮助您使用Flightradar24数据实时跟踪航班。非常适合航空爱好者、旅行规划师或任何对头顶航班好奇的人！

# Flightradar24 MCP 服务器 🛩️

一个 Claude 桌面 MCP 服务器，利用 Flightradar24 的数据帮助你实时跟踪航班。非常适合航空爱好者、旅行规划者或任何对头顶飞行感兴趣的人！

## 这个功能可以做什么？ ✨

- 🔍 实时跟踪任何航班
- ⏰ 获取特定航班的到达和出发时间
- 🌉 查看机场内航班的状态
- 🚨 监控紧急航班

## 设置指南 🚀

### 1. 前提条件
- 在您的计算机上安装 [Claude Desktop](https://claude.ai/desktop)
- 一个 Flightradar24 API 密钥（从 [Flightradar24 的网站](https://www.flightradar24.com/premium) 获取）*

### 2. 安装步骤

1. 将此仓库克隆到您计算机上的某个位置：
```bash
   git clone https://github.com/sunsetcoder/flightradar24-mcp-server.git
```

2. 安装依赖并构建项目：
```bash
   cd flightradar24-mcp-server
   npm install
   npm run build
```

### 3. 与 Claude Desktop 集成

1. 打开您的 Claude Desktop 配置文件：
```
   # 在 Mac 上：
   ~/Library/Application Support/Claude/claude_desktop_config.json
   
   # 在 Windows 上：
   %APPDATA%/Claude/claude_desktop_config.json
```

2. 在配置文件中的 `mcpServers` 对象下添加以下内容：
```json
   {
     "mcpServers": {
       "flightradar24-server": {
         "command": "node",
         "args": [
           "/Users///flightradar24-mcp-server/dist/index.js"
         ],
         "env": {
           "FR24_API_KEY": "your_api_key_here",
           "FR24_API_URL": "https://fr24api.flightradar24.com"
         }
       }
     }
   }
```

3. 重要步骤：
   - 将 `/FULL/PATH/TO/flightradar24-mcp-server` 替换为您实际克隆仓库的完整路径
   - 在 `env` 部分添加您的 Flightradar24 API 密钥
   - 确保在路径中使用正斜杠 (`/`)，即使是在 Windows 上也是如此

4. 重启 Claude Desktop 使更改生效

## 环境设置

1. 将 `.env.example` 复制为 `.env`：
```bash
   cp .env.example .env
```

2. 更新 `.env` 文件，填入您的实际 Flightradar24 API 密钥：
```env
   FR24_API_KEY=your_actual_api_key_here
```

注意：切勿将实际 API 密钥提交到版本控制系统。出于安全考虑，`.env` 文件被 git 忽略。

## 让我们试一试！ 🎮

一旦服务器配置完成，您可以向 Claude 提出如下问题：

1. “联合航空公司航班 UA123 的预计到达时间是什么时候？”
2. “显示 SFO 当前的所有航班”
3. “这个区域内是否有紧急航班？”
4. “显示接下来 2 小时内抵达 SFO 的所有国际航班”
5. “目前有多少商业航班正在太平洋上空飞行？”
6. “识别加利福尼亚地区内已宣布紧急情况的所有航班”

与 Claude 的示例对话：
```
You: What's the status of flight UA123?
Claude: Let me check that for you...
[Claude will use the MCP server to fetch real-time flight information]
```

## 常见问题与故障排除 🤔

### "Claude 无法连接到服务器"
- 检查 `claude_desktop_config.json` 中的路径是否正确
- 确保您使用的是完整的绝对路径
- 验证您的 API 密钥是否正确
- 尝试重启 Claude Desktop

### "服务器没有响应"
- 确保您的 Flightradar24 API 密钥有效
- 检查 API URL 是否正确
- 查看服务器日志中是否有任何错误信息

### FlightRadar API 访问
- 注意：使用 Flightradar24 的 API 需要 [订阅](https://fr24api.flightradar24.com/subscriptions-and-credits)

## 需要更多帮助？ 🆘

1. 确保 Claude Desktop 已正确安装
2. 验证您的 Flightradar24 API 密钥是活跃状态
3. 检查配置文件中的路径是否正确
4. 查看 MCP 服务器日志中的错误信息

## 许可证 📄

MIT

---

为航空爱好者用心制作 ❤️

**官方网站：** [https://github.com/sunsetcoder/flightradar24-mcp-server](https://github.com/sunsetcoder/flightradar24-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`travel and transportation`, `location services`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`/Users/<username>/<FULL_PATH...>/flightradar24-mcp-server/dist/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/sunsetcoder-flightradar24.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
