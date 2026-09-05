---
title: "魔搭文生图mcp服务"
description: "项目简介 现在文生图aigc火爆，创立如下mcp服务，可以使用指定模型生成图像，并保存到本地。当前只支持魔搭的四种模型，详情见后。 调用 generateimage 接口生成图片，并记录生成耗时。 成功时返回包含路径、宽度、高度、耗时的元组；失败时返回 None。 部署指南 环境依赖： ​​Node.js​​ 18+ 或 ​​Python​​ 3.8+（根据实际运行环境选择） 配置说明 参考以下…"
---

# 魔搭文生图mcp服务

项目简介 现在文生图aigc火爆，创立如下mcp服务，可以使用指定模型生成图像，并保存到本地。当前只支持魔搭的四种模型，详情见后。 调用 generateimage 接口生成图片，并记录生成耗时。 成功时返回包含路径、宽度、高度、耗时的元组；失败时返回 None。 部署指南 环境依赖： ​​Node.js​​ 18+ 或 ​​Python​​ 3.8+（根据实际运行环境选择） 配置说明 参考以下…

## 项目简介
    现在文生图aigc火爆，创立如下mcp服务，可以使用指定模型生成图像，并保存到本地。当前只支持魔搭的四种模型，详情见后。
    调用 generate_image 接口生成图片，并记录生成耗时。
    成功时返回包含路径、宽度、高度、耗时的元组；失败时返回 None。

## 部署指南

### 环境依赖：
​​Node.js​​ 18+ 或 ​​Python​​ 3.8+（根据实际运行环境选择）


### 配置说明
参考以下 JSON 配置格式（以 SSE 传输为例）：
```json
{
  "mcpServers": {
    "your-server-name": {
      "args": [
        "mcp-remote",
        "https://phoenixdna-t2i-modelscope-mcp.ms.show/gradio_api/mcp/sse",
        "--transport",
        "sse-only"
      ],
      "command": "npx"
    }
  }
}
```
## 使用示例
### 参数说明：
    Args:
        prompt (str): 图像生成提示词。
        model (str): 使用的模型名称，例如：
            - "black-forest-labs/FLUX.1-Krea-dev"
            - "Qwen/Qwen-Image"
            - "MusePublic/489_ckpt_FLUX_1"
            - "MusePublic/flux-high-res"
        width (int): 图像宽度（像素）。
        height (int): 图像高度（像素）。

    Returns:
        Optional[Tuple[str, int, int, float]]: 
            - fpath (str): 保存的图片本地路径。
            - width (int): 生成图片的宽度。
            - height (int): 生成图片的高度。
            - elapsed (float): 生成耗时，秒为单位，保留 1 位小数。

            如果生成失败，则返回 None。

### 案例：
    Example:
        >>> result = generate_gradio(
        ...     prompt="竹林和山峰，云海，无人机穿越视角",
        ...     model="Qwen/Qwen-Image",
        ...     width=1024,
        ...     height=1024
        ... )
        >>> print(result)
        ('results/success_20250829-193011.jpg', 1024, 1024, 8.7)
    """

**官方网站：** [https://www.modelscope.cn/studios/phoenixdna/t2i-modelscope-mcp](https://www.modelscope.cn/studios/phoenixdna/t2i-modelscope-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`entertainment and media`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`mcp-remote https://phoenixdna-t2i-modelscope-mcp.ms.show/gradio_api/mcp/sse --transport sse-only`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/phoenixdna-modelscope-t2i.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
