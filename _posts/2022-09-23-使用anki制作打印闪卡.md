---
layout: post
title: "使用anki制作打印闪卡"
category: tech
tags: [软件, 英语学习]
---

为了帮女儿背单词，我找到一份初中英语高频词列表，包含单词和释义，用电子表格乱序打印，效果不太好。后来把这个词库转换成[anki词库](https://github.com/metaldudu/anki-junior-school-hebei)，但又不想她多用手机，于是找到打印闪卡的方式。

首先要有合适的anki词库，我通过 [toPhonetics](https://tophonetics.com/zh/) 这个网站添加了对应的音标，数量比较少还行，数量更多就需要再想办法了。然后整合到词库里，正面是单词，反面是释义和音标，去掉了anki的播放音频。

然后使用插件 [Papercards - export & print flashcards to paper - AnkiWeb](https://ankiweb.net/shared/info/2042118948) ，代码是 2042118948 。选择牌组后，菜单选择：工具-Export to papercards，生成对应的 html 和 pdf 文件。注意这个插件依赖 wkhtmltopdf ，需要安装。

然后优化一下打印表现，插件默认字体很小。修改 html 文件头部的 css ，字体放大一点，边距适当缩小。然后用下面命令输出，参数是控制横向打印：

`wkhtmltopdf -O Landscape input.html output.pdf`

生成的 pdf 需要单双页双面打印，A4纸裁开成 4x4 的卡片即可。

顺便说一下这个高频词只有530个，显得有点少，不过高频词是基础，还是要多听多读，日常如果只看课本是不够的。