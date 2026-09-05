---
title: "地球数据MCP服务器"
description: "一个模型上下文协议服务器，可实现高效发现和检索NASA地球数据以进行地理空间分析。"
---

# 地球数据MCP服务器

一个模型上下文协议服务器，可实现高效发现和检索NASA地球数据以进行地理空间分析。

[![Datalayer](/mcp-assets/ebffabe66603ffc5befd3fb0a80b406d.svg)](https://datalayer.io)

[![成为赞助者](/mcp-assets/ac64e82bf123c4e77c9539d7abadcb39.svg)](https://github.com/sponsors/datalayer)

# 🪐 ✨ Earthdata MCP 服务器

[Actions](https://github.com/datalayer/earthdata-mcp-server/actions/workflows/build.yml)
[![PyPI - 版本](/mcp-assets/072238d536766621834bd11be56da91f.svg)](https://pypi.org/project/earthdata-mcp-server)

Earthdata MCP 服务器是一个 [模型上下文协议](https://modelcontextprotocol.io/introduction) (MCP) 服务器实现，它提供了与 [NASA 地球数据](https://www.earthdata.nasa.gov/) 交互的工具。它使地理空间分析中的数据集发现和检索更加高效。

以下演示使用此 MCP 服务器在 NASA Earthdata 上搜索数据集和数据颗粒，并使用 [jupyter-earth-mcp-server](https://github.com/datalayer/jupyter-earth-mcp-server) 在 Jupyter 中下载数据，以及使用 [jupyter-mcp-server](https://github.com/datalayer/jupyter-mcp-server) 进行进一步分析。

  

    
使用 AI 驱动的地理空间工具和 Jupyter 分析海平面上升 - 观看视频

  

  

    

  

## 与 Claude Desktop 一起使用

要与 Claude Desktop 一起使用，请将以下内容添加到您的 `claude_desktop_config.json` 文件中。

```json
{
  "mcpServers": {
    "earthdata": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "datalayer/earthdata-mcp-server:latest"
      ]
    }
  }
}
```

如果您使用的是 Linux，请使用以下命令启动 Claude。

```bash
make claude-linux
```

## 工具

该服务器提供 2 个工具。

### `search_earth_datasets`

- 在 NASA Earthdata 上搜索数据集。
- 输入：
  - search_keywords (str)：要在数据集标题中搜索的关键字。
  - count (int)：要返回的数据集数量。
  - temporal (tuple)：（可选）时间范围格式为 (date_from, date_to)。
  - bounding_box (tuple)：（可选）边界框格式为 (lower_left_lon, lower_left_lat, upper_right_lon, upper_right_lat)。
- 返回：数据集摘要列表。

### `search_earth_datagranules`

- 在 NASA Earthdata 上搜索数据颗粒。
- 输入：
  - short_name (str)：数据集的简称。
  - count (int)：要返回的数据颗粒数量。
  - temporal (tuple)：（可选）时间范围格式为 (date_from, date_to)。
  - bounding_box (tuple)：（可选）边界框格式为 (lower_left_lon, lower_left_lat, upper_right_lon, upper_right_lat)。
- 返回：数据颗粒列表。

## 提示

1. `sealevel_rise_dataset`
   - 搜索全球范围内与海平面上升相关的数据集。
   - 输入：
     - `start_year` (int)：起始年份。
      - `end_year` (int)：结束年份。
   - 返回：正确格式化的提示。

2. `ask_datasets_format`
    - 询问有关数据集格式的信息。
    - 返回：正确格式化的提示。

## 构建

```bash
# or run `docker build -t datalayer/earthdata-mcp-server .`
make build-docker
```

如果您愿意，您可以拉取预构建的镜像。

```bash
make pull-docker
```

**官方网站：** [https://github.com/datalayer/earthdata-mcp-server](https://github.com/datalayer/earthdata-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`research and data`, `location services`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`docker`
- 参数：`run -i --rm datalayer/earthdata-mcp-server:latest`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/datalayer-earthdata.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
