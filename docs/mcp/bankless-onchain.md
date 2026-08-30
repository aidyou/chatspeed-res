---
title: "链上MCP"
description: "实现了模型上下文协议，允许人工智能模型访问和交互区块链数据，包括读取合约状态、检索事件以及跨各种网络访问交易信息。"
---

# 链上MCP

实现了模型上下文协议，允许人工智能模型访问和交互区块链数据，包括读取合约状态、检索事件以及跨各种网络访问交易信息。

# Bankless Onchain MCP 服务器

[![License: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)
![Version](/mcp-assets/acecfa064090bf1e90020b170f74a660.svg)

通过 Bankless API 进行区块链数据交互的 MCP（模型上下文协议）服务器。

## 概述

Bankless Onchain MCP 服务器提供了一个通过 Bankless API 与链上数据交互的框架。它实现了模型上下文协议（MCP），允许 AI 模型以结构化的方式访问区块链状态和事件数据。

[https://github.com/user-attachments/assets/95732dff-ae5f-45a6-928a-1ae17c0ddf9d](https://github.com/user-attachments/assets/95732dff-ae5f-45a6-928a-1ae17c0ddf9d)

## 功能

该服务器提供了以下链上数据操作：

### 合约操作

- **读取合约状态** (`read_contract`)：从各种区块链网络上的智能合约中读取状态。
    - 参数：网络、合约地址、方法、输入、输出
    - 返回：带有类型值的合约调用结果

- **获取代理** (`get_proxy`)：检索代理实现合约地址。
    - 参数：网络、合约地址
    - 返回：实现合约地址

- **获取 ABI** (`get_abi`)：获取合约的 ABI（应用程序二进制接口）。
    - 参数：网络、合约地址
    - 返回：JSON 格式的合约 ABI

- **获取源代码** (`get_source`)：检索已验证合约的源代码。
    - 参数：网络、合约地址
    - 返回：源代码、ABI、编译器版本和其他合约元数据

### 事件操作

- **获取事件** (`get_events`)：根据主题获取合约的事件日志。
    - 参数：网络、地址、主题、可选主题
    - 返回：过滤后的事件日志

- **构建事件主题** (`build_event_topic`)：从事件名称和参数类型生成事件主题签名。
    - 参数：网络、事件名称、参数类型
    - 返回：事件主题哈希

### 交易操作

- **获取交易历史** (`get_transaction_history`)：检索用户地址的交易历史。
    - 参数：网络、用户地址、可选合约、可选方法 ID、可选起始区块、包含数据标志
    - 返回：包含哈希、数据、网络和时间戳的交易列表

- **获取交易信息** (`get_transaction_info`)：获取特定交易的详细信息。
    - 参数：网络、交易哈希
    - 返回：包括区块号、时间戳、from/to 地址、价值、gas 信息、状态和收据数据在内的交易详情

## 工具

```

- **read_contract**
    - 从区块链读取合约状态
    - 输入：
        - `network` (字符串，必填)：区块链网络（例如："ethereum", "polygon"）
        - `contract` (字符串，必填)：合约地址
        - `method` (字符串，必填)：要调用的合约方法
        - `inputs` (数组，必填)：方法调用的输入参数，每个包含：
            - `type` (字符串)：输入参数的类型（例如："address", "uint256"）
            - `value` (任意)：输入参数的值
        - `outputs` (数组，必填)：预期输出类型，每个包含：
            - `type` (字符串)：预期输出类型
    - 返回一个包含合约调用结果的数组

- **get_proxy**
    - 获取给定网络和合约的代理地址
    - 输入：
        - `network` (字符串，必填)：区块链网络（例如："ethereum", "base"）
        - `contract` (字符串，必填)：合约地址
    - 返回代理合约的实现地址

- **get_events**
    - 根据给定的网络和过滤条件获取事件日志
    - 输入：
        - `network` (字符串，必填)：区块链网络（例如："ethereum", "base"）
        - `addresses` (数组，必填)：用于过滤事件的合约地址列表
        - `topic` (字符串，必填)：主要主题以过滤事件
        - `optionalTopics` (数组，可选)：可选的附加主题（可以包括 null 值）
    - 返回一个对象，其中包含符合过滤条件的事件日志

- **build_event_topic**
    - 根据事件名称和参数构建事件主题签名
    - 输入：
        - `network` (字符串，必填)：区块链网络（例如："ethereum", "base"）
        - `name` (字符串，必填)：事件名称（例如："Transfer(address,address,uint256)"）
        - `arguments` (数组，必填)：事件参数类型，每个包含：
            - `type` (字符串)：参数类型（例如："address", "uint256"）
    - 返回一个包含事件签名的 keccak256 哈希值的字符串

## 安装

```
#0
```

## 使用

### 环境设置

在使用服务器之前，请设置您的 Bankless API 令牌。有关如何获取您的 Bankless API 令牌的详细信息，请访问 [https://docs.bankless.com/bankless-api/other-services/onchain-mcp](https://link.2)

```
#1
```

### 运行服务器

可以直接从命令行运行服务器：

```
#2
```

### 与 LLM 工具一起使用

该服务器实现了模型上下文协议（MCP），使其能够作为兼容 AI 模型的工具提供者使用。以下是一些示例调用：

#### read_contract

```
#3
```

#### get_proxy

```
#4
```

#### get_events

```
#5
```

#### build_event_topic

```
#6
```

## 开发

### 从源代码构建

```
#7
```

### 调试模式

```
#8
```

### 与 AI 模型集成

要将此服务器与支持MCP的AI应用程序集成，请在您的应用程序的服务器配置中添加以下内容：

```
#9
```

## 错误处理

服务器为不同场景提供了特定的错误类型：

- `BanklessValidationError`：无效的输入参数
- `BanklessAuthenticationError`：API令牌问题
- `BanklessResourceNotFoundError`：请求的资源未找到
- `BanklessRateLimitError`：API速率限制超出

## 提示技巧

为了指导LLM模型使用Bankless Onchain MCP Server，可以使用以下提示：

```
#10
```

## 许可证

MIT
```

**官方网站：** [https://github.com/bankless/onchain-mcp](https://github.com/bankless/onchain-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`finance`
- 标签：`databases`, `finance`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`@bankless/onchain-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/bankless-onchain.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
