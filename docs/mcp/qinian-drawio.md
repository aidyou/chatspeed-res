---
title: "drawio-mcp-server"
description: "Draw.io MCP 服务器是一种实现，它为AI代理系统带来了强大的图表绘制能力。此集成实现了：\n- 无缝绘图。"
---

# drawio-mcp-server

Draw.io MCP 服务器是一种实现，它为AI代理系统带来了强大的图表绘制能力。此集成实现了：
- 无缝绘图。

# Draw.io MCP 服务器

让我们使用最广泛使用的绘图工具 Draw.io（Diagrams.net）来进行一些 Vibe 图表绘制。

[Actions](https://github.com/lgazo/drawio-mcp-server/actions/workflows/ci.yml)

## 简介

Draw.io MCP 服务器是一个 [模型上下文协议 (MCP)](https://modelcontextprotocol.io) 的实现，它为 AI 代理系统带来了强大的图表功能。此集成实现了以下功能：

- **无缝 Draw.io 集成**：将您的 MCP 支持的应用程序与 Draw.io 丰富的图表功能连接起来
- **编程式图表控制**：通过 MCP 命令创建、修改和管理图表内容
- **智能图表分析**：检索有关图表及其组件的详细信息，供 AI 代理处理
- **代理系统开发**：构建包含可视化建模和图表自动化的复杂 AI 工作流

作为符合 MCP 标准的工具，它遵循工具集成的标准协议，使其与任何 MCP 客户端兼容。这种实现对于需要以下功能的 AI 系统特别有价值：
- 生成架构图
- 可视化复杂关系
- 注释技术文档
- 以编程方式创建流程图和过程图

该工具支持双向通信，允许同时控制 Draw.io 实例并提取图表信息，以便在您的 MCP 生态系统中由 AI 代理进一步处理。

## 要求

要使用 Draw.io MCP 服务器，您需要：

### 核心组件
- **Node.js** (v18 或更高版本) - MCP 服务器的运行时环境
- **Draw.io MCP 浏览器扩展** - 启用 Draw.io 和 MCP 服务器之间的通信

### MCP 生态系统
- **MCP 客户端**（例如，[MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector)）- 用于测试和调试集成
- **支持工具的语言模型 (LLM)** - 任何能够处理 MCP 工具调用的语言模型（例如，GPT-4, Claude 3 等）

### 开发可选项
- **pnpm** - 推荐的包管理器
- **Chrome DevTools** - 使用 `--inspect` 标志进行调试时使用

注意：Draw.io 桌面应用程序或网页版本必须对运行 MCP 服务器的系统可访问。

## 安装

### 与 Claude Desktop 连接

1. 安装 [Claude Desktop](https://claude.ai/download)
2. 打开或创建配置文件：
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`

3. 更新配置文件以包含此服务器：

  使用 npm

```json

{

   "mcpServers":{

      "drawio":{

         "command":"npx",

         "args":[

            "-y",

            "drawio-mcp-server"

         ]

      }

   }

}

```

  使用 pnpm

```json

{

   "mcpServers":{

      "drawio":{

         "command":"pnpm",

         "args":[

            "dlx",

            "drawio-mcp-server"

         ]

      }

   }

}

```

4. 重启 Claude Desktop

### 与 oterm 连接

如果您喜欢终端并且计划连接到自己的 Ollama 实例，这是一个替代的 MCP 客户端。

配置文件通常位于：~/.local/share/oterm/config.json

  使用 npm

```json

{

	"mcpServers": {

		"drawio": {

			"command": "npx",

			"args": [

			  "-y",

        "drawio-mcp-server"

			]

		}

	}

}

```

  使用 pnpm

```json

{

	"mcpServers": {

		"drawio": {

			"command": "pnpm",

			"args": [

			  "dlx",

        "drawio-mcp-server"

			]

		}

	}

}

```

### 与 Zed 连接

1. 打开 Zed 预览应用程序。
1. 单击右下角的助手 (✨) 图标。
1. 在助手面板的右上角单击设置。
1. 在上下文服务器部分，点击 + 添加上下文服务器。
1. 使用以下配置：

  使用 npm

```json

{

  /// The name of your MCP server

  "drawio": {

    "command": {

      /// The path to the executable

      "path": "npx",

      /// The arguments to pass to the executable

      "args": ["-y","drawio-mcp-server"],

      /// The environment variables to set for the executable

      "env": {}

    }

  }

}

```

  使用 pnpm

```json

{

  /// The name of your MCP server

  "drawio": {

    "command": {

      /// The path to the executable

      "path": "pnpm",

      /// The arguments to pass to the executable

      "args": ["dlx","drawio-mcp-server"],

      /// The environment variables to set for the executable

      "env": {}

    }

  }

}

```

### 浏览器扩展设置

为了控制 Draw.io 图表，您需要安装专用的浏览器扩展。

1. 在浏览器中打开 [Draw.io](https://app.diagrams.net/)
2. 从网络商店安装 Draw.io MCP 浏览器扩展，或者 [使用其他方法](https://github.com/lgazo/drawio-mcp-extension)

  

    

       alt="Chrome Web Store" />

  

    

      
       alt="Firefox add-ons" />

3. 确保已连接，扩展图标应显示绿色信号覆盖  />

## 功能

Draw.io MCP 服务器提供了以下用于程序化图表交互的工具：

### 图表检查工具
- **`get-selected-cell`**
  获取 Draw.io 中当前选中的单元格及其所有属性
  *返回*: 包含单元格属性（ID、几何形状、样式、值等）的 JSON 对象

- **`get-shape-categories`**
  从图表库中检索可用的形状类别
  *返回*: 包含类别 ID 和名称的类别对象数组

- **`get-shapes-in-category`**
  从图表库中检索指定类别的所有形状
  *参数*:
    - `category_id`: 要检索形状的类别的标识符
  *返回*: 包含形状属性和样式的形状对象数组

- **`get-shape-by-name`**
  通过名称从所有可用形状中检索特定形状
  *参数*:
    - `shape_name`: 要检索的形状的名称
  *返回*: 包括其类别和样式信息的形状对象

### 图表修改工具
- **`add-rectangle`**
  在活动的 Draw.io 页面上创建一个具有可自定义属性的新矩形形状：
  - 位置 (`x`, `y` 坐标)
  - 尺寸 (`width`, `height`)
  - 文本内容
  - 视觉样式（填充颜色、描边等，使用 Draw.io 样式语法）

- **`add-edge`**
  在两个单元格（顶点）之间创建连接
  *参数*:
    - `source_id`: 源单元格的 ID
    - `target_id`: 目标单元格的 ID
    - `text`: 边缘的可选文本标签
    - `style`: 边缘的可选样式属性

- **`delete-cell-by-id`**
  从图表中删除指定的单元格
  *参数*:
    - `cell_id`: 要删除的单元格的 ID

- **`add-cell-of-shape`**
  从图表库中添加一个特定形状类型的新单元格
  *参数*:
    - `shape_name`: 要创建的形状的名称
    - `x`, `y`: 位置坐标（可选）
    - `width`, `height`: 尺寸（可选）
    - `text`: 可选文本内容
    - `style`: 可选附加样式属性

## 相关资源

[故障排除](https://github.com/lgazo/drawio-mcp-server/blob/HEAD/TROUBLESHOOTING.md)

提示示例

[贡献指南](https://github.com/lgazo/drawio-mcp-server/blob/HEAD/CONTRIBUTING.md)

[架构](https://github.com/lgazo/drawio-mcp-server/blob/HEAD/ARCHITECTURE.md)

[开发](https://github.com/lgazo/drawio-mcp-server/blob/HEAD/DEVELOPMENT.md)

**官方网站：** [https://github.com/lgazo/drawio-mcp-server](https://github.com/lgazo/drawio-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y drawio-mcp-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/qinian-drawio.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
