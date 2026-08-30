---
title: "高德地图"
description: "高德地图是一个支持任何MCP协议客户端的服务器，允许用户轻松利用高德地图MCP服务器获取各种基于位置的服务。"
---

# 高德地图

高德地图是一个支持任何MCP协议客户端的服务器，允许用户轻松利用高德地图MCP服务器获取各种基于位置的服务。

## 产品介绍

为实现 LBS 服务与 LLM 更好的交互，高德地图 MCP Server 现已覆盖12大核心服务接口，提供全场景覆盖的地图服务，包括地理编码、逆地理编码、IP 定位、天气查询、骑行路径规划、步行路径规划、驾车路径规划、公交路径规划、距离测量、关键词搜索、周边搜索、详情搜索等。

为进一步提高开发者接入效率与体验，高德地图开放平台为开发者提供了[通用级 SSE 协议](https://lbs.amap.com/api/mcp-server/gettingstarted) MCP 服务解决方案。

## 高德地图开放平台通用级 SSE 协议 MCP 服务解决方案

#### 产品架构图

![](/mcp-assets/d20fa1ab7ce32e945458280acfb2c5a9.png)

#### 什么是 SSE？

Server-Sent Events（SSE，服务器发送事件）是一种基于 HTTP 协议的技术，允许服务器向客户端单向、实时地推送数据。在 SSE 模式下，开发者可以在客户端通过创建一个 EventSource 对象与服务器建立持久连接，服务器则通过该连接持续发送数据流，而无需客户端反复发送请求。

#### 产品特点

+   使用简单：适用普通用户基于MCP（SSE）方式，不必部署本地服务，简单通过 URL 地址配置即可使用。
    
+   自动升级：我们会持续进行迭代更新，无须用户自己任何额外操作使用。
    
+   更易于大模型理解：我们对原始的JSON结果进行了语义化的转换，更易于大模型理解内容。
    
+   零运维成本：采用全托管云服务架构，用户无需关心服务器维护、资源扩容等底层运维问题。
    
+   协议兼容：支持SSE长连接，适配不同业务场景的技术需求。
    

前往 [快速接入](https://lbs.amap.com/api/mcp-server/gettingstarted) 文档，了解如何接入 MCP Server SSE 服务

## 能力介绍

#### 地理编码

将详细的结构化地址转换为经纬度坐标。

输入

address&nbsp;(位置信息)，

city&nbsp;(城市信息，非必须)

输出

location&nbsp;(位置经纬度)

#### 逆地理编码

将一个高德经纬度坐标转换为行政区划地址信息。

输入

location&nbsp;(位置经纬度)

输出

addressComponent

&nbsp;(位置信息，包括省市区等信息)

#### IP 定位

IP 定位根据用户输入的 IP 地址，定位 IP 的所在位置。

输入

IP

输出

province&nbsp;(省)，city&nbsp;(城市)，adcode&nbsp;(城市编码)

#### 天气查询

根据城市名称或者标准adcode查询指定城市的天气。

输入

city

&nbsp;(城市名称或城市adcode)

输出

forecasts&nbsp;(预报天气)

#### 骑行路径规划

用于规划骑行通勤方案，规划时会考虑天桥、单行线、封路等情况。最大支持 500km 的骑行路线规划。

输入

origin

&nbsp;(起点经纬度)，

destination&nbsp;(终点经纬度)

输出

distance&nbsp;(规划距离)，duration&nbsp;(规划时间)，steps&nbsp;(规划步骤信息)

#### 步行路径规划

可以根据输入起点终点经纬度坐标，规划100km 以内的步行通勤方案，并且返回通勤方案的数据。

输入

origin

&nbsp;(起点经纬度)，

destination&nbsp;(终点经纬度)

输出

origin&nbsp;(

起点

信息)，destination&nbsp;(终点信息)，paths&nbsp;(规划具体信息)

#### 驾车路径规划

根据用户起终点经纬度坐标规划以小客车、轿车通勤出行的方案，并且返回通勤方案的数据。

输入

origin

&nbsp;(起点经纬度)，

destination&nbsp;(终点经纬度)

输出

origin&nbsp;(

起点

信息)，destination&nbsp;(终点信息)，paths&nbsp;(规划具体信息)

#### 公交路径规划

根据用户起终点经纬度坐标规划综合各类公共（火车、公交、地铁）交通方式的通勤方案，并且返回通勤方案的数据，跨城场景下必须传起点城市与终点城市。

输入

origin&nbsp;(起点经纬度)，destination&nbsp;(终点经纬度)，city&nbsp;(起点城市)，cityd&nbsp;(终点城市)

输出

origin&nbsp;(

起点

信息)，destination&nbsp;(终点信息)，distance&nbsp;(规划距离)，transits&nbsp;(规划具体信息)

#### 距离测量

测量两个经纬度坐标之间的距离。

输入

origin&nbsp;(起点经纬度)，destination&nbsp;(终点经纬度)

输出

origin_id&nbsp;(

起点

信息)，dest_id&nbsp;(终点信息)，distance&nbsp;(规划距离)，duration&nbsp;(时间)

#### 关键词搜索

根据用户传入关键词，搜索出相关的POI地点信息。

输入

keywords

&nbsp;(

搜索关键词

)，

city&nbsp;(查询城市，非必须)

输出

suggestion&nbsp;(搜索建议)，pois&nbsp;(地点信息列表)

#### 周边搜索

根据用户传入关键词以及坐标location，搜索出radius半径范围的POI地点信息。

输入

keywords

&nbsp;(

搜索关键词

)，

location&nbsp;(中心点经度纬度)，radius&nbsp;(搜索半径，非必须)

输出

pois&nbsp;(地点信息列表)

#### 详情搜索

查询关键词搜或者周边搜获取到的POI ID的详细信息。

输入

id

&nbsp;(

关键词搜或周边搜获取的poiid

)

输出

地点详情信息

location&nbsp;(地点经纬度)，address&nbsp;(地址)，business_area&nbsp;(商圈)，city(城市)，type&nbsp;(地点类型)&nbsp;等

**官方网站：** [https://www.npmjs.com/package/@amap/amap-maps-mcp-server](https://www.npmjs.com/package/@amap/amap-maps-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`location services`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @amap/amap-maps-mcp-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/amap-amap-maps.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
