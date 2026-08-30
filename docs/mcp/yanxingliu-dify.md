---
title: "Dify MCP 服务器"
description: "用于使用[Dify](https://github.com/langgenius/dify)的服务器。它通过调用MCP的工具来实现Dify工作流程的调用。"
---

# Dify MCP 服务器

用于使用[Dify](https://github.com/langgenius/dify)的服务器。它通过调用MCP的工具来实现Dify工作流程的调用。

# Model Context Protocol (MCP) Server for dify workflows
一个简单的MCP服务器实现，用于使用[dify](https://github.com/langgenius/dify)。通过调用MCP的工具来实现Dify工作流的调用。
## 🔨安装
可以通过[Smithery](https://smithery.ai/server/dify-mcp-server)或手动方式安装该服务器。两种方法都需要Config.yaml文件。因此，在安装之前我们需要准备好它。

### 准备config.yaml
在使用mcp服务器之前，您应该准备一个config.yaml文件来保存您的dify_base_url和dify_sks。示例配置如下：
```yaml
dify_base_url: "https://cloud.dify.ai/v1"
dify_app_sks:
  - "app-sk1"
  - "app-sk2"
```
您可以在终端中运行以下命令快速创建一个配置文件：
```
mkdir -p ~/tools && cat > ~/tools/config.yaml
```

**官方网站：** [https://github.com/YanxingLiu/dify-mcp-server](https://github.com/YanxingLiu/dify-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`--directory ${DIFY_MCP_SERVER_PATH} run dify_mcp_server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/yanxingliu-dify.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
