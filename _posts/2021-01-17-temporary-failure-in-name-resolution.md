---
layout: post
title: "下载错误Temporary failure in name resolution"
category: 
tags: [tech]
---

在用 annie 下载b站视频时，报错显示

> dial tcp: lookup upos-sz-mirrorcos.bilivideo.com: Temporary failure in name resolution

这个错误有段时间了，我一直以为是 annie 的问题，去主页看了看也没有类似的错误。今天想到可能是 aria2 的错误，搜了一下这个错误关键词，原来是系统DNS被修改。查看 /etc/resolv.conf ，发现只有一行

`Nameserver 192.168.2.1`

看了网上这个错误也会影响 wget ，而这个文件会被覆盖，所以修改成可用的DNS之后，要加上写保护。

`# chattr +i /etc/resolv.conf`


参考：

- https://wiki.archlinux.org/index.php/Domain_name_resolution
-[Annie downloader](https://github.com/iawia002/annie)
