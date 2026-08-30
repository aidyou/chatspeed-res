---
title: "深度搜索推理增强服务"
description: "通过集成DeepSeek R1的高级推理引擎以处理复杂推理任务，从而增强Claude推理能力的服务器。"
---

# 深度搜索推理增强服务

通过集成DeepSeek R1的高级推理引擎以处理复杂推理任务，从而增强Claude推理能力的服务器。

# 🧠 DeepSeek MCP Server

## 🚀 特性

**通过集成DeepSeek R1的高级推理引擎来增强Claude的推理能力。** 该服务器使Claude能够利用deepseek r1模型的推理能力处理复杂的推理任务。

- DeepSeek R1（大脑）充当高级推理规划器：

   - 规划多步骤逻辑分析策略
   - 构建认知框架
   - 评估信心和不确定性
   - 监控推理质量
   - 检测边缘情况和偏见

- Claude（执行者）实施推理计划：

   - 执行结构化分析
   - 实施计划策略
   - 提供最终响应
   - 处理用户交互
   - 管理系统集成

---

## 🚀 特性

### **高级推理能力**
- 支持复杂的多步骤推理任务。
- 为生成深思熟虑的响应而设计，注重精确性和效率。
- 使用无问芯穹的API

---

## 完整设置指南

### 前提条件
- Python 3.12 或更高版本
- `uv` 包管理器
- 用于DeepSeek的INFINI_API_KEY（在[无问芯穹](https://cloud.infini-ai.com/genstudio/model)注册）

1. **克隆仓库**
```bash
   git clone https://github.com/moyu6027/deepseek-MCP-server.git
   cd deepseek-MCP-server
```

2. **确保UV已设置**
   - **Windows**: 在PowerShell中运行以下命令：
```powershell
     powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
   - **Mac**: 运行以下命令：
```bash
     curl -LsSf https://astral.sh/uv/install.sh | sh
```

3. **创建虚拟环境**
```bash
   uv venv
   source .venv/bin/activate
```

4. **安装依赖项**
```bash
   uv add "mcp[cli]" httpx
```

5. **设置API密钥**
```bash
   echo "INFINI_API_KEY=your_key_here" > .env
```

6. **安装服务器**
```bash
   mcp install server.py -f .env
```

7. **配置MCP服务器**
   编辑`claude_desktop_config.json`文件以包含以下配置：

```json
   {
       "mcpServers": {
           "deepseek-mcp": {
               "command": "uv",
               "args": [
                   "--directory",
                   "PATH_TO_DEEPSEEK_MCP_SERVER",
                   "run",
                   "server.py"
               ]
           }
       }
   }
```

8. **运行服务器**
```bash
   uv run server.py
```

---

## 🛠 使用方法

### 启动服务器
当与Claude Desktop一起使用时，服务器会自动启动。请确保Claude Desktop已配置为检测MCP服务器。

### 示例工作流程
1. Claude接收到需要高级推理的查询。
2. 查询被转发给DeepSeek R1进行处理。
3. DeepSeek R1返回用`
`标签包裹的结构化推理。
4. Claude将推理整合到其最终响应中。

---

## 📄 许可证

本项目采用 MIT 许可证。详情请参阅 [LICENSE](https://github.com/moyu6027/deepseek-MCP-server/blob/HEAD/LICENSE) 文件。

---

**官方网站：** [https://github.com/moyu6027/deepseek-MCP-server](https://github.com/moyu6027/deepseek-MCP-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`memory`
- 标签：`knowledge and memory`, `developer tools`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`--directory PATH_TO_DEEPSEEK_MCP_SERVER run server.py`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/moyu6027-deepseek.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
