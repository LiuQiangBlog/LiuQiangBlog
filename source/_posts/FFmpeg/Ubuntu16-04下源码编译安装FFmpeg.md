---
title: Ubuntu16.04下源码编译安装FFmpeg
date: 2018-07-18 11:35:51
tags:
	- Ubuntu
	- FFmpeg
---

我的`Ubuntu16.04`系统配置的是清华镜像仓库。很多相关的软件已经有了，所以就不需要通过源码安装！

`创建目录：` 

在`Home` 目录下创建`ffmpeg`目录，并在其中创建3个子目录：`ffmpeg_sources`, `ffmpeg_build`, `bin`

<!-- more -->

```bash
cd ~
mkdir ffmpeg
cd ffmpeg
mkdir ffmpeg_sources
mkdir ffmpeg_build
mkdir bin
```

---

`安装依赖：`

```bash
sudo apt-get update -qq && sudo apt-get -y install \
  autoconf \
  automake \
  build-essential \
  cmake \
  git-core \
  libass-dev \
  libfreetype6-dev \
  libsdl2-dev \
  libtool \
  libva-dev \
  libvdpau-dev \
  libvorbis-dev \
  libxcb1-dev \
  libxcb-shm0-dev \
  libxcb-xfixes0-dev \
  pkg-config \
  texinfo \
  wget \
  zlib1g-dev
```

把这些依赖项安装完，并编译安装完`ffmpeg`之后，不想要这些第三方库了，可以卸载掉！

`安装NASM：` 某些库使用的汇编程序

```bash
cd ~/ffmpeg/ffmpeg_sources && \
wget https://www.nasm.us/pub/nasm/releasebuilds/2.13.03/nasm-2.13.03.tar.bz2 && \
tar xjvf nasm-2.13.03.tar.bz2 && \
cd nasm-2.13.03 && \
./autogen.sh && \
PATH="$HOME/ffmpeg/bin:$PATH" ./configure --prefix="$HOME/ffmpeg/ffmpeg_build" --bindir="$HOME/ffmpeg/bin" && \
make && \
make install
```

`安装Yasm：` 某些库使用的汇编程序

```bash
sudo apt-get install yasm
```

`安装libx264：` `H.264`视频编码器

```bash
sudo apt-get install libx264-dev
```

`安装libx265：` `H.265/HEVC`视频编码器

```bash
sudo apt-get install libx265-dev libnuma-dev
```

`安装libvpx：` `VP8/VP9`视频编码器/解码器

```bash
sudo apt-get install libvpx-dev
```

`安装libfdk-aac：` `AAC`音频编码器

```bash
sudo apt-get install libfdk-aac-dev
```

`安装libmp3lame：` `MP3`音频编码器

```bash
sudo apt-get install libmp3lame-dev
```

`安装libopus：` `Opus`音频编码器/解码器

```bash
sudo apt-get install libopus-dev
```

`安装libaom：` `AV1`视频编码器/解码器

```bash
cd ~/ffmpeg/ffmpeg_sources && \
git -C aom pull 2> /dev/null || git clone --depth 1 https://aomedia.googlesource.com/aom && \
mkdir aom_build && \
cd aom_build && \
PATH="$HOME/ffmpeg/bin:$PATH" cmake -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX="$HOME/ffmpeg/ffmpeg_build" -DENABLE_SHARED=off -DENABLE_NASM=on ../aom && \
PATH="$HOME/ffmpeg/bin:$PATH" make && \
make install
```

可能你发现了，无法下载Google仓库中的源码，那怎么办？不可能凉拌吧！

