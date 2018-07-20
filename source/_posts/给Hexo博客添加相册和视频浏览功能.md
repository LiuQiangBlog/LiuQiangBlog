---
title: 给Hexo博客添加相册和视频浏览功能
date: 2018-07-20 08:05:02
tags:
	- Hexo
---

这里我使用的`Hexo`主题是`Yilia`主题，作者在自己的博客中已经实现了相册功能，这里以此为模板，实现个人网站的相册和视频浏览功能。

<!-- more -->

首先，在自己博客的根目录下创建两个目录：`photos`和`min_photos`，分别用来存储照片和照片缩略图。为了美观，所有的照片都将通过`Python`脚本程序统一处理成正方形，且尺寸大小相同。为了方便快速加载照片，在原始照片的基础上由创建了一套缩略照片。脚本程序`Imageprocess.py`和`Tools.py`均放在博客的根目录下。为了方便图片的加载，我们需要将`photos`中的照片信息写入到`data.json`文件中，为了方便写入，照片的命名格式统一为`2018-07-18_xxx.png`的格式，当然照片可以是`jpeg`，`png`，`gif`，`jpg`等格式。只需要在脚本处理程序中添加更多的照片格式即可。处理完照片并将信息写入`data.json`文件之后，先在自己的`GitHub`上创建一个备份博客的仓库，然后在博客的根目录下执行`git init`命令，接着将整个博客`push`到远程`GitHub`仓库上。因为在博客中显示的照片需要一个具体的网络存储地址。

接着，在`source/photos`目录下存放拷贝自`Yilia`主题作者备份博客中的如下四个文件：

- `index.ejs` : 
- `ins.css` : 样式表，为了实现在博客页面中添加视频的功能，需要在该样式表末尾添加`video-container`样式。
- `ins.js` : 该文件中需要修改`render`函数中的图片加载地址，将`minSrc`和`src`换成你自己远程仓库中的存储照片的地址
- `lazyload.min.js` : 一个jQuery或Zepto的图片延迟加载插件。该插件在较长的页面中延迟加载图片。视窗外的图片会延迟加载，直到它们由于用户滚动而出现到视窗中。可以将它看做图像预加载技术的反向运用。在包含很多大图片且较长页面中使用延迟加载，能使页面载入更快。浏览器在只加载可见区域的图片后就达到绪状态。在某些情况下，它也能帮助减少服务器端的负载。

`videos.ejs` : 自己在`source/photos`目录下创建的文件，用于实现在博客页面添加视频的功能
`data.json` : 通过`Python`脚本程序生成的照片信息，方便加载存储在远程仓库中的所有照片

在`ins.css`文件的末尾添加`video-container`样式：

```css
/*video*/
.video-container {
z-index: 1;
position: relative;
padding-bottom: 56.25%;
margin: 0 auto;
}
.video-container iframe, .video-container object, .video-container embed {z-index: 1;position: absolute;top: 0;left: 7%;width: 85%;height: 85%;box-shadow: 0px 0px 20px 2px #888888;}
```

修改`ins.js`文件的`render`函数中的`minSrc`和`src`的内容：

```js
 var render = function render(res) {
      var ulTmpl = "";
      for (var j = 0, len2 = res.list.length; j < len2; j++) {
        var data = res.list[j].arr;
        var liTmpl = "";
        for (var i = 0, len = data.link.length; i < len; i++) {
          var minSrc = 'https://github.com/LiuQiangBlog/LiuQiangBlog/tree/master/min_photos/' + data.link[i];
          var src = 'https://github.com/LiuQiangBlog/LiuQiangBlog/tree/master/photos/' + data.link[i];
          var type = data.type[i];
          var target = src + (type === 'video' ? '.mp4' : '.jpeg');
          src += '';

          liTmpl += '<figure class="thumb" itemprop="associatedMedia" itemscope="" itemtype="http://schema.org/ImageObject">\
                <a href="' + src + '" itemprop="contentUrl" data-size="1080x1080" data-type="' + type + '" data-target="' + src + '">\
                  <img class="reward-img" data-type="' + type + '" data-src="' + minSrc + '" src="/assets/img/empty.png" itemprop="thumbnail" onload="lzld(this)">\
                </a>\
                <figcaption style="display:none" itemprop="caption description">' + data.text[i] + '</figcaption>\
            </figure>';
        }
        ulTmpl = ulTmpl + '<section class="archives album"><h1 class="year">' + data.year + '年<em>' + data.month + '月</em></h1>\
        <ul class="img-box-ul">' + liTmpl + '</ul>\
        </section>';
      }
      document.querySelector('.instagram').innerHTML = '<div class="photos" itemscope="" itemtype="http://schema.org/ImageGallery">' + ulTmpl + '</div>';
      createVideoIncon();
      _view2.default.init();
    };
```





