---
title: "yijing-bazi-mcp"
description: "一个基于MCP（Model Context Protocol）协议的专业易经八字分析服务器，为AI助手提供传统中华文化分析能力。本项目集成了易经卦象分析、八字命理推算、综合运势预测等功能，支持多种AI客户端接入。 📢 重要提示： 此项目已发布到 NPM，现在可以： - 在任意目录使用 npx yijing-bazi-mcp 命令 - 通过 npm install -g yijing-bazi-mc…"
---

# yijing-bazi-mcp

一个基于MCP（Model Context Protocol）协议的专业易经八字分析服务器，为AI助手提供传统中华文化分析能力。本项目集成了易经卦象分析、八字命理推算、综合运势预测等功能，支持多种AI客户端接入。 📢 重要提示： 此项目已发布到 NPM，现在可以： - 在任意目录使用 npx yijing-bazi-mcp 命令 - 通过 npm install -g yijing-bazi-mc…

# 易经八字分析MCP服务器

一个基于MCP（Model Context Protocol）协议的专业易经八字分析服务器，为AI助手提供传统中华文化分析能力。本项目集成了易经卦象分析、八字命理推算、综合运势预测等功能，支持多种AI客户端接入。

> **📢 重要提示：** 此项目已发布到 NPM，现在可以：
> - 在任意目录使用 `npx yijing-bazi-mcp` 命令
> - 通过 `npm install -g yijing-bazi-mcp` 全局安装
> - 支持版本指定，如 `npx yijing-bazi-mcp@latest`

## ✨ 核心特性

### 🔮 易经分析系统
- **多种起卦方式**：铜钱法、蓍草法、时间法、数字法
- **专业卦象解读**：本卦、变卦、互卦全面分析
- **智能决策建议**：基于卦象提供实用指导
- **上下文理解**：结合具体问题场景分析

### 🌟 八字命理系统
- **精准八字排盘**：支持公历/农历转换
- **全面性格分析**：五行、十神、格局分析
- **运势预测**：大运、流年、月运详细预测
- **多维度分析**：事业、财运、感情、健康

### 🔄 综合分析引擎
- **易经八字融合**：传统文化深度结合
- **智能关联分析**：多系统交叉验证
- **个性化咨询**：针对性命理建议
- **案例学习库**：丰富的实战案例

### 🚀 技术架构
- **标准协议支持**：完全兼容MCP协议规范
- **模块化设计**：引擎分离，易于扩展
- **智能缓存**：提升响应速度
- **完整日志**：便于调试和监控

## 🛠️ 环境要求

- **Node.js**: 18.0.0 或更高版本
- **npm**: 最新版本
- **操作系统**: Windows/macOS/Linux

## 📦 快速安装

### 方式一：本地安装

```bash
# 下载项目包
# 解压到本地目录
cd yijing-bazi-mcp

# 安装依赖
npm install

# 验证安装
node src/index.js --version
```

### 方式二：全局安装（推荐）

```bash
# 全局安装
npm install -g .

# 验证安装
yijing-bazi-mcp --version

# 本地开发运行（当前推荐）
node src/index.js

# 或使用 npm exec（本地项目）
npm exec yijing-bazi-mcp

# 或使用 npx（需要先发布到 NPM）
npx yijing-bazi-mcp

# 注意：这些命令会直接启动 MCP 服务器，而不是显示版本信息
```

## 🚀 启动服务

### MCP模式（标准协议）

适用于Claude Desktop、Cherry Studio等MCP客户端：

```bash
# 开发模式（自动重启）
npm run dev

# 生产模式
npm start
```

## 🔧 客户端配置

### Claude Desktop

**第一步：获取项目**

**选项 A：从 NPM 安装（推荐）**
```bash
# 全局安装
npm install -g yijing-bazi-mcp

# 或使用 npx（可在任意目录运行）
npx yijing-bazi-mcp@latest
```

**选项 B：本地开发/测试（当前推荐）**
```bash
# 克隆或下载项目
git clone 
cd yijing-bazi-mcp

# 安装依赖
npm install

# 测试运行
node src/index.js
```

**第二步：配置 Claude Desktop**

编辑 `claude_desktop_config.json` 文件：

**方式一：使用 npx（推荐）**
```json
{
  "mcpServers": {
    "yijing-bazi": {
      "command": "npx",
      "args": ["yijing-bazi-mcp@latest"],
      "env": {
        "LOG_LEVEL": "info",
        "NODE_ENV": "production"
      }
    }
  }
}
```

