---
title: "QGIS AI连接器"
description: "通过模型上下文协议将 Claude AI 连接到 QGIS，使 Claude 能够直接与 QGIS 交互并对其进行控制，以完成项目创建、图层操作和代码执行等任务。"
---

# QGIS AI连接器

通过模型上下文协议将 Claude AI 连接到 QGIS，使 Claude 能够直接与 QGIS 交互并对其进行控制，以完成项目创建、图层操作和代码执行等任务。

# QGISMCP - QGIS Model Context Protocol 集成

QGISMCP 通过 Model Context Protocol (MCP) 将 [QGIS](https://qgis.org/) 与 [Claude AI](https://claude.ai/chat) 连接起来，允许 Claude 直接与 QGIS 交互并控制它。这种集成支持提示辅助的项目创建、图层加载、代码执行等功能。

该项目强烈基于 [Siddharth Ahuja](https://x.com/sidahuj) 的 [BlenderMCP](https://github.com/ahujasid/blender-mcp/tree/main) 项目。

## 功能

- **双向通信**：通过基于套接字的服务器将 Claude AI 连接到 QGIS。
- **项目操作**：在 QGIS 中创建、加载和保存项目。
- **图层操作**：向项目中添加或移除矢量或栅格图层。
- **执行处理**：执行处理算法（[处理工具箱](https://docs.qgis.org/3.40/en/docs/user_manual/processing/toolbox.html)）。
- **代码执行**：从 Claude 在 QGIS 中运行任意 Python 代码。非常强大，但使用时也需格外小心。

## 组件

系统由两个主要组件组成：

1. **[QGIS 插件](https://github.com/jjsantos01/qgis_mcp/tree/HEAD/qgis_mcp_plugin)**：一个 QGIS 插件，在 QGIS 内创建一个套接字服务器以接收和执行命令。
2. **[MCP 服务器](https://github.com/jjsantos01/qgis_mcp/blob/HEAD/src/qgis_mcp/qgis_mcp_server.py)**：一个实现了 Model Context Protocol 并连接到 QGIS 插件的 Python 服务器。

## 安装

### 前提条件

- QGIS 3.X（仅测试过 3.22 版本）
- 云端桌面
- Python 3.10 或更新版本
- uv 包管理器：

如果你使用的是 Mac，请按如下方式安装 uv：

```bash
brew install uv
```

在 Windows Powershell 中

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

否则请参考其网站上的安装说明：[安装 uv](https://docs.astral.sh/uv/getting-started/installation/)

**⚠️ 在未安装 UV 之前不要继续**

### 下载代码

将此仓库下载到你的计算机上。你可以使用以下命令克隆它：

```bash
git clone git@github.com:jjsantos01/qgis_mcp.git
```

### QGIS 插件

你需要将 [qgis_mcp_plugin](https://github.com/jjsantos01/qgis_mcp/tree/HEAD/qgis_mcp_plugin) 文件夹及其内容复制到你的 QGIS 配置文件插件文件夹中。

你可以在 QGIS 中通过菜单 `设置` -> `用户配置文件` -> `打开活动配置文件夹` 来获取你的配置文件夹。然后进入 `Python/plugins` 并粘贴 `qgis_mcp_plugin` 文件夹。

> 在 Windows 机器上，插件文件夹通常位于：
    `C:\Users\USER\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins`，而在 MacOS 上：
    `~/Library/Application\ Support/QGIS/QGIS3/profiles/default/python/plugins`

然后关闭并重新打开 QGIS。转到菜单选项 `插件` -> `安装和管理插件`，选择 `所有` 标签页并搜索 "QGIS MCP"，然后勾选 QGIS MCP 复选框。

### Claude 桌面集成

转到 `Claude` > `设置` > `开发者` > `编辑配置` > `claude_desktop_config.json` 添加以下内容：

> 如果找不到 "开发者" 选项卡或 `claude_desktop_config.json`，请参阅此 [文档](https://modelcontextprotocol.io/quickstart/user#2-add-the-filesystem-mcp-server)。

```json
{
    "mcpServers": {
        "qgis": {
            "command": "uv",
            "args": [
                "--directory",
                "/ABSOLUTE/PATH/TO/PARENT/REPO/FOLDER/qgis_mcp/src/qgis_mcp",
                "run",
                "qgis_mcp_server.py"
            ]
        }

    }
}
```

## 使用

### 启动连接

1. 在 QGIS 中，进入 `插件` -> `QGIS MCP` -> `QGIS MCP`
    
2. 点击“启动服务器”
    

### 与 Claude 一起使用

一旦在 Claude 上设置了配置文件，并且 QGIS 中的服务器正在运行，你将看到带有 QGIS MCP 工具的锤子图标。

#### 工具

- `ping` - 用于检查服务器连接性的简单 ping 命令
- `get_qgis_info` - 获取当前安装的 QGIS 信息
- `load_project` - 从指定路径加载 QGIS 项目
- `create_new_project` - 创建一个新项目并保存
- `get_project_info` - 获取当前项目信息
- `add_vector_layer` - 向项目中添加矢量图层
- `add_raster_layer` - 向项目中添加栅格图层
- `get_layers` - 检索当前项目中的所有图层
- `remove_layer` - 通过 ID 从项目中移除图层
- `zoom_to_layer` - 缩放到指定图层的范围
- `get_layer_features` - 从矢量图层检索要素（可选限制）
- `execute_processing` - 使用给定参数执行处理算法
- `save_project` - 将当前项目保存到给定路径
- `render_map` - 将当前地图视图渲染为图像文件
- `execute_code` - 执行作为字符串提供的任意 PyQGIS 代码

### 示例命令

这是我在 [演示](https://x.com/jjsantoso/status/1900293848271667395) 中使用的示例：

```plain
You have access to the tools to work with QGIS. You will do the following:
    1. Ping to check the connection. If it works, continue with the following steps.
    2. Create a new project and save it at: "C:/Users/USER/GitHub/qgis_mcp/data/cdmx.qgz"
    3. Load the vector layer: ""C:/Users/USER/GitHub/qgis_mcp/data/cdmx/mgpc_2019.shp" and name it "Colonias".
    4. Load the raster layer: "C:/Users/USER/GitHub/qgis_mcp/data/09014.tif" and name it "BJ"
    5. Zoom to the "BJ" layer.
    6. Execute the centroid algorithm on the "Colonias" layer. Skip the geometry check. Save the output to "colonias_centroids.geojson".
    7. Execute code to create a choropleth map using the "POB2010" field in the "Colonias" layer. Use the quantile classification method with 5 classes and the Spectral color ramp.
    8. Render the map to "C:/Users/USER/GitHub/qgis_mcp/data/cdmx.png"
    9. Save the project.
```

**官方网站：** [https://github.com/jjsantos01/qgis_mcp](https://github.com/jjsantos01/qgis_mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`, `browser`
- 标签：`developer tools`, `os automation`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`--directory /ABSOLUTE/PATH/TO/PARENT/REPO/FOLDER/qgis_mcp/src/qgis_mcp run qgis_mcp_server.py`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/jjsantos01-qgis.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
