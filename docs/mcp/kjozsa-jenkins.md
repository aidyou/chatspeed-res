---
title: "Jenkins-MCP管理工具"
description: "通过可配置的MCP服务器，启用管理Jenkins操作的功能，例如列出作业、触发构建和检查构建状态。"
---

# Jenkins-MCP管理工具

通过可配置的MCP服务器，启用管理Jenkins操作的功能，例如列出作业、触发构建和检查构建状态。

# Jenkins MCP
[Smithery](https://smithery.ai/server/@kjozsa/jenkins-mcp)
用于管理Jenkins操作的MCP服务器。

  

## 安装
### 通过Smithery安装

要通过[Smithery](https://smithery.ai/server/@kjozsa/jenkins-mcp)自动为Claude Desktop安装Jenkins MCP：

```bash
npx -y @smithery/cli install @kjozsa/jenkins-mcp --client claude
```

### 手动安装
```bash
uvx install jenkins-mcp
```

## 配置
使用以下JSON配置片段添加MCP服务器：

```json
{
  "mcpServers": {
    "jenkins-mcp": {
      "command": "uvx",
      "args": ["jenkins-mcp"],
      "env": {
        "JENKINS_URL": "https://your-jenkins-server/",
        "JENKINS_USERNAME": "your-username",
        "JENKINS_PASSWORD": "your-password",
        "JENKINS_USE_API_TOKEN": "false"
      }
    }
  }
}
```

## CSRF Crumb处理

Jenkins通过“crumbs”（一种令牌）来实现CSRF保护，这些令牌必须随POST请求一起包含。此MCP服务器以两种方式处理CSRF crumbs：

1. **默认模式**：自动获取并包括构建请求中的CSRF crumbs
   - 使用会话cookie来保持Web会话
   - 在后台处理所有CSRF保护

2. **API令牌模式**：使用免于CSRF保护的Jenkins API令牌
   - 设置`JENKINS_USE_API_TOKEN=true`
   - 将`JENKINS_PASSWORD`设置为您的API令牌而不是密码
   - 适用于Jenkins 2.96+版本，该版本在API令牌认证时不需要crumbs

您可以在Jenkins中生成API令牌：用户 → 配置 → API令牌 → 添加新令牌

## 功能
- 列出Jenkins作业
- 触发带有可选参数的构建
- 检查构建状态
- 为安全API访问处理CSRF crumbs

## 开发
```bash
# Install dependencies
uv pip install -r requirements.txt

# Run in dev mode with Inspector
mcp dev jenkins_mcp/server.py
```

**官方网站：** [https://github.com/kjozsa/jenkins-mcp](https://github.com/kjozsa/jenkins-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `os automation`, `monitoring`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`jenkins-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/kjozsa-jenkins.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
