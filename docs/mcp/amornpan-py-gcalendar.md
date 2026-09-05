---
title: "py-mcp-gcalendar"
description: "Model Context Protocol server that provides seamless access to Google Calendar API with asynchronous operation support, enabling efficient calendar management through a standardized interface."
---

# py-mcp-gcalendar

Model Context Protocol server that provides seamless access to Google Calendar API with asynchronous operation support, enabling efficient calendar management through a standardized interface.

# Google Calendar MCP Server - คู่มือการติดตั้งและการใช้งาน

## 📘 ภาพรวม
Model Context Protocol (MCP) server ที่ให้บริการเข้าถึง Google Calendar API พร้อมรองรับการทำงานแบบ asynchronous operations ช่วยให้การจัดการปฏิทินมีประสิทธิภาพผ่านอินเตอร์เฟซที่เป็นมาตรฐาน

## 🚀 คุณสมบัติหลัก
- เชื่อมต่อกับ Google Calendar API แบบไร้รอยต่อ
- รองรับการทำงานแบบ asynchronous สำหรับประสิทธิภาพสูงสุด
- ระบบ authentication แบบ OAuth 2.0 พร้อมการต่ออายุโทเค็นอัตโนมัติ
- การจัดการข้อผิดพลาดและการล็อกแบบครอบคลุม
- อินเทอร์เฟซ MCP ที่เรียบง่ายสำหรับการใช้งานกับ Claude และ AI อื่นๆ

## 🔑 เครื่องมือ API
| เครื่องมือ | คำอธิบาย |
|------------|----------|
| **list** | ดึงรายการกิจกรรมในปฏิทิน (2 ปีย้อนหลังถึง 1 ปีล่วงหน้า) |
| **create-event** | สร้างกิจกรรมใหม่ในปฏิทิน |
| **delete-duplicates** | ลบกิจกรรมที่ซ้ำกัน |
| **delete-event** | ลบกิจกรรมที่ระบุ |

## 🛠️ การติดตั้ง

### สิ่งที่ต้องมีก่อน
- Python 3.9 หรือสูงกว่า
- การเชื่อมต่ออินเทอร์เน็ต
- โปรเจกต์ Google Cloud Console ที่มี Google Calendar API เปิดใช้งาน

### ขั้นตอนการติดตั้ง

1. **โคลนโปรเจกต์**
```bash
   git clone https://github.com/yourusername/GCalendar.git
   cd GCalendar
```

2. **สร้างสภาพแวดล้อมเสมือน (วิธีที่แนะนำ)**
```bash
   python -m venv gcalendar_venv
   
   # สำหรับ Windows
   gcalendar_venvScriptsactivate
   
   # สำหรับ macOS/Linux
   source gcalendar_venv/bin/activate
```

3. **ติดตั้งแพ็คเกจที่จำเป็น**
```bash
   pip install -r requirements.txt
```

4. **เตรียมโฟลเดอร์ที่จำเป็น**
```bash
   mkdir -p credentials logs
```

### การตั้งค่า Authentication