**注意：** 现在不再需要 `cwd` 参数，可以在任意目录运行

**方式二：使用本地项目（当前推荐）**
```json
{
  "mcpServers": {
    "yijing-bazi": {
      "command": "node",
      "args": ["src/index.js"],
      "cwd": "完整路径/yijing-bazi-mcp",
      "env": {
        "LOG_LEVEL": "info",
        "NODE_ENV": "development"
      }
    }
  }
}
```

**配置文件位置：**
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**方式二：直接调用**
```json
{
  "mcpServers": {
    "yijing-bazi": {
      "command": "node",
      "args": ["完整路径/yijing-bazi-mcp/src/index.js"],
      "env": {
        "LOG_LEVEL": "info"
      }
    }
  }
}
```

**Windows示例路径**：
```json
"cwd": "E:\\桌面\\项目资源\\腾讯云\\baidu-netdisk-auto-delete"
"args": ["E:\\桌面\\项目资源\\腾讯云\\baidu-netdisk-auto-delete\\src\\index.js"]
```

### Trae AI / Cursor IDE

在IDE的MCP设置中添加：

**方式一：使用 npm exec（推荐）**
```json
{
  "mcpServers": {
    "yijing-bazi": {
      "command": "npm",
      "args": ["exec", "yijing-bazi-mcp"],
      "cwd": "项目完整路径",
      "env": {
        "NODE_ENV": "development"
      }
    }
  }
}
```

**方式一备选：使用 npx（推荐）**
```json
{
  "mcpServers": {
    "yijing-bazi": {
      "command": "npx",
      "args": ["yijing-bazi-mcp@latest"],
      "env": {
        "NODE_ENV": "development"
      }
    }
  }
}
```

**方式二：直接调用**
```json
{
  "mcpServers": {
    "yijing-bazi": {
      "command": "node",
      "args": ["src/index.js"],
      "cwd": "项目完整路径",
      "env": {
        "NODE_ENV": "development"
      }
    }
  }
}
```

### Cherry Studio

1. 打开设置 → MCP服务器
2. 添加新服务器：
   - **名称**: `易经八字分析服务器`
   - **类型**: `STDIO`
   - **命令**: `npm`（推荐）、`npx`（如果可用）或 `node`
   - **参数**: `exec yijing-bazi-mcp`（npm方式）、`yijing-bazi-mcp`（npx方式）或 `完整路径/yijing-bazi-mcp/src/index.js`（node方式）
   - **工作目录**: `完整路径/yijing-bazi-mcp`

## 🛠️ 可用工具

### 易经工具

| 工具名称 | 功能描述 | 主要参数 |
|---------|---------|----------|
| `yijing_generate_hexagram` | 生成卦象 | question, method, context |
| `yijing_interpret` | 解读卦象 | hexagram, focus, detail_level |
| `yijing_advise` | 决策建议 | hexagram, question, time_frame |

### 八字工具

| 工具名称 | 功能描述 | 主要参数 |
|---------|---------|----------|
| `bazi_generate_chart` | 生成八字排盘 | birth_time, gender, timezone |
| `bazi_analyze` | 八字分析 | chart, analysis_type, detail_level |
| `bazi_forecast` | 运势预测 | chart, period_type, focus_aspects |

### 综合分析

| 工具名称 | 功能描述 | 主要参数 |
|---------|---------|----------|
| `combined_analysis` | 综合分析 | bazi_chart, hexagram, question |
| `destiny_consult` | 命理咨询 | birth_info, question, consultation_type |

### 学习功能

| 工具名称 | 功能描述 | 主要参数 |
|---------|---------|----------|
| `knowledge_learn` | 知识学习 | topic, level, learning_type |
| `case_study` | 案例研究 | case_id, system, category |

## 📖 使用示例

### 易经起卦示例

```json
{
  "tool": "yijing_generate_hexagram",
  "params": {
    "question": "今年是否适合创业？",
    "method": "coin",
    "context": "目前在大公司工作，考虑自主创业"
  }
}
```

### 八字分析示例

```json
{
  "tool": "bazi_generate_chart",
  "params": {
    "birth_time": "1990-05-15T10:30:00+08:00",
    "gender": "male",
    "is_lunar": false,
    "timezone": "Asia/Shanghai"
  }
}
```

### 综合分析示例

