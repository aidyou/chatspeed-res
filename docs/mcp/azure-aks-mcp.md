---
title: "Azure Kubernetes Service MCP"
description: "AKS-MCP The AKS-MCP is a Model Context Protocol (MCP) server that enables AI assistants to interact with Azure Kubernetes Service (AKS) clusters. It serves as a bridge between AI tools (like GitHub Co…"
---

# Azure Kubernetes Service MCP

AKS-MCP The AKS-MCP is a Model Context Protocol (MCP) server that enables AI assistants to interact with Azure Kubernetes Service (AKS) clusters. It serves as a bridge between AI tools (like GitHub Co…

# AKS-MCP


The AKS-MCP is a Model Context Protocol (MCP) server that enables AI assistants
to interact with Azure Kubernetes Service (AKS) clusters. It serves as a bridge
between AI tools (like GitHub Copilot, Claude, and other MCP-compatible AI
assistants) and AKS, translating natural language requests into AKS operations
and returning the results in a format the AI tools can understand.

It allows AI tools to:

- Operate (CRUD) AKS resources
- Retrieve details related to AKS clusters (VNets, Subnets, NSGs, Route Tables, etc.)
- Manage Azure Fleet operations for multi-cluster scenarios

## Supported Deployment Model and Security Considerations

**AKS-MCP is designed to be run locally, by a single trusted user, as a bridge
between that user's own AI assistant and their own Azure/AKS resources.** This
is the only deployment model the project supports and hardens for.

### The trust boundary

AKS-MCP executes command-line tools — including `az`, `kubectl`, `helm`,
`cilium`, and `hubble` — **using the identity of the process it runs as**. It
does not perform per-caller authorization, and it does not attempt to sandbox
the commands it runs. Therefore:

> **Anyone who can invoke AKS-MCP tools effectively has the full Azure and
> Kubernetes privileges of the identity AKS-MCP is running under.**

This includes the ability to obtain reusable credentials. For example, in
`readwrite` or `admin` mode a caller can reach Azure Resource Manager and AKS
with the server identity's full authority, and `kubectl` or `helm` can be used
to read Secrets, mint service account tokens, or deploy arbitrary workloads
into the cluster. This is an inherent consequence of exposing a CLI execution
surface — it is not prevented by `--access-level`.

Specific credential-returning Azure CLI commands (such as
`az account get-access-token` and `az aks get-credentials`) are rejected by an
explicit denylist. That denylist reduces accidental exposure — it is **not** a
security boundary, it does not cover the `kubectl`, `helm`, `cilium`, or
`hubble` surfaces, and it must not be relied upon to contain an untrusted
caller.

**Treat the ability to call AKS-MCP as equivalent to handing over a shell that
is already logged in as the server identity.**

### Network exposure and local authority

Removing HTTP/SSE transports and the official remote deployment artifacts
removes the supported network-reachable service and its remote-caller threat
model. In the supported configuration, AKS-MCP has no listener that accepts
requests from the network.

This does **not** make the local MCP client, its prompts, or `--access-level`
an authorization boundary. A person or process that controls the local client,
its server configuration, or AKS-MCP can normally run the same CLI commands
under the same identity without AKS-MCP. Protecting the workstation, client
configuration, and local credentials remains the operator's responsibility.

### What `--access-level` is and is not

`--access-level` (`readonly` / `readwrite` / `admin`) is a **guardrail to reduce
accidental damage** from an AI assistant that misinterprets a request. It is
**not** a security boundary against a deliberately malicious caller, and it must
not be relied upon to contain an untrusted party. Do not expose AKS-MCP to
callers you would not grant the underlying Azure/Kubernetes credentials to
directly.

### Recommended (supported) setup

- Run as a local subprocess, launched on demand by your local MCP client.
- Authenticate with your own developer identity via `az login`.
- Grant the identity only the Azure/Kubernetes permissions you actually need.

### Unsupported deployment models

AKS-MCP supports only stdio and must be launched as a local subprocess by an
MCP client. Do not expose it through HTTP, SSE, a container service, Helm,
Kubernetes, a proxy, or a gateway. Any third-party bridge is outside the
project's security and support boundary.

## How it works

AKS-MCP connects to Azure using the Azure SDK and provides a set of tools that
AI assistants can use to interact with AKS resources. It leverages the Model
Context Protocol (MCP) to facilitate this communication, enabling AI tools to
make API calls to Azure and interpret the responses.

## Azure CLI Authentication

AKS-MCP uses Azure CLI (az) for AKS operations. Azure CLI authentication is attempted in this order:

1. Service Principal (client secret): When `AZURE_CLIENT_ID`, `AZURE_CLIENT_SECRET`, `AZURE_TENANT_ID` environment variables are present, a service principal login is performed using the following command: `az login --service-principal -u CLIENT_ID -p CLIENT_SECRET --tenant TENANT_ID`

1. Workload Identity (federated token): When `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_FEDERATED_TOKEN_FILE` environment variables are present, a federated token login is performed using the following command: `az login --service-principal -u CLIENT_ID --tenant TENANT_ID --federated-token TOKEN`

1. User-assigned Managed Identity (managed identity client ID): When only `AZURE_CLIENT_ID` environment variable is present, a user-assigned managed identity login is performed using the following command: `az login --identity -u CLIENT_ID`

1. System-assigned Managed Identity: When `AZURE_MANAGED_IDENTITY` is set to `system`, a system-assigned managed identity login is performed using the following command: `az login --identity`

1. Existing Login: When none of the above environment variables are set, AKS-MCP assumes you have already authenticated (for example, via `az login`) and uses the existing session.

Optional subscription selection:

- If `AZURE_SUBSCRIPTION_ID` is set, AKS-MCP will run `az account set --subscription SUBSCRIPTION_ID` after login.

Notes and security:

- The federated token file must be exactly `/var/run/secrets/azure/tokens/azure-identity-token` and is strictly validated; other paths are rejected.
- After each login, AKS-MCP verifies authentication with `az account show --query id -o tsv`.
- Ensure the Azure CLI is installed and on PATH.

Environment variables used:

- `AZURE_TENANT_ID`
- `AZURE_CLIENT_ID`
- `AZURE_CLIENT_SECRET`
- `AZURE_FEDERATED_TOKEN_FILE`
- `AZURE_SUBSCRIPTION_ID`
- `AZURE_MANAGED_IDENTITY` (set to `system` to opt into system-assigned managed identity)

## Available Tools

The AKS-MCP server provides consolidated tools for interacting with AKS
clusters. By default, the server uses **unified tools** (`call_az` for Azure operations and `call_kubectl` for Kubernetes operations) which provide a more flexible interface. For backward compatibility, you can enable **legacy specialized tools** by setting the environment variable `USE_LEGACY_TOOLS=true`.

Some tools will require read-write or admin permissions to run debugging pods on your cluster. To enable read-write or admin permissions for the AKS-MCP server, add the **access level** parameter to your MCP configuration file:

1. Navigate to your **mcp.json** file, or go to MCP: List Servers -> AKS-MCP -> Show Configuration Details in the **Command Palette** (For VSCode; `Ctrl+Shift+P` on Windows/Linux or `Cmd+Shift+P` on macOS).
2. In the "args" section of AKS-MCP, add the following parameters: "--access-level", "readwrite" / "admin"

For example:
```
"args": [
  "--access-level",
  "readwrite"
]
```

These tools have been designed to provide comprehensive functionality
through unified interfaces:

Azure CLI Operations (Unified Tool)

**Tool:** `call_az` *(default, available when `USE_LEGACY_TOOLS` is not set or set to `false`)*

Unified tool for executing Azure CLI commands directly. This tool provides a flexible interface to run any Azure CLI command.

**Parameters:**
- `cli_command`: The complete Azure CLI command to execute (e.g., `az aks list --resource-group myRG`, `az vm list --subscription `)
- `timeout`: Optional timeout in seconds (default: 120)

**Example Usage:**
```json
{
  "cli_command": "az aks list --resource-group myResourceGroup --output json"
}
```

**Access Control:**
- **readonly**: Only read operations are allowed
- **readwrite/admin**: Both read and write operations are allowed

**Important:** Commands must be simple Azure CLI invocations without shell features like pipes (|), redirects (>, 

AKS Cluster Management (Legacy Tool)

**Tool:** `az_aks_operations` *(available when `USE_LEGACY_TOOLS=true`)*

Unified tool for managing Azure Kubernetes Service (AKS) clusters and related operations.

**Available Operations:**

- **Read-Only** (all access levels):
  - `show`: Show cluster details
  - `list`: List clusters in subscription/resource group
  - `get-versions`: Get available Kubernetes versions
  - `check-network`: Perform outbound network connectivity check
  - `nodepool-list`: List node pools in cluster
  - `nodepool-show`: Show node pool details
  - `account-list`: List Azure subscriptions

- **Read-Write** (`readwrite`/`admin` access levels):
  - `create`: Create new cluster
  - `delete`: Delete cluster
  - `scale`: Scale cluster node count
  - `start`: Start a stopped cluster
  - `stop`: Stop a running cluster
  - `update`: Update cluster configuration
  - `upgrade`: Upgrade Kubernetes version
  - `nodepool-add`: Add node pool to cluster
  - `nodepool-delete`: Delete node pool
  - `nodepool-scale`: Scale node pool
  - `nodepool-upgrade`: Upgrade node pool
  - `account-set`: Set active subscription
  - `login`: Azure authentication

- **Admin-Only** (`admin` access level):
  - `get-credentials`: Get cluster credentials for kubectl access

Network Resource Management

**Tool:** `aks_network_resources`

Unified tool for getting Azure network resource information used by AKS clusters.

**Available Resource Types:**

- `all`: Get information about all network resources
- `vnet`: Virtual Network information
- `subnet`: Subnet information
- `nsg`: Network Security Group information
- `route_table`: Route Table information
- `load_balancer`: Load Balancer information
- `private_endpoint`: Private endpoint information

Monitoring and Diagnostics

**Tool:** `aks_monitoring`

Unified tool for Azure monitoring and diagnostics operations for AKS clusters.

**Available Operations:**

- `metrics`: List metric values for resources
- `resource_health`: Retrieve resource health events for AKS clusters
- `app_insights`: Execute KQL queries against Application Insights telemetry data
- `diagnostics`: Check if AKS cluster has diagnostic settings configured
- `control_plane_logs`: Query AKS control plane logs with safety constraints
  and time range validation

Compute Resources

**Tool:** `get_aks_vmss_info`

- Get detailed VMSS configuration for node pools in the AKS cluster

**Tool:** `collect_aks_node_logs`

Collect system logs from AKS VMSS nodes for debugging and troubleshooting.

**Parameters:**
- `aks_resource_id`: AKS cluster resource ID
- `vmss_name`: VMSS name (obtain from `get_aks_vmss_info` or `kubectl get nodes`)
- `instance_id`: VMSS instance ID
- `log_type`: Type of logs to collect (`kubelet`, `containerd`, `kernel`, `syslog`)
- `lines`: Number of recent log lines to return (default: 500, max: 2000)
- `since`: Time range for logs (e.g., `1h`, `30m`, `2d`) - takes precedence over `lines`
- `level`: Log level filter (`ERROR`, `WARN`, `INFO`)
- `filter`: Filter logs by keyword (case-insensitive text match)

**Example Usage:**
```json
{
  "aks_resource_id": "/subscriptions/.../managedClusters/myAKS",
  "vmss_name": "aks-nodepool1-12345678-vmss",
  "instance_id": "0",
  "log_type": "kubelet",
  "since": "1h",
  "level": "ERROR",
  "filter": "ImagePullBackOff"
}
```

**Limitations:**
- Only supports Linux VMSS nodes (Windows nodes and standalone VMs are not supported yet)
- Only one run command can execute at a time per VMSS instance

**Tool:** `az_compute_operations`

Unified tool for managing Azure Virtual Machines (VMs) and Virtual Machine Scale Sets (VMSS) used by AKS.

**Available Operations:**

- `show`: Get details of a VM/VMSS
- `list`: List VMs/VMSS in subscription or resource group
- `get-instance-view`: Get runtime status
- `start`: Start VM
- `stop`: Stop VM
- `restart`: Restart VM/VMSS instances
- `reimage`: Reimage VMSS instances (VM not supported for reimage)

**Resource Types:** `vm` (single virtual machines), `vmss` (virtual machine scale sets)

Fleet Management

**Tool:** `az_fleet`

Comprehensive Azure Fleet management for multi-cluster scenarios.

**Available Operations:**

- **Fleet Operations**: list, show, create, update, delete, get-credentials
- **Member Operations**: list, show, create, update, delete
- **Update Run Operations**: list, show, create, start, stop, delete
- **Update Strategy Operations**: list, show, create, delete
- **ClusterResourcePlacement Operations**: list, show, get, create, delete

Supports both Azure Fleet management and Kubernetes ClusterResourcePlacement
CRD operations.

Diagnostic Detectors

**Tool:** `aks_detector`

Unified tool for executing AKS diagnostic detector operations.

**Available Operations:**

- `list`: List all available AKS cluster detectors
- `run`: Run a specific AKS diagnostic detector
- `run_by_category`: Run all detectors in a specific category

**Parameters:**

- `operation` (required): Operation to perform (`list`, `run`, or `run_by_category`)
- `aks_resource_id` (required): AKS cluster resource ID
- `detector_name` (required for `run` operation): Name of the detector to run
- `category` (required for `run_by_category` operation): Detector category
- `start_time` (required for `run` and `run_by_category` operations): Start time in UTC ISO format (within last 30 days)
- `end_time` (required for `run` and `run_by_category` operations): End time in UTC ISO format (within last 30 days, max 24h from start)

**Available Categories:**

- Best Practices
- Cluster and Control Plane Availability and Performance
- Connectivity Issues
- Create, Upgrade, Delete and Scale
- Deprecations
- Identity and Security
- Node Health
- Storage

**Example Usage:**

```json
{
  "operation": "list",
  "aks_resource_id": "/subscriptions/xxx/resourceGroups/xxx/providers/Microsoft.ContainerService/managedClusters/xxx"
}
```

```json
{
  "operation": "run",
  "aks_resource_id": "/subscriptions/xxx/resourceGroups/xxx/providers/Microsoft.ContainerService/managedClusters/xxx",
  "detector_name": "node-health-detector",
  "start_time": "2025-01-15T10:00:00Z",
  "end_time": "2025-01-15T12:00:00Z"
}
```

Azure Advisor

**Tool:** `aks_advisor_recommendation`

Retrieve and manage Azure Advisor recommendations for AKS clusters.

**Available Operations:**

- `list`: List recommendations with filtering options
- `report`: Generate recommendation reports
- **Filter Options**: resource_group, cluster_names, category (Cost,
  HighAvailability, Performance, Security), severity (High, Medium, Low)

Kubernetes Operations

*Note: All Kubernetes tools (kubectl, helm, cilium, hubble) are enabled by default. Use `--enabled-components` to selectively enable specific components.*

### Unified kubectl Tool (Default)

**Tool:** `call_kubectl` *(default, available when `USE_LEGACY_TOOLS` is not set or set to `false`)*

Unified tool for executing kubectl commands directly. This tool provides a flexible interface to run any `kubectl` command with full argument support.

**Parameters:**
- `args`: The kubectl command arguments (e.g., `get pods`, `describe node mynode`, `apply -f deployment.yaml`)

**Example Usage:**
```json
{
  "args": "get pods -n kube-system -o wide"
}
```

**Access Control:** Operations are restricted based on the configured access level:
- **readonly**: Only read operations (get, describe, logs, etc.) are allowed
- **readwrite/admin**: All operations including mutating commands (create, delete, apply, etc.)

### Legacy kubectl Tools (Specialized)

**Available when `USE_LEGACY_TOOLS=true`:**

- **Read-Only** (all access levels):
  - `kubectl_resources`: View resources (get, describe) - filtered to read-only operations in readonly mode
  - `kubectl_diagnostics`: Debug and diagnose (logs, events, top, exec, cp)
  - `kubectl_cluster`: Cluster information (cluster-info, api-resources, api-versions, explain)
  - `kubectl_config`: Configuration management (diff, auth, config) - filtered to read-only operations in readonly mode

- **Read-Write/Admin** (`readwrite`/`admin` access levels):
  - `kubectl_resources`: Full resource management (get, describe, create, delete, apply, patch, replace, cordon, uncordon, drain, taint)
  - `kubectl_workloads`: Workload lifecycle (run, expose, scale, autoscale, rollout)
  - `kubectl_metadata`: Metadata management (label, annotate, set)
  - `kubectl_config`: Full configuration management (diff, auth, certificate, config)

### Helm

**Tool:** `call_helm`

Helm package manager for Kubernetes.

### Cilium

**Tool:** `call_cilium`

Cilium CLI for eBPF-based networking and security.

### Hubble

**Tool:** `call_hubble`

Hubble network observability for Cilium.

Real-time Observability

**Tool:** `inspektor_gadget_observability`

Real-time observability tool for Azure Kubernetes Service (AKS) clusters using
eBPF.

**Available Actions:**

- `deploy`: Deploy Inspektor Gadget to the cluster (via the AKS cluster extension)
- `undeploy`: Remove the Inspektor Gadget cluster extension from the cluster
- `is_deployed`: Check deployment status
- `run`: Run one-shot gadgets
- `start`: Start continuous gadgets
- `stop`: Stop running gadgets
- `get_results`: Retrieve gadget results
- `list_gadgets`: List available gadgets

**Available Gadgets:**

- `observe_dns`: Monitor DNS requests and responses
- `observe_tcp`: Monitor TCP connections
- `observe_file_open`: Monitor file system operations
- `observe_process_execution`: Monitor process execution
- `observe_signal`: Monitor signal delivery
- `observe_system_calls`: Monitor system calls
- `top_file`: Top files by I/O operations
- `top_tcp`: Top TCP connections by traffic
- `tcpdump`: Capture network packets

## How to install

### Prerequisites

1. Set up [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) and authenticate:

```bash
   az login
```

### VS Code with GitHub Copilot (Recommended)

 One-Click Installation with the AKS Extension 

The easiest way to get started with AKS-MCP is through the **Azure Kubernetes Service Extension for VS Code**.

#### Step 1: Install the AKS Extension

1. Open VS Code and go to Extensions (`Ctrl+Shift+X` on Windows/Linux or `Cmd+Shift+X` on macOS).
1. Search for [Azure Kubernetes Service](https://marketplace.visualstudio.com/items?itemName=ms-kubernetes-tools.vscode-aks-tools).
1. Install the official Microsoft AKS extension.

#### Step 2: Launch the AKS-MCP Server

1. Open the **Command Palette** (`Ctrl+Shift+P` on Windows/Linux or `Cmd+Shift+P` on macOS).
2. Search and run: **AKS: Setup AKS MCP Server**.

Upon successful installation, the server will now be visible in **MCP: List Servers** (via Command Palette). From there, you can start the MCP server or view its status.

#### Step 3: Start Using AKS-MCP

Once started, the MCP server will appear in the **Copilot Chat: Configure Tools** dropdown under `MCP Server: AKS MCP`, ready to enhance contextual prompts based on your AKS environment. By default, all AKS-MCP server tools are enabled. You can review the list of available tools and disable any that are not required for your specific scenario.

Try a prompt like *"List all my AKS clusters"*, which will start using tools from the AKS-MCP server.

#### WSL Configuration

The MCP configuration differs depending on whether VS Code is running on Windows or inside WSL:

**🪟 Windows Host (VS Code on Windows)**: Use `"command": "wsl"` to invoke the WSL binary from Windows:

```json
{
  "servers": {
    "aks-mcp": {
      "type": "stdio",
      "command": "wsl",
      "args": [
        "--",
        "/home/you/.vs-kubernetes/tools/aks-mcp/aks-mcp"
      ]
    }
  }
}
```

**🐧 Remote-WSL (VS Code running inside WSL)**: Call the binary directly or use a shell wrapper:

```json
{
  "servers": {
    "aks-mcp": {
      "type": "stdio",
      "command": "bash",
      "args": [
        "-c",
        "/home/you/.vs-kubernetes/tools/aks-mcp/aks-mcp"
      ]
    }
  }
}
```

**Official site: ** [https://github.com/Azure/aks-mcp](https://github.com/Azure/aks-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `developer tools`, `azure`, `kubernetes`, `cloud`, `official`

## MCP Configuration

- Transport: `stdio`
- Command: `bash`
- Args: `-lc npx -y @azure/aks-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/azure-aks-mcp.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