1. **สร้างโปรเจกต์ Google Cloud Console**
   - ไปที่ [Google Cloud Console](https://console.cloud.google.com/)
   - สร้างโปรเจกต์ใหม่
   - เปิดใช้งาน Google Calendar API
   - สร้าง OAuth 2.0 Client ID
   - ดาวน์โหลด credentials.json ไปที่โฟลเดอร์ credentials/

2. **สร้างโทเค็น**
```bash
   python src/create_token.py
```
   - ทำตามขั้นตอนในเบราว์เซอร์เพื่อให้สิทธิ์การเข้าถึง
   - โทเค็นจะถูกบันทึกในโฟลเดอร์ credentials/ เป็น token.json

## ⚙️ การกำหนดค่าเทคนิค

### การกำหนดค่า MCP Server
เพิ่มในไฟล์ `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "gcalendar": {
      "command": "YOUR_PYTHON_PATH",
      "args": [
        "YOUR_PATH/GCalendar/src/mcp_server.py"
      ]
    }
  }
}
```

แทนที่ตัวยึดตำแหน่ง:
- `YOUR_PYTHON_PATH`: พาธไปยัง Python interpreter (จาก venv หรือ conda)
- `YOUR_PATH`: พาธเต็มไปยังโฟลเดอร์ที่โคลน

### โครงสร้างโปรเจกต์
```
GCalendar/
├── credentials/
│   ├── credentials.json   # จาก Google Cloud Console
│   └── token.json        # สร้างโดย create_token.py
├── logs/
│   └── calendar_service.log
├── src/
│   ├── calendar_service.py   # การดำเนินการปฏิทินหลัก
│   ├── create_token.py      # การสร้างโทเค็น
│   ├── list_past_events.py  # ยูทิลิตี้การแสดงรายการกิจกรรม
│   ├── mcp_client.py        # การใช้งาน MCP client
│   ├── mcp_server.py        # การใช้งานเซิร์ฟเวอร์หลัก
│   └── renew_token.py       # ยูทิลิตี้การต่ออายุโทเค็น
├── requirements.txt
└── README.md
```

## 📋 การใช้งาน

### การเริ่มใช้งานเซิร์ฟเวอร์

1. **เริ่มเซิร์ฟเวอร์ด้วยตนเอง**
```bash
   python src/mcp_server.py
```

2. **การใช้งานกับ Claude Desktop**
   - กำหนดค่าตามที่อธิบายในส่วนการกำหนดค่าข้างต้น
   - Claude จะเริ่มใช้งานเซิร์ฟเวอร์โดยอัตโนมัติเมื่อจำเป็น

### ตัวอย่างคำสั่ง

1. **ดูรายการกิจกรรมในปฏิทิน**
```
   แสดงกิจกรรมในปฏิทินของฉัน
```

2. **สร้างกิจกรรมใหม่**
```
   สร้างการประชุมชื่อ "ประชุมทีม" วันที่ 25 มีนาคม 2025 เวลา 14:00 น. ถึง 15:00 น.
```

3. **ลบกิจกรรมที่ซ้ำกัน**
```
   ลบกิจกรรม "ประชุมทีม" ที่ซ้ำกันในวันที่ 25 มีนาคม 2025
```

## 🔍 การแก้ไขปัญหา

### ปัญหาการรับรองความถูกต้อง
1. ตรวจสอบว่าไฟล์ credentials.json และ token.json อยู่ในโฟลเดอร์ credentials/
2. ลบ token.json และสร้างใหม่โดยใช้ create_token.py

### ปัญหาเกี่ยวกับเขตเวลา
1. ตรวจสอบว่าไลบรารี timezone ถูกติดตั้งแล้ว:
```bash
   pip install pytz tzdata
```

### การตรวจสอบล็อก
1. ดูไฟล์ล็อกเพื่อรับข้อมูลเพิ่มเติมเกี่ยวกับข้อผิดพลาด:
```bash
   cat logs/calendar_service.log
```

## 📚 การพึ่งพา
- google-auth-oauthlib==1.0.0
- google-auth-httplib2==0.1.0
- google-api-python-client==2.108.0
- aiohttp==3.8.5
- asyncio==3.4.3
- pytz==2023.3
- tzdata==2023.3

## 📄 ใบอนุญาต
โปรเจกต์นี้มีใบอนุญาตภายใต้ MIT License ดูไฟล์ LICENSE สำหรับรายละเอียด
"# py-mcp-gcalendar"

**Official site: ** [https://github.com/amornpan/py-mcp-gcalendar](https://github.com/amornpan/py-mcp-gcalendar)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `productivity`
- Tags: `calendar management`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `YOUR_PYTHON_PATH`
- Args: `YOUR_PATH/GCalendar/src/mcp_server.py`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/amornpan-py-gcalendar.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
