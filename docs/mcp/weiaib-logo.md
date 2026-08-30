---
title: "图标 MCP"
description: "一个智能Logo提取和处理的MCP（Model Context Protocol）服务器，支持从网站URL自动识别并提取Logo图标，并提供图像处理和矢量转换功能。 \n\n注：原文中并未包含具体的代码块或链接，因此在翻译时也未添加这些元素。如果需要进一步的信息或有具体的文档内容，请提供详细信息以便更准确地进行翻译。"
---

# 图标 MCP

一个智能Logo提取和处理的MCP（Model Context Protocol）服务器，支持从网站URL自动识别并提取Logo图标，并提供图像处理和矢量转换功能。 

注：原文中并未包含具体的代码块或链接，因此在翻译时也未添加这些元素。如果需要进一步的信息或有具体的文档内容，请提供详细信息以便更准确地进行翻译。

# logo-mcp

一个智能Logo提取和分析的MCP（Model Context Protocol）服务器，支持从网站URL自动识别并提取Logo图标，并提供详细的Logo分析功能。

## 功能特性

### 🎯 智能Logo提取
- **多源识别**：支持从favicon、Apple Touch图标、OpenGraph图像、CSS类名等多种方式提取Logo
- **智能评分**：自动评估候选Logo质量，选择最佳版本
- **格式支持**：支持PNG、JPG、SVG等多种图像格式
- **尺寸优化**：自动选择合适尺寸的Logo版本

### 📊 Logo分析
- **详细信息**：提供Logo尺寸、格式、类型等完整信息
- **多候选比较**：显示所有可能的Logo候选项及其评分
- **质量评估**：自动评估Logo图像质量和可用性
- **快速URL获取**：支持直接获取最佳Logo的URL地址



## 安装使用

### 作为MCP服务器使用

1. 安装依赖：
```bash
npm install @lucianaib/logo-mcp
```

2. 在MCP客户端配置中添加：
```json
{
  "mcpServers": {
    "logo-mcp": {
      "command": "npx",
      "args": ["@lucianaib/logo-mcp"]
    }
  }
}
```



### 开发环境设置

1. 克隆仓库：
```bash
git clone https://github.com/lfrbmw/Logo-MCP.git
cd Logo-MCP
```

2. 安装依赖：
```bash
npm install
```

3. 构建项目：
```bash
npm run build
```

4. 启动开发服务器：
```bash
npm run dev
```

## MCP工具
使用示例：
> 使用mcp提取 https://juejin.cn/的 Logo



### get_best_logo_url
从网站提取并返回最佳Logo的URL地址，适用于只需要获取最佳Logo URL的场景

**参数：**
- `url` (必需): 要分析的网站URL

**示例：**
```json
{
  "name": "get_best_logo_url",
  "arguments": {
    "url": "https://www.google.com"
  }
}
```

### analyze_logo
分析Logo的基本信息（尺寸、格式、质量等），支持onlyBestUrl参数只返回最佳Logo的URL

**参数：**
- `url` (必需): 要分析的网站URL
- `onlyBestUrl` (可选): 是否只返回最佳Logo的URL，默认为false

**示例：**
```json
{
  "name": "analyze_logo",
  "arguments": {
    "url": "https://www.github.com",
    "onlyBestUrl": false
  }
}
```

## 技术架构

### 核心模块

- **LogoExtractor**: 负责从网站提取Logo候选项，实现多源识别和智能评分算法
- **ImageProcessor**: 提供图像处理功能，包括格式转换、尺寸调整和质量增强

### 依赖库

- `@modelcontextprotocol/sdk`: MCP协议支持，提供服务器和通信框架
- `axios`: HTTP请求处理，用于获取网站内容和下载Logo图像
- `cheerio`: HTML解析，用于从网页中提取Logo相关信息
- `sharp`: 图像处理，提供格式转换、尺寸调整和增强功能
- `image-size`: 图像尺寸检测，用于获取Logo图像的尺寸信息
- `url-parse`: URL解析，用于处理和规范化网站URL
- `mime-types`: MIME类型检测，用于识别图像文件格式

## Logo提取策略

### 1. 多源候选提取
- Favicon链接 (`
`)
- Apple Touch图标 (`
`)
- OpenGraph图像 (``)
- CSS类名识别 (`.logo`, `#logo`, `.brand`等)
- 品牌相关图像

### 2. 智能评分算法
- **类型权重**：Logo类名 > Apple Touch > Favicon > 品牌图像 > OG图像
- **尺寸评分**：偏好32-512px的正方形或接近正方形图像
- **质量检测**：过滤损坏或空白图像

### 3. 最佳选择
根据综合评分自动选择最符合主视觉的Logo版本

## Logo分析流程

### 1. 多源提取
- **HTML解析**: 从页面meta标签提取favicon、apple-touch-icon等
- **CSS分析**: 通过类名和ID识别可能的Logo元素
- **OpenGraph**: 解析OG图像标签获取社交媒体使用的Logo
- **智能检测**: 识别页面上可能的品牌标识元素

### 2. 候选评分
- **类型权重**: 根据来源类型分配权重（如明确的logo类名权重更高）
- **尺寸分析**: 评估图像尺寸是否适合作为Logo（32px-512px范围内）
- **宽高比**: 优先选择接近正方形的图像
- **质量检测**: 检查图像是否损坏或过于模糊

### 3. 结果输出
- **详细分析**: 提供所有候选项的详细信息及评分
- **最佳推荐**: 根据综合评分推荐最合适的Logo
- **快速获取**: 支持直接返回最佳Logo的URL地址



## 错误处理

- **网络错误**：超时重试和友好提示
- **图像损坏**：自动检测和跳过
- **格式不支持**：清晰的错误信息
- **无Logo情况**：返回友好的无结果提示

## 性能优化

- **并发处理**：多候选Logo并行验证
- **缓存机制**：避免重复下载
- **内存管理**：及时释放图像缓冲区
- **超时控制**：防止长时间阻塞

## 贡献指南

1. Fork项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开Pull Request

## 许可证

本项目采用MIT许可证 - 查看 [LICENSE](https://github.com/lfrbmw/Logo-MCP/blob/HEAD/LICENSE) 文件了解详情

## 作者

- **lucianaib** - [GitHub](https://github.com/lfrbmw)

## 支持

如果您遇到问题或有功能建议，请在 [GitHub Issues](https://github.com/lfrbmw/Logo-MCP/issues) 中提出。

---

**Logo MCP** - 让Logo提取变得简单智能 🚀

**官方网站：** [https://github.com/lfrbmw/Logo-MCP](https://github.com/lfrbmw/Logo-MCP)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`files`, `media`
- 标签：`developer tools`, `entertainment and media`, `file systems`, `图标`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`@lucianaib/logo-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/weiaib-logo.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
