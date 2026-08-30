---
title: "做生物信息学分析的MCP"
description: "🎯 这是什么？ BioNext-MCP 是为 Cursor 设计的智能生物信息学分析工具，允许您通过自然语言对话执行复杂的生物信息学分析，而无需编写任何代码！ 简而言之： - 🗣️ 用自然语言告诉 Cursor 您要分析的数据 - 🤖 Cursor 自动生成专业的 Python 分析脚本 - ⚡ 系统自动执行脚本并显示结果 - 📊 获取美观的 HTML 报告和可视化图表 ✨ 主要功能 🧬 支持的分析类型 - 单细胞 RNA 测序 (scRNA-seq) - 细胞聚类、差异表达、轨迹分析 - 基因组学 - 变异分析、"
---

# 做生物信息学分析的MCP

🎯 这是什么？ BioNext-MCP 是为 Cursor 设计的智能生物信息学分析工具，允许您通过自然语言对话执行复杂的生物信息学分析，而无需编写任何代码！ 简而言之： - 🗣️ 用自然语言告诉 Cursor 您要分析的数据 - 🤖 Cursor 自动生成专业的 Python 分析脚本 - ⚡ 系统自动执行脚本并显示结果 - 📊 获取美观的 HTML 报告和可视化图表 ✨ 主要功能 🧬 支持的分析类型 - 单细胞 RNA 测序 (scRNA-seq) - 细胞聚类、差异表达、轨迹分析 - 基因组学 - 变异分析、

## 🎯 What is this?

BioNext-MCP is an intelligent bioinformatics analysis tool designed for Cursor, allowing you to perform complex bioinformatics analysis through natural language conversations without writing any code!

**Simply put:**
- 🗣️ Tell Cursor what data you want to analyze in plain language
- 🤖 Cursor automatically generates professional Python analysis scripts
- ⚡ System automatically executes scripts and displays results
- 📊 Get beautiful HTML reports and visualization charts

## ✨ Key Features

### 🧬 Supported Analysis Types
- **Single-cell RNA sequencing** (scRNA-seq) - Cell clustering, differential expression, trajectory analysis
- **Genomics** - Variant analysis, annotation, functional enrichment
- **Transcriptomics** - Differential expression, pathway analysis, co-expression networks
- **Proteomics** - Protein identification, quantitative analysis
- **Multi-omics integration** - Data fusion, correlation analysis

### 🎨 Smart Features
- **Automatic environment setup** - Detects Python, auto-installs required packages (pandas, numpy, matplotlib, etc.)
- **UTF-8 encoding support** - Perfect support for international characters
- **Visualization-first** - Automatically generates charts and displays them in HTML reports
- **Quality assurance** - Focuses on code completeness and analysis accuracy
- **Error handling** - Smart diagnosis of issues with solution suggestions

## 🚀 Quick Start

### Requirements
- **Python**: >= 3.9
- **Node.js**: >= 16.0.0
- **Operating System**: Windows, macOS, Linux

### Installation Steps

#### 1. Install Python Environment

