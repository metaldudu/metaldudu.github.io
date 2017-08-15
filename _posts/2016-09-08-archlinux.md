---
layout: post
title: "Archlinux笔记"
description: ""
category: geek
tags: [archlinux]
---

* 目录
{:toc}

# Archlinux笔记

> 修订 20160908

## 安装

参考WIKI：

* [Installation guide](https://wiki.archlinux.org/index.php/Installation_guide)
* [beginner's guide](https://wiki.archlinux.org/index.php/Beginners_guide)

### iso制作

U盘写入工具：[YUMI – Multiboot USB Creator](http://www.pendrivelinux.com/yumi-multiboot-usb-creator/)

### 引导安装

U盘引导，选择linux，出现提示符

### 建立网络连接

确定无线网络接口名，可能是wlp2s0

	$iw dev

执行 wifi-menu

	$wifi-menu wlp2s0

按照提示选择无线网络，填写密码，无错误提示就联网成功。

### 分区

* 对应选择mbr或者gpd格式的硬盘，新电脑可以用gpd。
* 擦除分区表

  sgdisk -Z /dev/sda

* 用 fdisk 建立 MBR 分区

	# fdisk /dev/sda

按照wiki分区。使用mkfs命令格式化分区

	# mkfs.ext4 /dev/sda1
	# mkfs.ext4 /dev/sda2

#### 挂载分区

显示当前分区布局：

	# lsblk -f

mount命令挂载：

	# mount /dev/sda1 /mnt
	# mkdir /mnt/home
	# mount /dev/sda2 /mnt/home

### 安装镜像

	# nano /etc/pacman.d/mirrorlist

保留清华，或者添加163的源。

    Server = http://mirrors.tuna.tsinghua.edu.cn/archlinux/arch
    Server = http://mirrors.163.com/archlinux/$repo/os/$arch

安装基本系统

	# pacstrap -i /mnt base base-devel

默认选择全部包，等待下载安装。

#### 生成 fstab

	# genfstab -U -p /mnt >> /mnt/etc/fstab

运行一次即可，然后可以查看：

	# nano /mnt/etc/fstab

修改根目录（此步骤的意思应该是从livecd模式切换成硬盘上的系统）

	# arch-chroot /mnt /bin/bash

### 基本配置

#### 修改时区编码

	# nano /etc/locale.gen

只保留以下：

	en_US.UTF-8 UTF-8
	zh_CN.UTF-8 UTF-8
	zh_TW.UTF-8 UTF-8

运行locale-gen命令，重建编码表。

	# locale-gen

enabel chinese

	# echo LANG=en_US.UTF-8 > /etc/locale.conf

#### 修改时区

    # ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

#### 修改时间模式

	# hwclock --systohc --utc

#### 设置电脑名

	# echo myhostname > /etc/hostname

#### 安装网络有关的包

	#pacman -S dialog
	#pacman -S wpa_supplicant
	#pacman -S netctl
	#pacman -S wireless_tools

#### 设置密码

	# passwd

### 安装并配置 bootloader

#### 安装GRUB

安装grub并执行安装到MBR

	# pacman -S grub
	# grub-install --target=i386-pc --recheck /dev/sda

生成配置文件

	# grub-mkconfig -o /boot/grub/grub.cfg

离开 chroot 环境：

	# exit

重启：

	# reboot

###无线网络配置

在beginner's guide 里推荐reboot之前就安装配置wifi，但我跳过这段，所以重新配置。

参考 [Wireless network configuration (简体中文)](https://wiki.archlinux.org/index.php/Wireless_network_configuration_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))

先查看设备

	# ip link

如果显示类似wlp2s0这样无线设备，证明设备正常，启用设备：

	# ip link set wlp2s0 up

之前安装步骤里安装了 dialog, wifi-menu ，所以可以执行：

	# wifi-menu wlp2s0

这时会自动生成一份配置文件，在/etc/netctl，不需编辑，查看一下然后自动启用它，my_network是该配置文件名：

	# netctl enable my_network

正常应该可以上网了，但是又失败。查看问题：

	# netctl status my_network

提示Loaded，但Active failed。把自动生成的带有“-”的profile重命名，然后重启一次就联网成功了。这部分可以查看 `etctl--h` 帮助。

## 安装X


### 安装Xorg

* 选择xinit和xfce
* 安装intel显卡
* 安装xorg和xfce

    $ pacman -S xorg-server xorg-xinit xorg-server-utils
    $ pacman -S xfce4 xfce4-goodies

尝试配置xinit，先拷贝配置文件

	$ cp /etc/skel/.xinitrc ~/

编辑它，只保留xfce一行，并且放在文件最后.运行startx就可以到xfce桌面！

#### 账户设置

因为一直用root登录，所以xfce里mousepad会提示root不安全，按照wiki的步骤增加账户：

先安装zsh：

	# pacman -S zsh

创建一个用户laodu，并使用zsh作默认shell（用bash也可以）

	# useradd -m -g users -G audio,video,floppy,network,rfkill,scanner,storage,optical,power,wheel,uucp -s /usr/bin/zsh laodu

创建密码：

	# passwd archie

注销xfce，切换到新用户，startx。

解决方法：安装sudo

	# pacman -S sudo

编辑sudo配置文件，只能用vi

	#visudo

取消wheel权限的注释，当用户使用sudo命令时，就可以以root身份执行命令了。

同样给新用户配置.xinitrc

    #cd ~
    #cp /etc/skel/.xinitrc ~
    #vi ~/.xinitrc

在最后一行取消xfce注释，然后startx启动。


## 硬件

* 安装触摸板 `pacman -S xf86-input-synaptics`
* 声卡，安装alsa `pacman -S alsa-utils`

解除静音，运行

	$ alsamixer

在顶部panel添加一个 audio mixer plugin，就是音量调节工具。

### 自动挂载U盘

安装gvfs，NTFS硬盘如果只读，需要安装ntfs-3g


### wicd管理无线网络

$ pacman -S wicd wicd-gtk notification-daemon

参考： https://wiki.archlinux.org/index.php/Wicd

    # systemctl enable wicd.service
    # gpasswd -a $USERNAME users
    # systemctl start wicd
    
## XFCE配置

### 安装中文字体

	#pacman -S wqy-microhei ttf-dejavu

### 输入法

选择使用iubs+rime（中州韵）输入法：

    $ pacman -S ibus ibus-qt ibus-rime

开始配置：

    $ ibus-setup

安装完毕，会出现提示：

>IBus has been started! If you cannot use IBus, please add below lines in $HOME/.bashrc, and relogin your desktop.
export GTK_IM_MODULE=ibus
export XMODIFIERS=@im=ibus
export QT_IM_MODULE=ibus

也就是把下面三行，添加到 $HOME/.bashrc，然后重启。在ibus设置中添加 input method -> chinese-rime

* rime配置简繁，用ctrl+~键，选择简体。更多设置，需要修改 ~/.config/ibus/rime/default.yaml
* 把脚本添加到系统启动，如下：

>
 #!/bin/bash
ibus-daemon -d
export XMODIFIERS="@im=ibus"
export GTK_IM_MODULE=ibus
export QT_IM_MODULE=xim
export ibus &

* 修改输入启动顺序，安装 dconf-edtior ，在desktop > ibus > general > engines-oder 修改顺序，使得默认输入法是英文。

### 快捷键设置

linux的 workspace 可以用 ctrl+F1/F2 切换，也可以用 ctrl+alt+方向键切换。

xfce桌面环境本身包含快捷键设置，位置在`Settings - Keyboard - Application Shortcuts`，按照自己的习惯，结合其他工具，可以极大提高效率。

* 常用软件的绑定：浏览器、终端、文本编辑器等等，比如可以绑定`Win+E` 到文件管理器，和 windows下一致。
* 截图：xfce自带截图工具，[官方帮助](http://docs.xfce.org/apps/screenshooter/usage)，我经常用截取区域，需要添加 `-r`。把命令 `xfce4-screenshooter -r` 加入快捷键即可。
* 快速启动软件，使用 dmenu ，直接绑定成 Win+space。dmenu的使用见下。
* exo-open --launch FileManager：super+e  #打开/home文件夹
* exo-open --launch TerminalEmulator：super+t  #终端

### dmenu

* 我通过[这个帖子](https://blog.henix.info/blog/dmenu-run/_.html)，修改了自己的脚本，绑定快捷键就可以启动了。


## 软件

### 安装yaourt

加Yaourt源至 /etc/pacman.conf:

	Server = http://repo.archlinuxcn.org/$arch
	Server = http://repo.archlinux.fr/$arch
	Server = http://repo-fr.archlinuxcn.org/$arch

执行

	pacman -Sy yaourt

提示三个包需要下载：packgage-query-1.14-1 yajl-2.1.0-1,yaourt-1.5-1，但第一个包总出现错误，原因：注意要加SigLevel = Optional TrustAll，这样就不会报PGP验证错误了。


### 常用软件

* 文本编辑：atom gvim mousepad retext
* 浏览器：chrome luakit
* 终端：xfce terminal
* 启动器：dmenu
* 系统信息：conky
* 电子书管理：Calibre
* 压缩：xarchiver
* PDF阅读：evince
* RSS阅读：liferea
* 网盘：nutstore
* 视频播放：smplayer
* 截图：xfce4-screenshooter
* 办公：WPS
* 下载：aria2

### CLI

* ydcv：有道查词
* [musicbox](https://github.com/darknessomi/musicbox)：网易云音乐播放




## 其他零散问题

### aria2

* web端：[http://ziahamza.github.io/webui-aria2/](http://ziahamza.github.io/webui-aria2/)
* 命令 `aria2c --enable-rpc --rpc-listen-all`
*  百度云配合插件：[121976](https://www.v2ex.com/t/121976)

### luakit
轻量级浏览器，安装后拷贝配置文件，字体调试：
[viewtopic.php?f=73&t=462549](http://forum.ubuntu.com.cn/viewtopic.php?f=73&t=462549)


### 压缩ISO文件

安装cdrkit，其中包含mkisofs命令，格式如下：

    #mkisofs -o xxx.iso /the/path


### 手动安装aur软件

下载之后，去/tmp/yaourt-tmp-yourname/soft文件夹下找到PKGBUILD和python2.patch两个文件，cp到和soft.tar.gz。终端cd到当前目录，然后执行：makepkg PKGBUILD。如无以外，当生成soft.pkg.tar.xz打包好的软件，最后sudo pacman -U soft.pkg.tar.zx，安装。


### U盘弹出需要root密码

修改 ` /usr/share/polkit-1/actions/org.freedesktop.udisks.policy ` 文件中， unmount by other use 的部分，把 `auth_admin_keep` 改成 `yes`

###  把 Whisker menu 加入快捷键

Settings Manager -> Keyboard -> Application Shortcuts -> Add -> xfce4-popup-whiskermenu

### 显示桌面

Settings Manager > Window Manager > Keyboard，绑定win+D

### 字体设置

配置文件在：~/.config/fontconfig/font.conf
安装WPS后，会修改默认sans字体，所以要重新配置。刷新字体缓存： fc-cache -vf，显示默认字体： fc-match

* `fc-list` 列出字体

### pacman

* 找到不依赖的包： `sudo pacman -Qtd`
* 卸载掉 `sudo pacman -Rs xxx`
* 列出xxx文件位置：`pacman -Ql xxx`

#### 桌面设置

* 安装 xfce4-whiskermenu-plugin ，菜单插件
* 拖动窗口到桌面一角或一边，可以平铺窗口

#### 文件管理器Thunar

* Thunar，支持多窗口操作
  * ctrl+S，支持模式选择文件
  * / 和 ~，可以定位到根目录和主目录
  * alt+左，返回上一目录

### conky

conky ：根据[bbs](https://bbs.archlinux.org/viewtopic.php?id=199217&p=3)
配置文件需要用/usr/share/doc/conky-1.10.0/convert.lua 转换，以符合新的格式：./convert.lua ~/.conkyrc

### 编码转换

* 显示文件编码：$file - i *
* vim转码：set fileencoding=utf-8
* enca支持批量转换：`enca -x utf-8 *`，指定语言参数`enca -L zh_CN -x utf-8`

### zip压缩

` zip -r myfile.zip ./* ` ：压缩当前目录文件和文件夹
` unzip -o -d /home/tmpfolder myfile.zip` ：解压，-o不提示覆盖

