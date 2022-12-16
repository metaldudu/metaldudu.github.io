---
layout: post
title: "思源黑体显示问题"
category: tech
tags: [font, linux]
---

前几天用了 cmus 播放音乐，偶然发现在歌曲列表里，“一”字会用宋体显示，而其他都是系统设置的思源黑体。这个现象也出现在 QuiteRSS 里面，“梅西”的“西”字。

搜索一圈也没找到问题的关键，我猜测是终端默认用西文等宽字体，遇到中文会选择黑体，但某些汉字笔画细就用衬线字体显示了。其实在操作系统和网页，黑体就挺好了。

另外有个问题是，思源字体和谷歌字体我都安装了，网上说两个字体其实是一样的，但貌似前者适用性更好，比如不会出现 CJK 文字显示混乱的问题（好像最开始我也遇到过）。至于安装思源宋体，完全是某一次想让 cablire 的 E-book Viewer 更美观，然而我也极少在笔记本电脑上看书，所以这次一并删掉。至此系统中中文字体只有：

- 思源黑体 adobe-source-han-sans
- 文泉驿微米黑、文泉驿微米黑等宽  wqy-microhei
- [霞鹜文楷](https://github.com/lxgw/LxgwWenKai) LXGWWenKai

系统、网页都用黑体，偶尔有阅读需求就用霞鹜文楷。另外终端用的是 [Fira Code](https://github.com/tonsky/FiraCode)。
