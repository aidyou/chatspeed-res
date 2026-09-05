---
title: "网站图片AI文生图"
description: "AI图片生成MCP Server 一个基于Model Context Protocol (MCP)的AI图片生成服务器，专门用于自动分析网页和文章内容，生成相应的AI图片。 功能特性 🎯 核心功能 1. 智能网页分析: 自动分析HTML内容，识别需要图片的区域 2. 文章配图生成: 分析文章内容，为关键段落生成配图 3. AI图片生成: 使用FLUX模型生成高质量图片 4. 英文提示词优化: 自动…"
---

# 网站图片AI文生图

AI图片生成MCP Server 一个基于Model Context Protocol (MCP)的AI图片生成服务器，专门用于自动分析网页和文章内容，生成相应的AI图片。 功能特性 🎯 核心功能 1. 智能网页分析: 自动分析HTML内容，识别需要图片的区域 2. 文章配图生成: 分析文章内容，为关键段落生成配图 3. AI图片生成: 使用FLUX模型生成高质量图片 4. 英文提示词优化: 自动…

# AI图片生成MCP Server

一个基于Model Context Protocol (MCP)的AI图片生成服务器，专门用于自动分析网页和文章内容，生成相应的AI图片。

## 功能特性

### 🎯 核心功能
1. **智能网页分析**: 自动分析HTML内容，识别需要图片的区域
2. **文章配图生成**: 分析文章内容，为关键段落生成配图
3. **AI图片生成**: 使用FLUX模型生成高质量图片
4. **英文提示词优化**: 自动将中文描述转换为适合AI生成的英文提示词
5. **HTML增强**: 将生成的图片自动嵌入到原始网页中

### 🛠️ 提供的工具

#### 1. analyze-and-generate-webpage-images
- **功能**: 分析网页HTML内容并生成相应图片
- **参数**:
  - `html`: 网页HTML内容
  - `generateImages`: 是否立即生成图片（默认true）

#### 2. analyze-and-generate-article-images
- **功能**: 分析文章内容并生成配图
- **参数**:
  - `content`: 文章内容
  - `title`: 文章标题（可选）
  - `generateImages`: 是否立即生成图片（默认true）

#### 3. generate-single-image
- **功能**: 根据提示词生成单张图片
- **参数**:
  - `prompt`: 英文提示词
  - `width`: 图片宽度（默认1024）
  - `height`: 图片高度（默认1024）
  - `model`: 使用的模型名称（可选）

#### 4. generate-enhanced-webpage
- **功能**: 将生成的图片嵌入到原始HTML中
- **参数**:
  - `originalHtml`: 原始HTML内容
  - `imageMapping`: 图片ID到URL的映射

#### 5. translate-prompt-to-english
- **功能**: 将中文描述翻译为英文提示词
- **参数**:
  - `chinesePrompt`: 中文提示词或描述
  - `style`: 图片风格（可选）

### 📊 提供的资源

#### 1. generated-images
- **URI**: `generated://images`
- **功能**: 获取所有已生成的AI图片信息

#### 2. generation-stats
- **URI**: `stats://generation`
- **功能**: 获取图片生成的统计信息

## 安装和使用

### 1. 安装依赖
```bash
npm install
```

### 2. 编译TypeScript
```bash
npm run build
```

### 3. 运行服务器
```bash
npm start
```

### 4. 开发模式
```bash
npm run dev
```

## 配置MCP客户端

### Claude Desktop配置
在Claude Desktop的配置文件中添加：

```json
{
  "mcpServers": {
    "ai-image-generator": {
      "command": "node",
      "args": ["/path/to/your/ai-image-generator-mcp-server/dist/index.js"],
      "env": {
        "MODELSCOPE_API_KEY": "your-modelscope-api-key-here"
      }
    }
  }
}
```

**重要**: 请将 `"your-modelscope-api-key-here"` 替换为您的真实ModelScope API密钥。

### 其他MCP客户端
根据您使用的MCP客户端，按照相应的配置方式添加此服务器，并在环境变量中设置API密钥。

## API密钥配置

### 1. 获取ModelScope API密钥
1. 访问 [ModelScope](https://modelscope.cn/)
2. 注册并登录账户
3. 进入个人中心 → API管理
4. 创建新的API密钥
5. 复制API密钥（格式：`ms-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`）

### 2. 配置环境变量
在MCP客户端配置文件的 `env` 部分设置API密钥，一次配置长期使用，类似于Google Maps的配置方式。

## 使用示例

配置完API密钥后，可以直接在MCP客户端中使用工具，无需再传递API密钥：

### 1. 分析网页并生成图片
```typescript
// 通过MCP客户端调用
const result = await mcpClient.callTool("analyze-and-generate-webpage-images", {
  html: "

我的网站
 alt='主页图片'>
",
  generateImages: true
});
```

### 2. 为文章生成配图
```typescript
const result = await mcpClient.callTool("analyze-and-generate-article-images", {
  content: "人工智能技术正在快速发展...",
  title: "AI技术发展趋势"
});
```

### 3. 生成单张图片
```typescript
const result = await mcpClient.callTool("generate-single-image", {
  prompt: "A beautiful landscape with mountains and lake, photorealistic, high quality",
  width: 1024,
  height: 768
});
```

## 技术架构

### 核心组件
- **ImageGenerator**: 负责与ModelScope API交互，生成AI图片
- **ContentAnalyzer**: 分析网页和文章内容，识别图片需求
- **AIImageGeneratorMCPServer**: 主服务器类，处理MCP协议通信

### 支持的图片格式
- 宽度: 200-1200像素
- 高度: 200-1200像素
- 格式: JPEG, PNG

### 使用的AI模型
- 默认模型: `MusePublic/489_ckpt_FLUX_1`
- 支持自定义模型（需要在ModelScope平台可用）

## 高级功能

### 智能内容分析
- 自动识别网页中的图片占位符
- 基于上下文生成相关的图片描述
- 智能推断图片尺寸和风格

### 提示词优化
- 自动将中文描述转换为英文
- 添加质量和风格描述符
- 基于内容上下文优化提示词

### 批量处理
- 支持同时生成多张图片
- 异步处理提高效率
- 错误处理和重试机制

## 错误处理

服务器包含完善的错误处理机制：
- API调用失败时的错误信息
- 网络连接问题的处理
- 无效参数的验证
- 详细的错误日志记录

## 性能优化

- 异步图片生成
- 内存中缓存生成的图片信息
- 批量处理优化
- 错误重试机制

## 扩展性

### 添加新的图片生成模型
在`ImageGenerator`类中添加新的模型支持：

```typescript
const newModel = 'your-new-model-id';
const response = await this.generateImage({
  prompt: "your prompt",
  model: newModel
});
```

### 添加新的分析算法
在`ContentAnalyzer`类中扩展分析功能：

```typescript
private customAnalyzer(content: string): AnalysisResult {
  // 实现自定义分析逻辑
}
```

## 贡献指南

1. Fork 项目
2. 创建特性分支
3. 提交更改
4. 推送到分支
5. 创建Pull Request

## 许可证

MIT License

## 联系方式

如有问题或建议，请通过以下方式联系：
- 创建Issue
- 提交Pull Request

## 更新日志

### v1.0.0
- 初始版本发布
- 支持网页和文章分析
- 集成FLUX图片生成模型
- 提供完整的MCP协议支持

**官方网站：** [https://github.com/alchaincyf/AIpic](https://github.com/alchaincyf/AIpic)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`browser`
- 标签：`browser automation`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`/path/to/your/ai-image-generator-mcp-server/dist/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/alchain-alchain-aipic.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
