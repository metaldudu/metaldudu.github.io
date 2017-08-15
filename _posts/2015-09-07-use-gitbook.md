---
layout: post
title: "使用gitbook编辑电子书"
description: ""
category: geek
tags: [gitbook]
---

gitbook是基于markdown格式的电子书整理工具，可以发布成html格式，或导出pdf、epub、mobi等格式。前一段时间我就发现这个工具，错误的认为它是基于github的，而且要基于git编辑。

事实上，gitbook是基于命令行的工具，手工编辑文档并实时预览，而且很方便生成电子书。同时，它可以关联到github下面，如何不熟悉就本地应用就可以。

## 安装

我是在archlinux下使用的，先安装 node.js 和 npm：

    $ sudo pacman -S nodejs
    $ sudo pacman -S npm


下面一步，如果按照网上的文档安装gitbook，会报错：

```
    You need to install 'gitbook-cli' to have access to the gitbook command anywhere on your system.
If you've installed this package globally, you need to uninstall it.
>> Run 'npm uninstall -g gitbook' then 'npm install -g gitbook-cli'
```

需要安装 gitbook-cli：

    $ sudo npm install -g gitbook-cli

## 运行

在运行前，先在书籍的目录下建立两个文档：README.md 和 SUMMARY.md。分别对应首页和目录，其中 SUMMARY.md 格式如下：

```
* [第1章](c1.md)
 * [第1节](c1s1.md)
 * [第2节](c1s2.md)
* [第2章](c2.md)
```

电子书的目录手动编辑就可以。执行以下命令就可以本地预览：

    $ gitbook serve -p
    
默认地址在： 

    http://localhost:4000/
    

## 发布

执行预览后，本地目录会有一个 `_books` 目录，就是生成的html格式，可以直接放到网站。电子书目录可以托管到github。也可以使用命令导出为电子书格式，`-o` 命令制定电子书文件名：

* gitbook epub
* gitbook mobi
* gitbook pdf

以上三种方式都可以直接生成电子书，效果可以接受。如果进一步优化电子书，可以就需要 Sigil 或者 Calibre 等工具。

### 电子书封面

把封面图片放到书籍目录下，命名为 cover.jpg ，推荐大小是 1800x2360。小封面命名为 cover_small.jpg，大小 200x262 。另外有一个自动生成封面的插件  autocover ：https://github.com/GitbookIO/plugin-autocover

更多的插件： https://github.com/GitbookIO/plugin

### 配置

配置存在 book.json 文件里，比如可以修改电子书名字：

    { "title": "My Awesome Book" }
    
可以使用这个网址检测文件的错误： http://jsonlint.com/


这样就可以生成简单的电子书了，我打算把之前整理的一些文章打包成一本书。


20160301update：开始写自己的电子书：[《简化生活》](https://www.gitbook.com/book/metaldudu/simple-life/details)

---

参考：

* [官方帮助](http://help.gitbook.com/)
* [使用Gitbook制作电子书](http://www.ituring.com.cn/article/127645)
* [使用GitBook平台发布电子书](http://www.ituring.com.cn/article/127744)

`20150907`
