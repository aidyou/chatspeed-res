---
title: "QuickChart MCP 服务器"
description: "一个用于生成可自定义数据可视化的MCP服务器，使用QuickChart.io，支持多种图表类型和Chart.js配置。"
---

# QuickChart MCP 服务器

一个用于生成可自定义数据可视化的MCP服务器，使用QuickChart.io，支持多种图表类型和Chart.js配置。

# quickchart-server MCP 服务器

![image](/mcp-assets/a495ea4a6dfe48b593c9635600caa82a.png)

  

>
 ![](/mcp-assets/c1486b4e2d8cfd67ed0257afeefda188.svg 'MCP 服务器')

这是一个使用 QuickChart.io 生成图表的 Model Context Protocol 服务器。

这是一个基于 TypeScript 的 MCP 服务器，提供了图表生成功能。它允许您通过 MCP 工具创建各种类型的图表。

## 概述

该服务器集成了 QuickChart.io 基于 URL 的图表生成功能，使用 Chart.js 配置来创建图表图像。用户可以通过提供数据和样式参数来生成各种类型的图表，服务器会将这些参数转换为图表 URL 或可下载的图像。

## 功能

### 工具
- `generate_chart` - 使用 QuickChart.io 生成图表 URL
  - 支持多种图表类型：条形图、折线图、饼图、环形图、雷达图、极区图、散点图、气泡图、径向仪表盘、速度计
  - 可自定义标签、数据集、颜色和其他选项
  - 返回生成的图表 URL

- `download_chart` - 将图表图像下载到本地文件
  - 参数包括图表配置和输出路径
  - 将图表图像保存到指定位置
![image](/mcp-assets/86b981a650a9c915c04fdfa0a91bd674.png)

![image](/mcp-assets/8dc7ec4ba11f643eaffb375b92838cc1.png)

## 支持的图表类型
- 条形图：用于比较不同类别的值
- 折线图：用于显示随时间变化的趋势
- 饼图：用于显示比例数据
- 环形图：类似于饼图，但中心为空
- 雷达图：用于显示多变量数据
- 极区图：用于显示具有固定角度段的比例数据
- 散点图：用于显示数据点分布
- 气泡图：用于三维数据可视化
- 径向仪表盘：用于显示范围内的单个值
- 速度计：用于速度计样式的值显示

## 使用方法

### 图表配置
服务器使用 Chart.js 配置格式。以下是一个基本示例：

```javascript
{
  "type": "bar",
  "data": {
    "labels": ["January", "February", "March"],
    "datasets": [{
      "label": "Sales",
      "data": [65, 59, 80],
      "backgroundColor": "rgb(75, 192, 192)"
    }]
  },
  "options": {
    "title": {
      "display": true,
      "text": "Monthly Sales"
    }
  }
}
```

### URL 生成
服务器将您的配置转换为 QuickChart URL：
```
https://quickchart.io/chart?c={...encoded configuration...}
```

## 开发

安装依赖项：
```bash
npm install
```

构建服务器：
```bash
npm run build
```

## 安装

### 安装

```bash
 npm install @gongrzhe/quickchart-mcp-server
```

### 通过 Smithery 安装
 
 通过 [Smithery](https://smithery.ai/server/@GongRzhe/Quickchart-MCP-Server) 自动安装适用于 Claude Desktop 的 QuickChart 服务器：
 
```bash
 npx -y @smithery/cli install @gongrzhe/quickchart-mcp-server --client claude
```

要与 Claude Desktop 一起使用，请添加服务器配置：

在 MacOS 上：`~/Library/Application Support/Claude/claude_desktop_config.json`
在 Windows 上：`%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "quickchart-server": {
      "command": "node",
      "args": ["/path/to/quickchart-server/build/index.js"]
    }
  }
}
```

或

```json
{
  "mcpServers": {
    "quickchart-server": {
      "command": "npx",
      "args": [
        "-y",
        "@gongrzhe/quickchart-mcp-server"
      ]
    }
  }
}
```

## 文档参考
- [QuickChart 文档](https://quickchart.io/documentation/)
- [图表类型参考](https://quickchart.io/documentation/chart-types/)

## 📜 许可证

本项目采用 MIT 许可证。

**官方网站：** [https://github.com/GongRzhe/Quickchart-MCP-Server](https://github.com/GongRzhe/Quickchart-MCP-Server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @gongrzhe/quickchart-mcp-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/gongrzhe-quickchart.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
