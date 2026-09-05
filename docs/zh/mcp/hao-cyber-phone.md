---
title: "MCP手机控制插件"
description: "一个用于MCP的插件，它使人工智能助手能够控制安卓手机，通过自然语言命令实现打电话、发信息、截屏和访问联系人等功能。"
---

# MCP手机控制插件

一个用于MCP的插件，它使人工智能助手能够控制安卓手机，通过自然语言命令实现打电话、发信息、截屏和访问联系人等功能。

# 📱 手机MCP插件
![Downloads](/mcp-assets/4d1f3086984595e9109c4d2031038cd5.svg)

🌟 一个强大的MCP插件，通过ADB命令轻松控制你的Android手机。

## 示例
- 根据浏览器中的今日天气，自动选择并播放网易音乐，无需确认
![play_mucic_x2](/mcp-assets/7ffd54c65ff5e102cecec104ce488286.gif)

- 从联系人中呼叫Hao。如果他不接电话，发送短信告诉他来101会议室。
![call_sms_x2](/mcp-assets/0ca7d3fcf13379dd8980c9a9cea21e5e.gif)

[中文文档](https://github.com/hao-cyber/phone-mcp/blob/HEAD/README_zh.md)

## ⚡ 快速开始

### 📥 安装
```bash
pip install phone-mcp
# or use uvx
uvx phone-mcp
```

### 🔧 配置

#### Cursor设置
在`~/.cursor/mcp.json`中配置：
```json
{
    "mcpServers": {
        "phone-mcp": {
            "command": "uvx",
            "args": [
                "phone-mcp"
            ]
        }
    }
}
```

#### Claude设置
添加到Claude配置中：
```json
{
    "mcpServers": {
        "phone-mcp": {
            "command": "uvx",
            "args": [
                "phone-mcp"
            ]
        }
    }
}
```

使用方法：
- 直接在Claude对话中使用命令，例如：
```
  请呼叫联系人hao
```

⚠️ 使用前，请确保：
- ADB已正确安装和配置
- 你的Android设备上已启用USB调试
- 设备通过USB连接到电脑

## 🎯 主要功能

- 📞 **通话功能**：拨打电话、结束通话、接听来电
- 💬 **消息**：发送和接收短信、获取原始消息
- 👥 **联系人**：访问手机联系人、通过自动化UI交互创建新联系人
- 📸 **媒体**：截屏、屏幕录制、媒体控制
- 📱 **应用程序**：启动应用、通过意图启动特定活动、列出已安装的应用、终止应用
- 🔧 **系统**：窗口信息、应用快捷方式
- 🗺️ **地图**：根据电话号码搜索兴趣点
- 🖱️ **UI交互**：点击、滑动、输入文本、按键
- 🔍 **UI检查**：按文本、ID、类或描述查找元素
- 🤖 **UI自动化**：等待元素、滚动查找元素
- 🧠 **屏幕分析**：结构化的屏幕信息和统一的交互
- 🌐 **网络浏览器**：在设备默认浏览器中打开URL
- 🔄 **UI监控**：监控UI变化，并等待特定元素出现或消失

## 🛠️ 要求

- Python 3.7+
- 启用了USB调试的Android设备
- ADB工具

## 📋 基本命令

### 设备与连接
```bash
# Check device connection
phone-cli check

# Get screen size
phone-cli screen-interact find method=clickable
```

### 通讯
```bash
# Make a call
phone-cli call 1234567890

# End current call
phone-cli hangup

# Send SMS
phone-cli send-sms 1234567890 "Hello"

# Get received messages (with pagination)
phone-cli messages --limit 10

# Get sent messages (with pagination)
phone-cli sent-messages --limit 10

# Get contacts (with pagination)
phone-cli contacts --limit 20

# Create a new contact with UI automation
phone-cli create-contact "John Doe" "1234567890"
```

### 媒体与应用
```bash
# Take screenshot
phone-cli screenshot

# Record screen
phone-cli record --duration 30

# Launch app (may not work on all devices)
phone-cli app camera

# Alternative app launch method using open_app (if app command doesn't work)
phone-cli open_app camera

# Close app
phone-cli close-app com.android.camera

# List installed apps (basic info, faster)
phone-cli list-apps

# List apps with pagination
phone-cli list-apps --page 1 --page-size 10

# List apps with detailed info (slower)
phone-cli list-apps --detailed

# Launch specific activity (reliable method for all devices)
phone-cli launch com.android.settings/.Settings

# Launch app by package name (may not work on all devices)
phone-cli app com.android.contacts

# Alternative launch by package name (if app command doesn't work)
phone-cli open_app com.android.contacts

# Launch app by package and activity (most reliable method)
phone-cli launch com.android.dialer/com.android.dialer.DialtactsActivity

# Open URL in default browser
phone-cli open-url google.com
```

### 屏幕分析与交互
```bash
# Analyze current screen with structured information
phone-cli analyze-screen

# Unified interaction interface
phone-cli screen-interact 
 [parameters]

# Tap at coordinates
phone-cli screen-interact tap x=500 y=800

# Tap element by text
phone-cli screen-interact tap element_text="Login"

# Tap element by content description
phone-cli screen-interact tap element_content_desc="Calendar"

# Swipe gesture (scroll down)
phone-cli screen-interact swipe x1=500 y1=1000 x2=500 y2=200 duration=300

# Press key
phone-cli screen-interact key keycode=back

# Input text
phone-cli screen-interact text content="Hello World"

# Find elements
phone-cli screen-interact find method=text value="Login" partial=true

# Wait for element
phone-cli screen-interact wait method=text value="Success" timeout=10

# Scroll to find element
phone-cli screen-interact scroll method=text value="Settings" direction=down max_swipes=5

# Monitor UI for changes
phone-cli monitor-ui --interval 0.5 --duration 30

# Monitor UI until specific text appears
phone-cli monitor-ui --watch-for text_appears --text "Welcome"

# Monitor UI until specific element ID appears
phone-cli monitor-ui --watch-for id_appears --id "login_button"

# Monitor UI until specific element class appears
phone-cli monitor-ui --watch-for class_appears --class-name "android.widget.Button"

# Monitor UI changes with output as raw JSON
phone-cli monitor-ui --raw
```

### 位置与地图
```bash
# Search nearby POIs with phone numbers
phone-cli get-poi 116.480053,39.987005 --keywords restaurant --radius 1000
```

## 📚 高级用法

### 应用程序和活动启动

该插件提供了多种方式来启动应用程序和活动：

1. **通过应用名称** (两种方法)：
```bash
   # 方法 1: 使用 app 命令（可能在某些设备上不起作用）
   phone-cli app camera
   
   # 方法 2: 使用 open_app 命令（如果 app 命令失败时的替代方案）
   phone-cli open_app camera
```

2. **通过包名** (两种方法)：
```bash
   # 方法 1: 使用 app 命令（可能在某些设备上不起作用）
   phone-cli app com.android.contacts
   
   # 方法 2: 使用 open_app 命令（如果 app 命令失败时的替代方案）
   phone-cli open_app com.android.contacts
```

3. **通过包名和活动名** (最可靠的方法)：
```bash
   # 此方法适用于所有设备
   phone-cli launch com.android.dialer/com.android.dialer.DialtactsActivity
```

> **注意**：如果您遇到 `app` 或 `open_app` 命令的问题，请始终使用带有完整组件名称（包/活动）的 `launch` 命令以获得最可靠的运行。

### 通过UI自动化创建联系人

插件提供了一种通过UI交互创建联系人的方式：

```bash
# Create a new contact with UI automation
phone-cli create-contact "John Doe" "1234567890"
```

该命令将执行以下操作：
1. 打开联系人应用程序
2. 导航到联系人创建界面
3. 填写姓名和电话号码字段
4. 自动保存联系人

### 基于屏幕的自动化

统一的屏幕交互接口使智能代理能够轻松地：

1. **分析屏幕**：获取UI元素和文本的结构化分析
2. **做出决策**：基于检测到的UI模式和可用操作
3. **执行交互**：通过一致的参数系统

### UI监控与自动化

插件提供了强大的UI监控功能，用于检测界面变化：

1. **基本UI监控**：
```bash
   # 以自定义间隔（秒）监控任何UI变化
   phone-cli monitor-ui --interval 0.5 --duration 30
```

2. **等待特定元素出现**：
```bash
   # 等待文本出现（对自动化测试有用）
   phone-cli monitor-ui --watch-for text_appears --text "登录成功"
   
   # 等待特定ID出现
   phone-cli monitor-ui --watch-for id_appears --id "confirmation_dialog"
```

3. **监控元素消失**：
```bash
   # 等待文本消失
   phone-cli monitor-ui --watch-for text_disappears --text "加载中..."
```

4. **获取详细的UI变化报告**：
```bash
   # 获取包含所有UI变化信息的原始JSON数据
   phone-cli monitor-ui --raw
```

> **提示**：UI监控对于自动化脚本特别有用，可以等待加载屏幕完成或确认UI中的动作已生效。

## 📚 详细文档

有关完整的文档和配置详情，请访问我们的 [GitHub仓库](https://github.com/hao-cyber/phone-mcp)。

## 🧰 工具文档

### 屏幕接口API

插件提供了强大的屏幕接口，并具有全面的API来与设备进行交互。以下是关键功能及其参数：

#### interact_with_screen
```python
async def interact_with_screen(action: str, params: Dict[str, Any] = None) -> str:
    """Execute screen interaction actions"""
```

- **参数:**
  - `action`: 动作类型 ("tap", "swipe", "key", "text", "find", "wait", "scroll")
  - `params`: 与每种动作类型相关的参数字典
- **返回:** 包含操作结果的 JSON 字符串

**示例:**
```python
# Tap by coordinates
result = await interact_with_screen("tap", {"x": 100, "y": 200})

# Tap by element text
result = await interact_with_screen("tap", {"element_text": "Login"})

# Swipe down
result = await interact_with_screen("swipe", {"x1": 500, "y1": 300, "x2": 500, "y2": 1200, "duration": 300})

# Input text
result = await interact_with_screen("text", {"content": "Hello world"})

# Press back key
result = await interact_with_screen("key", {"keycode": "back"})

# Find element by text
result = await interact_with_screen("find", {"method": "text", "value": "Settings", "partial": True})

# Wait for element to appear
result = await interact_with_screen("wait", {"method": "text", "value": "Success", "timeout": 10, "interval": 0.5})

# Scroll to find element
result = await interact_with_screen("scroll", {"method": "text", "value": "Privacy Policy", "direction": "down", "max_swipes": 8})
```

#### analyze_screen
```python
async def analyze_screen(include_screenshot: bool = False, max_elements: int = 50) -> str:
    """Analyze the current screen and provide structured information about UI elements"""
```
- **参数:**
  - `include_screenshot`: 结果中是否包含 base64 编码的截图
  - `max_elements`: 要处理的最大 UI 元素数量
- **返回:** 包含详细屏幕分析的 JSON 字符串

#### create_contact
```python
async def create_contact(name: str, phone: str) -> str:
    """Create a new contact with the given name and phone number"""
```
- **参数:**
  - `name`: 联系人的全名
  - `phone`: 联系人的电话号码
- **返回:** 包含操作结果的 JSON 字符串
- **位置:** 该函数位于 'contacts.py' 模块中，并实现了用于创建联系人的 UI 自动化

#### launch_app_activity
```python
async def launch_app_activity(package_name: str, activity_name: Optional[str] = None) -> str:
    """Launch an app using package name and optionally an activity name"""
```
- **参数:**
  - `package_name`: 要启动的应用程序包名
  - `activity_name`: 要启动的具体活动（可选）
- **返回:** 包含操作结果的 JSON 字符串
- **位置:** 该函数位于 'apps.py' 模块中

#### launch_intent
```python
async def launch_intent(intent_action: str, intent_type: Optional[str] = None, extras: Optional[Dict[str, str]] = None) -> str:
    """Launch an activity using Android intent system"""
```
- **参数:**
  - `intent_action`: 要执行的动作
  - `intent_type`: 意图的 MIME 类型（可选）
  - `extras`: 随意图传递的额外数据（可选）
- **返回:** 包含操作结果的 JSON 字符串
- **位置:** 该函数位于 'apps.py' 模块中

## 📄 许可证

Apache License, Version 2.0

# 联系人创建工具

此工具提供了一种使用 ADB 在 Android 设备上简单创建联系人的方法。

## 前提条件

- Python 3.x
- 已安装并配置好的 ADB (Android Debug Bridge)
- 连接并授权 ADB 的 Android 设备

## 使用方法

### 基本用法

只需运行脚本：

```bash
python create_contact.py
```

这将使用默认值创建一个联系人：
- 账户名: "你的账户名"
- 账户类型: "com.google"

### 高级用法

您可以使用 JSON 字符串提供自定义账户名和类型：

```bash
python create_contact.py '{"account_name": "your_account", "account_type": "com.google"}'
```

### 输出

脚本输出一个包含以下内容的 JSON 对象：
- `success`: 表示操作是否成功的布尔值
- `message`: 从命令中获取的任何输出或错误消息

成功输出示例：
```json
{"success": true, "message": ""}
```

## 错误处理

- 如果 ADB 不可用或设备未连接，脚本将返回错误
- 无效的 JSON 输入将导致错误消息
- 任何 ADB 命令错误都将被捕获并在 message 字段中返回

## 注意事项

- 确保您的 Android 设备已连接并授权使用 ADB
- 运行命令时，设备屏幕应处于解锁状态
- 某些设备可能需要额外权限才能修改联系人

### 应用程序和快捷方式
```bash
# Get app shortcuts (with pagination)
phone-cli shortcuts --package "com.example.app"
```

**官方网站：** [https://github.com/hao-cyber/phone-mcp](https://github.com/hao-cyber/phone-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`communication`
- 标签：`os automation`, `communication`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`phone-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/hao-cyber-phone.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
