---
title: PyQt5笔记08
date: 2018-07-20 21:37:51
components: true
reward: true
toc: true
tags:
	- PyQt5
---

`需求说明`：使用`PyQt5`中的`QMainWindow`和`QAction`创建带有`菜单栏`、`工具栏`和`状态栏`的窗口程序！

`模块导入`：

- `import os`
- `import sys`
- `from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QAction, QTextEdit, qApp`
- `from PyQt5.QtGui import QIcon`

`完整代码`：

```python
import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QAction, QTextEdit, qApp
from PyQt5.QtGui import QIcon

def getCurrentPath():
    dirName, fileName = os.path.split(sys.argv[0])
    return dirName + "/"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        exitAction = QAction(QIcon(getCurrentPath() + "exit.png"), "Exit", self)
        exitAction.setShortcut("Ctrl+Q") #快捷键中间不能有空格，否则无效
        exitAction.setStatusTip("Exit the Application") #当鼠标悬停在exitAction上面时，会在窗口程序的状态栏显示‘Exit the Application’
        exitAction.triggered.connect(QApplication.instance().quit)
        # exitAction.clicked.connect(qApp.quit)
        

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar("Exit")
        toolbar.addAction(exitAction)

        self.statusBar()

        textEdit = QTextEdit("Hello World!", self)
        self.setCentralWidget(textEdit)

        self.resize(640, 480)
        self.setWindowTitle("Simple MenuBar")
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

- 编写基于`QMainWindow`的窗口程序时，需要充分了解什么是`菜单栏`、`菜单`和`菜单项`，`菜单项`的集合形成`菜单`，而`菜单`的集合形成`菜单栏`！
- `工具栏`是显示`位图式按钮`的`工具条`，`位图式按钮`用于执行命令，按下`位图式按钮`相当于选择菜单项，如果某个`菜单项`具有和`工具栏按钮`相同的ID，那么使用`工具栏按钮`将会调用映射到该`菜单项`的同一个处理函数！
- 可以配置`按钮`，使其在外观和行为上表现为`普通按钮`、`单选按钮`或`复选框`！

`运行效果`：
![2018-07-21 08-49-54屏幕截图.png](https://i.loli.net/2018/07/21/5b528347ec027.png)

---
- 本文作者：LiuQiang
- 版权声明：本文为作者的原创文章，转载时请务必注明出处！

