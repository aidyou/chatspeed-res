---
title: "紫微斗数mcp(MCP&Agent挑战赛)"
description: "紫微斗数 MCP 服务器 一个基于 Model Context Protocol (MCP) 的专业紫微斗数命理分析服务器，提供完整的命盘生成、解读、分析和可视化功能。支持传统紫微斗数算法，集成现代数据持久化和可视化技术。 🌟 功能特点 核心功能 - 🔮 命盘生成: 基于农历算法生成完整的紫微斗数命盘 - 📖 命盘解读: 提供详细的命盘分析和专业解释 - 🌟 运势分析: 分析当前和未来的运势走向…"
---

# 紫微斗数mcp(MCP&Agent挑战赛)

紫微斗数 MCP 服务器 一个基于 Model Context Protocol (MCP) 的专业紫微斗数命理分析服务器，提供完整的命盘生成、解读、分析和可视化功能。支持传统紫微斗数算法，集成现代数据持久化和可视化技术。 🌟 功能特点 核心功能 - 🔮 命盘生成: 基于农历算法生成完整的紫微斗数命盘 - 📖 命盘解读: 提供详细的命盘分析和专业解释 - 🌟 运势分析: 分析当前和未来的运势走向…

# 紫微斗数 MCP 服务器

一个基于 Model Context Protocol (MCP) 的专业紫微斗数命理分析服务器，提供完整的命盘生成、解读、分析和可视化功能。支持传统紫微斗数算法，集成现代数据持久化和可视化技术。

## 🌟 功能特点

### 核心功能
- 🔮 **命盘生成**: 基于农历算法生成完整的紫微斗数命盘
- 📖 **命盘解读**: 提供详细的命盘分析和专业解释
- 🌟 **运势分析**: 分析当前和未来的运势走向
- 💕 **合婚分析**: 双人命盘合婚配对分析
- 📅 **择日功能**: 根据命盘选择吉日良辰
- 🤖 **AI智能解盘**: 结合传统命理与现代AI技术

### 可视化功能
- 🎨 **命盘图像**: 生成多种样式的可视化命盘图表
- 📊 **数据可视化**: 支持SVG、PNG、HTML多种格式输出
- 🎭 **主题定制**: 传统、现代、彩色、单色等多种配色方案

### 专业分析
- ⭐ **星曜信息**: 查询各个星曜的详细信息和影响
- 🏠 **宫位分析**: 获取十二宫位的含义和深度分析
- 📈 **人生时间轴**: 大运流年详细分析
- 👥 **人际关系**: 家庭、朋友、事业关系分析
- 💼 **职业指导**: 职业发展和决策支持
- 🏥 **健康分析**: 健康趋势和养生建议
- 🎓 **教育指导**: 学习能力和教育规划

## 📦 安装

### 环境要求
- Node.js 18.0+
- npm 8.0+
- SQLite 3.0+

### 安装依赖

```bash
npm install
```

## 🚀 使用方法

### 启动服务器

```bash
# 开发模式
npm run dev

# 生产模式
npm start
```

### 客户端配置 (stdio)

如果您使用支持MCP的客户端（如Claude Desktop），可以通过stdio方式连接到本服务：

#### Claude Desktop配置

在Claude Desktop的配置文件中添加以下配置：

```json
{
  "mcpServers": {
    "ziwei-doushu": {
      "command": "npx",
      "args": ["-y","ziwei-mcp"]
    }
  }
}
```


## 📚 API 文档

### 核心工具

#### 1. generate_chart - 生成命盘
生成完整的紫微斗数命盘

**参数:**
- `name` (string): 姓名
- `birthDate` (string): 出生日期 (YYYY-MM-DD)
- `birthTime` (string): 出生时间 (HH:MM)
- `gender` (string): 性别 (male/female)
- `location` (object): 出生地点
  - `province` (string): 省份
  - `city` (string): 城市
  - `longitude` (number): 经度
  - `latitude` (number): 纬度
- `timezone` (string): 时区 (默认: Asia/Shanghai)
- `calendar` (string): 历法 (solar/lunar，默认: solar)

#### 2. interpret_chart - 命盘解读
提供详细的命盘分析和解释

**参数:**
- `chartId` (string): 命盘ID
- `aspects` (array): 解读方面
  - personality: 性格特质
  - career: 事业发展
  - wealth: 财富运势
  - relationships: 感情关系
  - health: 健康状况
  - family: 家庭关系
- `detailLevel` (string): 详细程度 (basic/detailed/comprehensive)

#### 3. analyze_fortune - 运势分析
分析特定时期的运势走向

**参数:**
- `chartId` (string): 命盘ID
- `period` (string): 分析周期 (current_year/next_year/decade/custom)
- `startDate` (string): 开始日期 (YYYY-MM-DD)
- `endDate` (string): 结束日期 (YYYY-MM-DD)
- `aspects` (array): 分析方面

#### 4. analyze_compatibility - 合婚分析
双人命盘合婚配对分析

**参数:**
- `chart1Id` (string): 第一人命盘ID
- `chart2Id` (string): 第二人命盘ID
- `analysisType` (string): 分析类型 (marriage/business/friendship)
- `aspects` (array): 分析维度

#### 5. select_auspicious_date - 择日功能
根据命盘选择吉日良辰

