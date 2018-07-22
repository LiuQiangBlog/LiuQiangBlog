---
title: PyQt5笔记05
date: 2018-07-20 20:12:20
components: true
reward: true
toc: true
tags:
	- PyQt5
---

`需求说明`：使用`PyQt5`中的`QMessageBox`和`closeEvent`实现`[PyQt5笔记04]`中关闭窗口程序时弹出消息对话框，并根据用户的选择来判断是否最终关闭窗口！

`模块导入`：

- `import os`
- `import sys`
- `from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, qApp, QMessageBox`
- `from PyQt5.QtGui import QIcon, QFont`

`完整代码`：

```python
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox, qApp
from PyQt5.QtGui import QIcon, QFont, QFontDatabase

def getCurrentPath():
    dirName, fileName = os.path.split(sys.argv[0])
    return dirName + "/"

# def getAvaliableFont():
#     fontDatabase = QFontDatabase()
#     fontFamilies = fontDatabase.families() #直接返回的是当前系统下的可用字体列表
#     # print(fontFamilies)
#     found = False
#     for font in fontFamilies:
#         if font == "SansSerif":
#             found = True
#     if found:
#         print("SansSerif is avaliable!")
#     else:
#         print("SansSerif is not avaliable!")

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        QToolTip.setFont(QFont("Times", 12))
        button = QPushButton("Quit", self)
        button.setToolTip("This Button is used for <b>Closing</b> the Window")
        button.resize(button.sizeHint())
        button.move(50, 50)
        # button.clicked.connect(QApplication.instance().quit)
        button.clicked.connect(qApp.quit) #注意调用槽函数没有括号，即没有quit()中的括号
        self.setGeometry(640, 480, 600, 200)
        self.setWindowTitle("Message Box")
        self.getPath = getCurrentPath()
        self.setWindowIcon(QIcon(self.getPath + "ico.png"))
        self.show()

    def closeEvent(self, event): #当我们触发关闭窗口系统的主窗口请求事件时，Qt库会自动调用该函事件处理函数
        reply = QMessageBox.question(self,\
                                     "Message", "Are you sure to quit?",\
                                     QMessageBox.Yes | QMessageBox.No | QMessageBox.Ignore,\
                                     QMessageBox.No
                                     )

        if reply == QMessageBox.Yes:
            event.accept() #等价于QEvent对象的setAccepted(True)
        else:
            event.ignore() #等价于QEvent对象的setAccepted(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    sys.exit(app.exec_())
```

`实例总结`：

- `closeEvent()`函数是一个虚函数，当我们编程是用到了该函数，一定要重新实现该事件处理函数的功能！
- `QMessageBox`是一个消息对话框类，在本例中我们调用的是静态成员函数`QMessageBox.question()`来弹出一个询问对话框供用户选择，除此之外，还有`QMessageBox.about()`, `QMessageBox.aboutQt()`, `QMessageBox.critical()`, `QMessageBox.information()`, `QMessageBox.warning()`。
- 接受关闭窗口的请求时执行函数`event.accent()`，拒绝该请求时执行函数`event.ingnore()`，沉默即拒绝！

`运行效果`：

![2018-07-20 20-47-31屏幕截图.png](https://i.loli.net/2018/07/20/5b51dd236a034.png)

---

- 本文作者：LiuQiang
- 版权声明：本文为作者的原创文章，转载时请务必注明出处！