---
title: "Windows-MCP.Net"
description: "Windows MCP.Net is a .NET-based Windows desktop automation MCP (Model Context Protocol) server that gives AI assistants the ability to interact with the Windows desktop environment. Table of Contents…"
---

# Windows-MCP.Net

Windows MCP.Net is a .NET-based Windows desktop automation MCP (Model Context Protocol) server that gives AI assistants the ability to interact with the Windows desktop environment. Table of Contents…

# Windows MCP.Net

A .NET-based Windows desktop automation MCP (Model Context Protocol) server that gives AI assistants the ability to interact with the Windows desktop environment.

## Table of Contents

- [Features](#features)
- [Use Cases](#use-cases)
- [Screenshots](#screenshots)
- [Tech Stack](#tech-stack)
- [API Docs](#api-docs)
- [Project Structure](#project-structure)
- [Feature Extension Ideas](#feature-extension-ideas)
- [Configuration](#configuration)
- [Contribution Guide](#contribution-guide)
- [Changelog](#changelog)
- [Support](#support)

## Quick Start

### Prerequisites
- Windows operating system
- .NET 10.0 Runtime or later

**Important**: This project requires .NET 10 to run. Please make sure .NET 10 is installed locally first. If it is not installed yet, visit the [.NET 10 download page](https://dotnet.microsoft.com/zh-cn/download/dotnet/10.0) to download and install it.

### 1. MCP Client Configuration

Add the following configuration to your MCP client:

#### Using a globally installed tool (recommended)
```
{
    "mcpServers": {
     "WindowsMCP.Net": {
      "type": "stdio",
      "command": "dnx",
      "args": ["WindowsMCP.Net@", "--yes"],
      "env": {}
    }
    }
}
```

#### Running directly from the project source (development mode)

**Option 1: Workspace configuration**

Create a `.vscode/mcp.json` file in the project root:
```
{
  "mcpServers": {
    "Windows-MCP.Net-Dev": {
      "type": "stdio",
      "command": "dotnet",
      "args": ["run", "--project", "src/Windows-MCP.Net.csproj"],
      "cwd": "${workspaceFolder}",
      "env": {}
    }
  }
}
```

**Option 2: User configuration**

Run `MCP: Open User Configuration` from the VS Code command palette and add:
```
{
  "mcpServers": {
    "Windows-MCP.Net-Local": {
      "type": "stdio",
      "command": "dotnet",
      "args": ["run", "--project", "src/Windows-MCP.Net.csproj"],
      "env": {}
    }
  }
}
```

> **Note**: Running from source is convenient for development and debugging; changes take effect without reinstalling. VS Code 1.102+ supports automatic discovery and management of MCP servers.

### 2. Installation and Running

#### Option 1: Global install (recommended)
```
dotnet tool install --global WindowsMCP.Net
```

#### Option 2: Run from source
```
# Clone the repository
git clone https://github.com/AIDotNet/Windows-MCP.Net.git
cd Windows-MCP.Net

# Build the project
dotnet build

# Run the project
dotnet run --project src/Windows-MCP.Net.csproj
```

### 3. Getting Started
After configuration, restart your MCP client and start using Windows desktop automation!

## Features

### Core Features
- **App Launch**: Launch applications from the Start menu by name
- **PowerShell Integration**: Execute PowerShell commands and return results
- **Desktop State Capture**: Get the current desktop state, including active apps, UI elements, etc.
- **Clipboard Operations**: Copy and paste text content
- **Mouse Operations**: Click, drag, and move the mouse cursor
- **Keyboard Operations**: Text input, key presses, and shortcut combinations
- **Window Management**: Resize and reposition windows, switch between applications
- **Scrolling**: Scroll at specified coordinates
- **Web Scraping**: Fetch webpage content and convert it to Markdown
- **Browser Operations**: Open a URL in the default browser
- **Screenshots**: Capture the screen and save to a temporary directory
- **File System Operations**: Create, read, write, copy, move, and delete files and directories
- **OCR Text Recognition**: Extract text from the screen or a selected region, and locate text
- **System Control**: Adjust screen brightness, system volume, screen resolution, and other system settings
- **Wait Control**: Add delays between operations

### Supported Tools

## Desktop Tools

| Tool | Description |
|---------|----------|
| **LaunchTool** | Launch an application from the Start menu |
| **PowershellTool** | Execute PowerShell commands and return the exit code |
| **StateTool** | Capture desktop state information, including apps and UI elements |
| **ClipboardTool** | Copy and paste to/from the clipboard |
| **ClickTool** | Mouse clicks (left, right, middle; single, double, triple) |
| **TypeTool** | Type text at specified coordinates, with clear and Enter support |
| **ResizeTool** | Resize and reposition windows |
| **SwitchTool** | Switch to a specified application window |
| **ScrollTool** | Scroll at specified coordinates or the current mouse position |
| **DragTool** | Drag from source coordinates to target coordinates |
| **MoveTool** | Move the mouse cursor to specified coordinates |
| **ShortcutTool** | Execute keyboard shortcut combinations |
| **KeyTool** | Press a single keyboard key |
| **WaitTool** | Pause for a specified number of seconds |
| **ScrapeTool** | Scrape webpage content and convert it to Markdown |
| **ScreenshotTool** | Capture the screen, save to a temporary directory, and return the image path |
| **OpenBrowserTool** | Open a specified URL in the default browser |

## FileSystem Tools

| Tool | Description |
|---------|----------|
| **ReadFileTool** | Read the content of a specified file |
| **WriteFileTool** | Write content to a file |
| **CreateFileTool** | Create a new file and write specified content |
| **CopyFileTool** | Copy a file to a specified location |
| **MoveFileTool** | Move or rename a file |
| **DeleteFileTool** | Delete a specified file |
| **GetFileInfoTool** | Get file information (size, creation time, etc.) |
| **ListDirectoryTool** | List files and subdirectories in a directory |
| **CreateDirectoryTool** | Create a new directory |
| **DeleteDirectoryTool** | Delete a directory and its contents |
| **SearchFilesTool** | Search for files in a specified directory |

## OCR Tools

| Tool | Description |
|---------|----------|
| **ExtractTextFromScreenTool** | Extract text from the entire screen using OCR |
| **ExtractTextFromRegionTool** | Extract text from a specified screen region using OCR |
| **FindTextOnScreenTool** | Locate specified text on screen using OCR |
| **GetTextCoordinatesTool** | Get the coordinates of text on screen |
| **ExtractTextFromFileTool** | Extract text from an image file using OCR |

## UI Element Tools

| Tool | Description |
|---------|----------|
| **FindElementByTextTool** | Find a UI element by its text content |
| **FindElementByClassNameTool** | Find a UI element by its class name |
| **FindElementByAutomationIdTool** | Find a UI element by its automation ID |
| **GetElementPropertiesTool** | Get property information for the element at specified coordinates |
| **WaitForElementTool** | Wait for a specified element to appear on screen |

## SystemControl Tools

| Tool | Description |
|---------|----------|
| **BrightnessTool** | Adjust screen brightness, supporting increments and exact percentages |
| **VolumeTool** | Adjust system volume, supporting increments and exact percentages |
| **ResolutionTool** | Set screen resolution (high, medium, low) |

## Use Cases

### AI Assistant Desktop Automation
- **Smart customer service bots**: AI assistants can operate Windows applications automatically to help users complete complex desktop tasks
- **Voice assistant integration**: Control desktop applications via voice commands combined with speech recognition
- **Smart office assistant**: AI assistants handle routine office tasks automatically, such as document organization and email sending

### Office Automation
- **Automated data entry**: Automatically extract data from web pages or documents and enter it into Excel or other applications
- **Report generation**: Automatically collect system information and screenshots to produce formatted reports
- **Batch file processing**: Organize, rename, and categorize large numbers of files and documents automatically
- **Email automation**: Automatically send periodic reports and notification emails

### Software Testing and QA
- **UI automation testing**: Simulate user operations to test desktop application features automatically
- **Regression testing**: Automatically execute repetitive test cases to ensure software quality
- **Performance monitoring**: Automatically collect application performance data and generate monitoring reports
- **Bug reproduction**: Automatically reproduce reported issues to assist developers in debugging

### Business Process Automation
- **Customer service**: Automatically handle customer requests and update CRM systems
- **Order processing**: Automatically collect order information from multiple channels and enter it into systems
- **Inventory management**: Automatically update inventory data and generate restock reminders
- **Financial reconciliation**: Automatically compare financial data across systems and flag discrepancies

### Data Collection and Analysis
- **Web data scraping**: Automatically collect product prices, news, and other information from multiple websites
- **Competitor analysis**: Periodically collect competitor product information and pricing
- **Market research**: Automatically collect and organize market data to generate analysis reports
- **Social media monitoring**: Monitor brand mentions and automatically collect user feedback

### Gaming and Entertainment
- **Game assistance**: Automate repetitive in-game tasks (please follow game rules)
- **Streaming assistant**: Automatically manage streaming software, switch scenes, and send messages
- **Media management**: Automatically organize music and video files and update media libraries

### Healthcare
- **Medical record entry**: Automatically convert paper medical records to electronic format
- **Medical image analysis**: Automatically extract key information from medical reports using OCR
- **Appointment management**: Automatically handle patient appointment requests and update hospital systems

### Education and Training
- **Online exams**: Automatically grade multiple-choice questions and generate score reports
- **Course management**: Automatically update course information and notify students
- **Learning progress tracking**: Automatically record student activity and generate progress reports

### Manufacturing and Logistics
- **Production data collection**: Automatically collect data from production equipment and update ERP systems
- **Quality inspection**: Detect product quality automatically using image recognition
- **Logistics tracking**: Automatically update shipment status and send tracking information to customers

### System Operations
- **Server monitoring**: Automatically check server status and generate monitoring reports
- **Log analysis**: Automatically analyze system logs to identify abnormal patterns
- **Backup management**: Automatically execute data backups and verify backup integrity
- **Software deployment**: Automate software installation and configuration processes

## Tech Stack

- **.NET 10.0**: Built on the latest .NET framework
- **Model Context Protocol**: Uses the MCP protocol for communication
- **Microsoft.Extensions.Hosting**: Application hosting framework
- **Serilog**: Structured logging
- **HtmlAgilityPack**: HTML parsing and web scraping
- **ReverseMarkdown**: HTML to Markdown conversion

## Project Structure

```
src/
├── Windows-MCP.Net/         # Main project
│   ├── .mcp/                # MCP server configuration
│   │   └── server.json      # Server configuration file
│   ├── Exceptions/          # Custom exception classes (to be extended)
│   ├── Interface/           # Service interface definitions
│   │   ├── IDesktopService.cs   # Desktop service interface
│   │   ├── IFileSystemService.cs # File system service interface
│   │   └── IOcrService.cs       # OCR service interface
│   ├── Models/              # Data models (to be extended)
│   ├── Prompts/             # Prompt templates (to be extended)
│   ├── Services/            # Core service implementations
│   │   ├── DesktopService.cs    # Desktop operations service
│   │   ├── FileSystemService.cs # File system service
│   │   └── OcrService.cs        # OCR service
│   ├── Tools/               # MCP tool implementations
│   │   ├── Desktop/             # Desktop operation tools
│   │   │   ├── ClickTool.cs         # Click tool
│   │   │   ├── ClipboardTool.cs     # Clipboard tool
│   │   │   ├── DragTool.cs          # Drag tool
│   │   │   ├── GetWindowInfoTool.cs # Window info tool
│   │   │   ├── KeyTool.cs           # Key press tool
│   │   │   ├── LaunchTool.cs        # App launch tool
│   │   │   ├── MoveTool.cs          # Mouse move tool
│   │   │   ├── OpenBrowserTool.cs   # Browser open tool
│   │   │   ├── PowershellTool.cs    # PowerShell execution tool
│   │   │   ├── ResizeTool.cs        # Window resize tool
│   │   │   ├── ScrapeTool.cs        # Web scraping tool
│   │   │   ├── ScreenshotTool.cs    # Screenshot tool
│   │   │   ├── ScrollTool.cs        # Scroll tool
│   │   │   ├── ShortcutTool.cs      # Shortcut tool
│   │   │   ├── StateTool.cs         # Desktop state tool
│   │   │   ├── SwitchTool.cs        # App switching tool
│   │   │   ├── TypeTool.cs          # Text input tool
│   │   │   ├── UIElementTool.cs     # UI element operation tool
│   │   │   └── WaitTool.cs          # Wait tool
│   │   ├── FileSystem/          # File system tools
│   │   │   ├── CopyFileTool.cs      # File copy tool
│   │   │   ├── CreateDirectoryTool.cs # Directory creation tool
│   │   │   ├── CreateFileTool.cs    # File creation tool
│   │   │   ├── DeleteDirectoryTool.cs # Directory deletion tool
│   │   │   ├── DeleteFileTool.cs    # File deletion tool
│   │   │   ├── GetFileInfoTool.cs   # File info tool
│   │   │   ├── ListDirectoryTool.cs # Directory listing tool
│   │   │   ├── MoveFileTool.cs      # File move tool
│   │   │   ├── ReadFileTool.cs      # File read tool
│   │   │   ├── SearchFilesTool.cs   # File search tool
│   │   │   └── WriteFileTool.cs     # File write tool
│   │   └── OCR/                 # OCR tools
│   │       ├── ExtractTextFromRegionTool.cs # Region text extraction tool
│   │       ├── ExtractTextFromScreenTool.cs # Screen text extraction tool
│   │       ├── FindTextOnScreenTool.cs      # Screen text search tool
│   │       └── GetTextCoordinatesTool.cs    # Text coordinate tool
│   ├── Program.cs           # Program entry point
│   └── Windows-MCP.Net.csproj   # Project file
└── Windows-MCP.Net.Test/    # Test project
    ├── DesktopToolsExtendedTest.cs  # Desktop tool extension tests
    ├── FileSystemToolsExtendedTest.cs # File system tool extension tests
    ├── OCRToolsExtendedTest.cs      # OCR tool extension tests
    ├── ToolTest.cs                  # Tool base tests
    ├── UIElementToolTest.cs         # UI element tool tests
    └── Windows-MCP.Net.Test.csproj  # Test project file
```

## Feature Extension Ideas

### Planned Features

#### Advanced UI Recognition and Interaction
- **Enhanced UI element recognition**: Support more UI frameworks (WPF, WinForms, UWP)
- **Optimized OCR text recognition**: Multi-language support for higher accuracy
- **Smart wait mechanism**: Dynamically wait for elements to finish loading

#### Enhanced File System Operations
- **Advanced file search**: Support content search and regular expression matching
- **Batch file operations**: Support batch copy, move, and rename
- **File monitoring**: Watch file system changes in real time

#### System Monitoring and Performance Analysis
- **System resource monitoring**: CPU, memory, disk, and network usage
- **Process management**: Process listing, performance monitoring, and process control
- **Performance analysis reports**: Generate detailed system performance reports

#### Multimedia Capabilities
- **Audio control**: System volume control and audio device management
- **Image processing**: Image scaling, cropping, and format conversion
- **Screen recording**: Screen recording and playback support

#### Networking and Communication
- **Network diagnostics**: Ping, port scanning, and connectivity tests
- **HTTP client**: RESTful API calls
- **WiFi management**: WiFi network scanning and connection management

#### Security and Permission Management
- **Permission checks**: User permission validation and management
- **Data encryption**: Encrypted storage for sensitive data
- **Operation auditing**: Complete operation logs and audit trails

### Development Roadmap

#### Phase 1 (High priority) - Core feature enhancements
- UI element recognition tools (Windows API implementation complete)
- File management tool enhancements
- System monitoring tools
- Basic security tools

#### Phase 2 (Medium priority) - Feature extensions
- OCR text recognition optimization
- Advanced file search
- Audio control tools
- Network diagnostic tools
- Excel operation support

#### Phase 3 (Low priority) - Advanced features
- Image processing tools
- Task scheduling system
- Database operation support
- Macro recording and playback

## Configuration

### Logging Configuration

The project uses Serilog for logging. Log files are stored in the `logs/` directory:

- Console output: real-time log display
- File output: rotated daily, retained for 31 days
- Log level: Debug and above

### Environment Variables

| Variable | Description | Default |
|--------|------|--------|
| `ASPNETCORE_ENVIRONMENT` | Runtime environment | `Production` |

## License

This project is open source under the MIT License. See the LICENSE file for details.

## Related Links

- [Model Context Protocol](https://modelcontextprotocol.io/)
- [.NET Documentation](https://docs.microsoft.com/dotnet/)
- [Windows API Documentation](https://docs.microsoft.com/windows/win32/)

## Contribution Guide

We welcome community contributions! If you would like to contribute, follow these steps:

### Setting Up the Development Environment

1. **Clone the repository**
```
   git clone https://github.com/AIDotNet/Windows-MCP.Net.git
   cd Windows-MCP.Net
```

2. **Install dependencies**
```
   dotnet restore
```

3. **Run tests**
```
   dotnet test
```

4. **Build the project**
```
   dotnet build
```

### Contribution Flow

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Standards

- Follow C# coding conventions
- Add unit tests for new features
- Update related documentation
- Make sure all tests pass

### Reporting Issues

When reporting an issue, please include:
- Operating system version
- .NET version
- Detailed error information
- Steps to reproduce

## Support

If you run into problems or have suggestions:

1. Check the [Issues](https://github.com/AIDotNet/Windows-MCP.Net/issues)
2. Create a new Issue
3. Join the discussion
4. Check the [Wiki](https://github.com/AIDotNet/Windows-MCP.Net/wiki) for more help

---

**Note**: This tool requires appropriate Windows permissions to perform desktop automation operations. Please make sure you use it in a trusted environment.

**Disclaimer**: When using this tool for automation, please comply with applicable laws, regulations, and software license agreements. The developers assume no liability for misuse of the tool.

**Official site: ** [https://github.com/AIDotNet/Windows-MCP.Net](https://github.com/AIDotNet/Windows-MCP.Net)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`, `browser`, `files`
- Tags: `browser automation`, `developer tools`, `file systems`, `mcp`, `windows`

## MCP Configuration

- Transport: `stdio`
- Command: `dnx`
- Args: `WindowsMCP.Net@ --yes`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/xuzeyu-windows-net.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
