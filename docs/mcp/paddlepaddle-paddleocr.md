---
title: "PaddleOCR MCP 服务器"
description: "PaddleOCR MCP服务器 概述 PaddleOCR MCP服务器为AI应用提供工业级OCR和文档解析能力。基于PaddleOCR——一个经过5万+GitHub star验证，被MinerU、RAGFlow、OmniParser等头部项目深度集成的成熟解决方案，并基于MCP理念做了针对性的优化。 官方文档：https://paddlepaddle.github.io/PaddleOCR/latest/version3.x/deployment/mcpserver.html PaddleOCR GitHub仓库"
---

# PaddleOCR MCP 服务器

PaddleOCR MCP服务器 概述 PaddleOCR MCP服务器为AI应用提供工业级OCR和文档解析能力。基于PaddleOCR——一个经过5万+GitHub star验证，被MinerU、RAGFlow、OmniParser等头部项目深度集成的成熟解决方案，并基于MCP理念做了针对性的优化。 官方文档：https://paddlepaddle.github.io/PaddleOCR/latest/version3.x/deployment/mcpserver.html PaddleOCR GitHub仓库

# PaddleOCR MCP服务器
## 概述
PaddleOCR MCP服务器为AI应用提供工业级OCR和文档解析能力。基于PaddleOCR——一个经过5万+GitHub star验证，被MinerU、RAGFlow、OmniParser等头部项目深度集成的成熟解决方案，并基于MCP理念做了针对性的优化。

* **官方文档**：[https://paddlepaddle.github.io/PaddleOCR/latest/version3.x/deployment/mcp_server.html](https://paddlepaddle.github.io/PaddleOCR/latest/version3.x/deployment/mcp_server.html)
* **PaddleOCR GitHub仓库**：[https://github.com/PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)
* **PaddleOCR产线功能在线体验：**
    * [PaddleOCR官网](https://aistudio.baidu.com/paddleocr)

    * ModelScope 魔搭社区
        * [PP-OCRv5](https://modelscope.cn/studios/PaddlePaddle/PP-OCRv5_Online_Demo)
        * [PP-StructureV3](https://modelscope.cn/studios/PaddlePaddle/PP-StructureV3_Online_Demo)
        * [PaddleOCR-VL](https://modelscope.cn/studios/PaddlePaddle/PaddleOCR-VL_Online_Demo)

## 核心功能
### 文字识别（基于PP-OCRv5）
* **多语言支持**：支持中英日韩等37种语言，支持印刷体、手写体识别
* **高精度识别**：识别精度达到开源方案领先水平
* **结构化输出**：返回包含文字坐标和内容的JSON数据

### 文档解析（基于PP-StructureV3） & 大模型文档解析（基于PaddleOCR-VL）
* **版面智能分析**：识别文本块、标题、段落、图片、表格等版面元素
* **结构化转换**：将PDF和图像转换为保留原始结构的Markdown格式
* **复杂文档处理**：处理含有复杂表格、公式、手写文字的文档

### MCP优化
* **智能输出模式**：
    * `simple`模式包含识别到的文本/Markdown内容等关键信息
    * `detailed`模式包含边界框坐标等详细信息

* **PP-OCRv5**：两种输出模式均包含置信度和统计信息，帮助agent评估结果质量
* **PP-StructureV3和PaddleOCR-VL**：两种输出模式均支持图文混合输出，保留图片原始位置信息

## 部署模式
### 工作模式
* **本地Python库**：直接在本地运行PaddleOCR模型
* **PaddleOCR官网服务**：调用PaddleOCR官网提供的云服务
* **自托管服务**：连接自托管的PaddleOCR服务

### 传输机制
* **stdio**：适用于本地集成的标准输入输出模式
* **Streamable HTTP**：支持远程调用的可流式HTTP传输

## 在ModelScope上部署远程服务
1. 在[PaddleOCR官网](https://aistudio.baidu.com/paddleocr/task)点击左上角的“API”，在希望使用的功能对应的代码调用示例中复制服务基础URL（`API_URL`去除`/ocr`等端点后缀）与访问令牌（`TOKEN`）。
2. 在本页面右侧配置`PADDLEOCR_MCP_AISTUDIO_ACCESS_TOKEN`和`PADDLEOCR_MCP_SERVER_URL`，分别设置为上一步骤获取到的访问令牌与服务基础URL。将`PADDLEOCR_MCP_PIPELINE`设置为产线名称（`OCR`、`PP-StructureV3`或`PaddleOCR-VL`）：

    | 功能 | `PADDLEOCR_MCP_PIPELINE` |
    | - | - |
    | 文字识别（PP-OCRv5） | `OCR` |
    | 文档解析（PP-StructureV3） | `PP-StructureV3` |
    | 大模型文档解析（PaddleOCR-VL） | `PaddleOCR-VL` |

3. 点击“连接”，启动服务，之后可在Claude for Desktop、Cherry Studio等MCP host中使用。

## 典型应用场景
### 文档数字化
* 提取手写笔记的内容，并存储到笔记软件中
* 将图片/PDF文档转换为可用Word/Excel编辑的格式

### 开发工作流
* 手写思路/伪代码转换为可运行脚本
* 将文档图片快速转换为Markdown格式的项目文档

## 技术优势
* **成熟稳定**：经过大量生产环境验证的工业级OCR方案
* **精度领先**：OCR、文档解析等在公开评测中超越众多商业方案
* **易于集成**：部署步骤简单，几分钟完成集成
* **成本可控**：支持本地部署，避免数据外传和API调用费用

---

**开始使用PaddleOCR MCP服务器，让您的AI应用具备工业级文档理解能力。**

**官方网站：** [https://github.com/PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`--from paddleocr-mcp paddleocr_mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/paddlepaddle-paddleocr.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
