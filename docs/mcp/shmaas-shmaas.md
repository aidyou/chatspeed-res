---
title: "mcp-shmaas"
description: "Product Introduction This currently supports querying bus and subway information for coordinates within Shanghai. Business Cooperation 1. For business cooperation inquiries, please send an email to da…"
---

# mcp-shmaas

Product Introduction This currently supports querying bus and subway information for coordinates within Shanghai. Business Cooperation 1. For business cooperation inquiries, please send an email to da…

## Product Introduction
This  currently supports querying bus and subway information for coordinates within Shanghai.

### Business Cooperation
1. For business cooperation inquiries, please send an email to databd@shmaas.cn.
2. After the business cooperation is completed, the system will configure a merchant ID and salt value for the merchant, which will be used for request authentication.

#### Sending Requests
- Request process: Connection initialization, sending business requests
- Request URL: `https://apigtw.shmaas.net/ai-biz`

##### Connection Initialization API Documentation
- Request URL: `https://apigtw.shmaas.net/ai-biz/sse`
- Request Method: GET
- Response Example:
 
id:ba9de9a6-2ba6-4a00-a43e-7ef941891a94
event:endpoint
data:/mcp?sessionId=ba9de9a6-2ba6-4a00-a43e-7ef941891a94

The path and query parameters after `data:` are used as the path and parameters for the business request. Example concatenated URL: `https://apigtw.shmaas.net/ai-biz/sse/mcp?sessionId=ba9de9a6-2ba6-4a00-a43e-7ef941891a94`

##### Sending Business Request API Documentation
- Request URL: The URL concatenated with the `data` returned from the connection initialization interface
- Request Method: POST
- Request Parameters: Include root-level parameters and `params` parameters, as detailed below

###### Root-Level Parameters
| Parameter Name | Type | Required | Description | Example Value |
| --- | --- | --- | --- | --- |
| jsonrpc | string | Yes | JSON-RPC protocol version | "2.0" |
| method | string | Yes | The name of the method being called | "tools/call" |
| id | string | Yes | Unique identifier for the request | "e3f3b929-1" |
| params | object | Yes | Object containing method parameters | - |

###### params Parameters
| Parameter Name | Type | Required | Description | Example Value |
| --- | --- | --- | --- | --- |
| name | string | Yes | Actual business method name | "findNearByTrafficBus" |
| arguments | object | Yes | Business parameters | {"nearRadiusDistance":500,"cityCode":"310100","lat":"39.9042","lon":116.4074} |

###### Example of Assembling Request Body Parameters
json
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

