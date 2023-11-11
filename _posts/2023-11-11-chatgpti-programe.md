---
layout: post
title: "ChatGPT 辅助编程"
category: tech 
tags: [AI]
---

前一段试了 bing 的 AI 绘画，做了一个自制电子书的封面，效果满意。这两天偶然看到一篇帖子，说用 ChatGPT 辅助编程的，于是试了试。效果惊人！

第一个脚本写的是抓取 TMDB 网站某个电视剧剧集列表，ChatGPT 很清晰的给出基于 BeautifulSoup 的抓取脚本，对于上下文的错误也能理解我的意图。我最初的提问是：

> 请给出python代码，获取 https://www.themoviedb.org/tv/46923-shetland/seasons 这个网址下面， 类名为 "season_wrapper" 的部分中，"content"下面<h2>和<h4> 标签的内容

如果有多个类名，它会修改并循环处理。它能理解我指出某个错误，同时顾及其他部分，而且有变量命名规范，注释很清楚。

第二个脚本是修改之前写过的，在一张图片上显示一段文字。首先它引导我正确安装 python-pillow 这个包，并且在我运行出错后，提醒我试着重新安装这个包，解决了一个 ` ImportError: libimagequant.so.0: cannot open shared object file: No such file or directory` 错误，这个错误在彻底删除 python-pillow 再安装后解决。

之后 ChatGPT 犯了一个错误。我遇到报错 `AttributeError: 'ImageDraw' object has no attribute 'textsize'` ，它多次回复说：

> ImageDraw 对象确实没有 textsize 属性

但它给出的方法，都保留了这个属性。我只好自己搜索，发现这个属性已经改成 `textlength` 了，也就是说 ChatGPT 没有更新，也可能是我用的版本比较低（ChatGPT v2）。修改后程序就正常运行了。

而且你可以把写好的脚本贴给它看，它会分析你的改动，并且经常性的鼓励你，这一点比很多老师都可爱太多。

相比我自己靠 google 写脚本，使用 ChatGPT 可太方便了。另外对比了一下下 Bard ，感觉基本在一个水平上。


