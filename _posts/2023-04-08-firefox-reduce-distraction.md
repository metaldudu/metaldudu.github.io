---
layout: post
title: "firefox浏览器减少干扰"
category: tech
tags: [tech]
---

切换到 firefox 做主力，除了安全性以外还有一点，就是自定义更多。减少浏览器的干扰，有两方面，一是布局二是内容。

布局上尽量扩大可用面积，减少不必要的UI组建，可以使用 userChrome.css 自定义布局。我参考了 https://github.com/Dook97/firefox-qutebrowser-userchrome 这个比较极端的方案，试用一段时间把地址栏和鼠标提示url的部分打开，这里是[我的配置](https://gist.github.com/metaldudu/6572156f27174624795d7a9f2ca8a405)。多用快捷键而不是鼠标，效率会高很多，比如在xfce里设置快捷键让窗口靠左靠右，不需要鼠标拖动。况且这么一设置，firefox 没有标题栏无法拖动。

内容方面，用 uBlock Origin 来屏蔽广告，同时对常去的网站进行“消毒”，就是屏蔽不想要的元素。比如大部分网站都有醒目的链接，提示下载移动端，直接屏蔽掉就清爽了很多。

用 [darkreader](https://github.com/darkreader/darkreader) 或 [Dark Mode](https://mybrowseraddon.com/dark-mode.html) 来获得暗色模式，减少视觉刺激。

firefox 会阻止网页自动播放视频。看视频时灵活使用全屏、网页全屏，获得更好的体验。另外如果看直播，可以[绕开浏览器获取地址](https://github.com/wbt5/real-url)，直接用 mpv 播放。

firefox 支持阅读模式，快捷键是 ctrl+alt+r 。在手机上遇到悬浮提示安装app时，可以打开阅读模式，针对知乎很好用。