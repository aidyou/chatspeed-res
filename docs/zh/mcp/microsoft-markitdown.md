---
title: "MarkItDown"
description: "MarkItDown 是一款轻量级的 Python 工具，可以将各种文件转换为 Markdown 格式，适用于与 LLMs 及相关文本分析流程配合使用。与 textract 类似，它更专注于保留文档的重要结构和内容作为 Markdown（包括：标题、列表、表格、链接等）。尽管输出通常易于阅读且适合人类阅读，但其主要面向文本分析工具，可能不是为人类阅读而进行高保真文档转换的最佳选择。"
---

# MarkItDown

MarkItDown 是一款轻量级的 Python 工具，可以将各种文件转换为 Markdown 格式，适用于与 LLMs 及相关文本分析流程配合使用。与 textract 类似，它更专注于保留文档的重要结构和内容作为 Markdown（包括：标题、列表、表格、链接等）。尽管输出通常易于阅读且适合人类阅读，但其主要面向文本分析工具，可能不是为人类阅读而进行高保真文档转换的最佳选择。

# MarkItDown

[![PyPI](/mcp-assets/ddcb88f3a372521b16dbb58ca4810e31.svg)](https://pypi.org/project/markitdown/)
![PyPI - Downloads](/mcp-assets/cc98ab83910950e85d58a143b19dc7e2.svg)
[![Built by AutoGen Team](/mcp-assets/3f999ffa00ebf8811c637220f2adf83c.svg)](https://github.com/microsoft/autogen)

> [!TIP]
> MarkItDown 现在提供了一个 MCP（模型上下文协议）服务器，用于与 Claude Desktop 等 LLM 应用程序集成。更多信息请参见 [markitdown-mcp](https://github.com/microsoft/markitdown/tree/main/packages/markitdown-mcp)。

> [!IMPORTANT]
> 从 0.0.1 到 0.1.0 的重大变更：
> * 依赖项现在被组织成可选的功能组（详情见下文）。使用 `pip install 'markitdown[all]'` 可以保持向后兼容的行为。
> * `convert_stream()` 现在需要一个二进制文件对象（例如，以二进制模式打开的文件或 `io.BytesIO` 对象）。这是一个重大变更，之前的版本还接受文本文件对象，如 `io.StringIO`。
> * `DocumentConverter` 类接口已更改为从文件流中读取而不是文件路径。*不再创建临时文件*。如果您是插件或自定义 `DocumentConverter` 的维护者，可能需要更新您的代码。否则，如果您仅使用 `MarkItDown` 类或 CLI（如这些示例所示），则无需更改任何内容。

MarkItDown 是一个轻量级的 Python 工具，用于将各种文件转换为 Markdown，以便在 LLM 和相关文本分析管道中使用。在这方面，它最类似于 [textract](https://github.com/deanmalmgren/textract)，但重点是保留重要的文档结构和内容作为 Markdown（包括：标题、列表、表格、链接等）。虽然输出通常具有合理的可读性和人类友好性，但它主要设计为由文本分析工具消费——可能不是高保真文档转换的最佳选择，尤其是用于人类阅读的文档。

目前，MarkItDown 支持以下文件类型：

- PDF
- PowerPoint
- Word
- Excel
- 图像（EXIF 元数据和 OCR）
- 音频（EXIF 元数据和语音转录）
- HTML
- 基于文本的格式（CSV、JSON、XML）
- ZIP 文件（遍历内容）
- YouTube URL
- EPub
- ……更多！

## 为什么选择 Markdown？

Markdown 非常接近纯文本，具有最少的标记或格式，但仍能表示重要的文档结构。主流的 LLM，如 OpenAI 的 GPT-4，天然“支持”Markdown，并且经常在未提示的情况下将其纳入响应中。这表明它们已经接受了大量 Markdown 格式的文本训练，并且理解得很好。作为附带的好处，Markdown 规范也非常高效地利用了令牌。

## 安装

要安装 MarkItDown，请使用 pip：`pip install 'markitdown[all]'`。或者，您可以从源代码安装：

```bash
git clone git@github.com:microsoft/markitdown.git
cd markitdown
pip install -e 'packages/markitdown[all]'
```

## 使用方法

### 命令行

```bash
markitdown path-to-file.pdf > document.md
```

或者使用 `-o` 指定输出文件：

```bash
markitdown path-to-file.pdf -o document.md
```

您还可以通过管道传递内容：

```bash
cat path-to-file.pdf | markitdown
```

### 可选依赖项
MarkItDown 有一些可选依赖项，用于激活各种文件格式。在本文档的前面部分，我们使用 `[all]` 选项安装了所有可选依赖项。然而，您也可以单独安装它们以获得更多的控制。例如：

bash
pip install 'markitdown[pdf, docx, pptx]'

将仅安装 PDF、DOCX 和 PPTX 文件的依赖项。

目前，以下可选依赖项可用：

* `[all]` 安装所有可选依赖项
* `[pptx]` 安装 PowerPoint 文件的依赖项
* `[docx]` 安装 Word 文件的依赖项
* `[xlsx]` 安装 Excel 文件的依赖项
* `[xls]` 安装旧版 Excel 文件的依赖项
* `[pdf]` 安装 PDF 文件的依赖项
* `[outlook]` 安装 Outlook 消息的依赖项
* `[az-doc-intel]` 安装 Azure 文档智能的依赖项
* `[audio-transcription]` 安装 WAV 和 MP3 文件音频转录的依赖项
* `[youtube-transcription]` 安装获取 YouTube 视频转录的依赖项

### 插件

MarkItDown 还支持第三方插件。插件默认是禁用的。要列出已安装的插件：

```bash
markitdown --list-plugins
```

要启用插件，请使用：

```bash
markitdown --use-plugins path-to-file.pdf
```

要查找可用的插件，可以在 GitHub 上搜索标签 `#markitdown-plugin`。要开发插件，请参阅 `packages/markitdown-sample-plugin`。

### Azure 文档智能

要使用 Microsoft 文档智能进行转换：

```bash
markitdown path-to-file.pdf -o document.md -d -e ""
```

有关如何设置 Azure 文档智能资源的更多信息，请参阅 [这里](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/how-to-guides/create-document-intelligence-resource?view=doc-intel-4.0.0)

### Python API

Python 中的基本用法：

```python
from markitdown import MarkItDown

md = MarkItDown(enable_plugins=False) # 设置为 True 以启用插件
result = md.convert("test.xlsx")
print(result.text_content)
```

Python 中的文档智能转换：

```python
from markitdown import MarkItDown

md = MarkItDown(docintel_endpoint="")
result = md.convert("test.pdf")
print(result.text_content)
```

要使用大型语言模型进行图像描述，请提供 `llm_client` 和 `llm_model`：

```python
from markitdown import MarkItDown
from openai import OpenAI

client = OpenAI()
md = MarkItDown(llm_client=client, llm_model="gpt-4o")
result = md.convert("example.jpg")
print(result.text_content)
```

### Docker

```sh
docker build -t markitdown:latest .
docker run --rm -i markitdown:latest  output.md
```
## 贡献

本项目欢迎贡献和建议。大多数贡献需要您签署一份
贡献者许可协议（CLA），声明您有权并且确实授予我们使用您的贡献的权利。详情请访问 https://cla.opensource.microsoft.com。

当您提交拉取请求时，CLA 机器人会自动确定您是否需要提供 CLA 并相应地装饰 PR（例如，状态检查、评论）。只需按照机器人提供的指示操作即可。您只需在整个使用我们 CLA 的仓库中执行一次此操作。

本项目已采用 [Microsoft 开源行为准则](https://opensource.microsoft.com/codeofconduct/)。有关更多信息，请参阅 [行为准则常见问题](https://opensource.microsoft.com/codeofconduct/faq/) 或通过 [opencode@microsoft.com](mailto:opencode@microsoft.com) 联系我们以获取任何其他问题或评论。

### 如何贡献

您可以查看问题或帮助审查 PR 来提供帮助。任何问题或 PR 都是受欢迎的，但我们还标记了一些“开放供贡献”和“开放供审查”的问题和 PR，以帮助促进社区贡献。这些只是建议，您可以通过任何方式贡献。

|            | 全部                                                          | 特别需要社区帮助                                                                                                      |
| ---------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **问题**   | [所有问题](https://github.com/microsoft/markitdown/issues) | [开放供贡献的问题](https://github.com/microsoft/markitdown/issues?q=is%3Aissue+is%3Aopen+label%3A%22open+for+contribution%22) |
| **PRs**    | [所有 PRs](https://github.com/microsoft/markitdown/pulls)   | [开放供审查的 PRs](https://github.com/microsoft/markitdown/pulls?q=is%3Apr+is%3Aopen+label%3A%22open+for+reviewing%22)              |

### 运行测试和检查

- 导航到 MarkItDown 包：

```sh
  cd packages/markitdown
```

- 在您的环境中安装 `hatch` 并运行测试：

```sh
  pip install hatch  # 其他安装 hatch 的方法：https://hatch.pypa.io/dev/install/
  hatch shell
  hatch test
```

  （备选）使用 Devcontainer，其中已安装所有依赖项：

```sh
  # 在 Devcontainer 中重新打开项目并运行：
  hatch test
```

- 在提交 PR 前运行预提交检查：`pre-commit run --all-files`

### 贡献第三方插件

您还可以通过创建和分享第三方插件来贡献。更多详细信息请参阅 `packages/markitdown-sample-plugin`。

## 商标

本项目可能包含项目、产品或服务的商标或徽标。授权使用 Microsoft

使用商标或徽标必须遵守 [Microsoft 的商标和品牌指南](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)。在本项目的修改版本中使用 Microsoft 商标或徽标时，不得引起混淆或暗示 Microsoft 的赞助。第三方商标或徽标的使用需遵循相关第三方的政策。

**官方网站：** [https://github.com/microsoft/markitdown](https://github.com/microsoft/markitdown)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`docker`
- 参数：`run --rm -i markitdown-mcp:latest`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/microsoft-markitdown.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
