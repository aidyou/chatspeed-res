---
title: "析言MCP"
description: "一种自然语言交互的数据库查询MCP服务，嵌入专用text-to-sql的SOTA模型获得更高的查询精度"
---

# 析言MCP

一种自然语言交互的数据库查询MCP服务，嵌入专用text-to-sql的SOTA模型获得更高的查询精度

## 功能
- 🌐 通过 [XiYanSQL](https://github.com/XGenerationLab/XiYan-SQL) 以自然语言获取数据
- 🖱️ 列出可用的 MySQL 表作为资源
- 🔧 读取表内容

## 工具预览
- 工具 ``get_data`` 提供了一个自然语言接口，用于从数据库中检索数据。该服务器将输入的自然语言转换为 SQL，并调用数据库以返回查询结果。

- ``mysql://{table_name}`` 资源允许在指定特定表名时从数据库中获取一部分示例数据供模型参考。
- ``mysql://`` 资源将列出当前数据库的名称。

## 安装
### 通过 pip 安装

需要 Python 3.11 及以上版本。
您可以通过 pip 安装服务器，它将安装最新版本。

```bash
pip install xiyan-mcp-server
```

安装后，您可以直接运行服务器：
```bash
python -m xiyan_mcp_server
```
但在完成以下配置之前，它不会提供任何功能。
您会得到一个 yml 文件。之后，您可以通过以下命令运行服务器：
```yaml
env YML=path/to/yml python -m xiyan_mcp_server
```

### 通过 Smithery.ai 安装
请参见 [@XGenerationLab/xiyan_mcp_server](https://smithery.ai/server/@XGenerationLab/xiyan_mcp_server)

尚未完全测试。

## 配置

您需要一个 yml 配置文件来配置服务器。
在 config_demo.yml 中提供了默认配置文件，内容如下：

```yaml
model:
  name: "XGenerationLab/XiYanSQL-QwenCoder-32B-2412"
  key: ""
  url: "https://api-inference.modelscope.cn/v1/"

database:
  host: "localhost"
  port: 3306
  user: "root"
  password: ""
  database: ""
```

### LLM 配置
``Name`` 是要使用的模型名称，``key`` 是模型的 API 密钥，``url`` 是模型的 API URL。我们支持以下模型。

| 版本      | 通用 LLMs (GPT, qwenmax)                              | Modelscope 的前沿模型                        | Dashscope 的前沿模型                                 | 本地 LLMs            |
|-----------|---------------------------------------------------|-------------------------------------|--------------------------------------------------|---------------------|
| 描述      | 基本，易于使用                                      | 性能最佳，稳定，推荐                     | 性能最佳，试用                                     | 缓慢，高安全性      |
| 名称      | 官方模型名称 (如 gpt-3.5-turbo,qwen-max)            | XGenerationLab/XiYanSQL-QwenCoder-32B-2412  | xiyansql-qwencoder-32b                           | xiyansql-qwencoder-3b |
| 密钥      | 服务提供商的 API 密钥 (如 OpenAI, 阿里云)             | 模型的 API 密钥                           | 通过电子邮件获取的 API 密钥                          | ""                  |
| URL       | 服务提供商的端点 (如 "https://api.openai.com/v1") | https://api-inference.modelscope.cn/v1/ | https://xiyan-stream.biz.aliyun.com/service/api/xiyan-sql | http://localhost:5090 |

#### 通用 LLMs
如果您希望使用通用 LLMs，例如 gpt3.5，可以直接进行如下配置：
```yaml
model:
  name: "gpt-3.5-turbo"
  key: "YOUR KEY"
  url: "https://api.openai.com/v1"
database:
```

如果您希望使用来自阿里巴巴的 Qwen，例如 Qwen-max，可以使用以下配置。
```yaml
model:
  name: "qwen-max"
  key: "YOUR KEY"
  url: "https://dashscope.aliyuncs.com/compatible-mode/v1"
database:
```
#### 文本到 SQL 的前沿模型
我们推荐使用 XiYanSQL-qwencoder-32B (https://github.com/XGenerationLab/XiYanSQL-QwenCoder)，这是文本到 SQL 的前沿模型，详细见 [Bird 基准](https://bird-bench.github.io/)。
使用该模型有两种方式。您可以使用以下任一方式。
(1) [Modelscope](https://www.modelscope.cn/models/XGenerationLab/XiYanSQL-QwenCoder-32B-2412)，  (2) 阿里巴巴云 DashScope。

##### (1) Modelscope 版本
您需要申请 Modelscope 的 ``key`` 用于 API 推断，网址为 https://www.modelscope.cn/docs/model-service/API-Inference/intro。
然后您可以使用以下配置：
```yaml
model:
  name: "XGenerationLab/XiYanSQL-QwenCoder-32B-2412"
  key: ""
  url: "https://api-inference.modelscope.cn/v1/"
```

查看我们的 [模型描述](https://www.modelscope.cn/models/XGenerationLab/XiYanSQL-QwenCoder-32B-2412) 获取更多细节。 

##### (2) Dashscope 版本

我们已在阿里巴巴云 DashScope 上部署该模型，因此您需要设置以下环境变量：
将您的电子邮件发送给我以获取 ``key``。 (godot.lzl@alibaba-inc.com)
在电子邮件中，请附上以下信息：
```yaml
name: "YOUR NAME",
email: "YOUR EMAIL",
organization: "your college or Company or Organization"
```
我们将根据您的电子邮件向您发送 ``key``。您可以在 yml 文件中填写该 ``key``。
该 ``key`` 有效期为 1 个月或 200 次查询或其他法律限制。

```yaml
model:
  name: "xiyansql-qwencoder-32b"
  key: "KEY"
  url: "https://xiyan-stream.biz.aliyun.com/service/api/xiyan-sql"
database:
```

注意：该模型服务仅供试用，如果您需要在生产环境中使用，请与我们联系。

另外，您也可以在自己的服务器上部署模型 [XiYanSQL-qwencoder-32B](https://github.com/XGenerationLab/XiYanSQL-QwenCoder)。

#### 本地模型
注意：本地模型较慢（在我的 MacBook 上每次查询约 12 秒）。
如果您需要稳定和快速的服务，我们仍然推荐使用 Modelscope 版本。

在本地模式下运行 xiyan_mcp_server，您需要：
1) 一台至少 16GB RAM 的 PC/Mac
2) 6GB 磁盘空间

步骤 1：安装额外的 Python 包
```bash
pip install flask modelscope torch==2.2.2 accelerate>=0.26.0 numpy=2.2.3
```

步骤 2：（可选）手动下载模型
我们推荐 [xiyansql-qwencoder-3b](https://www.modelscope.cn/models/XGenerationLab/XiYanSQL-QwenCoder-3B-2502/)。
您可以通过以下方式手动下载该模型：
```bash
modelscope download --model XGenerationLab/XiYanSQL-QwenCoder-3B-2502
```
这将占用您 6GB 的磁盘空间。

步骤 3：下载脚本并运行服务器 src/xiyan_mcp_server/local_xiyan_server.py
```bash
python local_xiyan_server.py
```
服务器将运行在 http://localhost:5090/

步骤 4：准备配置并运行 xiyan_mcp_server
config.yml 应如下所示：
```yaml
model:
  name: "xiyansql-qwencoder-3b"
  key: "KEY"
  url: "http://127.0.0.1:5090"
```

到此为止，本地模式已准备就绪。

### 数据库配置
``host``、``port``、``user``、``password`` 和 ``database`` 是 MySQL 数据库的连接信息。

您可以使用本地或任何远程数据库。目前我们支持 MySQL（未来将支持更多方言）。

```yaml
database:
  host: "localhost"
  port: 3306
  user: "root"
  password: ""
  database: ""
```

## 启动
### Claude 桌面
在您的 Claude 桌面配置文件中添加以下内容，参考 
Claude 桌面配置示例
。
```json
{
    "mcpServers": {
        "xiyan-mcp-server": {
            "command": "python",
            "args": [
                "-m",
                "xiyan_mcp_server"
            ],
            "env": {
                "YML": "PATH/TO/YML"
            }
        }
    }
}
```
### Cline
准备与 [Claude 桌面](#claude-desktop) 相同的配置。

### Goose
在配置中添加以下命令，参考 
Goose 配置示例
。
```yaml
env YML=path/to/yml python -m xiyan_mcp_server
```
### Cursor
使用与 [Goose](#goose) 相同的命令。

### Witsy
在命令中添加以下内容。
```yaml
python -m xiyan_mcp_server
```
添加一个环境变量：键为 YML，值为您 yml 文件的路径。
参考 
Witsy 配置示例
。

## 无法正常工作！
请联系我们：

钉钉群
｜ 

在微博上关注我

## 引用
如果您认为我们的工作对您有帮助，请随意引用我们。
```bib
@article{xiyansql,
      title={A Preview of XiYan-SQL: A Multi-Generator Ensemble Framework for Text-to-SQL}, 
      author={Yingqi Gao and Yifu Liu and Xiaoxia Li and Xiaorong Shi and Yin Zhu and Yiming Wang and Shiqi Li and Wei Li and Yuntao Hong and Zhiling Luo and Jinyang Gao and Liyu Mou and Yu Li},
      year={2024},
      journal={arXiv preprint arXiv:2411.08599},
      url={https://arxiv.org/abs/2411.08599},
      primaryClass={cs.AI}
}
```

**官方网站：** [https://github.com/XGenerationLab/xiyan_mcp_server](https://github.com/XGenerationLab/xiyan_mcp_server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`python`
- 参数：`-m xiyan_mcp_server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/xgenerationlab-xiyan.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