如果不想太麻烦的话，可以直接通过[我的个人网站](https://liuqiangblog.github.io)的联系方式联系我，我可以给你发一份。

最后，我们终于可以安装关键的`FFmpeg`了。

安装`ffmpeg：`

```bash
cd ~/ffmpeg/ffmpeg_sources && \
wget -O ffmpeg-snapshot.tar.bz2 https://ffmpeg.org/releases/ffmpeg-snapshot.tar.bz2 && \
tar xjvf ffmpeg-snapshot.tar.bz2 && \
cd ffmpeg && \
PATH="$HOME/ffmpeg/bin:$PATH" PKG_CONFIG_PATH="$HOME/ffmpeg/ffmpeg_build/lib/pkgconfig" ./configure \
  --prefix="$HOME/ffmpeg/ffmpeg_build" \
  --pkg-config-flags="--static" \
  --extra-cflags="-I$HOME/ffmpeg/ffmpeg_build/include" \
  --extra-ldflags="-L$HOME/ffmpeg/ffmpeg_build/lib" \
  --extra-libs="-lpthread -lm" \
  --bindir="$HOME/ffmpeg/bin" \
  --enable-gpl \
  --enable-libaom \
  --enable-libass \
  --enable-libfdk-aac \
  --enable-libfreetype \
  --enable-libmp3lame \
  --enable-libopus \
  --enable-libvorbis \
  --enable-libvpx \
  --enable-libx264 \
  --enable-libx265 \
  --enable-nonfree && \
PATH="$HOME/ffmpeg/bin:$PATH" make -j4 && \
make install && \
hash -r
```

`激活ffmpeg：`

```bash
source ~/.profile
gedit ~/.profile

# set PATH so it includes user's private bin directories
PATH="$HOME/ffmpeg/bin:$HOME/.local/bin:$PATH" # 此处将PATH原始路径为：PATH="$HOME/bin是不对的
# 注意：每次新打开一个shell终端窗口，都需要执行source ~/.profile，再执行ffmpeg
source ~/.profile
ffmpeg #测试ffmpeg是否安装成功

#如果不想这么麻烦，可以直接在~/.bashrc文件的末尾添加如下的内容：
export PATH=/home/liuqiang/ffmpeg/bin:$PATH
#再执行
source ~/.bashrc
#最后每次打开终端，都可以直接执行ffmpeg命令了
```

输出结果为：

```bash
liuqiang@LiuQiang-Ubuntu16:~$ ffmpeg
ffmpeg version N-91482-g8aa6d9a Copyright (c) 2000-2018 the FFmpeg developers
  built with gcc 5.4.0 (Ubuntu 5.4.0-6ubuntu1~16.04.10) 20160609
  configuration: --prefix=/home/liuqiang/ffmpeg/ffmpeg_build --pkg-config-flags=--static --extra-cflags=-I/home/liuqiang/ffmpeg/ffmpeg_build/include --extra-ldflags=-L/home/liuqiang/ffmpeg/ffmpeg_build/lib --extra-libs='-lpthread -lm' --bindir=/home/liuqiang/ffmpeg/bin --enable-gpl --enable-libaom --enable-libass --enable-libfdk-aac --enable-libfreetype --enable-libmp3lame --enable-libopus --enable-libvorbis --enable-libvpx --enable-libx264 --enable-libx265 --enable-nonfree
  libavutil      56. 18.102 / 56. 18.102
  libavcodec     58. 21.105 / 58. 21.105
  libavformat    58. 17.101 / 58. 17.101
  libavdevice    58.  4.101 / 58.  4.101
  libavfilter     7. 26.100 /  7. 26.100
  libswscale      5.  2.100 /  5.  2.100
  libswresample   3.  2.100 /  3.  2.100
  libpostproc    55.  2.100 / 55.  2.100
Hyper fast Audio and Video encoder
usage: ffmpeg [options] [[infile options] -i infile]... {[outfile options] outfile}...

Use -h to get full help or, even better, run 'man ffmpeg'
```

至此，`ffmpeg`的源码编译安装就结束了，祝你使用愉快！

阅读`ffmpeg`编译的文档：如果你想通过`man ffmpeg`命令开本地的`ffmpeg`文档，可以添加如下的环境变量到`shell`终端：

```bash
echo "MANPATH_MAP $HOME/ffmpeg/bin $HOME/ffmpeg/ffmpeg_build/share/man" >> ~/.manpath
```

测试`man ffmpeg`：

```bash
man ffmpeg
```

输出结果为：

```bash
FFMPEG(1)                                                                                                                                                                                    FFMPEG(1)

NAME
       ffmpeg - ffmpeg video converter

SYNOPSIS
       ffmpeg [global_options] {[input_file_options] -i input_url} ... {[output_file_options] output_url} ...

DESCRIPTION
       ffmpeg is a very fast video and audio converter that can also grab from a live audio/video source. It can also convert between arbitrary sample rates and resize video on the fly with a high
       quality polyphase filter.

       ffmpeg reads from an arbitrary number of input "files" (which can be regular files, pipes, network streams, grabbing devices, etc.), specified by the "-i" option, and writes to an arbitrary
       number of output "files", which are specified by a plain output url. Anything found on the command line which cannot be interpreted as an option is considered to be an output url.

       Each input or output url can, in principle, contain any number of streams of different types (video/audio/subtitle/attachment/data). The allowed number and/or types of streams may be limited
       by the container format. Selecting which streams from which inputs will go into which output is either done automatically or with the "-map" option (see the Stream selection chapter).

       To refer to input files in options, you must use their indices (0-based). E.g.  the first input file is 0, the second is 1, etc. Similarly, streams within a file are referred to by their
       indices. E.g. "2:3" refers to the fourth stream in the third input file. Also see the Stream specifiers chapter.

       As a general rule, options are applied to the next specified file. Therefore, order is important, and you can have the same option on the command line multiple times. Each occurrence is then
       applied to the next input or output file.  Exceptions from this rule are the global options (e.g. verbosity level), which should be specified first.

       Do not mix input and output files -- first specify all input files, then all output files. Also do not mix options which belong to different files. All options apply ONLY to the next input or
       output file and are reset between files.

       ·   To set the video bitrate of the output file to 64 kbit/s:

                   ffmpeg -i input.avi -b:v 64k -bufsize 64k output.avi

       ·   To force the frame rate of the output file to 24 fps:

                   ffmpeg -i input.avi -r 24 output.avi

       ·   To force the frame rate of the input file (valid for raw formats only) to 1 fps and the frame rate of the output file to 24 fps:

                   ffmpeg -r 1 -i input.m2v -r 24 output.avi

       The format option may be needed for raw input files.

DETAILED DESCRIPTION
       The transcoding process in ffmpeg for each output can be described by the following diagram:

                _______              ______________
               |       |            |              |
               | input |  demuxer   | encoded data |   decoder
               | file  | ---------> | packets      | -----+
               |_______|            |______________|      |
                                                          v
                                                      _________
                                                     |         |
                                                     | decoded |
                                                     | frames  |
                                                     |_________|
                ________             ______________       |
               |        |           |              |      |
               | output | <-------- | encoded data | <----+
               | file   |   muxer   | packets      |   encoder
               |________|           |______________|
...
```



参考文献：[CompilationGuide/Ubuntu](https://trac.ffmpeg.org/wiki/CompilationGuide/Ubuntu) | [CompilationGuide/Generic](https://trac.ffmpeg.org/wiki/CompilationGuide/Generic) | 



---

- `本文作者`：LiuQiang
- `版权声明`：本文为作者的原创文章，转载时请务必注明出处！