```json
{
  "tool": "combined_analysis",
  "params": {
    "birth_time": "1990-05-15T10:30:00+08:00",
    "gender": "male",
    "question": "未来三年的事业发展方向",
    "analysis_focus": ["career", "wealth", "timing"]
  }
}
```

## 🏗️ 项目架构

```
易经八字分析MCP服务器/
├── 📁 .promptx/              # PromptX AI配置
│   ├── pouch.json           # 项目配置
│   └── resource/            # 资源文件
├── 📁 src/                  # 源代码目录
│   ├── 📁 engines/          # 核心分析引擎
│   │   ├── yijing-engine.js        # 易经分析引擎
│   │   ├── bazi-engine.js          # 八字分析引擎
│   │   ├── combined-engine.js      # 综合分析引擎
│   │   ├── combined-analysis-engine.js # 深度分析引擎
│   │   └── knowledge-engine.js     # 知识学习引擎
│   ├── 📁 data/             # 数据库模块
│   │   ├── hexagram-database.js    # 卦象数据库
│   │   ├── bazi-database.js        # 八字数据库
│   │   └── knowledge-database.js   # 知识库
│   ├── 📁 utils/            # 工具函数
│   │   ├── logger.js              # 日志系统
│   │   ├── error-handler.js       # 错误处理
│   │   ├── validator.js           # 参数验证
│   │   ├── cache.js               # 缓存管理
│   │   ├── date-utils.js          # 日期工具
│   │   ├── yijing-calculator.js   # 易经计算
│   │   ├── bazi-calculator.js     # 八字计算
│   │   ├── analysis-integrator.js # 分析整合
│   │   ├── search-engine.js       # 搜索引擎
│   │   ├── performance.js         # 性能监控
│   │   └── validation.js          # 数据验证
│   ├── 📁 config/           # 配置文件
│   │   └── config.js              # 主配置文件
│   ├── index.js             # MCP服务器入口

├── 📄 mcp-config.json       # MCP服务器配置
├── 📄 start-mcp-servers.js  # 服务器启动脚本
├── 📄 stop-mcp-servers.js   # 服务器停止脚本
├── 📄 package.json          # 项目依赖配置
└── 📄 README.md             # 项目说明文档
```

## 🧪 测试与调试

### 运行测试

```bash
# 测试八字生成功能
node -e "const { YijingBaziMCPServer } = require('./src/index.js'); const server = new YijingBaziMCPServer(); server.baziEngine.generateChart({birth_datetime: '1990-05-15T10:30:00+08:00', timezone: 'Asia/Shanghai', gender: 'male'}).then(result => console.log('测试成功:', JSON.stringify(result, null, 2))).catch(err => console.error('测试失败:', err.message));"

# 测试易经起卦功能
node -e "const { YijingBaziMCPServer } = require('./src/index.js'); const server = new YijingBaziMCPServer(); server.yijingEngine.generateHexagram({method: 'random', question: '测试问题'}).then(result => console.log('起卦成功:', JSON.stringify(result, null, 2))).catch(err => console.error('起卦失败:', err.message));"

# 查看服务器启动状态
node src/index.js
```

### 调试模式

```bash
# Windows PowerShell调试
$env:LOG_LEVEL="debug"; node src/index.js

# 查看日志文件
Get-Content logs/app.log -Wait

# 或使用记事本查看
notepad logs/app.log
```

### 故障排除

#### 常见问题及解决方案

**1. "could not determine executable to run" 错误**
```bash
# 解决方案A：使用最新版本
npx yijing-bazi-mcp@latest

# 解决方案B：清除 NPM 缓存
npm cache clean --force

# 解决方案C：使用本地开发方式（如果在项目目录内）
node src/index.js
```

**2. "spawn npx ENOENT" 错误**
```bash
# 解决方案：使用 npm exec 替代 npx
# 将配置中的 "command": "npx" 改为 "command": "npm"
# 将 "args": ["yijing-bazi-mcp"] 改为 "args": ["exec", "yijing-bazi-mcp"]
```

**2. "MCP 服务器启动失败" 错误**
```bash
# 检查步骤：
# 1. 验证 Node.js 版本
node --version  # 需要 18.0.0+

# 2. 检查项目依赖
npm install

# 3. 测试直接启动
node src/index.js

# 4. 测试 npm exec
npm exec yijing-bazi-mcp
```

