---
title: "Figma 资源访问器"
description: "允许您的AI编码代理直接访问Figma文件和原型。有关任何问题/改进建议，可以给我发私信：https://x.com/jasonzhou1993\n\n1. 访问所有Figma页面\n2. 访问所有Figma组件\n3. 访问Figma原型流程"
---

# Figma 资源访问器

允许您的AI编码代理直接访问Figma文件和原型。有关任何问题/改进建议，可以给我发私信：https://x.com/jasonzhou1993

1. 访问所有Figma页面
2. 访问所有Figma组件
3. 访问Figma原型流程

# Figma MCP Python

[![PyPI version](/mcp-assets/dec8b35f184274331a6b0bde60435e1d.svg)](https://badge.fury.io/py/figma-mcp)

允许您的AI编码代理直接访问Figma文件和原型。
如果您有任何问题或改进建议，可以私信我：[https://x.com/jasonzhou1993](https://x.com/jasonzhou1993)

  

## 使用pipx快速安装

```bash
pipx install figma-mcp
```

### 对于Cursor：

1. 在设置中，使用以下命令添加一个MCP服务器：
```shell
figma-mcp --figma-api-key=your_figma_key
```

2. 或者在项目中添加一个`.cursor/mcp.json`文件：

```json
{
  "mcpServers": {
    "figma-python": {
      "command": "figma-mcp",
      "args": [
        "--figma-api-key=your_figma_key"
      ]
    } 
  }
}
```

### 对于像Windsurf这样的其他IDE，使用MCP配置文件（例如`mcp_config.json`）：

```json
{
  "mcpServers": {
    "figma-python": {
      "command": "figma-mcp",
      "args": [
        "--figma-api-key=your_figma_key"
      ]
    } 
  }
}
```

## 安装uv并设置环境
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv
source .venv/bin/activate
uv sync
```

## 本地测试
```bash
python -m figma_mcp.main
```

**官方网站：** [https://github.com/JayZeeDesign/figma-mcp](https://github.com/JayZeeDesign/figma-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`art and culture`, `image and video processing`, `developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`figma-mcp`
- 参数：`--figma-api-key=your_figma_key`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/jayzeedesign-figma.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
