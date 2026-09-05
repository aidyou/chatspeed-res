---
title: "mogutongxue-mcp-server"
description: "About what I want to achieve on Windows computer: 'Xiao Ai, open Kuwo Music' and 'Xiao Ai, cut the song' ---关于我想在windows电脑上实现：'小爱同学，打开酷我音乐'与'小爱同学，切歌'这件事- 实现\"蘑菇同学,打开酷我音乐\"与\"蘑菇同学,切歌\"这两件事 实现原理:java运行cmd命令"
---

# mogutongxue-mcp-server

About what I want to achieve on Windows computer: 'Xiao Ai, open Kuwo Music' and 'Xiao Ai, cut the song' ---关于我想在windows电脑上实现：'小爱同学，打开酷我音乐'与'小爱同学，切歌'这件事- 实现"蘑菇同学,打开酷我音乐"与"蘑菇同学,切歌"这两件事 实现原理:java运行cmd命令

# mogutongxue-蘑菇同学-mcp-server

About what I want to achieve on Windows computer: 'Xiao Ai, open Kuwo Music' and 'Xiao Ai, cut the song'
---关于我想在windows电脑上实现：'小爱同学，打开酷我音乐'与'小爱同学，切歌'这件事-

## 演示视频:
https://www.bilibili.com/video/av114929751298782/

## 作用:

实现"蘑菇同学,打开酷我音乐"与"蘑菇同学,切歌"这两件事

```
GET http://localhost:8001/chat/option/call?
    query=小爱同学,我常用的软件都在C盘rj文件夹内,打开酷我音乐

GET http://localhost:8001/chat/option/call?
    query=小爱同学,切歌
```



实现原理:java运行cmd命令与java模拟键盘按键

```java
//真正干活的两句代码
//运行cmd
new ProcessBuilder("cmd", "/c", "start", "\"\"", "\"" + filePath + "\"").start();

//模拟键盘按下
robot.keyPress(keyCode);
```



## 部署方式:

1.下载源码 或 git clone

2.运行代码 (我是用idea运行的qwq) 应该是需要在本机部署maven和jdk21,然后mvn run (大概吧qwq,java萌新哭唧唧)

3.添加mcp

##### json格式:

```json
{
  "mcpServers": {
    "mogutongxue": {
      "url": "http://localhost:8083/sse"
    }
  }
}
```

##### 自定义添加:

类型:sse

url: http://localhost:8083/sse

4.修改一下代码qwq (想着开发个可视化的ui界面,但是感觉太麻烦了,就不想弄了)

修改以下位置

...\mogutongxue-mcp\mogutongxue-api\src\main\resources\config.json

参照'切歌',写一下你想让mcp实现的快捷键功能即可

其他的都不用动qwq,当然你想加点其他的东西也可以

5以上,此致敬礼qwq



## 写在后面:

java小白,闲着没事写着玩的,希望能给大佬们提供一丢丢思路,希望有一天能真的用自然语言操作计算机

**Official site: ** [https://github.com/mogu520999/mogutongxue](https://github.com/mogu520999/mogutongxue)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `files`, `communication`, `media`
- Tags: `communication`, `entertainment and media`, `file systems`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/mogu520999-mogutongxue.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
