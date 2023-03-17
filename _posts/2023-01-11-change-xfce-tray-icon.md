---
layout: post
title: "修改xfce任务栏图标"
category: tech
tags: [linux]
---

换成暗色主题，有些程序的任务栏图标很不协调，大小不一或者颜色鲜艳，手动替换可以解决。

## 替换 GoldenDict 图标

首先系统图标的位置在 `/usr/share/icons` ，以常用的 Papirus 图标为例，包含 Papirus/Papirus-Light/ePapirus 三套图标，分别对应文件夹。查询图标位置：

`find . -type f -iname '*goldendict*'`

结果：

```
./Papirus-Light/16x16/panel/goldendict-tray.svg
./Papirus-Light/16x16/panel/goldendict-scan-tray.svg
./Papirus-Light/22x22/panel/goldendict-tray.svg
./Papirus-Light/22x22/panel/goldendict-scan-tray.svg
./Papirus-Light/24x24/panel/goldendict-tray.svg
./Papirus-Light/24x24/panel/goldendict-scan-tray.svg
./Papirus/16x16/panel/goldendict-tray.svg
./Papirus/16x16/panel/goldendict-scan-tray.svg
./Papirus/22x22/panel/goldendict-tray.svg
./Papirus/22x22/panel/goldendict-scan-tray.svg
./Papirus/24x24/panel/goldendict-tray.svg
./Papirus/24x24/panel/goldendict-scan-tray.svg
./ePapirus/24x24/panel/goldendict-tray.svg
./ePapirus/24x24/panel/goldendict-scan-tray.svg
```


在把任务栏设置为 32px 高、系统主题选择 Papirus/Papirus-Dark 时，经过查找发现 GoldenDict 在任务栏调用的文件是：

 `/usr/share/icons/Papirus/22x22/panel/goldendict-tary.svg`

GoldenDict 的图标有些偏小，可以用同一目录下 `gitify-tray.svg` 来替换，效果好一些。

使用命令重建图标缓存：

`sudo gtk-update-icon-cache -f /usr/share/icons/*`

## Audacious

经过查找发现，对应 HiContracst 主题的任务栏图标文件是：

`/usr/share/icons/hicolor/scalable/apps/aucadious.svg`

对应 Papirus/Papirus-Dark 主题的替换命令

`sudo cp /usr/share/icons/Papirus/22x22/panel/audacious-panel.svg /usr/share/icons/Papirus/22x22/apps/audacious.svg` 

## flameshot

替换命令

`sudo cp /usr/share/icons/Papirus/22x22/panel/flameshot-tray.svg /usr/share/icons/Papirus/22x22/apps/flameshot.svg`

## Calibre

Calibre 在任务栏对应的图标是 `/usr/share/calibre/images/lt.png` ，256x256大小，替换一个就可以，比如用 Papirus 主题里的 `/usr/share/icons/Papirus/24x24/panel/calibre-tray.svg`  使用 inkscape 转换：

`cd /usr/share/calibre/images/`

`sudo cp /usr/share/icons/Papirus/24x24/panel/calibre-tray.svg ./`

`inkscape -w 256 -h 256 calibre-tray.svg --export-filename lt.png`

可能每次 Calibre 更新后，该文件会被覆盖。

PS. 用 Uluancher 调用 Calibre 时，显示的图标是：

`/usr/share/icons/hicolor/48x48/apps/calibre-gui.png`

## 修改 Fcitx5 图标

rime 输入法对应图标：

`/usr/share/icons/Papirus-Dark/22x22/actions/fcitx-rime.svg`

菜单中 Keyboad-English (US) 对应图标：

`/usr/share/icons/Papirus-Dark/16x16/devices/input-keyboard.svg`

Notification Plugin 里的 Keyboad-English (US) 图标，~~没有找到在哪儿~~ 因为从 16 放大到 22 ，所以图标发虚，暂时未找到解决方法。

## show desktop 按钮

对应 `/usr/share/icons/Papirus/16x16/apps/cs-desktop.svg` 替换命令：

`sudo cp /usr/share/icons/Papirus/16x16/panel/disper-panel.svg /usr/share/icons/Papirus/16x16/apps/cs-desktop.svg`

## 预览图标

右键点击面板 Applications Menu ，选择替换图标，可以预览系统主题的图标，支持查找。

### 参考

- [linux mint - How can I change an icon in my system tray? - Unix & Linux Stack Exchange](https://unix.stackexchange.com/questions/635739/how-can-i-change-an-icon-in-my-system-tray)
- [xfce:xfce4-settings:4.10:appearance [Xfce Docs]](https://docs.xfce.org/xfce/xfce4-settings/4.10/appearance)