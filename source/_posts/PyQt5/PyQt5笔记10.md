---
title: PyQt5笔记10
date: 2018-07-21 09:24:14
components: true
reward: true
toc: true
tags:
	- PyQt5
---

`需求说明`：使用`PyQt5`中的`QMainWindow`和`QAction`实现某个`菜单项`带有`默认状态`的窗口程序！

`模块导入`:

- `import os`
- `import sys`
- `from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDesktopWidget, QMenu, QAction, qApp, QTextEdit, QToolBar`
- `from PyQt5.QtGui import QIcon`

`完整代码`：

```python
import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDesktopWidget, QMenu, QAction, qApp, QTextEdit, QToolBar
from PyQt5.QtGui import QIcon

def getCurrentPath():
    dirName, fileName = os.path.split(sys.argv[0])
    return dirName + "/"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        viewMenu = menubar.addMenu("&View")

        exitAction = QAction(QIcon(getCurrentPath() + "exit.png"), "Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit the Application")
        exitAction.triggered.connect(qApp.quit) #qApp == QApplication.instance()
        fileMenu.addAction(exitAction)

        importMenu = QMenu("Import", self)
        importAction = QAction(QIcon(getCurrentPath() + "import.png"), "Import Mail", self)
        importMenu.addAction(importAction)

        newAction = QAction(QIcon(getCurrentPath() + "new.png"), "New File", self)
        fileMenu.addAction(newAction) #添加动作
        fileMenu.addMenu(importMenu) #添加子菜单

        viewStateAction = QAction(QIcon(getCurrentPath() + "view.png"), "View StatusBar", self)
        viewStateAction.setStatusTip("View StatusBar")
        viewStateAction.setCheckable(True) # 设置该菜单项可切换'on/off'状态
        viewStateAction.setChecked(True) # 设置该菜单项的默认状态为'on'
        viewStateAction.triggered.connect(self.toggleMenu) #具有toggle功能的按钮当被设置为checked时会发射state信号
        viewMenu.addAction(viewStateAction)

        # toolbar = self.addToolBar("Exit") #创建一个工具栏对象并绑定标识符
        toolbar = QToolBar(self)
        self.addToolBar(toolbar)
        toolbar.addAction(exitAction)
        toolbar.addAction(viewStateAction)

        self.statusbar = self.statusBar() #创建状态栏对象
        self.statusbar.showMessage("Ready")

        textEdit = QTextEdit("Hello, World!", self)
        self.setCentralWidget(textEdit)

        self.setWindowTitle("Mainwindow with SubMenu")
        self.setWindowIcon(QIcon(getCurrentPath() + "ico.png"))
        self.resize(640, 480)
        self.center()
        self.show()

    def center(self):
        Rect = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        Rect.moveCenter(cp)
        self.move(Rect.topLeft())

    def closeEvent(self, event):     
        reply = QMessageBox.question(self,\
                                     "Message",\
                                     "Are you sure to quit?",\
                                     QMessageBox.Yes | QMessageBox.No | QMessageBox.Ignore,\
                                     QMessageBox.No
                                     )

        if reply == QMessageBox.Yes:
            event.accept() #等价于QEvent对象的setAccepted(True)
        else:
            event.ignore() #等价于QEvent对象的setAccepted(False)

    def toggleMenu(self, state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
```

`实例总结`：

- `setCheckable(True)`函数用于设置`菜单项`为具有`开关`功能的菜单项，比如`word`文档中的`Bold`菜单项即为`开关`菜单项，用户在编辑文档的时候，可以切换是否开启`Bold`文字加粗功能！

`运行效果`：

![2018-07-21 10-25-16屏幕截图.png](https://i.loli.net/2018/07/21/5b5299a8d8709.png)

---
- 本文作者：LiuQiang
- 版权声明：本文为作者的原创文章，转载时请务必注明出处！