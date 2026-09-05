---
title: "wuying-agentbay-mcp-server"
description: "无影AgentBay是AI 时代的Agent云基础设施， 面向企业、开发者、AI厂商，提供可一键配置的AI Agent任务执行工具和执行环境。您可以通过无影API或AgentBay MCP Server快速集成，并调用相关工具获取Serverless服务。"
---

# wuying-agentbay-mcp-server

无影AgentBay是AI 时代的Agent云基础设施， 面向企业、开发者、AI厂商，提供可一键配置的AI Agent任务执行工具和执行环境。您可以通过无影API或AgentBay MCP Server快速集成，并调用相关工具获取Serverless服务。

AgentBay of the Invisible is the AI era's cloud infrastructure for Agents, designed for enterprises, developers, and AI vendors. It provides a one-click configurable AI Agent task execution tool and environment. You can quickly integrate and call related tools to obtain Serverless services through the Invisible API or AgentBay MCP Server.

## **Product Overview**

![Invisible AgentBay Product Overview](/mcp-assets/e5b3836b1d1e84f52bdbfad2d9779a7e.png)

## **Cloud Service Specifications**

### **Cloud Resources**

Currently, you can activate usage by purchasing the [New User 0.01 RMB Offer](https://help.aliyun.com/zh/agentbay/product-overview/new-user-trial-instructions?spm=5176.30918410.J_WB32E9T-bokl57SJYCiyd.1.942e3c658LjrMW) (limited to new users), supporting up to 10 concurrent instances. The service region will be automatically assigned based on your access IP address.

The Invisible AgentBay SDK is open-source: [👉Star us on GitHub🌟](https://github.com/aliyun/wuying-agentbay-sdk)

### **Product Advantages**
1. **Rich Scenarios, Comprehensive Coverage**

Provides four core environments—browser, code, PC, and mobile—for agent development, covering everything from web automation to code compilation, and from desktop operations to mobile app control, ensuring full-scenario support for agent operation.

2. **Diverse Integration, Flexible Configuration**

Offers three integration methods—API, SDK, and MCP—for agent development, catering to both technical experts who can deeply customize and general developers who can get started quickly, truly achieving a zero-threshold to professional-level coverage.

3. **Powerful Infrastructure, Intelligent Scheduling**

Leveraging the powerful computing capabilities of Alibaba Cloud, it achieves second-level elastic scaling and maintenance capabilities for thousands of concurrent operations, allowing developers to focus on innovative agent development without worrying about the underlying infrastructure and operational challenges.

## **Operation Steps**

### Step 1: Create an API Key
1. Log in to the [AgentBay Console](https://agentbay.console.aliyun.com/).

2. Click **Service Management** in the left navigation bar.
    
3. On the **Service Management** page, click **Create API KEY**.
    
4. In the **Create API KEY** dialog box, enter the name and click **OK**.
    
### Step 2: Select the Appropriate Sandbox Environment Based on Your Needs
1. On the Service Management page, click **View MCP Address** in the operation column of the target API KEY.
2. The currently supported image types and corresponding IMAGEIDs are as follows:
+ Windows: windows_latest
+ Linux: linux_latest
+ Browser: browser_latest
+ Code: code_latest
+ Mobile: mobile_latest

### Step 3: Complete MCP Service Configuration
1. Return to the ModelScope - Invisible Agent Development Kit AgentBay - Service Details page.
2. In the right-side Service Configuration Information panel, select Remote and click "Configure". Alternatively, you can choose Stdio to deploy the MCP service using personal paid resources.
3. Choose the transmission type: AgentBay currently supports SSE, Streamable HTTP, and Stdio. SSE and Streamable HTTP are recommended.
4. Enter the APIKEY and IMAGEID for Invisible AgentBay. You can also fill in other IMAGEIDs according to your needs. You can create custom images by subscribing to Pro or Ultra packages and filling in the custom IMAGEID.
5. For the Remote method, click "Connect" to try it out. For the Stdio method, select "Personal Account Authorized Resources" for deployment.
6. Click "Try", and after being redirected to the "MCP Playground" page, start the Invisible AgentBay MCP service to try it out.

## Frequently Asked Questions

### **Q1: What is Invisible AgentBay? Is it a virtual machine?**

Invisible AgentBay is not simply a virtual machine but a complete AI Agent cloud infrastructure platform. Specifically:

+   **Positioning**: It is an AI-era Agent cloud infrastructure launched by Alibaba Cloud, aimed at enterprises, developers, and AI vendors.
    
+   **Core Functions**:
    
    +   Standard Runtime: Pre-integrates a large number of standard tools for Agent task execution, packaged in MCP for quick enterprise integration.
        
    +   User State Persistence: Through the self-developed persistence architecture of the Invisible, user configuration files, cookies, etc., are securely isolated and saved, and dynamically mounted, making the cloud environment infinitely close to the local environment.
        
    +   Real-time End-Cloud Interaction: The self-developed ASP protocol of the Invisible can stream the cloud screen in real time to the user's local end, allowing users and AI to alternately control the cloud environment. Additionally, ASP supports network and peripheral redirection channels, enabling the cloud environment to sense and control local devices.
        
+   **Technical Architecture**:
    
    +   Self-developed persistent file system that can dynamically retain user states and files as needed.+   Self-developed ASP end-cloud real-time communication protocol, making the cloud environment perceptible, imitable, and controllable for the local environment.
    
+   Based on Alibaba Cloud's Wuying resource pool, globally deployed with nearby access.
    
+   Provides Serverless service capabilities, allowing customers to schedule environment sessions with one click.
    
+   Integrates standard MCP toolsets such as Browser, File, and Terminal.
    
+   Supports quick integration via SDK or MCP Server, both of which are compatible.

### **Q2: How can AI Agent products in the market integrate with Wuying AgentBay?**

AI Agent products can integrate with Wuying AgentBay through the following methods:

1.  **Basic Integration Process**:
    
    1.  Apply for an API Key
        
    2.  Complete the custom image creation and resource pool definition configuration (optional)
        
    3.  Complete the MCP service configuration (optional)
        
    4.  Integrate the AgentBay SDK (optional)
        
    5.  Initiate a tool usage request from the client or server (session scheduling)
        
2.  **Integration Methods**:
    
    +   Through the AgentBay SDK
        
    +   Through the MCP Server
        
3.  **Access Methods**:
    
    +   Supports embedding WebView in the client to stream the cloud environment
        
    +   Supports using a browser for access
        
    +   Access format: `https://wuying.aliyun.com?mcp.html?authcode=
&resourceId=`
        
        **Note**
        
        This URL will be returned by the MCP Server when initiating a tool call.

### **Q3: Wuying AgentBay supports the MCP protocol; what is its relationship with MCP Servers available in the market?**

The relationship between Wuying AgentBay and MCP Servers is as follows:

+   **Protocol Support**:
    
    +   Wuying AgentBay fully supports the MCP (Model Context Protocol) protocol.
        
    +   Provides standardized MCP interfaces to ensure compatibility with the existing MCP ecosystem.
        
+   **Tool Integration**:
    
    Offers mainstream MCP toolsets, including but not limited to:
    
    +   Browser tool: supports browser operations
        
    +   File tool: supports file operations
        
    +   Terminal tool: supports terminal operations
        
+   **Ecosystem Relationship**:
    
    +   Can seamlessly integrate with the existing MCP Server ecosystem.
        
    +   Supports functional extensions of existing MCP Servers.
        
    +   Provides a unified interface standard for easy management and integration.

### **Q4: When using AI Agents, I don't want to leak personal privacy. How does Wuying AgentBay protect my private data?**

Wuying AgentBay ensures user privacy and data security through the following mechanisms:

+   **Isolation Mechanism**:
    
    +   Provides a completely isolated VM environment for each user.
        
    +   The environment session is reset after completion, leaving no data behind.
        
+   **Access Control**:
    
    +   Authenticates identity through API Keys.
        
    +   Provides secure access control mechanisms.
        
+   **Data Handling**:
    
    +   Local data is not uploaded to the cloud, and cloud data is not retained unless explicitly authorized and requested by the user.
        
    +   Provides secure data transmission channels.
        
    +   Supports encrypted data storage.

### **Q5: When agents execute various tasks, they often consume a lot of local computing power, making it difficult to do other things on my computer. Can Wuying AgentBay solve this problem, and if so, how?**

Wuying AgentBay can effectively address the issue of local computing power consumption through the following methods:

+   **Cloud Execution**:
    
    +   Tasks are executed in Alibaba Cloud's resource pool, without occupying local computing resources.
        
    +   Provides Serverless services, allocating computing resources on demand.
        
    +   Supports elastic scaling, automatically adjusting resources based on task requirements.
        
+   **Resource Optimization**:
    
    +   Utilizes cloud-based distributed computing.
        
    +   Supports parallel task processing.
        
    +   Automatically scales resources up or down.
        
+   **Performance Assurance**:
    
    +   Provides professional cloud computing resource pools.
        
    +   Ensures efficient task execution.
        
    +   Local devices only need to handle basic interaction operations.

**Official site: ** [https://help.aliyun.com/zh/agentbay/product-overview/](https://help.aliyun.com/zh/agentbay/product-overview/)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `developer tools`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y wuying-agentbay-mcp-server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/agentbay-wuying-agentbay.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
