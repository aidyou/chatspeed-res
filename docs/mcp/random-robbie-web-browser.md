---
title: "mcp-web-browser"
description: "An advanced web browsing server enabling headless browser interactions via a secure API, providing features like navigation, content extraction, element interaction, and screenshot capture."
---

# mcp-web-browser

An advanced web browsing server enabling headless browser interactions via a secure API, providing features like navigation, content extraction, element interaction, and screenshot capture.

# MCP Web Browser Server

An advanced web browsing server for the Model Context Protocol (MCP) powered by Playwright, enabling headless browser interactions through a flexible, secure API.

## 🌐 Features

- **Headless Web Browsing**: Navigate to any website with SSL certificate validation bypass
- **Full Page Content Extraction**: Retrieve complete HTML content, including dynamically loaded JavaScript
- **Multi-Tab Support**: Create, manage, and switch between multiple browser tabs
- **Advanced Web Interaction Tools**:
  - Extract text content
  - Click page elements
  - Input text into form fields
  - Capture screenshots
  - Extract page links with filtering capabilities
  - Scroll pages in any direction
  - Execute JavaScript on pages
  - Refresh pages
  - Wait for navigation to complete
- **Resource Management**: Automatic cleanup of unused resources after inactivity
- **Enhanced Page Information**: Get detailed metadata about the current page

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- MCP SDK
- Playwright

### Installation

```bash
# Install MCP and Playwright
pip install mcp playwright

# Install browser dependencies
playwright install
```

### Configuration for Claude Desktop

Add to your `claude_desktop_config.json`:

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

## 💡 Usage Examples

### Basic Web Navigation

```python
# Browse to a website
page_content = browse_to("https://example.com")

# Extract page text
text_content = extract_text_content()

# Extract text from a specific element
title_text = extract_text_content("h1.title")
```

### Web Interaction

```python
# Navigate to a page
browse_to("https://example.com/login")

# Input text into a form
input_text("#username", "your_username")
input_text("#password", "your_password")

# Click a login button
click_element("#login-button")
```

### Screenshot Capture

```python
# Capture full page screenshot
full_page_screenshot = get_page_screenshots(full_page=True)

# Capture specific element screenshot
element_screenshot = get_page_screenshots(selector="#main-content")
```

### Link Extraction

```python
# Get all links on the page
page_links = get_page_links()

# Get links matching a pattern
filtered_links = get_page_links(filter_pattern="contact")
```

### Multi-Tab Browsing

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

### Advanced Interactions

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

## 🛡️ Security Features

- SSL certificate validation bypass
- Secure browser context management
- Custom user-agent configuration
- Error handling and comprehensive logging
- Configurable timeout settings
- CSP bypass control
- Protection against cookie stealing

## 🔧 Troubleshooting

### Common Issues

- **SSL Certificate Errors**: Automatically bypassed
- **Slow Page Load**: Adjust timeout in `browse_to()` method
- **Element Not Found**: Verify selectors carefully
- **Browser Resource Usage**: Auto-cleanup after inactivity period

### Logging

All significant events are logged with detailed information for easy debugging.

## 📋 Tool Parameters

### `browse_to(url: str, context: Optional[Any] = None)`
- `url`: Website to navigate to
- `context`: Optional context object (currently unused)

### `extract_text_content(selector: Optional[str] = None, context: Optional[Any] = None)`
- `selector`: Optional CSS selector to extract specific content
- `context`: Optional context object (currently unused)

### `click_element(selector: str, context: Optional[Any] = None)`
- `selector`: CSS selector of the element to click
- `context`: Optional context object (currently unused)

### `get_page_screenshots(full_page: bool = False, selector: Optional[str] = None, context: Optional[Any] = None)`
- `full_page`: Capture entire page screenshot
- `selector`: Optional element to screenshot
- `context`: Optional context object (currently unused)

### `get_page_links(filter_pattern: Optional[str] = None, context: Optional[Any] = None)`
- `filter_pattern`: Optional text pattern to filter links
- `context`: Optional context object (currently unused)

### `input_text(selector: str, text: str, context: Optional[Any] = None)`
- `selector`: CSS selector of input element
- `text`: Text to input
- `context`: Optional context object (currently unused)

### `create_new_tab(url: Optional[str] = None, context: Optional[Any] = None)`
- `url`: Optional URL to navigate to in the new tab
- `context`: Optional context object (currently unused)

### `switch_tab(tab_id: str, context: Optional[Any] = None)`
- `tab_id`: ID of the tab to switch to
- `context`: Optional context object (currently unused)

### `list_tabs(context: Optional[Any] = None)`
- `context`: Optional context object (currently unused)

### `close_tab(tab_id: Optional[str] = None, context: Optional[Any] = None)`
- `tab_id`: Optional ID of the tab to close (defaults to current tab)
- `context`: Optional context object (currently unused)

### `refresh_page(context: Optional[Any] = None)`
- `context`: Optional context object (currently unused)

### `get_page_info(context: Optional[Any] = None)`
- `context`: Optional context object (currently unused)

### `scroll_page(direction: str = "down", amount: str = "page", context: Optional[Any] = None)`
- `direction`: Direction to scroll ('up', 'down', 'left', 'right')
- `amount`: Amount to scroll ('page', 'half', or a number)
- `context`: Optional context object (currently unused)

### `wait_for_navigation(timeout_ms: int = 10000, context: Optional[Any] = None)`
- `timeout_ms`: Maximum time to wait in milliseconds
- `context`: Optional context object (currently unused)

### `execute_javascript(script: str, context: Optional[Any] = None)`
- `script`: JavaScript code to execute
- `context`: Optional context object (currently unused)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Setup

```bash
# Clone the repository
git clone https://github.com/random-robbie/mcp-web-browser.git

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venvScriptsactivate`

# Install dependencies
pip install -e .[dev]
```

## 📄 License

MIT License

## 🔗 Related Projects

- [Model Context Protocol](https://modelcontextprotocol.io)
- [Playwright](https://playwright.dev)
- [Claude Desktop](https://claude.ai/desktop)

## 💬 Support

For issues and questions, please [open an issue](https://github.com/random-robbie/mcp-web-browser/issues) on GitHub.

**Official site: ** [https://github.com/random-robbie/mcp-web-browser](https://github.com/random-robbie/mcp-web-browser)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `browser`
- Tags: `browser automation`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `python`
- Args: `/path/to/your/server.py`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/random-robbie-web-browser.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
