---
title: PyQt5笔记15
date: 2018-07-21 15:41:40
components: true
reward: true
toc: true
tags:
	- PyQt5
---

`需求说明`：使用`PyQt5`中的`QLCDNumber`和`QSlider`基于信号和槽机制实现两者之间的通信！

`模块导入`：

- `import os`
- `import sys`
- `from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QLCDNumber, QSlider, QVBoxLayout`
- `from PyQt5.QtGui import QIcon`
- `from PyQt5.QtCore import Qt`

`完整代码`：

```python
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QLCDNumber, QSlider, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

def getCurrentPath():
    dirName, fileName = os.path.split(sys.argv[0])
    return dirName + "/"

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        lcd = QLCDNumber(self)
        slider = QSlider(Qt.Horizontal, self)
        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(slider)

        self.setLayout(vbox)
        slider.valueChanged.connect(lcd.display) #关联现有的信号和槽函数，即PyQt5自带的
        self.resize(640, 480)
        self.setWindowTitle("Signal&Slot")
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

`实例总结`：

- `from PyQt5.QtCore import Qt`导入的`Qt`模块中主要包含了`Qt5`界面开发框架中的一个全局常量和全局变量！
- `slider.valueChanged.connect(lcd.display)`关联了信号和槽函数！
  - `事件驱动模型`中有三个概念：`事件源`、`事件对象`和`事件目标`，`事件源`是其状态发生改变的对象，`事件对象`封装了来自`事件源`的`状态改变`，`事件对象`包含了诸多描述该事件的`属性`，`事件对象`特定于生成的`事件类型`。`事件源`委托`事件目标`代为处理`状态改变`这件事！

`运行效果`：

![2018-07-21 16-24-31屏幕截图.png](https://i.loli.net/2018/07/21/5b52edcab55d4.png)

---
- 本文作者：LiuQiang
- 版权声明：本文为作者的原创文章，转载时请务必注明出处！