### 脚本程序

`ImageProcess.py`

```python
# coding=utf-8  
from PIL import Image  
import shutil  
import os  

class Graphics:  
    '''Image Process Class
    Parameters: infile, outfile
    ---
    infile: file path to load image

    outfile: file path to save image
    '''
    def __init__(self, infile, outfile):
        self.infile = infile
        self.outfile = outfile

    def fixed_size(self, width, height):  
        """按照固定尺寸处理图片"""  
        im = Image.open(self.infile)  
        out = im.resize((width, height),Image.ANTIALIAS)  
        out.save(self.outfile)  

    def resize_by_width(self, w_divide_h):  
        """按照宽度进行所需比例缩放"""  
        im = Image.open(self.infile)  
        (x, y) = im.size   
        x_s = x  
        y_s = x/w_divide_h  
        out = im.resize((x_s, y_s), Image.ANTIALIAS)   
        out.save(self.outfile)  

    def resize_by_height(self, w_divide_h):  
        """按照高度进行所需比例缩放"""  
        im = Image.open(self.infile)  
        (x, y) = im.size   
        x_s = y*w_divide_h  
        y_s = y  
        out = im.resize((x_s, y_s), Image.ANTIALIAS)   
        out.save(self.outfile)  

    def resize_by_size(self, size):  
        """按照生成图片文件大小进行处理(单位KB)"""  
        size *= 1024  
        im = Image.open(self.infile)  
        size_tmp = os.path.getsize(self.infile)  
        q = 100  
        while size_tmp > size and q > 0:  
            print (q)  
            out = im.resize(im.size, Image.ANTIALIAS)  
            out.save(self.outfile, quality=q)  
            size_tmp = os.path.getsize(self.outfile)  
            q -= 5  
        if q == 100:  
            shutil.copy(self.infile, self.outfile)  
  
    def cut_by_ratio(self):  
        """按照图片长宽进行分割
        
        ------------
        取中间的部分，裁剪成正方形
        """  
        im = Image.open(self.infile)  
        (x, y) = im.size  
        # print(x,"&",y)
        width = height = 660 #此处将图片处理成统一的大小:660x660
        region = (int(x/2-width/2), int(y/2-height/2), int(x/2+width/2), int(y/2+height/2))
        # print(region)
        crop_img = im.crop(region)
        crop_img.save(self.outfile) 
        # if x > y:  
        #     # region = (int(x/2-y/2), 0, int(x/2+y/2), y)  
        #     region = (int(x/2-width/2), int(y/2-height/2), int(x/2+width/2), int(y/2+height/2)) 

        #     #裁切图片  
        #     crop_img = im.crop(region)  
        #     #保存裁切后的图片  
        #     crop_img.save(self.outfile)             
        # elif x < y:  
        #     # region = (0, int(y/2-x/2), x, int(y/2+x/2))
        #     region = (int(x/2-width/2), int(y/2-height/2), int(x/2+width/2), int(y/2+height/2)) 
        #     #裁切图片  
        #     crop_img = im.crop(region)  
        #     #保存裁切后的图片  
        #     crop_img.save(self.outfile)             
```

`Tools.py`

