---
title: "MCP邮件服务器工具"
description: "提供IMAP和SMTP功能，使开发人员能够无缝集成和自动化工作流来管理电子邮件服务。"
---

# MCP邮件服务器工具

提供IMAP和SMTP功能，使开发人员能够无缝集成和自动化工作流来管理电子邮件服务。

# mcp-email-server

[![Release](/mcp-assets/44568dba424b415d971809a279ce2b35.svg)](https://img.shields.io/github/v/release/ai-zerolab/mcp-email-server)
[![Build status](/mcp-assets/abc15660130701393306443a8e2a39cb.svg)](https://github.com/ai-zerolab/mcp-email-server/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](/mcp-assets/56374751c0b5213655ce0d5025025dc6.svg)](https://codecov.io/gh/ai-zerolab/mcp-email-server)
[![Commit activity](/mcp-assets/c488edaf3f16a47fb518204f08a6584b.svg)](https://img.shields.io/github/commit-activity/m/ai-zerolab/mcp-email-server)
[![License](/mcp-assets/3558c36785ba77f4575ce643a3a48f2a.svg)](https://img.shields.io/github/license/ai-zerolab/mcp-email-server)
[Smithery](https://smithery.ai/server/@ai-zerolab/mcp-email-server)

通过 MCP 服务器实现 IMAP 和 SMTP

- **Github 仓库**: 
- **文档** 

## 安装

### 手动安装

我们推荐使用 [uv](https://github.com/astral-sh/uv) 来管理您的环境。

尝试 `uvx mcp-email-server@latest ui` 进行配置，并为 mcp 客户端使用以下配置：

```json
{
  "mcpServers": {
    "zerolib-email": {
      "command": "uvx",
      "args": ["mcp-email-server@latest", "stdio"]
    }
  }
}
```

此包在 PyPI 上可用，因此您可以使用 `pip install mcp-email-server` 进行安装。

之后，使用 UI 配置您的电子邮件服务器：`mcp-email-server ui`

然后您可以在 [Claude Desktop](https://claude.ai/download) 中试用。如果您想将其与其他 mcp 客户端集成，请运行 `$which mcp-email-server` 获取路径，并在客户端中进行如下配置：

```json
{
  "mcpServers": {
    "zerolib-email": {
      "command": "{{ ENTRYPOINT }}",
      "args": ["stdio"]
    }
  }
}
```

如果 `docker` 可用，您可以尝试使用 docker 镜像，但可能需要通过 `MCP` 使用 `tools` 在客户端中进行配置。默认配置路径是 `~/.config/zerolib/mcp_email_server/config.toml`

```json
{
  "mcpServers": {
    "zerolib-email": {
      "command": "docker",
      "args": ["run", "-it", "ghcr.io/ai-zerolab/mcp-email-server:latest"]
    }
  }
}
```

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@ai-zerolab/mcp-email-server) 自动为 Claude Desktop 安装 Email Server：

```bash
npx -y @smithery/cli install @ai-zerolab/mcp-email-server --client claude
```

## 开发

此项目使用 [uv](https://github.com/ai-zerolab/uv) 管理。

尝试 `make install` 以安装虚拟环境并安装预提交钩子。

对于本地开发，请使用 `uv run mcp-email-server`。

## 发布新版本

- 在 [PyPI](https://pypi.org/) 上创建一个 API Token。
- 访问 [此页面](https://github.com/ai-zerolab/mcp-email-server/settings/secrets/actions/new)，将 API Token 添加到项目的密钥中，名称为 `PYPI_TOKEN`。
- 在 Github 上创建 [新发布](https://github.com/ai-zerolab/mcp-email-server/releases/new)。
- 创建格式为 `*.*.*` 的新标签。

更多详情请见 [这里](https://fpgmaas.github.io/cookiecutter-uv/features/cicd/#how-to-trigger-a-release)。

**官方网站：** [https://github.com/ai-zerolab/mcp-email-server](https://github.com/ai-zerolab/mcp-email-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`communication`
- 标签：`communication`, `developer tools`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`mcp-email-server@latest stdio`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/ai-zerolab-email.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
