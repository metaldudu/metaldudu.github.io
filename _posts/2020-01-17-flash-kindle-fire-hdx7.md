---
layout: post
title: "kindlefire平板刷机"
category: tech
tags: [手机]
---

偶然看到淘宝有卖刷好安卓7的kindlefire hdx7 三代平板，手上这个很久没打开了，试了试原有系统装不上b站的app，于是想刷一下，折腾的简单记录如下。

- 之前用kingroot，把机器root了，也（幸亏）装了 Safestrap
- 我直接下载了最新的 [LineageOS 14.1](https://forum.xda-developers.com/kindle-fire-hdx/orig-development/rom-cm-14-1-thor-t3517481) ，刷入后无法启动，出现官方的回复界面，我手欠还点了恢复，结果机器内部存储被清空
- 在xda论坛搜了一圈，结论是这个机器无法拷贝新的刷机包，已经死循环了。结果偶然看到帖子，说可以用adb方式传入数据
- 按照[亚马逊官方指导](https://developer.amazon.com/zh/docs/fire-tablets/connecting-adb-to-device.html)，安装adb驱动。这里的坑在于win7识别这个平板，正常状态是识别成平板设备，需要删掉这个设备，重新连接。发现新的usb设备后，手动更新驱动，选择亚马逊驱动安装的文件夹，这样会识别出adb设备。
- 命令行使用 `adb divices` ，会出现设备，然后用 `adb push xxx.img /sdcard/` 传送刷机包
- 因为暂时无法解锁（[解锁方法](https://zhuanlan.zhihu.com/p/22577425)），选择了旧版的CM11

