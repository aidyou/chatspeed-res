---
title: "免费文字生成图像或视频MCP工具"
description: "一个用于图像和视频生成的MCP（模型上下文协议）服务器，支持BigModel AI平台上的CogView和CogVideoX模型。它提供了图像和视频生成、配置管理、异步处理、错误处理、TypeScript支持和调试工具等功能。"
---

# 免费文字生成图像或视频MCP工具

一个用于图像和视频生成的MCP（模型上下文协议）服务器，支持BigModel AI平台上的CogView和CogVideoX模型。它提供了图像和视频生成、配置管理、异步处理、错误处理、TypeScript支持和调试工具等功能。

# MCP Image Video Generation Server

一个免费生成图像和视频的 MCP (Model Context Protocol) 服务器，支持 BigModel AI 平台的 CogView 和 CogVideoX 模型。

## 功能

- 🎨 **图像生成**: 使用 CogView 模型（cogview-4, cogview-4-250304, cogview-3-flash）生成高质量图像，默认使用 cogview-3-flash 免费模型
- 🎬 **视频生成**: 使用 CogVideoX 模型（cogvideox-3, cogvideox-2, cogvideox-flash）生成视频，默认使用 cogvideox-flash 模型
- ⚙️ **配置管理**: 支持环境变量配置和动态设置更新
- 🔄 **异步处理**: 支持视频生成任务状态查询和自动等待完成
- 🛡️ **错误处理**: 内置重试机制和详细错误信息
- 📝 **TypeScript**: 完整的类型安全支持
- 🔧 **调试支持**: 内置 MCP Inspector 和 VS Code 调试配置
- 🎯 **无水印**: 默认生成无水印内容（可以在 bigmodel.cn 安全管理中去掉水印）

## API Key 申请

在使用本服务器之前，您需要在 BigModel.cn 平台申请 API Key。模型用免费的模型

### 申请步骤

