---
layout: post
title: "制作mobi格式漫画书"
category: tech
tags: [漫画]
---

## 格式

- cbr、cbz：传统的漫画格式，即rar、zip格式压缩包，很多漫画软件支持。
- mobi：用kindle看只能选这个。
- webp：谷歌的无损图片格式，压缩比高，不少网站选用（比如豆瓣）。

## 图片来源

一个浏览器脚本：[Xianzun manhuagui & omanhua Downloader](https://greasyfork.org/zh-TW/scripts/28410)，可以连续下载所有漫画图片，我测试了“漫画柜”，偶尔会卡死，但基本可用。

我试了试，不能抓到这个网站的图片地址，应该是加密的js。

## 格式转换

安装 libwebp 和 imagemagick。

webp到png： `dwebp 1.webp -o 1.png`

png到jpg，压缩大小： `convert -scale 80% -quality 80% 1.png 1.jpg`

打包成cbz： `zip -r 1.cbz folder/`

通过calibre的 ebook-convert 可用直接转换成mobi，但没找到指定封面的方法，不指定会随机选择一张图片做封面。

`ebook-convert 1.cbz 1.mobi --no-inline-toc`

所以用calibre手工导入cbz，维护元数据、封面，然后转换，注意选择不要添加目录。
