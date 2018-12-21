---
title: PyQt5笔记18
date: 2018-07-21 20:01:07
components: true
reward: true
toc: true
tags:
	- PyQt5
---

`需求说明`：使用`PyQt5`中的`sender()`函数获取指定信号的发出者！

`模块导入`：

- `import os`
- `import sys`
- `from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QPushButton`
- `from PyQt5.QtGui import QIcon`

`完整代码`：

```python
import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QPushButton
from PyQt5.QtGui import QIcon

def getCurrentPath():
    dirName, fileName = os.path.split(sys.argv[0])
    return dirName + "/"

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        btn1 = QPushButton("Button_1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button_2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.btnClicked)
        btn2.clicked.connect(self.btnClicked)

        self.stsbar = self.statusBar()
        self.resize(640, 480)
        self.setWindowTitle("findSender")
        self.setWindowIcon(QIcon(getCurrentPath() + "ico.png"))
        self.center()
        self.show()

    def btnClicked(self):
        sender = self.sender()
        self.stsbar.showMessage(sender.text() + "was pressed!")
    
    def center(self):
        rect = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        rect.moveCenter(cp)
        self.move(rect.topLeft())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    sys.exit(app.exec_())
```

`实例总结`：

- `QObject* QObject::sender()`函数返回的是一个`QObject`类型的发送信号的对象的指针，当然在python中没有指针的说法，那么我们就当返回的是`QObject`对象即可，我们知道`QObject`类是所有控件的基类！

`运行效果`：

![2018-07-21 20-21-57屏幕截图.png](https://i.loli.net/2018/07/21/5b5327b4bdfbb.png)

---
- 本文作者：LiuQiang
- 版权声明：本文为作者的原创文章，转载时请务必注明出处！