**参数:**
- `chartId` (string): 命盘ID
- `eventType` (string): 事件类型
- `dateRange` (object): 日期范围
- `preferences` (object): 偏好设置

### 可视化工具

#### 6. generate_visualization - 生成可视化图表
生成命盘可视化图表，支持多种样式和格式

**参数:**
- `chartId` (string): 命盘ID
- `visualizationType` (string): 可视化类型
  - traditional_chart: 传统命盘
  - modern_wheel: 现代轮盘
  - palace_grid: 宫位网格
  - star_map: 星曜地图
- `includeElements` (array): 包含元素
- `colorScheme` (string): 配色方案
- `outputFormat` (string): 输出格式 (svg/png/html)

### 专业分析工具

#### 7. analyze_life_timeline - 人生时间轴分析
分析人生时间轴，包括大运流年详细分析

#### 8. analyze_relationships - 人际关系分析
分析人际关系，包括家庭、朋友、同事等

#### 9. career_guidance - 职业发展指导
职业发展指导和决策支持

#### 10. health_analysis - 健康分析
健康分析和养生建议

#### 11. educational_guidance - 教育指导
教育和学习指导

## 🛠️ 开发指南

### 开发环境设置

```bash
# 进入项目目录
cd 紫微斗数

# 安装依赖
npm install

# 启动MCP服务器
npm start

# 或启动开发模式
npm run dev
```

### 可用脚本

```bash
npm start      # 启动MCP服务器
npm run dev    # 启动开发模式（带调试）
npm test       # 运行基础测试
npm run lint   # ESLint代码检查
npm run format # Prettier代码格式化
```

### 代码规范

- 使用 ESLint 进行代码检查
- 使用 Prettier 进行代码格式化
- 遵循 CommonJS 模块规范
- 支持 Node.js 18.0+ 版本

## 🔧 配置说明

### 配置文件

项目使用以下配置文件：

- `config/sqlite-config.js` - SQLite数据库配置
- `config/persistence-config.js` - 数据持久化配置
- `package.json` - 项目依赖和脚本配置

### 数据库配置

项目使用 SQLite 作为数据存储，配置文件位于 `config/sqlite-config.js`。

## 📖 使用示例

### 生成命盘示例

```javascript
// 通过MCP调用
const chart = await mcpClient.callTool('generate_chart', {
  name: '张三',
  birthDate: '1990-01-01',
  birthTime: '08:30',
  gender: 'male',
  location: {
    province: '北京市',
    city: '北京市',
    longitude: 116.4074,
    latitude: 39.9042
  }
});
```

### 命盘解读示例

```javascript
const interpretation = await mcpClient.callTool('interpret_chart', {
  chartId: chart.id,
  aspects: ['personality', 'career', 'wealth'],
  detailLevel: 'detailed'
});
```

## 🤝 贡献指南

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

### 提交规范

```
feat: 新功能
fix: 修复bug
docs: 文档更新
style: 代码格式调整
refactor: 代码重构
test: 测试相关
chore: 构建过程或辅助工具的变动
```

## 📄 许可证

本项目采用 MIT 许可证。

## 🆘 支持与反馈

- 📚 详细文档: 紫微斗数MCP开发文档
- 📋 SQLite部署: [SQLite部署指南](https://github.com/SiwuXue/ziwei-mcp/blob/HEAD/SQLite部署指南.md)
- 🎨 SVG生成: [SVG生成器使用指南](https://github.com/SiwuXue/ziwei-mcp/blob/HEAD/SVG生成器使用指南.md)

## 🔗 相关链接

- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Claude Desktop](https://claude.ai/desktop)
- [lunar-javascript库](https://github.com/6tail/lunar-javascript) - 农历转换核心库

---

**注意**: 本项目仅供学习和研究使用，命理分析结果仅供参考，不应作为人生重大决策的唯一依据。

## 📋 更新日志

### v1.0.0 (2024-01-01)
- ✨ 初始版本发布
- 🔮 实现基础命盘生成功能
- 📖 支持命盘解读和运势分析
- 🎨 添加SVG图像生成
- 💾 集成SQLite数据持久化
- 🤖 支持AI智能解盘
- 💕 添加合婚分析功能
- 📅 实现择日功能

## ❓ 常见问题

**Q: 为什么生成的命盘与其他软件不同？**
A: 不同的紫微斗数软件可能使用不同的算法和参数，本服务基于传统算法实现，结果可能存在差异。

**Q: 支持哪些地区的时区？**
A: 支持全球主要时区，默认使用Asia/Shanghai（北京时间）。

**Q: 数据会保存多长时间？**
A: 目前数据会永久保存在本地SQLite数据库中，您可以手动清理不需要的数据。

**Q: 如何获得更准确的分析结果？**
A: 请确保输入准确的出生日期、时间和地点信息，时间精确到分钟级别。

## 🔧 技术支持

如遇到技术问题，请提供以下信息：
1. 错误信息和错误代码
2. 输入的参数信息
3. 操作系统和Node.js版本
4. 详细的操作步骤

解释数据

**官方网站：** [https://github.com/SiwuXue/ziwei-mcp](https://github.com/SiwuXue/ziwei-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`memory`, `media`
- 标签：`knowledge and memory`, `art and culture`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y ziwei-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/wuai60-ziwei.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
