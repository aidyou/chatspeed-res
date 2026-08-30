---
title: "哔哩视频提取器"
description: "BiliBili MCP Processor 一个基于 Model Context Protocol (MCP) 的哔哩哔哩视频内容处理工具，可以加载、分析和导出B站视频的字幕和内容。 功能特性 - 🎥 视频内容加载: 使用LangChain加载器获取B站视频内容和字幕 - 🔍 内容搜索: 在视频内容中进行文本搜索，支持上下文显示 - 📝 智能摘要: 自动生成视频内容摘要 - 📤 多格式导出: 支持导出为TXT、JSON、SRT字幕格式 - 🔐 认证支持: 支持B站登录认证以获取完整内容 - 🌐 MCP协议: 完全"
---

# 哔哩视频提取器

BiliBili MCP Processor 一个基于 Model Context Protocol (MCP) 的哔哩哔哩视频内容处理工具，可以加载、分析和导出B站视频的字幕和内容。 功能特性 - 🎥 视频内容加载: 使用LangChain加载器获取B站视频内容和字幕 - 🔍 内容搜索: 在视频内容中进行文本搜索，支持上下文显示 - 📝 智能摘要: 自动生成视频内容摘要 - 📤 多格式导出: 支持导出为TXT、JSON、SRT字幕格式 - 🔐 认证支持: 支持B站登录认证以获取完整内容 - 🌐 MCP协议: 完全

# BiliBili MCP Processor  
  
一个基于 Model Context Protocol (MCP) 的哔哩哔哩视频内容处理工具，可以加载、分析和导出B站视频的字幕和内容。  
  
## 功能特性  
  
- 🎥 **视频内容加载**: 使用LangChain加载器获取B站视频内容和字幕  
- 🔍 **内容搜索**: 在视频内容中进行文本搜索，支持上下文显示  
- 📝 **智能摘要**: 自动生成视频内容摘要  
- 📤 **多格式导出**: 支持导出为TXT、JSON、SRT字幕格式  
- 🔐 **认证支持**: 支持B站登录认证以获取完整内容  
- 🌐 **MCP协议**: 完全兼容MCP协议，可与Claude Desktop等客户端集成  
  
## 安装依赖  
  
### 使用 uv (推荐)  
  
```
uv add "mcp[cli]"  
uv add langchain langchain-community bilibili-api-python
```
### 使用 pip
```bash
pip install -r requirements.txt
```
## 环境配置
为了获取完整的视频内容，需要配置B站认证信息（可选）：
```bash
export BILIBILI_SESSDATA="your_sessdata_value"  
export BILIBILI_BUVID3="your_buvid3_value"   
export BILIBILI_BILI_JCT="your_bili_jct_value"  
export BILIBILI_EXPORT_PATH="./export"  # 可选，默认为 ./export
```
这些值可以从浏览器登录B站后的Cookie中获取。

## 快速开始
### 安装到Claude Desktop：
```bash
mcp install BiliBiliProcessor.py --name "BiliBili Processor"
```
## 工具使用
### 1. load_bilibili_video
  加载哔哩哔哩视频内容到内存中。
  
  参数:
  
  video_url (str): B站视频URL
  use_auth (bool): 是否使用认证信息，默认为True
  返回: 包含视频ID、文档数量、内容长度等信息的字典
### 2. get_video_content
  获取已加载视频的内容。
  
  参数:
  
  video_id (str): 视频ID
  page_index (int, 可选): 页面索引，不指定则返回所有页面
  返回: 视频内容数据

### 3. search_in_video
  在视频内容中搜索指定文本。
  
  参数:
  
  video_id (str): 视频ID
  query (str): 搜索查询
  case_sensitive (bool): 是否区分大小写，默认为False
  返回: 搜索结果，包含匹配位置和上下文

### 4. extract_video_summary
  提取视频内容摘要。
  
  参数:
  
  video_id (str): 视频ID
  max_length (int): 摘要最大长度，默认500字符
  返回: 视频摘要和统计信息

### 5. export_video_content
  导出视频内容到文件。
  
  参数:
  
  video_id (str): 视频ID
  target_format (str): 目标格式 (txt/json/srt)，默认为txt
  output_path (str, 可选): 输出路径，不指定则自动生成
  返回: 导出结果信息

### 6. get_bilibili_auth_status
  检查哔哩哔哩认证状态。
  
  返回: 认证状态和配置说明

**官方网站：** [https://github.com/TaoPeiLing/BiliBiliMCP](https://github.com/TaoPeiLing/BiliBiliMCP)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`entertainment and media`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`run --with mcp[cli] --with langchain --with langchain-community --with bilibili-api-python mcp run /path/to/your/BiliBiliProcessor.py`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/taopl1990-bilibilimcp.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
