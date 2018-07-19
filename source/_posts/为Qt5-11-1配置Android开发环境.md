---
title: 为Qt5.11.1配置Android开发环境
date: 2018-07-18 21:27:06
tags:
	- Qt5
	- Android
---

### 安装`JDK`：

[下载JDK](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html?utm_source=androiddevtools&utm_medium=website)

通过`tar zxvf jdk-8u181-linux-x64.tar.gz`命令解压。

在`shell`终端配置文件`.bashrc`中设置环境变量：

<!-- more -->

```bash
export JAVA_HOME=/home/liuqiang/Android/jdk1.8.0_181 #这是我的环境配置路径
export JRE_HOME=$JAVA_HOME/jre
export CLASSPATH=.:$CLASSPATH:$JAVA_HOME/lib:$JRE_HOME/lib
export PATH=$PATH:$JAVA_HOME/bin:$JRE_HOME/bin
```

测试是否安装完成：

```bash
java -version
java
javac
```

输出无误即可。

### 安装`Gradle Build Tool`：

[Gradle安装教程](https://gradle.org/install/)

### 安装`Android NDK`：

手动下载安装包解压即可。解压的路径：在`~/Android`目录下解压，`Android SDK Tools`中的各种工具也是安装在这个目录下，甚至`JDK`也可以直接解压在这个目录下，方便统一管理。

[NDK各版本下载](https://blog.csdn.net/gyh198/article/details/75036686) | [官网NDK各版本下载](https://developer.android.google.cn/ndk/downloads/older_releases) 

### 安装`Android SDK Tools`：

首先我们需要手动下载`sdk-tools-linux-3859397.zip`这个文件，原因是我不想安装`android studio`这个庞然大物，毕竟我是要在`QtCreator`中进行开发，并非真的要在`android`IDE中开发，我只是需要`sdkmanager`这个命令工具帮助我下载、安装和卸载等管理在应用开发过程中用到的各种`SDK Packages`，[Android开发者官网](https://developer.android.com/studio/)上可以下载到`Command line tools only`。关于这个工具，官网的解释是这样的：If you do not need Android Studio, you can download the basic Android   command line tools below. You can use the included [`sdkmanager`](https://developer.android.com/studio/command-line/sdkmanager)   to download other SDK packages. These tools are included in Android Studio. 当前官网最新版本是：`sdk-tools-linux-4333796.zip`，网速不好的话，可以用去网上搜索下载旧一点的版本，然后用`sdkmanager`命令行工具进行更新即可。

[sdkmanager用法简介](https://developer.android.google.cn/studio/command-line/sdkmanager) 。

```bash
cd /home/liuqiang/Android/tools/bin #sdk-tools-linux-4333796.zip解压后的目录为tools
./sdkmanager --list #输出所有可用的SDK Packages
./sdkmanager "platforms;android-24" #这里安装了3个版本的Android平台
./sdkmanager "platforms;android-26"
./sdkmanager "platforms;android-28"
./sdkmanager "build-tools;28.0.0"
./sdkmanager "platform-tools"
./sdkmanager "emulator"
./sdkmanager "patcher;v4"
./sdkmanager "ndk-bundle" #这个就是Android NDK，体积很大，网速不好的话，建议转为离线安装
```

`./sdkmanager --list`输出的结果如下：

```bash
liuqiang@LiuQiang-Ubuntu16:~/Android/tools/bin$ ./sdkmanager --list
Installed packages:=====================] 100% Computing updates...             
  Path                 | Version | Description                | Location             
  -------              | ------- | -------                    | -------              
  build-tools;28.0.0   | 28.0.0  | Android SDK Build-Tools 28 | build-tools/28.0.0/  
  emulator             | 27.3.9  | Android Emulator           | emulator/            
  patcher;v4           | 1       | SDK Patch Applier v4       | patcher/v4/          
  platform-tools       | 28.0.0  | Android SDK Platform-Tools | platform-tools/      
  platforms;android-24 | 2       | Android SDK Platform 24    | platforms/android-24/
  platforms;android-26 | 2       | Android SDK Platform 26    | platforms/android-26/
  platforms;android-28 | 4       | Android SDK Platform 28    | platforms/android-28/
  tools                | 26.1.1  | Android SDK Tools          | tools/               

Available Packages:
  Path                                                                                     | Version      | Description                                                         
  -------                                                                                  | -------      | -------                                                             
  add-ons;addon-google_apis-google-15                                                      | 3            | Google APIs                                                         
  add-ons;addon-google_apis-google-16                                                      | 4            | Google APIs                                                         
  add-ons;addon-google_apis-google-17                                                      | 4            | Google APIs                                                         
  add-ons;addon-google_apis-google-18                                                      | 4            | Google APIs                                                         
  add-ons;addon-google_apis-google-19                                                      | 20           | Google APIs                                                         
  add-ons;addon-google_apis-google-21                                                      | 1            | Google APIs                                                         
  add-ons;addon-google_apis-google-22                                                      | 1            | Google APIs                                                         
  add-ons;addon-google_apis-google-23                                                      | 1            | Google APIs                                                         
  add-ons;addon-google_apis-google-24                                                      | 1            | Google APIs                                                         
  add-ons;addon-google_gdk-google-19                                                       | 11           | Glass Development Kit Preview                                       
  build-tools;19.1.0                                                                       | 19.1.0       | Android SDK Build-Tools 19.1                                        
  build-tools;20.0.0                                                                       | 20.0.0       | Android SDK Build-Tools 20                                          
  build-tools;21.1.2                                                                       | 21.1.2       | Android SDK Build-Tools 21.1.2                                      
  build-tools;22.0.1                                                                       | 22.0.1       | Android SDK Build-Tools 22.0.1                                      
  build-tools;23.0.1                                                                       | 23.0.1       | Android SDK Build-Tools 23.0.1                                      
  build-tools;23.0.2                                                                       | 23.0.2       | Android SDK Build-Tools 23.0.2                                      
  build-tools;23.0.3                                                                       | 23.0.3       | Android SDK Build-Tools 23.0.3                                      
  build-tools;24.0.0                                                                       | 24.0.0       | Android SDK Build-Tools 24                                          
  build-tools;24.0.1                                                                       | 24.0.1       | Android SDK Build-Tools 24.0.1                                      
  build-tools;24.0.2                                                                       | 24.0.2       | Android SDK Build-Tools 24.0.2                                      
  build-tools;24.0.3                                                                       | 24.0.3       | Android SDK Build-Tools 24.0.3                                      
  build-tools;25.0.0                                                                       | 25.0.0       | Android SDK Build-Tools 25                                          
  build-tools;25.0.1                                                                       | 25.0.1       | Android SDK Build-Tools 25.0.1                                      
  build-tools;25.0.2                                                                       | 25.0.2       | Android SDK Build-Tools 25.0.2                                      
  build-tools;25.0.3                                                                       | 25.0.3       | Android SDK Build-Tools 25.0.3                                      
  build-tools;26.0.0                                                                       | 26.0.0       | Android SDK Build-Tools 26                                          
  build-tools;26.0.1                                                                       | 26.0.1       | Android SDK Build-Tools 26.0.1                                      
  build-tools;26.0.2                                                                       | 26.0.2       | Android SDK Build-Tools 26.0.2                                      
  build-tools;26.0.3                                                                       | 26.0.3       | Android SDK Build-Tools 26.0.3                                      
  build-tools;27.0.0                                                                       | 27.0.0       | Android SDK Build-Tools 27                                          
  build-tools;27.0.1                                                                       | 27.0.1       | Android SDK Build-Tools 27.0.1                                      
  build-tools;27.0.2                                                                       | 27.0.2       | Android SDK Build-Tools 27.0.2                                      
  build-tools;27.0.3                                                                       | 27.0.3       | Android SDK Build-Tools 27.0.3                                      
  build-tools;28.0.0                                                                       | 28.0.0       | Android SDK Build-Tools 28                                          
  build-tools;28.0.0-rc1                                                                   | 28.0.0 rc1   | Android SDK Build-Tools 28-rc1                                      
  build-tools;28.0.0-rc2                                                                   | 28.0.0 rc2   | Android SDK Build-Tools 28-rc2                                      
  build-tools;28.0.1                                                                       | 28.0.1       | Android SDK Build-Tools 28.0.1                                      
  cmake;3.6.4111459                                                                        | 3.6.4111459  | CMake 3.6.4111459                                                   
  docs                                                                                     | 1            | Documentation for Android SDK                                       
  emulator                                                                                 | 27.3.9       | Android Emulator                                                    
...                                                                                       ...                                                              
  ndk-bundle                                                                               | 17.1.4828580 | NDK                                                                 
  patcher;v4                                                                               | 1            | SDK Patch Applier v4                                                
  platform-tools                                                                           | 28.0.0       | Android SDK Platform-Tools                                          
  platforms;android-10                                                                     | 2            | Android SDK Platform 10                                             
  platforms;android-11                                                                     | 2            | Android SDK Platform 11                                             
  platforms;android-12                                                                     | 3            | Android SDK Platform 12                                             
  platforms;android-13                                                                     | 1            | Android SDK Platform 13                                             
  platforms;android-14                                                                     | 4            | Android SDK Platform 14                                             
  platforms;android-15                                                                     | 5            | Android SDK Platform 15                                             
  platforms;android-16                                                                     | 5            | Android SDK Platform 16                                             
  platforms;android-17                                                                     | 3            | Android SDK Platform 17                                             
  platforms;android-18                                                                     | 3            | Android SDK Platform 18                                             
  platforms;android-19                                                                     | 4            | Android SDK Platform 19                                             
  platforms;android-20                                                                     | 2            | Android SDK Platform 20                                             
  platforms;android-21                                                                     | 2            | Android SDK Platform 21                                             
  platforms;android-22                                                                     | 2            | Android SDK Platform 22                                             
  platforms;android-23                                                                     | 3            | Android SDK Platform 23                                             
  platforms;android-24                                                                     | 2            | Android SDK Platform 24                                             
  platforms;android-25                                                                     | 3            | Android SDK Platform 25                                             
  platforms;android-26                                                                     | 2            | Android SDK Platform 26                                             
  platforms;android-27                                                                     | 3            | Android SDK Platform 27                                             
  platforms;android-28                                                                     | 4            | Android SDK Platform 28                                             
  platforms;android-7                                                                      | 3            | Android SDK Platform 7                                              
  platforms;android-8                                                                      | 3            | Android SDK Platform 8                                              
  platforms;android-9                                                                      | 2            | Android SDK Platform 9                                              
  sources;android-15                                                                       | 2            | Sources for Android 15                                              
  sources;android-16                                                                       | 2            | Sources for Android 16                                              
  sources;android-17                                                                       | 1            | Sources for Android 17                                              
...
...
  tools                                                                                    | 26.1.1       | Android SDK Tools                                                   
```

我这里将所需的工具包都进行了安装和更新，所以没有更新提示功能，如果你安装了某些不是最新版本的工具，会有更新提示。

### 配置`Android`开发环境

打开`QtCreator`，选择：`工具`》`选项`》`设备`》`Android`，单击`浏览`按钮添加`JDK location`，单击`浏览`按钮设置`Android SDK 的路径`和`Android NDK的路径`，其实`QtCreator`中已经集成了`SDK Manager`工具，我们可以`安装`，`更新`和`卸载` Android SDK中的工具，但是Android NDK工具体积较大，最好离线安装，手动下载解压。

### 将手机设置为USB调模式试

我的手机是`魅蓝Note6`，USB调试与其他的手机不一样，第一次使用USB调试的时候，需要先在：设置》关于手机》版本号，这里连击4-5次激活开发者模式，然后转到：设置》辅助功能》开发者选项，开启`USB调试`并在弹出窗口中选择`确定`，还可以选择关闭`通过USB验证应用`，因为至少我们知道自己的应用是没有毒的。

### 编译没有问题，部署应用出错

```bash
adb: failed to install /home/liuqiang/Qt5.11.1/Examples/Qt-5.11.1/widgets/widgets/build-analogclock-Android_for_armeabi_v7a_GCC_4_9_Qt_5_11_1_for_Android_armv7-Debug/android-build//build/outputs/apk/android-build-debug.apk: Failure [INSTALL_FAILED_USER_RESTRICTED]
Installing to device failed!
```

原因很简单，因为手机设备有应用保护功能，未知应用会禁止自动安装，所以我们需要在手机中允许安装当前应用即可。

`参考文献：` [Connecting Android Devices](https://doc.qt.io/qtcreator/creator-developing-android.html) | [sdkmanager](https://developer.android.google.cn/studio/command-line/sdkmanager) |

- 本文作者：LiuQiang
- 版权声明：本文为作者的原创文章，转载时请务必注明出处！

