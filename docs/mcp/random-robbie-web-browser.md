---
title: "智能浏览器"
description: "一个高级的网络浏览服务器，通过安全的API启用无头浏览器交互，提供导航、内容提取、元素交互和截图捕获等功能。"
---

# 智能浏览器

一个高级的网络浏览服务器，通过安全的API启用无头浏览器交互，提供导航、内容提取、元素交互和截图捕获等功能。

# MCP Web 浏览器服务器

一个基于 Playwright 的高级网页浏览服务器，为 Model Context Protocol (MCP) 提供支持，通过灵活且安全的 API 实现无头浏览器交互。

## 🌐 功能

- **无头网页浏览**：访问任何网站，并绕过 SSL 证书验证
- **全页面内容提取**：获取完整的 HTML 内容，包括动态加载的 JavaScript
- **多标签页支持**：创建、管理和切换多个浏览器标签页
- **高级网页交互工具**：
  - 提取文本内容
  - 点击页面元素
  - 在表单字段中输入文本
  - 捕获屏幕截图
  - 提取页面链接并具有过滤功能
  - 向任意方向滚动页面
  - 在页面上执行 JavaScript
  - 刷新页面
  - 等待导航完成
- **资源管理**：在不活动后自动清理未使用的资源
- **增强页面信息**：获取当前页面的详细元数据

## 🚀 快速开始

### 前提条件

- Python 3.10+
- MCP SDK
- Playwright

### 安装

```bash
# Install MCP and Playwright
pip install mcp playwright

# Install browser dependencies
playwright install
```

### Claude Desktop 配置

将以下内容添加到 `claude_desktop_config.json` 文件中：

```json
{
  "mcpServers": {
    "web-browser": {
      "command": "python",
      "args": [
        "/path/to/your/server.py"
      ]
    }
  }
}
```

## 💡 使用示例

### 基本网页导航

```python
# Browse to a website
page_content = browse_to("https://example.com")

# Extract page text
text_content = extract_text_content()

# Extract text from a specific element
title_text = extract_text_content("h1.title")
```

### 网页交互

```python
# Navigate to a page
browse_to("https://example.com/login")

# Input text into a form
input_text("#username", "your_username")
input_text("#password", "your_password")

# Click a login button
click_element("#login-button")
```

### 屏幕截图捕获

```python
# Capture full page screenshot
full_page_screenshot = get_page_screenshots(full_page=True)

# Capture specific element screenshot
element_screenshot = get_page_screenshots(selector="#main-content")
```

### 链接提取

```python
# Get all links on the page
page_links = get_page_links()

# Get links matching a pattern
filtered_links = get_page_links(filter_pattern="contact")
```

### 多标签页浏览

```python
# Create a new tab
tab_id = create_new_tab("https://example.com")

# Create another tab
another_tab_id = create_new_tab("https://example.org")

# List all open tabs
tabs = list_tabs()

# Switch between tabs
switch_tab(tab_id)

# Close a tab
close_tab(another_tab_id)
```

### 高级交互

```python
# Scroll the page
scroll_page(direction="down", amount="page")

# Execute JavaScript on the page
result = execute_javascript("return document.title")

# Get detailed page information
page_info = get_page_info()

# Refresh the current page
refresh_page()

# Wait for navigation to complete
wait_for_navigation(timeout_ms=5000)
```

## 🛡️ 安全特性

- 绕过 SSL 证书验证
- 安全的浏览器上下文管理
- 自定义用户代理配置
- 错误处理和全面的日志记录
- 可配置的超时设置
- CSP 绕过控制
- 防止 cookie 被窃取

## 🔧 故障排除

### 常见问题

- **SSL 证书错误**：自动绕过
- **页面加载缓慢**：调整 `browse_to()` 方法中的超时时间
- **找不到元素**：仔细检查选择器
- **浏览器资源使用**：在不活动期后自动清理

### 日志

所有重要事件都会被记录下来，提供详细的调试信息。

## 📋 工具参数

### `browse_to(url: str, context: Optional[Any] = None)`
- `url`: 要导航到的网站
- `context`: 可选的上下文对象（目前未使用）

### `extract_text_content(selector: Optional[str] = None, context: Optional[Any] = None)`
- `selector`: 可选的 CSS 选择器，用于提取特定内容
- `context`: 可选的上下文对象（目前未使用）

### `click_element(selector: str, context: Optional[Any] = None)`
- `selector`: 要点击的元素的 CSS 选择器
- `context`: 可选的上下文对象（目前未使用）

### `get_page_screenshots(full_page: bool = False, selector: Optional[str] = None, context: Optional[Any] = None)`

- `full_page`: 捕获整个页面的截图
- `selector`: 可选元素以进行截图
- `context`: 可选上下文对象（当前未使用）

### `get_page_links(filter_pattern: Optional[str] = None, context: Optional[Any] = None)`
- `filter_pattern`: 可选文本模式以过滤链接
- `context`: 可选上下文对象（当前未使用）

### `input_text(selector: str, text: str, context: Optional[Any] = None)`
- `selector`: 输入元素的 CSS 选择器
- `text`: 要输入的文本
- `context`: 可选上下文对象（当前未使用）

### `create_new_tab(url: Optional[str] = None, context: Optional[Any] = None)`
- `url`: 在新标签页中导航到的可选 URL
- `context`: 可选上下文对象（当前未使用）

### `switch_tab(tab_id: str, context: Optional[Any] = None)`
- `tab_id`: 要切换到的标签页 ID
- `context`: 可选上下文对象（当前未使用）

### `list_tabs(context: Optional[Any] = None)`
- `context`: 可选上下文对象（当前未使用）

### `close_tab(tab_id: Optional[str] = None, context: Optional[Any] = None)`
- `tab_id`: 要关闭的标签页的可选 ID（默认为当前标签页）
- `context`: 可选上下文对象（当前未使用）

### `refresh_page(context: Optional[Any] = None)`
- `context`: 可选上下文对象（当前未使用）

### `get_page_info(context: Optional[Any] = None)`
- `context`: 可选上下文对象（当前未使用）

### `scroll_page(direction: str = "down", amount: str = "page", context: Optional[Any] = None)`
- `direction`: 滚动方向（'up', 'down', 'left', 'right'）
- `amount`: 滚动量（'page', 'half' 或一个数字）
- `context`: 可选上下文对象（当前未使用）

### `wait_for_navigation(timeout_ms: int = 10000, context: Optional[Any] = None)`
- `timeout_ms`: 最大等待时间（毫秒）
- `context`: 可选上下文对象（当前未使用）

### `execute_javascript(script: str, context: Optional[Any] = None)`
- `script`: 要执行的 JavaScript 代码
- `context`: 可选上下文对象（当前未使用）

## 🤝 贡献

欢迎贡献！请随时提交 Pull Request。

### 开发设置

```bash
# Clone the repository
git clone https://github.com/random-robbie/mcp-web-browser.git

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -e .[dev]
```

## 📄 许可证

MIT 许可证

## 🔗 相关项目

- [Model Context Protocol](https://modelcontextprotocol.io)
- [Playwright](https://playwright.dev)
- [Claude Desktop](https://claude.ai/desktop)

## 💬 支持

对于问题和疑问，请在 GitHub 上[打开一个问题](https://github.com/random-robbie/mcp-web-browser/issues)。

**官方网站：** [https://github.com/random-robbie/mcp-web-browser](https://github.com/random-robbie/mcp-web-browser)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`browser`
- 标签：`browser automation`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`python`
- 参数：`/path/to/your/server.py`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/random-robbie-web-browser.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
