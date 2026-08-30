---
title: "无影 Agent 开发套件 AgentBay"
description: "无影AgentBay是AI 时代的Agent云基础设施， 面向企业、开发者、AI厂商，提供可一键配置的AI Agent任务执行工具和执行环境。您可以通过无影API或AgentBay MCP Server快速集成，并调用相关工具获取Serverless服务。"
---

# 无影 Agent 开发套件 AgentBay

无影AgentBay是AI 时代的Agent云基础设施， 面向企业、开发者、AI厂商，提供可一键配置的AI Agent任务执行工具和执行环境。您可以通过无影API或AgentBay MCP Server快速集成，并调用相关工具获取Serverless服务。

无影AgentBay是AI 时代的Agent云基础设施， 面向企业、开发者、AI厂商，提供可一键配置的AI Agent任务执行工具和执行环境。您可以通过无影API或AgentBay MCP Server快速集成，并调用相关工具获取Serverless服务。

## **产品大图**

![无影AgentBay产品大图](/mcp-assets/e5b3836b1d1e84f52bdbfad2d9779a7e.png)

## **云服务规格**

### **云资源**

目前您可通过购买[新人0.01元优惠](https://help.aliyun.com/zh/agentbay/product-overview/new-user-trial-instructions?spm=5176.30918410.J_WB32E9T-bokl57SJYCiyd.1.942e3c658LjrMW)开通使用（限新人），最大支持10个并发实例，服务地域将根据您的接入IP地址自动分配

无影 AgentBay SDK 已开源：[👉Star us on GitHub🌟](https://github.com/aliyun/wuying-agentbay-sdk)

### **产品优势**
1. **场景丰富，覆盖全面**

为智能体开发提供浏览器、代码、电脑、移动端四大核心环境，从网页自动化到代码编译，从桌面操作到移动应用控制，实现智能体全场景运行的环境支持。

2. **接入多样，集成灵活**

为智能体开发提供API、SDK和MCP三种接入方式，面向开发者友好且灵活，技术专家可深度定制，普通开发者也能快速上手，真正实现零门槛到专业化的全覆盖。

3. **基建强大，调度智能**

依托阿里云强大算力，实现秒级弹性伸缩与千级并发的运维能力，让开发者无需担心智能体运行所需的基础建设和运维难题，专注智能体创新开发的工作中。

## **操作步骤**

### 步骤1：创建API Key
1.  登录[AgentBay控制台](https://agentbay.console.aliyun.com/)。

2.  在左侧导航栏中单击**服务管理**。
    
3.  在**服务管理**页面上单击**创建API KEY**。
    
4.  在**创建API KEY**对话框中输入名称，并单击**确定**。
    
### 步骤2：根据您的需求选择合适的沙箱环境
1. 在服务管理页面上，在目标API KEY的操作列中单击**查看MCP地址**。
2. 目前支持的镜像类型和对应的IMAGEID如下:
+ Windows: windows_latest
+ Linux：linux_latest
+ Browser：browser_latest
+ Code：code_latest
+ Mobile：mobile_latest

### 步骤3：完成MCP服务配置
1. 返回魔搭——无影 Agent 开发套件 AgentBay——服务详情页面。
2. 在右侧的服务配置信息面板中选择 Remote，点击“配置”。也可以选择 Stdio，使用个人付费资源部署MCP服务。
3. 选择传输类型：AgentBay目前支持 SSE、Streamable HTTP、Stdio三种传输类型。推荐使用 SSE 和 Streamable HTTP。
4. 输入 无影AgentBay 的 APIKEY 和 IMAGEID。也可以根据自己的需求填写其他的 IMAGEID，您可以通过订阅 Pro 或 Ultra 权益包，创建自定义镜像，填写自定义的 IMAGEID。
5. Remote方式点击“连接”即可去试用，Stdio方式需选择“个人账号授权资源”进行部署。
6. 点击“试用”，跳转到“MCP实验场”页面后，开启无影AgentBay MCP服务，即可试用。

## 常见问题

### **Q1: 无影AgentBay是什么？是虚拟机吗？**

无影AgentBay不是简单的虚拟机，而是一个完整的AI Agent云基础设施平台。具体来说：

+   **定位**：它是阿里云推出的AI时代的Agent云基础设施，面向企业、开发者和AI厂商。
    
+   **核心功能**：
    
    +   标准Runtime：预集成大量面向Agent任务执行的标准工具，并以MCP封装，以便企业快速集成。
        
    +   用户状态持久化：通过无影自研的持久化架构，安全隔离地保存用户配置文件、Cookie等，并动态挂载，让云环境无限接近本地环境。
        
    +   实时端云交互：无影自研ASP协议可将云端画面实时串流到用户本地，让用户和AI可以交替控制云环境。且ASP支持网络和外设重定向通道，让云环境可以感知和控制本地设备。
        
+   **技术架构**：
    
    +   自研持久化文件系统，可动态按需保留用户状态和文件。
        
    +   自研ASP端云实时通信协议，让云环境可感知、模仿、控制本地环境。
        
    +   底层基于阿里云无影资源池，全球部署，就近接入。
        
    +   提供Serverless服务能力，客户可以一键调度环境会话。
        
    +   集成了Browser、File、Terminal等标准MCP工具集。
        
    +   支持通过SDK或者MCP Server快速接入，两者均兼容。
        

### **Q2: 市场上的AI Agent产品如何接入无影AgentBay？**

AI Agent产品可以通过以下方式接入无影AgentBay：

1.  **基础接入流程**：
    
    1.  申请API Key
        
    2.  完成自定义镜像制作和资源池定义配置（可选）
        
    3.  完成MCP服务配置（可选）
        
    4.  集成AgentBay SDK（可选）
        
    5.  客户端或服务端发起工具使用请求（会话调度）
        
2.  **接入方式**：
    
    +   通过AgentBay SDK接入
        
    +   通过MCP Server接入
        
3.  **访问方式**：
    
    +   支持客户端内嵌WebView串流云环境
        
    +   支持跳转浏览器使用
        
    +   访问格式：`https://wuying.aliyun.com?mcp.html?authcode=
&resourceId=`
        
        **说明**
        
        在发起工具调用时，该URL会由MCP Server返回。
        

### **Q3: 无影AgentBay支持MCP协议，和市场上的MCP Server之间是什么关系？**

无影AgentBay与MCP Server的关系如下：

+   **协议支持**：
    
    +   无影AgentBay完全支持MCP（Model Context Protocol）协议。
        
    +   提供标准化的MCP接口，确保与现有MCP生态兼容。
        
+   **工具集成**：
    
    提供主流的MCP工具集，包括但不限于：
    
    +   Browser工具：支持浏览器操作
        
    +   File工具：支持文件操作
        
    +   Terminal工具：支持终端操作
        
+   **生态关系**：
    
    +   可以与现有的MCP Server生态系统无缝集成。
        
    +   支持现有MCP Server的功能扩展。
        
    +   提供统一的接口标准，便于管理和集成。
        

### **Q4: 使用AI Agent时，我不想泄露个人隐私，无影AgentBay如何保障我的私人数据？**

无影AgentBay通过以下机制保障用户隐私和数据安全：

+   **隔离机制**：
    
    +   为每个用户提供完全隔离的VM环境。
        
    +   环境会话结束后即重置，不留存任何数据。
        
+   **访问控制**：
    
    +   通过API Key进行身份认证。
        
    +   提供安全的访问控制机制。
        
+   **数据处理**：
    
    +   本地数据不会上传到云端，云端数据不会被保留，除非用户明确授权和要求。
        
    +   提供安全的数据传输通道。
        
    +   支持数据加密存储。
        

### **Q5: Agent执行各种任务时经常消耗大量本地算力，我的电脑都不能做其他事了，无影AgentBay是否能解决这个问题？是如何解决的？**

无影AgentBay可以通过以下方式有效解决本地算力消耗问题：

+   **云端执行**：
    
    +   任务在阿里云的资源池中执行，不占用本地计算资源。
        
    +   提供Serverless服务，按需分配计算资源。
        
    +   支持弹性扩展，根据任务需求自动调整资源。
        
+   **资源优化**：
    
    +   采用云端分布式计算。
        
    +   支持任务并行处理。
        
    +   资源自动扩缩容。
        
+   **性能保障**：
    
    +   提供专业的云计算资源池。
        
    +   确保任务执行效率。
        
    +   本地设备只需要处理基础的交互操作。

**官方网站：** [https://help.aliyun.com/zh/agentbay/product-overview/](https://help.aliyun.com/zh/agentbay/product-overview/)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y wuying-agentbay-mcp-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/agentbay-wuying-agentbay.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
