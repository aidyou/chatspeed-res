---
title: "Bonsai IFC分析器"
description: "一种集成了 Claude 和 Blender 的模型上下文协议服务器，允许用户通过自然语言命令分析和交互 IFC（工业基础类）建筑模型。"
---

# Bonsai IFC分析器

一种集成了 Claude 和 Blender 的模型上下文协议服务器，允许用户通过自然语言命令分析和交互 IFC（工业基础类）建筑模型。

# Bonsai-mcp - 通过 IfcOpenShell 实现的 Blender 模型上下文协议 IFC 集成

Bonsai-mcp 是 [BlenderMCP](https://github.com/ahujasid/blender-mcp) 的一个分支，它通过 Bonsai 扩展了原有的功能，特别支持 IFC（Industry Foundation Classes）模型。此集成是一个快速的概念验证，旨在展示将 Claude 或任何 LLM（尽管仅使用 Claude Desktop Client 进行过测试）连接到 Blender 以执行 IfcOpenShell 命令的能力。

## 特性

- **IFC 特定功能**：查询 IFC 模型、分析空间结构和检查建筑元素
- **五个强大的 IFC 工具**：检查项目信息、列出实体、检查属性、探索空间结构和分析关系
- **顺序思考**：包含来自 [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking) 的顺序思考工具，用于结构化问题解决
- **从原始 BlenderMCP 实现中的执行代码工具**：在 Blender 中创建和修改对象、应用材质以及执行 Python 代码
- **使用标准模型进行测试**：已验证与默认 ifcopenshell 房屋模型 ([AC20-FZK-Haus.ifc](https://www.ifcwiki.org/images/e/e3/AC20-FZK-Haus.ifc)) 兼容

## 组件

系统由两个主要组件组成：

1. **Blender 插件 (`addon.py`)**：一个 Blender 插件，在 Blender 内创建一个套接字服务器以接收和执行命令，包括特定于 IFC 的操作
2. **MCP 服务器 (`blender_mcp_tools.py`)**：一个实现 Model Context Protocol 并连接到 Blender 插件的 Python 服务器

## 安装

### 前提条件

- Blender 3.0 或更新版本
- Python 3.10 或更新版本
- uv 包管理器
- 用于 Blender 的 Bonsai BIM 插件（用于 IFC 功能）

**安装 uv：**

**Mac:**
```bash
brew install uv
```

**Windows:**
```bash
powershell -c "irm https://astral.sh/uv/install.ps1 | iex" 
set Path=C:\Users\[username]\.local\bin;%Path%
```

对于其他平台，请参阅 [uv 安装指南](https://docs.astral.sh/uv/getting-started/installation/)。

### 克隆仓库

```bash
git clone https://github.com/JotaDeRodriguez/Bonsai_mcp
```

### Claude for Desktop 集成

编辑您的 `claude_desktop_config.json` 文件（Claude > 设置 > 开发者 > 编辑配置），添加以下内容：

```json
{
    "mcpServers": {
        "Bonsai-mcp": {
            "command": "uv",
            "args": [
              "--directory",
              "\\your\\path\\to\\Bonsai_mcp",
              "run",
              "tools.py"
          ]
        }
    }
}
```

### 安装 Blender 插件

1. 从此仓库下载 `addon.py` 文件
2. 打开 Blender
3. 转到“编辑”>“偏好设置”>“插件”
4. 点击“安装...”并选择 `addon.py` 文件
5. 通过勾选“界面：Blender MCP - IFC”旁边的复选框来启用插件

## 使用

### 启动连接

1. 在 Blender 中，转到 3D 视图侧边栏（如果不可见，请按 N 键）
2. 找到“Blender MCP - IFC”选项卡
3. 点击“连接到 Claude”
4. 确保 MCP 服务器正在运行

### 与 Claude 一起使用

连接后，您将在 Claude 的界面中看到一个锤子图标，其中包含用于 Blender MCP IFC 集成的工具。

## IFC 工具

此分支增加了五个强大的 IFC 特定工具：

### 1. get_ifc_project_info

获取有关 IFC 项目的基本信息，包括名称、描述和不同实体类型的数量。

### 2. list_ifc_entities

列出特定类型的 IFC 实体（墙、门、空间等）。

示例： "列出此 IFC 模型中的所有墙壁" 或 "显示这栋建筑中的窗户"

### 3. get_ifc_properties

通过 GlobalId 获取特定 IFC 实体的所有属性。

示例： "ID 为 1Dvrgv7Tf5IfTEapMkwDQY 的墙有哪些属性？"

### 4. get_ifc_spatial_structure

获取 IFC 模型的空间层次结构（场地、建筑、楼层、空间）。

示例： "显示这栋建筑的空间结构"

### 5. get_ifc_relationships

获取特定 IFC 实体的所有关系。

示例： "入口门有哪些关系？"

## 执行 Blender 代码

这是从原始 MCP 实现中继承的功能。允许 Claude 在 Blender 中执行任意 Python 代码。请谨慎使用。

## 顺序思维工具

此集成还包括顺序思维工具，该工具有助于详细、逐步地进行问题解决和分析。

### 工具参数：

- `thought` (字符串)：当前思考步骤
- `nextThoughtNeeded` (布尔值)：是否需要另一个思考步骤
- `thoughtNumber` (整数)：当前思考步骤编号
- `totalThoughts` (整数)：估计所需的总思考步骤数
- `isRevision` (布尔值, 可选)：是否修订了之前的思考
- `revisesThought` (整数, 可选)：正在重新考虑哪个思考步骤
- `branchFromThought` (整数, 可选)：分支点的思考步骤编号
- `branchId` (字符串, 可选)：分支标识符
- `needsMoreThoughts` (布尔值, 可选)：是否需要更多思考步骤

示例： "使用顺序思维来分析这座建筑的能源效率"

## 示例命令

以下是一些你可以要求 Claude 对 IFC 模型执行的操作示例：

- "分析这个 IFC 模型并告诉我它有多少面墙、门和窗户"
- "显示这个建筑模型的空间结构"
- "列出此 IFC 模型中的所有空间及其属性"
- "识别这栋建筑中的所有结构元素"
- "这面墙与其他元素之间有什么关系？"
- "使用顺序思维根据 IFC 模型为这栋建筑创建维护计划"

## 故障排除

- **连接问题**：确保 Blender 插件服务器正在运行，并且 MCP 服务器已在 Claude 中配置
- **IFC 模型未加载**：验证你已安装 Bonsai BIM 插件并且已加载 IFC 文件
- **超时错误**：尝试简化你的请求或将它们分解成更小的步骤

## 技术细节

IFC 集成使用 Bonsai BIM 模块在 Blender 中访问 ifcopenshell 功能。通信采用与原始 BlenderMCP 相同的基于 JSON 的 TCP 套接字协议。

## 限制与安全注意事项

- 原项目中的 `execute_blender_code` 工具仍然可用，允许在 Blender 中运行任意 Python 代码。请谨慎使用并始终保存您的工作。
- 复杂的 IFC 模型可能需要将操作分解为更小的步骤。
- IFC 查询性能取决于模型的大小和复杂性。

## 致谢

- 原始 BlenderMCP 由 [Siddharth Ahuja](https://github.com/ahujasid/blender-mcp)
- 顺序思维工具来自 [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking)
- IFC 集成基于 Bonsai BIM 插件为 Blender 构建

## 待办事项
- 光标实现
- 添加 'get_selected_ifc_elements' 的描述

**官方网站：** [https://github.com/JotaDeRodriguez/Bonsai_mcp](https://github.com/JotaDeRodriguez/Bonsai_mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`art and culture`, `developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`--directory \your\path\to\Bonsai_mcp run tools.py`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/jotaderodriguez-bonsai.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
