---
title: PyQt5笔记06
date: 2018-07-20 21:03:45
components: true
reward: true
toc: true
tags:
	- PyQt5
---

`需求说明`：使用`PyQt5`中的`QDesktopWidget`实现`[PyQt5笔记05]`中的窗口程序处于桌面的中间位置！

`模块导入`：

- `import os`
- `import sys`
- `from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox, qApp, QDesktopWidget`
- `from PyQt5.QtGui import QIcon, QFont`

`完整代码`：

```python
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox, qApp, QDesktopWidget
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
        # button.clicked.connect(qApp.quit) #注意调用槽函数没有括号，即没有quit()中的括号
        # self.setGeometry(640, 280, 640, 480)
        self.resize(640, 480)
        self.setWindowTitle("Message Box")
        self.setWindowIcon(QIcon(getCurrentPath() + "ico.png"))
        # self.center() # 方法1
        self.center2() # 方法2
        self.show()
    
    def center(self):
        Rect = self.frameGeometry() #返回一个QRect类型的对象
        cp = QDesktopWidget().availableGeometry().center() #返回一个QPoint类型的对象
        Rect.moveCenter(cp) #将QRect类型的对象中心移动到桌面的中心，使得两个矩形的中心重合
        self.move(Rect.topLeft()) #将窗口移动到QRect类型的对象的左上角
        
    def center2(self): #第二种居中方法
        Rect2 = self.frameGeometry()
        Screen = QDesktopWidget().screenGeometry() 
        self.move((Screen.width() - Rect2.width())/2, (Screen.height() - Rect2.height())/2)

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

- 从上面实现的`center()`函数可知，要使窗口程序的界面居于操作系统桌面的中央，必须借助一个与窗口程序尺寸相同的矩形对象`Rect`，即`self.frameGeometry()`函数生成的一个中间对象！
- `Rect.moveCenter(cp)`只有矩形对象有该方法可直接调用来移动矩形的中心到指定位置！
- `self.move(Rect.topLeft())`该移动方法是以`self`部件的左上角顶点为参考点，即将窗口部件的左上角顶点移动到与之同尺寸的现正处于桌面中央的矩形的左上角顶点，最终实现窗口程序处于桌面的中心！

`运行效果`：

![2018-07-20 21-12-58屏幕截图.png](https://i.loli.net/2018/07/20/5b51dfe66bd68.png)

---

- 本文作者：LiuQiang
- 版权声明：本文为作者的原创文章，转载时请务必注明出处！