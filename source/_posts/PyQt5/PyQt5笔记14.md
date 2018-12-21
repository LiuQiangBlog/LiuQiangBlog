---
title: PyQt5笔记14
date: 2018-07-21 13:51:38
components: true
reward: true
toc: true
tags:
	- PyQt5
---

`需求说明`：使用`PyQt5`中的`QGridLayout`实现多中类型的窗口部件的布局！

`模块导入`：

- `import os`
- `import sys`
- `from PyQt5.QtWidgets import QWidget, QDesktopWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication, QPushButton`
- `from PyQt5.QtGui import QIcon`

`完整代码`：

```python
import os
import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication, QPushButton
from PyQt5.QtGui import QIcon
def getCurrentPath():
    dirName, fileName = os.path.split(sys.argv[0])
    return dirName + "/"

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        title = QLabel('&Title')
        titleEdit = QLineEdit()
        title.setBuddy(titleEdit)

        author = QLabel('&Author')
        authorEdit = QLineEdit()
        author.setBuddy(authorEdit)

        description = QLabel('&Description')
        descriptionEdit = QTextEdit()
        description.setBuddy(descriptionEdit)

        ok = QPushButton("OK")
        cancel = QPushButton("Cancel")
        cancel.clicked.connect(self.close)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 0, 0, 1, 1)
        grid.addWidget(titleEdit, 0, 1, 1, 3)

        grid.addWidget(author, 1, 0, 1, 1)
        grid.addWidget(authorEdit, 1, 1, 1, 3)

        grid.addWidget(description, 2, 0, 1, 1)
        grid.addWidget(descriptionEdit, 2, 1, 5, 3) # 行的跨度为5，列的跨度为1
        # QGridLayout::addWidget(QWidget *widget,\
        #                        int fromRow,\ #行起始位置
        #                        int fromColumn,\ #列起始位置
        #                        int rowSpan,\
        #                        int columnSpan,\
        #                        Qt::Alignment alignment = ...)
        grid.addWidget(ok, 8, 2, 1, 1) # 2+5+1 = 8
        grid.addWidget(cancel, 8, 3, 1, 1)
        self.setLayout(grid) 
        
        self.resize(350, 300)
        self.setWindowTitle('Books') 
        self.setWindowIcon(QIcon(getCurrentPath() + "ico.png"))   
        self.center()
        self.show()
    
    def center(self):
        Rect = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        Rect.moveCenter(cp)
        self.move(Rect.topLeft())
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

`实例总结`：

- `QGridLayout`是窗口控件的布局管理中应用最为广泛的，我们需要熟练使用，主要用到5个参数，第1个参数是被布局的控件对象，第2个参数是控件在窗口界面中的行的起始位置，第3个参数是控件在窗口界面中的列起始位置，第4个参数是当前被布局的控件需要跨越多少行，第5个参数是当前被布局的控件需要跨越多少列！
- 需要注意的是`QGridLayout`函数的第2、3个参数的起始值为0而不是1！

`运行效果`：

![2018-07-21 15-29-07屏幕截图.png](https://i.loli.net/2018/07/21/5b52e0cb9ed92.png)

---
- 本文作者：LiuQiang
- 版权声明：本文为作者的原创文章，转载时请务必注明出处！