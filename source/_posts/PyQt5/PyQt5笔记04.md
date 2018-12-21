---
title: PyQt5笔记04
date: 2018-07-20 19:43:37
components: true
reward: true
toc: true
tags:
	- PyQt5
---

`需求说明`：使用`PyQt5`中的`QPushButton().clicked.connect(qApp.quit)`信号和槽及关联方法实现关闭`[PyQt5笔记03]`中的窗口程序的功能！

`模块导入`：

- `import os`
- `import sys`
- `from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, qApp`
- `from PyQt5.QtGui import QIcon, QFont`

`完整代码`：

```python
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, qApp
from PyQt5.QtGui import QIcon, QFont

def getCurrentPath():
    dirName, fileName = os.path.split(sys.argv[0])
    return dirName + "/"

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont("SansSerif", 12))

        button = QPushButton("Quit", self)
        # button.clicked.connect(QApplication.instance().quit)
        button.clicked.connect(qApp.quit) #注意调用槽函数没有括号，即没有quit()中的括号
        button.resize(button.sizeHint())
        button.setToolTip("This Button is used for <b>Closing</b> the Window")
        button.move(50, 50)

        self.setGeometry(640, 280, 640, 480)
        self.setWindowTitle("Close Window")
        self.dirPath = getCurrentPath()
        self.setWindowIcon(QIcon(self.dirPath + "ico.png"))
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    sys.exit(app.exec_())
```

`实例总结`：

- 注意调用槽函数时没有括号，例如本例中调用的槽函数`qApp.quit()`并没有添加括号哦！
- `qApp`是一个指向应用程序实例对象的全局指针，等价于`QApplication.instance()`和`QCoreApplication::instance()`！

`运行效果`：

![2018-07-20 20-10-32屏幕截图.png](https://i.loli.net/2018/07/20/5b51d14f1f4f5.png)