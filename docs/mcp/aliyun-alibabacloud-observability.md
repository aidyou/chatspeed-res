---
title: "alibabacloud-observability-mcp-server"
description: "Alibaba Cloud Observability MCP Server provides a set of tools for accessing various products in Alibaba Cloud's observability suite. It covers products including Alibaba Cloud Log Service (SLS), Alib…"
---

# alibabacloud-observability-mcp-server

Alibaba Cloud Observability MCP Server provides a set of tools for accessing various products in Alibaba Cloud's observability suite. It covers products including Alibaba Cloud Log Service (SLS), Alib…

## AliCloud Observability MCP Service

  

  

### Introduction

The AliCloud Observability MCP Service provides a series of tools for accessing various AliCloud observability products, including AliCloud Log Service (SLS), AliCloud Application Real-Time Monitoring Service (ARMS), and AliCloud Cloud Monitoring. Any intelligent agent that supports the MCP protocol can quickly integrate with these services. The supported products are as follows:

- [AliCloud Log Service (SLS)](https://help.aliyun.com/zh/sls/product-overview/what-is-log-service)
- [AliCloud Application Real-Time Monitoring Service (ARMS)](https://help.aliyun.com/zh/arms/?scm=20140722.S_help@@%E6%96%87%E6%A1%A3@@34364._.RL_arms-LOC_2024NSHelpLink-OR_ser-PAR1_215042f917434789732438827e4665-V_4-P0_0-P1_0)

Currently, the MCP tools primarily focus on AliCloud Log Service, with support for other products to be added gradually. The detailed tools are as follows:

### Version History
You can view the version history.

##### Example Scenarios

- **Scenario One**: Quickly query the structure of a specific logstore
    - Tools used:
        - `sls_list_logstores`
        - `sls_describe_logstore`
    

- **Scenario Two**: Fuzzy query to find the application with the highest traffic in a specific logstore over the past day
    - Analysis:
        - Determine if the logstore exists
        - Retrieve the logstore structure
        - Generate a query statement based on requirements (users can confirm and modify the statement)
        - Execute the query statement
        - Generate a response based on the query results
    - Tools used:
        - `sls_list_logstores`
        - `sls_describe_logstore`
        - `sls_translate_natural_language_to_query`
        - `sls_execute_query`
    

- **Scenario Three**: Query the slowest traces for a specific application in ARMS
    - Analysis:
        - Determine if the application exists
        - Retrieve the application structure
        - Generate a query statement based on requirements (users can confirm and modify the statement)
        - Execute the query statement
        - Generate a response based on the query results
    - Tools used:
        - `arms_search_apps`
        - `arms_generate_trace_query`
        - `sls_translate_natural_language_to_query`
        - `sls_execute_query`
    

### Permission Requirements

To ensure that the MCP Server can successfully access and operate your AliCloud observability resources, you need to configure the following permissions:

1. **AliCloud Access Key (AccessKey)**:
    * The service requires a valid AliCloud AccessKey ID and AccessKey Secret.
    * For information on obtaining and managing AccessKeys, refer to the [official AliCloud AccessKey management documentation](https://help.aliyun.com/document_detail/53045.html).

2. If you do not provide an AccessKey and AccessKey Secret during initialization, the default credential chain will be used for login:
   1. If both `ALIBABA_CLOUD_ACCESS_KEY_ID` and `ALIBABA_CLOUD_ACCESS_KEY_SECRET` environment variables exist and are non-empty, they will be used as the default credentials.
   2. If `ALIBABA_CLOUD_ACCESS_KEY_ID`, `ALIBABA_CLOUD_ACCESS_KEY_SECRET`, and `ALIBABA_CLOUD_SECURITY_TOKEN` are all set, the STS Token will be used as the default credentials.

3. **RAM Authorization (Important)**:
    * The RAM user or role associated with the AccessKey **must** be granted the necessary permissions to access the relevant cloud services.
    * **Strongly recommended to follow the "least privilege principle"**: Grant only the minimum set of permissions required to run the MCP tools you plan to use, to minimize security risks.
    * Based on the tools you need to use, refer to the following documentation for permission configuration:
        * **Log Service (SLS)**: If you need to use `sls_*` related tools, refer to the [Log Service permission documentation](https://help.aliyun.com/zh/sls/overview-8) and grant the necessary read, query, etc., permissions.
        * **Application Real-Time Monitoring Service (ARMS)**: If you need to use `arms_*` related tools, refer to the [ARMS permission documentation](https://help.aliyun.com/zh/arms/security-and-compliance/overview-8?scm=20140722.H_74783._.OR_help-T_cn~zh-V_1) and grant the necessary query permissions.
    * Configure the required permissions based on your actual use case.

### Security and Deployment Recommendations

Please pay attention to the following security matters and best practices for deployment:

1. **Key Security**:
    * The MCP Server will use the AccessKey you provide to call AliCloud OpenAPI, but it **will not store your AccessKey in any form** and will not use it for any purposes other than the designed functionality.

2. **Access Control (Critical)**:

*   When you choose to access the MCP Server via the **SSE (Server-Sent Events) protocol**, **you are responsible for managing access control and security for this service endpoint**.
*   **It is strongly recommended** to deploy the MCP Server in an **internal network or trusted environment**, such as within your private VPC (Virtual Private Cloud), to avoid direct exposure to the public internet.
*   The recommended deployment method is to use **Alibaba Cloud Function Compute (FC)** and configure its network settings to **VPC-only access** to achieve network isolation and security.
*   **Note**: **Do not** expose the MCP Server SSE endpoint configured with your AccessKey on the public internet without any authentication or access control mechanisms, as this will pose a significant security risk.

### Usage Instructions

Before using the MCP Server, you need to obtain the Alibaba Cloud AccessKeyId and AccessKeySecret. Please refer to [Alibaba Cloud AccessKey Management](https://help.aliyun.com/document_detail/53045.html).

#### Installation Using pip
> ⚠️ Requires Python 3.10 or later.

You can install it directly using pip. The installation command is as follows:

bash
pip install mcp-server-aliyun-observability

1. After installation, you can run it directly. The run command is as follows:

bash
python -m mcp_server_aliyun_observability --transport sse --access-key-id  --access-key-secret 

You can pass specific parameters via the command line:
- `--transport` specifies the transport method, which can be `sse` or `stdio`. The default value is `stdio`.
- `--access-key-id` specifies the Alibaba Cloud AccessKeyId. If not specified, it will use the `ALIBABA_CLOUD_ACCESS_KEY_ID` environment variable.
- `--access-key-secret` specifies the Alibaba Cloud AccessKeySecret. If not specified, it will use the `ALIBABA_CLOUD_ACCESS_KEY_SECRET` environment variable.
- `--log-level` specifies the log level, which can be `DEBUG`, `INFO`, `WARNING`, or `ERROR`. The default value is `INFO`.
- `--transport-port` specifies the transport port. The default value is `8000`, and it is only effective when `--transport` is set to `sse`.

2. Start using the `uv` command

bash
uv run mcp-server-aliyun-observability

### Installation from Source Code

bash
# Clone the source code
git clone git@github.com:aliyun/alibabacloud-observability-mcp-server.git
# Enter the source code directory
cd alibabacloud-observability-mcp-server
# Install
pip install -e .
# Run
python -m mcp_server_aliyun_observability --transport sse --access-key-id  --access-key-secret 

### AI Tool Integration

> Example using the SSE startup method, with the transport port set to 8888. Adjust according to your actual usage.

#### Integration with Cursor, Cline, etc.
1. Using the SSE startup method
json
{
  "mcpServers": {
    "alibaba_cloud_observability": {
      "url": "http://localhost:7897/sse"
    }
  }
}

2. Using the stdio startup method
   Start directly from the source code directory, note:
   1. You need to specify the `--directory` parameter to indicate the source code directory, preferably using an absolute path.
   2. It is best to use an absolute path for the `uv` command. If using a virtual environment, use the absolute path of the virtual environment.
json
{
  "mcpServers": {
    "alibaba_cloud_observability": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/your/alibabacloud-observability-mcp-server",
        "run",
        "mcp-server-aliyun-observability"
      ],
      "env": {
        "ALIBABA_CLOUD_ACCESS_KEY_ID": "",
        "ALIBABA_CLOUD_ACCESS_KEY_SECRET": ""
      }
    }
  }
}

3. Using the stdio startup method - starting from a module
json
{
  "mcpServers": {
    "alibaba_cloud_observability": {
      "command": "uv",
      "args": [
        "run",
        "mcp-server-aliyun-observability"
      ],
      "env": {
        "ALIBABA_CLOUD_ACCESS_KEY_ID": "",
        "ALIBABA_CLOUD_ACCESS_KEY_SECRET": ""
      }
    }
  }
}

#### Cherry Studio Integration

#### Cursor Integration

#### ChatWise Integration

Sure, here is the translation of the provided Chinese technical document into English, while strictly maintaining the code blocks, links, and format structure:

If you have the actual content of the document, please provide it, and I will translate it accordingly. The images are retained as they are.

**Official site: ** [https://github.com/aliyun/alibabacloud-observability-mcp-server](https://github.com/aliyun/alibabacloud-observability-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `developer tools`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uv`
- Args: `--directory yourpath/alibabacloud-observability-mcp-server run mcp-server-aliyun-observability`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/aliyun-alibabacloud-observability.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
