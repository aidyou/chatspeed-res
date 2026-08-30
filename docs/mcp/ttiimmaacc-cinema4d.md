---
title: "Cinema 4D AI助手"
description: "将Cinema 4D与Claude连接起来，通过自然语言命令实现人工智能辅助的3D建模和场景操作。"
---

# Cinema 4D AI助手

将Cinema 4D与Claude连接起来，通过自然语言命令实现人工智能辅助的3D建模和场景操作。

# Cinema4D MCP — Model Context Protocol (MCP) 服务器

Cinema4D MCP 服务器将 Cinema 4D 连接到 Claude，使用户能够通过提示辅助进行 3D 操作。

## 目录

- [组件](#components)
- [前提条件](#prerequisites)
- [安装](#installation)
- [设置](#setup)
- [使用](#usage)
- [开发](#development)
- [故障排除与调试](#troubleshooting--debugging)
- [文件结构](#file-structure)
- [工具命令](#tool-commands)

## 组件

1. **C4D 插件**: 一个监听来自 MCP 服务器的命令并在 Cinema 4D 环境中执行这些命令的套接字服务器。
2. **MCP 服务器**: 一个实现 MCP 协议并提供 Cinema 4D 集成工具的 Python 服务器。

## 前提条件

- Cinema 4D
- Python 3.10 或更高版本

## 开发安装

要安装项目，请按照以下步骤操作：

### 克隆仓库

```bash
git clone https://github.com/ttiimmaacc/cinema4d-mcp.git
cd cinema4d-mcp
```

### 安装包

```bash
pip install -e .
```

### 使封装脚本可执行

```bash
chmod +x bin/cinema4d-mcp-wrapper
```

## 设置

### Cinema 4D 插件设置

要设置 Cinema 4D 插件，请按照以下步骤操作：

1. **复制插件文件**: 将 `c4d_plugin/mcp_server_plugin.pyp` 文件复制到 Cinema 4D 的插件文件夹中。路径根据您的操作系统而异：

   - macOS: `/Users/USERNAME/Library/Preferences/Maxon/Maxon Cinema 4D/plugins/`
   - Windows: `C:\Users\USERNAME\AppData\Roaming\Maxon\Maxon Cinema 4D\plugins\`

2. **启动套接字服务器**:
   - 打开 Cinema 4D。
   - 转到扩展 > 套接字服务器插件
   - 您应该会看到一个套接字服务器控制对话框窗口。点击启动服务器。

### Claude Desktop 配置

要配置 Claude Desktop，您需要修改其配置文件：

1. **打开配置文件**:

   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
   - 或者，使用 Claude Desktop 中的设置菜单（设置 > 开发人员 > 编辑配置）。

2. **添加 MCP 服务器配置**:
   对于开发/未发布的服务器，添加以下配置：
```json
   "mcpServers": {
     "cinema4d": {
       "command": "python3",
       "args": ["/Users/username/cinema4d-mcp/main.py"]
     }
   }
```
3. **更新配置文件后重启 Claude Desktop**。

  [TODO] 对于已发布的服务器

```json
{
  "mcpServers": {
    "cinema4d": {
      "command": "cinema4d-mcp-wrapper",
      "args": []
    }
  }
}
```

   

## 使用

1. 确保 Cinema 4D 套接字服务器正在运行。
2. 打开 Claude Desktop 并在输入框中查找锤子图标 🔨，这表示 MCP 工具可用。
3. 使用可用的[工具命令](#tool-commands)通过 Claude 与 Cinema 4D 进行交互。

## 测试

### 命令行测试

要直接从命令行测试 Cinema 4D 套接字服务器：

```bash
python main.py
```

您应该会看到确认服务器成功启动并连接到 Cinema 4D 的输出。

### 使用 MCP 测试框架测试

该仓库包含一个简单的测试框架，用于运行预定义的命令序列：

1. **测试命令文件** (`tests/mcp_test_harness.jsonl`)：包含一系列以 JSONL 格式编写的命令，可以按顺序执行。每一行代表一个带有参数的 MCP 命令。

2. **GUI 测试运行器** (`tests/mcp_test_harness_gui.py`)：一个简单的 Tkinter GUI 用于运行测试命令：

```bash
   python tests/mcp_test_harness_gui.py
```

   该 GUI 允许你：

   - 选择一个 JSONL 测试文件
   - 按顺序运行命令
   - 查看来自 Cinema 4D 的响应

此测试框架特别适用于：

- 快速测试新命令
- 在更新后验证插件功能
- 为调试重新创建复杂场景
- 测试不同版本 Cinema 4D 之间的兼容性

## 故障排除与调试

1. 检查日志文件：

```bash
   tail -f ~/Library/Logs/Claude/mcp*.log
```

2. 确认在打开 Claude Desktop 后，Cinema 4D 控制台显示连接信息。

3. 直接测试包装脚本：

```bash
   cinema4d-mcp-wrapper
```

4. 如果出现找不到 mcp 模块的错误，请全局安装它：

```bash
   pip install mcp
```

5. 对于高级调试，使用 [MCP Inspector](https://github.com/modelcontextprotocol/inspector)：
```bash
   npx @modelcontextprotocol/inspector uv --directory /Users/username/cinema4d-mcp run cinema4d-mcp
```

## 项目文件结构

```
cinema4d-mcp/
├── .gitignore
├── LICENSE
├── README.md
├── main.py
├── pyproject.toml
├── setup.py
├── bin/
│   └── cinema4d-mcp-wrapper
├── c4d_plugin/
│   └── mcp_server_plugin.pyp
├── src/
│   └── cinema4d_mcp/
│       ├── __init__.py
│       ├── server.py
│       ├── config.py
│       └── utils.py
└── tests/
    ├── test_server.py
    ├── mcp_test_harness.jsonl
    └── mcp_test_harness_gui.py
```

## 工具命令

### 场景和执行通用命令

- `get_scene_info`：获取当前 Cinema 4D 场景的概要信息。
- `list_objects`：列出所有场景对象（包括层次结构）。
- `group_objects`：将选定的对象分组到一个新的空对象下。
- `execute_python`：在 Cinema 4D 内执行自定义 Python 代码。
- `save_scene`：将当前 Cinema 4D 项目保存到磁盘。
- `load_scene`：加载一个 `.c4d` 文件到场景中。
- `set_keyframe`：在对象属性上设置关键帧（位置、旋转等）。

### 对象创建与修改

- `add_primitive`：向场景中添加一个基本体（立方体、球体、圆锥等）。
- `modify_object`：修改现有对象的变换或属性。
- `create_abstract_shape`：创建一个有机的、非标准的抽象形状。

### 摄像机与动画

- `create_camera`：向场景中添加一个新的摄像机。
- `animate_camera`：沿路径（线性或样条）动画化摄像机。

### 灯光与材质

- `create_light`：向场景中添加灯光（全向光、聚光灯等）。
- `create_material`：创建一个标准的 Cinema 4D 材质。
- `apply_material`：将材质应用到目标对象。
- `apply_shader`：生成并应用风格化或程序化着色器。

### Redshift 支持

- `validate_redshift_materials`：检查 Redshift 材质设置和连接。

### MoGraph 与场

- `create_mograph_cloner`：添加一个 MoGraph 克隆器（线性、径向、网格等）。
- `add_effector`：添加一个 MoGraph 效应器（随机、平面等）。
- `apply_mograph_fields`：添加并将 MoGraph 场链接到对象。

### 动力学与物理

- `create_soft_body`: 为对象添加软体标签。
- `apply_dynamics`: 应用刚体或软体物理效果。

### 渲染与预览

- `render_frame`: 渲染一帧并保存到磁盘（仅文件输出）。
- `render_preview`: 渲染快速预览并返回 base64 图像（供 AI 使用）。
- `snapshot_scene`: 捕获场景快照（包括对象和预览图像）。

## 兼容性计划与路线图

| Cinema 4D 版本 | Python 版本 | 兼容性状态 | 备注                                             |
| ----------------- | -------------- | -------------------- | ------------------------------------------------- |
| R21 / S22         | Python 2.7     | ❌ 不支持     | 旧版 API 和 Python 版本过时             |
| R23               | Python 3.7     | 🔍 未计划       | 目前未测试                              |
| S24 / R25 / S26   | Python 3.9     | ⚠️ 可能（待定）    | 需要测试并对缺失的 API 进行回退处理   |
| 2023.0 / 2023.1   | Python 3.9     | 🧪 进行中       | 为核心功能提供回退支持                 |
| 2023.2            | Python 3.10    | 🧪 进行中       | 与计划的测试基础保持一致                  |
| 2024.0            | Python 3.11    | ✅ 支持         | 已验证                                          |
| 2025.0+           | Python 3.11    | ✅ 完全支持   | 主要开发目标                        |

### 兼容性目标

- **短期目标**：确保与 C4D 2023.1+（Python 3.9 和 3.10）兼容
- **中期目标**：为缺失的 MoGraph 和 Field API 添加条件处理
- **长期目标**：如果需求出现，考虑为 R23–S26 支持提供可选的旧插件模块

## 最近修复的问题

- 修复了 MoGraph 字段中“应用到：无”的问题
  - 通过直接在目标对象下插入来修复字段层次结构
  - 实现了适用于 Cinema 4D 2025.1 的正确字段驱动器标签连接
  - 增加了多种字段链接方法以实现最大兼容性
  - 通过使用多个参数 ID 启用了“使用字段”复选框
  - 修复了字段可见性和父子关系问题
- 通过提供正确的参数 ID 修复了网格克隆器创建问题
- 通过定义适当的字段类型常量修复了 MoGraph 字段应用问题
- 在 list_objects 命令中改进了层次显示
- 提高了克隆器可见性和创建可靠性

**官方网站：** [https://github.com/ttiimmaacc/cinema4d-mcp](https://github.com/ttiimmaacc/cinema4d-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`art and culture`, `image and video processing`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`cinema4d-mcp-wrapper`
- 参数：无

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/ttiimmaacc-cinema4d.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
