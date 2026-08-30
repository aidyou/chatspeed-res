---
title: "Blender"
description: "通过模型上下文协议（MCP）将Blender连接到Claude AI，使Claude能够直接与Blender交互并对其进行控制，从而实现AI辅助的3D建模、场景操作和渲染。"
---

# Blender

通过模型上下文协议（MCP）将Blender连接到Claude AI，使Claude能够直接与Blender交互并对其进行控制，从而实现AI辅助的3D建模、场景操作和渲染。

# BlenderMCP - Blender 模型上下文协议集成

BlenderMCP 通过模型上下文协议 (MCP) 将 Blender 连接到 Claude AI，使 Claude 能够直接与 Blender 交互并控制它。此集成支持通过提示辅助进行3D建模、场景创建和操作。

[完整教程](https://www.youtube.com/watch?v=lCyQ717DuzQ)

### 加入社区

提供反馈，获取灵感，并在此基础上构建：[Discord](https://discord.gg/xcJxvuW6)

### 支持者

**主要支持者:**

[CodeRabbit](https://www.coderabbit.ai/)

**所有支持者:**

[支持此项目](https://github.com/sponsors/ahujasid)

## 发布说明 (1.1.0)

- 通过 Poly Haven API 增加了对 Poly Haven 资源的支持
- 通过 Hyper3D Rodin 增加了提示3D模型的支持
- 对于新用户，可以直接跳到安装部分。对于现有用户，请参阅以下几点
- 下载最新的 addon.py 文件替换旧文件，然后添加到 Blender 中
- 从 Claude 中删除 MCP 服务器并重新添加，这样应该就可以正常工作了！

## 功能

- **双向通信**：通过基于套接字的服务器将 Claude AI 连接到 Blender
- **对象操作**：在 Blender 中创建、修改和删除3D对象
- **材质控制**：应用和修改材质和颜色
- **场景检查**：获取当前 Blender 场景的详细信息
- **代码执行**：从 Claude 执行任意 Python 代码

## 组件

系统由两个主要组件组成：

1. **Blender 插件 (`addon.py`)**：一个 Blender 插件，在 Blender 内部创建一个套接字服务器以接收和执行命令
2. **MCP 服务器 (`src/blender_mcp/server.py`)**：一个实现模型上下文协议并连接到 Blender 插件的 Python 服务器

## 安装

### 先决条件

- Blender 3.0 或更高版本
- Python 3.10 或更高版本
- uv 包管理器:

**如果你使用的是 Mac，请按如下方式安装 uv**
```bash
brew install uv
```
**在 Windows 上**
```bash
powershell -c "irm https://astral.sh/uv/install.ps1 | iex" 
```
然后
```bash
set Path=C:\Users\nntra\.local\bin;%Path%
```

其他安装说明请参见其网站：[安装 uv](https://docs.astral.sh/uv/getting-started/installation/)

**⚠️ 在安装 UV 之前请勿继续**

### Claude 桌面集成

[观看设置说明视频](https://www.youtube.com/watch?v=neoK_WMq92g)（假设你已经安装了 uv）

转到 Claude > 设置 > 开发者 > 编辑配置 > claude_desktop_config.json 并包含以下内容：

```json
{
    "mcpServers": {
        "blender": {
            "command": "uvx",
            "args": [
                "blender-mcp"
            ]
        }
    }
}
```

### 光标集成

通过 uvx 运行 blender-mcp 而不永久安装它。转到光标设置 > MCP 并粘贴此命令。

```bash
uvx blender-mcp
```

[光标设置视频](https://www.youtube.com/watch?v=wgWsJshecac)

**⚠️ 仅运行一个 MCP 服务器实例（要么在光标上，要么在 Claude 桌面上），不要同时运行两者**

### 安装 Blender 插件

1. 从此仓库下载 `addon.py` 文件
1. 打开 Blender
2. 转到编辑 > 首选项 > 插件
3. 点击“安装...”并选择 `addon.py` 文件
4. 通过选中“界面: Blender MCP”旁边的复选框启用插件

## 使用

### 启动连接

1. 在 Blender 中，转到 3D 视图侧边栏（如果不可见，请按 N 键）
2. 找到 "BlenderMCP" 标签
3. 如果你希望从他们的 API 获取资源，请勾选 Poly Haven 复选框（可选）
4. 点击 "连接到 Claude"
5. 确保 MCP 服务器在你的终端中运行

### 与 Claude 一起使用

一旦在 Claude 上设置了配置文件，并且插件在 Blender 上运行，你将在 Blender MCP 中看到带有工具的锤子图标。

#### 功能

- 获取场景和对象信息
- 创建、删除和修改形状
- 为对象应用或创建材质
- 在 Blender 中执行任何 Python 代码
- 通过 [Poly Haven](https://polyhaven.com/) 下载正确的模型、资产和 HDRIs
- 通过 [Hyper3D Rodin](https://hyper3d.ai/) 生成 AI 3D 模型

### 示例命令

以下是一些你可以要求 Claude 执行的示例：

- "在一个地牢中创建一个低多边形场景，其中有一条龙守护着一锅金子" [演示](https://www.youtube.com/watch?v=DqgKuLYUv00)
- "使用 HDRIs、纹理以及来自 Poly Haven 的岩石和植被等模型来创建海滩氛围" [演示](https://www.youtube.com/watch?v=I29rn92gkC4)
- 提供参考图片，并根据它创建一个 Blender 场景 [演示](https://www.youtube.com/watch?v=FDRb03XPiRo)
- "通过 Hyper3D 生成一个花园侏儒的 3D 模型"
- "获取当前场景的信息，并从中制作一个 threejs 草图" [演示](https://www.youtube.com/watch?v=jxbNI5L7AH8)
- "让这辆车变成红色并且具有金属质感"
- "创建一个球体并将其放置在立方体上方"
- "使照明像工作室一样"
- "将相机对准场景，并使其呈现等距视角"

## Hyper3D 集成

Hyper3D 的免费试用密钥允许你每天生成有限数量的模型。如果达到每日限制，你可以等待次日重置或从 hyper3d.ai 和 fal.ai 获取自己的密钥。

## 故障排除

- **连接问题**：确保 Blender 插件服务器正在运行，并且已在 Claude 上配置了 MCP 服务器，不要在终端中运行 uvx 命令。有时第一个命令无法通过，但之后会开始正常工作。
- **超时错误**：尝试简化你的请求或将它们分解为更小的步骤
- **Poly Haven 集成**：Claude 有时行为不稳定
- **是否尝试过重启？**：如果你仍然遇到连接错误，尝试重新启动 Claude 和 Blender 服务器

## 技术细节

### 通信协议

系统使用基于 TCP 套接字的简单 JSON 协议：

- **命令** 作为包含 `type` 和可选 `params` 的 JSON 对象发送
- **响应** 是包含 `status` 和 `result` 或 `message` 的 JSON 对象

## 限制与安全注意事项

- `execute_blender_code` 工具允许在Blender中运行任意的Python代码，这可能会非常强大但也具有潜在危险。在生产环境中使用时请务必谨慎。在使用此工具前请**始终**保存您的工作。
- Poly Haven 需要下载模型、纹理和HDRI图像。如果您不想使用它，请在Blender中的复选框里关闭它。
- 复杂的操作可能需要分解成更小的步骤

## 贡献

欢迎贡献！请随时提交Pull Request。

## 免责声明

这是一个第三方集成，并非由Blender官方制作。由[Siddharth](https://x.com/sidahuj)制作。

**官方网站：** [https://github.com/ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`image and video processing`, `developer tools`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`blender-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/ahujasid-blender.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
