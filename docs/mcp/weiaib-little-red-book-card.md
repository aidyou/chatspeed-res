---
title: "小红薯📕卡片MCP"
description: "将Markdown文档转换为精美的知识卡片的工具，支持多种风格。可以作为MCP（Model Context Protocol）工具使用，并提供诸如将Markdown转换为HTML、生成图片以及支持18种不同主题等多种功能。"
---

# 小红薯📕卡片MCP

将Markdown文档转换为精美的知识卡片的工具，支持多种风格。可以作为MCP（Model Context Protocol）工具使用，并提供诸如将Markdown转换为HTML、生成图片以及支持18种不同主题等多种功能。

# 小红薯📕卡片MCP (Little Red Book Card MCP)

将 Markdown 文档转换为精美的知识卡片，支持多种风格的MCP工具。

[![npm version](/mcp-assets/ae3f1f68b65710da6a2b989a0d0ff914.svg)](https://www.npmjs.com/package/little-red-book-card-mcp)
[![License: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)
[![TypeScript](/mcp-assets/e2f4f7eb3c57946e147a6d1fb44ccbbc.svg)](https://www.typescriptlang.org/)
[![Node.js](/mcp-assets/148c8c2430c0ccd90f9e06f3c3ea5e04.svg)](https://nodejs.org/)

## 如何在MCP中配置小红书卡片工具

### 基本配置格式

```json
{
  "mcpServers": {
    "little-red-book-card-mcp": {
      "command": "npx",
      "args": ["@lucianaib/little-red-book-card-mcp"]
    }
  }
}
```



### 使用效果
> 随便制作一个Markdown内容，并将其转换为知识卡片图片，儿童童话风格，尺寸为手机大小

效果如下：

## 功能特性

### 🎨 多种主题样式
支持18种不同的主题风格，满足各种场景需求：

**现代风格**
- 📱 **苹果备忘录** - 简洁清新的苹果风格备忘录
- 🪟 **玻璃拟态** - 现代玻璃拟态效果
- 🌈 **梦幻渐变** - 梦幻般的渐变色彩
- 🌿 **清新自然** - 清新的自然绿色调

**创意风格**
- 🎨 **波普艺术** - 鲜艳大胆的波普艺术风格
- 🏛️ **艺术装饰** - 奢华的装饰艺术风格
- 🎭 **水彩艺术** - 水彩画艺术效果
- 🌌 **赛博朋克** - 赛博朋克霓虹风格

**专业风格**
- 📊 **商务简报** - 专业商务简报风格
- 📰 **日本杂志** - 日本杂志排版风格
- 🖋️ **复古打字机** - 复古打字机风格
- 📓 **笔记本** - 仿笔记本纸张效果

**特色风格**
- 🟣 **紫色小红书** - 小红书风格的紫色主题
- 🇨🇳 **中国传统** - 中国传统文化风格
- 🧸 **儿童童话** - 儿童童话风格
- ⚫ **极简黑白** - 极简黑白配色
- 🌟 **温暖柔和** - 温暖舒适的柔和色调
- 🏢 **简约高级灰** - 极简的高级灰色调
- 🖤 **暗黑科技** - 暗黑科技风格

### 📝 核心功能
- ✅ **Markdown转HTML卡片** - 将Markdown文档转换为精美的知识卡片
- 🖼️ **图片生成功能** - 将HTML卡片转换为PNG/JPEG图片文件
- 📁 **文件读取支持** - 支持直接读取Markdown文件
- 🎯 **多种卡片类型** - 支持通过type参数指定卡片类型/尺寸
- 📊 **内容统计** - 自动计算字数和字符数
- 🌟 **长内容处理** - 智能分割长内容，避免性能问题
- 🔧 **MCP集成** - 完整的MCP工具集成，易于集成到各种平台

## 快速开始

### 全局安装

```bash
npm install -g little-red-book-card-mcp
```

或者使用pnpm：

```bash
pnpm add little-red-book-card-mcp
```

### 作为MCP工具使用

1. **启动MCP服务器**：
```bash
   node dist/index.js
```

2. **可用工具**：
   - `convert_markdown_to_card` - 将Markdown转换为知识卡片
   - `generate_card_image` - 将Markdown转换为知识卡片图片
   - `list_available_themes` - 列出所有可用主题

3. **转换示例**：

   **HTML卡片生成（默认手机尺寸 mobile）**：
```json
   {
     "name": "convert_markdown_to_card",
     "arguments": {
       "content": "# 标题\n\n这是Markdown内容。",
       "theme": "紫色小红书",
       "type": "mobile",
       "filePath": "optional/path/to/file.md"
     }
   }
```

   **图片生成示例（默认手机尺寸 mobile）**：
```json
   {
     "name": "generate_card_image",
     "arguments": {
       "content": "# 标题\n\n这是Markdown内容。",
       "theme": "清新自然",
       "type": "mobile",
       "outputDir": "./output",
       "format": "png",
       "quality": 80
     }
   }
```

## API接口

### convert_markdown_to_card
将Markdown内容转换为知识卡片。

**参数**：
- `content` (string, 必需) - Markdown内容
- `theme` (string, 必需) - 主题名称
- `type` (string, 可选) - 卡片类型 ('mobile', 'standard', 'large', 'small', 'wide')，默认 `mobile`
- `filePath` (string, 可选) - Markdown文件路径

**返回**：
```json
{
  "html": "完整的HTML卡片代码",
  "css": "主题CSS样式",
  "metadata": {
    "theme": "主题名称",
    "type": "卡片类型",
    "wordCount": "字数",
    "charCount": "字符数"
  }
}
```

### generate_card_image
将Markdown内容转换为知识卡片图片。

**参数**：
- `content` (string, 必需) - Markdown内容
- `theme` (string, 必需) - 主题名称
- `type` (string, 可选) - 卡片类型 ('mobile', 'standard', 'large', 'small', 'wide')，默认 `mobile`
- `filePath` (string, 可选) - Markdown文件路径
- `outputDir` (string, 可选) - 输出目录，默认为当前目录
- `format` (string, 可选) - 图片格式 ('png', 'jpeg')，默认为 'png'
- `quality` (number, 可选) - 图片质量（仅jpeg格式），默认为 80

**返回**：
```json
{
  "imagePath": "生成的图片文件路径",
  "metadata": {
    "theme": "主题名称",
    "type": "卡片类型",
    "format": "图片格式",
    "size": "文件大小（字节）",
    "wordCount": "字数",
    "charCount": "字符数"
  }
}
```

### list_available_themes
列出所有可用的主题样式。

**返回**：
```json
{
  "themes": [
    {
      "name": "主题名称",
      "key": "主题键名",
      "description": "主题描述"
    }
  ],
  "count": "主题数量"
}
```

## 开发环境设置

### 克隆和安装

```bash
git clone 
cd little-red-book-card-mcp
pnpm install
```

### 编译和运行

```bash
# 编译项目
npm run build

# 运行开发服务器
npm run dev

# 运行测试（Jest）
npm test

# 查看测试覆盖率
npm run test:coverage
```

## 文件结构

```
├── src/
│   ├── index.ts          # MCP主服务器实现
├── tests/
│   ├── index.test.ts     # 主要测试文件
│   ├── setup.ts          # 测试环境设置
├── dist/                 # 编译输出目录
├── package.json          # 项目配置
├── tsconfig.json         # TypeScript配置
├── jest.config.js        # Jest测试配置
└── README.md             # 项目说明

### 常用脚本

- `npm run build`：编译 TypeScript
- `npm run start`：启动 MCP 服务器（stdio）
- `npm run generate:pop-mobile`：生成波普艺术手机尺寸示例图片
```

## 技术栈

- **TypeScript** - 类型安全的JavaScript开发
- **Node.js** - 运行时环境
- **MCP SDK** - Model Context Protocol开发框架
- **marked** - Markdown解析器
- **cheerio** - HTML操作库
- **puppeteer** - HTML到图片转换
- **Jest** - 测试框架

## 许可证

MIT License - 详见 LICENSE 文件

## 贡献

欢迎提交Issue和Pull Request！

### 开发指南

1. Fork 项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

### 代码规范

- 使用 TypeScript 编写
- 遵循 ESLint 规范
- 添加适当的单元测试
- 保持代码注释清晰

## 更新日志

### v1.0.2 (2024-10-29)
- 🚀 成功发布到npm registry
- 🔧 修复包名配置问题
- 📝 更新MCP配置示例
- 🧪 优化发布流程

### v1.0.0 (2024-10-29)
- ✅ 初始版本发布
- 🎨 支持18种主题样式
- 📝 实现Markdown到HTML卡片转换
- 📁 支持文件读取功能
- 🔧 完整的MCP工具集成
- 📊 自动内容统计功能
- 🌟 长内容智能分割
- 🧪 完整的测试覆盖

## 支持

如果您在使用过程中遇到问题，可以通过以下方式获得帮助：

- 📖 查看 [文档](#api接口)
- 🐛 提交 [Issue](https://github.com/your-repo/issues)
- 📧 发送邮件至 [support@example.com](mailto:support@example.com)

## 致谢

感谢所有为这个项目做出贡献的开发者和测试者！

---

**小红书卡片MCP** - 让您的Markdown内容焕发新生！

**官方网站：** [https://github.com/OnePieceLwc/little-red-book-card-mcp](https://github.com/OnePieceLwc/little-red-book-card-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`memory`
- 标签：`knowledge and memory`, `小红薯📕卡片`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`@lucianaib/little-red-book-card-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/weiaib-little-red-book-card.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
