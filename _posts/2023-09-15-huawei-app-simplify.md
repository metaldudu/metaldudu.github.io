---
layout: post
title: "华为鸿蒙内置应用精简"
category: tech
tags: [手机]
---

华为 mate50 已经是鸿蒙系统，新机内置的一些应用可以卸载，比之前 emui 好一些（但好的有限）。对比发现应用市场、主题等应用臃肿了不少，而且不断推广告，甚至钱包刷地铁后弹出提示也带广告，实在不能不吐槽。一个为国争光的企业，一个代表未来的系统，充满了小米一样的广告（而小米广告看起来更合理，主打一个性价比）。这样的鸿蒙，怕是年年都要换手机才能承受啊。

按照之前 mate30 的程序用 adb 停用/卸载内置应用，鸿蒙版本 3.0.0.380，时间20230915，操作需谨慎，可以先停用一段时间再卸载。

另外照例找一些轻量开源的替代。

### 系统更新启用和关闭

adb shell pm disable-user com.huawei.android.hwouc 
adb shell pm enable com.huawei.android.hwouc

### 其他可选关闭

adb shell pm disable-user com.huawei.himovie.local 视频播放器
adb shell pm disable-user com.sohu.sohuvideo.emplayer HiMoviePlayerPlus
adb shell pm disable-user com.huawei.music.local 音乐播放器
adb shell pm disable-user com.huawei.search 智慧搜索
adb shell pm disable-user com.huawei.vassistant 智慧语音
adb shell pm disable-user com.huawei.hitouch 
adb shell pm disable-user com.huawei.ohos.suggestion 
adb shell pm disable-user com.huawei.intelligent 智慧助手·今天
adb shell pm disable-user com.huawei.ohos.famanager 服务中心
adb shell pm disable-user com.huawei.appmarket 应用市场
adb shell pm disable-user com.huawei.fastapp 快应用
adb shell pm disable-user com.huawei.browser 浏览器
adb shell pm disable-user com.huawei.hwdetectrepair 智能监测基础服务
adb shell pm disable-user com.huawei.searchservice 
adb shell pm disable-user com.huawei.tips 智能提醒
adb shell pm disable-user com.huawei.gameassistant 游戏空间
adb shell pm disable-user com.huawei.meetime 
adb shell pm disable-user com.huawei.magazine 杂志锁屏
adb shell pm disable-user com.huawei.hicar 华为汽车
adb shell pm disable-user com.huawei.parentcontrol 健康使用手机（家长模式）
adb shell pm disable-user com.huawei.printservice 华为打印
adb shell pm disable-user com.huawei.notepad 备忘录
adb shell pm disable-user com.huawei.ohos.suggestion 小艺建议
adb shell pm disable-user com.huawei.ohos.inputmethod 小艺输入法
adb shell pm disable-user com.huawei.phoneservice 我的华为
adb shell pm disable-user com.huawei.compass 
adb shell pm disable-user com.huawei.hmos.compass 指南针
adb shell pm disable-user com.huawei.livewallpaper.paradise 动态壁纸1
adb shell pm disable-user com.huawei.scenepack 旅行助手
adb shell pm disable-user com.huawei.ohos.mirror 镜子
adb shell pm disable-user com.huawei.mirror 镜子
adb shell pm disable-user com.huawei.hwread.dz.local 文档阅读器
adb shell pm disable-user com.huawei.filemanager.fa 文件管理卡片
adb shell pm disable-user com.huawei.skytone 天际通
adb shell pm disable-user com.huawei.hwvoipservice 畅连服务
adb shell pm disable-user com.huawei.email 邮箱
adb shell pm disable-user com.huawei.onekeylock.hmservice 一键锁屏
adb shell pm disable-user com.huawei.scanner 智慧视觉

### 替代方案

- 应用市场 F-droid / AuroraStore
- 输入法 谷歌拼音 / Gboard
- 视频播放 VLC
- 音频播放 Musicolet
- 文件管理 CX文件管理器
- 浏览器 Firefox  / via
- 阅读 KOReader
- 图库 Aves