```python
import os
import sys
import json
from PIL import Image
from datetime import datetime
from ImageCut import Graphics

# 定义压缩比，数值越大，压缩越小
SIZE_normal = 1.0
SIZE_small = 1.5
SIZE_more_small = 2.0
SIZE_more_small_small = 3.0


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
        if fileformat.lower() == "jpg" or fileformat.lower() == "jpeg" or fileformat.lower() == "png" or fileformat.lower() == "gif":
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

def compress(choose, des_dir, src_dir, file_list):
    """压缩算法，img.thumbnail对图片进行压缩，
    
    参数
    -----------
    choose: str
            选择压缩的比例，有4个选项，越大压缩后的图片越小
    """
    if choose == '1':
        scale = SIZE_normal
    if choose == '2': #压缩成2/3的尺寸
        scale = SIZE_small
    if choose == '3': #压缩成1/2的尺寸
        scale = SIZE_more_small
    if choose == '4': #压缩成1/3的尺寸
        scale = SIZE_more_small_small
    for infile in file_list:
        img = Image.open(src_dir+infile)
        # size_of_file = os.path.getsize(infile)
        w, h = img.size
        img.thumbnail((int(w/scale), int(h/scale))) #产生缩略图
        img.save(des_dir + infile)

def compress_photo():
    '''调用压缩图片的函数
    '''
    src_dir, des_dir = getCurrentPath() + "photos/", getCurrentPath() + "min_photos/"
    
    if directory_exists(src_dir):
        if not directory_exists(src_dir):
            make_directory(src_dir)
        # business logic
        file_list_src = list_img_file(src_dir)
    if directory_exists(des_dir):
        if not directory_exists(des_dir):
            make_directory(des_dir)
        file_list_des = list_img_file(des_dir)
        # print file_list
    '''如果已经压缩了，就不再压缩'''
    for i in range(len(file_list_des)):
        if file_list_des[i] in file_list_src:
            file_list_src.remove(file_list_des[i])
    compress('4', des_dir, src_dir, file_list_src)


def handle_photo():
    '''根据图片的文件名处理成需要的json格式的数据
    
    -----------
    最后将data.json文件存到博客的source/photos文件夹下
    '''
    src_dir, des_dir = getCurrentPath() + "photos/", getCurrentPath() + "min_photos/"
    file_list = list_img_file(src_dir)
    list_info = []
    for i in range(len(file_list)):
        filename = file_list[i]
        date_str, info = filename.split("_")
        info, _ = info.split(".")
        date = datetime.strptime(date_str, "%Y-%m-%d")
        year_month = date_str[0:7]            
        if i == 0:  # 处理第一个文件
            new_dict = {"date": year_month, "arr":{'year': date.year,
                                                    'month': date.month,
                                                    'link': [filename],
                                                    'text': [info],
                                                    'type': ['image']
                                                    }
                        } 
            list_info.append(new_dict)
        elif year_month != list_info[-1]['date']:  # 不是最后的一个日期，就新建一个dict
            new_dict = {"date": year_month, "arr":{'year': date.year,
                                                   'month': date.month,
                                                   'link': [filename],
                                                   'text': [info],
                                                   'type': ['image']
                                                   }
                        }
            list_info.append(new_dict)
        else:  # 同一个日期
            list_info[-1]['arr']['link'].append(filename)
            list_info[-1]['arr']['text'].append(info)
            list_info[-1]['arr']['type'].append('image')
    list_info.reverse()  # 翻转
    final_dict = {"list": list_info}
    with open(getCurrentPath() + "source/photos/data.json","w") as fp:
        json.dump(final_dict, fp)


def cut_photo():
    """裁剪算法
    
    ----------
    调用Graphics类中的裁剪算法，将src_dir目录下的文件进行裁剪（裁剪成正方形）
    """
    src_dir = getCurrentPath() + "photos/"
    # print(src_dir)
    # src_dir = "/media/liuqiang/LiuQiang/4_PyQt5/Program/PyQt5/photos/"
    print(src_dir)
    # dst_dir = getCurrentPath() + "cropped_photos/"
    if not directory_exists(src_dir):
        make_directory(src_dir)
    if directory_exists(src_dir):
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

def git_operation():
    '''
    git 命令行函数，将仓库提交
    
    ----------
    需要安装git命令行工具，并且添加到环境变量中
    '''
    #首次运行
    os.system('git init')
    os.system('git add --all')
    os.system('git commit -m "add photos"')
    os.system('git remote add origin https://github.com/LiuQiangBlog/LiuQiangBlog.git')
    os.system('git push -u origin master')
    #后续运行
    # os.system('git add --all')
    # os.system('git commit -m "update repository"')
    # os.system('git remote add origin https://github.com/LiuQiangBlog/LiuQiangBlog.git')
    # os.system('git push origin master')

if __name__ == "__main__":
    # cut_photo()
    # compress_photo()   # 压缩图片，并保存到mini_photos文件夹下
    # git_operation()    # 提交到github仓库
    handle_photo()     # 将文件处理成json格式，存到博客仓库中
```

