---
title: "网络搜索助手"
description: "一个自定义的MCP工具，将Perplexity AI的API与Claude桌面端集成，使Claude能够进行基于网络的研究并提供带引用的答案。"
---

# 网络搜索助手

一个自定义的MCP工具，将Perplexity AI的API与Claude桌面端集成，使Claude能够进行基于网络的研究并提供带引用的答案。

# Perplexity 工具 for Claude 桌面版

一个自定义的 MCP 工具，将 Perplexity AI 的 API 与 Claude 桌面版集成，允许 Claude 执行基于网络的研究并提供带有引用的答案。

## 安装前提条件

1. 安装 Git:
   - 对于 Mac: 
     - 首先通过在终端中粘贴以下内容安装 [Homebrew](https://brew.sh/):
```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
     - 然后安装 Git:
```bash
     brew install git
```
   - 对于 Windows:
     - 从 [git-scm.com](https://git-scm.com/downloads) 下载 Git
     - 运行安装程序

2. 安装 Node.js:
   - 对于 Mac: 
```bash
     brew install node
```
   - 对于 Windows:
     - 从 [nodejs.org](https://nodejs.org/) 下载
     - 运行安装程序

3. 通过运行以下命令验证安装：
```bash
git --version
node --version
```

## 工具安装

1. 克隆仓库
```bash
git clone https://github.com/letsbuildagent/perplexity-tool
cd perplexity-tool
```

2. 安装依赖项
```bash
npm install
```

3. 设置您的 API 密钥

您有两个选项：

选项 1（快速设置）:
- 打开 `server.js`
- 找到这一行:
```javascript
const PERPLEXITY_API_KEY = "YOUR-API-KEY-HERE";
```
- 将其替换为您的 Perplexity API 密钥

选项 2（最佳实践）:
- 创建一个 .env 文件：
```bash
  # 在 Mac/Linux 上:
  touch .env
  open .env
  
  # 在 Windows 上:
  notepad .env
```
  或者直接在文本编辑器中创建一个名为 `.env` 的新文件
- 将您的 API 密钥添加到 .env 文件中：
```
  PERPLEXITY_API_KEY=your-api-key-here
```
- 安装 dotenv:
```bash
  npm install dotenv
```
- 更新 server.js:
```javascript
  import 'dotenv/config'
  const PERPLEXITY_API_KEY = process.env.PERPLEXITY_API_KEY;
```

4. 配置 Claude 桌面版
- 打开 `~/Library/Application Support/Claude/claude_desktop_config.json`
- 添加此配置：
```json
{
  "mcpServers": {
    "perplexity-tool": {
      "command": "node",
      "args": [
        "/full/path/to/perplexity-tool/server.js"
      ]
    }
  }
}
```
将 `/full/path/to` 替换为您克隆仓库的实际路径。

5. 重启 Claude 桌面版

## 使用方法

安装完成后，您可以通过 Claude 使用该工具，并使用如下命令：

- "Ask Perplexity about recent developments in AI"
- "Use Perplexity to research the history of quantum computing"
- "Search Perplexity for information about climate change, focusing on the last month"

### 高级选项

您可以指定额外的参数：
- `temperature`: 控制响应的随机性 (0-2)
- `max_tokens`: 限制响应长度
- `search_domain_filter`: 限制搜索到特定域
- `search_recency_filter`: 按时间段过滤 (day/week/month/year)

## 故障排除

注：原文中的代码块和链接保持不变。如果需要具体的命令或配置示例，请补充完整信息。

1. 未找到 Git：
   - 确保你已正确安装 Git
   - 尝试重启你的终端
   - 在 Mac 上，确保 Homebrew 已添加到你的 PATH 中

2. Node.js 错误：
   - 使用 `node --version` 验证 Node.js 安装
   - 尝试重新安装 Node.js

3. API 密钥问题：
   - 确保你已正确复制了 API 密钥
   - 检查 .env 文件中是否有额外的空格
   - 如果使用选项 2，请验证 dotenv 是否已安装

4. 工具未在 Claude 中显示：
   - 检查 claude_desktop_config.json 中的路径
   - 确保路径指向你的 server.js 文件
   - 重启 Claude Desktop
   - 检查控制台是否有任何错误信息

## 许可证

MIT

## 安全提示

如果你打算分享代码或将其公开：
- 不要将你的 API 密钥提交到 Git
- 使用 .env 方法（选项 2）
- 将 .env 添加到你的 .gitignore 文件中

**官方网站：** [https://github.com/letsbuildagent/perplexity-tool](https://github.com/letsbuildagent/perplexity-tool)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`browser`
- 标签：`search`, `browser automation`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`/full/path/to/perplexity-tool/server.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/letsbuildagent-perplexity-tool.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
