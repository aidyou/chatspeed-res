---
title: "及刻场景识别"
description: "MCP Server 产品名称:[及刻场景识别] [v1.1] [基于 MCP 协议的及刻场景MCP Server提供了IP定位，人口热力查询，POI信息查询，基站信息查询，客流情况查询等。] [位置服务] [人口热力，POI，基站，客流，场景识别] 本 MCP server 产品提供以下 Tools(工具/能力): [IP 位置 - 检索指定单个IP聚合后的位置。] 输入: ip：IP地址，必填 ，支持IPv4和IPv6 输出: - responseid string  平台公共网响应ID 必需 - code integer  公共网关响应码 必需 - message string  公共网关响应参数 必需 - bizcode integer  API服务响应码 必需 - bizmessage string  API服务响应信息 必需 - da"
---

# 及刻场景识别

MCP Server 产品名称:[及刻场景识别] [v1.1] [基于 MCP 协议的及刻场景MCP Server提供了IP定位，人口热力查询，POI信息查询，基站信息查询，客流情况查询等。] [位置服务] [人口热力，POI，基站，客流，场景识别] 本 MCP server 产品提供以下 Tools(工具/能力): [IP 位置 - 检索指定单个IP聚合后的位置。] 输入: ip：IP地址，必填 ，支持IPv4和IPv6 输出: - responseid string  平台公共网响应ID 必需 - code integer  公共网关响应码 必需 - message string  公共网关响应参数 必需 - bizcode integer  API服务响应码 必需 - bizmessage string  API服务响应信息 必需 - da

MCP Server 产品名称:[及刻场景识别]

# 版本信息
[v1.1]
## 产品描述
[基于 MCP 协议的及刻场景MCP Server提供了IP定位，人口热力查询，POI信息查询，基站信息查询，客流情况查询等。]
# 分类
[位置服务]
# 标签
[人口热力，POI，基站，客流，场景识别]
## Tools
本 MCP server 产品提供以下 Tools(工具/能力):
### Tool1:[IP位置查询 post_v1_signal_ip_location]
#### 详细描述
[IP 位置 - 检索指定单个`IP`聚合后的位置。]
#### 调试所离的输入参数:
输入:  
ip：IP地址，必填 ，支持IPv4和IPv6  
输出:  
- response_id string  平台公共网响应ID 必需   
- code integer  公共网关响应码 必需  
- message string  公共网关响应参数 必需  
- biz_code integer  API服务响应码 必需  
- biz_message string  API服务响应信息 必需  
- data object  API服务响应数据 必需  
    - ip string IP地址 必需  
    - longitude_wgs84 number  聚合后的经度 必需  
    - latitude_wgs84 number  聚合后的纬度 必需  
#### 最容易被唤起的 Prompt 示例
[检索IP位置]

### Tool2:[区域人口热力查询 post_v1_heat_map]
#### 详细描述
[区域热力（最近10天） - 传入圆形围栏或多边形围栏查询该区域近期内的人群热力 返回同时包含空间+时间的数据：cell_heat：空间维度，每个格子内的热力值；time_range：时间维度，每天、每个小时的数据（10天×24小时）。]
#### 调试所离的输入参数:  
输入:  
   -cell_level：int，非必填，自定义格子大小 (非必传，Google S2 Cell Level，支持10~18级)   
   -circle：string，非必填，圆形围栏，一个包含 center_point 和 radius 的JSON对象。center_point 是中心点经纬度数组，radius 是半径（单位：米）。例如: "{\"center_point\": [113.93, 22.53], \"radius\": 500}"  
   -fence：string，非必填，多边形围栏，一个由经纬度坐标数组组成的数组。至少需要3个坐标点，且首尾坐标必须相同以形成闭合区域。例如: "[[113.9,22.5],[113.9,22.6],[113.8,22.6],[113.9,22.5]]"  
输出:  
- response_id string  平台公共网响应ID 必需  
- code integer  公共网关响应码 必需  
- message string  公共网关响应参数 必需  
- biz_code integer  API服务响应码 必需  
- biz_message string  API服务响应信息 必需  
- data object  API服务响应数据 必需  
    -  items array [object {6}] 必需  
        - cell_token string S2格子Token 必需  
        - cell_id string  S2格子ID 必需  
        - cell_center array[number] 格子中心坐标 WGS84坐标系，前经后纬 必需  
        -  cell_level string S2格子层级 必需  
        - cell_heat string  格子热力 必需  
        - time_range array [object {2}]  时间维度的明细数据 必需  
            - date string  日期 必需   
            - heat array[integer] 每天内各个小时的热力值 共有24个小时 必需  
#### 最容易被唤起的 Prompt 示例
[区域人口热力查询]

### Tool3:[基站信息查询post_v1_signal_cell_location]
#### 详细描述
[基站位置 - 检索特定基站聚合后的位置，同时返回基站标识cell_code 提供以下四种组合检索方式：1. lac+ci 2. lac 3. ci 4. cell_code。]
#### 调试所离的输入参数:  
输入:  
   -cell_code：string，非必填，完整的基站Code (MCC - MNC - LAC/TAC - CI/NCI)  
   -ci：string，非必填，基站Code第四位  
   -lac：string，非必填，基站Code第三位  
输出:  
- response_id string  平台公共网响应ID 必需  
- code integer  公共网关响应码 必需  
- message string  公共网关响应参数 必需  
- biz_code integer  API服务响应码 必需  
- biz_message string  API服务响应信息 必需  
- data object  API服务响应数据 必需  
    -  items array [object {6}] 可选  
        - cell_token string 完整的基站Code 必需  
        - operator string  运营商 必需  
        - network_type string  网络制式 如：LTE、NR 必需  
        - network_generation string 网络世代 如：4G、5G必需  
        - heat integer 基站热度 大于1的整数，值越大表示越多用户接入该基站 必需  
        - pci integer 物理小区标识 必需  
        - earfcn integer 载波频点 必需  
        - longitude_wgs84 number 聚合后的经度（WGS84坐标系）必需  
        - latitude_wgs84 number 聚合后的纬度（WGS84坐标系）必需  
