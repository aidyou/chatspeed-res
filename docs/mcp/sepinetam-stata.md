---
title: "stata-mcp"
description: "Stata-MCP Let LLM help you achieve your regression analysis with Stata ✨ --- Looking for other Stata integrations or others? - A VScode or Cursor integrated here. Confused it? 💡 Difference - Jupyter L…"
---

# stata-mcp

Stata-MCP Let LLM help you achieve your regression analysis with Stata ✨ --- Looking for other Stata integrations or others? - A VScode or Cursor integrated here. Confused it? 💡 Difference - Jupyter L…

Stata-MCP

 Let LLM help you achieve your regression analysis with Stata ✨

![en](/mcp-assets/0eedd0c75f6dbccbae1486d81bfae9d0.svg)



[![PyPI version](/mcp-assets/8ba846b66dd1319463f712d5d7b0ebcf.svg)](https://pypi.org/project/stata-mcp/)
[![License: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://github.com/sepinetam/stata-mcp/blob/HEAD/LICENSE)
[![Issue](/mcp-assets/6254c643f4b946be409d2492b9ce6d6e.svg)](https://github.com/sepinetam/stata-mcp/issues/new)
[![Ask DeepWiki](/mcp-assets/0c95d8c98b281c617e230e437947ee44.svg)](https://deepwiki.com/SepineTam/stata-mcp)

---

> Looking for other Stata integrations or others?
>
> - A VScode or Cursor integrated [here](https://github.com/hanlulong/stata-mcp). Confused it? 💡 Difference
> - Jupyter Lab Usage (Important: Stata 17+) [here](https://github.com/sepinetam/Jupyter-Stata)
> - [NBER-MCP](https://github.com/sepinetam/NBER-MCP) 🔧 under construction
> - [AER-MCP](https://github.com/sepinetam/AER-MCP)
> - [Econometrics-Agent](https://github.com/FromCSUZhou/Econometrics-Agent)
> - [TexIV](https://github.com/sepinetam/TexIV) - A machine learning-driven framework that transforms text data into usable variables for empirical research using advanced NLP and ML techniques

## 💡 Quick Start
> Standard config requires: please make sure the stata is installed at the default path, and the stata cli (for macOS and Linux) exists.

The standard config json as follows, you can DIY your config via add envs.
```json
{
  "mcpServers": {
    "stata-mcp": {
      "command": "uvx",
      "args": [
        "stata-mcp"
      ]
    }
  }
}
```

For more detailed usage information, visit the Usage guide. 

And some advanced usage, visit the Advanced guide

### Prerequisites
- [uv](https://github.com/astral-sh/uv) - Package installer and virtual environment manager
- Claude, Cline, ChatWise, or other LLM service
- Stata License
- Your API-KEY from LLM

### Installation
For the new version, you don't need to install the `stata-mcp` package again, you can just use the following command to check whether your computer can use stata-mcp.
```bash
uvx stata-mcp --usable
uvx stata-mcp --version
```

If you want to use it locally, you can install it via pip or download the source code.

**Download via pip**
```bash
pip install stata-mcp
```

**Download source code and compile**
```bash
git clone https://github.com/sepinetam/stata-mcp.git
cd stata-mcp

uv build
```
Then you can find the compiled `stata-mcp` binary in the `dist` directory. You can use it directly or add it to your PATH.

For example:
```bash
uvx /path/to/your/whl/stata_mcp-1.6.0-py3-non-any.whl  # here is the wheel file name, you can change it to your version
```

## 📝 Documentation
- For more detailed usage information, visit the Usage guide.
- Advanced Usage, visit the Advanced
- Some questions, visit the Questions
- Difference with [Stata-MCP@hanlulong](https://github.com/hanlulong/stata-mcp), visit the Difference

## 💡 Questions
- Cherry Studio 32000 wrong
- Cherry Studio 32000 error
- Windows Support
- Network Errors When Running Stata-MCP

## 🚀 Roadmap
- [x] macOS support
- [x] Windows support
- [ ] Additional LLM integrations
- [ ] Performance optimizations

## ⚠️ Disclaimer
This project is for research purposes only. I am not responsible for any damage caused by this project. Please ensure you have proper licensing to use Stata.

For more information, refer to the Statement.

## 🐛 Report Issues
If you encounter any bugs or have feature requests, please [open an issue](https://github.com/sepinetam/stata-mcp/issues/new).

## 📄 License
[MIT License](https://github.com/sepinetam/stata-mcp/blob/HEAD/LICENSE) and Extensions

## 📚 Citation
If you use Stata-MCP in your research, please cite this repository using one of the following formats:

### BibTeX
```bibtex
@software{sepinetam2025stata,
  author = {Song Tan},
  title = {Stata-MCP: Let LLM help you achieve your regression analysis with Stata},
  year = {2025},
  url = {https://github.com/sepinetam/stata-mcp},
  version = {1.6.0}
}
```

### APA
```
Song Tan. (2025). Stata-MCP: Let LLM help you achieve your regression analysis with Stata (Version 1.6.0) [Computer software]. https://github.com/sepinetam/stata-mcp
```

### Chicago
```
Song Tan. 2025. "Stata-MCP: Let LLM help you achieve your regression analysis with Stata." Version 1.6.0. https://github.com/sepinetam/stata-mcp.
```

## 📬 Contact
Email: [sepinetam@gmail.com](mailto:sepinetam@gmail.com)

Or contribute directly by submitting a [Pull Request](https://github.com/sepinetam/stata-mcp/pulls)! We welcome contributions of all kinds, from bug fixes to new features.

## ❤️ Acknowledgements
The author sincerely thanks the Stata official team for their support and the Stata License for authorizing the test development.

## ✨ Star History

[![Star History Chart](/mcp-assets/7ff5ea12648cd650854ef8cf69c6f49e.svg)](https://www.star-history.com/#sepinetam/stata-mcp&Date)

**Official site: ** [https://github.com/sepinetam/stata-mcp](https://github.com/sepinetam/stata-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `research and data`, `stata`, `回归分析`, `实证研究`, `经济学`, `计量经济学`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `stata-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/sepinetam-stata.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
