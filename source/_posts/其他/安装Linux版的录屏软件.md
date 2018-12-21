---
title: 安装Linux版的录屏软件
date: 2018-07-18 10:07:58
components: true
reward: true
tags:
	- Linux
	- 录屏软件
---

### 简介

`recordmydesktop`是`Linux`平台非常好用的录屏软件，可以说是`Linux`平台的首选录屏软件，在各`Linux`发行版本中都可以使用。

<!-- more -->

- 查询一下recordmydesktop是否存在于软件源中：`sudo apt-cache search recordmydesktop` ，如果有的话，会输出如下的内容：
```bash
liuqiang@LiuQiang-Ubuntu16:~$ sudo apt-cache search recordmydesktop
[sudo] liuqiang 的密码： 
gtk-recordmydesktop - Graphical frontend for recordMyDesktop screencast tool
recordmydesktop - Captures audio-video data of a Linux desktop session

```
- 安装录屏和录音软件：`sudo apt-get install recordmydesktop gtk-recordmydesktop`
- 启动程序：按下`super`键，输入`recordmydesktop`查找我们刚才安装的录屏软件.
- 卸载程序：执行命令`sudo apt autoremove recordmydesktop  gtk-recordmydesktop `

