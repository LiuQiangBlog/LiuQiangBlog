---
title: PyQt5笔记03
date: 2018-07-20 18:39:57
components: true
reward: true
toc: true
tags:
	- PyQt5
---

`需求说明`：使用`PyQt5`中的`QToolTip`为`[PyQt5笔记02]`中的界面应用程序实现当鼠标悬停在窗口部件上时，会弹出提示窗口！

`模块导入`：

- `import os`
- `import sys`
- `from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton`
- `from PyQt5.QtGui import QIcon`

`完整代码`：

```python
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton
from PyQt5.QtGui import QFont, QIcon

def getCurrentDir():
    dirName, fileName = os.path.split(sys.argv[0])
    return dirName + "/"

class MyWidget(QWidget):
    def __init__(self): #用于对象的初始化，在Python中self类似于C++的this指针
        super().__init__() #用于父对象的初始化
        self.initUI() #调用界面初始化函数

    def initUI(self):
        QToolTip.setFont(QFont("SansSerif", 12)) #使用静态方法设置用于渲染提示的字体类型和大小

        self.setToolTip("This is a <b>QWidget</b> widget") #设置提示的内容
        
        button = QPushButton("Button", self) #创建一个按钮对象并指定其父对象
        button.setToolTip("This is a <b>QPushButton</b> widget")
        button.resize(button.sizeHint()) #使用推荐的尺寸
        button.move(50, 50) #将按钮移动到指定的位置，相对于父对象的左上角，即程序窗口的左上角

        self.setGeometry(640, 480, 600, 200) #x, y, width, height
        self.setWindowTitle("Window ToolTips")
        self.setWindowIcon(QIcon(getCurrentDir() + "ico.png"))

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    sys.exit(app.exec_())
```

`实例总结`：

- 这里使用的是静态方法`QToolTip.setFont(QFont("SansSerif", 12))`为`QToolTip`的内容设置渲染字体！
- 我们可以使用`setToolTip(QString)`方法为任何窗口对象设置提示的内容
- 我们可以使用`setGeometry(x,y,width,height)`设置窗口部件相对于父部件的位置及自身的大小

`运行效果`：

![2018-07-20 19-34-54屏幕截图.png](https://i.loli.net/2018/07/20/5b51c9046825f.png)
![2018-07-20 19-35-08屏幕截图.png](https://i.loli.net/2018/07/20/5b51c90469ccc.png)

---

- 本文作者：LiuQiang
- 版权声明：本文为作者的原创文章，转载时请务必注明出处！