---
title: PyQt5笔记07
date: 2018-07-20 21:27:26
components: true
reward: true
toc: true
tags:
	- PyQt5
---

`需求说明`：使用`PyQt5`中的`QMainWindow`创建一个主窗口程序！

`模块导入`：

- `import os`
- `import sys`
- `from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget`
- `from PyQt5.QtGui import QIcon`

`完整代码`：

```python
import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
from PyQt5.QtGui import QIcon

def getCurrentPath():
    dirName, fileName = os.path.split(sys.argv[0])
    return dirName + "/"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage("Ready")
        self.resize(640, 480)
        self.setWindowTitle("MainWindow StatusBar")
        self.setWindowIcon(QIcon(getCurrentPath() + "ico.png"))
        self.center()
        self.show()

    def center(self):
        Rect = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        Rect.moveCenter(cp)
        self.move(Rect.topLeft())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
```

`实例总结`：

- 继承自`QMainWindow`窗口程序与前面继承自`QWidget`的窗口程序不同，最明显的区别是前者有`菜单栏`，`工具栏`和`状态栏`！
- 设置状态栏的显示信息使用`self.statusBar().showMessage("Ready")`来实现！

`运行效果`：

![2018-07-20 21-30-52屏幕截图.png](https://i.loli.net/2018/07/20/5b51e41acc515.png)

---

- 本文作者：LiuQiang
- 版权声明：本文为作者的原创文章，转载时请务必注明出处！