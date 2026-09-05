---
title: "MCP官方示例"
description: "这个MCP服务器试图运用MCP协议的所有功能。它并不是一个实用的服务器，而是为MCP客户端开发者提供的测试服务器。它实现了提示、工具、资源、采样等功能，以展示MCP的能力。"
---

# MCP官方示例

这个MCP服务器试图运用MCP协议的所有功能。它并不是一个实用的服务器，而是为MCP客户端开发者提供的测试服务器。它实现了提示、工具、资源、采样等功能，以展示MCP的能力。

# Everything MCP 服务器

这个MCP服务器尝试使用MCP协议的所有功能。它并不打算成为一个有用的服务器，而是为MCP客户端的开发者提供一个测试服务器。它实现了提示、工具、资源、采样等功能，以展示MCP的能力。

## 组件

### 工具

1. `echo`
   - 简单工具，用于回显输入消息
   - 输入：
     - `message` (字符串): 要回显的消息
   - 返回: 包含回显消息的文本内容

2. `add`
   - 将两个数字相加
   - 输入：
     - `a` (数字): 第一个数字
     - `b` (数字): 第二个数字
   - 返回: 加法结果的文本形式

3. `longRunningOperation`
   - 演示长时间操作的进度通知
   - 输入：
     - `duration` (数字, 默认值: 10): 操作持续时间（秒）
     - `steps` (数字, 默认值: 5): 进度步骤数
   - 返回: 包含持续时间和步骤数的完成消息
   - 在执行过程中发送进度通知

4. `sampleLLM`
   - 使用MCP采样功能演示LLM采样能力
   - 输入：
     - `prompt` (字符串): 发送给LLM的提示
     - `maxTokens` (数字, 默认值: 100): 生成的最大令牌数
   - 返回: 生成的LLM响应

5. `getTinyImage`
   - 返回一个小的测试图片
   - 不需要输入
   - 返回: Base64编码的PNG图片数据

6. `printEnv`
   - 打印所有环境变量
   - 对于调试MCP服务器配置非常有用
   - 不需要输入
   - 返回: 所有环境变量的JSON字符串

7. `annotatedMessage`
   - 演示如何使用注释来提供关于内容的元数据
   - 输入：
     - `messageType` (枚举: "error" | "success" | "debug"): 消息类型，用于演示不同的注释模式
     - `includeImage` (布尔, 默认值: false): 是否包含示例图片
   - 返回: 带有不同注释的内容：
     - 错误消息: 高优先级(1.0)，对用户和助手可见
     - 成功消息: 中等优先级(0.7)，面向用户
     - 调试消息: 低优先级(0.3)，面向助手
     - 可选图片: 中等优先级(0.5)，面向用户
   - 示例注释:
```json
     {
       "priority": 1.0,
       "audience": ["user", "assistant"]
     }
```

8. `getResourceReference`
   - 返回一个可以被MCP客户端使用的资源引用
   - 输入：
     - `resourceId` (数字, 1-100): 要引用的资源ID
   - 返回: 包含以下内容的资源引用：
     - 文本介绍
     - 嵌入式资源，`type: "resource"`
     - 使用资源URI的文本说明

### 资源

服务器提供了100个测试资源，分为两种格式：
- 偶数编号资源：
  - 纯文本格式
  - URI模式: `test://static/resource/{even_number}`
  - 内容: 简单的文本描述

- 奇数编号资源：
  - 二进制块格式
  - URI模式: `test://static/resource/{odd_number}`
  - 内容: Base64编码的二进制数据

资源特性：
- 支持分页（每页10项）
- 允许订阅资源更新
- 展示资源模板
- 每5秒自动更新已订阅的资源

### 提示词

1. `simple_prompt`
   - 基础提示，无参数
   - 返回：单条消息交换

2. `complex_prompt`
   - 高级提示，展示参数处理
   - 必需参数：
     - `temperature` (数字)：温度设置
   - 可选参数：
     - `style` (字符串)：输出样式偏好
   - 返回：包含图片的多轮对话

3. `resource_prompt`
   - 展示如何在提示中嵌入资源引用
   - 必需参数：
     - `resourceId` (数字)：要嵌入资源的ID（1-100）
   - 返回：带有嵌入资源引用的多轮对话
   - 展示了如何直接在提示消息中包含资源

### 日志记录

服务器每隔15秒发送随机级别的日志消息，例如：

```json
{
  "method": "notifications/message",
  "params": {
    "level": "info",
    "data": "Info-level message"
  }
}
```

## 与Claude桌面版一起使用

在您的`claude_desktop_config.json`中添加：

```json
{
  "mcpServers": {
    "everything": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-everything"
      ]
    }
  }
}
```

**官方网站：** [https://github.com/modelcontextprotocol/servers/tree/main/src/everything](https://github.com/modelcontextprotocol/servers/tree/main/src/everything)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @modelcontextprotocol/server-everything`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/modelcontextprotocol-everything.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
