---
layout: post
title: "chromedriver"
category: tech
tags: [linux]
---

在使用某学习工具时，依赖 chromedriver 模拟浏览器（应该是 selenium），但因为 archlinux 下面 google-chrome 不在官方源里，而官方源里的 chromedriver 总是最新版，经常出现浏览器和 chromedriver 版本不一致，学习工具报错。

解决方法是让二者匹配，单独下载对应版本的 chromedriver。或者直接用官方源里的 chromium。

chromium 登录谷歌帐号，需要创建 `~/.config/chromium-flags.conf ` 文件，添加如下内容：

```
--oauth2-client-id=77185425430.apps.googleusercontent.com
--oauth2-client-secret=OTJgUOQcT7lO7GsGZq2G4IlT
```

重启后可以二步验证登录。

本来我更倾向于用 Firefox ，但在笔记本上偶尔会卡死。另外在从 KDE 切换到 xfce 后，google-chrome 无法启动，搜索了一圈发现只要删掉 `~/.config` 目录里的配置就好了。

---

[Enabling Chromium to sync with Google Account - Stack Overflow](https://stackoverflow.com/questions/67459316/enabling-chromium-to-sync-with-google-account)