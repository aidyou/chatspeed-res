---
title: "微信公众号API-MCP-Server"
description: "# 微信公众号 MCP 服务简介\n\n## 服务概述\n\n微信公众号MCP（模型控制协议）服务是一个专为通过AI自动化简化微信公众号管理而设计的专业工具。该服务为在微信公众号上创建、发布和管理内容提供了标准化接口，消除了常规发布任务中的手动干预需求。\n\n## 核心功能\n\n- **访问令牌管理**：安全处理认证凭证\n- **内容创建**：支持文本、图片和HTML格式的富媒体内容草稿的程序化创建\n- **发布自动化**：定时或按需将内容发布到微信公众号\n- **资源管理**：高效处理媒体资源和草稿内容\n- **MCP兼容性**：通过模型控制协议标准与AI代理和LLM系统无缝集成\n\n## 技术实现\n\n基于FastMCP框架构建，该服务暴露了一组可由AI系统调用的标准化工具，用于在微信公众号上执行操作。服务处理与微信API的所有通信，透明地管理认证、速率限制和错误处理。\n\n## 使用场景\n\n- 从AI生成内容自动发布内容\n- 定时发布定期更新或通讯\n- 与内容管理系统集成，实现跨平台发布\n- 使AI助手能够管理社交媒体存在\n\n## 集成方式\n\n该服务可以与任何支持MCP协议的系统集成，包括Cursor、ModelScope和自定义MCP客户端。它可以在本地部署或在服务器上部署以进行集中访问。"
---

# 微信公众号API-MCP-Server

# 微信公众号 MCP 服务简介

## 服务概述

微信公众号MCP（模型控制协议）服务是一个专为通过AI自动化简化微信公众号管理而设计的专业工具。该服务为在微信公众号上创建、发布和管理内容提供了标准化接口，消除了常规发布任务中的手动干预需求。

## 核心功能

- **访问令牌管理**：安全处理认证凭证
- **内容创建**：支持文本、图片和HTML格式的富媒体内容草稿的程序化创建
- **发布自动化**：定时或按需将内容发布到微信公众号
- **资源管理**：高效处理媒体资源和草稿内容
- **MCP兼容性**：通过模型控制协议标准与AI代理和LLM系统无缝集成

## 技术实现

基于FastMCP框架构建，该服务暴露了一组可由AI系统调用的标准化工具，用于在微信公众号上执行操作。服务处理与微信API的所有通信，透明地管理认证、速率限制和错误处理。

## 使用场景

- 从AI生成内容自动发布内容
- 定时发布定期更新或通讯
- 与内容管理系统集成，实现跨平台发布
- 使AI助手能够管理社交媒体存在

## 集成方式

该服务可以与任何支持MCP协议的系统集成，包括Cursor、ModelScope和自定义MCP客户端。它可以在本地部署或在服务器上部署以进行集中访问。

# 微信公众号 MCP 服务器

这是一个基于 FastMCP 框架的微信公众号MCP服务器，提供了一系列实用的微信公众号 API 接口封装，包括草稿创建、发布、删除等功能。

## 项目简介

本项目使用 Python 和 FastMCP 框架，通过 Model Control Protocol (MCP) 规范提供微信公众号管理 API，可以轻松集成到各种 AI 系统和自动化工作流程中，帮助用户便捷地管理微信公众号内容。

## 微信公众平台

