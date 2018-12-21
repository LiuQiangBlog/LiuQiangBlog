---
title: PyQt5笔记16
date: 2018-07-21 16:34:39
components: true
reward: true
toc: true
tags:
	- PyQt5
---

`需求说明`：使用`PyQt5`中的`keyPressEvent`实现当按下`Esc`快捷键时，窗口程序执行关闭操作！

`模块导入`：

- `import os`
- `import sys`
- `from PyQt5.QtWidgets import QWidget, QApplication`
- `from PyQt5.QtCore import Qt`

`完整代码`：

```python
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

def getCurrentPath():
    dirName, fileName = os.path.split(sys.argv[0])
    return dirName + "/"

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.resize(640, 480)
        self.setWindowTitle("KeyPressEvent")
        self.setWindowIcon(QIcon(getCurrentPath() + "ico.png"))
        self.center()
        self.show()
    
    def center(self):
        Rect = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        Rect.moveCenter(cp)
        self.move(Rect.topLeft())
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    sys.exit(app.exec_())
```

`实例总结`：

- 如果我们想要在自己的程序中实现基于键盘事件某些功能，那么就需要重写`keyPressEvent()`事件函数！

`运行效果`：

![2018-07-21 17-02-51屏幕截图.png](https://i.loli.net/2018/07/21/5b52f6c9b8390.png)

---
- 本文作者：LiuQiang
- 版权声明：本文为作者的原创文章，转载时请务必注明出处！