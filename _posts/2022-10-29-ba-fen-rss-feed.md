---
layout: post
title: "八分的RSS订阅"
category: tech
tags: [podcast, software]
---

这几年常听的播客里，八分是一直听下来的，今年到了第四季，官方把 RSS 关闭转而在喜马拉雅独家播放。因为对移动端的垃圾应用不感兴趣，所以之前是用曲线救国的方式听：

- 定期访问[梁文道·八分](https://www.ximalaya.com/album/51101122)，使用[脚本](https://greasyfork.org/zh-CN/scripts/435495)下载 m4a 文件
- 用 [Syncthing](https://syncthing.net/) 同步到手机
- 用 [Muiscolet](https://krosbits.in/musicolet/) 播放，一遍用1.3倍速

这个方法也是在 github 上看到有人这么做，不过是用的云服务。

今天想到 RSSHub 应该可以实现输出喜马拉雅的更新，果然找到这个地址：

[https://rsshub.app/ximalaya/album/51101122/0/shownote](https://rsshub.app/ximalaya/album/51101122/0/shownote)

这个 RSS 地址需要科学上网，但实际音频地址不需要。而且我之前的播客也是手动获取喜马拉雅的音频地址，算是偷偷利用吧。

同样 RSSHub 号称万物皆可 RSS ，能找到很多订阅内容，而且可以自行部署，方便有针对性的接收信息。