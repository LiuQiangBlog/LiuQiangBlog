---
title: PyQt5笔记21
date: 2018-07-22 14:38:52
components: true
reward: true
toc: true
tags:
	- PyQt5
---

`需求说明`：使用`PyQt5`中的`QColorDialog`实现通过颜色对话框设定画布的颜色！

`模块导入`：

- `import os`
- `import sys`
- `from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QPushButton, QFrame, QColorDialog`
- `from PyQt5.QtGui import QIcon, QColor`

`完整代码`：

```python
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QPushButton, QFrame, QColorDialog
from PyQt5.QtGui import QIcon, QColor

def getCurrentPath():
    dirName, fileName = os.path.split(sys.argv[0])
    return dirName + "/"

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        color = QColor(0, 0, 0) #r, g, b, a
        btn = QPushButton("ColorDialog", self)
        btn.move(80, 80)
        btn.clicked.connect(self.showDialog)

        self.frame = QFrame(self)
        self.frame.setStyleSheet("QWidget {background-color: %s}" %format(color.name()))
        self.frame.setGeometry(300, 80, 200, 200)
        self.resize(640, 480)
        self.setWindowTitle("ColorDialog")
        self.setWindowIcon(QIcon(getCurrentPath() + "ico.png"))
        self.center()
        self.show()
    
    def center(self):
        rect = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        rect.moveCenter(cp)
        self.move(rect.topLeft())
    
    def showDialog(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.frame.setStyleSheet("QWidget {background-color: %s}" %format(color.name()))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    sys.exit(app.exec_())
```

`实例总结`：

- 使用`QColorDialog.getColor()`可以获取用户选择输入的颜色
- `self.frame.setStyleSheet("QWidget {background-color: %s}" %format(color.name()))`可以设置画布的颜色

`运行效果`：

![2018-07-22 15-25-21屏幕截图.png](https://i.loli.net/2018/07/22/5b5432606f8b0.png)

---
- 本文作者：LiuQiang
- 版权声明：本文为作者的原创文章，转载时请务必注明出处！