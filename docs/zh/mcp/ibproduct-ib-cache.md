---
title: "模型上下文缓存器"
description: "一种模型上下文协议服务器，通过在语言模型交互之间高效缓存数据来减少令牌消耗，自动存储和检索信息以最小化冗余令牌使用。"
---

# 模型上下文缓存器

一种模型上下文协议服务器，通过在语言模型交互之间高效缓存数据来减少令牌消耗，自动存储和检索信息以最小化冗余令牌使用。

# 内存缓存服务器

一个模型上下文协议（MCP）服务器，通过在语言模型交互之间高效地缓存数据来减少令牌消耗。与任何使用令牌的MCP客户端和任何语言模型兼容。

## 安装

1. 克隆仓库：
```bash
git clone git@github.com:ibproduct/ib-mcp-cache-server
cd ib-mcp-cache-server
```

2. 安装依赖项：
```bash
npm install
```

3. 构建项目：
```bash
npm run build
```

4. 添加到您的MCP客户端设置中：
```json
{
  "mcpServers": {
    "memory-cache": {
      "command": "node",
      "args": ["/path/to/ib-mcp-cache-server/build/index.js"]
    }
  }
}
```

5. 当您使用MCP客户端时，服务器将自动启动

## 验证其工作情况

当服务器正常运行时，您会看到：
1. 终端中的消息：“内存缓存MCP服务器正在stdio上运行”
2. 多次访问相同数据时性能提高
3. 无需您采取任何行动 - 缓存会自动发生

您可以按照以下方式验证服务器是否正在运行：
1. 打开您的MCP客户端
2. 查看启动服务器的终端中是否有任何错误消息
3. 执行可以从缓存中受益的操作（如多次读取同一文件）

## 配置

服务器可以通过`config.json`或环境变量进行配置：

```json
{
  "maxEntries": 1000,        // Maximum number of items in cache
  "maxMemory": 104857600,    // Maximum memory usage in bytes (100MB)
  "defaultTTL": 3600,        // Default time-to-live in seconds (1 hour)
  "checkInterval": 60000,    // Cleanup interval in milliseconds (1 minute)
  "statsInterval": 30000     // Stats update interval in milliseconds (30 seconds)
}
```

### 配置设置说明

1. **maxEntries** (默认: 1000)
   - 可以存储在缓存中的最大项目数
   - 防止缓存无限增长
   - 超过限制时，最旧且未使用的项目将被优先移除

2. **maxMemory** (默认: 100MB)
   - 最大内存使用量（以字节为单位）
   - 防止过度消耗内存
   - 超过限制时，最近最少使用的项目将被移除

3. **defaultTTL** (默认: 1小时)
   - 默认情况下项目在缓存中停留的时间
   - 超过此时间后，项目将自动被移除
   - 防止陈旧数据占用内存

4. **checkInterval** (默认: 1分钟)
   - 服务器检查过期项目的频率
   - 较低的值使内存使用更准确
   - 较高的值减少CPU使用

5. **statsInterval** (默认: 30秒)
   - 缓存统计信息更新的频率
   - 影响命中/未命中率的准确性
   - 帮助监控缓存的有效性

## 它如何减少令牌消耗

内存缓存服务器通过自动存储原本需要在您和语言模型之间重新发送的数据来减少令牌消耗。您不需要做任何特别的事情 - 当您通过MCP客户端与任何语言模型交互时，缓存会自动发生。

以下是一些缓存示例：

### 1. 文件内容缓存
多次读取文件时：
- 第一次：完整读取文件内容并缓存
- 后续次数：从缓存中检索内容而不是重新读取文件
- 结果：重复文件操作使用的令牌更少

### 2. 计算结果
执行计算或分析时：
- 第一次：执行完整的计算并将结果缓存
- 后续次数：如果输入相同，则从缓存中检索结果
- 结果：重复计算使用的令牌更少

### 3. 常用数据
频繁访问的数据会被缓存，从而减少令牌消耗。

当多次需要相同的数据时：
- 第一次：数据被处理并缓存
- 随后的几次：从缓存中检索数据，直到TTL过期
- 结果：访问相同信息时使用的令牌更少

## 自动缓存管理

服务器通过以下方式自动管理缓存过程：
- 首次遇到数据时存储数据
- 在可用时提供缓存数据
- 根据设置移除旧的或未使用的数据
- 通过统计数据跟踪效果

## 优化技巧

### 1. 设置适当的TTL
- 对于经常变化的数据，TTL应较短
- 对于静态内容，TTL可以较长

### 2. 调整内存限制
- 更高以增加缓存（节省更多令牌）
- 如果担心内存使用，则降低

### 3. 监控缓存统计
- 命中率高 = 令牌节省良好
- 命中率低 = 调整TTL或限制

## 环境变量配置

您可以在MCP设置中使用环境变量来覆盖config.json中的设置：

```json
{
  "mcpServers": {
    "memory-cache": {
      "command": "node",
      "args": ["/path/to/build/index.js"],
      "env": {
        "MAX_ENTRIES": "5000",
        "MAX_MEMORY": "209715200",  // 200MB
        "DEFAULT_TTL": "7200",      // 2 hours
        "CHECK_INTERVAL": "120000",  // 2 minutes
        "STATS_INTERVAL": "60000"    // 1 minute
      }
    }
  }
}
```

您还可以指定自定义配置文件的位置：
```json
{
  "env": {
    "CONFIG_PATH": "/path/to/your/config.json"
  }
}
```

服务器将：
1. 在其目录中查找config.json
2. 应用任何环境变量覆盖
3. 如果两者均未指定，则使用默认值

## 实践中测试缓存

要查看缓存在实际中的工作情况，请尝试以下场景：

1. **文件读取测试**
   - 读取并分析一个大文件
   - 再次就该文件提出相同的问题
   - 第二次响应应该更快，因为文件内容已被缓存

2. **数据分析测试**
   - 对某些数据进行分析
   - 再次请求相同的分析
   - 第二次分析应使用缓存的结果

3. **项目导航测试**
   - 探索项目的结构
   - 再次查询相同的文件/目录
   - 目录列表和文件内容将从缓存中提供

当您注意到以下情况时，表示缓存正在工作：
- 重复操作的响应更快
- 关于不变内容的回答一致
- 不需要重新读取未更改的文件

**官方网站：** [https://github.com/ibproduct/ib-mcp-cache-server](https://github.com/ibproduct/ib-mcp-cache-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`memory`
- 标签：`knowledge and memory`, `developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`/path/to/ib-mcp-cache-server/build/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/ibproduct-ib-cache.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
