---
layout: post
title: "python共享文件"
category: tech
tags: []
---

前两天一个朋友给我传文件，用了ksweb，一个安卓系统的服务器应用，支持http、php、mysql。这个朋友搭建了WordPress，看上去很不错。我花了点时间，在旧手机上实验了这个应用，发现有它的优势，可以作为一个轻量级的服务。

我突然想到，可以直接用python实现：

`python -m http.server`

只要在路由器配置端口转发和IP绑定，其他人就可以访问，小范围分享文件很方便，本地pc传文件到手机也可以。有时候思维被限制了，想不到简单的方法。

