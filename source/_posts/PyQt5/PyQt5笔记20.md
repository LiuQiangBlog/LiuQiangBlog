---
title: PyQt5笔记20
date: 2018-07-21 21:41:34
components: true
reward: true
toc: true
tags:
	- PyQt5
---

`需求说明`：使用`PyQt5`中的`QInputDialog`实现窗口应用程序集成简单的内容输入功能！

`导入模块`：

- `import os`
- `import sys`
- `from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QPushButton, QLineEdit, QInputDialog`
- `from PyQt5.QtGui import QIcon`

`完整代码`：

```python
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QPushButton, QLineEdit, QInputDialog
from PyQt5.QtGui import QIcon

def getCurrentPath():
    dirName, fileName = os.path.split(sys.argv[0])
    return dirName + "/"

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        btn = QPushButton("Dialog", self)
        btn.move(20, 20)
        btn.clicked.connect(self.showDialog)

        self.lineEdit = QLineEdit(self)
        self.lineEdit.move(130, 22)

        self.resize(640, 480)
        self.setWindowTitle("InputDialog")
        self.setWindowIcon(QIcon(getCurrentPath() + "ico.png"))
        self.center()
        self.show()
    
    def center(self):
        rect = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        rect.moveCenter(cp)
        self.move(rect.topLeft())
    
    def showDialog(self):
        text, ok = QInputDialog.getText(self, "Input Dialog", "Enter your name: ") #返回的数据类型是QString, ok
        if ok:
            self.lineEdit.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    sys.exit(app.exec_())
```

`实例总结`：

- 本实例内容输入功能的实现本质上就是自定义并关联槽函数！

`运行效果`：

![2018-07-22 14-09-07屏幕截图.png](https://i.loli.net/2018/07/22/5b541f90e0d0e.png)

---
- 本文作者：LiuQiang
- 版权声明：本文为作者的原创文章，转载时请务必注明出处！