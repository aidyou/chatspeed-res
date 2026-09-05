---
title: "紫微斗数_工具（\"MCP&Agent挑战赛\"）"
description: "npm version License: MIT Node.js Version TypeScript 基于 iztro 的模型上下文协议 (MCP) 服务器 生成紫微斗数星盘，支持地理编码和真太阳时转换 ✨ 功能特性 🌟 星盘生成: 根据出生信息生成详细的紫微斗数星盘 🌍 地理编码服务: 使用高德地图API将地点名称转换为精确坐标 ⏰ 真太阳时转换: 采用天文算法计算高精度真太阳时 🔌 MCP集…"
---

# 紫微斗数_工具（"MCP&Agent挑战赛"）

npm version License: MIT Node.js Version TypeScript 基于 iztro 的模型上下文协议 (MCP) 服务器 生成紫微斗数星盘，支持地理编码和真太阳时转换 ✨ 功能特性 🌟 星盘生成: 根据出生信息生成详细的紫微斗数星盘 🌍 地理编码服务: 使用高德地图API将地点名称转换为精确坐标 ⏰ 真太阳时转换: 采用天文算法计算高精度真太阳时 🔌 MCP集…

npm version 许可证: MIT Node.js 版本 TypeScript

基于 iztro 的模型上下文协议 (MCP) 服务器

生成紫微斗数星盘，支持地理编码和真太阳时转换

✨ 功能特性
🌟 星盘生成: 根据出生信息生成详细的紫微斗数星盘
🌍 地理编码服务: 使用高德地图API将地点名称转换为精确坐标
⏰ 真太阳时转换: 采用天文算法计算高精度真太阳时
🔌 MCP集成: 与MCP兼容客户端无缝集成
🔒 安全配置: 支持环境变量和配置文件
🚀 快速开始
安装
bash
npm install -g ziwei_iztro-mcpserver

配置
⚠️ 重要提示：使用前请配置您自己的API密钥！

方式一：环境变量（推荐）
bash
# 复制示例环境文件
cp .env.example .env

# 编辑 .env 文件并添加您的高德地图API密钥
echo "AMAP_API_KEY=your_actual_api_key_here" > .env

方式二：配置文件
bash
# 复制示例配置文件
cp iztro-mcp-config.example.json iztro-mcp-config.json

# 编辑配置文件并添加您的API密钥

获取高德地图API密钥
访问 [高德开放平台](https://lbs.amap.com/)
注册账号并登录
创建应用，选择"Web服务"类型
获取您的API密钥
自动化设置（推荐）
bash
# 运行交互式设置脚本
npm run setup

这将引导您完成配置过程并创建必要的文件。

📋 使用方法
作为独立服务器
bash
# 启动MCP服务器
ziwei_iztro-mcpserver
# 或者
npm start

与MCP客户端集成
添加到您的MCP客户端配置中：
json
{
  "mcpServers": {
    "iztro": {
      "command": "npx",
      "args": ["ziwei_iztro-mcpserver"]
    }
  }
}

或者本地安装：
json
{
  "mcpServers": {
    "iztro": {
      "command": "node",
      "args": ["/path/to/ziwei_iztro-mcpserver/dist/index.js"]
    }
  }
}

🛠️ 可用工具
1. geocode_location
将地点名称转换为精确坐标。

参数：

location (string, 必需): 地点名称，例如："安徽省合肥市庐江县金牛镇"
返回：
json
{
  "location": "安徽省合肥市庐江县金牛镇",
  "longitude": 117.123456,
  "latitude": 31.654321,
  "formatted_address": "安徽省合肥市庐江县金牛镇"
}

2. convert_to_apparent_solar_time
根据地理位置将北京时间转换为真太阳时。

参数：

beijingTime (string, 必需): 北京时间，格式为 YYYY-MM-DD HH:mm:ss
longitude (number, 必需): 经度（东经为正，西经为负）
latitude (number, 可选): 纬度（北纬为正，南纬为负）
返回：
json
{
  "beijing_time": "2024-01-01 12:00:00",
  "longitude": 117.123456,
  "latitude": 31.654321,
  "apparent_solar_time": "2024-01-01 12:08:30"
}

3. generate_astrolabe
生成紫微斗数星盘，支持基于地点的真太阳时转换。

参数：

birthday (string, 必需): 出生日期，格式为 YYYY-MM-DD
birthTime (number, 必需): 出生时辰 (0-11)，其中 0=子时，1=丑时，以此类推
gender (string, 必需): 性别，'男' 或 '女'
calendarType (string, 可选): 日历类型，'solar' 或 'lunar'，默认为 'solar'
isLeapMonth (boolean, 可选): 是否为闰月（仅农历有效）
language (string, 可选): 输出语言，支持 'zh-CN', 'zh-TW', 'en-US', 'ja-JP', 'ko-KR', 'vi-VN'
location (string, 可选): 出生地点，用于真太阳时转换
返回： 完整的星盘数据，如果提供了地点参数，还包含地点处理信息。

🛠️ 开发
前置要求
Node.js >= 16.0.0
npm 或 yarn
TypeScript 5.0+
本地开发
bash
# 克隆仓库
git clone https://github.com/smogievogie/ziwei_iztro-mcpserver.git
cd ziwei_iztro-mcpserver

# 安装依赖
npm install

# 构建项目
npm run build

# 运行设置脚本
npm run setup

# 启动开发服务器
npm run dev

测试
bash
# 使用 MCP Inspector 测试
npx @modelcontextprotocol/inspector node dist/index.js

📚 技术细节
真太阳时计算
基于 Jean Meeus《天文算法》
考虑地球轨道椭圆性和轴倾斜
与天文年历相比精度在3秒内支持早子时和晚子时区分
地理编码服务
由高德地图API提供支持
高精度坐标转换
支持中国境内详细地址解析
地理编码失败时自动回退到原始时间
🤝 贡献
欢迎贡献！请随时提交Pull Request。

开发指南
Fork 本仓库
创建 功能分支：`git checkout -b feature/amazing-feature`
提交 您的更改：`git commit -m 'Add amazing feature'`
推送 到分支：`git push origin feature/amazing-feature`
提交 Pull Request
代码规范
使用TypeScript确保类型安全
遵循ESLint配置
添加适当的单元测试
根据需要更新文档
📄 许可证
本项目采用MIT许可证 - 详见 [LICENSE](https://github.com/smogievogie/ziwei_iztro-mcpserver/blob/HEAD/LICENSE) 文件。

🙏 致谢
iztro - 紫微斗数核心库
MCP SDK - 模型上下文协议TypeScript SDK
高德地图API - 地理编码服务提供商
📞 支持
问题反馈: [GitHub Issues](https://github.com/your-repo/issues)
讨论: [GitHub Discussions](https://github.com/your-repo/discussions)
文档: [项目Wiki](https://github.com/your-repo/wiki)
为紫微斗数爱好者用❤️制作

**官方网站：** [https://github.com/smogievogie/ziwei_iztro-mcpserver.git](https://github.com/smogievogie/ziwei_iztro-mcpserver.git)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`art and culture`, `research and data`, `other`, `（"mcp&agent挑战赛"）`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`ziwei_iztro-mcpserver`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/haha008gg-ziwei-iztro-mcpserver1-1.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
