---
title: "中文名：思维导图MCP服务器"
description: "一种模型上下文协议服务器，可以将Markdown内容转换为交互式思维导图，使人工智能助手能够通过HTML内容或保存的文件来可视化分层信息。"
---

# 中文名：思维导图MCP服务器

一种模型上下文协议服务器，可以将Markdown内容转换为交互式思维导图，使人工智能助手能够通过HTML内容或保存的文件来可视化分层信息。

# Mindmap MCP 服务器

  

一个用于将 Markdown 内容转换为交互式思维导图的模型上下文协议 (MCP) 服务器。

## 安装

```bash
pip install mindmap-mcp-server
```

或者使用 `uvx`：

```bash
uvx mindmap-mcp-server
```

或者使用 `docker`，更安全且更简单。

## 前提条件

当使用命令 `python` 或 `uvx` 运行服务器时，此软件包需要安装 Node.js。

## 使用方法

### 使用 Claude Desktop 或其他 MCP 客户端

将此服务器添加到您的 `claude_desktop_config.json` 中：

 
 使用 `uvx`：

```json
{
  "mcpServers": {
    "mindmap": {
      "command": "uvx",
      "args": ["mindmap-mcp-server", "--return-type", "html"]
    }
  }
}
```

或  

推荐：

```json
{
  "mcpServers": {
    "mindmap": {
      "command": "uvx",
      "args": ["mindmap-mcp-server", "--return-type", "filePath"]
    }
  }
}
```

我们使用 `--return-type` 来指定思维导图内容的返回类型，您可以根据需要选择 `html` 或 `filePath`。   
`html` 将返回整个思维导图的 HTML 内容，您可以在 AI 客户端的工件中预览； 

![return_html_content](/mcp-assets/443bba13eb9b9e82bc3c4a59a0bf475b.png)

![html_preview](/mcp-assets/eaf973752a9347f3efb69551224a9b97.png)

`filePath` 将把思维导图保存到文件并返回文件路径，您可以在浏览器中打开它。这可以**节省您的令牌**！

![generate_file](/mcp-assets/97fc0f89f2a0d93dee93308b90e4e011.png)

![file_to_open](/mcp-assets/1f83cf08af81f6375480f8fe3b5ed54e.png) 

使用 `python`：