1. **访问 BigModel 开放平台**

   - 打开浏览器访问：[https://www.bigmodel.cn/claude-code?ic=QHPPFCALMK](https://bigmodel.cn/)
   - 点击右上角"登录"或"注册"

2. **注册/登录账号**

   - 使用手机号或邮箱注册账号
   - 完成实名认证（根据平台要求）
   - 登录到开发者控制台

3. **获取 API Key**
   - 点击右上角头像，找到 API Key 后点击进入
   - 添加新的 API Key（注意保密）

### 费用说明

- **免费额度**: 新用户通常会获得一定的免费调用额度
- **计费方式**: 按实际调用次数和资源使用量计费
- **余额查询**: 在控制台可以查看余额和使用情况
- **充值方式**: 支持多种在线充值方式

### 模型定价

| 模型类型 | 模型名称        | 费用类型    | 推荐场景             |
| -------- | --------------- | ----------- | -------------------- |
| 图像生成 | cogview-3-flash | 免费/低成本 | 快速原型、日常使用   |
| 图像生成 | cogview-4       | 付费        | 高质量图像、专业用途 |
| 视频生成 | cogvideox-flash | 免费        | 快速视频生成         |
| 视频生成 | cogvideox-3     | 付费        | 标准质量视频         |

> 💡 **建议**: 开发和测试阶段建议使用免费模型（cogview-3-flash），生产环境根据需求选择付费模型。

### API Key 使用注意事项

- 🔒 **保密**: API Key 相当于密码，请勿在代码仓库中公开
- ✅ **权限**: 确保 API Key 有权限访问所需的模型服务
- 🔄 **轮换**: 定期更换 API Key 以提高安全性
- 📊 **监控**: 定期检查 API 使用量和费用情况

## 使用方法

### MCP 配置

在你的 MCP 客户端配置中添加：

```json
{
  "mcpServers": {
    "image-video-generation": {
      "command": "npx",
      "args": ["-y", "image-video-generation-mcp@latest"],
      "env": {
        "IMAGE_VIDEO_GENERATION_API_KEY": "your_api_key"
      },
      "type": "stdio"
    }
  }
}
```

## 默认模型

- **图像生成**: `cogview-3-flash` (免费模型，快速生成)
- **视频生成**: `cogvideox-flash` (快速视频生成)

### 环境变量说明

| 环境变量                                     | 必需 | 默认值            | 说明             |
| -------------------------------------------- | ---- | ----------------- | ---------------- |
| `IMAGE_VIDEO_GENERATION_API_KEY`             | ✅   | -                 | API 密钥         |
| `IMAGE_VIDEO_GENERATION_DEFAULT_IMAGE_MODEL` | ❌   | `cogview-3-flash` | 默认图像生成模型 |
| `IMAGE_VIDEO_GENERATION_DEFAULT_VIDEO_MODEL` | ❌   | `cogvideox-flash` | 默认视频生成模型 |

### 支持的工具

#### 1. generate_image

生成图像，支持以下参数：

- `prompt` (必需): 图像描述文本
- `model`: 模型选择 (`cogview-4`, `cogview-4-250304`, `cogview-3-flash`)
- `quality`: 图像质量 (`standard`, `hd`)
- `size`: 图像尺寸 (例如 `1024x1024`)
- `watermark_enabled`: 是否添加水印
- `user_id`: 用户追踪 ID

#### 2. generate_video

生成视频，支持以下参数：

- `prompt` (必需): 视频描述文本 (最大 512 字符)
- `model`: 模型选择 (`cogvideox-3`, `cogvideox-2`, `cogvideox-flash`)
- `quality`: 输出质量模式 (`speed`, `quality`)
- `size`: 视频分辨率 (例如 `1920x1080`)
- `fps`: 帧率 (30, 60)
- `duration`: 视频时长 (5, 10 秒)
- `with_audio`: 是否启用 AI 生成音频
- `watermark_enabled`: 是否控制水印

#### 3. query_video_result

查询异步视频生成任务结果：

- `task_id` (必需): 视频生成任务返回的 ID

#### 4. wait_for_video

等待视频生成完成并返回结果：

- `task_id` (必需): 任务 ID
- `max_wait_time`: 最大等待时间 (默认 300000 毫秒)
- `poll_interval`: 轮询间隔 (默认 5000 毫秒)

#### 5. configure_models

配置默认模型和设置：

- `default_image_model`: 默认图像生成模型
- `default_video_model`: 默认视频生成模型
- `timeout`: 请求超时时间
- `max_retries`: 最大重试次数

## 故障排除

### MCP 连接问题

如果遇到 MCP 连接不上的问题，请检查以下几点：

1. **API Key 配置**：确保已正确设置 `IMAGE_VIDEO_GENERATION_API_KEY` 环境变量

2. **网络连接**：确保能访问 `https://open.bigmodel.cn/api`

3. **版本问题**：使用最新版本
```bash
   # 清除 npm 缓存并使用最新版本
   npm cache clean --force
   npx -y image-video-generation-mcp@latest
```

4. **配置文件格式**：确保 MCP 配置文件格式正确
```json
   {
     "mcpServers": {
       "image-video-generation": {
         "command": "npx",
         "args": ["-y", "image-video-generation-mcp@latest"],
         "env": {
           "IMAGE_VIDEO_GENERATION_API_KEY": "your_bigmodel_api_key"
         },
         "type": "stdio"
       }
     }
   }
```

### 常见错误

- **"API Key is required"**：需要设置 `IMAGE_VIDEO_GENERATION_API_KEY` 环境变量
- **"command not found"**：npm 缓存问题，尝试清除缓存或等待几分钟
- **连接超时**：检查网络连接和防火墙设置

## 支持

如有问题，请提交 [GitHub Issues](https://github.com/156554395/image-video-generation-mcp/issues)。

## 相关链接

- [BigModel API 文档](https://docs.bigmodel.cn/)
- [MCP 协议](https://modelcontextprotocol.io/)

**官方网站：** [https://github.com/156554395/image-video-generation-mcp](https://github.com/156554395/image-video-generation-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`entertainment and media`, `developer tools`, `文生图`, `文生视频`, `图片和视频`, `生成图片`, `生成视频`, `视频生成`, `图片生成`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y image-video-generation-mcp@latest`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/seostar-image-video-generation.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
