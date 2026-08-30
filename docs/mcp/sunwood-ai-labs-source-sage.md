---
title: "源智 Markdown 文档生成器"
description: "一个基于 TypeScript 的服务器，可以将项目目录结构以 Markdown 格式可视化，并自动为文件内容添加语法高亮的文档说明，同时支持可自定义的排除模式。"
---

# 源智 Markdown 文档生成器

一个基于 TypeScript 的服务器，可以将项目目录结构以 Markdown 格式可视化，并自动为文件内容添加语法高亮的文档说明，同时支持可自定义的排除模式。

# 🌟 SourceSage MCP

## 📖 概要

SourceSage 是一个 MCP 服务器，可以将项目的目录结构以美观的 Markdown 格式可视化。它用 TypeScript 实现，提供了高级的自定义选项和灵活的排除模式功能。此外，它还可以自动记录每个文件的内容，帮助您更好地了解整个项目。

## 🎯 主要特性

- 📁 以 Markdown 格式输出目录结构
- 🎨 美观的树状结构显示（ASCII 艺术）
- 📝 文件内容的自动文档化（带语言特定的语法高亮）
- 🔍 灵活的排除模式（.SourceSageignore）
- 🚀 基于 ES2022 和 Node16 模块系统的最新实现
- 💫 通过严格的类型检查保证高可靠性

## 🛠️ 技术栈

- 🔷 TypeScript (ES2022 目标)
- 📦 Model Context Protocol SDK (v0.6.0)
- 🌐 Node.js (Node16 模块系统)
- 📚 glob (v11.0.0) - 文件模式匹配
- 🎭 ignore (v6.0.2) - 灵活的文件排除功能

## 📂 项目结构

```plaintext
source-sage/
├── assets/
│   └── header.svg          # プロジェクトヘッダー画像
├── src/
│   └── index.ts           # メインサーバー実装
├── build/                 # コンパイル済みJavaScriptファイル
├── .gitignore            # Gitの除外設定
├── .SourceSageignore     # SourceSage固有の除外設定
├── package.json          # プロジェクト設定・依存関係
├── README.md            # プロジェクトドキュメント
└── tsconfig.json        # TypeScript設定
```

## ⚙️ TypeScript 配置

```json
{
  "compilerOptions": {
    "target": "ES2022",        // 最新のECMAScript機能を活用
    "module": "Node16",        // Node.js 16の最新モジュールシステムを使用
    "moduleResolution": "Node16",
    "outDir": "./build",      // コンパイル済みファイルの出力先
    "rootDir": "./src",       // ソースファイルのルートディレクトリ
    "strict": true,           // 厳格な型チェックを有効化
    "esModuleInterop": true,  // CommonJSモジュールとの相互運用性を確保
    "skipLibCheck": true,     // 型定義ファイルのチェックをスキップ
    "forceConsistentCasingInFileNames": true  // ファイル名の大文字小文字を厳格に管理
  }
}
```

## ⚙️ 安装

### 从 npm 安装
```bash
npm install -g @sunwood-ai-labs/source-sage-mcp-server
```

### 从源码构建
```bash
git clone https://github.com/sunwood-ai-labs/source-sage-mcp-server.git
cd source-sage-mcp-server
npm install
npm run build
```

## 🔧 使用方法

### 作为 MCP 服务器配置

1. 在 MCP 的配置文件中添加以下内容:

```json
{
  "mcpServers": {
    "source-sage": {
      "command": "node",
      "args": ["C:/path/to/source-sage/build/index.js"]
    }
  }
}
```

### 🎮 可用工具

#### generate_structure

生成项目的目录结构，并创建包含文件内容的详细文档。

```typescript
interface GenerateStructureArgs {
  // 構造を生成するディレクトリのパス（必須）
  // 必ず絶対パスで指定してください
  path: string;
  // .SourceSageignoreファイルのパス（オプション）
  // 指定する場合は絶対パスで指定してください
  ignorePath?: string;
}
```

### 使用示例

```typescript
// 絶対パスでの使用（推奨）
const result = await mcpClient.callTool('source-sage', 'generate_structure', {
  path: 'C:/Users/your-name/path/to/your-project',
  ignorePath: 'C:/Users/your-name/path/to/your-project/.SourceSageignore'
});
```

