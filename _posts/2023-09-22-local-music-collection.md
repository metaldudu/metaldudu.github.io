---
layout: post
title: "本地音乐收集整理"
category: tech
tags: [音乐]
---

移动互联网越发展，弊端暴露的越多，总有一小撮人会反技术流行，比如回归到把音乐文件放到本地播放。虽然不能达到丰富，但至少对自己胃口，也会少一些限制。

这两天把 `~/Music` 目录整理了一下，记录一下：

- 目录：简单分一下：albums/songs/OST/others
- 格式：所有格式转为 flac/mp3 ，使用 Kid3 修改ID3信息
- 封面：单曲的封面嵌入文件，专辑直接用 cover.jpg

音乐的来源如果没有无损，就直接视频网站或在线音乐网站抓，低音质凑合。通常油管非常丰富，本地播放只是为了方便。

工具方面，用 ffmpeg 转码异常方便。之前选播放器，一直用 [Audacious](https://audacious-media-player.org/)，主打一个简洁方便，但在专辑管理方面差很多。这次找到 [AQuod Libet](https://quodlibet.readthedocs.io/en/latest/) ，本身定位于音乐库，有多种视图可选，非常方便以听专辑。看很多推荐 windows 平台的 musicbee ，在 linux 下有几个工具够用就好。

维护好 ID3 信息有点麻烦，但一劳永逸，类似电子书的元信息。本地数据有 30G 左右，稍微注意备份一下，丢了也不担心。