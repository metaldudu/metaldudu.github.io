---
layout: post
title: "使用Jekyll-Bootstrap搭建blog"
description: ""
category: geek
tags: [jekyll]
---

注意：本文是我搭建此blog的记录，会定期修改。

#### 缘起
经过一段时间在豆瓣和微信公众平台的书写，我决定找一个相对安静的书写平台，经过寻找，决定使用Github的服务，基于[Jekyll-Bootstrap](http://jekyllbootstrap.com/) 。

#### 基本需求和现实

* 稳定的服务：Github服务器，二级域名，未来可以绑定其他域名
* 基于文本的书写：Markdown格式
* 快速上手 ：熟悉ruby、git、Markdown，需要花费一定时间，但投入产出比很高
* 安全性：文本易于备份
* 评论和分享：目前使用[Disqus](http://disqus.com/)的评论服务

#### 主要过程

1. 注册Github用户，安装Git。
2. 按照[Jekyll-Bootstrap](http://jekyllbootstrap.com/) 网站的步骤，3分钟搞定框架。
3. 本地安装Jekyll，可以方便的测试修改，非必须

	* 安装ruby环境rubyinstaller 和开发组件DevKit，下载： [rubyinstaller.org](http://rubyinstaller.org/downloads/)
	* 安装jekyll时，1.4.2和ruby2.0.0可以正常配合，1.4.3不行 [jekyll安装与应用](http://www.cnblogs.com/BeginMan/p/3549241.html)
	* 编码问题：
		* 需要在本地_config.yml中添加一行： encoding: utf-8
		* [修改convertible.rb这个方法](http://andriylin.github.io/tech/2013/07/14/Jekyll-Invalid-GBK/)，我实验失败
		* 所有文档都保存为utf8

#### 相关工具

* [Prose](http://prose.io/)：一个在线编辑github文档的工具
* [Markdown语法（简体中文版）](https://gitcafe.com/riku/Markdown-Syntax-CN/)

#### blog操作

* `rake page`

#### 参考文档

* [git添加SSHkeys](http://blog.csdn.net/keyboardota/article/details/7603630)
* [阮一峰：github Pages和Jekyll入门](http://www.ruanyifeng.com/blog/2012/08/blogging_with_jekyll.html)
* [写作环境搭建(git+github+markdown+jekyll)](http://site.douban.com/196781/widget/notes/12161495/note/264946576/)
* [使用github+jekyll搭建blog环境，完美替代wordpress](http://www.heiniuhaha.com/lessons/2012/08/09/use-jekyll-build-blog/)


---

### 20141121更新

+ 从[github.com/mojombo](http://github.com/mojombo)folk了新的blog，学习GIT。
+ 按照Disqus的[代码](http://docs.disqus.com/developers/universal/)，修改post.html，加入评论系统。
+ 重新按照教程：[http://blog.jsfor.com/skill/2013/09/07/jekyll-local-structures-notes/](http://blog.jsfor.com/skill/2013/09/07/jekyll-local-structures-notes/) 搭建本地环境。

#### 发布

    git pull origin master //先同步远程文件，后面的参数会自动连接你远程的文件
    git status //查看本地自己修改了多少文件
    git add -A //添加
    git commit * -m "write some mark"
    git push origin master //更新到远程服务器上

---

## 20141203更新

+ 安装git的windows客户端:http://msysgit.github.io/
+ 把git/bin 目录添加到系统变量path下

### 安装jekyll

+ 在[rubyinstaller](http://rubyinstaller.org/downloads/)网站下载对应版本的ruby和devkit。
+ 先安装ruby，解压缩devkit包到c:/devkit
+ 运行以下
	cd C:\DevKit

	ruby dk.rb init（这一步后需要修改devkit下的config.yml，设置自己的ruby目录）

	ruby dk.rb install
+ 正常安装后，就可以安装jekyll了。
	 gem install jekyll
+ 如果提示SSL错误，说明rubygems.org的镜像因为被墙，可以替换成taobao的源
	$ gem sources --remove https://rubygems.org/
	$ gem sources -a https://ruby.taobao.org/
+ 使用`jekyll --version`测试是否成功
+ 安装rdiscount解析markdown
	gem install rdiscount
+ 运行Jekyll服务：
	jekyll serve
+ 本地调试成功，就可以同步到github。

---

### 20150219更新

更换到Ubuntu下，搭建环境非常容易，参考文档：

+ http://michaelchelen.net/81fa/install-jekyll-2-ubuntu-14-04/

仍需要注意替换ruby.taobao.org，以及安装nodejs。

---

### 20160305更新

jekyll升级到3，ruby需要2以上，需要安装rvm指定ruby版本。其他看jekyll官方文档即可。参考官方升级文档：

* https://jekyllrb.com/docs/upgrading/2-to-3/


### TOC支持

文章开头添加：


* 目录
{:toc}