###### Request Header Parameters
Refer to the Open Platform Access Gateway (URL: https://open-web.shmaas.cn/docs/guide), you need to sort the original message of the `arguments` in the request as follows, and calculate the `X-Sign` based on the sorted gateway:

java
package com.maas.ai.util;

import com.alibaba.fastjson2.JSON;

import java.util.*;

/**
 * Map sorting utility class
 * Used to sort the parameters in the Map by ASCII code of the key, and recursively handle nested Maps
 */
public class MapSortUtil {

    /**
     * Sorts the parameters in the Map by ASCII code of the key, and recursively handles nested Maps
     * @param params Parameter Map
     * @return Sorted JSON string
     */
    public static String sortAndConvertToJson(Map params) {
        Map sortedMap = sortMapByKey(params);
        return JSON.toJSONString(sortedMap);
    }

    /**
     * Recursively sorts the Map, handling nested Maps and Lists
     * @param map Map to be sorted
     * @return Sorted Map
     */
    @SuppressWarnings("unchecked")
    public static Map sortMapByKey(Map map) {
        if (map == null) {
            return null;
        }
        
        // Use TreeMap to automatically sort by ASCII code of the key
        Map sortedMap = new TreeMap();
        
        for (Map.Entry entry : map.entrySet()) {
            Object value = entry.getValue();
            
            if (value instanceof Map) {
                // Recursively handle nested Maps
                sortedMap.put(entry.getKey(), sortMapByKey((Map) value));
            } else if (value instanceof List) {
                // Handle possibly nested Maps in the List
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
}## Capability Introduction
### Existing MCP Protocol Features
Currently, two MCP protocol features are provided. The specific information is as follows:
#### Query Nearby Buses Based on Latitude, Longitude, and Distance
**params.name=findNearByTrafficBus**
##### Business Parameter Description
**Request Parameters**

| Name              | Parameter Type | Description               | Required | Notes                                   |
| ----------------- | -------------- | ------------------------- | -------- | --------------------------------------- |
| cityCode          | string         | City code                 | Yes      | Default 310100;                         |
| isGetStopArrive   | string         | Whether to get arrival info| No       | 1 - Get, otherwise not; default not;    |
| lon               | string         | Longitude                 | Yes      |                                         |
| lat               | string         | Latitude                  | Yes      |                                         |
| nearRadiusDistance| string         | Radius (unit: meters)     | No       | Default 1000;                           |
| coordinateType    | string         | Coordinate type           | No       | 1: WGS-84, 2: GC-J02, default WGS-84;  |

**Response Parameters**

| Name                | Parameter Type | Description                                   | Notes                                  |
| ------------------- | -------------- | --------------------------------------------- | -------------------------------------- |
| retCode             | int            | Response code                                 | 0 indicates success                    |
| retMsg              | string         | Response message                              |                                        |
| - nearByTrafficLineStop | object        | Information about bus/subway line stops       |                                        |
| &nbsp;&nbsp;&nbsp;&nbsp;indexId       | int            | Unique data identifier                        |                                        |
| &nbsp;&nbsp;&nbsp;&nbsp;lineId        | string         | Line number                                   |                                        |
| &nbsp;&nbsp;&nbsp;&nbsp;lineName      | string         | Line name                                     |                                        |
| &nbsp;&nbsp;&nbsp;&nbsp;stopId        | string         | Stop number                                   |                                        |
| &nbsp;&nbsp;&nbsp;&nbsp;stopName      | string         | Stop name                                     |                                        |
| &nbsp;&nbsp;&nbsp;&nbsp;startStopName | string         | Starting stop name                            |                                        |
| &nbsp;&nbsp;&nbsp;&nbsp;endStopName   | string         | Ending stop name                              |                                        |
| &nbsp;&nbsp;&nbsp;&nbsp;startEarlyLateTime | string    | Earliest departure time - latest departure time | Format hh:mm;|
| &nbsp;&nbsp;&nbsp;&nbsp;endEarlyLateTime | string      | Earliest arrival time - latest arrival time    | Format hh:mm;|
| &nbsp;&nbsp;&nbsp;&nbsp;upDown        | string         | Up or down direction                          | 0 - Up, 1 - Down;                      |
| &nbsp;&nbsp;&nbsp;&nbsp;type          | string         | Public transport type                         | 1 - Bus, 2 - Subway, 3 - Ferry;        |
| - point             | object         | Current stop's latitude and longitude         |                                        |
| &nbsp;&nbsp;&nbsp;&nbsp;lon          | string         | Longitude                                     |                                        |
| &nbsp;&nbsp;&nbsp;&nbsp;lat          | string         | Latitude                                      |                                        |
| - sai               | object         | Vehicle arrival information                   |                                        |
| &nbsp;&nbsp;&nbsp;&nbsp;currentBusDistance | string    | Distance of the nearest vehicle from this stop (unit: meters)| || &nbsp;&nbsp;&nbsp;&nbsp;currentBusArriveTime | string | Estimated time of arrival for the nearest bus (unit: minutes) |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;currentBusComfort | string | Crowding level of the nearest bus | 0-Unknown, 1-Comfortable, 2-Somewhat Comfortable, 3-Crowded |
| &nbsp;&nbsp;&nbsp;&nbsp;upDown        | string   | Up or down direction | 0-Up, 1-Down; |
| &nbsp;&nbsp;&nbsp;&nbsp;currentBusStopCount | string | Number of stops remaining until the nearest bus arrives |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;currentLicensePlate | string | License plate of the nearest bus |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;currentBarrierFree | string | Whether the nearest bus is accessible | Boolean type, true/false; |
| &nbsp;&nbsp;&nbsp;&nbsp;nextBusDistance | string | Distance to the next bus from the current station (unit: meters) |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;nextBusArriveTime | string | Estimated time of arrival for the next bus (unit: minutes) |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;nextBusStopCount | string | Number of stops remaining until the next bus arrives |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;nextLicensePlate | string | License plate of the next bus |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;nextBarrierFree | string | Whether the next bus is accessible | Boolean type, true/false; |
| - dispatchCarSchedule | object   | Bus schedule |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;lineId        | string   | Line number |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;lineName      | string   | Line name |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;direction     | string   | Up or down direction | 0-Up, 1-Down; |
| &nbsp;&nbsp;&nbsp;&nbsp;scheduleCode  | int      | Dispatch code | -1-Not in operation, 0-No real-time data, 1-Waiting for regular departure; |
| &nbsp;&nbsp;&nbsp;&nbsp;scheduleMsgDefault | string | Dispatch message |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;scheduleMsgShort | string | Dispatch message |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;- dispatchCars | object   | Departure details |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vehicle    | string   | Vehicle license plate |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time       | string   | Departure time |                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;countdown  | string   | Countdown |                                       |

#### Query Metro Information Based on Latitude, Longitude, and Distance
**params.name=queryNearByMetro**
##### Business Parameter Description
**Request Parameters**

| Name                | Parameter Type | Description         | Required | Notes                          |
| ------------------- | -------------- | ------------------- | -------- | ----------------------------- |
| cityCode            | string         | City code           | Yes      | Only input 310100; |
| lon                 | string         | Longitude           | Yes      |                                |
| lat                 | string         | Latitude            | Yes      |                                |
| coordinateType      | int            | Coordinate system type | No      | 1-WGS-84, 2-GCJ02; Default is 2; || nearRadiusDistance  | int      | Radius (unit: meters) | Optional       | Default is 1000, maximum is 3000;|

**Response Parameters**

| Name                | Data Type | Description                 | Remarks                                                         |
| ------------------- | -------- | -------------------- | ------------------------------------------------------------ |
| retCode             | int      | Response code             | 0 indicates success, others indicate failure;|
| retMsg              | string   | Response message             |                                                              |
| - normalMetroList   | object   | Normal metro information         |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;indexId       | int      | Unique database ID         |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;lineNo        | string   | Line number             |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;lineName      | string   | Line name             |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;upDown        | int      | Up or down               | 0-Up, 1-Down;|
| &nbsp;&nbsp;&nbsp;&nbsp;startStopName | string   | Starting station name       |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;endStopName   | string   | Ending station name       |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;startEarlyLateTime | string | First train time           | Format hhmm;|
| &nbsp;&nbsp;&nbsp;&nbsp;endEarlyLateTime | string | Last train time           | Format hhmm;|
| &nbsp;&nbsp;&nbsp;&nbsp;priceRange    | string   | Fare range (unit: yuan) | e.g., 3-7;|
| &nbsp;&nbsp;&nbsp;&nbsp;lineType      | int      | Line type             | 0-Regular, 1-Night, 2-Temporary (no info currently), 3-Section, 4-Major stops; |
| &nbsp;&nbsp;&nbsp;&nbsp;- station     | object   | Station information             |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stopNo        | string   | Station number             |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stopName      | string   | Station name             |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;startEarlyLateTime | string | Station first train time       | Format hhmm;|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;endEarlyLateTime | string | Station last train time       | Format hhmm;|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type          | int      | Boarding and alighting agreement           | 0 or null means both boarding and alighting allowed, 1 means alighting only;|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- point       | object   | Station location             |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lon        | string   | Longitude                 |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lat        | string   | Latitude                 |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- dispatchCarSchedule | object   | Interval information             |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;scheduleCode  | int      | Dispatch code             | -1 indicates not in operation, 0 indicates no real-time data, 1 indicates normal data;|| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;scheduleType  | int      | Scheduling type      | 0 indicates arriving every xx minutes, 1 indicates arriving at xx o'clock; |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;scheduleTime  | string   | Scheduling time      |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;scheduleMsg   | string   | Scheduling message   |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;scheduleMsgDefault | string   | Default scheduling message |                                                              |
| - bigStationMetroList | object   | Major station metro information |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;indexId       | int      | Unique database ID   |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;lineNo        | string   | Line number          |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;lineName      | string   | Line name            |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;upDown        | int      | Up or down direction | 0 - Up, 1 - Down; |
| &nbsp;&nbsp;&nbsp;&nbsp;startStopName | string   | Starting station name |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;endStopName   | string   | Ending station name  |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;startEarlyLateTime | string | First train time     | Format: hhmm; |
| &nbsp;&nbsp;&nbsp;&nbsp;endEarlyLateTime | string | Last train time      | Format: hhmm; |
| &nbsp;&nbsp;&nbsp;&nbsp;priceRange    | string   | Fare range (unit: yuan) | e.g., 3-7; |
| &nbsp;&nbsp;&nbsp;&nbsp;lineType      | int      | Line type            | 0 - Regular, 1 - Night, 2 - Temporary (no information available), 3 - Sectional, 4 - Major stations; |
| &nbsp;&nbsp;&nbsp;&nbsp;- station     | object   | Station information  |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stopNo        | string   | Station number       |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stopName      | string   | Station name         |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;startEarlyLateTime | string | First train time at the station | Format: hhmm; |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;endEarlyLateTime | string | Last train time at the station | Format: hhmm; |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type          | int      | Boarding and alighting agreement | 0 or empty means both boarding and alighting allowed, 1 means alighting only; |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- point       | object   | Station location     |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lon        | string   | Longitude            |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lat        | string   | Latitude             |                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-

**Official site: ** [https://www.shmaas.cn/](https://www.shmaas.cn/)
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

Resource file: `resources/mcp/shmaas-shmaas.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
