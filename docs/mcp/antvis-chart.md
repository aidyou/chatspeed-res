---
title: "mcp-server-chart"
description: "MCP Server Chart A Model Context Protocol server for generating charts using AntV."
---

# mcp-server-chart

MCP Server Chart A Model Context Protocol server for generating charts using AntV.

# MCP Server Chart  ![](/mcp-assets/c1486b4e2d8cfd67ed0257afeefda188.svg 'MCP Server')  [![build](/mcp-assets/028e5ab54615f767fa595703c0ea8476.svg)](https://github.com/antvis/mcp-server-chart/actions/workflows/build.yml) [![npm Version](/mcp-assets/f9d26838f9b033046358b612f96109cc.svg)](https://www.npmjs.com/package/@antv/mcp-server-chart) [Smithery](https://smithery.ai/server/@antvis/mcp-server-chart) [![npm License](/mcp-assets/5816f652aa1f0cc4eedb21a2f733e09e.svg)](https://www.npmjs.com/package/@antv/mcp-server-chart)

A Model Context Protocol server for generating charts using [AntV](https://github.com/antvis/).

  

This is a TypeScript-based MCP server that provides chart generation capabilities. It allows you to create various types of charts through MCP tools. You can also use it in [Dify](https://marketplace.dify.ai/plugins/antv/visualization).

## ✨ Features

Now 20+ charts supported.

1. `generate_area_chart`: Generate an `area` chart, used to display the trend of data under a continuous independent variable, allowing observation of overall data trends.
1. `generate_bar_chart`: Generate a `bar` chart, used to compare values across different categories, suitable for horizontal comparisons.
1. `generate_boxplot_chart`: Generate a `boxplot`, used to display the distribution of data, including the median, quartiles, and outliers.
1. `generate_column_chart`: Generate a `column` chart, used to compare values across different categories, suitable for vertical comparisons.
1. `generate_district_map` - Generate a `district-map`, used to show administrative divisions and data distribution.
1. `generate_dual_axes_chart`: Generate a `dual-axes` chart, used to display the relationship between two variables with different units or ranges.
1. `generate_fishbone_diagram`: Generate a `fishbone` diagram, also known as an Ishikawa diagram, used to identify and display the root causes of a problem.
1. `generate_flow_diagram`: Generate a `flowchart`, used to display the steps and sequence of a process.
1. `generate_funnel_chart`: Generate a `funnel` chart, used to display data loss at different stages.
1. `generate_histogram_chart`: Generate a `histogram`, used to display the distribution of data by dividing it into intervals and counting the number of data points in each interval.
1. `generate_line_chart`: Generate a `line` chart, used to display the trend of data over time or another continuous variable.
1. `generate_liquid_chart`: Generate a `liquid` chart, used to display the proportion of data, visually representing percentages in the form of water-filled spheres.
1. `generate_mind_map`: Generate a `mind-map`, used to display thought processes and hierarchical information.
1. `generate_network_graph`: Generate a `network` graph, used to display relationships and connections between nodes.
1. `generate_organization_chart`: Generate an `organizational` chart, used to display the structure of an organization and personnel relationships.
1. `generate_path_map` - Generate a `path-map`, used to display route planning results for POIs.
1. `generate_pie_chart`: Generate a `pie` chart, used to display the proportion of data, dividing it into parts represented by sectors showing the percentage of each part.
1. `generate_pin_map` - Generate a `pin-map`, used to show the distribution of POIs.
1. `generate_radar_chart`: Generate a `radar` chart, used to display multi-dimensional data comprehensively, showing multiple dimensions in a radar-like format.
1. `generate_sankey_chart`: Generate a `sankey` chart, used to display data flow and volume, representing the movement of data between different nodes in a Sankey-style format.
1. `generate_scatter_chart`: Generate a `scatter` plot, used to display the relationship between two variables, showing data points as scattered dots on a coordinate system.
1. `generate_treemap_chart`: Generate a `treemap`, used to display hierarchical data, showing data in rectangular forms where the size of rectangles represents the value of the data.
1. `generate_venn_chart`: Generate a `venn` diagram, used to display relationships between sets, including intersections, unions, and differences.
1. `generate_violin_chart`: Generate a `violin` plot, used to display the distribution of data, combining features of boxplots and density plots to provide a more detailed view of the data distribution.
1. `generate_word_cloud_chart`: Generate a `word-cloud`, used to display the frequency of words in textual data, with font sizes indicating the frequency of each word.

> [!NOTE]
> The above geographic visualization chart generation tool uses [AMap service](https://lbs.amap.com/) and currently only supports map generation within China.

## 🤖 Usage

To use with `Desktop APP`, such as Claude, VSCode, [Cline](https://cline.bot/mcp-marketplace), Cherry Studio, Cursor, and so on, add the MCP server config below. On Mac system:

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

On Window system:

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

Also, you can use it on [aliyun](https://bailian.console.aliyun.com/?tab=mcp#/mcp-market/detail/antv-visualization-chart), [modelscope](https://www.modelscope.cn/mcp/servers/@antvis/mcp-server-chart), [glama.ai](https://glama.ai/mcp/servers/@antvis/mcp-server-chart), [smithery.ai](https://smithery.ai/server/@antvis/mcp-server-chart) or others with HTTP, SSE Protocol.

## 🚰 Run with SSE or Streamable transport

Install the package globally.

```bash
npm install -g @antv/mcp-server-chart
```

Run the server with your preferred transport option:

```bash
# For SSE transport (default endpoint: /sse)
mcp-server-chart --transport sse

# For Streamable transport with custom endpoint
mcp-server-chart --transport streamable
```

Then you can access the server at:

- SSE transport: `http://localhost:1122/sse`
- Streamable transport: `http://localhost:1122/mcp`

## 🎮 CLI Options

You can also use the following CLI options when running the MCP server. Command options by run cli with `-h`.

```plain
MCP Server Chart CLI

Options:
  --transport, -t  Specify the transport protocol: "stdio", "sse", or "streamable" (default: "stdio")
  --port, -p       Specify the port for SSE or streamable transport (default: 1122)
  --endpoint, -e   Specify the endpoint for the transport:
                   - For SSE: default is "/sse"
                   - For streamable: default is "/mcp"
  --help, -h       Show this help message
```

## 📠 Private Deployment

`MCP Server Chart` provides a free chart generation service by default. For users with a need for private deployment, they can try using `VIS_REQUEST_SERVER` to customize their own chart generation service.

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

You can use AntV's project [GPT-Vis-SSR](https://github.com/antvis/GPT-Vis/tree/main/bindings/gpt-vis-ssr) to deploy an HTTP service in a private environment, and then pass the URL address through env `VIS_REQUEST_SERVER`.

- **Method**: `POST`
- **Parameter**: Which will be passed to `GPT-Vis-SSR` for renderring. Such as, `{ "type": "line", "data": [{ "time": "2025-05", "value": "512" }, { "time": "2025-06", "value": "1024" }] }`.
- **Return**: The return object of HTTP service.
  - **success**: `boolean` Whether generate chart image successfully.
  - **resultObj**: `string` The chart image url.
  - **errorMessage**: `string` When `success = false`, return the error message.

> [!NOTE]
> The private deployment solution currently does not support geographic visualization chart generation include 3 tools: `geographic-district-map`, `geographic-path-map`, `geographic-pin-map`.

## 🗺️ Generate Records

By default, users are required to save the results themselves, but we also provide a service for viewing the chart generation records, which requires users to generate a service identifier for themselves and configure it.

Use Alipay to scan and open the mini program to generate a personal service identifier (click the "My" menu below, enter the "My Services" page, click the "Generate" button, and click the "Copy" button after success):

Next, you need to add the `SERVICE_ID` environment variable to the MCP server configuration. For example, the configuration for Mac is as follows (for Windows systems, just add the `env` variable):

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

After updating the MCP Server configuration, you need to restart your AI client application and check again whether you have started and connected to the MCP Server successfully. Then you can try to generate the map again. After the generation is successful, you can go to the "My Map" page of the mini program to view your map generation records.

## 🔨 Development

Install dependencies:

```bash
npm install
```

Build the server:

```bash
npm run build
```

Start the MCP server:

```bash
npm run start
```

## 📄 License

MIT@[AntV](https://github.com/antvis).

**Official site: ** [https://github.com/antvis/mcp-server-chart](https://github.com/antvis/mcp-server-chart)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `developer tools`, `antv`, `visualization`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @antv/mcp-server-chart`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/antvis-chart.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
