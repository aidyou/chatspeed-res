---
title: "铁路票务信息查询系统"
description: "可以从铁路12306转件中获取票务信息"
---

# 铁路票务信息查询系统

可以从铁路12306转件中获取票务信息

12306MCP - 中国铁路智能购票助手

🚄 12306MCP（12306 Model-Context Protocol）是一个基于 AI 和自动化技术的智能铁路购票工具，旨在优化 12306 官网及 APP 的购票体验，提供自动抢票、候补监控、智能查询、多账号管理等功能。

🔧 功能特性

✅ 智能抢票 - 自动监控余票，快速下单

✅ 候补订单增强 - 实时监控候补成功率，自动调整策略

✅ 多账号支持 - 同时管理多个 12306 账号

✅ 自动验证码识别 - 支持滑块、点选验证码自动处理

✅ 查询优化 - 智能推荐最佳车次、座位

✅ 通知提醒 - 微信/Telegram/邮件通知抢票结果

🚀 快速开始

1. 安装

方式 1：npm 全局安装（推荐）

npm install -g 12306mcp 

方式 2：npx 临时运行

npx 12306mcp 

2. 配置

首次运行会自动生成配置文件 ~/.12306mcp/config.json，请按提示填写：

{ "accounts": [ { "username": "你的12306账号", "password": "密码（建议使用加密存储）" } ], "notification": { "email": "your-email@example.com", "wechat": "微信推送Key（可选）" } } 

3. 使用

基本命令

12306mcp --help # 查看帮助 12306mcp monitor # 监控余票 12306mcp grab --train G1234 --date 2025-01-01 --from 北京 --to 上海 # 自动抢票 12306mcp backup --train K1234 --date 2025-01-01 # 自动候补下单 

⚙️ 高级功能

1. 多账号模式

支持同时监控多个账号，提高抢票成功率：

12306mcp --account 账号1,账号2 monitor 

2. 自定义抢票策略

在 config.json 中可设置：

优先车次（高铁/动车/直达）

座位偏好（一等座/二等座/无座）

抢票频率（避免被封禁）

3. 代理设置（防封禁）

{ "proxy": "http://127.0.0.1:1080", "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ..." } 

⚠️ 注意事项

合法合规使用：本工具仅用于学习和技术研究，请勿滥用，避免影响 12306 系统正常运行。

账号安全：建议使用独立密码或二步验证，防止账号泄露。

防封策略：

避免高频请求（默认 5-10 秒/次）

使用代理 IP 轮换

模拟真实浏览器行为

📜 开源协议

本项目基于 MIT License 开源，欢迎贡献代码！

GitHub: https://github.com/your-repo/12306mcp

📢 反馈与支持

遇到问题？欢迎提交 Issue 或联系：

📧 Email: support@12306mcp.com

💬 Telegram: @12306mcp_support

🚀 祝您购票顺利，旅途愉快！ 🚄✨

**官方网站：** [https://www.modelscope.cn/mcp](https://www.modelscope.cn/mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`
- 标签：`search`, `chinese`

## MCP 配置

- 传输方式：`http`
- 启动命令：``
- 参数：无

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/bwxnwnx-12306.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
