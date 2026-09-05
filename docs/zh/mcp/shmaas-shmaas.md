---
title: "随申行mcp服务"
description: "产品介绍 本目前支持查询坐标在上海市内的公交、地铁信息。 商务合作 1. 商务合作需求，请发送邮件至 databd@shmaas.cn 。 2. 商务合作完成后，系统会为商户配置商户id及盐值，用于请求鉴权。 发送请求 - 请求过程：连接初始化、发送业务请求 - 请求地址：https://apigtw.shmaas.net/ai-biz 连接初始化接口文档 - 请求地址: https://apig…"
---

# 随申行mcp服务

产品介绍 本目前支持查询坐标在上海市内的公交、地铁信息。 商务合作 1. 商务合作需求，请发送邮件至 databd@shmaas.cn 。 2. 商务合作完成后，系统会为商户配置商户id及盐值，用于请求鉴权。 发送请求 - 请求过程：连接初始化、发送业务请求 - 请求地址：https://apigtw.shmaas.net/ai-biz 连接初始化接口文档 - 请求地址: https://apig…

## 产品介绍
本目前支持查询坐标在上海市内的公交、地铁信息。

### 商务合作
1. 商务合作需求，请发送邮件至 databd@shmaas.cn 。
2. 商务合作完成后，系统会为商户配置商户id及盐值，用于请求鉴权。

#### 发送请求
- 请求过程：连接初始化、发送业务请求
- 请求地址：`https://apigtw.shmaas.net/ai-biz`

##### 连接初始化接口文档
- 请求地址: `https://apigtw.shmaas.net/ai-biz/sse`
- 请求方式：GET
- 返回示例：
```
id:ba9de9a6-2ba6-4a00-a43e-7ef941891a94
event:endpoint
data:/mcp?sessionId=ba9de9a6-2ba6-4a00-a43e-7ef941891a94
```
其中`data:`后的path及查询参数作为业务请求的path及参数，示例拼接地址：`https://apigtw.shmaas.net/ai-biz/sse/mcp?sessionId=ba9de9a6-2ba6-4a00-a43e-7ef941891a94`

##### 发送业务请求接口文档
- 请求地址：与上述连接初始化接口返回的`data`拼接后的地址
- 请求方式：POST
- 请求参数：包含根级参数与`params`参数，具体如下

###### 根级参数
| 参数名 | 类型 | 必填 | 说明 | 示例值 |
| --- | --- | --- | --- | --- |
| jsonrpc | string | 是 | JSON-RPC协议版本 | "2.0" |
| method | string | 是 | 调用的方法名 | "tools/call" |
| id | string | 是 | 请求唯一标识符 | "e3f3b929-1" |
| params | object | 是 | 方法参数对象 | - |

###### params 参数
| 参数名 | 类型 | 必填 | 说明 | 示例值 |
| --- | --- | --- | --- | --- |
| name | string | 是 | 实际业务方法名 | "findNearByTrafficBus" |
| arguments | object | 是 | 业务参数 | {"nearRadiusDistance":500,"cityCode":"310100","lat":"39.9042","lon":116.4074} |

###### 请求体组装参数示例
```json
{
    "jsonrpc":"2.0",
    "method":"tools/call",
    "id":"e3f3b929-1",
    "params":{
        "name":"findNearByTrafficBus",
        "arguments":{
            "nearRadiusDistance":500,
            "cityCode":"310100",
            "lat":"39.9042",
            "lon":116.4074
        }
    }
}
```

###### 请求头参数
参考开放平台接入网关（地址：https://open-web.shmaas.cn/docs/guide ），需将请求的`arguments`原始报文按如下工具排序，根据排序后的网关计算`X-Sign`：

