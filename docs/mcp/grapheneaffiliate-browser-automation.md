---
title: "浏览器自动化-MCP"
description: "启用人工智能代理通过标准化接口控制网络浏览器，进行诸如启动、交互和关闭浏览器等操作。"
---

# 浏览器自动化-MCP

启用人工智能代理通过标准化接口控制网络浏览器，进行诸如启动、交互和关闭浏览器等操作。

# 浏览器自动化 MCP 服务器

这是一个为 Roo Code 提供浏览器自动化功能的模型上下文协议 (MCP) 服务器。它使 AI 代理能够通过标准化接口控制网页浏览器。

## 功能

- 浏览器控制（启动、关闭）
- 鼠标交互（在指定坐标点击）
- 键盘输入（键入文本）
- 页面导航（向上/向下滚动）
- 固定视口大小（900x600）

## 安装

1. 克隆仓库：
```bash
git clone https://github.com/grapheneaffiliates/browser-automation-mcp.git
cd browser-automation-mcp
```

2. 安装依赖项：
```bash
npm install
```

3. 构建项目：
```bash
npm run build
```

## 配置

在您的 Cline MCP 设置文件中添加以下内容：

```json
{
  "mcpServers": {
    "browser": {
      "command": "node",
      "args": ["path/to/browser-server/build/index.js"],
      "disabled": false,
      "alwaysAllow": []
    }
  }
}
```

## 可用工具

该服务器提供以下 MCP 工具：

- `launch_browser`: 在指定 URL 启动一个新的浏览器实例
- `click`: 在页面上的特定 x,y 坐标处点击
- `type`: 在页面上键入文本
- `scroll`: 向上或向下滚动页面
- `close_browser`: 关闭浏览器实例

## 使用示例

```typescript
// Using the MCP tools in Roo Code
const result = await use_mcp_tool({
  server_name: "browser",
  tool_name: "launch_browser",
  arguments: {
    url: "https://example.com"
  }
});
```

## 许可证

MIT

**官方网站：** [https://github.com/grapheneaffiliate/browser-automation-mcp](https://github.com/grapheneaffiliate/browser-automation-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`browser`
- 标签：`browser automation`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`path/to/browser-server/build/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/grapheneaffiliate-browser-automation.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
