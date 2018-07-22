---
title: 基于Hexo的Yilia主题搭建博客网站
date: 2018-07-17 21:04:41
reward: true
tags:
	- Hexo
	- Yilia	
---

### 安装Git

```bash
sudo apt-get install git
```

### 安装Node.js

<!-- more -->

```bash
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.2/install.sh | bash
source ~/.bashrc #因为上一步向终端配置文件写入了环境变量
nvm install stable
```

### 安装Hexo

```bash
npm install -g hexo-cli
```

### 注册一个GitHub账户，并创建一个仓库

> 这里我创建了一个仓库名称为`LiuQiangBlog.github.io`，其中LiuQiangBlog是我的GitHub名称，仓库描述可有可无，仓库选择为public类型，因为这个是免费的，最后选中初始化仓库选项，这样我们就不用手动初始化了，最后点击`Create repository`按钮即可创建一个仓库。

### 创建并设置SSH Key

- 创建`SSH Key`：

```bash
ssh-keygen -t rsa -C "xxxxxx@163.com" #注意：此处的邮箱换成你自己的，接着一路按下Enter键即可
```

输出结果如下：

```bash
liuqiang@LiuQiang-Ubuntu16:~$ ssh-keygen -t rsa -C "xxxxxx@163.com" 
Generating public/private rsa key pair.
Enter file in which to save the key (/home/liuqiang/.ssh/id_rsa): 
Created directory '/home/liuqiang/.ssh'.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/liuqiang/.ssh/id_rsa.
Your public key has been saved in /home/liuqiang/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:xxxxxxxxxxxx xxxxxx@163.com
The key's randomart image is:
+---[RSA 2048]----+
|       .  .o..   |
|  .   o .oo o    |
| . + . +.*.+ .   |
|. B B  .*.+ o    |
|.+ B o +S+ o     |
|. o = ..X        |
| . o o * +       |
|  .   . = +      |
|   .E    ..+     |
+----[SHA256]-----+
```

- 设置`SSH Key`：

> 接下来到GitHub上，打开“Account settings”--“SSH Keys”页面，然后点击“Add SSH Key”，填上Title（随意写），在Key文本框里粘贴 id_rsa.pub文件里的全部内容，点“Add Key”，你就应该看到已经添加的Key，可以添加多个Key。

- 验证是否成功

验证是否成功，在git bash里输入下面的命令：

```bash
ssh -T git@github.com
```
如果初次设置的话，会出现如下界面，输入yes 同意即可：

```bash
liuqiang@LiuQiang-Ubuntu16:~$ ssh -T git@github.com
The authenticity of host 'github.com (13.229.188.59)' can't be established.
RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'github.com,13.229.188.59' (RSA) to the list of known hosts.
Hi LiuQiangBlog! You've successfully authenticated, but GitHub does not provide shell access.
```

- 设置username和email：
下面开始设置username和email，因为github每次commit都会记录他们：

```bash
git config --global user.name "xxxxxx" #你的GitHub登陆名
git config --global user.email "xxxxxx@163.com" #你的GitHub注册邮箱
```

- 创建一个`Hexo`静态网站：

```bash
cd /media/liuqiang/LiuQiang
mkdir RoboticsBlog
hexo init RoboticsBlog
cd RoboticsBlog
npm install
hexo -v #查看hexo是否安装成功
hexo g #生成站点
hexo s #开启服务器
hexo new "PyQt5入门编程实践" #在_posts目录下生成一篇新的博客文章
npm install hexo-deployer-git --save #生成及部署文章之前需要安装一个扩展
hexo d -g #编辑好文章之后就可以生成和部署了
#输入LiuQiangBlog
#输入LiuQiangBlog对应的密码

#后期部署步骤可以简化为下面2个命令：
hexo clean
hexo d -g
#如果是本地调试站点的话
hexo clean #清除上一次生成的站点
hexo g #生成静态站点
hexo s #启动服务器
```

### 关联本地站点和远程站点

在`Hexo`站点的_config.yaml文件中（注意：不是`Yilia`主题中的_config.yaml文件）修改成如下的内容：