```java
package com.maas.ai.util;

import com.alibaba.fastjson2.JSON;

import java.util.*;

/**
 * Map排序工具类
 * 用于将Map中的参数按key的ASCII码排序，并递归处理嵌套的Map
 */
public class MapSortUtil {

    /**
     * 将Map中的参数按key的ASCII码排序，并递归处理嵌套的Map
     * @param params 参数Map
     * @return 排序后的JSON字符串
     */
    public static String sortAndConvertToJson(Map params) {
        Map sortedMap = sortMapByKey(params);
        return JSON.toJSONString(sortedMap);
    }

    /**
     * 递归排序Map，处理嵌套的Map和List
     * @param map 待排序的Map
     * @return 排序后的Map
     */
    @SuppressWarnings("unchecked")
    public static Map sortMapByKey(Map map) {
        if (map == null) {
            return null;
        }
        
        // 使用TreeMap按key的ASCII码自动排序
        Map sortedMap = new TreeMap();
        
        for (Map.Entry entry : map.entrySet()) {
            Object value = entry.getValue();
            
            if (value instanceof Map) {
                // 递归处理嵌套的Map
                sortedMap.put(entry.getKey(), sortMapByKey((Map) value));
            } else if (value instanceof List) {
                // 处理List中可能嵌套的Map
                List list = (List) value;
                List processedList = new ArrayList();
                for (Object item : list) {
                    if (item instanceof Map) {
                        processedList.add(sortMapByKey((Map) item));
                    } else {
                        processedList.add(item);
                    }
                }
                sortedMap.put(entry.getKey(), processedList);
            } else {
                sortedMap.put(entry.getKey(), value);
            }
        }
        
        return sortedMap;
    }
}
```

## 能力介绍
### 现有MCP协议功能
目前提供2款MCP协议的功能，具体信息如下：
#### 根据经纬度及距离查询附近公交
**params.name=findNearByTrafficBus**
##### 业务参数说明
**请求参数**

| 名称              | 参数类型 | 描述               | 是否必须 | 说明                                   |
| ----------------- | -------- | ------------------ | -------- | -------------------------------------- |
| cityCode          | string   | 城市编码           | 是       | 默认310100；                           |
| isGetStopArrive   | string   | 是否获取到站信息   | 否       | 1-获取，其他不获取；默认不获取；       |
| lon               | string   | 经度               | 是       |                                        |
| lat               | string   | 纬度               | 是       |                                        |
| nearRadiusDistance| string   | 半径（单位：米）| 否       | 默认1000；                             |
| coordinateType    | string   | 坐标类型           | 否       | 1：WGS-84，2：GC-J02，默认WGS-84；|


**响应参数**

| 名称                | 参数类型 | 描述                                   | 说明                                  |
| ------------------- | -------- | -------------------------------------- | ------------------------------------- |
| retCode             | int      | 响应编码                               | 0代表调用成功                         |
| retMsg              | string   | 响应信息                               |                                       |
| - nearByTrafficLineStop | object   | 公交地铁线路的站点信息                 |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;indexId       | int      | 数据唯一标识                           |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;lineId        | string   | 线路编号                               |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;lineName      | string   | 线路名称                               |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;stopId        | string   | 站点编号                               |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;stopName      | string   | 站点名称                               |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;startStopName | string   | 线路起点站名称                         |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;endStopName   | string   | 线路终点站名称                         |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;startEarlyLateTime | string | 最早始发时间-最晚始发时间               | 格式hh:mm；|
| &nbsp;&nbsp;&nbsp;&nbsp;endEarlyLateTime | string | 最早到站时间-最晚到站时间               | 格式hh:mm；|
| &nbsp;&nbsp;&nbsp;&nbsp;upDown        | string   | 上下行                                 | 0-上行，1-下行；|
| &nbsp;&nbsp;&nbsp;&nbsp;type          | string   | 公共交通类型                           | 1-公交，2-地铁，3-轮渡；|
| - point             | object   | 当前站点经纬度                         |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;lon          | string   | 经度                                   |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;lat          | string   | 纬度                                   |                                       |
| - sai               | object   | 车辆到站信息                           |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;currentBusDistance | string | 最近一辆车距离本站距离（单位：米）|                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;currentBusArriveTime | string | 最近一辆车预计多久后到达（单位：分钟） |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;currentBusComfort | string | 最近一辆车拥挤程度                     | 0-未知，1-舒适，2-较舒适，3-拥挤|
| &nbsp;&nbsp;&nbsp;&nbsp;upDown        | string   | 上下行                                 | 0-上行，1-下行；|
| &nbsp;&nbsp;&nbsp;&nbsp;currentBusStopCount | string | 最近一辆车距离当前还有几站             |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;currentLicensePlate | string | 最近一辆车车牌                         |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;currentBarrierFree | string | 最近一辆车是否无障碍                   | bool类型，true/false；|
| &nbsp;&nbsp;&nbsp;&nbsp;nextBusDistance | string | 下一辆车距离本站距离（单位：米）|                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;nextBusArriveTime | string | 下一辆车预计多久后到达（单位：分钟）|                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;nextBusStopCount | string | 下一辆车距离当前还有几站               |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;nextLicensePlate | string | 下一辆车车牌                           |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;nextBarrierFree | string | 下一辆车是否无障碍                     | bool类型，true/false；|
| - dispatchCarSchedule | object   | 车辆发车时刻表                         |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;lineId        | string   | 线路编号                               |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;lineName      | string   | 线路名称                               |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;direction     | string   | 上下行                                 | 0-上行，1-下行；|
| &nbsp;&nbsp;&nbsp;&nbsp;scheduleCode  | int      | 调度编码                               | -1-不在运营时间，0-暂无实时数据，1-等待常规发车； |
| &nbsp;&nbsp;&nbsp;&nbsp;scheduleMsgDefault | string | 调度提示                               |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;scheduleMsgShort | string | 调度提示                               |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;- dispatchCars | object   | 发车明细                               |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vehicle    | string   | 车牌号                                 |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time       | string   | 发车时间                               |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;countdown  | string   | 倒计时                                 |                                       |

