---
layout: post
title: "MDwiki笔记"
category: tech
tags: [markdown]
---

## MDwiki

[MDwiki](https://github.com/Dynalon/mdwiki)是一套简单的wiki系统，基于markdown文件，运行于客户端（HTML5/Javascript）。所以，本地运行或上传到github都很方便。

## 需求

- 支持静态文件的服务器

## 如何使用

- 下载最新的mdwiki.html文件，[地址](https://github.com/Dynalon/mdwiki/releases)，不建议选择mdwiki-slim.html，文件体积小但需要实时下载资源。
- 创建一个文件夹作wiki的目录，直接修改 mdwiki.html 为 index.html，配置好服务器就可以访问了。
- 新建 `index.md`，这就wiki的主页，这是wiki的起始页。
- 在wiki目录下创建要写的wiki页面，比如test.md，在`index.md`文件中添加链接，如`[test](test.md)`
- 刷新浏览器，预览。

## 自定义导航

在wiki目录下创建两个文件，`navigation.md` 和 `config.json`，分别实现顶部导航，和页面侧边导航。示例如下：

**navigation.md**

```
# Your wiki name

[Home](index.md)
[About](about.md)
[Download](download.md)
```

**config.json**
```
{
    "useSideMenu": true,
    "lineBreaks": "gfm",
    "additionalFooterText": "All content and images &copy; by John Doe",
    "anchorCharacter": "#"
}
```

## 基于python的服务器

在linux下可以方便的使用python的内置服务器，建立一个脚本`run.sh`并增加运行权限：

```
#!/bin/bash

python3 makeindex.py
xdg-open http://localhost:8000
python3 -m http.server
```
每次双击脚本，就可以打开浏览器并查看wiki。

windonws下可以建立 `run.bat`

```
python makeindex.py
python -m http.server

path=%path%, "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
start chrome http://127.0.0.1:8000

```

## 自动生成文件索引

可以通过简单的python脚本，实现所有markdown文件的索引页。

---

更新时间：20181015

参考文档

* [MDwiki (and how to get started)](https://gist.github.com/alias1/a8c3c2fd7bf2f50ff666)