微信公众平台官方网址：[https://mp.weixin.qq.com](https://mp.weixin.qq.com)

您需要先在微信公众平台注册并创建公众号，获取开发者ID(AppID)和密钥(AppSecret)才能使用本工具。

## 安装方法

### 使用 pip 安装

```bash
pip install wechat_oa_mcp
```

## 项目结构

```
./
├── README.md              # 项目文档
├── examples/              # 使用示例
│   └── simple_usage.py    # 简单使用示例
├── setup.py               # 安装配置
├── pyproject.toml         # Python项目配置
└── wechat_oa_mcp/         # 包主目录
    ├── __init__.py        # 包初始化文件
    ├── __main__.py        # 模块直接执行入口
    ├── cli.py             # 命令行工具入口
    └── server.py          # 主要功能代码
```

## 依赖项

- Python 3.10+
- fastmcp
- requests

## 功能列表

本服务器提供以下功能:

- **获取微信 Access Token**: 获取接口调用凭证
- **创建微信公众号草稿**: 创建图文消息草稿
- **发布微信公众号草稿**: 将草稿发布到公众号
- **删除微信公众号草稿**: 删除未发布的草稿
- **删除永久素材**: 删除公众号中的永久素材

## API 接口说明

### 1. 获取 Access Token

```python
WeChat_get_access_token
```

**输入参数:**
```json
AppID: String·第三方用户唯一凭证(公众号-设置与开发-开发接口管理中获取)
AppSecret: String·第三方用户唯一凭证密钥(公众号-设置与开发-开发接口管理中获取)
```

**输出:**
```json
{
  "success": true,
  "error": null,
  "access_token": "获取到的access_token",
  "expires_in": 7200
}
```

### 2. 创建草稿

```python
WeChat_create_draft
```

**输入参数:**
```json
access_token: String·你的access_token，调用接口凭证，可通过WeChat_get_access_token获取
image_url: String·封面图片URL
title: String·文章标题
content: String·图文消息的具体内容，支持HTML标签，必须少于2万字符，小于1M
author: String·(可选)作者名称
digest: String·(可选)图文消息的摘要，仅有单图文消息才有摘要，多图文此处为空。如果本字段为没有填写，则默认抓取正文前54个字。
content_source_url: String·(可选)图文消息的原文地址，即点击"阅读原文"后的URL
need_open_comment: Integer·(可选)Uint32 是否打开评论，0不打开(默认)，1打开
```

**输出:**
```json
{
  "success": true,
  "error": null,
  "draft_media_id": "草稿的media_id",
  "image_media_id": "封面图片的media_id"
}
```

### 3. 发布草稿

```python
WeChat_publish_draft
```

**输入参数:**
```json
access_token: String·调用接口凭证，可通过WeChat_get_access_token获取
draft_media_id: String·在之前调用WeChat_create_draft之后返回的draft_media_id
```

**输出:**
```json
{
  "success": true,
  "error": null,
  "errmsg": "ok",
  "publish_id": "发布任务id"
}
```

### 4. 删除草稿

```python
WeChat_del_draft
```

**输入参数:**
```json
access_token: String·调用接口凭证，可通过WeChat_get_access_token获取
media_id: String·草稿对应凭证，也就是WeChat_create_draft返回的draft_media_id
```

**输出:**
```json
{
  "success": true,
  "error": null,
  "errcode": 0,
  "errmsg": "ok"
}
```

### 5. 删除永久素材

```python
WeChat_del_material
```

**输入参数:**
```json
access_token: String·调用接口凭证，可通过WeChat_get_access_token获取
media_id: String·永久素材对应凭证，也就是WeChat_create_draft返回的image_media_id
```

**输出:**
```json
{
  "success": true,
  "error": null,
  "errcode": 0,
  "errmsg": "ok"
}
```

## 使用方法

### 1. 安装服务器

```bash
# 通过pip安装
pip install wechat_oa_mcp
```

### 2. 调用MCP Server的几种方式

#### 2.1 通过代码调用

您可以通过以下方式在Python代码中直接调用微信MCP API（只需完成安装步骤即可使用）：

```python
from wechat_oa_mcp import (
    WeChat_get_access_token,
    WeChat_create_draft,
    WeChat_publish_draft,
    WeChat_del_draft,
    WeChat_del_material
)

# 获取access_token
token_result = WeChat_get_access_token({
    "AppID": "您的微信AppID",
    "AppSecret": "您的微信AppSecret"
})

if token_result["success"]:
    access_token = token_result["access_token"]

    # 创建草稿
    draft_result = WeChat_create_draft({
        "access_token": access_token,
        "image_url": "https://example.com/image.jpg",
        "title": "测试文章标题",
        "content": "
这是文章内容
",
        "author": "作者名称"
    })

    if draft_result["success"]:
        draft_id = draft_result["draft_media_id"]
        image_id = draft_result["image_media_id"]

        # 发布草稿
        publish_result = WeChat_publish_draft({
            "access_token": access_token,
            "draft_media_id": draft_id
        })

        if publish_result["success"]:
            print(f"发布成功！发布ID: {publish_result['publish_id']}")

        # 删除草稿示例
        # 注意：通常在发布后才会删除草稿，这里仅为演示API用法
        del_draft_result = WeChat_del_draft({
            "access_token": access_token,
            "media_id": draft_id
        })

        if del_draft_result["success"]:
            print(f"删除草稿成功：{del_draft_result['errmsg']}")

        # 删除素材示例
        # 注意：通常在不需要图片素材时才会删除，这里仅为演示API用法
        del_material_result = WeChat_del_material({
            "access_token": access_token,
            "media_id": image_id
        })

        if del_material_result["success"]:
            print(f"删除素材成功：{del_material_result['errmsg']}")
```

#### 2.2 通过MCP Inspector进行调试

只需完成安装步骤后，即可使用以下命令进行交互测试：

```bash
npx @modelcontextprotocol/inspector python -m wechat_oa_mcp
```

之后访问 http://localhost:6274 可进行交互测试

#### 2.3 通过json添加mcp server

**注意：此方式需要先启动MCP服务器**

1. 首先通过命令行启动服务：

```bash
# 直接启动（默认端口8000）
wechat-oa-mcp
# 或者
python -m wechat_oa_mcp

# 指定端口启动
wechat-oa-mcp --port 8123
# 或者
python -m wechat_oa_mcp --port 8123
```

2. 然后将微信MCP服务器添加到其他MCP兼容应用（如Cursor）的配置中：

```json
{
    "mcpServers": {
        "wechat_oa_mcp": {
            "type": "sse",
            "url": "http://localhost:8000/sse"
        }
    }
}
```

**配置参数说明：**
- `type`: 通信协议类型，支持"sse"(Server-Sent Events)
- `url`: 服务器地址，默认端口为8000。如果之前指定了port，则以指定端口号为准
- `wechat_oa_mcp`: 服务器名称，可自定义

## 技术架构

本项目基于 FastMCP 框架，通过 MCP 协议提供微信公众号相关服务。服务器采用模块化设计，每个功能都封装为独立的 MCP 工具，可以单独调用。

服务器内部通过 HTTP 请求与微信公众号 API 通信，处理认证、参数校验等细节，让使用者可以专注于业务逻辑而不用关心底层实现。

## 使用限制

为了分散服务器压力，每个IP每分钟内最多能调用同一接口五次。

## IP白名单配置

根据微信公众号开发接口管理规定，通过开发者ID及密码调用获取access_token接口时，需要设置访问来源IP为白名单。请将以下IP添加至微信公众号-设置与开发-开发接口管理-IP白名单：

```
106.15.125.133
```

## 致谢

- 感谢 FastMCP 项目提供的框架支持

**免责声明：此 MCP 服务器仅限研究用途，禁止用于商业目的。**

**官方网站：** [https://www.modelscope.cn/mcp](https://www.modelscope.cn/mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`python`
- 参数：`--directory /Users/project/mcp/wechat/wechat_oa_mcp -m wechat_oa_mcp --port 8123`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/jupiterc-wechat-oa.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