使用此仓库中的[特定 Python 文件](https://github.com/YuChenSSR/mindmap-mcp-server/blob/main/mindmap_mcp_server/server.py)：

```json
{
  "mcpServers": {
    "mindmap": {
      "command": "python",
      "args": ["/path/to/your/mindmap_mcp_server/server.py", "--return-type", "html"]
    }
  }
}
```

  
或   

```json
{
  "mcpServers": {
    "mindmap": {
      "command": "python",
      "args": ["/path/to/your/mindmap_mcp_server/server.py", "--return-type", "filePath"]
    }
  }
}
```
我们使用 `--return-type` 来指定思维导图内容的返回类型，您可以根据需要选择 `html` 或 `filePath`。有关更多详细信息，请参阅使用 `uvx` 部分。

使用 `docker`：

首先，拉取镜像：

```bash
docker pull ychen94/mindmap-converter-mcp
```

其次，设置服务器：

```json
{
  "mcpServers": {
    "mindmap-converter": {
      "command": "docker",
      "args": ["run", "--rm", "-i", "-v", "/path/to/output/folder:/output", "ychen94/mindmap-converter-mcp:latest"]
    }
  }
}
```
⚠️ 请将 `/path/to/output/folder` 替换为您系统上希望保存思维导图的实际路径，例如在 macOS 上为 `/Users/username/Downloads` 或在 Windows 上为 `C:\\Users\\username\\Downloads`。

**Docker 容器提供的工具**
该服务器提供了以下 MCP 工具：
```

1. **markdown-to-mindmap-content**  
将 Markdown 转换为 HTML 思维导图并返回整个 HTML 内容。  
在 `docker` 命令中，您不需要使用参数 `-v` 和 `/path/to/output/folder:/output`。  
**参数**:   
    •	markdown (字符串，必填)：要转换的 Markdown 内容  
    •	toolbar (布尔值，可选)：是否显示工具栏（默认：true）  
**最适合用于**：简单的思维导图，HTML 内容大小不是问题的情况。您可以使用 AI 客户端中的 **artifact** 预览思维导图。  
2. **markdown-to-mindmap-file**  
将 Markdown 转换为 HTML 思维导图，并将其保存到挂载目录中的文件。  
**参数**:  
    •	markdown (字符串，必填)：要转换的 Markdown 内容  
    •	filename (字符串，可选)：自定义文件名（默认：自动生成的时间戳名称）  
    •	toolbar (布尔值，可选)：是否显示工具栏（默认：true）  
**最适合用于**：复杂的思维导图或希望**保存令牌**以供以后使用的情况。  
您可以在浏览器中打开 html 文件来查看思维导图。此外，您还可以使用 [iterm-mcp-server](https://github.com/ferrislucas/iterm-mcp) 或其他终端的 mcp 服务器，在不中断工作流程的情况下在浏览器中打开文件。

### 故障排除

**找不到文件**  
如果您的思维导图文件无法访问：  
    1	检查是否已正确将卷挂载到 Docker 容器  
    2	确保路径格式对于您的操作系统是正确的  
    3	确保 Docker 有权访问该目录  

**找不到 Docker 命令**  
    1	验证 Docker 是否已安装并在您的 PATH 中  
    2	尝试使用 Docker 的绝对路径  

**Claude 中未出现服务器**  
    1	在配置更改后重启 Claude for Desktop  
    2	检查 Claude 日志中的连接错误  
    3	验证 Docker 是否正在运行  

**高级用法  
与其他 MCP 客户端一起使用**  
此服务器不仅适用于 Claude for Desktop，还适用于任何兼容 MCP 的客户端。该服务器实现了 Model Context Protocol (MCP) 1.0 规范。  

## 注意事项

三种安装方法已在 macOS 和 Linux 上成功测试。

对于使用 `npx` 安装此 MCP 时遇到问题的 Windows 用户，请考虑使用 Docker 方法。或者，如果您使用 Visual Studio Code，则 ["Markmap"](https://link.1) 扩展可能比使用命令行工具更简单。

## 功能

此服务器提供了一个使用 `markmap-cli` 库将 Markdown 内容转换为思维导图的工具：

- 将 Markdown 转换为交互式思维导图 HTML
- 可创建离线可用的思维导图
- 可隐藏工具栏
- 返回 HTML 内容或文件路径

## 示例

在 Claude 中，您可以这样询问：

1. 
"**请使用思维导图工具为以下 Markdown 代码生成思维导图:**
```
#8
```
"

如果您想将思维导图保存到文件中，然后使用 iTerm MCP 服务器在浏览器中打开它：

2. 
"**使用思维导图工具为以下 markdown 输入代码生成思维导图，然后使用 iterm 打开生成的 html 文件。
输入代码：**
```
#9
```

3.
"**思考将大象放入冰箱的过程，并提供一个思维导图。使用终端打开它。**"

    
查看结果
    
![aiworkflow](/mcp-assets/fb26494393244c974e67c762ebbf172d.png)

![mindmapinbrowser](/mcp-assets/b11757c00fbf1fae1849db18a0d4bbd3.png)

 

 
**还有更多**

## 许可证

该项目采用 MIT 许可证。
更多详情，请参阅 [此项目仓库](https://link.2) 中的 LICENSE 文件。

---
 
如果这个项目对你有帮助，请考虑给它一个 Star ⭐️

技术的进步应该惠及所有人，而不是剥削大众。
```

**官方网站：** [https://github.com/YuChenSSR/mindmap-mcp-server](https://github.com/YuChenSSR/mindmap-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`memory`, `files`
- 标签：`knowledge and memory`, `file systems`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`mindmap-mcp-server --return-type html`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/yuchenssr-mindmap.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
