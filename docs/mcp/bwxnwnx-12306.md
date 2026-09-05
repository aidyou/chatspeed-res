---
title: "12306"
description: "You can obtain ticket information from the Railway 12306 app."
---

# 12306

You can obtain ticket information from the Railway 12306 app.

12306MCP - Intelligent Railway Ticket Booking Assistant for China

🚄 12306MCP (12306 Model-Context Protocol) is an intelligent railway ticket booking tool based on AI and automation technology, aimed at optimizing the ticket purchasing experience on the official 12306 website and app. It provides features such as automatic ticket grabbing, waitlist monitoring, smart queries, and multi-account management.

🔧 Features

✅ Smart Ticket Grabbing - Automatically monitors available tickets and places orders quickly

✅ Enhanced Waitlist Orders - Real-time monitoring of waitlist success rates, with automatic strategy adjustments

✅ Multi-Account Support - Manages multiple 12306 accounts simultaneously

✅ Automatic Captcha Recognition - Supports automatic handling of slider and point selection captchas

✅ Query Optimization - Recommends the best train and seat options intelligently

✅ Notification Alerts - Sends WeChat/Telegram/email notifications about ticket grabbing results

🚀 Quick Start

1. Installation

Method 1: npm Global Installation (Recommended)

bash
npm install -g 12306mcp

Method 2: npx Temporary Execution

bash
npx 12306mcp

2. Configuration

The first run will automatically generate a configuration file at `~/.12306mcp/config.json`. Please fill it out as prompted:

json
{ 
  "accounts": [ 
    { 
      "username": "Your 12306 username", 
      "password": "Password (It's recommended to use encrypted storage)" 
    } 
  ], 
  "notification": { 
    "email": "your-email@example.com", 
    "wechat": "WeChat Push Key (Optional)" 
  } 
}

3. Usage

Basic Commands

bash
12306mcp --help # View help
12306mcp monitor # Monitor available tickets
12306mcp grab --train G1234 --date 2025-01-01 --from Beijing --to Shanghai # Automatic ticket grabbing
12306mcp backup --train K1234 --date 2025-01-01 # Automatic waitlist order placement

⚙️ Advanced Features

1. Multi-Account Mode

Supports simultaneous monitoring of multiple accounts to increase the success rate of ticket grabbing:

bash
12306mcp --account account1,account2 monitor

2. Custom Ticket Grabbing Strategies

In `config.json`, you can set:

- Preferred train types (High-speed/EMU/Direct)
- Seat preferences (First Class/Second Class/No Seat)
- Grabbing frequency (to avoid being blocked)

3. Proxy Settings (To Prevent Blocking)

json
{ 
  "proxy": "http://127.0.0.1:1080", 
  "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ..." 
}

⚠️ Important Notes

Legal and Compliant Use: This tool is intended for learning and technical research only. Do not misuse it, and avoid affecting the normal operation of the 12306 system.

Account Security: It is recommended to use a separate password or two-factor authentication to prevent account leaks.

Anti-Blocking Strategies:

- Avoid high-frequency requests (default 5-10 seconds per request)
- Use rotating proxy IPs
- Simulate real browser behavior

📜 Open Source License

This project is open-sourced under the MIT License. Contributions are welcome!

GitHub: https://github.com/your-repo/12306mcp

📢 Feedback and Support

Encountered an issue? Feel free to submit an Issue or contact us:

📧 Email: support@12306mcp.com

💬 Telegram: @12306mcp_support

🚀 Wishing you a smooth ticket booking process and a pleasant journey! 🚄✨

**Official site: ** [https://www.modelscope.cn/mcp](https://www.modelscope.cn/mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `search`
- Tags: `search`, `chinese`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/bwxnwnx-12306.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