#### 根据经纬度及距离查询地铁信息
**params.name=queryNearByMetro**
##### 业务参数说明
**请求参数**

| 名称                | 参数类型 | 描述         | 是否必须 | 说明                          |
| ------------------- | -------- | ------------ | -------- | ----------------------------- |
| cityCode            | string   | 城市编码     | 是       | 仅输入310100；|
| lon                 | string   | 经度         | 是       |                                |
| lat                 | string   | 纬度         | 是       |                                |
| coordinateType      | int      | 坐标系类型   | 否       | 1-WGS-84，2-GCJ02；默认2；|
| nearRadiusDistance  | int      | 半径（单位：米） | 否       | 默认1000，最大3000；|

**响应参数**

| 名称                | 参数类型 | 描述                 | 说明                                                         |
| ------------------- | -------- | -------------------- | ------------------------------------------------------------ |
| retCode             | int      | 响应编码             | 0表示调用成功，其余失败；|
| retMsg              | string   | 响应信息             |                                                              |
| - normalMetroList   | object   | 普通地铁信息         |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;indexId       | int      | 数据库唯一id         |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;lineNo        | string   | 线路编号             |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;lineName      | string   | 线路名称             |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;upDown        | int      | 上下行               | 0-上行，1-下行；|
| &nbsp;&nbsp;&nbsp;&nbsp;startStopName | string   | 线路起点站名称       |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;endStopName   | string   | 线路终点站名称       |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;startEarlyLateTime | string | 首班车时间           | 格式hhmm；|
| &nbsp;&nbsp;&nbsp;&nbsp;endEarlyLateTime | string | 末班车时间           | 格式hhmm；|
| &nbsp;&nbsp;&nbsp;&nbsp;priceRange    | string   | 票价范围（单位：元） | eg：3-7；|
| &nbsp;&nbsp;&nbsp;&nbsp;lineType      | int      | 线路类型             | 0-普通车，1-夜班车，2-临时保障车（暂无信息），3-区间车，4-大站车； |
| &nbsp;&nbsp;&nbsp;&nbsp;- station     | object   | 站点信息             |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stopNo        | string   | 站点编号             |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stopName      | string   | 站点名称             |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;startEarlyLateTime | string | 站点首班车时间       | 格式hhmm；|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;endEarlyLateTime | string | 站点末班车时间       | 格式hhmm；|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type          | int      | 上下客协议           | 0或者空表示可上下，1表示仅下；|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- point       | object   | 站点位置             |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lon        | string   | 经度                 |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lat        | string   | 纬度                 |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- dispatchCarSchedule | object   | 间隔信息             |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;scheduleCode  | int      | 调度编码             | -1表示不在运营时间，0表示暂无实时数据，1表示数据正常；|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;scheduleType  | int      | 调度类型             | 0表示间隔xx分钟到站，1表示xx点到站；|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;scheduleTime  | string   | 调度时间             |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;scheduleMsg   | string   | 调度提示             |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;scheduleMsgDefault | string   | 调度提示             |                                                              |
| - bigStationMetroList | object   | 大站地铁信息         |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;indexId       | int      | 数据库唯一id         |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;lineNo        | string   | 线路编号             |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;lineName      | string   | 线路名称             |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;upDown        | int      | 上下行               | 0-上行，1-下行；|
| &nbsp;&nbsp;&nbsp;&nbsp;startStopName | string   | 线路起点站名称       |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;endStopName   | string   | 线路终点站名称       |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;startEarlyLateTime | string | 首班车时间           | 格式hhmm；|
| &nbsp;&nbsp;&nbsp;&nbsp;endEarlyLateTime | string | 末班车时间           | 格式hhmm；|
| &nbsp;&nbsp;&nbsp;&nbsp;priceRange    | string   | 票价范围（单位：元） | eg：3-7；|
| &nbsp;&nbsp;&nbsp;&nbsp;lineType      | int      | 线路类型             | 0-普通车，1-夜班车，2-临时保障车（暂无信息），3-区间车，4-大站车； |
| &nbsp;&nbsp;&nbsp;&nbsp;- station     | object   | 站点信息             |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stopNo        | string   | 站点编号             |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stopName      | string   | 站点名称             |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;startEarlyLateTime | string | 站点首班车时间       | 格式hhmm；|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;endEarlyLateTime | string | 站点末班车时间       | 格式hhmm；|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type          | int      | 上下客协议           | 0或者空表示可上下，1表示仅下；|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- point       | object   | 站点位置             |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lon        | string   | 经度                 |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lat        | string   | 纬度                 |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- dispatchCarSchedule | object   | 间隔信息             |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;scheduleCode  | int      | 调度编码             | -1表示不在运营时间，0表示暂无实时数据，1表示数据正常；|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;scheduleType  | int      | 调度类型             | 0表示间隔xx分钟到站，1表示xx点到站；|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;scheduleTime  | string   | 调度时间             |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;scheduleMsg   | string   | 调度提示             |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;scheduleMsgDefault | string   | 调度提示             |                                                              |
| - fixedStationMetroList | object   | 定点上下车地铁信息   |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;indexId       | int      | 数据库唯一id         |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;lineNo        | string   | 线路编号             |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;lineName      | string   | 线路名称             |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;upDown        | int      | 上下行               | 0-上行，1-下行；|
| &nbsp;&nbsp;&nbsp;&nbsp;startStopName | string   | 线路起点站名称       |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;endStopName   | string   | 线路终点站名称       |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;startEarlyLateTime | string | 首班车时间           | 格式hh:mm；|
| &nbsp;&nbsp;&nbsp;&nbsp;endEarlyLateTime | string | 末班车时间           | 格式hh:mm；|
| &nbsp;&nbsp;&nbsp;&nbsp;priceRange    | string   | 票价范围（单位：元） | eg：3-7；|
| &nbsp;&nbsp;&nbsp;&nbsp;lineType      | int      | 线路类型             | 0-普通车，1-夜班车，2-临时保障车（暂无信息），3-区间车，4-大站车； |
| &nbsp;&nbsp;&nbsp;&nbsp;- station     | object   | 站点信息             |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stopNo        | string   | 站点编号             |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stopName      | string   | 站点名称             |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;startEarlyLateTime | string | 站点首班车时间       | 格式hh:mm；|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;endEarlyLateTime | string | 站点末班车时间       | 格式hh:mm；|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type          | int      | 上下客协议           | 0或者空表示可上下，1表示仅下；|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- point       | object   | 站点位置             |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lon        | string   | 经度    

**官方网站：** [https://www.shmaas.cn/](https://www.shmaas.cn/)
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

资源文件：`resources/mcp/shmaas-shmaas.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
