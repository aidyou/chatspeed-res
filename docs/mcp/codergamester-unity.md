---
title: "Unity编辑器助手"
description: "Unity Editor的Model Context Protocol实现，允许AI助手通过执行菜单项、选择对象、管理包、运行测试和访问资源的工具与Unity项目进行交互。"
---

# Unity编辑器助手

Unity Editor的Model Context Protocol实现，允许AI助手通过执行菜单项、选择对象、管理包、运行测试和访问资源的工具与Unity项目进行交互。

# MCP Unity 编辑器 (游戏引擎)

[![](/mcp-assets/d4184d72d7bf151a0d8778c272bd9a4f.svg 'MCP 启用')](https://modelcontextprotocol.io/introduction)
[![](/mcp-assets/9b700283d756a88564d8b5b453be0905.svg 'Unity')](https://unity.com/releases/editor/archive)
[![](/mcp-assets/148c8c2430c0ccd90f9e06f3c3ea5e04.svg 'Node.js')](https://nodejs.org/en/download/)

[Smithery](https://smithery.ai/server/@CoderGamester/mcp-unity)
[![](/mcp-assets/4d6facd625d9b6e2a16ce8e07e00105a.svg '星星')](https://github.com/CoderGamester/mcp-unity/stargazers)
[![](/mcp-assets/001aa60de15e858c5fc854b03602f104.svg '分支')](https://github.com/CoderGamester/mcp-unity/network/members)
[![](/mcp-assets/8f9cfbb56c5a2696e6809907d3b704ae.svg '最近提交')](https://github.com/CoderGamester/mcp-unity/commits/main)
[![](/mcp-assets/3936e2c22a65da85cb0bf816374d21f8.svg 'MIT 许可证')](https://opensource.org/licenses/MIT)

  

```
                              ,/(/.   *(/,                                  
                          */(((((/.   *((((((*.                             
                     .*((((((((((/.   *((((((((((/.                         
                 ./((((((((((((((/    *((((((((((((((/,                     
             ,/(((((((((((((/*.           */(((((((((((((/*.                
            ,%%#((/((((((*                    ,/(((((/(#&@@(                
            ,%%##%%##((((((/*.             ,/((((/(#&@@@@@@(                
            ,%%######%%##((/(((/*.    .*/(((//(%@@@@@@@@@@@(                
            ,%%####%#(%%#%%##((/((((((((//#&@@@@@@&@@@@@@@@(                
            ,%%####%(    /#%#%%%##(//(#@@@@@@@%,   #@@@@@@@(                
            ,%%####%(        *#%###%@@@@@@(        #@@@@@@@(                
            ,%%####%(           #%#%@@@@,          #@@@@@@@(                
            ,%%##%%%(           #%#%@@@@,          #@@@@@@@(                
            ,%%%#*              #%#%@@@@,             *%@@@(                
            .,      ,/##*.      #%#%@@@@,     ./&@#*      *`                
                ,/#%#####%%#/,  #%#%@@@@, ,/&@@@@@@@@@&\.                    
                 `*#########%%%%###%@@@@@@@@@@@@@@@@@@&*´                   
                    `*%%###########%@@@@@@@@@@@@@@&*´                        
                        `*%%%######%@@@@@@@@@@&*´                            
                            `*#%%##%@@@@@&*´                                 
                               `*%#%@&*´                                     
                                                       
     ███╗   ███╗ ██████╗██████╗         ██╗   ██╗███╗   ██╗██╗████████╗██╗   ██╗
     ████╗ ████║██╔════╝██╔══██╗        ██║   ██║████╗  ██║██║╚══██╔══╝╚██╗ ██╔╝
     ██╔████╔██║██║     ██████╔╝        ██║   ██║██╔██╗ ██║██║   ██║    ╚████╔╝ 
     ██║╚██╔╝██║██║     ██╔═══╝         ██║   ██║██║╚██╗██║██║   ██║     ╚██╔╝  
     ██║ ╚═╝ ██║╚██████╗██║             ╚██████╔╝██║ ╚████║██║   ██║      ██║   
     ╚═╝     ╚═╝ ╚═════╝╚═╝              ╚═════╝ ╚═╝  ╚═══╝╚═╝   ╚═╝      ╚═╝   
```

MCP Unity 是针对 Unity 编辑器的 Model Context Protocol 的实现，允许 AI 助手与您的 Unity 项目进行交互。这个包提供了一个桥梁，连接 Unity 和实现了 MCP 协议的 Node.js 服务器，使像 Claude、Windsurf 和 Cursor 这样的 AI 代理能够在 Unity 编辑器中执行操作。

## 功能
此 MCP 当前提供了以下 
工具
：

- 
**execute_menu_item**
: 执行 Unity 菜单项（带有 MenuItem 属性标记的功能）
- 
**select_gameobject**
: 通过路径或实例 ID 在 Unity 层次结构中选择游戏对象
- 
**update_component**
: 更新 GameObject 上的组件字段，如果 GameObject 不包含该组件，则将其添加到 GameObject
- 
**add_package**
: 在 Unity 包管理器中安装新包
- 
**run_tests**
: 使用 Unity 测试运行器运行测试
- 
**notify_message**
: 在 Unity 编辑器中显示消息

此 MCP 当前提供了以下 
资源
：

- 
**get_menu_items**
: 检索 Unity 编辑器中所有可用菜单项的列表，以辅助 
**execute_menu_item**
 工具
- 
**get_hierarchy**
: 检索 Unity 层次结构中的所有游戏对象的列表
- 
**get_gameobject**
: 通过实例 ID 检索特定 GameObject 的详细信息，包括所有 GameObject 组件及其序列化属性和字段
- 
**get_console_logs**
: 检索 Unity 控制台中的所有日志列表
- 
**get_packages**
: 从 Unity 包管理器检索已安装和可用包的信息
- 
**get_assets**
: 从 Unity 资源数据库检索资源信息
- 
**get_tests**
: 从 Unity 测试运行器检索测试信息

## 需求

- Unity 2022.3 或更高版本 - 用于[安装服务器](#install-server)
- Node.js 18 或更高版本 - 用于[启动服务器](#start-server)
- npm 9 或更高版本 - 用于[调试服务器](#debug-server)

## 

安装

安装此 MCP Unity 服务器是一个多步骤的过程：

### 步骤 1: 通过 Unity 包管理器安装 Unity MCP 服务器包
1. 打开 Unity 包管理器（Window > Package Manager）
2. 点击左上角的 "+" 按钮
3. 选择 "Add package from git URL..."
4. 输入：`https://github.com/CoderGamester/mcp-unity.git`
5. 点击 "Add"

### 步骤 2: 安装 Node.js 
> 要运行 MCP Unity 服务器，你需要在计算机上安装 Node.js 18 或更高版本：

Windows

1. 访问 [Node.js 下载页面](https://nodejs.org/en/download/)
2. 下载 LTS 版本的 Windows 安装程序 (.msi)（推荐）
3. 运行安装程序并按照安装向导进行操作
4. 通过打开 PowerShell 并运行以下命令来验证安装：
```bash
   node --version
```

macOS

1. 访问 [Node.js 下载页面](https://nodejs.org/en/download/)
2. 下载 LTS 版本的 macOS 安装程序 (.pkg)（推荐）
3. 运行安装程序并按照安装向导进行操作
4. 或者，如果你已安装 Homebrew，可以运行：
```bash
   brew install node@18
```
5. 通过打开终端并运行以下命令来验证安装：
```bash
   node --version
```

### 步骤 3: 配置 AI LLM 客户端

选项 1: 使用 Unity 编辑器配置

1. 打开 Unity 编辑器
2. 导航到 Tools > MCP Unity > Server Window
3. 如下图所示，点击你的 AI LLM 客户端的 "Configure" 按钮

4. 使用弹出窗口确认配置安装

选项 2: 通过 Smithery 配置

要通过 [Smithery](https://smithery.ai/server/@CoderGamester/mcp-unity) 安装 MCP Unity，请使用以下命令：

```
Currently not available
```

选项 3: 手动配置

打开你的 AI 客户端的 MCP 配置文件（例如 Claude Desktop 中的 claude_desktop_config.json），并复制以下文本：

> 将 `ABSOLUTE/PATH/TO` 替换为你的 MCP Unity 安装的绝对路径，或者直接从 Unity 编辑器中的 MCP 服务器窗口复制文本（Tools > MCP Unity > Server Window）。

```json
{
   "mcpServers": {
   "mcp-unity": {
      "command": "node",
      "args": [
         "ABSOLUTE/PATH/TO/mcp-unity/Server/build/index.js"
      ],
      "env": {
         "UNITY_PORT": "8090"
      }
   }
   }
}
```

## 

启动 Unity 编辑器 MCP 服务器
1. 打开 Unity 编辑器
2. 导航到 Tools > MCP Unity > Server Window
3. 点击 "Start Server" 以启动 WebSocket 服务器
4. 打开 Claude Desktop 或您的 AI 编码 IDE（例如 Cursor IDE, Windsurf IDE 等）并开始执行 Unity 工具
   

> 当 AI 客户端连接到 WebSocket 服务器时，它将自动显示在窗口的绿色框中

## 可选：设置 WebSocket 端口
默认情况下，WebSocket 服务器运行在 8090 端口。您可以通过以下两种方式更改此端口：

选项 1：使用 Unity 编辑器

1. 打开 Unity 编辑器
2. 导航到 Tools > MCP Unity > Server Window
3. 将 "WebSocket Port" 值更改为所需的端口号
4. Unity 将设置系统环境变量 UNITY_PORT 为新的端口号
5. 重启 Node.js 服务器
6. 再次点击 "Start Server" 以重新连接 Unity 编辑器 WebSocket 到 Node.js MCP 服务器

选项 2：使用终端

1. 在终端中设置 UNITY_PORT 环境变量
   - PowerShell
```powershell
   $env:UNITY_PORT = "8090"
```
   - 命令提示符/终端
```cmd
   set UNITY_PORT=8090
```
2. 重启 Node.js 服务器
3. 再次点击 "Start Server" 以重新连接 Unity 编辑器 WebSocket 到 Node.js MCP 服务器

## 

调试服务器

构建 Node.js 服务器

MCP Unity 服务器是使用 Node.js 构建的。需要将 TypeScript 代码编译成 JavaScript 并放置在 `build` 目录中。
要构建服务器，请打开一个终端并执行以下步骤：

1. 导航到 Server 目录：
```bash
   cd ABSOLUTE/PATH/TO/mcp-unity/Server
```

2. 安装依赖项：
```bash
   npm install
```

3. 构建服务器：
```bash
   npm run build
```

4. 运行服务器：
```bash
   node build/index.js
```

   

使用 MCP Inspector 调试

使用 [@modelcontextprotocol/inspector](https://github.com/modelcontextprotocol/inspector) 调试服务器：
   - PowerShell
```powershell
   $env:UNITY_PORT=8090; npx @modelcontextprotocol/inspector node Server/build/index.js
```
   - 命令提示符/终端
```cmd
   set UNITY_PORT=8090 && npx @modelcontextprotocol/inspector node Server/build/index.js
```

在关闭终端或使用 [MCP Inspector](https://github.com/modelcontextprotocol/inspector) 调试之前，请勿忘记使用 `Ctrl + C` 关闭服务器。

启用控制台日志

1. 在您的终端或 log.txt 文件中启用日志记录：
   - PowerShell
```powershell
   $env:LOGGING = "true"
   $env:LOGGING_FILE = "true"
```
   - 命令提示符/终端
```cmd
   set LOGGING=true
   set LOGGING_FILE=true
```

## 故障排除

连接问题

- 确保 WebSocket 服务器正在运行（检查 Unity 中的 Server Window）
- 检查是否有防火墙限制阻止了连接
- 确保端口号正确（默认是 8080）
- 在 Unity 编辑器的 MCP Server 窗口中更改端口号。（工具 > MCP Unity > 服务器窗口）

服务器无法启动

- 检查 Unity 控制台中的错误信息
- 确保 Node.js 已正确安装并且可以在您的 PATH 中访问
- 验证服务器目录中是否已安装所有依赖项

菜单项无法执行

- 确保菜单项路径正确（区分大小写）
- 检查菜单项是否需要确认
- 验证菜单项在当前上下文中是否可用

## 支持与反馈

如果您有任何问题或需要支持，请在此仓库中打开一个[问题](https://github.com/CoderGamester/mcp-unity/issues)。

您也可以通过以下方式联系我们：
- [![](/mcp-assets/b6f093496278e747d7449e7eb9b6142c.svg 'LinkedIn')](https://www.linkedin.com/in/miguel-tomas/)
- Discord: gamester7178

## 贡献

欢迎贡献！请随时提交 Pull Request 或打开一个 Issue 提出您的请求。

**提交您的更改**时，请遵循 [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) 格式。

## 许可证

此项目遵循 [MIT 许可证](https://github.com/codergamester/mcp-unity/blob/HEAD/LICENSE.md)

**官方网站：** [https://github.com/codergamester/mcp-unity](https://github.com/codergamester/mcp-unity)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `virtualization`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`ABSOLUTE/PATH/TO/mcp-unity/Server/build/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/codergamester-unity.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
