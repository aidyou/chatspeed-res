---
title: "关于我想在windows电脑上实现：'蘑菇同学，打开酷我音乐' 与 '蘑菇同学，切歌'这件事-(MCP&Agent挑战赛)"
description: "关于我想在Windows电脑上实现：“小爱同学，打开酷我音乐”与“小爱同学，切歌”这件事\n\n- 实现“蘑菇同学, 打开酷我音乐”与“蘑菇同学, 切歌”这两件事\n- 实现原理：Java运行CMD命令\n\njava\n// 示例代码：使用Java执行CMD命令\npublic class MusicController {\n    public static void main(String[] args) {\n        try {\n            // 打开酷我音乐\n            Process processOpen = Runtime.getRuntime().exec(\"start \\\"\\\" \\\"C:\\\\Program Files\\\\Kuwo\\\\KuwoMusic.exe\\\"\");\n            processOpen.waitFor();\n\n            // 切歌（假设通过发送快捷键或调用API来实现）\n            Process processSkip = Runtime.getRuntime().exec(\"powershell -command \\\"Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.SendKeys]::SendWait('{MEDIA_NEXT_TRACK}')\\\"\");\n            processSkip.waitFor();\n        } catch (Exception e) {\n            e.printStackTrace();\n        }\n    }\n}\n\n\n上述代码展示了如何使用Java来执行CMD命令以实现打开酷我音乐和切歌的功能。请注意，实际路径和命令可能需要根据你的具体环境进行调整。\n\n更多关于Java执行系统命令的信息可以参考[官方文档](https://docs.oracle.com/javase/8/docs/api/java/lang/Runtime.html#exec-java.lang.String-)。"
---

# 关于我想在windows电脑上实现：'蘑菇同学，打开酷我音乐' 与 '蘑菇同学，切歌'这件事-(MCP&Agent挑战赛)

关于我想在Windows电脑上实现：“小爱同学，打开酷我音乐”与“小爱同学，切歌”这件事

- 实现“蘑菇同学, 打开酷我音乐”与“蘑菇同学, 切歌”这两件事
- 实现原理：Java运行CMD命令

java
// 示例代码：使用Java执行CMD命令
public class MusicController {
    public static void main(String[] args) {
        try {
            // 打开酷我音乐
            Process processOpen = Runtime.getRuntime().exec("start \"\" \"C:\\Program Files\\Kuwo\\KuwoMusic.exe\"");
            processOpen.waitFor();

            // 切歌（假设通过发送快捷键或调用API来实现）
            Process processSkip = Runtime.getRuntime().exec("powershell -command \"Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.SendKeys]::SendWait('{MEDIA_NEXT_TRACK}')\"");
            processSkip.waitFor();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}


上述代码展示了如何使用Java来执行CMD命令以实现打开酷我音乐和切歌的功能。请注意，实际路径和命令可能需要根据你的具体环境进行调整。

更多关于Java执行系统命令的信息可以参考[官方文档](https://docs.oracle.com/javase/8/docs/api/java/lang/Runtime.html#exec-java.lang.String-)。

# mogutongxue-蘑菇同学-mcp-server

关于我想在Windows电脑上实现：'小爱同学，打开酷我音乐'与'小爱同学，切歌'这件事

## 演示视频:
https://www.bilibili.com/video/av114929751298782/

## 作用:

实现"蘑菇同学,打开酷我音乐"与"蘑菇同学,切歌"这两件事

GET http://localhost:8001/chat/option/call?
    query=小爱同学,我常用的软件都在C盘rj文件夹内,打开酷我音乐

GET http://localhost:8001/chat/option/call?
    query=小爱同学,切歌

实现原理: Java运行CMD命令与Java模拟键盘按键

java
// 真正干活的两句代码
// 运行cmd
new ProcessBuilder("cmd", "/c", "start", "\"\"", "\"" + filePath + "\"").start();

// 模拟键盘按下
robot.keyPress(keyCode);

## 部署方式:

1. 下载源码 或 git clone

2. 运行代码 (我是用idea运行的qwq) 应该是需要在本机部署maven和jdk21,然后mvn run (大概吧qwq,java萌新哭唧唧)

3. 添加mcp

##### json格式:

json
{
  "mcpServers": {
    "mogutongxue": {
      "url": "http://localhost:8083/sse"
    }
  }
}

##### 自定义添加:

类型: sse

url: http://localhost:8083/sse

4. 修改一下代码qwq (想着开发个可视化的ui界面,但是感觉太麻烦了,就不想弄了)

修改以下位置

...\mogutongxue-mcp\mogutongxue-api\src\main\resources\config.json

参照'切歌',写一下你想让mcp实现的快捷键功能即可

其他的都不用动qwq,当然你想加点其他的东西也可以

5以上,此致敬礼qwq

## 写在后面:

Java小白,闲着没事写着玩的,希望能给大佬们提供一丢丢思路,希望有一天能真的用自然语言操作计算机

**官方网站：** [https://github.com/mogu520999/mogutongxue](https://github.com/mogu520999/mogutongxue)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`files`, `communication`, `media`
- 标签：`communication`, `entertainment and media`, `file systems`

## MCP 配置

- 传输方式：`http`
- 启动命令：``
- 参数：无

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/mogu520999-mogutongxue.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