### 输出示例

实际项目结构的输出示例：

```plaintext
# 📁 Project: source-sage

## 🌳 ディレクトリ構造

OS: win32
Directory: C:\Users\your-name\source-sage

└─ source-sage/
   ├─ src/
   │  └─ index.ts          # MCPサーバーの主要な実装
   ├─ package.json         # プロジェクトの依存関係と設定
   ├─ README.md           # プロジェクトの詳細な説明
   └─ tsconfig.json       # TypeScriptのコンパイル設定
```

此输出包括以下信息：

- 📁 项目名称和操作系统信息
- 🌳 目录树结构
- 📝 各文件的角色和说明
- 🔍 通过 .SourceSageignore 排除不需要的文件

## 📝 .SourceSageignore 的配置

在项目的根目录下创建 `.SourceSageignore` 文件，并写入需要排除的模式。默认情况下，包含如下排除模式：

```plaintext
# バージョン管理システム関連
.git
.gitignore

# キャッシュファイル
__pycache__
.pytest_cache
**/__pycache__/**
*.pyc

# ビルド・配布関連
build
dist
*.egg-info

# 一時ファイル・出力
output
output.md
test_output
.SourceSageAssets
.SourceSageAssetsDemo

# アセット
*.png
*.svg
assets

# その他
LICENSE
example
folder
package-lock.json
```

## 🔄 输出示例

```plaintext
  # 📁 Project: my-project

  ## 🌳 ディレクトリ構造

  OS: win32
  Directory: C:\path\to\my-project

  └─ my-project/
    ├─ src/
    │  ├─ index.ts
    │  └─ utils/
    │     └─ helper.ts
    └─ package.json

  ## 📄 ファイル内容

  ### 📝 `src/index.ts`
  **Type**: TypeScript Source File

```

## 👨‍💻 开发者信息

### 主要实现细节

- **Server Class**: `SourceSageServer` 类提供 MCP 服务器的核心功能
- **Tree Building**: 
  - `buildTree` 方法递归解析目录结构
  - 适当排序目录和文件以进行显示
- **File Filtering**: 
  - 使用 `ignore` 包实现灵活的文件排除
  - 支持丰富的默认排除模式和自定义设置
- **Content Generation**:
  - 根据文件类型提供适当的语法高亮
  - 提供基于文件类型的附加信息
- **Async Processing**: 
  - 使用 `glob` 包进行高效的文件扫描
  - 通过异步处理支持大型项目

### 开发环境设置

```bash
# リポジトリのクローン
git clone https://github.com/sunwood-ai-labs/source-sage-mcp-server.git

# 依存関係のインストール
npm install

# 開発用ビルド
npm run build

# 開発サーバーの起動
npm run inspector
```

### 可用的 npm 脚本

- `npm run build`: 编译 TypeScript 并设置执行权限
- `npm run prepare`: 安装时自动构建
- `npm run watch`: 开发时自动编译
- `npm run inspector`: 启动 MCP 检查器

## 🤝 贡献

1. Fork 此仓库
2. 创建新分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m '✨ feat: 添加了很棒的功能'`)
4. 将分支推送到远程 (`git push origin feature/amazing-feature`)
5. 创建 Pull Request

## 📄 许可证

MIT License - 详情请参阅 LICENSE 文件。

## 🔗 相关链接

- [npm 包](https://www.npmjs.com/package/@sunwood-ai-labs/source-sage-mcp-server)
- [GitHub 仓库](https://github.com/sunwood-ai-labs/source-sage-mcp-server)
- [报告 Bug](https://github.com/sunwood-ai-labs/source-sage-mcp-server/issues)

## 👥 维护者

- Sunwood AI Labs 团队

---

由 Sunwood AI Labs 出于热爱制作

**官方网站：** [https://github.com/Sunwood-ai-labs/source-sage-mcp-server](https://github.com/Sunwood-ai-labs/source-sage-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`files`
- 标签：`developer tools`, `file systems`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`C:/path/to/source-sage/build/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/sunwood-ai-labs-source-sage.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
