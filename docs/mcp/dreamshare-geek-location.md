---
title: "Geek_Location"
description: "MCP Server Product Name: [Jike Scene Recognition] [v1.1] [Based on the MCP protocol, the Jike Scene MCP Server provides IP location, population heat map queries, POI information queries, base station…"
---

# Geek_Location

MCP Server Product Name: [Jike Scene Recognition] [v1.1] [Based on the MCP protocol, the Jike Scene MCP Server provides IP location, population heat map queries, POI information queries, base station…

MCP Server Product Name: [Jike Scene Recognition]

# Version Information
[v1.1]
## Product Description
[The Jike Scene MCP Server based on the MCP protocol provides IP location, population heat map queries, POI information queries, base station information queries, and customer flow situation queries.]
# Category
[Location Services]
# Tags
[Population Heat Map, POI, Base Station, Customer Flow, Scene Recognition]
## Tools
This MCP server product offers the following Tools (capabilities):
### Tool1: [IP Location Query post_v1_signal_ip_location]
#### Detailed Description
[IP Location - Retrieves the aggregated location of a specified single `IP`.]
#### Debugging Input Parameters:
Input:  
- ip: IP address, required, supports IPv4 and IPv6  
Output:  
- response_id string Platform common gateway response ID, required  
- code integer Common gateway response code, required  
- message string Common gateway response parameter, required  
- biz_code integer API service response code, required  
- biz_message string API service response message, required  
- data object API service response data, required  
  - ip string IP address, required  
  - longitude_wgs84 number Aggregated longitude, required  
  - latitude_wgs84 number Aggregated latitude, required  
#### Most Likely Prompt Example
[Retrieve IP location]

### Tool2: [Area Population Heat Map Query post_v1_heat_map]
#### Detailed Description
[Area Heat (last 10 days) - Inputs a circular or polygonal fence to query the recent population heat in that area. Returns data containing both spatial and temporal dimensions: cell_heat: spatial dimension, heat value within each grid; time_range: temporal dimension, daily and hourly data (10 days × 24 hours).]
#### Debugging Input Parameters:  
Input:  
- cell_level: int, optional, custom grid size (not required, Google S2 Cell Level, supports levels 10~18)  
- circle: string, optional, circular fence, a JSON object containing center_point and radius. center_point is an array of the center's latitude and longitude, and radius is the radius (unit: meters). For example: "{\"center_point\": [113.93, 22.53], \"radius\": 500}"  
- fence: string, optional, polygonal fence, an array of arrays of latitude and longitude coordinates. At least 3 coordinate points are needed, and the first and last points must be the same to form a closed area. For example: "[[113.9,22.5],[113.9,22.6],[113.8,22.6],[113.9,22.5]]"  
Output:  
- response_id string Platform common gateway response ID, required  
- code integer Common gateway response code, required  
- message string Common gateway response parameter, required  
- biz_code integer API service response code, required  
- biz_message string API service response message, required  
- data object API service response data, required  
  - items array [object {6}] required  
    - cell_token string S2 cell token, required  
    - cell_id string S2 cell ID, required  
    - cell_center array[number] Cell center coordinates, WGS84 coordinate system, longitude first then latitude, required  
    - cell_level string S2 cell level, required  
    - cell_heat string Cell heat, required  
    - time_range array [object {2}] Detailed data for the time dimension, required  
      - date string Date, required  
      - heat array[integer] Heat values for each hour of the day, 24 hours in total, required  
#### Most Likely Prompt Example
[Area population heat map query]

### Tool3: [Base Station Information Query post_v1_signal_cell_location]
#### Detailed Description
[Base Station Location - Retrieves the aggregated location of a specific base station, also returning the base station identifier cell_code. Provides four combinations for retrieval: 1. lac+ci 2. lac 3. ci 4. cell_code.]
#### Debugging Input Parameters:  
Input:  
- cell_code: string, optional, complete base station code (MCC - MNC - LAC/TAC - CI/NCI)  
- ci: string, optional, fourth part of the base station code  
- lac: string, optional, third part of the base station code  
Output:  
- response_id string Platform common gateway response ID, required  
- code integer Common gateway response code, required  
- message string Common gateway response parameter, required  
- biz_code integer API service response code, required  
- biz_message string API service response message, required  
- data object API service response data, required  
  - items array [object {6}] optional- cell_token string Complete base station Code Required
- operator string Operator Required
- network_type string Network type, e.g., LTE, NR Required
- network_generation string Network generation, e.g., 4G, 5G Required
- heat integer Base station heat An integer greater than 1, the larger the value, the more users are connected to the base station Required
- pci integer Physical Cell Identifier Required
- earfcn integer Carrier frequency point Required
- longitude_wgs84 number Aggregated longitude (WGS84 coordinate system) Required
- latitude_wgs84 number Aggregated latitude (WGS84 coordinate system) Required
#### Example of the Most Easily Invoked Prompt
[Base Station Information Query]

### Tool4: [WiFi Location Query post_v1_signal_ap_location]
#### Detailed Description
[WiFi Location - Retrieves the aggregated location of a specific WiFi and returns the unique WiFi identifier ap_code. Provides the following three combinations for retrieval: 1. bssid + ssid 2. bssid 3. ssid. The case of bssid is insensitive.]
#### Debugging Input Parameters:
Input:
   -bssid: string, optional, WiFi MAC address (BSSID)
   -ssid: string, optional, WiFi name (SSID)
Output:
- response_id string Platform common gateway response ID Required
- code integer Common gateway response code Required
- message string Common gateway response parameter Required
- biz_code integer API service response code Required
- biz_message string API service response information Required
- data object API service response data Required
    - items array [object {6}] Optional
        - ssid string WiFi name Required
        - bssid string WiFi MAC address Required
        - ap_code string Unique WiFi identifier Required
        - spot_rate number Concentration of the aggregated location Range 0~1, the higher the value, the more concentrated the WiFi signal Required
        - longitude_wgs84 number Aggregated longitude (WGS84 coordinate system) Required
        - latitude_wgs84 number Aggregated latitude (WGS84 coordinate system) Required
        - update_time number Aggregation time 13-digit timestamp, WiFi location is re-aggregated every 14 days Required
        - first_report_time number Time when the WiFi was first collected 13-digit timestamp Required
        - last_report_time number Time when the WiFi was last collected Required
#### Example of the Most Easily Invoked Prompt
[WiFi Information Query]

### Tool5: [Customer Flow Trend Query get_v1_citymap_HistoryCustomer]
#### Detailed Description
[Scene Customer Flow Trend - Queries the historical customer flow trend of a specified scene.]
#### Debugging Input Parameters:
Input:
   -aoi_id: string, optional, the unique ID of the scene to be queried
   -competitor_id: string, optional, competitor scene's ID, multiple IDs separated by commas (not required)
   -end_month: string, optional, end month (format: YYYY-MM)
   -start_month: string, optional, start month (format: YYYY-MM)
Output:
- response_id string Platform common gateway response ID Required
- code integer Common gateway response code Required
- message string Common gateway response parameter Required
- biz_code integer API service response code Required
- biz_message string API service response information Required
- data object API service response data Optional
    - date string Optional
    - res array [object {2}] Daily customer flow Optional
        - p_id string Required
        - data array [object {2}] Required
            - data string Required
            - visitor_filter_uv integer Required
    - avg object Average daily customer flow Optional
        - avg_count_visitor_filter_uv integer Required
        - avg_count_visitor_filter_uv_without_delivery integer Required
    - cnt object Total customer flow Optional
        - cnt_count_visitor_filter_uv integer Required
        - count_visitor_filter_uv_without_delivery integer Required
    - res_waimai array [object {2}] Daily takeaway customer flow Optional
        - p_id string Optional
        - data array [object {2}] Optional
            - date string Required
            - delivery_pv integer Required
    - avg_waimai object Average daily takeaway Optional
        - avg_count_delivery_pv integer Required
   - cnt_waimai object Total takeaway customers Optional- count_delivery_pv integer Required  
- res_tangshi array [object {2}] Optional  
    - p_id string Required  
    - data array [object {2}] Required  
        - date string Required  
        - tangshi_uv integer Required  
- avg_tangshi object Optional  
    - avg_count_tangshi_uv integer Required  
- cnt_tangshi object Optional  
    - count_tangshi_uv integer Required  
- competitor object Competitor ID Optional   
    - 2479612 string Required  
    - 2515824 string Required  
- cost string Monthly Total Income Optional  
- out_uv integer Cumulative Store Traffic Optional  

#### Example of the Most Easily Invoked Prompt
[Customer Flow Query]

## Compatible Platforms
[Ark, Python, Cursor, etc.]
## Service Activation Link (for the entire product)
[http://mcp.isjike.com/mcp-servers/opendata/sse]
## Authentication Method
[When calling the interface, add your acquired API Key as a Bearer Token to the HTTP Header. Please apply for the key and activate the related service at http://mcp.isjike.com/mcp-servers/opendata/sse.]
## Installation and Deployment
[Please provide detailed installation and deployment instructions here, choosing an appropriate description based on the characteristics of your product.]
### Customer Services (Scenario One)
If the customer adopts this method, they need to provide an API key to directly call the service. The specific steps are as follows:
[MCP services, if needed, please go to Jike Open Platform to apply for a token: https://data.isjike.com/. The specific steps are as follows:
1. Register and create an API Key
   After registering or logging in, go to the Console to create an API Key.
2. Apply for the required capabilities
   Go to the Capability Center to apply for the capabilities you need.
3. Obtain data
   Integrate with your AI agent
   Use the API Key on your large model platform to activate Jike MCP services.]

**Official site: ** [https://github.com/Dreamshare02/MCP](https://github.com/Dreamshare02/MCP)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `location services`, `chinese`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/dreamshare-geek-location.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
