---
title: PyQt5笔记09
date: 2018-07-21 08:58:26
components: true
reward: true
toc: true
tags:
	- PyQt5
---

`需求说明`：使用`PyQt5`中的`QMainWindow`、`QMenu`和`QAction`实现带有子菜单的窗口程序！

`模块导入`：

- `import os`
- `import sys`
- `from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDesktopWidget, QMenu, QAction, qApp, QTextEdit`
- `from PyQt5.QtGui import QIcon`

`完整代码`：

```python
import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDesktopWidget, QMenu, QAction, qApp, QTextEdit
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

        toolbar = self.addToolBar("Exit")
        toolbar.addAction(exitAction)

        self.statusBar()

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
```

`实例总结`：

- `子菜单`本质上就是一个`菜单`，只是`子菜单`还可以插入普通的`菜单`中，`子菜单`中也同样可以添加多个`菜单项`，也就是说展开`菜单`，我们看到的不仅仅有`菜单项`，还可以有`子菜单`，展开`子菜单`，我们可以看到其中包含的`菜单项`！
- `子菜单`的目的在于将具有相关功能的`菜单项`集合在一起，便于`记忆`和`操作`！

`运行效果`：

![2018-07-21 09-16-41屏幕截图.png](https://i.loli.net/2018/07/21/5b5289ddeed33.png)

---
- 本文作者：LiuQiang
- 版权声明：本文为作者的原创文章，转载时请务必注明出处！

