---
title: "OBS远程控制面板"
description: "一台通过OBS WebSocket协议提供远程控制OBS Studio工具的服务器，可以通过MCP客户端界面管理场景、源、流媒体和录制。"
---

# OBS远程控制面板

一台通过OBS WebSocket协议提供远程控制OBS Studio工具的服务器，可以通过MCP客户端界面管理场景、源、流媒体和录制。

# OBS MCP 服务器

一个用于OBS Studio的MCP服务器，提供通过OBS WebSocket协议控制OBS的工具。

## 功能

- 连接到OBS WebSocket服务器
- 通过MCP工具控制OBS
- 提供以下功能的工具：
  - 常规操作
  - 场景管理
  - 源控制
  - 场景项操作
  - 流媒体和录制
  - 转场效果

## 安装

```bash
npm install
npm run build
```

## 使用方法

1. 确保开启了WebSocket服务器的OBS Studio正在运行（工具 > WebSocket服务器设置）。记下WS的密码。
2. 如果需要的话，在环境变量中设置WebSocket密码：

```bash
export OBS_WEBSOCKET_PASSWORD="your_password_here"
```

3. 运行OBS MCP服务器以检查它是否能够构建并连接成功：

```bash
npm run build
npm run start
```

4. 使用MCP服务器设置配置你的Claude桌面：

```json
{
  "mcpServers": {
    "obs": {
      "command": "node",
      "args": [
        "/build/index.js"
      ],
      "env": {
        "OBS_WEBSOCKET_PASSWORD": "
"
      }
    }
  }
}
```

5. 使用Claude来控制你的OBS！

## 可用工具

该服务器按类别组织提供了如下工具：

- 通用工具：版本信息、统计信息、快捷键、工作室模式
- 场景工具：列出场景、切换场景、创建/删除场景
- 源工具：管理源、设置、音频级别、静音/取消静音
- 场景项工具：管理场景中的项（位置、可见性等）
- 流媒体工具：开始/停止流媒体、录制、虚拟摄像头
- 转场工具：设置转场、持续时间、触发转场

## 环境变量

- `OBS_WEBSOCKET_URL`：WebSocket URL（默认值: ws://localhost:4455）
- `OBS_WEBSOCKET_PASSWORD`：与OBS WebSocket认证所需的密码（如果需要）

## 要求

- Node.js 16+
- 启用了WebSocket服务器的OBS Studio 31+
- Claude桌面

## 许可证

详情请参见[LICENSE](https://github.com/royshil/obs-mcp/blob/HEAD/LICENSE)文件。

**官方网站：** [https://github.com/royshil/obs-mcp](https://github.com/royshil/obs-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`os automation`, `entertainment and media`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`<obs-mcp_root>/build/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/royshil-obs.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