**Recommended: Official Website Installation**
1. Visit [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download Python 3.9 or higher
3. **Make sure to check "Add Python to PATH" during installation**

**Verify Installation**
Open command prompt and type:
```bash
python --version
```
If you see version information, installation was successful!

#### 2. Install BioNext-MCP

**Download Project**
```bash
git clone https://github.com/Cherine0205/BioNext-mcp.git
cd BioNext-mcp
```

**Install Dependencies**
```bash
npm install
npm run build
```

#### 3. Configure Cursor

**Find Configuration File**
- Windows: `%APPDATA%\Cursor\User\settings.json`
- macOS: `~/Library/Application Support/Cursor/User/settings.json`
- Linux: `~/.config/Cursor/User/settings.json`

**Add Configuration**
```json
{
  "mcpServers": {
    "bioinformatics-workflow": {
      "command": "node",
      "args": ["D:\\path\\to\\BioNext-mcp\\dist\\index.js"],
      "cwd": "D:\\path\\to\\BioNext-mcp",
      "env": {
        "PROJECT_PATH": "D:\\path\\to\\your\\analysis\\directory",
        "PYTHON_PATH": "/usr/bin/python3"
      }
    }
  }
}
```

**Important:** 
- Replace paths with your actual installation paths
- Set analysis directory to where you want results saved
- Restart Cursor

## 💡 How to Use

### Basic Conversation Flow

1. **Describe Your Analysis Needs**
```
I have a single-cell RNA sequencing data file data.h5ad, and I want to perform cell clustering analysis and differential expression analysis
```

2. **Cursor will generate analysis scripts and execute them automatically**
3. **Get detailed HTML reports** including:
   - Execution results and statistics
   - Generated charts and visualizations
   - Complete analysis logs

### Practical Examples

#### 🧪 Single-cell Analysis
```
Please help me analyze this scRNA-seq data:
- File: C:\data\pbmc3k.h5ad
- Need: quality control, normalization, clustering, marker gene identification
- Output: UMAP plot, clustering heatmap, differential expression gene list
```

#### 🧬 Gene Expression Analysis
```
I have RNA-seq expression matrices from two groups:
- Control group: control_samples.csv
- Treatment group: treatment_samples.csv
- Analysis: differential expression, GO enrichment, KEGG pathway analysis
- Visualization: volcano plot, heatmap, pathway diagrams
```

#### 📊 Data Exploration
```
Help me explore this gene expression dataset:
- File: gene_expression.csv
- Need: data overview, correlation analysis, PCA analysis
- Generate: statistical summary, correlation heatmap, PCA plot
```

## 🎨 Beautiful Reports

### HTML Report Features
- **📊 Visualization Gallery** - Automatically detects and displays generated images
- **🔍 Interactive Viewing** - Click images to zoom and view
- **📝 Detailed Logs** - Complete execution process records
- **📈 Statistical Summary** - Script execution status and performance metrics

### Automatic Browser Opening
- Reports automatically open in browser after analysis completion
- If not auto-opened, manually open the generated HTML file

## 🛠️ Common Issues

### Python-related
**Q: "Python not found" error?**
A: Ensure Python is installed and added to PATH environment variable

**Q: Package installation fails?**
A: System will automatically retry, or manually run `pip install package_name`

### Analysis-related
**Q: Script execution fails?**
A: 
- Check if data file paths are correct
- Confirm data format meets requirements
- Check error logs for detailed information

**Q: No HTML report generated?**
A: HTML reports are only generated when all scripts execute successfully, fix execution errors first

### Data Formats
**Q: What data formats are supported?**
A: 
- CSV, TSV, Excel files
- HDF5 format (.h5, .h5ad)
- FASTA, FASTQ sequence files
- VCF variant files
- Other common bioinformatics formats

## 🎯 Usage Tips

### 1. Clear Description of Needs
```
✅ Good description:
"Analyze single-cell data, perform quality control (filter low-quality cells), normalization, dimensionality reduction (PCA+UMAP), clustering (leiden algorithm), find marker genes for each cluster"

❌ Vague description:
"Analyze this data"
```

### 2. Provide Complete File Paths
```
✅ Use absolute paths:
"C:\Users\username\data\sample.h5ad"

❌ Relative paths may fail:
"./data/sample.h5ad"
```

### 3. Specify Output Requirements
```
✅ Clear output:
"Generate UMAP plot, heatmap, save results to CSV file"

❌ Unclear:
"Do some visualization"
```

### 4. Step-by-step Analysis
For complex analyses, break into multiple conversations:
1. First: Data loading and quality control
2. Second: Normalization and dimensionality reduction
3. Third: Clustering and visualization
4. Fourth: Differential analysis

## 🔧 Cursor Integration

### Integration Features
This project has been optimized for Cursor IDE with the following features:

- **MCP Server Support** - Full Model Context Protocol server implementation
- **Environment Variable Configuration** - Complete Python and Node.js environment configuration
- **Automatic Dependency Management** - Automatically installs required Python packages and Node.js modules
- **Error Handling Mechanism** - Comprehensive error diagnosis and solutions

### System Requirements
- **Python**: >= 3.9
- **Node.js**: >= 16.0.0
- **Memory**: >= 2GB RAM
- **Storage**: >= 1GB available space

### Environment Variables
- `PROJECT_PATH`: Analysis result output path
- `PYTHON_PATH`: Python interpreter path
- `NODE_ENV`: Node.js runtime environment
- `PYTHON_VERSION`: Python version requirement

## 🎉 Start Your Bioinformatics Journey

You're ready now! Open Cursor, tell it what data you want to analyze, and let AI handle the complex bioinformatics analysis for you!

---

## 📞 Get Help

- **GitHub Issues**: Report problems or suggest improvements
- **Documentation**: View detailed usage documentation
- **Examples**: Reference example analysis cases

**Remember:** Describe your analysis needs in natural language, Cursor will handle all the technical details for you! 🚀

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Welcome to submit Issues and Pull Requests to improve this project!

---

**BioNext-MCP Team** - Making bioinformatics analysis simple and accessible!

**官方网站：** [https://github.com/Cherine0205/BioNext-mcp/tree/modelscope-deployment](https://github.com/Cherine0205/BioNext-mcp/tree/modelscope-deployment)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`research and data`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`bioinformatics-mcp-server@latest`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/judy4algorithmn-mcp4bioinformatics.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