```bash
# Deployment
## Docs: https://hexo.io/docs/deployment.html
deploy:
  type: git
  repository: https://github.com/LiuQiangBlog/LiuQiangBlog.github.io.git #关联远程站点
  branch: master
```

最后，通过`hexo d -g`命令部署完网站之后，就可以访问了，这里我可以访问我的站点了：

https://liuqiangblog.github.io

### 添加GitMent评论系统

首先需要注册gitment帐号，https://github.com/settings/applications/new，Github头像下拉菜单 > Settings > 左边Developer settings下的OAuth Application > Register a new application，填写相关信息：

1. `Application name`, `Homepage URL`, `Application description` 都可以随意填写
2. `Authorization callback URL` 一定要写自己Github Pages的URL
    (ps: 之前我自己就是在这里碰壁了，调试半天才发现)
3. 填写完上述信息后按`Register application`按钮，得到`Client ID`和`Client Secret`
接着在Yilia主题的配置文件`_config.yaml`中设置如下的内容：
```yaml
#5、Gitment
#gitment_owner: '...'      #你的 GitHub ID
#gitment_repo: '...'          #存储评论的 repo，直接将存储博客的repo作为存储评论的repo即可
#gitment_oauth:
#  client_id: '...'           #client ID
#  client_secret: '...'       #client secret
```

### 添加来必力评论系统

首先需要在来必力的官网进行注册，选择安装免费的`city`版本，会生成一段如下的代码：

```ejs
<!-- 来必力City版安装代码 data-uid中会包含你自己的uid-->
<div id="lv-container" data-id="city" data-uid="xxxxxx==">
	<script type="text/javascript">
   (function(d, s) {
       var j, e = d.getElementsByTagName(s)[0];

       if (typeof LivereTower === 'function') { return; }

       j = d.createElement(s);
       j.src = 'https://cdn-city.livere.com/js/embed.dist.js';
       j.async = true;

       e.parentNode.insertBefore(j, e);
   })(document, 'script');
	</script>
<noscript> 为正常使用来必力评论功能请激活JavaScript</noscript>
</div>
<!-- City版安装代码已完成 -->
```

将上述代码存放在`/themes/yilia/layout/_partial/post`目录下新建的一个`livere.ejs`文件中，接着在`Yilia`主题的配置文件`_config.yaml` 中设置如下的内容：

```yaml
# 来必力评论
livere: xxxxxx #此处粘贴你自己的上面代码中的data-uid内容，注意不要包含`==`
```

最后，在`/themes/yilia/layout/_partial/post` 目录下的`article.ejs`文件的适当位置添加如下的内容（相信你一定能找到添加评论插件的位置）：

```ejs
<% if (!index && post.comments){ %>
  <% if (theme.duoshuo){ %>
  <%- partial('post/duoshuo', {
      key: post.slug,
      title: post.title,
      url: config.url+url_for(post.path)
    }) %>
  <% } %>
<!-- 下面即为添加来必力评论系统需要添加的内容 -->
  <% if (theme.livere){ %>
  <%- partial('post/livere', {
      key: post.slug,
      title: post.title,
      url: config.url+url_for(post.path)
    }) %>
  <% } %>
```

### 启动Yilia主题自带的分享功能

```yaml
#注意：此处操作的是Yilia主题的_config.yaml文件
share_jia: true #即开启Yilia主题自带的分享功能
```

启动之后，我们会遇到一点问题，那就是微信分享用不了，无法生成用于分享的二维码。为此，我们需要稍作修改即可：

`/themes/yilia/layout/_partial/post`目录下的`share.ejs`文件，修改的结果如下：

```ejs
<div class="page-modal wx-share js-wx-box">
    <a class="close js-modal-close" href="javascript:;"><i class="icon icon-close"></i></a>
    <p>扫一扫，分享到微信</p>
    <div class="wx-qrcode">
      <img src="https://img.fanhaobai.com/qrcode.php?url=https://liuqiangblog.github.io/" alt="微信分享二维码">
    </div>
</div>
```

注意：请将url的地址替换成你自己的网站地址。

这样，我们就完美实现了Yilia主题自带的分享功能，`hexo clean`，`hexo g`，`hexo s`启动本地服务器查看分享效果，没问题的话，就可以直接部署了`hexo clean`，`hexo d -g`.

