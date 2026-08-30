---
title: "知识库MCP服务"
description: "一个便携式、本地化、简单便捷的MCP服务器，用于支持txtai“一体化”嵌入式数据库的语义/图谱检索。任何以tar.gz形式存在的txtai嵌入式数据库都可以被加载。"
---

# 知识库MCP服务

一个便携式、本地化、简单便捷的MCP服务器，用于支持txtai“一体化”嵌入式数据库的语义/图谱检索。任何以tar.gz形式存在的txtai嵌入式数据库都可以被加载。

# 嵌入 MCP 服务器

这是一个由 txtai 提供支持的模型上下文协议 (MCP) 服务器实现，通过标准化接口提供语义搜索、知识图谱功能和 AI 驱动的文本处理。

## txtai 的强大功能：一体化嵌入数据库

该项目利用 [txtai](https://github.com/neuml/txtai)，这是一个用于 RAG 的一体化嵌入数据库，它利用了语义搜索、知识图谱构建和语言模型工作流。txtai 提供了几个关键优势：

- **统一向量数据库**：在一个平台上结合了向量索引、图网络和关系数据库
- **语义搜索**：根据含义而不是仅仅基于关键词来查找信息
- **知识图谱集成**：自动从数据中构建和查询知识图谱
- **便携式知识库**：将整个知识库存储为压缩归档文件（.tar.gz），可以轻松共享和加载
- **可扩展管道系统**：通过统一 API 处理文本、文档、音频、图像和视频
- **本地优先架构**：无需将数据发送到外部服务即可在本地运行所有内容

## 工作原理

该项目包含一个知识库构建工具和一个 MCP 服务器。知识库构建工具是一个用于创建和管理知识库的命令行界面。MCP 服务器提供了访问知识库的标准化接口。

不需要使用知识库构建工具来构建知识库。您始终可以通过编写 Python 脚本甚至使用 jupyter 笔记本来使用 txtai 的编程接口构建知识库。只要知识库是使用 txtai 构建的，就可以被 MCP 服务器加载。更好的是，知识库可以是文件系统上的一个文件夹或导出的 .tar.gz 文件。只需将其提供给 MCP 服务器，它就会加载它。

### 1. 使用 kb_builder 构建知识库

`kb_builder` 模块提供了一个用于创建和管理知识库的命令行界面：

- 从各种来源（文件、目录、JSON）处理文档
- 提取文本并创建嵌入
- 自动构建知识图谱
- 导出便携式知识库

请注意，它的功能可能有限，目前仅出于方便而提供。

### 2. 启动 MCP 服务器

MCP 服务器提供了访问知识库的标准化接口：

- 语义搜索能力
- 知识图谱查询和可视化
- 文本处理管道（摘要、提取等）
- 完全符合模型上下文协议

## 安装

### 推荐：使用 uv 和 Python 3.10+

我们推荐使用 [uv](https://github.com/astral-sh/uv) 并配合 Python 3.10 或更新版本以获得最佳体验。这提供了更好的依赖项管理和一致的行为保证。

```bash
# Install uv if you don't have it already
pip install -U uv

# Create a virtual environment with Python 3.10 or newer
uv venv --python=3.10  # or 3.11, 3.12, etc.

# Activate the virtual environment (bash/zsh)
source .venv/bin/activate
# For fish shell
# source .venv/bin/activate.fish

# Install from PyPI
uv pip install kb-mcp-server
```

> **注意**：我们将 transformers 固定在 4.49.0 版本，以避免在 4.50.0 及更高版本中出现关于 `transformers.agents.tools` 的弃用警告。如果你使用的是更新版本的 transformers，你可能会看到这些警告，但它们不会影响功能。

### 使用 conda

```bash
# Create a new conda environment (optional)
conda create -n embedding-mcp python=3.10
conda activate embedding-mcp

# Install from PyPI
pip install kb-mcp-server
```

### 从源代码安装

```bash
# Create a new conda environment
conda create -n embedding-mcp python=3.10
conda activate embedding-mcp

# Clone the repository
git clone https://github.com/Geeksfino/kb-mcp-server.git.git
cd kb-mcp-server

# Install dependencies
pip install -e .
```

### 使用 uv（更快的替代方案）

```bash
# Install uv if not already installed
pip install uv

# Create a new virtual environment
uv venv
source .venv/bin/activate

# Option 1: Install from PyPI
uv pip install kb-mcp-server

# Option 2: Install from source (for development)
uv pip install -e .
```

### 使用 uvx（无需安装）

[uvx](https://github.com/astral-sh/uv) 允许你直接从 PyPI 运行包而无需安装它们：

```bash
# Run the MCP server
uvx --from kb-mcp-server@0.3.0 kb-mcp-server --embeddings /path/to/knowledge_base

# Build a knowledge base
uvx --from kb-mcp-server@0.3.0 kb-build --input /path/to/documents --config config.yml

# Search a knowledge base
uvx --from kb-mcp-server@0.3.0 kb-search /path/to/knowledge_base "Your search query"
```

## 命令行使用

### 构建知识库

你可以使用从 PyPI 安装的命令行工具、Python 模块直接或方便的 shell 脚本：

#### 使用从 PyPI 安装的命令

```bash
# Build a knowledge base from documents
kb-build --input /path/to/documents --config config.yml

# Update an existing knowledge base with new documents
kb-build --input /path/to/new_documents --update

# Export a knowledge base for portability
kb-build --input /path/to/documents --export my_knowledge_base.tar.gz

# Search a knowledge base
kb-search /path/to/knowledge_base "What is machine learning?"

# Search with graph enhancement
kb-search /path/to/knowledge_base "What is machine learning?" --graph --limit 10
```

#### 使用 uvx（无需安装）

```bash
# Build a knowledge base from documents
uvx --from kb-mcp-server@0.3.0 kb-build --input /path/to/documents --config config.yml

# Update an existing knowledge base with new documents
uvx --from kb-mcp-server@0.3.0 kb-build --input /path/to/new_documents --update

# Export a knowledge base for portability
uvx --from kb-mcp-server@0.3.0 kb-build --input /path/to/documents --export my_knowledge_base.tar.gz

# Search a knowledge base
uvx --from kb-mcp-server@0.3.0 kb-search /path/to/knowledge_base "What is machine learning?"

# Search with graph enhancement
uvx --from kb-mcp-server@0.3.0 kb-search /path/to/knowledge_base "What is machine learning?" --graph --limit 10
```

#### 使用 Python 模块

```bash
# Build a knowledge base from documents
python -m kb_builder build --input /path/to/documents --config config.yml

# Update an existing knowledge base with new documents
python -m kb_builder build --input /path/to/new_documents --update

# Export a knowledge base for portability
python -m kb_builder build --input /path/to/documents --export my_knowledge_base.tar.gz
```

#### 使用便捷脚本

仓库包括了便捷的包装脚本，使构建和搜索知识库更加容易：

```bash
# Build a knowledge base using a template configuration
./scripts/kb_build.sh /path/to/documents technical_docs

# Build using a custom configuration file
./scripts/kb_build.sh /path/to/documents /path/to/my_config.yml

# Update an existing knowledge base
./scripts/kb_build.sh /path/to/documents technical_docs --update

# Search a knowledge base
./scripts/kb_search.sh /path/to/knowledge_base "What is machine learning?"

# Search with graph enhancement
./scripts/kb_search.sh /path/to/knowledge_base "What is machine learning?" --graph
```

运行 `./scripts/kb_build.sh --help` 或 `./scripts/kb_search.sh --help` 获取更多选项。

### 启动 MCP 服务器

#### 使用从 PyPI 安装的命令

```bash
# Start with a specific knowledge base folder
kb-mcp-server --embeddings /path/to/knowledge_base_folder

# Start with a given knowledge base archive
kb-mcp-server --embeddings /path/to/knowledge_base.tar.gz
```

#### 使用 uvx（无需安装）

```bash
# Start with a specific knowledge base folder
uvx kb-mcp-server@0.2.6 --embeddings /path/to/knowledge_base_folder

# Start with a given knowledge base archive
uvx kb-mcp-server@0.2.6 --embeddings /path/to/knowledge_base.tar.gz
```

#### 使用 Python 模块

```bash
# Start with a specific knowledge base folder
python -m txtai_mcp_server --embeddings /path/to/knowledge_base_folder

# Start with a given knowledge base archive
python -m txtai_mcp_server --embeddings /path/to/knowledge_base.tar.gz
```

## MCP 服务器配置

MCP 服务器通过环境变量或命令行参数进行配置，而不是 YAML 文件。YAML 文件仅用于在构建知识库时配置 txtai 组件。

以下是配置 MCP 服务器的方法：

```bash
# Start the server with command-line arguments
kb-mcp-server --embeddings /path/to/knowledge_base --host 0.0.0.0 --port 8000

# Or using uvx (no installation required)
uvx kb-mcp-server@0.2.6 --embeddings /path/to/knowledge_base --host 0.0.0.0 --port 8000

# Or using the Python module
python -m txtai_mcp_server --embeddings /path/to/knowledge_base --host 0.0.0.0 --port 8000

# Or use environment variables
export TXTAI_EMBEDDINGS=/path/to/knowledge_base
export MCP_SSE_HOST=0.0.0.0
export MCP_SSE_PORT=8000
python -m txtai_mcp_server
```

常见的配置选项：
- `--embeddings`：知识库路径（必需）
- `--host`：绑定到的主机地址（默认：localhost）
- `--port`：监听端口（默认：8000）
- `--transport`：使用的传输方式，可以是 'sse' 或 'stdio'（默认：stdio）
- `--enable-causal-boost`：启用因果增强功能以提高相关性评分
- `--causal-config`：自定义因果增强配置的 YAML 文件路径

## 配置 LLM 客户端以使用 MCP 服务器

要配置一个 LLM 客户端以使用 MCP 服务器，你需要创建一个 MCP 配置文件。以下是一个示例 `mcp_config.json`：

### 直接使用服务器

如果你使用虚拟 Python 环境来安装服务器，你可以使用以下配置 - 请注意，像 Claude 这样的 MCP 主机如果使用虚拟环境将无法连接到服务器，你需要使用虚拟环境中执行 "pip install" 或 "uv pip install" 的 Python 可执行文件的绝对路径，例如

```json
{
  "mcpServers": {
    "kb-server": {
      "command": "/your/home/project/.venv/bin/kb-mcp-server",
      "args": [
        "--embeddings", 
        "/path/to/knowledge_base.tar.gz"
      ],
      "cwd": "/path/to/working/directory"
    }
  }
}
```

### 使用系统默认 Python

如果你使用系统默认的 Python，你可以使用以下配置：

```json
{
    "rag-server": {
      "command": "python3",
      "args": [
        "-m",
        "txtai_mcp_server",
        "--embeddings",
        "/path/to/knowledge_base.tar.gz",
        "--enable-causal-boost"
      ],
      "cwd": "/path/to/working/directory"
    }
}
```

或者，如果你正在使用 uvx，假设你已经通过 "brew install uvx" 等方式在系统中安装了 uvx，或者你已经安装了 uvx 并使其全局可访问，例如：

```
# Create a symlink to /usr/local/bin (which is typically in the system PATH)
sudo ln -s /Users/cliang/.local/bin/uvx /usr/local/bin/uvx
```

这会从您的用户特定安装创建一个符号链接到系统范围的位置。对于像 Claude Desktop 这样的 macOS 应用程序，您可以通过创建或编辑 launchd 配置文件来修改系统范围的 PATH：
```
# Create a plist file to set environment variables for all GUI applications
sudo nano /Library/LaunchAgents/environment.plist
```
添加以下内容：

```xml

  Label
  my.startup
  ProgramArguments
  

    sh
    -c
    launchctl setenv PATH $PATH:/Users/cliang/.local/bin
  

  RunAtLoad
  

```

然后加载它：
```
sudo launchctl load -w /Library/LaunchAgents/environment.plist
```
不过，您需要重启计算机才能使更改生效。

```json
{
  "mcpServers": {
    "kb-server": {
      "command": "uvx",
      "args": [
        "kb-mcp-server@0.2.6",
        "--embeddings", "/path/to/knowledge_base",
        "--host", "localhost",
        "--port", "8000"
      ],
      "cwd": "/path/to/working/directory"
    }
  }
}
```

将此配置文件放置在您的 LLM 客户端可以访问的位置，并配置客户端使用它。具体的配置步骤将取决于您的具体 LLM 客户端。

## 高级知识库配置

使用 txtai 构建知识库需要一个 YAML 配置文件，该文件控制嵌入过程的各个方面。此配置由 `kb_builder` 工具使用，而不是 MCP 服务器本身。

可能需要调整分段/切块策略、嵌入模型和评分方法，以及配置图构建、因果增强、混合搜索的权重等。

幸运的是，txtai 提供了一个强大的 YAML 配置系统，无需编码。这里是一个全面的知识库构建配置示例：

```yaml
# Path to save/load embeddings index
path: ~/.txtai/embeddings
writable: true

# Content storage in SQLite
content:
  path: sqlite:///~/.txtai/content.db

# Embeddings configuration
embeddings:
  # Model settings
  path: sentence-transformers/nli-mpnet-base-v2
  backend: faiss
  gpu: true
  batch: 32
  normalize: true
  
  # Scoring settings
  scoring: hybrid
  hybridalpha: 0.75

# Pipeline configuration
pipeline:
  workers: 2
  queue: 100
  timeout: 300

# Question-answering pipeline
extractor:
  path: distilbert-base-cased-distilled-squad
  maxlength: 512
  minscore: 0.3

# Graph configuration
graph:
  backend: sqlite
  path: ~/.txtai/graph.db
  similarity: 0.75  # Threshold for creating graph connections
  limit: 10  # Maximum connections per node
```

### 配置示例

`src/kb_builder/configs` 目录包含适用于不同用例和存储后端的配置模板：

#### 存储和后端配置
- `memory.yml`: 内存向量（开发时最快，无持久性）
- `sqlite-faiss.yml`: SQLite 用于内容 + FAISS 用于向量（基于本地文件的持久性）
- `postgres-pgvector.yml`: PostgreSQL + pgvector（生产就绪，完全持久性）

#### 领域特定配置
- `base.yml`: 基础配置模板
- `code_repositories.yml`: 优化于代码仓库
- `data_science.yml`: 针对数据科学文档配置
- `general_knowledge.yml`: 通用知识库
- `research_papers.yml`: 优化于学术论文
- `technical_docs.yml`: 针对技术文档配置

您可以将这些作为自己配置的起点：

```bash
python -m kb_builder build --input /path/to/documents --config src/kb_builder/configs/technical_docs.yml

# Or use a storage-specific configuration
python -m kb_builder build --input /path/to/documents --config src/kb_builder/configs/postgres-pgvector.yml
```

## 高级功能

### 知识图谱能力

MCP 服务器利用 txtai 的内置图功能提供强大的知识图谱能力：

- **自动图构建**: 自动从您的文档中构建知识图谱
- **图遍历**: 导航相关概念和文档
- **路径查找**: 发现不同信息片段之间的连接
- **社区检测**: 识别相关信息的集群

### 因果增强机制

MCP 服务器包括一种复杂的因果增强机制，通过识别和优先处理因果关系来提高搜索相关性：

- **模式识别**：在查询和文档中检测因果语言模式
- **多语言支持**：根据检测到的查询语言自动应用适当的模式
- **可配置的提升倍数**：不同类型的因果匹配可以接收自定义的提升因子
- **增强的相关性**：解释因果关系的结果在搜索结果中被优先考虑

此机制通过呈现解释概念之间关系的内容，显著提高了对“为什么”和“如何”问题的回答质量。因果提升配置通过 YAML 文件高度可定制，允许适应不同的领域和语言。

## 许可证

MIT 许可证 - 详情请参阅 LICENSE 文件

**官方网站：** [https://github.com/Geeksfino/kb-mcp-server](https://github.com/Geeksfino/kb-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`, `memory`, `data`
- 标签：`knowledge and memory`, `search`, `research and data`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`kb-mcp-server@0.2.6 --embeddings /path/to/knowledge_base --host localhost --port 8000`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/geeksfino-kb.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
