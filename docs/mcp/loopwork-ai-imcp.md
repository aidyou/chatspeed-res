---
title: "iMCP服务"
description: "一个为您的信息、联系人等提供MCP服务器的macOS应用程序"
---

# iMCP服务

一个为您的信息、联系人等提供MCP服务器的macOS应用程序

iMCP 是一款 macOS 应用程序，用于将您的数字生活与 AI 连接起来。
它支持 [Claude Desktop](https://claude.ai/download) 以及越来越多的支持
[模型上下文协议 (MCP)](https://modelcontextprotocol.io/introduction) 的客户端列表。

## 功能

  

    

       width="48" height="48" alt="" role="presentation"/>
    

    

日历

    
查看和管理日历事件，包括使用可自定义设置（如重复、提醒和可用性状态）创建新事件。

  

  

    

       width="48" height="48" alt="" role="presentation"/>
    

    

联系人

    
访问关于您自己的联系信息，并按姓名、电话号码或电子邮件地址搜索您的联系人。

  

  

    

       width="48" height="48" alt="" role="presentation"/>
    

    

位置

    
访问当前位置数据，并在地址和地理坐标之间进行转换。

  

  

    

       width="48" height="48" alt="" role="presentation"/>
    

    

地图

    
提供地点搜索、路线指引、兴趣点查找、旅行时间估算和静态地图图像生成等位置服务。

  

  

    

       width="48" height="48" alt="" role="presentation"/>
    

    

消息

    
访问特定参与者在自定义日期范围内的消息历史记录。

  

  

    

       width="48" height="48" alt="" role="presentation"/>
    

    

提醒事项

    
查看并创建具有可自定义到期日期、优先级和提醒的不同提醒事项列表中的提醒事项。

  

  

    

       width="48" height="48" alt="" role="presentation"/>
    

    

天气

    
访问任何地点的当前天气状况，包括温度、风速和天气条件。

  

> [!TIP]
> 对于新的功能有建议？
> 请通过 
 联系我们。

## 开始使用

### 下载并打开应用程序

首先，[下载 iMCP 应用程序](https://iMCP.app/download)
（需要 macOS 15.3 或更高版本）。

 alt="首次启动时 iMCP 的截图" />

当您打开应用程序时，
会在菜单栏中看到一个
 />
图标。

点击此图标会显示 iMCP 菜单，该菜单中列出了所有可用的服务。最初，所有服务都会显示为灰色，表示它们处于非活动状态。

顶部的蓝色切换开关表示 MCP 服务器正在运行，并且已准备好与兼容 MCP 的客户端连接。

 alt="macOS权限对话框截图" />

### 激活服务

要激活某个服务，请点击其图标。系统将提示您一个权限对话框。例如，在激活日历访问时，您会看到一个对话框询问“`iMCP`希望完全访问您的日历”。点击允许完全访问继续。

> [!IMPORTANT]
> iMCP **不会** 收集或存储您的任何数据。
> 像 Claude Desktop 这样的客户端_确实会_在工具调用过程中将您的数据发送出去。

 alt="所有服务均已启用的iMCP截图" />

一旦被激活，每个服务的图标将从灰色变为它们特有的颜色——日历为红色、消息为绿色、位置为蓝色等。

重复这一过程以激活您想要启用的所有功能。这些权限遵循 Apple 的标准安全模型，使您可以完全控制 iMCP 可以访问哪些信息。

 -->

 -->

### 连接到 Claude Desktop

如果您尚未安装 Claude Desktop，可以[在此下载](https://claude.ai/download)。

打开 Claude Desktop 并转到“设置... (⌘,)”。点击设置面板侧边栏中的“开发者”，然后点击“编辑配置”。这将在
`~/Library/Application Support/Claude/claude_desktop_config.json` 创建一个配置文件。

要将 iMCP 连接到 Claude Desktop，请点击  />
\> “配置 Claude Desktop”。

这将添加或更新使用应用程序中捆绑的 `imcp-server` 可执行文件的 MCP 服务器配置。文件中的其他 MCP 服务器配置将被保留。

您也可以手动配置 Claude Desktop

点击  />
\> “复制服务器命令到剪贴板”。然后在编辑器中打开 `claude_desktop_config.json` 并输入以下内容：

```json
{
  "mcpServers" : {
    "iMCP" : {
      "command" : "{paste iMCP server command}"
    }
  }
}
```

 />

### 从 Claude Desktop 调用 iMCP 工具

退出并重新打开 Claude Desktop 应用程序。您将被提示批准连接。

> [!NOTE]
> 您可能会看到这个对话框两次；请两次都点击批准。

批准连接后，您现在应该在聊天框的右下角看到 🔨12。点击它可以看到由 iMCP 提供给 Claude 的所有工具列表。

   alt="启用工具后的 Claude Desktop 截图" />

现在您可以向 Claude 询问需要访问您的个人数据的问题，例如：
> "我这里的天气怎么样？"

Claude 将使用适当的工具检索此信息，为您提供准确、个性化的回答，而无需在对话中手动分享这些数据。

   alt="Claude 对用户消息 '我这里的天气怎么样？' 的响应截图" />

## 技术细节

### 应用程序与命令行接口

iMCP 是一个 macOS 应用程序，其中包含一个命令行可执行文件 `imcp-server`。
* [iMCP.app](https://github.com/loopwork-ai/imcp/tree/HEAD/App) 提供了配置服务的界面，并且最重要的是，
  它提供了一种与 macOS 系统权限交互的方式，
  以便它可以访问联系人、日历和其他信息。
* [imcp-server](https://github.com/loopwork-ai/imcp/tree/HEAD/CLI) 提供了一个 MCP 服务器，该服务器
  使用标准输入/输出进行通信
  ([stdio 传输][mcp-transports])。

应用程序和命令行接口通过 Bonjour 在本地网络上相互通信，
用于自动发现。两者都广播类型为 "_mcp._tcp" 和域为 "local" 的服务。
来自 MCP 客户端的请求由命令行接口从 `stdin` 读取并转发给应用程序；
应用程序的响应由命令行接口接收并通过 `stdout` 写出。
有关实现细节，请参见 [`StdioProxy`](https://github.com/loopwork-ai/iMCP/blob/8cf9d250286288b06bf5d3dda78f5905ad0d7729/CLI/main.swift#L47)。

对于这个项目，我们创建了 [mcp-swift-sdk](https://github.com/loopwork-ai/mcp-swift-sdk)：
这是一个用于 Model Context Protocol 服务器和客户端的 Swift SDK。
应用程序使用这个包来处理来自 MCP 客户端的代理请求。

### iMessage 数据库访问

Apple 不提供公开 API 来访问您的消息。然而，macOS 上的 Messages 应用将数据存储在位于
`~/Library/Messages/chat.db` 的 SQLite 数据库中。

iMCP 运行在 [App Sandbox](https://developer.apple.com/documentation/security/app-sandbox) 中，
这限制了其对用户数据和系统资源的访问。
当您启用 Messages 服务时，系统会提示您通过标准文件选择器打开 `chat.db` 文件。
这样做之后，macOS 会将该文件添加到应用程序的沙盒中。
[`NSOpenPanel`](https://developer.apple.com/documentation/appkit/nsopenpanel) 就是这样神奇地工作的。

但是，打开 iMessage 数据库只是完成了一半的工作。
在过去几年里，
Apple 已经不再以纯文本形式存储消息，
而是转向专有的 `typedstream` 格式。

为此项目，我们创建了 [Madrid](https://github.com/loopwork-ai/Madrid)：
这是一个用于读取您的 iMessage 数据库的 Swift 包。
它包括一个解码 Apple `typedstream` 格式的 Swift 实现，
该实现改编自 Christopher Sardegna 的 [imessage-exporter](https://github.com/ReagentX/imessage-exporter) 项目
及其关于反向工程 `typedstream` 的[博客文章](https://chrissardegna.com/blog/reverse-engineering-apples-typedstream-format/)。

### JSON-LD for Tool Results

iMCP 提供的工具返回的结果是 [JSON-LD](https://json-ld.org) 文档。例如，`fetchContacts` 工具使用了 [Contacts 框架](https://developer.apple.com/documentation/contacts)，该框架用 [`CNContact`](https://developer.apple.com/documentation/contacts/cncontact) 类型表示人和组织。以下是这种类型的对象如何被编码为 JSON-LD 的示例：

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Loopwork Limited",
  "url": "https://loop.work"
}
```

[Schema.org](https://schema.org) 为人们、邮政地址、事件以及其他我们想要表示的对象提供了标准词汇表。而 JSON-LD 是一种方便的编码格式，适用于人类、人工智能以及传统软件。

对于此项目，我们创建了 [Ontology](https://github.com/loopwork-ai/Ontology)：一个用于处理结构化数据的 Swift 包。它包括来自 Apple 框架（如 iMCP 工具返回的）类型的便捷初始化器。

## 致谢

- [Justin Spahr-Summers](https://jspahrsummers.com/) ([@jspahrsummers](https://github.com/jspahrsummers))、David Soria Parra ([@dsp-ant](https://github.com/dsp-ant)) 和 Ashwin Bhat ([@ashwin-ant](https://github.com/ashwin-ant)) 对 MCP 的贡献。
- [Christopher Sardegna](https://chrissardegna.com) ([@ReagentX](https://github.com/ReagentX)) 反向工程了 Messages 应用程序使用的 `typedstream` 格式。

## 许可证

本项目采用 Apache License, Version 2.0 授权。

## 法律声明

iMessage® 是苹果公司注册的商标。  
本项目与苹果公司无关，未得到其认可或赞助。

**官方网站：** [https://github.com/loopwork-ai/imcp](https://github.com/loopwork-ai/imcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`productivity`, `data`
- 标签：`calendar management`, `location services`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`{paste iMCP server command}`
- 参数：无

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/loopwork-ai-imcp.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