**3. 路径配置问题**
```json
// Windows 路径示例（注意双反斜杠）
{
  "mcpServers": {
    "yijing-bazi": {
      "command": "npm",
      "args": ["exec", "yijing-bazi-mcp"],
      "cwd": "E:\\桌面\\项目资源\\腾讯云\\baidu-netdisk-auto-delete",
      "env": {
        "LOG_LEVEL": "info"
      }
    }
  }
}
```

**4. 权限问题**
```bash
# 确保有执行权限（Linux/Mac）
chmod +x src/index.js

# Windows 以管理员身份运行终端
```

#### 测试配置

运行测试脚本验证配置：
```bash
# 运行配置测试
node test-npx.js

# 手动测试各种启动方式
node src/index.js                    # 直接启动
npm exec yijing-bazi-mcp            # npm exec 方式
npx yijing-bazi-mcp                 # npx 方式（如果可用）
```

### 环境变量配置

可选创建 `.env` 文件（项目已有默认配置）：

```bash
# 日志配置
LOG_LEVEL=info
NODE_ENV=production

# MCP配置
SERVER_NAME=yijing-bazi-mcp-server
SERVER_VERSION=1.0.0

# 功能开关
ENABLE_CACHE=true
ENABLE_PERFORMANCE_MONITORING=true
```

## 📚 文档资源

- 📁 [项目结构](#🏗️-项目架构) - 详细的代码组织说明
- 🛠️ [工具列表](#🛠️-可用工具) - 完整的API工具文档
- 📖 [使用示例](#📖-使用示例) - 实际调用案例
- 🔧 [配置指南](#🔧-客户端配置) - 各种客户端配置方法

## 🚀 发布到魔塔社区

### NPX 调用方法

魔塔社区用户可以直接通过 npx 使用本项目：

```bash
# 直接运行（推荐）
npx yijing-bazi-mcp@latest

# 或者全局安装后使用
npm install -g yijing-bazi-mcp
yijing-bazi-mcp
```

### 魔塔社区配置示例

在您的 AI 客户端中配置 MCP 服务器：

```json
{
  "mcpServers": {
    "yijing-bazi": {
      "command": "npx",
      "args": ["yijing-bazi-mcp@latest"],
      "env": {
        "LOG_LEVEL": "info"
      }
    }
  }
}
```

### 功能特性

- 🔮 **八字分析**：基于出生时间进行命理分析
- 📿 **易经卦象**：提供卦象解读和占卜功能
- 🧠 **智能问答**：结合传统文化知识的AI对话
- 🔄 **实时计算**：动态生成个性化分析结果
- 📊 **详细报告**：提供全面的命理解读报告

## 🤝 开发贡献

### 本地开发

1. **修改代码** - 直接编辑源文件
2. **测试功能** - 使用上述测试命令验证
3. **查看日志** - 检查 `logs/` 目录下的日志文件
4. **重启服务** - 重新启动MCP客户端以加载更改

### 开发规范

- 保持代码风格一致
- 添加必要的错误处理
- 更新相关注释和文档
- 测试新功能的稳定性

### 问题反馈

如遇到问题，请检查：
1. Node.js版本是否符合要求（18+）
2. 依赖包是否正确安装
3. 路径配置是否正确
4. 日志文件中的错误信息

## 📄 版本信息

- **当前版本**: 1.0.0
- **发布日期**: 2024年
- **兼容性**: MCP协议标准
- **Node.js**: 18.0.0+

## 🙏 致谢

- 🔗 [MCP协议](https://modelcontextprotocol.io/) - 提供标准化AI工具协议
- 📅 [lunar-javascript](https://github.com/6tail/lunar-javascript) - 精确的农历计算库
- 🎯 [PromptX](https://promptx.ai/) - AI开发工具支持
- 📚 传统易学文化 - 为项目提供深厚理论基础
- 👥 开源社区 - 持续的支持和贡献

## ⚠️ 免责声明

本项目仅供学习研究使用，分析结果仅供参考，不构成任何决策建议。使用者应理性对待分析结果，重要决策请结合实际情况综合考虑。

---

**🌟 专业的易经八字分析MCP服务器 🌟**

*传统文化与现代AI技术的完美结合*

**Official site: ** [https://github.com/SiwuXue/yijing-bazi-mcp-server](https://github.com/SiwuXue/yijing-bazi-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `memory`
- Tags: `knowledge and memory`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `yijing-bazi-mcp@latest`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/wuai60-yijing-bazi.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
