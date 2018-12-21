---
title: PyQt5笔记12
date: 2018-07-21 11:19:17
components: true
reward: true
toc: true
tags:
	- PyQt5
---

`需求说明`：使用`PyQt5`中的`QHbxoLayout`和`QVboxLayout`实现窗口部件的布局管理！

`模块导入`：

- `import os`
- `import sys`
- `from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QPushButton, QHBoxLayout, QVBoxLayout, qApp`
- `from PyQt5.QtGui import QIcon`

`完整代码`：

```python
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QPushButton, QHBoxLayout, QVBoxLayout, QAction, qApp
from PyQt5.QtGui import QIcon

def getCurrentPath():
    dirName, fileName = os.path.split(sys.argv[0])
    return dirName + "/"

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        OkButton = QPushButton("Ok", self)
        CancelButton = QPushButton("Cancel", self)
        QuitButton = QPushButton("Quit", self)
        QuitButton.clicked.connect(self.close) #关闭窗口程序

        HBLayout = QHBoxLayout() #这里不可以指定父部件，因为self.setLayout()会管理部件之间的关系，如果此处指定父部件的话，会因为重复指定而出现问题
        HBLayout.addStretch(1) #在添加按钮之前添加Stretch会将按钮往右侧挤压
        HBLayout.addWidget(OkButton)
        HBLayout.addWidget(CancelButton)
        HBLayout.addWidget(QuitButton)
        HBLayout.addStretch(2)

        VBLayout = QVBoxLayout() 
        VBLayout.addStretch(1) #在添加水平布局之前添加Stretch会将按钮往底部挤压
        VBLayout.addLayout(HBLayout)
        VBLayout.addStretch(2)

        self.setLayout(VBLayout)

        self.resize(640, 480)
        self.setWindowTitle("Widget with Layout")
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
    window = MyWidget()
    sys.exit(app.exec_())
```

`实例总结`:

- `QVBoxLayout`、`QHBoxLayout`和` self.setLayout()`实现窗口部件相对于窗口的布局！

`运行效果`：

![2018-07-21 13-08-51屏幕截图.png](https://i.loli.net/2018/07/21/5b52bfef251b9.png)

---
- 本文作者：LiuQiang
- 版权声明：本文为作者的原创文章，转载时请务必注明出处！