### 添加Mob分享功能

首先需要在Mob官网注册账户，接着创建一个应用，在sharesdk中可以看到我们需要的`shareSDKappkey`

```yaml
sharesdk: true #是否开启Mob分享
shareSDKappkey: 26de74740fc04 # 上一步申请到的app key
```

在`/themes/yilia/layout/_partial`目录下创建一个`share`目录，并在次目录下创建一个`share.ejs`文件，接着输入如下的内容：

```ejs
<!--MOB SHARE BEGIN-->
<div class="-mob-share-ui-button -mob-share-open">分享</div>
<div class="-mob-share-ui" style="display: none">
        <ul class="-mob-share-list">
            <li class="-mob-share-weibo"><p>新浪微博</p></li>
            <li class="-mob-share-tencentweibo"><p>腾讯微博</p></li>
            <li class="-mob-share-qzone"><p>QQ空间</p></li>
            <li class="-mob-share-qq"><p>QQ好友</p></li>
            <li class="-mob-share-weixin"><p>微信</p></li>                        
	    <li class="-mob-share-twitter"><p>Twitter</p></li>     
            <li class="-mob-share-youdao"><p>有道云笔记</p></li>
            <li class="-mob-share-mingdao"><p>明道</p></li>            
            <li class="-mob-share-linkedin"><p>LinkedIn</p></li>
        </ul>
    <div class="-mob-share-close">取消</div>
</div>
<div class="-mob-share-ui-bg"></div>
<script id="-mob-share" src="http://f1.webshare.mob.com/code/mob-share.js?appkey={{ theme.shareSDKappkey }}"></script>
<!--MOB SHARE END-->
```

最后在`/themes/yilia/`目录下的`article.ejs`文件中添加如下的内容：

```ejs
<% if (!index && theme.share_jia){ %>
<%- partial('post/share') %>
<% } %>
<!-- 下面即为需要添加的内容 -->
<% if (!index && theme.sharesdk){ %>
<%- partial('_partial/share/share.ejs') %>
<% } %>
```



### 添加网易云音乐

这里我直接在左侧栏中适当的位置插入网易云音乐（注意一定要在`<header>`...`</header>` 内插入，具体位置看个人喜好了）：

```ejs
<div style="position:relative; margin-left:-15px; margin-top:-10px; width:50%">
<iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=260 height=75 src="//music.163.com/outchain/player?type=2&id=33035954&auto=0&height=66">         </iframe>   
</div>
```

如果不想在访问网站时自动播放音乐，可以将上述代码中的`auto`设置为`0`即可，默认是设置为`1`，即访问网站时自动播放插入的音乐。

### 统计文章的阅读次数

`/themes/yilia/layout/_partial/post`目录下的`article.ejs`文件中添加如下的内容：

```ejs
<% if (!post.noDate){ %>
<%- partial('post/date', {class_name: 'archive-article-date', date_format: null}) %>
<% } %>
<!-- 下面即为添加统计文章的阅读次数-->
<% if ( !index ){ %>
    <span class="archive-article-date">
        本文总阅读量<span id="busuanzi_value_page_pv"></span>次
    </span>
<% } %>
```

### 统计网站的访问次数和访客数量

`/themes/yilia/layout/_partial/post`目录下的`footer.ejs`文件末尾加如下的内容：

```ejs
  <script async src="//dn-lbstatics.qbox.me/busuanzi/2.3/busuanzi.pure.mini.js"></script>
  <span id="busuanzi_container_site_pv"> 
      本站总访问量<span id="busuanzi_value_site_pv"></span>次
  </span>
  <span id="busuanzi_container_site_uv"> 
      您是第<span id="busuanzi_value_site_uv"></span>位访客
  </span>
```

### 添加音乐和视频

首先，我们需要安装如下的两个插件，在站点的根目录下执行如下的两个终端命令：

```bash
npm install hexo-tag-dplayer
npm install hexo-tag-aplayer
```



> 文章作者：LiuQiang
> 版权声明：本文为作者的原创文章，转载请务必注明出处！



