---
title: "mcp2serial"
description: "A bridge that connects physical hardware devices with AI large language models via serial communication, allowing users to control hardware using natural language commands."
---

# mcp2serial

A bridge that connects physical hardware devices with AI large language models via serial communication, allowing users to control hardware using natural language commands.

# MCP2Serial: The Bridge Connecting the Physical World with AI LLMs

[English](https://github.com/mcp2everything/mcp2serial/blob/HEAD/README_EN.md) | Simplified Chinese

Control hardware with natural language and open a new era of IoT

## System Architecture

MCP2Serial system architecture diagram

## Workflow

MCP2Serial workflow diagram

## Project Vision

MCP2Serial is a project that connects serial devices to AI LLMs. It seamlessly bridges the physical world and AI models through the Model Context Protocol (MCP), ultimately enabling:
- Control your hardware devices with natural language
- AI responds in real time and adjusts physical parameters
- Give your devices the ability to understand and execute complex commands

## Key Features

- **Smart Serial Communication**
  - Auto-detect and configure serial devices; you can also specify the port
  - Supports multiple baud rates (default 115200)
  - Real-time status monitoring and error handling

- **MCP Protocol Integration**
  - Full Model Context Protocol support
  - Resource management and tool calls
  - Flexible prompt system

## Supported Clients

MCP2Serial supports any client implementing the MCP protocol, including:

| Client | Feature Support | Notes |
|--------|----------|------|
| Claude Desktop | Full support | Recommended; supports all MCP features |
| Continue | Full support | Great developer-tool integration |
| Cline | Resources + tools | Supports multiple AI providers |
| Zed | Basic support | Supports prompt commands |
| Sourcegraph Cody | Resources | Integrated via OpenCTX |
| Firebase Genkit | Partial support | Supports resource list and tools |

## Supported AI Models

Thanks to flexible client support, MCP2Serial works with many AI models:

### Cloud models
- OpenAI (GPT-4, GPT-3.5)
- Anthropic Claude
- Google Gemini
- AWS Bedrock
- Azure OpenAI
- Google Cloud Vertex AI

### Local models
- All models supported by LM Studio
- All models supported by Ollama
- Any OpenAI API-compatible model

### Prerequisites
Python 3.11 or later
Claude Desktop or Cline

## Quick Start

### 1. Installation

#### Windows users
Download [install.py](https://raw.githubusercontent.com/mcp2everything/mcp2serial/main/install.py)
```bash
python install.py
```
#### macOS users
```bash
# Download the installer
curl -O https://raw.githubusercontent.com/mcp2everything/mcp2serial/main/install_macos.py

# Run the installer
python3 install_macos.py
```

#### Ubuntu/Raspberry Pi users
```bash
# Download the installer
curl -O https://raw.githubusercontent.com/mcp2everything/mcp2serial/main/install_ubuntu.py

# Run the installer
python3 install_ubuntu.py
```

The installer automatically:
- Checks the system environment
- Installs required dependencies
- Creates the default config file
- Configures Claude Desktop (if installed)
- Checks serial devices

### Manual step-by-step dependency install
```bash
# Windows:
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
# macOS:
curl -LsSf https://astral.sh/uv/install.sh | sh
```
The main dependency is the uv tool, so once Python, uv, and Claude or Cline are installed, you are ready.

### Basic configuration
Add the following to your MCP client config (e.g. Claude Desktop or Cline):
Note: If you used the auto installer it configures Claude Desktop for you, so this step is not needed.
Using the default config file:
```json
{
    "mcpServers": {
        "mcp2serial": {
            "command": "uvx",
            "args": [
                "mcp2serial"
            ]
        }
    }
}
```
> Note: Restart Cline or Claude after changing the configuration

Configure the serial port and commands:
Note: The config below defaults to COM11; adjust it to match your setup
```yaml
# config.yaml
serial:
  port: COM11  # or auto-detect
  baud_rate: 115200  # optional, default 115200
  timeout: 1.0  # optional, default 1.0
  read_timeout: 1.0  # read timeout; raises an error if no response within 1 second
  response_start_string: OK  # optional, the start string of the serial response, default OK

commands:
  set_pwm:
    command: "PWM {frequency}\n"
    need_parse: false
    prompts:
      - "Set PWM to {value}"
```
## Configuration Guide
### Config file location

The config file (`config.yaml`) can be placed in several locations. The program searches in this order:

#### 1. Current working directory (for development/testing)
- Path: `./config.yaml`
- Example: if you run the program from `C:\Projects`, it looks for `C:\Projects\config.yaml`
- Use case: development and testing
- No special permissions needed

#### 2. User home directory (recommended for personal use)
```bash
# Windows:
C:\Users\<username>\.mcp2serial\config.yaml

# macOS:
/Users/<username>/.mcp2serial/config.yaml

# Linux:
/home/<username>/.mcp2serial/config.yaml
```
- Use case: personal configuration
- Create the `.mcp2serial` directory:
```bash
  # Windows (in Command Prompt)
  mkdir "%USERPROFILE%\.mcp2serial"
  
  # macOS/Linux
  mkdir -p ~/.mcp2serial
```

#### 3. System-level config (for multi-user environments)
```bash
# Windows (requires admin privileges)
C:\ProgramData\mcp2serial\config.yaml

# macOS/Linux (requires root)
/etc/mcp2serial/config.yaml
```
- Use case: shared multi-user configuration
- Create the directory and set permissions:
```bash
  # Windows (run as administrator)
  mkdir "C:\ProgramData\mcp2serial"
  
  # macOS/Linux (run as root)
  sudo mkdir -p /etc/mcp2serial
  sudo chown root:root /etc/mcp2serial
  sudo chmod 755 /etc/mcp2serial
```

The program searches the locations in the above order and uses the first valid config file it finds. Pick the location that fits your needs:
- Development/testing: use the current directory
- Personal use: use your home directory (recommended)
- Multi-user environments: use a system-level config (ProgramData or /etc)

### Serial config & advanced command config
Add custom commands in `config.yaml`:
By default no real serial port is used; a loopback port is used for demos, so no changes are needed
```yaml
serial:
  # Serial config
  port: LOOP_BACK  # optional; auto-detected if not set. LOOP_BACK enables loopback mode: whatever you send comes back
  baud_rate: 115200  # optional, default 115200
  timeout: 1.0  # optional, default 1.0
  read_timeout: 1.0  # read timeout; raises an error if no response within 1 second
  response_start_string: CMD  # optional, the start string of the serial response, default OK

commands:
  # PWM control command
  set_pwm:
    command: "CMD_PWM {frequency}"  # actual command format sent; the server appends the line ending automatically
    need_parse: false  # no need to parse the response
    prompts:
      - "Set PWM to max"
      - "Set PWM to min"
      - "Set PWM to {value}"
      - "Turn off PWM"
      - "Set PWM to half"
```

Using a real serial port
```yaml
# config.yaml
serial:
  port: COM11  # or auto-detect
  baud_rate: 115200  # optional, default 115200
  timeout: 1.0  # optional, default 1.0
  read_timeout: 1.0  # read timeout; raises an error if no response within 1 second
  response_start_string: OK  # optional, the start string of the serial response, default OK

commands:
  set_pwm:
    command: "PWM {frequency}\n"
    need_parse: false
    prompts:
      - "Set PWM to {value}"
```
Specifying a config file:
For example, to load the Pico config file: Pico_config.yaml
```json
{
    "mcpServers": {
        "mcp2serial": {
            "command": "uvx",
            "args": [
                "mcp2serial",
                "--config",
                "Pico"  // config file name; do not include the _config.yaml suffix
            ]
        }
    }
}
```
To use multiple serial ports, register additional mcp2serial services pointing at different config files.
To connect more than one device, e.g. a second device:
Load the Pico2 config file: Pico2_config.yaml
```json
{
    "mcpServers": {
        "mcp2serial2": {
            "command": "uvx",
            "args": [
                "mcp2serial",
                "--config",
                "Pico2"  // config file name; do not include the _config.yaml suffix
            ]
        }
    }
}
```

### Response parsing

1. Simple responses (`need_parse: false`):
   - A message starting with "OK" from the device means success
   - Other responses are treated as errors

2. Responses needing parsing (`need_parse: true`):
   - The full response is returned in the `result.raw` field
   - You can parse it further at the application layer

### Hardware connection

1. Connect your device to the computer via USB
2. Open Device Manager and note the COM port of your device
3. Configure the correct port and baud rate in `config.yaml`

Hardware connection and COM port configuration

### Start the client - Claude Desktop or Cline

Example in Claude

Example in Cline

### Hardware programming
Firmware can be downloaded from the project repository. Currently a Pico MicroPython code example is provided. Save it onto the Pico board and run it.

### Quick start from source
1. Install from source
```bash
# Install from source:
git clone https://github.com/mcp2everything/mcp2serial.git
cd mcp2serial

# Create a virtual environment
uv venv .venv

# Activate it
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

# Install development dependencies
uv pip install --editable .
```

2. Configure the serial port and commands:
By default no real serial port is used; a loopback port is used for the demo
If your computer has no serial port or none is currently available,
set the port parameter to LOOP_BACK so you can send commands directly from the command line.
In that case also change the response start string so it matches the commands you send.
For example if you send LED_ON,
the response start string should also be LED_ON
```yaml
serial:
  # Serial config
  port: LOOP_BACK  # optional; auto-detected if not set. LOOP_BACK enables loopback mode: whatever you send comes back
  baud_rate: 115200  # optional, default 115200
  timeout: 1.0  # optional, default 1.0
  read_timeout: 1.0  # read timeout; raises an error if no response within 1 second
  response_start_string: CMD  # optional, the start string of the serial response, default OK

commands:
  # PWM control command
  set_pwm:
    command: "CMD_PWM {frequency}"  # actual command format sent; the server appends the line ending automatically
    need_parse: false  # no need to parse the response
    prompts:
      - "Set PWM to max"
      - "Set PWM to min"
      - "Set PWM to {value}"
      - "Turn off PWM"
      - "Set PWM to half"
```

If using a real serial port
```yaml
# config.yaml
serial:
  port: COM11  # or auto-detect
  baud_rate: 115200  # optional, default 115200
  timeout: 1.0  # optional, default 1.0
  read_timeout: 1.0  # read timeout; raises an error if no response within 1 second
  response_start_string: OK  # optional, the start string of the serial response, default OK

commands:
  set_pwm:
    command: "PWM {frequency}\n"
    need_parse: false
    prompts:
      - "Set PWM to {value}"
```

### MCP client configuration

When using an MCP-capable client (e.g. Claude Desktop or Cline), add the following to the client config:
Config for auto-installed setups
Config for source development setups
#### Using the default demo parameters:
```json
{
    "mcpServers": {
        "mcp2serial": {
            "command": "uv",
            "args": [
                "--directory",
                "/your/actual/path/mcp2serial",  // e.g. "C:/Users/Administrator/Documents/develop/my-mcp-server/mcp2serial"
                "run",
                "mcp2serial"
            ]
        }
    }
}
```
#### Specifying a config file name
```json
{
    "mcpServers": {
        "mcp2serial": {
            "command": "uv",
            "args": [
                "--directory",
                "/your/actual/path/mcp2serial",  // e.g. "C:/Users/Administrator/Documents/develop/my-mcp-server/mcp2serial"
                "run",
                "mcp2serial",
                "--config", // optional, specify the config file name
                "Pico"  // optional, config file name; do not include the _config.yaml suffix
            ]
        }
    }
}
```

3. Run the server:
```bash
# Make sure the virtual environment is active
.venv\Scripts\activate

# Run the server (uses the default config.yaml; the example uses the LOOP_BACK loopback port, so no real port or device is needed)
uv run src/mcp2serial/server.py
or
uv run mcp2serial
# Run the server (uses the specified Pico_config.yaml)
uv run src/mcp2serial/server.py --config Pico
or
uv run mcp2serial --config Pico
```

## Documentation

- [Installation guide](https://github.com/mcp2everything/mcp2serial/blob/HEAD/docs/zh/installation.md)
- API docs
- Configuration guide

## Use Cases

1. **Smart home automation**
   - Control lights, fans, and other devices with natural language
   - AI adjusts device parameters automatically based on the environment

2. **Industrial automation**
   - Smart control of production line equipment
   - Real-time monitoring and adjustment of process parameters

3. **Education and research**
   - IoT teaching demos
   - Hardware control experiment platforms

4. **Prototyping**
   - Quickly validate hardware control solutions
   - Simplify the development process

## Project Roadmap

### Phase 1: Protocol expansion
- **Industrial protocol support**
  - MODBUS RTU/TCP
  - OPC UA
  - MQTT
  - CoAP
  - TCP/IP Socket
  
- **Hardware interface expansion**
  - I2C
  - SPI
  - CAN
  - 1-Wire
  - GPIO

### Phase 2: MCP2Anything platform
- **Unified integration platform**
  - Visual configuration UI
  - One-click enablement for each protocol
  - Real-time monitoring dashboard
  - Device management system

- **Smart features**
  - Automatic protocol detection
  - Automatic device discovery
  - Smart parameter optimization
  - Anomaly alerting system

### Phase 3: Ecosystem building
- **Plugin marketplace**
  - Protocol plugins
  - Device drivers
  - Custom feature modules
  - Community contribution integration

- **Cloud service integration**
  - Device cloud management
  - Remote control
  - Data analysis
  - AI training platform

### Phase 4: Industry solutions
- **Vertical domain adaptation**
  - Industrial automation
  - Smart buildings
  - Agricultural IoT
  - Smart cities

- **Custom services**
  - Industry protocol adaptation
  - Professional technical support
  - Solution consulting
  - Training services

## Vision

MCP2Serial is opening a new chapter in IoT:

- **Protocol unification**: Full protocol support via the MCP2Anything platform
- **Plug and play**: One-click configuration, automatic discovery, zero-friction usage
- **AI empowerment**: Deep AI integration for intelligent decision making
- **Open ecosystem**: An active developer community and plugin marketplace

## Roadmap

MCP2Serial is opening a new chapter in IoT:

- **Multi-protocol support**: Plans to support more communication protocols (I2C, SPI, etc.)
- **Device ecosystem**: Building an open device support ecosystem
- **AI enhancement**: Integrating more AI capabilities for smarter control logic
- **Visualization**: Developing intuitive monitoring and configuration interfaces

## Related Resources

- [MCP protocol spec](https://modelcontextprotocol.io/)
- Project docs
- Example code
- FAQ

## Contributing

We welcome all forms of contribution, whether new features, documentation improvements, or bug reports. See the contribution guide for more information.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/mcp2everything/mcp2serial/blob/HEAD/LICENSE) file

**Official site: ** [https://github.com/mcp2everything/mcp2serial](https://github.com/mcp2everything/mcp2serial)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `home automation and iot`, `os automation`, `developer tools`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `mcp2serial`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/mcp2everything-mcp2serial.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
