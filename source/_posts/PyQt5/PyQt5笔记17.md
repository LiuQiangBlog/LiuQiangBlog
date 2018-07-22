---
title: PyQt5笔记17
date: 2018-07-21 17:13:15
components: true
reward: true
toc: true
tags:
	- PyQt5
---

`需求说明`：使用`PyQt5`中的`mouseMoveEvent()`函数实现跟踪并显示鼠标位置的坐标值到`QLabel`中！

`模块导入`：

- `import os`
- `import sys`
- 

`完整代码`：

```python
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QGridLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

x = 0
y = 0
def getCurrentPath():
    dirName, fileName = os.path.split(sys.argv[0])
    return dirName + "/"

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        global x
        global y
        text = "x: {}, y:{}".format(x, y)
        self.label =QLabel(text, self)
        grid = QGridLayout()
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)
        self.setLayout(grid)
        self.setMouseTracking(True) #开启鼠标跟踪模式
        self.resize(640, 480)
        self.setWindowTitle("MouseTracking")
        self.setWindowIcon(QIcon(getCurrentPath() + "ico.png"))
        self.center()
        self.show()
    def center(self):
        Rect = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        Rect.moveCenter(cp)
        self.move(Rect.topLeft())

    def mouseMoveEvent(self, event):
        global x
        global y
        x = event.x()
        y = event.y()
        text = "x:{}, y:{}".format(x, y)
        self.label.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    sys.exit(app.exec_())
```

`实例总结`：

- `mouseMoveEvent()`即鼠标移动事件处理函数，由于是虚函数，我们需要重写该事件处理函数！
- 获取鼠标移动事件中鼠标位置的函数为`QMouseEvent::x() `和`QMouseEvent::y()`，注意数据类型均为`int`型！

`运行效果`：

![2018-07-21 19-55-24屏幕截图.png](https://i.loli.net/2018/07/21/5b531f371f753.png)

---
- 本文作者：LiuQiang
- 版权声明：本文为作者的原创文章，转载时请务必注明出处！