#### 最容易被唤起的 Prompt 示例
[基站信息查询]

### Tool4:[WiFi位置查询post_v1_signal_ap_location]
#### 详细描述
[WiFi 位置 - 检索特定 WiFi 聚合后的位置，同时返回 WiFi 唯一标识ap_code 提供以下三种组合检索方式： 1. bssid + ssid 2. bssid 3. ssidbssid的大小写不敏感]
#### 调试所离的输入参数:  
输入:  
   -bssid：string，非必填，WiFi MAC 地址 (BSSID)  
   -ssid：string，非必填，WiFi 名称 (SSID)  
输出:  
- response_id string  平台公共网响应ID 必需  
- code integer  公共网关响应码 必需  
- message string  公共网关响应参数 必需  
- biz_code integer  API服务响应码 必需  
- biz_message string  API服务响应信息 必需  
- data object  API服务响应数据 必需  
    - items array [object {6}] 可选  
        - ssid string WiFi 名称 必需  
        - bssid string WiFi MAC 地址 必需 
        - ap_code string WiFi 唯一标识 必需  
        - spot_rate number 聚合位置的集中度 取值范围0~1，值越大说明WiFi信号越集中 必需  
        - longitude_wgs84 number 聚合后的经度（WGS84坐标系）必需  
        - latitude_wgs84 number 聚合后的纬度（WGS84坐标系）必需  
        - update_time number 聚合的时间 13位时间戳，WiFi位置每隔14天会重新聚合一次 必需  
        - first_report_time number WiFi首次被采集到的时间 13位时间戳 必需  
        - last_report_time number  WiFi最近一次被采集到的时间 必需  
#### 最容易被唤起的 Prompt 示例
[wifi信息查询]

### Tool5:[客流趋势查询get_v1_citymap_HistoryCustomer]
#### 详细描述
[场景客流趋势 - 查询指定场景的历史客流趋势。]
#### 调试所离的输入参数:
输入:  
   -aoi_id：string，非必填，要查询的场景的唯一ID  
   -competitor_id：string，非必填，竞品场景的ID,多个ID用逗号分隔(非必传)  
   -end_month：string，非必填，终止月份(格式:YYYY-MM)  
   -start_month：string，非必填，起始月份(格式:YYYY-MM)  
输出:  
- response_id string  平台公共网响应ID 必需  
- code integer  公共网关响应码 必需  
- message string  公共网关响应参数 必需  
- biz_code integer  API服务响应码 必需  
- biz_message string  API服务响应信息 必需  
- data object  API服务响应数据 可选  
    - date string 可选  
    - res array [object {2}] 天级客流 可选  
        - p_id string 必需  
        - data array [object {2}] 必需  
            - data string 必需  
            - visitor_filter_uv integer 必需  
    - avg object 日均客流 可选  
        - avg_count_visitor_filter_uv integer 必需  
        - avg_count_visitor_filter_uv_without_delivery integer 必需  
    - cnt object 总客流 可选  
        - cnt_count_visitor_filter_uv integer 必需  
        - count_visitor_filter_uv_without_delivery integer 必需  
    - res_waimai array [object {2}]  外卖天级客流 可选  
        - p_id string 可选  
        - data array [object {2}] 可选  
            - date string 必需  
            - delivery_pv integer 必需  
    - avg_waimai object 外卖日均 可选  
        - avg_count_delivery_pv integer 必需  
   - cnt_waimai object 外卖总人数 可选  
        - count_delivery_pv integer 必需  
    - res_tangshi array [object {2}]  可选  
        - p_id string必需  
        - data array [object {2}] 必需  
            - date string 必需  
            - tangshi_uv integer 必需  
    - avg_tangshi object 可选  
        - avg_count_tangshi_uv integer 必需  
    - cnt_tangshi object 可选  
        - count_tangshi_uv integer 必需  
    - competitor object 竞品id 可选   
        - 2479612 string 必需  
        - 2515824 string 必需  
    - cost string 月总收入 可选  
    - out_uv integer 累计过店客流 可选  
#### 最容易被唤起的 Prompt 示例
[客流查询]

## 可适配平台
[方舟，python，cursor等]
## 服务开通链接(整体产品)
[http://mcp.isjike.com/mcp-servers/opendata/sse]
## 鉴权方式
[调用接口时，将自己的申请的 API Key 作为 Bearer Token 添加到 HTTP Header 中。请在 http://mcp.isjike.com/mcp-servers/opendata/sse 申请密钥并开通相关服务。]
## 安装部署
[请在此处提供详细的安装和部署说明，根据您的产品特性选择合适的描述方式。]
### 客户部等服务(情况一）
若客户采用此方式，需提供 api key 以直接调取服务，具体步骤如下:
[MCP服务如需调用，请到及刻开放平台申请token：https://data.isjike.com/。具体步骤如下：
1
注册并创建API Key
注册或登录后跳转到 控制台 创建API Key
2
按需申请能力
前往 能力中心 申请您需要的能力
3
获取数据
接入您的AI智能体
在您的大模型平台使用API Key开通及刻MCP服务]

**官方网站：** [https://github.com/Dreamshare02/MCP](https://github.com/Dreamshare02/MCP)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`location services`, `chinese`

## MCP 配置

- 传输方式：`http`
- 启动命令：``
- 参数：无

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/dreamshare-geek-location.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
