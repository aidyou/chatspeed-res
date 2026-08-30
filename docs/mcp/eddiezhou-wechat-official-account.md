---
title: "微信公众号创作助手（MCP&Agent挑战赛）"
description: "--- name: 微信公众号内容创作助手 version: 1.0 description: 基于多模态AI的微信公众号内容自动化生成与发布辅助工具 author: AI Assistant --- 微信公众号内容自动化助手 一个基于Python和MCP（Model Control Plane）服务的微信公众号内容自动化生成工具，实现从素材生成到草稿创建的完整流程自动化。 使用说明视频（参照） B站：https://www.bilibili.com/video/BV1iEhzzaEKr/ 抖音：https://w"
---

# 微信公众号创作助手（MCP&Agent挑战赛）

--- name: 微信公众号内容创作助手 version: 1.0 description: 基于多模态AI的微信公众号内容自动化生成与发布辅助工具 author: AI Assistant --- 微信公众号内容自动化助手 一个基于Python和MCP（Model Control Plane）服务的微信公众号内容自动化生成工具，实现从素材生成到草稿创建的完整流程自动化。 使用说明视频（参照） B站：https://www.bilibili.com/video/BV1iEhzzaEKr/ 抖音：https://w

---
name: 微信公众号内容创作助手
version: 1.0
description: 基于多模态AI的微信公众号内容自动化生成与发布辅助工具
author: AI Assistant
---

# 微信公众号内容自动化助手

一个基于Python和MCP（Model Control Plane）服务的微信公众号内容自动化生成工具，实现从素材生成到草稿创建的完整流程自动化。

# 使用说明视频（参照）
B站：https://www.bilibili.com/video/BV1iEhzzaEKr/  
抖音：https://www.douyin.com/user/self?modal_id=7544390677770112291

## 核心功能

- **Access Token获取**：自动获取微信公众号接口调用凭证
- **AI封面生成与上传**：利用多模态AI生成文章封面图片并自动上传至微信公众号永久素材库
- **AI文稿生成**：通过AI生成微信公众号文章内容
- **草稿自动创建**：将AI生成的封面和内容自动组装并提交至微信公众号草稿箱

## 公众号后台配置说明（重要）

**IP白名单配置（重要！！！）：**  
  【设置于开发】->【开发接口管理】->【基本配置】-> IP白名单  
   添加如下IP：47.92.200.108

**开发者ID获取（重要！！！）：**  
  【设置于开发】->【开发接口管理】->【基本配置】-> 开发者ID  

**开发者密码获取（重要！！！）：**  
  【设置于开发】->【开发接口管理】->【基本配置】-> 开发者密码

**系统提示词（重要！！！）：**  
  将上述拿到APP_ID和APP_SECRET给到系统提示词。以下为例子，请替换成你自己的。  
    APP_ID=wxcef12345678901c1  
    APP_SECRET=d1234567890abcdefghijkl123456789

## 环境要求

- 微信公众号开发者账号
- MCP服务支持

## MCP服务说明

本工具通过MCP（Model Control Plane）服务实现AI能力的调用与管理，主要集成了以下AI能力：

- **多模态图像生成**：用于创建符合微信公众号要求的封面图片（比例2.35:1）
- **文本生成**：用于自动撰写微信公众号文章内容
- **内容优化**：对生成的文本内容进行格式调整，使其符合微信公众号发布要求

## 工作流程

### 1. Access Token获取

系统首先通过微信公众号的AppID和AppSecret调用微信官方接口获取Access Token，作为后续所有接口调用的基础凭证。

```python
# 获取微信公众号接口调用凭证
def get_wechat_access_token(appid, secret):
    url = "https://api.weixin.qq.com/cgi-bin/token"
    params = {
        "grant_type": "client_credential",
        "appid": appid,
        "secret": secret
    }
    # 发送请求并处理响应...
```

### 2. AI封面生成与上传

利用MCP服务集成的多模态AI生成符合要求的封面图片，并自动上传至微信公众号永久素材库，获取media_id用于后续草稿创建。

**生成与上传流程：**
1. 通过MCP服务调用多模态AI模型，根据文章主题生成封面图片
2. 将生成的图片调整为符合微信公众号要求的尺寸和比例（2.35:1）
3. 调用微信永久素材上传接口，上传调整后的图片
4. 解析返回结果，提取并保存media_id

```python
# 上传永久素材（图片）
def upload_wechat_permanent_media(access_token, media_file):
    url = f"https://api.weixin.qq.com/cgi-bin/material/add_material?access_token={access_token}&type=image"
    # 处理文件并上传...
```

### 3. AI文稿生成与草稿创建

通过MCP服务调用文本生成AI模型创建文章内容，并结合之前获取的media_id创建微信公众号草稿。

**文稿生成与草稿创建流程：**
1. 通过MCP服务调用文本生成AI模型，根据主题生成文章内容
2. 对生成的内容进行格式优化，确保符合微信公众号发布规范
3. 调用微信公众号草稿创建接口，使用生成的内容和封面素材ID创建草稿

```python
# 添加草稿至草稿箱
def add_wechat_draft(access_token, title, content, thumb_media_id):
    url = f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={access_token}"
    # 构建请求数据并发送...
```

## 注意事项

- 请确保您的微信公众号已开启开发者模式，并获取了正确的AppID和AppSecret
- Access Token有效期为2小时，过期后需重新获取
- 上传的素材将占用微信公众号的素材库配额，请合理管理素材
- 生成的内容和封面图片可能需要人工审核后再发布
- 请遵守微信公众号平台的内容规范和使用条款

## 配置说明

使用前请确保配置以下必要参数：

- 微信公众号AppID
- 微信公众号AppSecret
- MCP服务相关配置（如有需要）

## 常见问题

### Q: 为什么获取Access Token失败？
**A:** 请检查AppID和AppSecret是否正确，以及网络连接是否正常。

### Q: 上传素材时提示"invalid media_id"？
**A:** 确保使用的是有效的永久素材media_id，临时素材ID无法用于创建草稿。

### Q: 生成的内容质量不理想怎么办？
**A:** 可以尝试调整AI模型的提示词（prompt），提供更详细的主题描述。

## 技术栈

- Python
- MCP（Model Control Plane）服务
- 微信公众号API
- 多模态AI模型（图像生成）
- 文本生成AI模型

## License

Apache 2.0

**官方网站：** [https://modelscope.cn/studios/EddieZhou/Wechat_Official_Account](https://modelscope.cn/studios/EddieZhou/Wechat_Official_Account)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`communication`
- 标签：`communication`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`mcp-remote https://eddiezhou-wechat-official-account.ms.show/gradio_api/mcp/sse --transport sse-only`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/eddiezhou-wechat-official-account.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
