---
title: PyQt5笔记19
date: 2018-07-21 20:32:57
components: true
reward: true
toc: true
tags:
	- PyQt5
---

`需求说明`：使用`PyQt5`中的`pyqtSignal`实现发送自定义信号！

`模块导入`：

- `import os`
- `import sys`
- `from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget `
- `from PyQt5.QtCore import pyqtSignal, QObject`
- `from PyQt5.QtGui import QIcon`

`完整代码`：

```python
import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtGui import QIcon

def getCurrentPath():
    dirName, fileName = os.path.split(sys.argv[0])
    return dirName + "/"
    
class Communicate(QObject): #自定义可以通过emit()函数发射信号的类
    #只有继承自QObject的类才能通过emit()函数发射信号

    closeApp = pyqtSignal()

class MyWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.comm = Communicate()
        self.comm.closeApp.connect(self.close) #关联信号和槽
        self.resize(640, 480)
        self.setWindowTitle("Customized Signal")
        self.setWindowIcon(QIcon(getCurrentPath() + "ico.png"))
        self.center()
        self.show()
    
    def center(self):
        rect = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        rect.moveCenter(cp)
        self.move(rect.topLeft())
    
    def mousePressEvent(self, event): #当鼠标按下时，发射关闭窗口程序的信号
        self.comm.closeApp.emit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    sys.exit(app.exec_())
```

`实例总结`：

- 自定义可以通过`emit()`函数发射信号的类必须继承自`QObject`基类！
- 可以通过`mousePressEvent(self, event)`鼠标单击事件处理函数来执行`emit()`函数实现关闭窗口信号的发射！

`运行效果`：


![2018-07-21 21-32-35屏幕截图.png](https://i.loli.net/2018/07/21/5b5336ce97a7c.png)

---
- 本文作者：LiuQiang
- 版权声明：本文为作者的原创文章，转载时请务必注明出处！