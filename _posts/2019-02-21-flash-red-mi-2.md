---
layout: post
title: "红米2刷机记录"
category: tech
tags: []
---

上一次刷机还是两年前的nexus5，这次的目的是在红米2手机（移动版，安卓4.4）上安装 linux deploy，所以需要root。简单过程如下：

1. 搜到一个页面有详细资料：[红米2刷机资源简单整理](https://redmi2-flashing-tips.github.io/)
2. 下载最新版的LineageOS，[地址](https://download.lineageos.org/wt88047)
3. 下载TWRP包，作者时代的导航者，[地址](http://blog.sina.cn/dpool/blog/s/blog_beaf52dc0102w9w8.html?type=-1)
4. 红米2按电源和音量减，进入米兔画面fastboot
5. 连接数据线，运行TWRP包的bat文件，写入recovery，重启进入，刷入LineageOS包。重启后报邮件app运行错误，禁用后正常。
6. 下载最新的supersu，按照步骤5刷入，重启后反复重启现实mi图标，俗称“卡米”。怀疑镜像
7. 此时用电源键加音量加启动手机，无法进入recovery模式。
8. 下载最新版的TWRP镜像，覆盖，通过fastboot进入TWRP，发现新版不支持SD卡，使用adb push传输。重新刷机。
9. 改用magisk，重复步骤5刷入，然后安装 magisk manager，busybox，Linux Deploy，都在github找最新版。
10. 按照网上帖子配置安装 Ubuntu，源选择 `http://mirrors.ustc.edu.cn/ubuntu-ports/`


后续的工作：

1. 默认python3，安装bs4：`apt-get install python3-bs4`
2. 编辑crontab

待续