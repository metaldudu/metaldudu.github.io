---
layout: post
title: "Linux下RSSreader对比"
category: tech
tags: [RSS]
---

因为换了2k显示器，发现原有的 QuiteRSS 字体偏大，也缺少暗色模式，于是又折腾一圈，比较了几个 linux 下的本地阅读器：

###  Liferea

前些年从 feedly 切换到本地，基于 gtk ，体积小速度快，支持暗色模式，只支持 http 代理，界面比较简洁。支持订阅的分组拖动，这一点原生应用强大。可以通关插件 [Edit Accels](https://github.com/mozbugbox/liferea-plugin-studio) 自定义快捷键。一直在[更新](https://github.com/lwindolf/liferea/)

### QuiteRSS

之前因为需要 socks5 代理用了一段时间，速度快，支持 http/socks5 代理，支持自定义快捷键。界面老套，没有暗色模式。长期不更新了。

### Fluent Reader

应该是打包了 Electron 的套壳程序，体积巨大。支持 pac 模式的代理，实测可行。但分组管理订阅功能几乎残废，这一点就直接pass了。美观的一塌糊涂。

### NewsFlash

软件体积和美观做到了平衡，也支持修改配置文件来添加代理，但并不支持拖动订阅。在我这里遇到一个bug，每次启动程序，配置文件都会重置，以至于任何修改都无法保存，只能弃了。

### RSS Guard

功能完备，包括代理、主题（gtk主题），基于账户登录的管理模式，内容渲染效果不好，界面逻辑和主流程序不一样。

另外基于 Gnome/KDE 的阅读器没测试。结论是用回了 Liferea ，天道好轮回。

另外我还试了试 newsboat ，命令行无法显示图片，其他都好。