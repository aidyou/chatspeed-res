---
title: "Perplexity Ask"
description: "一种MCP服务器实现，它集成了Sonar API，为克劳德提供了无与伦比的实时、全网研究能力。"
---

# Perplexity Ask

一种MCP服务器实现，它集成了Sonar API，为克劳德提供了无与伦比的实时、全网研究能力。

# Perplexity Ask MCP 服务器

一个集成了 Sonar API 的 MCP 服务器实现，为 Claude 提供无与伦比的实时全网研究功能。

## 工具

- **perplexity_ask**
  - 通过与 Sonar API 进行对话来执行实时网络搜索。
  - **输入:**
    - `messages` (数组): 会话消息数组。
      - 每条消息必须包含：
        - `role` (字符串): 消息的角色（例如，`system`, `user`, `assistant`）。
        - `content` (字符串): 消息的内容。

## 配置

### 第一步： 

克隆此仓库：

```bash
git clone git@github.com:ppl-ai/modelcontextprotocol.git
```

导航到 `perplexity-ask` 目录并安装必要的依赖项：

```bash
cd modelcontextprotocol/perplexity-ask && npm install
```

### 第二步：获取 Sonar API 密钥

1. 注册 [Sonar API 账户](https://docs.perplexity.ai/guides/getting-started)。
2. 按照账户设置说明从开发者仪表板生成您的 API 密钥。
3. 在环境变量中将 API 密钥设置为 `PERPLEXITY_API_KEY`。

### 第三步：配置 Claude 桌面版

1. 在[这里](https://claude.ai/download)下载 Claude 桌面版。 

2. 将以下内容添加到您的 `claude_desktop_config.json` 文件中：

```json
{
  "mcpServers": {
    "perplexity-ask": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e",
        "PERPLEXITY_API_KEY",
        "mcp/perplexity-ask"
      ],
      "env": {
        "PERPLEXITY_API_KEY": "YOUR_API_KEY_HERE"
      }
    }
  }
}
```

### NPX

```json
{
  "mcpServers": {
    "perplexity-ask": {
      "command": "npx",
      "args": [
        "-y",
        "server-perplexity-ask"
      ],
      "env": {
        "PERPLEXITY_API_KEY": "YOUR_API_KEY_HERE"
      }
    }
  }
}
```

您可以使用以下命令访问文件：

```bash
vim ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

### 第四步：构建 Docker 镜像

Docker 构建命令：

```bash
docker build -t mcp/perplexity-ask:latest -f Dockerfile .
```

### 第五步：测试

让我们确保 Claude 桌面版已经识别我们在 `perplexity-ask` 服务器中暴露的两个工具。您可以通过查找锤子图标来确认这一点：

点击锤子图标后，您应该能看到 Filesystem MCP 服务器提供的工具：

如果您看到这两个工具，这意味着集成已激活。恭喜！这意味着 Claude 现在可以使用 Perplexity 了。然后您可以像使用 Perplexity 网页应用程序一样使用它。

### 第六步：高级参数

目前使用的搜索参数是默认值。您可以在 `index.ts` 脚本中直接修改 API 调用中的任何搜索参数。为此，请参考官方 [API 文档](https://docs.perplexity.ai/api-reference/chat-completions)。

### 故障排除

Claude 文档提供了一个非常优秀的 [故障排除指南](https://modelcontextprotocol.io/docs/tools/debugging)，您可以参考。但如果您需要额外的支持或 [报告错误](https://github.com/ppl-ai/api-discussion/issues)，仍然可以通过 api@perplexity.ai 联系我们。

## 许可证

此 MCP 服务器根据 MIT 许可证发布。这意味着您可以自由地使用、修改和分发该软件，但需遵守 MIT 许可证的条款和条件。更多详情，请参见项目仓库中的 LICENSE 文件。

**官方网站：** [https://github.com/ppl-ai/modelcontextprotocol](https://github.com/ppl-ai/modelcontextprotocol)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`
- 标签：`search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y server-perplexity-ask`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/ppl-ai-modelcontextprotocol.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
