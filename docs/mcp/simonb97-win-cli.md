---
title: "Windows命令行MCP服务器"
description: "一种模型上下文协议（MCP）服务器，提供对Windows系统的安全命令行访问，允许像Claude Desktop这样的MCP客户端在PowerShell、CMD和Git Bash shell中安全地执行命令，并带有可配置的安全控制。"
---

# Windows命令行MCP服务器

一种模型上下文协议（MCP）服务器，提供对Windows系统的安全命令行访问，允许像Claude Desktop这样的MCP客户端在PowerShell、CMD和Git Bash shell中安全地执行命令，并带有可配置的安全控制。

# Windows CLI MCP 服务器
[![NPM 下载量](/mcp-assets/105e24710c8fb4bfe089a461707ec204.svg)](https://www.npmjs.com/package/@simonb97/server-win-cli)
[![NPM 版本](/mcp-assets/3dda89a8f1f4e0585d74025330935cb8.svg)](https://www.npmjs.com/package/@simonb97/server-win-cli?activeTab=versions)
[Smithery](https://smithery.ai/server/@simonb97/server-win-cli)

用于在 Windows 系统上进行安全命令行交互的 [MCP 服务器](https://modelcontextprotocol.io/introduction)，它允许受控访问 PowerShell、CMD、Git Bash 命令行以及通过 SSH 访问远程系统。它使 MCP 客户端（如 [Claude Desktop](https://claude.ai/download)）能够对您的系统执行操作，类似于 [Open Interpreter](https://github.com/OpenInterpreter/open-interpreter)。

>[!IMPORTANT]
> 该 MCP 服务器提供了直接访问您系统的命令行接口和通过 SSH 访问远程系统的权限。启用后，它将授予访问您的文件、环境变量、命令执行能力和远程服务器管理的权限。
>
> - 审查并限制允许的路径和 SSH 连接
> - 启用目录限制
> - 配置命令阻止
> - 考虑安全性影响
>
> 有关更多详细信息，请参阅 [配置](#configuration)。

- [功能](#features)
- [与 Claude Desktop 的使用](#usage-with-claude-desktop)
- [配置](#configuration)
  - [配置位置](#configuration-locations)
  - [默认配置](#default-configuration)
  - [配置设置](#configuration-settings)
    - [安全设置](#security-settings)
    - [Shell 配置](#shell-configuration)
    - [SSH 配置](#ssh-configuration)
- [API](#api)
  - [工具](#tools)
  - [资源](#resources)
- [安全注意事项](#security-considerations)
- [许可证](#license)

## 功能

- **多 Shell 支持**：在 PowerShell、命令提示符 (CMD) 和 Git Bash 中执行命令
- **SSH 支持**：通过 SSH 在远程系统上执行命令
- **资源暴露**：将 SSH 连接、当前目录和配置作为 MCP 资源查看
- **安全控制**：
  - 命令和 SSH 命令阻止（完整路径、大小写变化）
  - 工作目录验证
  - 最大命令长度限制
  - 命令日志记录和历史跟踪
  - 智能参数验证
- **可配置性**：
  - 自定义安全规则
  - 特定于 Shell 的设置
  - SSH 连接配置文件
  - 路径限制
  - 阻止命令列表

有关服务器向 MCP 客户端提供的工具和资源的更多详细信息，请参阅 [API](#api) 部分。

**注意**：服务器仅允许在已配置的目录内、使用允许的命令以及在已配置的 SSH 连接上执行操作。

## 与 Claude Desktop 的使用

将以下内容添加到您的 `claude_desktop_config.json` 文件中：

```json
{
  "mcpServers": {
    "windows-cli": {
      "command": "npx",
      "args": ["-y", "@simonb97/server-win-cli"]
    }
  }
}
```

如果要使用特定配置文件，请添加 `--config` 标志：

```json
{
  "mcpServers": {
    "windows-cli": {
      "command": "npx",
      "args": [
        "-y",
        "@simonb97/server-win-cli",
        "--config",
        "path/to/your/config.json"
      ]
    }
  }
}
```

配置完成后，您可以：
- 使用可用工具直接执行命令
- 在“资源”部分查看已配置的 SSH 连接和服务器配置
- 通过提供的工具管理 SSH 连接

## 配置

服务器使用 JSON 配置文件来自定义其行为。您可以为安全控制、shell 配置和 SSH 连接指定设置。

1. 要创建默认配置文件，可以：

**a)** 将 `config.json.example` 复制为 `config.json`，或者

**b)** 运行：

```bash
npx @simonb97/server-win-cli --init-config ./config.json
```

2. 然后按照 [Usage with Claude Desktop](#usage-with-claude-desktop) 部分的描述设置 `--config` 标志以指向您的配置文件。

### 配置位置

服务器按以下顺序查找配置：

1. 由 `--config` 标志指定的路径
2. 当前目录下的 ./config.json
3. 用户主目录下的 ~/.win-cli-mcp/config.json

如果未找到配置文件，服务器将使用默认（受限）配置：

### 默认配置

**注意**：默认配置旨在具有限制性和安全性。有关每个设置的更多详细信息，请参阅 [Configuration Settings](#configuration-settings) 部分。

```json
{
  "security": {
    "maxCommandLength": 2000,
    "blockedCommands": [
      "rm",
      "del",
      "rmdir",
      "format",
      "shutdown",
      "restart",
      "reg",
      "regedit",
      "net",
      "netsh",
      "takeown",
      "icacls"
    ],
    "blockedArguments": [
      "--exec",
      "-e",
      "/c",
      "-enc",
      "-encodedcommand",
      "-command",
      "--interactive",
      "-i",
      "--login",
      "--system"
    ],
    "allowedPaths": ["User's home directory", "Current working directory"],
    "restrictWorkingDirectory": true,
    "logCommands": true,
    "maxHistorySize": 1000,
    "commandTimeout": 30,
    "enableInjectionProtection": true
  },
  "shells": {
    "powershell": {
      "enabled": true,
      "command": "powershell.exe",
      "args": ["-NoProfile", "-NonInteractive", "-Command"],
      "blockedOperators": ["&", "|", ";", "`"]
    },
    "cmd": {
      "enabled": true,
      "command": "cmd.exe",
      "args": ["/c"],
      "blockedOperators": ["&", "|", ";", "`"]
    },
    "gitbash": {
      "enabled": true,
      "command": "C:\\Program Files\\Git\\bin\\bash.exe",
      "args": ["-c"],
      "blockedOperators": ["&", "|", ";", "`"]
    }
  },
  "ssh": {
    "enabled": false,
    "defaultTimeout": 30,
    "maxConcurrentSessions": 5,
    "keepaliveInterval": 10000,
    "keepaliveCountMax": 3,
    "readyTimeout": 20000,
    "connections": {}
  }
}
```

### 配置设置

配置文件分为三个主要部分：`security`、`shells` 和 `ssh`。

#### 安全设置

```json
{
  "security": {
    // Maximum allowed length for any command
    "maxCommandLength": 1000,

    // Commands to block - blocks both direct use and full paths
    // Example: "rm" blocks both "rm" and "C:\\Windows\\System32\\rm.exe"
    // Case-insensitive: "del" blocks "DEL.EXE", "del.cmd", etc.
    "blockedCommands": [
      "rm", // Delete files
      "del", // Delete files
      "rmdir", // Delete directories
      "format", // Format disks
      "shutdown", // Shutdown system
      "restart", // Restart system
      "reg", // Registry editor
      "regedit", // Registry editor
      "net", // Network commands
      "netsh", // Network commands
      "takeown", // Take ownership of files
      "icacls" // Change file permissions
    ],

    // Arguments that will be blocked when used with any command
    // Note: Checks each argument independently - "cd warm_dir" won't be blocked just because "rm" is in blockedCommands
    "blockedArguments": [
      "--exec", // Execution flags
      "-e", // Short execution flags
      "/c", // Command execution in some shells
      "-enc", // PowerShell encoded commands
      "-encodedcommand", // PowerShell encoded commands
      "-command", // Direct PowerShell command execution
      "--interactive", // Interactive mode which might bypass restrictions
      "-i", // Short form of interactive
      "--login", // Login shells might have different permissions
      "--system" // System level operations
    ],

    // List of directories where commands can be executed
    "allowedPaths": ["C:\\Users\\YourUsername", "C:\\Projects"],

    // If true, commands can only run in allowedPaths
    "restrictWorkingDirectory": true,

    // If true, saves command history
    "logCommands": true,

    // Maximum number of commands to keep in history
    "maxHistorySize": 1000,

    // Timeout for command execution in seconds (default: 30)
    "commandTimeout": 30,

    // Enable or disable protection against command injection (covers ;, &, |, \`)
    "enableInjectionProtection": true
  }
}
```

#### Shell 配置

```json
{
  "shells": {
    "powershell": {
      // Enable/disable this shell
      "enabled": true,
      // Path to shell executable
      "command": "powershell.exe",
      // Default arguments for the shell
      "args": ["-NoProfile", "-NonInteractive", "-Command"],
      // Optional: Specify which command operators to block
      "blockedOperators": ["&", "|", ";", "`"]  // Block all command chaining
    },
    "cmd": {
      "enabled": true,
      "command": "cmd.exe",
      "args": ["/c"],
      "blockedOperators": ["&", "|", ";", "`"]  // Block all command chaining
    },
    "gitbash": {
      "enabled": true,
      "command": "C:\\Program Files\\Git\\bin\\bash.exe",
      "args": ["-c"],
      "blockedOperators": ["&", "|", ";", "`"]  // Block all command chaining
    }
  }
}
```

#### SSH 配置

```json
{
  "ssh": {
    // Enable/disable SSH functionality
    "enabled": false,

    // Default timeout for SSH commands in seconds
    "defaultTimeout": 30,

    // Maximum number of concurrent SSH sessions
    "maxConcurrentSessions": 5,

    // Interval for sending keepalive packets (in milliseconds)
    "keepaliveInterval": 10000,

    // Maximum number of failed keepalive attempts before disconnecting
    "keepaliveCountMax": 3,

    // Timeout for establishing SSH connections (in milliseconds)
    "readyTimeout": 20000,

    // SSH connection profiles
    "connections": {
      // NOTE: these examples are not set in the default config!
      // Example: Local Raspberry Pi
      "raspberry-pi": {
        "host": "raspberrypi.local", // Hostname or IP address
        "port": 22, // SSH port
        "username": "pi", // SSH username
        "password": "raspberry", // Password authentication (if not using key)
        "keepaliveInterval": 10000, // Override global keepaliveInterval
        "keepaliveCountMax": 3, // Override global keepaliveCountMax
        "readyTimeout": 20000 // Override global readyTimeout
      },
      // Example: Remote server with key authentication
      "dev-server": {
        "host": "dev.example.com",
        "port": 22,
        "username": "admin",
        "privateKeyPath": "C:\\Users\\YourUsername\\.ssh\\id_rsa", // Path to private key
        "keepaliveInterval": 10000,
        "keepaliveCountMax": 3,
        "readyTimeout": 20000
      }
    }
  }
}
```

## API

### 工具

- **execute_command**

  - 在指定的 shell 中执行命令
  - 输入：
    - `shell` (字符串)：要使用的 shell ("powershell", "cmd" 或 "gitbash")
    - `command` (字符串)：要执行的命令
    - `workingDir` (可选字符串)：工作目录
  - 返回命令输出文本，如果执行失败则返回错误消息

- **get_command_history**

  - 获取已执行命令的历史记录
  - 输入：`limit` (可选数字)
  - 返回带时间戳的命令历史记录及其输出

- **ssh_execute**

  - 通过 SSH 在远程系统上执行命令
  - 输入：
    - `connectionId` (字符串)：要使用的 SSH 连接的 ID
    - `command` (字符串)：要执行的命令
  - 返回命令输出文本，如果执行失败则返回错误消息

- **ssh_disconnect**
  - 断开与 SSH 服务器的连接
  - 输入：
    - `connectionId` (字符串)：要断开的 SSH 连接的 ID
  - 返回确认消息

- **create_ssh_connection**
  - 创建一个新的 SSH 连接
  - 输入：
    - `connectionId` (字符串)：新 SSH 连接的 ID
    - `connectionConfig` (对象)：连接配置详情，包括主机、端口、用户名以及密码或私钥路径
  - 返回确认消息

- **read_ssh_connections**
  - 读取所有配置的 SSH 连接
  - 返回配置中的所有 SSH 连接列表

- **update_ssh_connection**
  - 更新现有的 SSH 连接
  - 输入：
    - `connectionId` (字符串)：要更新的 SSH 连接的 ID
    - `connectionConfig` (对象)：新的连接配置详情
  - 返回确认消息

- **delete_ssh_connection**
  - 删除一个 SSH 连接
  - 输入：
    - `connectionId` (字符串)：要删除的 SSH 连接的 ID
  - 返回确认消息

- **get_current_directory**
  - 获取服务器的当前工作目录
  - 返回当前工作目录路径

### 资源

- **SSH 连接**
  - URI 格式：`ssh://{connectionId}`
  - 包含连接详情，敏感信息被屏蔽
  - 每个配置的 SSH 连接都有一个资源
  - 示例：`ssh://raspberry-pi` 显示 "raspberry-pi" 连接的配置

- **SSH 配置**
  - URI: `ssh://config`
  - 包含总体 SSH 配置和所有连接（密码被屏蔽）
  - 显示设置如 defaultTimeout, maxConcurrentSessions 和连接列表

- **当前目录**
  - URI: `cli://currentdir`
  - 包含 CLI 服务器的当前工作目录
  - 显示默认执行命令的路径

- **CLI 配置**
  - URI: `cli://config`
  - 包含 CLI 服务器配置（不包括敏感数据）
  - 显示安全设置、shell 配置和 SSH 设置

## 安全考虑

### 内置安全特性（始终激活）

以下安全特性被硬编码到服务器中，无法禁用：

- **不区分大小写的命令拦截**：所有命令拦截都是不区分大小写的（例如，如果"del"在blockedCommands中，则"DEL.EXE", "del.cmd"等都会被拦截）
- **智能路径解析**：服务器解析完整的命令路径以防止绕过尝试（如果"rm"被拦截，则会拦截"C:\\Windows\\System32\\rm.exe"）
- **命令解析智能**：避免误报（例如，不会因为"rm"在blockedCommands中就拦截"warm_dir"）
- **输入验证**：所有用户输入在执行前都会进行验证
- **Shell 进程管理**：进程在执行完毕或超时后会被正确终止
- **敏感数据掩码**：密码在资源中自动被掩码处理（替换为********）

### 可配置的安全特性（默认激活）

这些安全特性可以通过config.json文件进行配置：

- **命令拦截**：在`blockedCommands`数组中指定的命令将被拦截（默认包括像rm, del, format这样的危险命令）
- **参数拦截**：在`blockedArguments`数组中指定的参数将被拦截（默认包括潜在危险的标志）
- **命令注入保护**：防止命令链（通过设置`enableInjectionProtection: true`默认启用）
- **工作目录限制**：限制命令执行到指定目录（通过设置`restrictWorkingDirectory: true`默认启用）
- **命令长度限制**：限制最大命令长度（默认：2000个字符）
- **命令超时**：终止运行时间过长的命令（默认：30秒）
- **命令日志记录**：记录命令历史（通过设置`logCommands: true`默认启用）

### 重要安全警告

以下不是功能特性，但是一些需要注意的重要安全考虑事项：

- **环境访问**：命令可能有权访问环境变量，其中可能包含敏感信息
- **文件系统访问**：命令可以在允许的路径内读写文件——请仔细配置`allowedPaths`以防止访问敏感数据

## 许可证

本项目根据MIT许可证发布 - 详情请参阅[LICENSE](https://github.com/SimonB97/win-cli-mcp-server/blob/HEAD/LICENSE)文件。

**官方网站：** [https://github.com/SimonB97/win-cli-mcp-server](https://github.com/SimonB97/win-cli-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`files`
- 标签：`os automation`, `file systems`, `developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @simonb97/server-win-cli`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/simonb97-win-cli.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
