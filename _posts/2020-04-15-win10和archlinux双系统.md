---
layout: post
title: "win10和archlinux双系统"
category: tech
tags: []
---

今天收到荣耀MagicBook，机器的版本是“Ryzen 5 3500U 16GB 512GB（冰河银）MagicBook 2019”，14寸屏幕，包含win10和office家庭版联网会自动激活，也包含华为定制的软件，包括和手机传输的 HONOR Magic-link，这些虽好对我用处不大。照例是安装 Arch linux，下面是一些记录。

### MagicBook的一些问题

F2进入BIOS，F12选择启动介质

### 按照官方指引安装

按照官方指引非常必要，我按照之前自己的笔记，结果出了一个错。在安装gurb之后重启，居然看不到linux本身的启动项，只有windows。原因排查了一下，是因为2019年11月，arch linux 的base 包已经不再包含linux内核，需要单独安装。

    # pacstrap /mnt base linux linux-firmware

之后使用 fstab 生成后就可以看到正确的启动列表。

### BIOS模式

之前我在两台笔记本上安装过，这次依然踩了几个坑。主板已经全面更新到UEFI模式，而之前我都是用LEGACY模式。双系统如果已经安装好win10，会创建好EFI分区，只需要注意挂载这个分区就可以了。

### 网络安装

base包没有网络管理工具，之前我用的 wicd ，这次直接选择了 networkmanager。官方指引只包含基本的安装，其实可以把用户设置、网络、桌面系统都安装好再重启。

如果错过安装了网络，可以再次用引导U盘启动，使用 wifi-menu 连接无线网络后，使用 archchroot 挂载已经安装的分区，补上需要的包即可。

### 声音

安装 alsa-utils 和  pulseaudio，前者可以使用 alsamixer 来调整声音设备音量，取消静音按m键；后者在任务栏显示声音图标。运行 `aplay- l` 可以看到当前音频设备：

    card 0: Generic [HD-Audio Generic], device 3: HDMI 0 [HDMI 0]
    Subdevices: 1/1
      Subdevice #0: subdevice #0
    card 0: Generic [HD-Audio Generic], device 7: HDMI 1 [HDMI 1]
      Subdevices: 1/1
      Subdevice #0: subdevice #0
    card 1: Generic_1 [HD-Audio Generic], device 0: ALC256 Analog [ALC256 Analog]
      Subdevices: 1/1
      Subdevice #0: subdevice #0

默认应该选择 card1 ，所以建立 `~/.asoundrc` ，内容如下：

    defaults.pcm.card 1
    defaults.pcm.device 0
    defaults.ctl.card 1
注销一下就可以了。

