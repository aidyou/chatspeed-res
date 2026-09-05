---
title: "Dart知识管理服务"
description: "一个官方的AI模型上下文协议服务器， enables AI助手通过提示和工具创建/管理任务和文档来与Dart项目管理进行交互。"
---

# Dart知识管理服务

一个官方的AI模型上下文协议服务器， enables AI助手通过提示和工具创建/管理任务和文档来与Dart项目管理进行交互。

Dart MCP Server

  

    

    

  

[Dart](https://itsdart.com?nr=1) 是由 AI 驱动的项目管理工具。

`dart-mcp-server` 是 Dart 的官方 AI [模型上下文协议 (MCP)](https://github.com/modelcontextprotocol) 服务器。

- [特性](#features)
  - [提示词](#prompts)
  - [资源模板](#resource-templates)
  - [工具](#tools)
    - [任务管理](#task-management)
    - [文档管理](#document-management)
- [设置](#setup)
  - [查找客户端的 MCP 设置文件](#find-the-mcp-settings-file-for-the-client)
    - [Claude](#claude)
    - [Cline](#cline)
    - [其他任何客户端](#any-other-client)
  - [设置 MCP 服务器](#set-up-the-mcp-server)
  - [变体：使用 Docker 设置](#variant-setup-with-docker)
- [帮助和资源](#help-and-resources)
- [贡献](#contributing)
- [许可](#license)

## 特性

### 提示词

以下提示词可用：

- `create-task` - 在 Dart 中创建一个带有标题、描述、状态、优先级和分配人的新任务
- `create-doc` - 在 Dart 中创建一个带有标题、文本内容和文件夹的新文档
- `summarize-tasks` - 获取任务摘要，可选按状态和分配人过滤

这些提示词使得 AI 助手能够轻松执行 Dart 中的常见操作，而无需理解底层 API 细节。

### 资源模板

以下资源可用：

- `dart-config:` - 关于用户空间的配置信息
- `dart-task:///{taskId}` - 关于特定任务的详细信息
- `dart-doc:///{docId}` - 关于特定文档的详细信息

### 工具

以下工具可用：

#### 任务管理

- `get_config` - 获取关于用户空间的信息，包括可用的分配人、看板、文件夹、状态、标签、优先级和规模
- `list_tasks` - 列出任务，可选按分配人、状态、看板、优先级、截止日期等过滤
- `create_task` - 创建一个带有标题、描述、状态、优先级、规模、日期、看板、分配人、标签和父任务的新任务
- `get_task` - 通过 ID 检索现有任务
- `update_task` - 更新现有任务的属性
- `delete_task` - 将任务移动到回收站（可恢复）

#### 文档管理

- `list_docs` - 列出文档，可选按文件夹、标题、文本内容等过滤
- `create_doc` - 创建一个带有标题、文本内容和文件夹的新文档
- `get_doc` - 通过 ID 检索现有文档
- `update_doc` - 更新现有文档的属性
- `delete_doc` - 将文档移动到回收站（可恢复）

每个工具都支持全面的输入验证，并返回结构化的 JSON 响应。

## 设置

运行MCP服务器最简单的方法是使用`npx`，但也可以使用Docker设置。

### 查找客户端的MCP设置文件

#### Claude

1. 根据需要[安装Claude Desktop](https://claude.ai/download)
2. 打开`claude_desktop_config.json`文件，可以通过打开Claude Desktop应用程序，进入其设置，打开“开发者”选项卡，并点击“编辑配置”按钮来定位该文件
3. 按照下面的“设置MCP服务器”步骤操作

#### Cline

1. 根据需要在您的IDE中[安装Cline](https://cline.bot/)
2. 通过打开您的IDE，打开Cline侧边栏，点击顶部从左数第二个“MCP Servers”图标按钮，打开“已安装”标签页，并点击“配置MCP服务器”按钮来安装MCP服务器
3. 按照下面的“设置MCP服务器”步骤操作

#### 其他任何客户端

1. 找到MCP设置文件，通常是`[client]_mcp_settings.json`
2. 按照下面的“设置MCP服务器”步骤操作

### 设置MCP服务器

1. 根据需要[安装npx](https://nodejs.org/en/download)，它随Node一起提供
2. 从[您的Dart资料](https://app.itsdart.com/?settings=account)复制您的认证令牌
3. 将以下内容添加到您的MCP设置中，请确保将`dsa...`替换为您的实际Dart令牌

```json
   {
     "mcpServers": {
       "dart": {
         "command": "npx",
         "args": ["-y", "dart-mcp-server"],
         "env": {
           "DART_TOKEN": "dsa_..."
         }
       }
     }
   }
```

### 变体：使用Docker设置

如果上述`npx`设置不适合您，我们还提供了Docker设置。按照上面的说明找到MCP设置文件。

1. 根据需要[安装Docker](https://www.docker.com/products/docker-desktop/)
2. 使用`docker build -t mcp/dart .`构建Docker容器
3. 从[您的Dart资料](https://app.itsdart.com/?settings=account)复制您的认证令牌
4. 将以下内容添加到您的MCP设置中，请确保将`dsa...`替换为您的实际Dart令牌

```json
   {
     "mcpServers": {
       "dart": {
         "command": "docker",
         "args": ["run", "-i", "--rm", "-e", "DART_TOKEN", "mcp/dart"],
         "env": {
           "DART_TOKEN": "dsa_..."
         }
       }
     }
   }
```

## 帮助和资源

- [主页](https://www.itsdart.com/?nr=1)
- [Web应用](https://app.itsdart.com/)
- [帮助中心](https://help.itsdart.com/)
- [错误与功能](https://app.itsdart.com/p/r/JFyPnhL9En61)
- [库源代码](https://github.com/its-dart/dart-mcp-server/)
- [Discord聊天](https://discord.gg/RExv8jEkSh)
- 电子邮件联系我们: [support@itsdart.com](mailto:support@itsdart.com)

## 贡献

欢迎贡献！请提出问题或提交拉取请求。

## 许可证

此项目根据[MIT许可证](https://github.com/its-dart/dart-mcp-server/blob/HEAD/LICENSE)许可。

**官方网站：** [https://github.com/its-dart/dart-mcp-server](https://github.com/its-dart/dart-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`memory`
- 标签：`knowledge and memory`, `note taking`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y dart-mcp-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/its-dart-dart.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
