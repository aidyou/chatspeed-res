---
title: "代码知识记忆库工具"
description: "通过向量嵌入技术，为项目提供记忆库和RAG上下文支持，以增强代码理解和管理，并与RooCode和Cline集成。"
---

# 代码知识记忆库工具

通过向量嵌入技术，为项目提供记忆库和RAG上下文支持，以增强代码理解和管理，并与RooCode和Cline集成。

# 代码知识工具

一个使用向量嵌入技术的代码仓库知识管理工具。该工具利用先进的嵌入技术帮助维护和查询关于您的代码库的知识。

## 构建与安装

### 1. 构建包

首先，您需要构建分发文件：

```bash
# Clone the repository
git clone https://github.com/yourusername/code-knowledge-tool.git
cd code-knowledge-tool

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate

# Install build tools
python -m pip install --upgrade pip build

# Build the package
python -m build
```

这将在 `dist/` 目录中创建两个文件：
- code_knowledge_tool-0.1.0-py3-none-any.whl (用于安装的 wheel 文件)
- code_knowledge_tool-0.1.0.tar.gz (源码分发)

### 2. 安装包

#### 先决条件

1. 确保 Ollama 已安装并正在运行：
```bash
# Install Ollama (if not already installed)
curl https://ollama.ai/install.sh | sh

# Start Ollama service
ollama serve
```

2. 安装包：

##### 选项 1：从 wheel 文件安装（推荐用于使用）

```bash
# Navigate to where you built the package
cd /path/to/code_knowledge_tool

# Install from the wheel file
pip install dist/code_knowledge_tool-0.1.0-py3-none-any.whl
```

##### 选项 2：以可编辑模式安装（推荐用于开发）

如果您希望修改工具或为其开发做出贡献，这个选项是最好的：

```bash
# Assuming you're already in the code-knowledge-tool directory
# and have activated your virtual environment

# Install in editable mode with development dependencies
pip install -e ".[dev]"
```

## 与 RooCode/Cline 集成

1. 将 MCP 配置复制到您的设置中：

对于 Cline (VSCode)：
```bash
# Open the settings file
open ~/Library/Application\ Support/Code/User/globalStorage/rooveterinaryinc.roo-cline/settings/cline_mcp_settings.json
```

添加此配置：
```json
{
  "mcpServers": {
    "code_knowledge": {
      "command": "python",
      "args": ["-m", "code_knowledge_tool.mcp_tool"],
      "env": {
        "PYTHONPATH": "${workspaceFolder}"
      }
    }
  }
}
```

对于 RooCode：
```bash
# Open the settings file
open ~/Library/Application\ Support/RooCode/roocode_config.json
```
添加与上面相同的配置。

2. 重启 RooCode/Cline 以加载新工具。

## 作为记忆库和 RAG 上下文提供者使用

此工具可以充当您项目的记忆库和 RAG 上下文提供者。要进行设置，请执行以下步骤：

1. 将提供的模板复制到您的项目中：
```bash
cp clinerules_template.md /path/to/your/project/.clinerules
```

2. 根据您项目的需求自定义 .clinerules 中的规则和模式

模板包括有关以下内容的全面说明：
- 知识库管理
- 基于 RAG 的开发工作流程
- 代码质量指南
- 记忆管理实践

详见 clinerules_template.md 获取完整的配置和使用详情。

## 特性

- 本地向量存储用于代码知识
- 使用 Ollama 高效生成嵌入
- 支持多种文件类型
- 上下文感知的代码理解
- 通过 MCP 与 RooCode 和 Cline 集成
- 基于 RAG 的上下文增强
- 持久化的知识存储

## 要求

- Python 3.8 或更高版本
- 本地运行的 Ollama 服务
- chromadb 用于向量操作

## 开发

### 运行测试

该项目遵循以集成测试为主的测试方法，侧重于端到端功能和 MCP 合约一致性。测试套件包括：

1. MCP 合约测试
   - 工具注册与执行
   - 资源管理
   - 知识操作
   - 错误处理

2. 包构建测试
   - 安装验证
   - 依赖解析
   - MCP 服务器初始化
   - 基本功能

要运行测试：
```bash
# Install test dependencies
pip install -e ".[dev]"

# Run all tests
pytest

# Run specific test suites
pytest tests/integration/test_mcp_contract.py -v  # MCP functionality
pytest tests/integration/test_package_build.py -v  # Installation verification
```

测试环境要求：
```bash
# Ensure Ollama is running
ollama serve
```

测试使用临时目录 (test_knowledge_store)，该目录在每次测试运行之间自动清理。

有关测试策略和模式的更多详细信息，请参阅 `docs/` 中的文档。

## 未来的分发

如果您希望通过 pip 提供此包（即 `pip install code-knowledge-tool`），则需要：

1. 在 [PyPI](https://pypi.org) 上注册一个账号
2. 安装 twine: `pip install twine`
3. 上传你的发行版: `twine upload dist/*`

不过，目前请使用上述描述的本地构建和安装方法。

## 许可证

MIT 许可证

**官方网站：** [https://github.com/davidvc/code-knowledge-mcptool](https://github.com/davidvc/code-knowledge-mcptool)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`, `memory`
- 标签：`knowledge and memory`, `developer tools`, `search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`python`
- 参数：`-m code_knowledge_tool.mcp_tool`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/davidvc-code-knowledge-mcptool.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
