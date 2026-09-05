---
title: "地图旅行者MCP"
description: "一种MCP服务器，它在Google Maps上创建虚拟旅行环境，允许用户引导一个头像进行旅程，并带有照片报告和SNS集成。"
---

# 地图旅行者MCP

一种MCP服务器，它在Google Maps上创建虚拟旅行环境，允许用户引导一个头像进行旅程，并带有照片报告和SNS集成。

# Virtual Traveling bot environment for MCP

英语 / [日语](https://github.com/mfukushim/map-traveler-mcp/blob/HEAD/README_jp.md)

这是一个MCP服务器，它为虚拟化身在Google地图上旅行创建了一个环境。

通过Claude Desktop等MCP客户端，您可以向虚拟化身发出指令，并通过照片报告其旅程的进展情况。

> 现已支持 librechat https://www.librechat.ai/。

## 功能

#### MCP 服务器工具功能

作为MCP服务器，可以使用以下功能。可用功能取决于设置和执行状态。

您可以直接指定功能名称，但Claude LLM会自动识别，因此可以用一般术语指定操作。

示例：
“你现在在哪里？” “让我们出发去东京站。”

- get_traveler_view_info(includePhoto:boolean,includeNearbyFacilities:boolean)  
  获取当前旅行化身的位置信息。  
  - includePhoto: 获取附近的谷歌街景照片。如果您设置了图像生成AI，它会合成化身。
  - includeNearbyFacilities: 获取附近设施的信息。
- get_traveler_location()  
  获取当前旅行化身的地址和附近设施信息。
- reach_a_percentage_of_destination()
  达到目的地的指定百分比（仅在moveMode=skip时有效）
  timeElapsedPercentage: 向目的地前进的百分比进度(0~100)
- set_traveler_location(address: string)  
  设置当前旅行化身的位置。
  - address: 地址信息（确切地址，或Google Maps或Claude可以识别的一般名称等）
- get_traveler_destination_address  
  获取您设置的旅行化身的目的地
- set_traveler_destination_address(address: string)  
  设置旅行化身的目的地
   - address: 地址信息（确切地址，或Google Maps或Claude可以识别的一般名称等）
- start_traveler_journey  
  在目的地开始旅程。（仅在moveMode=realtime时有效）
- stop_traveler_journey  
  停止旅程。（仅在moveMode=realtime时有效）
- set_traveler_info(settings:string)  
  设置旅行者的属性。动态更改您想要改变的旅行者个性，如姓名和性格。但是，如果您使用角色脚本，脚本将更加稳定。
  - settings: 如姓名和性格等设置信息。
- get_traveler_info  
  获取旅行者的属性。获取旅行者的个性。
- set_avatar_prompt(prompt:string)  
  设置生成旅行化身图像时的提示。默认为动漫风格女性。强制执行动漫风格以防止产生虚假图像。
  - prompt
- reset_avatar_prompt  
  将化身生成提示重置为默认值。
- get_sns_feeds  
  获取指定自定义订阅中的Bluesky SNS文章（包含特定标签的订阅）。
- get_sns_mentions  
  获取最近对自己发布的Bluesky SNS帖子的提及（点赞、回复）。
- post_sns_writer(message:string)  
  使用指定的自定义订阅发布文章到Bluesky SNS。设置特定标签以便能够确定该帖子是由旅行机器人生成的。
  - message: 文章内容
- reply_sns_writer(message:string,id:string)  
  回复具有指定ID的文章。设置特定标签以便能够确定该帖子是由旅行机器人生成的。
  - message: 回复内容
  - id: 要回复的帖子ID
- add_like(id:string)  
  给指定的帖子添加赞。
  - id: 要点赞的帖子ID
- tips  
  指导您如何设置尚未配置的功能。
- get_setting  
  获取环境和图像设置。

#### MCP资源

有两个自定义提示样本。
当你通过 Claude Desktop 导入提示时，Claude 将扮演旅行者的角色。
SNS 兼容版本在进行旅行对话的同时控制 SNS 的输入和输出。

- role.txt  
  Claude 将扮演旅行者。

- roleWithSns.txt  
  Claude 将扮演旅行者。它还控制读取和发布到 SNS。
- carBattle.txt  
  这是一个关于从横滨到东京运送秘密文件的小说游戏。场景是自动生成的。设置 moveMode=skip 来游玩。

## 设置

你需要获取并设置多个 API 的访问密钥，例如用于访问多个 Google 地图和生成图像。
使用 API 可能会产生费用。

#### 使用 Claude Desktop 的设置
claude_desktop_config.json
```json
{
  "mcpServers": {
    "traveler": {
      "command": "npx",
      "args": ["-y", "@mfukushim/map-traveler-mcp"],
      "env":{
        "MT_GOOGLE_MAP_KEY":"(Google Map API key)",
        "MT_MAP_API_URL": "(Optional: Map API custom endpoint. Example: direction=https://xxxx,places=https://yyyy )",
        "MT_TIME_SCALE": "(Optional:Scale of travel time on real roads duration. default 4)",
        "MT_SQLITE_PATH":"(db save path: e.g. %USERPROFILE%/Desktop/traveler.sqlite ,$HOME/traveler.sqlite )",
        "MT_REMBG_PATH": "(absolute path of the installed rembg cli)",
        "MT_REMBG_URL": "(rembg API URL)",
        "MT_PIXAI_KEY":"(pixAi API key)",
        "MT_SD_KEY":"(or Stability.ai image generation API key",
        "MT_PIXAI_MODEL_ID": "(Optional: pixAi ModelId, if not set use default model 1648918127446573124 ",
        "MT_COMFY_URL": "(Option: Generate image using ComfyUI API at specified URL. Example: http://192.168.1.100:8188)",
        "MT_COMFY_WORKFLOW_T2I": "(Optional: Path to API workflow file when using text to image with ComfyUI. If not specified: assets/comfy/t2i_sample.json)",
        "MT_COMFY_WORKFLOW_I2I": "(Optional: Path of API workflow file when image to image in ComfyUI. If not specified: assets/comfy/i2i_sample.json)",
        "MT_COMFY_PARAMS": "(Optional: Variable values to send to the workflow via comfyUI API)",
        "MT_FIXED_MODEL_PROMPT": "(Optional: Fixed avatar generation prompt. You will no longer be able to change your avatar during conversations.)",
        "MT_BODY_AREA_RATIO": "(Optional: Acceptable avatar image area ratio. default 0.042)",
        "MT_BODY_HW_RATIO": "(Optional: Acceptable avatar image aspect ratios. default 1.5~2.3)",
        "MT_BODY_WINDOW_RATIO_W": "(Optional: Avatar composite window horizontal ratio. default 0.5)",
        "MT_BODY_WINDOW_RATIO_H": "(Optional: Avatar composite window aspect ratio. default 0.75)",
        "MT_BS_ID":"(Bluesky sns registration address)",
        "MT_BS_PASS":"(bluesky sns password)",
        "MT_BS_HANDLE":"(bluesky sns handle name: e.g. xxxxxxxx.bsky.social )",
        "MT_FILTER_TOOLS": "(Optional: Directly filter the tools to be used. All are available if not specified. e.g. tips,set_traveler_location)",
        "MT_MOVE_MODE": "(Option: Specify whether the movement mode is realtime or skip. default realtime)",
        "MT_IMAGE_WIDTH": "(Option: Output image width (pixels) Default is 512)",
        "MT_NO_IMAGE": "(Options: true = do not output image, not specified = output image if possible, default is not specified)"
      }
    }
  }
}
```
> 注意：环境变量已重命名为标准蛇形命名法。添加了 MT_ 前缀，因为它们可能会与其他环境变量（如 librechat 中的）一起使用。旧名称仍可用于向后兼容。  

请为 Google Map API 设置以下三个凭据。  
- 街景静态 API
- 地点 API（新）
- 时区 API
- 方向 API

[https://developers.google.com/maps/documentation/streetview/get-api-key](https://developers.google.com/maps/documentation/streetview/get-api-key)

如果你想使用图像生成 AI，请设置 pixAi_key 或 sd_key。还需要在你的 PC 上安装 python3.7~3.11 并安装 rembg cli（推荐使用虚拟环境）。

[https://platform.pixai.art/docs](https://platform.pixai.art/docs)  
[https://platform.stability.ai/docs/api-reference#tag/SDXL-1.0-and-SD1.6/operation/textToImage](https://platform.stability.ai/docs/api-reference#tag/SDXL-1.0-and-SD1.6/operation/textToImage)

bluesky SNS 地址/密码是可选的。建议创建一个专用账户，因为它会自动发布内容。

[https://bsky.app/](https://bsky.app/)

你也可以运行实践模式，这种模式不需要验证用的 API 密钥。

#### 实践模式设置
claude_desktop_config.json
```json
{
  "mcpServers": {
    "traveler": {
      "command": "npx",
      "args": ["-y", "@mfukushim/map-traveler-mcp"]
    }
  }
}
```

## 如何使用

#### 使用实践模式

1. 安装 nodejs 22。

2. 设置 Claude Desktop 以供使用。

3. 在 claude_desktop_config.json 中反映上述设置之一。

4. 重启 Claude Desktop。设置可能需要一些时间（如果发生错误，请尝试再次重启 Claude Desktop。如果仍然不起作用，请参阅下面的说明）。确保屏幕右下角出现以下标记。

  

5. 询问“你现在在哪里？”和“开始旅行。”将开始对话。使用 API 时会出现确认屏幕，请选择允许。

6. 从 MCP 中选择附加，并选择 role.txt。

7. 已内置旅行提示，您可以随意与之交谈。

#### 使用完整功能

1. 获取 Google Map API 访问密钥，并设置 Street View Static API、Places API（新）、Time Zone API 和 Directions API 的权限。在 `claude_desktop_config.json` 的 env 中设置这些，并重新启动。
   此时，旅行日志将基于真实地图。如果没有叠加，旅行图片也将被输出。
2. 决定一个不会干扰磁盘的路径，并将其设置在 `claude_desktop_config.json` 的 env 中的 sqlite_path 里。（例如：`%USERPROFILE%/Desktop/traveler.sqlite` 或 `$HOME/Documents/traveler.sqlite` 等）
   此时，您的旅行日志将被保存，即使关闭 Claude Desktop，您也可以继续旅程。
3. 安装 Python 3.7 到 3.11，并使用 cli 安装 rembg。我们建议使用如 venv 这样的虚拟环境。
```bash
  python3 -m venv venv
  . venv/bin/activate or .\venv\Scripts\activate
  pip install "rembg[cpu,cli]"
```
  使用示例图像文件检查 rembg cli 是否正常工作。输入包含人物的图像，如果输出文件中人物被剪切出来，则表示一切正常。  
```bash
  rembg i source_image_file dest_image_file
```
4. rembg cli 将安装在 Python exe 位置，因此获取该路径。文件位置取决于操作系统和 Python 的安装状态，但在 venv 的情况下，它位于 (虚拟环境名称)\Scripts\rembg.exe 或 (虚拟环境名称)/bin/rembg 上方的目录中。如果您找不到，请使用文件搜索软件查找路径。将该路径设置为 `claude_desktop_config.json` 中 env 的 rembg_path。（例如：`"rembg_path": "C:\\Users\\xxxx\\Documents\\rembg_venv\\venv\\Scripts\\rembg.exe"`）
5. 从 pixAI 或 Stability.ai 网站获取图像生成 API 密钥。将密钥设置为 `claude_desktop_config.json` 的 env 中的 pixAi_key 或 sd_key。
   现在头像将被叠加到旅行图像上。
6. 获取 bluesky SNS 的地址/密码和用户名。分别在 `claude_desktop_config.json` 的 env 中设置 bs_id、bs_pass 和 bs_handle。
   导入旅行知识提示角色文件 roleWithSns.txt 以向 SNS 报告旅行活动（它将自动作为机器人发布，因此建议分配专用账户）

除了通过 cli 准备 rembg 外，我们还添加了一个允许您将 rembg 作为服务 API 处理的设置。  
如果您配置了以下 rembg 服务，可以通过设置 remBgUrl 来使用 rembg。  

[https://github.com/danielgatis/rembg?tab=readme-ov-file#rembg-s](https://github.com/danielgatis/rembg?tab=readme-ov-file#rembg-s)  

如果您使用 Docker 版本来启动容器并访问，设置非常简单。  

[https://github.com/danielgatis/rembg?tab=readme-ov-file#usage-as-a-docker](https://github.com/danielgatis/rembg?tab=readme-ov-file#usage-as-a-docker)  

#### 当使用外部 ComfyUI（适用于更高级用户）

您还可以使用本地 ComfyUI 作为图像生成服务器。您可以自行详细配置图像生成特性，以减少 API 成本。

不过，配置将会相当复杂，图像生成可能需要更长的时间。

1. 配置ComfyUI以API模式运行。
2. 在环境变量中将服务器URL设置为`comfy_url`。
3. 以JSON字符串的形式在环境变量中设置详细的配置值，例如要使用的模型。
示例。
```json
{
  "env": {
    "comfy_url": "http://192.168.1.100:8188",
    "comfy_workflow_t2i": "C:\\Documents\\t2itest.json",
    "comfy_workflow_i2i":"C:\\Documents\\i2itest.json",
    "comfy_params":"ckpt_name='animagineXL40_v40.safetensors',denoise=0.65"
  }
}
```
4. 默认的工作流程可以使用包中的`assets/comfy/t2i_sample.json`和`assets/comfy/i2i_sample.json`。你可以使用%来指定变量，并在`comfy_params`中定义这些变量。

## 使用libreChat

它已经被调整以兼容libreChat。这使得它的使用更加简便，但仍然需要一些额外的设置。  
此外，除非你使用的电脑具有足够的性能（比如能够稳定运行Docker），否则似乎不会很稳定。

#### 安装libreChat  

请确保按照官方网站上的描述正确安装并运行。  
在这种情况下，由于需要进行额外的配置，我们推荐使用Docker方式进行安装。

[https://www.librechat.ai/docs/local/docker](https://www.librechat.ai/docs/local/docker)  

按照官方指南配置`librechat.yaml`文件。  
我认为你需要添加一个本地或API LLM服务。  

[https://www.librechat.ai/docs/configuration/librechat_yaml](https://www.librechat.ai/docs/configuration/librechat_yaml)  

创建登录用户。  

[https://www.librechat.ai/docs/configuration/authentication#create-user-script](https://www.librechat.ai/docs/configuration/authentication#create-user-script)  

请进行设置以便能够进行常规的聊天对话。  

#### 增加带有额外设置的rembg容器  

为了通过Docker使用rembg，请增加拉取和运行rembg Docker容器的操作。

`docker-compose.override.yml`
```yml
 services:
   api:
     volumes:
       - type: bind
         source: ./librechat.yaml
         target: /app/librechat.yaml

   rembg:
     image: danielgatis/rembg:latest
     restart: always
     command: "s --host 0.0.0.0 --port 7000 --log_level info"

```

#### 向MCP服务添加map-traveler-mcp  

在`librechat.yaml`中添加
```yaml
mcpServers:
  traveler:
    type: stdio
    command: npx
    args:
      - -y
      - "@mfukushim/map-traveler-mcp"
```

添加`.env`文件（与`claude_desktop_config.json`中的`env`相同）

```env
# map-traveler-mcp
GoogleMapApi_key=(Google Map API key)
sqlite_path=/home/run_test.sqlite (e.g. librechat in an unobtrusive location inside the container, or in an external directory that you don't want to mount.)
remBgUrl=http://rembg:7000 (rembg Service API URL, container URL)
(Other settings such as image generation AI settings, PixAI key, stability.ai API key, ComfyUI settings, etc.)

```

完成设置后，请重启容器。  
在速度较慢的PC上，MCP初始化可能会失败。多次重启可能有所帮助，但这可能会难以成功运行...

#### libreChat 设置

要在libreChat中使用MCP功能，请利用Agents功能。

1. 在对话屏幕中，选择 Agents。  
   

2. 从屏幕右侧的面板中选择 Agent Builder 并配置您的代理。  
   

3. 选择 Add Tools 来使用 map-traveler。  
   

4. 将会出现代理工具屏幕，请选择并添加所有 map-traveler-mcp 工具（如果未列出 map-traveler-mcp 工具，则 MCP 初始化失败，请重启容器或通过检查日志等重新检查设置）。  
   
  
   
  
5. 在指令区域输入额外脚本。  
   由于 libreChat 没有 MCP 资源功能，请将以下 URL 的内容文本复制到指令区域中代替。   
   https://github.com/mfukushim/map-traveler-mcp/blob/main/assets/scenario/role.txt  
   
  
6. 点击 Create 按钮保存代理。  
   

7. 开始新的聊天。

## 安装指南（日语，但有很多图片）

1. 介绍和练习模式  
   https://note.com/marble_walkers/n/n7a8f79e4fb30
2. 数据库、Google 地图 API、图像生成 API  
   https://note.com/marble_walkers/n/n765257c27f3b
3. 头像提示  
   https://note.com/marble_walkers/n/nc7273724faea
4. 社交媒体集成  
   https://note.com/marble_walkers/n/na7c956befe7b
5. 应用程序 1  
   https://note.com/marble_walkers/n/n3c86edd8e817
6. ComfyUI API  
   https://note.com/marble_walkers/n/ncefc7c05d102  
7. 应用程序 2  
   https://note.com/marble_walkers/n/ne7584ed231c8
8. LibreChat 设置  
   https://note.com/marble_walkers/n/n339bf7905324

#### 关于源代码的补充说明

我使用 Effect.ts 来简化错误管理和为了自我学习。  
我们也使用了 Effect Service，但由于 MCP 调用的工作方式，我们认为通过 Service 进行整合并不是最优的选择。  
我认为直接在 Effect 中处理 MCP 调用会更简单。

#### 最新更新注意事项

在 env 中添加了 image_width。默认值为 512。将其设置得更小可能会降低 LLM API 的成本。
添加了一个针对没有图像输入/输出的 MCP 客户端不输出图像的 env 设置。
"MT_NO_IMAGE": "true" 将不会生成或输出任何图像。其他与图像相关的设置可以省略。
```
{
  
  "env": {
    "MT_NO_IMAGE": "true"
  }
  
}
or
{
  
  "env": {
    "GoogleMapApi_key": "xxxx",
    "MT_NO_IMAGE": "true"
  }
  
}

```

**官方网站：** [https://github.com/mfukushim/map-traveler-mcp](https://github.com/mfukushim/map-traveler-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`location services`, `image and video processing`, `social media`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @mfukushim/map-traveler-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/mfukushim-map-traveler.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
