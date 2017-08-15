---
layout: post
title: "使用SSH登录git"
description: ""
category: geek
tags: [git]
---

## 使用目的

git的两种登录模式：https和SSH，后者可以免去输入密码。

## 本地安装和创建公钥

Arch Linux 下，安装openssh：

` sudo pacman -S openssh`

使用 ssh-keygen 创建公钥

`#ssh-keygen -t rsa`

忽略提示（一次是要求添加passphrase，第二次是保存位置），会在用户目录下创建 .ssh 文件夹，内有公钥文件。有关passphrase，目前没有使用。

## 在GitHub里添加SSH key

打开GitHub或者其他git服务的设置页面，找到添加SSH key 的位置，把 `~/.ssh/id_rsa.pub` 文件内容复进去，保存。这时可以用命令测试，比如

`ssh -T git@github.com`

会提示，输入yes确认，会看到正确提示。

## 在git中修改登录模式

使用 `git remote -v` 可以显示当前连结情况，使用 `git remote set-url` 命令修改登录模式，例如：

`git remote set-url origin https://github.com/USERNAME/REPOSITORY.git`

---

参考：

* [GitHub help / SSH](https://help.github.com/categories/ssh/)

`20160927`
