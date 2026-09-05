---
title: "可视化图表-MCP-Server"
description: "这是一个基于AntV的模型上下文协议服务器，用于生成图表。它支持超过20种类型的图表，并且可以与多种桌面应用程序和平台一起使用。"
---

# 可视化图表-MCP-Server

这是一个基于AntV的模型上下文协议服务器，用于生成图表。它支持超过20种类型的图表，并且可以与多种桌面应用程序和平台一起使用。

# MCP 服务器图表  ![](/mcp-assets/c1486b4e2d8cfd67ed0257afeefda188.svg 'MCP 服务器')  [![构建](/mcp-assets/028e5ab54615f767fa595703c0ea8476.svg)](https://github.com/antvis/mcp-server-chart/actions/workflows/build.yml) [![npm 版本](/mcp-assets/f9d26838f9b033046358b612f96109cc.svg)](https://www.npmjs.com/package/@antv/mcp-server-chart) [Smithery](https://smithery.ai/server/@antvis/mcp-server-chart) [![npm 许可证](/mcp-assets/5816f652aa1f0cc4eedb21a2f733e09e.svg)](https://www.npmjs.com/package/@antv/mcp-server-chart)

一个用于生成图表的 Model Context Protocol 服务器，使用 [AntV](https://github.com/antvis/)。

  

这是一个基于 TypeScript 的 MCP 服务器，提供了图表生成功能。它允许您通过 MCP
工具创建各种类型的图表。您也可以在 [Dify](https://marketplace.dify.ai/plugins/antv/visualization) 中使用它。

## ✨ 功能

现已支持 20 多种图表。

1. `generate_area_chart`: 生成 `面积` 图表，用于显示连续自变量下的数据趋势，便于观察整体数据趋势。
1. `generate_bar_chart`: 生成 `条形` 图表，用于比较不同类别的值，适合水平比较。
1. `generate_boxplot_chart`: 生成 `箱线图`，用于显示数据分布，包括中位数、四分位数和异常值。
1. `generate_column_chart`: 生成 `柱状` 图表，用于比较不同类别的值，适合垂直比较。
1. `generate_district_map` - 生成 `行政区划地图`，用于显示行政区域划分和数据分布。
1. `generate_dual_axes_chart`: 生成 `双轴` 图表，用于显示两个具有不同单位或范围的变量之间的关系。
1. `generate_fishbone_diagram`: 生成 `鱼骨图`，也称为石川图，用于识别并显示问题的根本原因。
1. `generate_flow_diagram`: 生成 `流程图`，用于显示过程中的步骤和顺序。
1. `generate_funnel_chart`: 生成 `漏斗` 图表，用于显示不同阶段的数据流失情况。
1. `generate_histogram_chart`: 生成 `直方图`，通过将数据分成区间并计算每个区间内的数据点数量来显示数据分布。
1. `generate_line_chart`: 生成 `折线` 图表，用于显示随时间或其他连续变量变化的数据趋势。
1. `generate_liquid_chart`: 生成 `液体` 图表，用于显示数据的比例，以水填充球体的形式直观表示百分比。
1. `generate_mind_map`: 生成 `思维导图`，用于显示思维过程和层次信息。
1. `generate_network_graph`: 生成 `网络` 图，用于显示节点之间的关系和连接。
1. `generate_organization_chart`: 生成 `组织结构` 图表，用于显示组织结构和人员关系。
1. `generate_path_map` - 生成 `路径地图`，用于显示 POI 的路线规划结果。
1. `generate_pie_chart`: 生成 `饼图`，用于显示数据的比例，将其分为由扇形表示的部分，显示每个部分的百分比。
1. `generate_pin_map` - 生成 `标记地图`，用于显示 POI 的分布。
1. `generate_radar_chart`: 生成 `雷达` 图表，用于全面显示多维数据，在类似雷达的格式中显示多个维度。1.
   `generate_sankey_chart`: 生成`sankey`图，用于显示数据流和量，以Sankey样式格式表示不同节点间的数据流动。
1. `generate_scatter_chart`: 生成`scatter`散点图，用于显示两个变量之间的关系，在坐标系上以分散的点形式展示数据点。
1. `generate_treemap_chart`: 生成`treemap`树状图，用于显示层次结构数据，通过矩形的形式展现数据，其中矩形的大小代表数据值。
1. `generate_venn_chart`: 生成`venn`文氏图，用于显示集合间的关系，包括交集、并集和差集。
1. `generate_violin_chart`: 生成`violin`小提琴图，用于显示数据分布情况，结合箱线图和密度图的特点提供更详细的数据分布视图。
1. `generate_word_cloud_chart`: 生成`word-cloud`词云图，用于显示文本数据中词语出现的频率，字体大小表示每个词的频率。

> [!NOTE]
> 上述地理可视化图表生成工具使用[AMap服务](https://lbs.amap.com/)，目前仅支持在中国范围内的地图生成。

## 🤖 使用方法

与`桌面应用程序`如Claude, VSCode, [Cline](https://cline.bot/mcp-marketplace), Cherry Studio,
Cursor等一起使用时，请添加以下MCP服务器配置。在Mac系统上：

```json
{
  "mcpServers": {
    "mcp-server-chart": {
      "command": "npx",
      "args": [
        "-y",
        "@antv/mcp-server-chart"
      ]
    }
  }
}
```

在Windows系统上：

```json
{
  "mcpServers": {
    "mcp-server-chart": {
      "command": "cmd",
      "args": [
        "/c",
        "npx",
        "-y",
        "@antv/mcp-server-chart"
      ]
    }
  }
}
```

此外，您还可以通过HTTP或SSE协议在[阿里云](https://bailian.console.aliyun.com/?tab=mcp#/mcp-market/detail/antv-visualization-chart)、[modelscope](https://www.modelscope.cn/mcp/servers/@antvis/mcp-server-chart)、[glama.ai](https://glama.ai/mcp/servers/@antvis/mcp-server-chart)
或 [smithery.ai](https://smithery.ai/server/@antvis/mcp-server-chart) 等平台上使用它。

## 🚰 通过SSE或Streamable传输运行

全局安装包。

bash
npm install -g @antv/mcp-server-chart

使用您偏好的传输选项运行服务器：

```bash
# 对于SSE传输（默认端点: /sse）
mcp-server-chart --transport sse

# 对于具有自定义端点的Streamable传输
mcp-server-chart --transport streamable
```

然后您可以访问服务器：

- SSE传输：`http://localhost:1122/sse`
- Streamable传输：`http://localhost:1122/mcp`

## 🎮 CLI选项

运行MCP服务器时也可以使用以下CLI选项。通过运行带有`-h`参数的命令来查看选项。

plain
MCP Server Chart CLI

选项:
--transport, -t 指定传输协议："stdio"、"sse" 或 "streamable"（默认："stdio"）
--port, -p 为SSE或streamable传输指定端口（默认：1122）
--endpoint, -e 指定传输端点：

- 对于SSE：默认是"/sse"
- 对于streamable：默认是"/mcp"
  --help, -h 显示此帮助信息

## 📠 私有部署

`MCP Server Chart` 默认提供免费的图表生成服务。对于需要私有部署的用户，可以尝试使用`VIS_REQUEST_SERVER`来自定义自己的图表生成服务。

```json
{
  "mcpServers": {
    "mcp-server-chart": {
      "command": "npx",
      "args": [
        "-y",
        "@antv/mcp-server-chart"
      ],
      "env": {
        "VIS_REQUEST_SERVER": ""
      }
    }
  }
}
```

您可以使用AntV的项目[GPT-Vis-SSR](https://github.com/antvis/GPT-Vis/tree/main/bindings/gpt-vis-ssr)
在私有环境中部署HTTP服务，然后通过环境变量`VIS_REQUEST_SERVER`传递URL地址。

- **方法**：`POST`- **参数**：将传递给 `GPT-Vis-SSR` 用于渲染。例如，
  `{ "type": "line", "data": [{ "time": "2025-05", "value": "512" }, { "time": "2025-06", "value": "1024" }] }`。
- **返回值**：HTTP 服务的返回对象。
    - **success**：`boolean` 是否成功生成图表图像。
    - **resultObj**：`string` 图表图像的 URL。
    - **errorMessage**：`string` 当 `success = false` 时，返回错误信息。

> [!NOTE]
> 私有部署方案目前不支持地理可视化图表生成，包括以下3个工具：`geographic-district-map`、`geographic-path-map`、
`geographic-pin-map`。

## 🗺️ 生成记录

默认情况下，用户需要自行保存结果，但我们还提供了一项查看图表生成记录的服务，这需要用户为自己生成一个服务标识符并进行配置。

使用支付宝扫描并打开小程序以生成个人服务标识符（点击下方“我的”菜单，进入“我的服务”页面，点击“生成”按钮，在成功后点击“复制”按钮）：

接下来，你需要在 MCP 服务器配置中添加 `SERVICE_ID` 环境变量。例如，Mac 的配置如下（对于 Windows 系统，只需添加 `env` 变量即可）：

```json
{
  "mcpServers": {
    "AntV Map": {
      "command": "npx",
      "args": [
        "-y",
        "@antv/mcp-server-chart"
      ],
      "env": {
        "SERVICE_ID": "***********************************"
      }
    }
  }
}
```

更新 MCP 服务器配置后，你需要重启你的 AI 客户端应用程序，并再次检查是否已成功启动并连接到 MCP
服务器。然后你可以尝试重新生成地图。生成成功后，你可以前往小程序中的“我的地图”页面查看你的地图生成记录。

## 🔨 开发

安装依赖：

```bash
npm install
```

构建服务器：

```bash
npm run build
```

启动 MCP 服务器：

```bash
npm run start
```

## 📄 许可证

MIT@[AntV](https://github.com/antvis)。

**官方网站：** [https://github.com/antvis/mcp-server-chart](https://github.com/antvis/mcp-server-chart)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `antv`, `visualization`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @antv/mcp-server-chart`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/antvis-chart.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
