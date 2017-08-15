---
layout: post
title: "使用本地文件做chrome新标签页"
description: ""
category: geek
tags: [git]
---

# 使用本地文件做chrome新标签页

Chrome新版本把新标签页作为搜索入口，bing和google都会显示搜索框，速度慢。网上的自定义newtab的插件，大多功能多余。在[网上](http://superuser.com/questions/907234/change-chrome-new-tab-page-to-local-file)找到一个自制插件的方法，在Chrome54下可用。

## 步骤

* 新建文件夹
* 创建 `home.html` 文件作为要显示的页面
* 创建 `manifest.json` 文件，内容如下

    {
  "name": "My custom new tab page",
  "description": "Overrides the new tab page",
  "version": "0.1",
  "incognito": "split",
  "chrome_url_overrides": {
    "newtab": "home.html"
  },
  "manifest_version": 2
}
* 打开Chrome插件管理，勾选开发者模式
* 定位刚才的文件夹，完成！


链接：

* [Change Chrome New Tab Page to local file](http://superuser.com/questions/907234/change-chrome-new-tab-page-to-local-file)

`20161128`
