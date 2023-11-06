---
title: 第 3 步：大功告成
icon: info
---

本篇会告诉你如何开启机器人与开关功能

# 开关功能

首先你要了解这个机器人的目录，

```text
module
 - NO_USE  # 关闭的功能
 - zh_cn  # 中文
 - zh_cht  # 繁体补丁
```

如果你不需要繁体请删除 zh_cht 文件夹

关闭功能请在这些文件中找到对应文件后扔到 NO_USE 文件夹中（zh_cn 与 zh_cht 里的文件都得扔进去）

# 开始使用

然后你就可以使用

```shell
pdm run python main.py
```

来运行机器人了

如果你想在后台使用，请自行搜索 `screen` 或 `tmux` 的使用方法

直接在搜索引擎内搜索 `Linux screen` 或 `Linux tmux` 即可（推荐使用 tmux）

本文档不赘述这两个工具的使用方法，如需教程请移步搜索引擎