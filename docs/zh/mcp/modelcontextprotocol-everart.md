---
title: "EverArt生成器"
description: "用于Claude桌面端的图像生成服务器，采用EverArt的API。"
---

# EverArt生成器

用于Claude桌面端的图像生成服务器，采用EverArt的API。

# EverArt MCP 服务器

为使用 EverArt API 的 Claude 桌面端提供的图像生成服务器。

## 安装
```bash
npm install
export EVERART_API_KEY=your_key_here
```

## 配置
添加到 Claude 桌面端配置：

### Docker
```json
{
  "mcpServers": {
    "everart": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "-e", "EVERART_API_KEY", "mcp/everart"],
      "env": {
        "EVERART_API_KEY": "your_key_here"
      }
    }
  }
}
```

### NPX

```json
{
  "mcpServers": {
    "everart": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-everart"],
      "env": {
        "EVERART_API_KEY": "your_key_here"
      }
    }
  }
}
```

## 工具

### generate_image
生成具有多种模型选项的图像。在浏览器中打开结果并返回 URL。

参数：
```typescript
{
  prompt: string,       // 图像描述
  model?: string,       // 模型 ID（默认值："207910310772879360"）
  image_count?: number  // 图像数量（默认值：1）
}
```

模型：
- 5000: FLUX1.1（标准）
- 9000: FLUX1.1-ultra
- 6000: SD3.5
- 7000: Recraft-Real
- 8000: Recraft-Vector

所有生成的图像尺寸为 1024x1024。

示例用法：
```javascript
const result = await client.callTool({
  name: "generate_image",
  arguments: {
    prompt: "一只优雅坐着的猫",
    model: "7000",
    image_count: 1
  }
});
```

响应格式：
```
图像生成成功！
图像已在您的默认浏览器中打开。

生成详情：
- 模型：7000
- 提示词： "一只优雅坐着的猫"
- 图像 URL：https://storage.googleapis.com/...

您也可以点击上方的 URL 再次查看图像。
```

## 使用 Docker 构建

```sh
docker build -t mcp/everart -f src/everart/Dockerfile . 
```

**官方网站：** [https://github.com/modelcontextprotocol/servers/tree/main/src/everart](https://github.com/modelcontextprotocol/servers/tree/main/src/everart)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`art and culture`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @modelcontextprotocol/server-everart`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/modelcontextprotocol-everart.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
