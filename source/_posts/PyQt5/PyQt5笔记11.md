---
title: PyQt5笔记11
date: 2018-07-21 10:30:21
components: true
reward: true
toc: true
tags:
	- PyQt5
---

`需求说明`：使用`PyQt5`中的`QMainWindow`和`QMenu`实现带有弹出式菜单的窗口应用程序！

`模块导入`：

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

        self.exitAction = QAction(QIcon(getCurrentPath() + "exit.png"), "Exit", self)
        self.exitAction.setShortcut("Ctrl+Q")
        self.exitAction.setStatusTip("Exit the Application")
        # self.exitAction.triggered.connect(qApp.quit) #qApp == QApplication.instance()，直接关闭窗口
        self.exitAction.triggered.connect(self.close) #此处会触发窗口关闭事件，进而弹出提示消息窗口
        fileMenu.addAction(self.exitAction)

        importMenu = QMenu("Import", self)
        self.importAction = QAction(QIcon(getCurrentPath() + "import.png"), "Import Mail", self)
        importMenu.addAction(self.importAction)

        self.newAction = QAction(QIcon(getCurrentPath() + "new.png"), "New File", self)
        fileMenu.addAction(self.newAction) #添加动作
        fileMenu.addMenu(importMenu) #添加子菜单

        self.viewStateAction = QAction(QIcon(getCurrentPath() + "view.png"), "View StatusBar", self)
        self.viewStateAction.setStatusTip("View StatusBar")
        self.viewStateAction.setCheckable(True)
        self.viewStateAction.setChecked(True)
        self.viewStateAction.triggered.connect(self.toggleMenu)
        viewMenu.addAction(self.viewStateAction)

        # toolbar = self.addToolBar("Exit") #创建一个工具栏对象并绑定标识符
        toolbar = QToolBar(self)
        self.addToolBar(toolbar)
        toolbar.addAction(self.exitAction)
        toolbar.addAction(self.viewStateAction)

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
        reply = QMessageBox.question(self, "Message", "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No | QMessageBox.Ignore, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept() #等价于QEvent对象的setAccepted(True)
        else:
            event.ignore() #等价于QEvent对象的setAccepted(False)

    def toggleMenu(self, state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

    def contextMenuEvent(self, event):
       
        popMenu = QMenu(self)
        
        newAction = popMenu.addAction("New")
        opnAction = popMenu.addAction("Open")
        quitAction = popMenu.addAction("Quit")
        # self.mapToGlobal(event.pos())将鼠标事件发生的位置映射到全局坐标系
        action = popMenu.exec_(self.mapToGlobal(event.pos())) #返回选中的菜单项
        
        if action == quitAction:
            qApp.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
```

`实例总结`：

- 为了实现鼠标右键的弹出式菜单效果，我们需要重新实现`contextMenuEvent()`事件处理函数！
- `self.close()`槽函数触发的事件等价于鼠标关闭窗口程序，不同于`qApp.quit()`，`qApp.quit()`是直接退出程序！

`运行效果`：

![2018-07-21 11-13-14屏幕截图.png](https://i.loli.net/2018/07/21/5b52a4e0e80d9.png)

---
- 本文作者：LiuQiang
- 版权声明：本文为作者的原创文章，转载时请务必注明出处！