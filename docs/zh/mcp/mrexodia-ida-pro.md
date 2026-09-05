---
title: "IDA自动化反编译工具"
description: "用于自动化逆向工程的IDA Pro MCP服务器。"
---

# IDA自动化反编译工具

用于自动化逆向工程的IDA Pro MCP服务器。

# IDA Pro MCP

简单的 [MCP 服务器](https://modelcontextprotocol.io/introduction)，允许在 IDA Pro 中进行振动逆向工程。

[https://github.com/user-attachments/assets/6ebeaa92-a9db-43fa-b756-eececce2aca0](https://github.com/user-attachments/assets/6ebeaa92-a9db-43fa-b756-eececce2aca0)

视频中使用的二进制文件和提示可以在 [mcp-reversing-dataset](https://github.com/mrexodia/mcp-reversing-dataset) 仓库中找到。

可用功能：

- `check_connection`: 检查 IDA 插件是否正在运行。
- `get_metadata()`: 获取当前 IDB 的元数据。
- `get_function_by_name(name)`: 根据名称获取函数。
- `get_function_by_address(address)`: 根据地址获取函数。
- `get_current_address()`: 获取用户当前选择的地址。
- `get_current_function()`: 获取用户当前选择的函数。
- `convert_number(text, size)`: 将数字（十进制、十六进制）转换为不同的表示形式。
- `list_functions(offset, count)`: 列出数据库中的所有函数（分页）。
- `list_strings(offset, count)`: 列出数据库中的所有字符串（分页）。
- `search_strings(pattern, offset, count)`: 搜索包含给定模式的字符串（不区分大小写）。
- `decompile_function(address)`: 反编译指定地址的函数。
- `disassemble_function(start_address)`: 获取函数的汇编代码（地址：指令；注释）。
- `get_xrefs_to(address)`: 获取指向给定地址的所有交叉引用。
- `get_entry_points()`: 获取数据库中的所有入口点。
- `set_comment(address, comment)`: 为函数反汇编和伪代码中的给定地址设置注释。
- `rename_local_variable(function_address, old_name, new_name)`: 重命名函数中的局部变量。
- `rename_global_variable(old_name, new_name)`: 重命名全局变量。
- `set_global_variable_type(variable_name, new_type)`: 设置全局变量的类型。
- `rename_function(function_address, new_name)`: 重命名函数。
- `set_function_prototype(function_address, prototype)`: 设置函数的原型。
- `declare_c_type(c_declaration)`: 从 C 声明创建或更新本地类型。
- `set_local_variable_type(function_address, variable_name, new_type)`: 设置局部变量的类型。

## 先决条件

- [Python](https://www.python.org/downloads/) (**3.11 或更高版本**)
  - 使用 `idapyswitch` 切换到最新版本的 Python
- [IDA Pro](https://hex-rays.com/ida-pro) (8.3 或更高版本，推荐 9.0)
- 支持的 MCP 客户端（选择一个你喜欢的）
  - [Cline](https://cline.bot)
  - [Roo Code](https://marketplace.visualstudio.com/items?itemName=RooVeterinaryInc.roo-cline)
  - [Claude](https://claude.ai/download)

## 安装

安装（或升级）IDA Pro MCP 包：

```sh
pip install --upgrade git+https://github.com/mrexodia/ida-pro-mcp
```

配置 MCP 服务器并安装 IDA 插件：

```
ida-pro-mcp --install
```

**重要**：确保完全重启 IDA/Visual Studio Code/Claude 以使安装生效。Claude 在后台运行，你需要从托盘图标中退出它。

[https://github.com/user-attachments/assets/65ed3373-a187-4dd5-a807-425dca1d8ee9](https://github.com/user-attachments/assets/65ed3373-a187-4dd5-a807-425dca1d8ee9)

## 提示工程

大型语言模型（LLMs）容易产生幻觉，因此在提示时需要具体明确。对于逆向工程中的整数和字节之间的转换尤其存在问题。以下是一个最小示例提示，如果您使用不同的提示获得了良好的结果，请随时开始讨论或提出问题：

> 您的任务是在IDA Pro中分析一个crackme程序。您可以使用MCP工具来获取信息。通常请使用以下策略：
> - 检查反编译并根据您的发现添加注释
> - 将变量重命名为更有意义的名称
> - 如果必要，更改变量和参数类型（特别是指针和数组类型）
> - 更改函数名称以使其更具描述性
> - 如果需要更多细节，请反汇编该函数并根据您的发现添加注释
> - **切勿自行转换数字进制**。如果需要，请使用`convert_number` MCP工具！
> - 不要尝试暴力破解，仅从反汇编和简单的Python脚本中推导出解决方案
> - 最后创建一个`report.md`文件，记录您的发现和采取的步骤
> - 当您找到解决方案时，向用户请求反馈，并提供您找到的密码

这个提示只是第一次实验，请分享如果您找到了改进输出的方法！

## 提高LLM准确性的技巧

大型语言模型（LLMs）是强大的工具，但它们有时会难以处理复杂的数学计算或表现出“幻觉”（即编造事实）。确保告诉LLM使用`convert_number` MCP工具，对于某些操作，您可能还需要[math-mcp](https://github.com/EthanHenrickson/math-mcp)。

另外需要注意的是，LLMs在处理混淆代码时表现不佳。在尝试使用LLM解决问题之前，请先查看二进制文件，并花些时间（自动地）移除以下内容：

- 字符串加密
- 导入哈希
- 控制流扁平化
- 代码加密
- 反反编译技巧

您还应该使用Lumina或FLIRT等工具尝试解析所有开源库代码和C++ STL，这将进一步提高准确性。

## 手动安装

_注意_：本部分针对需要详细安装说明的LLMs和高级用户。

## 手动安装MCP服务器 (Cline/Roo Code)

要自己安装MCP服务器，请按照以下步骤操作：

1. 全局安装[uv](https://github.com/astral-sh/uv)：
   - Windows: `pip install uv`
   - Linux/Mac: `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. 克隆此仓库，例如`C:\MCP\ida-pro-mcp`。
3. 转到Cline/Roo Code中的_MCP Servers_配置（参见截图）。
4. 点击_Installed_标签。
5. 点击_Configure MCP Servers_，这将打开`cline_mcp_settings.json`。
6. 添加`ida-pro-mcp`服务器：

```json
{
  "mcpServers": {
    "github.com/mrexodia/ida-pro-mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "c:\\MCP\\ida-pro-mcp",
        "run",
        "server.py",
        "--install-plugin"
      ],
      "timeout": 1800,
      "disabled": false,
      "autoApprove": [
        "check_connection",
        "get_metadata",
        "get_function_by_name",
        "get_function_by_address",
        "get_current_address",
        "get_current_function",
        "convert_number",
        "list_functions",
        "list_strings",
        "search_strings",
        "decompile_function",
        "disassemble_function",
        "get_xrefs_to",
        "get_entry_points",
        "set_comment",
        "rename_local_variable",
        "rename_global_variable",
        "set_global_variable_type",
        "rename_function",
        "set_function_prototype",
        "declare_c_type",
        "set_local_variable_type"
      ],
      "alwaysAllow": [
        "check_connection",
        "get_metadata",
        "get_function_by_name",
        "get_function_by_address",
        "get_current_address",
        "get_current_function",
        "convert_number",
        "list_functions",
        "list_strings",
        "search_strings",
        "decompile_function",
        "disassemble_function",
        "get_xrefs_to",
        "get_entry_points",
        "set_comment",
        "rename_local_variable",
        "rename_global_variable",
        "set_global_variable_type",
        "rename_function",
        "set_function_prototype",
        "declare_c_type",
        "set_local_variable_type"
      ]
    }
  }
}
```

要检查连接是否正常工作，您可以执行以下工具调用：

```

github.com/mrexodia/ida-pro-mcp
check_connection

```

## IDA插件安装

IDA Pro 插件将在 MCP 服务器启动时自动安装。如果您禁用了 `--install-plugin` 选项，请按照以下步骤操作：

1. 将 (`src/ida_pro_mcp/mcp-plugin.py`) 复制（**不要移动**）到您的插件文件夹中（在 Windows 上为 `%appdata%\Hex-Rays\IDA Pro\plugins`）。
2. 打开一个 IDB 文件并点击 `编辑 -> 插件 -> MCP` 来启动服务器。

## 与其他 MCP 服务器的比较

虽然有几个可用的 IDA Pro MCP 服务器，但我创建了自己的版本，原因如下：

1. 安装过程应完全自动化。
2. 其他插件的架构使得快速添加新功能变得困难（过多不必要的依赖项模板）。
3. 学习新技术很有趣！

如果你想查看它们，这里有一个列表（按我发现它们的顺序排列）：

- https://github.com/taida957789/ida-mcp-server-plugin (仅支持 SSE 协议，需要在 IDAPython 中安装依赖)。
- https://github.com/fdrechsler/mcp-server-idapro (使用 TypeScript 的 MCP 服务器，添加新功能需要大量模板)。
- https://github.com/MxIris-Reverse-Engineering/ida-mcp-server (自定义套接字协议，模板)。

欢迎随时提交 PR 以将你的 IDA Pro MCP 服务器添加到这里。

## 开发

添加新功能是一个非常简单且流程化的过程。你只需要在 [`mcp-plugin.py`](https://github.com/mrexodia/ida-pro-mcp/blob/164df8cf4ae251cc9cc0f464591fa6df8e0d9df4/src/ida_pro_mcp/mcp-plugin.py#L406-L419) 中添加一个新的 `@jsonrpc` 函数，你的函数就可以在 MCP 服务器中使用，无需任何额外的模板！下面是一个视频，我在不到两分钟内添加了 `get_metadata` 函数（包括测试）：

[https://github.com/user-attachments/assets/951de823-88ea-4235-adcb-9257e316ae64](https://github.com/user-attachments/assets/951de823-88ea-4235-adcb-9257e316ae64)

要测试 MCP 服务器本身：

```sh
uv run fastmcp dev server.py
```

这将在 [http://localhost:5173](http://localhost:5173) 打开一个 Web 界面，允许您与 MCP 工具进行交互以进行测试。

为了测试，我创建了一个指向 IDA 插件的符号链接，然后直接向 `http://localhost:13337/mcp` 发送 JSON-RPC 请求。在 [启用符号链接](https://learn.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development) 后，您可以运行以下命令：

```sh
uv run ida-pro-mcp --install
```

**官方网站：** [https://github.com/mrexodia/ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`--directory c:MCPida-pro-mcp run server.py --install-plugin`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/mrexodia-ida-pro.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
