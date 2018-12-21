---
title: Python3实现将批量图片裁剪成正方形
date: 2018-07-16 15:32:25
comments: true
reward: true
categories: 
	- Python3笔记
toc: true
tags: 
	- Python3
	- Pillow
---

### 1 简介
本文将介绍如何通过Python3实现批量裁剪不规则图片，实现将图片统一裁剪成正方形，达到美观展示的目的。

<!--more-->

### 2 功能实现
#### 2.1相关类

**ImageCut.py**

```python
# coding=utf-8  
from PIL import Image  
import shutil  
import os  

class Graphics:  
    '''图片处理类
    
    参数: infile, outfile
    ------
    infile: 加载图片文件的路径
    outfile: 转存图片文件的路径
    '''
    def __init__(self, infile, outfile):
        self.infile = infile
        self.outfile = outfile
  
    def cut_by_ratio(self):  
        """按照图片长宽进行分割
        
        参数: None
        ------
        取中间的部分，裁剪成正方形
        """  
        im = Image.open(self.infile)  
        (x, y) = im.size  
        if x > y:  
            region = (int(x/2-y/2), 0, int(x/2+y/2), y)  
            #裁切图片  
            crop_img = im.crop(region)  
            #保存裁切后的图片  
            crop_img.save(self.outfile)             
        elif x < y:  
            region = (0, int(y/2-x/2), x, int(y/2+x/2))
            #裁切图片  
            crop_img = im.crop(region)  
            #保存裁切后的图片  
            crop_img.save(self.outfile)             

```

#### 2.2 相关函数

**ImageProcess.py**

```python
import os
import sys
from PIL import Image
from ImageCut import Graphics

def getCurrentPath():
    dirName, fileName = os.path.split(sys.argv[0])
    return dirName + "/"

def list_img_file(directory):
    """列出目录下所有文件，并筛选出图片文件列表返回"""
    old_list = os.listdir(directory)
    # print old_list
    new_list = []
    for filename in old_list:
        name, fileformat = filename.split(".")
        if fileformat.lower() == "jpg" or fileformat.lower() == "png" or fileformat.lower() == "gif":
            new_list.append(filename)
    # print new_list
    return new_list

def make_directory(directory):
    """创建目录"""
    os.makedirs(directory)

def directory_exists(directory):
    """判断目录是否存在"""
    if os.path.exists(directory):
        return True
    else:
        return False

def cut_photo():
    """裁剪算法
    
    参数：None
    ------
    调用Graphics类中的裁剪算法，将src_dir目录下的文件进行裁剪（裁剪成正方形）
    """
    src_dir = getCurrentPath() + "photos/"
    # dst_dir = getCurrentPath() + "cropped_photos/"
    if directory_exists(src_dir):
        if not directory_exists(src_dir):
            make_directory(src_dir)
        # business logic
        file_list = list_img_file(src_dir)
        # print file_list
        if file_list:
            # print_help()
            for infile in file_list:
                img = Image.open(src_dir + infile)
                Graphics(infile=src_dir + infile, outfile=src_dir + infile).cut_by_ratio() #原地替换 
                # Graphics(infile=src_dir + infile, outfile=dst_dir + infile).cut_by_ratio() #图片转储         
        else:
            pass
    else:
        print("source directory not exist!") 

if __name__ == "__main__":
    cut_photo()
```

### 3 使用方法

在**ImageProcess.py**文件所在的目录下创建一个**photos**目录，然后将有待批量处理的图片放进来，最后运行**ImageProcess.py**文件即可。

**注意：**此处并没有转存图片，而是直接裁剪后的文件替换原文件，如果要实现将批量裁剪后的图片文件转储到一个文件夹下，我们需要再建一个新的目录，我们暂且叫做**cropped_photos**，然后将**ImageProcess.py**文件中的如下语句：

```python
Graphics(infile=src_dir + infile, outfile=src_dir + infile).cut_by_ratio() #原地替换 
# Graphics(infile=src_dir + infile, outfile=dst_dir + infile).cut_by_ratio() #图片转储   
```

替换成：

```python
# Graphics(infile=src_dir + infile, outfile=src_dir + infile).cut_by_ratio() #原地替换 
Graphics(infile=src_dir + infile, outfile=dst_dir + infile).cut_by_ratio() #图片转储   
```

运行**ImageProcess.py**文件即可实现批量图片裁剪和转储。

---

- 本文作者：LiuQiang
- 版权声明：本文为作者的原创文章，转载时请务必注明出处！