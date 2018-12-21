---
title: PyQt5笔记02
date: 2018-07-20 18:23:21
components: true
reward: true
toc: true
tags:
	- PyQt5
---

### 为应用程序添加图标

`需求说明`：使用`PyQt5`中的`QIcon`为`[PyQt5笔记01]`中的界面应用程序添加一个图标！

`模块导入`：

- `import os`
- `import sys`
- `from PyQt5.QtWidgets import QApplication, QWidget`
- `from PyQt5.QtGui import QIcon`

`完整代码`：

```python
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

def getCurrentDir():
    dirName, fileName = os.path.split(sys.argv[0])
    return dirName + "/" #返回当前文件所在目录的绝对路径
    
class MyWidget(QWidget):
    def __init__(self): #用于对象的初始化，在Python中self类似于C++的this指针
        super().__init__() #用于父对象的初始化
        # 不同于Python2中的super(MyWidget, self).__init__()
        self.initUI() #调用界面初始化函数
    
    def initUI(self):
        self.setGeometry(600, 200, 640, 480)
        self.setWindowTitle("Window with Icon")
        self.setWindowIcon(QIcon(getCurrentDir() + "ico.png"))
        # 注意：Ubuntu下相对路径下无法访问图标资源，必须绝对路径！
        # self.setWindowIcon(QIcon("ico.png")) 
        
        self.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    sys.exit(app.exec_())
```

`实例总结`：

- 绝大部分的界面应用程序都有自己的图标，因此知道如何实现为界面应用程序添加图标是非常重要的！
- `Ubuntu`系统下编程访问图标资源需要使用绝对路径，否则无法实现图标资源的加载！
- 获取当前正在运行的程序所在的目录可以使用`os.path.split(argv[0])`来实现！

`运行效果`：

![2018-07-20 19-17-03屏幕截图.png](https://i.loli.net/2018/07/20/5b51c55eace86.png)

---

- 本文作者：LiuQiang
- 版权声明：本文为作者的原创文章，转载时请务必注明出处！

