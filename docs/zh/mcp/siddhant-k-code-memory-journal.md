---
title: "Memory Journal MCP服务器（记忆日志MCP服务器）"
description: "这个MCP服务器通过位置、标签和人物帮助用户搜索和分析他们的照片库，提供照片分析和模糊匹配等功能，以增强照片管理。"
---

# Memory Journal MCP服务器（记忆日志MCP服务器）

这个MCP服务器通过位置、标签和人物帮助用户搜索和分析他们的照片库，提供照片分析和模糊匹配等功能，以增强照片管理。

# 📸 Smart Photo Journal MCP Server

**Smart Photo Journal** 是一个旨在帮助您使用强大且直观的工具来搜索和分析您的照片库的MCP服务器。无论您是在回忆家庭时刻还是与朋友寻找特定的照片，这个服务器都能满足您的需求！🎉

> **灵感来源：** [burningion/video-editing-mcp](https://github.com/burningion/video-editing-mcp)
> 特别感谢[@burningion](https://x.com/burningion)提出使用MCP进行创意媒体管理的创新想法！

## 🎯 功能

- **位置搜索：** 轻松找到特定地点的照片。🌍
- **标签搜索：** 通过关键词或标签如“生日”、“海滩”或“假期”搜索照片。🎉
- **人物搜索：** 快速定位包含特定人物的照片。👥
- **照片分析：** 发现有趣的见解，比如您拍照最频繁的时间和日期。🕰️
- **模糊匹配：** 不确定确切名称？没关系！该服务器支持模糊匹配以增加灵活性。🔍

## 🚀 开始使用

### 前提条件

1. 确保您有macOS并拥有一个照片库。
2. 安装[uv](https://docs.astral.sh/uv/)来管理依赖项并运行服务器。

### 安装

1. 克隆仓库：

```bash
   git clone https://github.com/Siddhant-K-code/memory-journal-mcp-server.git
   cd memory-journal-mcp-server
```

2. 使用`uv`安装依赖项：

```bash
   uv sync
```

3. 配置MCP服务器。更新您的`claude_desktop_config.json`文件如下配置：

```json
   {
     "mcpServers": {
       "smart-photo-journal": {
         "command": "/Users//.local/bin/uv",
         "args": [
           "--directory",
           "/Users/
/memory-journal-mcp-server",
           "run",
           "server.py"
         ]
       }
     }
   }
```

4. 用以下命令启动服务器或者直接打开Claude Desktop：
```bash
   uv run server.py
```

> **注意：** 将``和`
`替换为您实际的设备用户名和克隆目录路径。
> 您会收到一个弹出窗口，授权服务器访问您的照片。这些操作仅限于本地，除了Claude服务外不会与任何人共享数据。

### MCP服务器初始化

当服务器启动时，您将看到：

```
Starting Smart Photo Journal MCP server.
```

现在它已经准备好处理您的照片查询了！🎉

---

## 🛠️ 使用方法

### 可用工具

1. **位置搜索**

   - 描述：查找在特定位置拍摄的照片。
   - 输入示例：
```json
     {
       "location": "乌代布尔"
     }
```
   - 预期输出：
```
     找到 5 张来自乌代布尔的照片：
     📷 IMG_1234.jpg
     ...
```

2. **标签搜索**

   - 描述：通过标签或关键词搜索照片。
   - 输入示例：
```json
     {
       "label": "生日"
     }
```
   - 预期输出：
```
     标记为 '生日' 的照片 (找到 3 张)：
     📷 IMG_5678.jpg
     ...
```

3. **人物搜索**

   - 描述：查找包含特定人物的照片。
   - 输入示例：
```json
     {
       "person": "妈妈"
     }
```
   - 预期输出：
```
     包含妈妈的照片 (找到 10 张)：
     📷 IMG_9101.jpg
     ...
```

4. **照片分析**
   - 描述：分析你的照片库中的模式，例如拍照最常见的时间或日子。
   - 输入示例：
```json
     {}
```
   - 预期输出：
```
     📸 照片拍摄模式：
     总照片数：200
     ...
```

---

## 📚 示例用例

### 1. **家庭和朋友相册整理器**

想要将所有家庭时刻汇集在一起吗？使用 `people-search` 工具并输入诸如“爸爸”、“妈妈”或“任何朋友”的名字来查找包含特定人物的照片。

### 2. **度假亮点**

使用 `location-search` 工具搜索你度假目的地的照片。

### 3. **回忆往昔**

想看看过去的生日照片吗？使用 `label-search` 并输入“生日”，重温那些美好的时光！

### 4. **了解你的摄影习惯**

使用 `photo-analysis` 工具了解你大部分照片的拍摄时间和地点。据此计划你的下一次拍摄！

---

## ⚡ 获取最佳结果的小贴士

- 确保你的照片库已加载到 macOS 中。
- 尽可能具体地提供搜索查询以获得更准确的结果。
- 当你不确定确切的名字时，可以使用模糊匹配以增加灵活性。

**官方网站：** [https://github.com/Siddhant-K-code/memory-journal-mcp-server](https://github.com/Siddhant-K-code/memory-journal-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`image and video processing`, `location services`, `knowledge and memory`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`/Users/<YOUR_DEVICE_USERNAME>/.local/bin/uv`
- 参数：`--directory /Users/<PATH_TO_CLONED_DIR>/memory-journal-mcp-server run server.py`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/siddhant-k-code-memory-journal.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
