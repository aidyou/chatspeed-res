---
title: "地质搜索"
description: "使克劳德能够通过自然语言查询Macrostrat API的综合地质数据，包括地质单元、地层柱、矿物和时间尺度。"
---

# 地质搜索

使克劳德能够通过自然语言查询Macrostrat API的综合地质数据，包括地质单元、地层柱、矿物和时间尺度。

# macrostrat-mcp
用于 Macrostrat API 的 Claude MCP 服务器

[Smithery](https://smithery.ai/server/@blake365/macrostrat-mcp)

  

这是一个 Model Context Protocol (MCP) 服务器的实现，用于在 [Claude Desktop](https://claude.ai/download) 中提供对 [Macrostrat API](https://macrostrat.org/api) 的访问。

## 概述

这个 Model Context Protocol (MCP) 服务器使 AI 助手和应用程序能够：

- 查询由 Macrostrat API 提供的全面地质数据和信息
- 访问地质单元、地层柱、矿物、时间尺度等
- 分析地质数据以提高地质理解
- 从数据中创建图形并进行数据分析

用户可以使用自然语言运行查询。

## 示例输出

**Q. 纳什维尔（田纳西州）的地质历史是什么？**

A.
让我检查一下纳什维尔所在位置的地质数据。

从 macrostrat（本地）查看 find-units 的结果
```json
{
  "lat": 36.1627,
  "lng": -86.7816,
  "responseType": "long"
}
```

### 纳什维尔（田纳西州）的地质历史
1. 中元古代基底（16-11亿年前）
- 火成岩基底岩石（花岗岩和流纹岩）
- 古老北美克拉通的一部分

2. 早-中寒武纪（5.18-5.04亿年前）
- 罗马组：混合碳酸盐-硅质碎屑沉积物
- 浅海环境
- 发展中的大陆架的一部分

3. 中-晚寒武纪（5.04-4.98亿年前）
- 康萨加组：石灰岩和混合沉积物
- 继续海洋沉积
- 交替出现的石灰岩和页岩表明海平面波动

4. 晚寒武纪-早奥陶纪（4.98-4.70亿年前）
- 诺克斯白云岩：巨大的白云岩序列
- 广泛的浅海平台
- 厚度可达1200米
- 代表了长期稳定的海洋条件

5. 中-晚奥陶纪（4.70-4.43亿年前）
几个重要的地层：
- 斯通河组（包括墨菲斯伯勒、皮尔斯、黎巴嫩石灰岩）
- 纳什维尔组（包括赫米塔奇、比格比-坎农、卡瑟斯地层）
- 主要是石灰岩沉积
- 富含化石
- 浅海环境
- 多次海平面变化周期

6. 早-中志留纪（4.43-4.23亿年前）
- 从布拉斯菲尔德到迪凯特组
- 继续海洋石灰岩沉积
- 从浅水到深水的各种海洋环境

7. 中泥盆纪-早密西西比纪（3.90-3.57亿年前）
- 佩格拉姆组到查塔努加页岩
- 转向更多的碎屑（页岩）沉积
- 查塔努加页岩代表了更深、缺氧的条件

8. 早-晚密西西比纪（3.57-3.31亿年前）
几个石灰岩地层：
- 福特佩恩组
- 华沙石灰岩
- 圣路易斯石灰岩
- 蒙特格尔石灰岩
- 哈特斯尔组
- 回归碳酸盐台地条件
- 多样的海洋环境

9. 新生代至今

- 长期的侵蚀和暴露
- 当前地貌的发展
- 纳什维尔穹顶结构的形成
- 河流和溪流沉积

### 主要特征
- 该地区在其大部分地质历史中主要是一个海洋环境
- 以石灰岩构造为主，表明温暖浅海的存在
- 多次海平面变化周期
- 丰富的化石记录，尤其是在奥陶纪岩石中
- 纳什维尔穹顶构造特征的一部分
- 长期的侵蚀作用移除了较年轻的岩石
- 当前地形由各种石灰岩单位的不同侵蚀程度塑造而成

### 当今基岩
纳什维尔今天的基岩主要由暴露在地表的奥陶纪石灰岩构成，尤其是斯通河组和纳什维尔组石灰岩。这些岩石在许多地方都有很好的暴露，并影响了当地喀斯特地形的发展，包括该地区常见的洞穴和天坑。

## 安装

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@blake365/macrostrat-mcp) 自动安装适用于 Claude Desktop 的 Macrostrat API 服务器：

```bash
npx -y @smithery/cli install @blake365/macrostrat-mcp --client claude
```

### 额外步骤

如果您想对服务器进行修改，可以通过编辑 `src/index.ts` 文件来实现。
- 运行 `npm install` 来安装依赖项
- 运行 `npm run build` 来构建服务器
- 在进行更改后退出并重新启动 Claude Desktop

## 与 Claude Desktop 连接

1. 打开您的 Claude Desktop 配置文件：
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`

2. 添加服务器配置：
```json
{
    "mcpServers": {
        "macrostrat": {
            "command": "node",
            "args": [
                "/Full/Route/to/Folder/macrostrat/build/index.js"
            ]
        }
    }
}
```

3. 关闭/退出然后重新启动 Claude Desktop

重新启动后，您应该会在文本框右下角看到一个小锤子图标。将鼠标悬停在图标上时，您会看到可用的 MCP 工具数量。

## 故障排除

如果在运行服务器时遇到错误，可能需要提供 `node` 命令的完整路径。例如，在 macOS 上：`/usr/local/bin/node`

**官方网站：** [https://github.com/blake365/macrostrat-mcp](https://github.com/blake365/macrostrat-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`research and data`, `search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`/Full/Route/to/Folder/macrostrat/build/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/blake365-macrostrat.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
