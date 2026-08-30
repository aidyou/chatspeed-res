---
title: "反虚假信息 MCP 服务器"
description: "启用对主张的分析、来源的验证以及使用多种认识论框架来检测操纵，以确保信息的可信度和道德性。"
---

# 反虚假信息 MCP 服务器

启用对主张的分析、来源的验证以及使用多种认识论框架来检测操纵，以确保信息的可信度和道德性。

# 反废话 MCP 服务器

一个用于分析声明、验证来源和使用多种认识论框架检测操纵的模型上下文协议服务器。

## 功能

该服务器提供了三种主要工具，用于检测和分析废话：

### 1. analyze_claim
使用多种认识论框架分析声明：

- **经验框架**
  - 关注可验证的证据
  - 评估可重复的结果
  - 交叉引用学术和科学资源
  - 评估方法严谨性

- **责任框架**
  - 评估道德影响
  - 评估社区影响
  - 考虑传统知识
  - 验证来源可信度

- **和谐框架**
  - 评估与已建立知识的一致性
  - 整合多种视角
  - 考虑情境适当性
  - 评估系统影响

- **多元框架**
  - 结合所有其他框架
  - 考虑多种认知方式
  - 评估情境适当性
  - 评估实际结果
  - 检查与社区价值观的一致性

### 2. validate_sources
- 提取并分析引用的来源
- 验证可信度和权威性
- 在多个平台上交叉引用
- 评估方法合理性
- 检查利益冲突

### 3. check_manipulation
检测操纵策略，包括：
- 情感操纵
- 社会压力
- 假权威
- 人为稀缺
- 制造紧迫感

## 安装

### 先决条件
- Node.js >= 18.0.0
- npm 或 yarn

### 设置

1. 安装依赖项：
```bash
npm install
```

2. 构建服务器：
```bash
npm run build
```

3. 添加到 Claude Desktop (MacOS)：
```json
{
  "mcpServers": {
    "anti-bullshit": {
      "command": "node",
      "args": ["/path/to/anti-bullshit-mcp-server/build/index.js"]
    }
  }
}
```

路径：`~/Library/Application Support/Claude/claude_desktop_config.json`

或者对于 VSCode 扩展：
路径：`~/Library/Application Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`

## 使用示例

```typescript
// Analyze a claim
const result = await analyze_claim({
  text: "Studies show that 87% of experts agree with this controversial claim",
  framework: "empirical"
});

// Validate sources
const validation = await validate_sources({
  text: "According to Dr. Smith's groundbreaking research...",
  framework: "responsible"
});

// Check for manipulation
const check = await check_manipulation({
  text: "Act now! This exclusive offer expires in the next 10 minutes!"
});
```

## 开发

开发时自动重建：
```bash
npm run watch
```

使用 MCP Inspector 调试：
```bash
npm run inspector
```

## 测试时间线

服务器使用 2025-01-01 作为声明的时间分析参考日期（特别是对 Goodman 的“grue”悖论和其他类似的哲学难题相关）。

## 许可证

MIT

## 作者

Teglon Labs (teglon@vibes.lol)

## 贡献

1. 分叉仓库
2. 创建你的功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -am 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 打开 Pull Request

**官方网站：** [https://github.com/bmorphism/anti-bullshit-mcp-server](https://github.com/bmorphism/anti-bullshit-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`research and data`, `security and iam`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`/path/to/anti-bullshit-mcp-server/build/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/bmorphism-anti-bullshit.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
