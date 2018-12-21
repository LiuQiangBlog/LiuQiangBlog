---
title: PyQt5笔记13
date: 2018-07-21 13:22:05
components: true
reward: true
toc: true
tags:
	- PyQt5
---

`需求说明`：使用`PyQt5`中的`QGridLayout`、`QLineEdit`、`QPushButton`和`Qt`实现一个简单的计算器！

`模块导入`：

- `import os`
- `import sys`
- `from math import sqrt`
- `from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QPushButton, QGridLayout, QLineEdit`
- `from PyQt5.QtGui import QIcon`
- `from PyQt5.QtCore import Qt`

`完整代码`：

```python
import os
import sys
from math import sqrt
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QPushButton, QGridLayout, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

number = 0.0
newNumber = 0.0
sumIterate = 0.0
sumAll = 0.0
operator = ""
opVar = False

def getCurrentPath():
    dirName, fileName = os.path.split(sys.argv[0])
    return dirName + "/"

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        Grid = QGridLayout()
        self.setLayout(Grid)

        self.Display = QLineEdit("12345", self)
        self.Display.setReadOnly(True)
        self.Display.setAlignment(Qt.AlignRight)

        Clear = QPushButton("Clear", self)
        BackSpace = QPushButton("Back", self)
        
        One = QPushButton("1", self)
        Two = QPushButton("2", self)
        Three = QPushButton("3", self)
        Four = QPushButton("4", self)
        Five = QPushButton("5", self)
        Six = QPushButton("6", self)
        Seven = QPushButton("7", self)
        Eight = QPushButton("8", self)
        Nine = QPushButton("9", self)
        Zero = QPushButton("0", self)

        Point = QPushButton(".", self)

        Plus = QPushButton("+", self)
        Minus = QPushButton("-", self)
        Multiply = QPushButton("*", self)
        Divide = QPushButton("/", self)
        Equal = QPushButton("=", self)
        Square = QPushButton("x²")
        Root = QPushButton("√", self)

        numbers = [One, Two, Three, Four, Five, Six, Seven, Eight, Nine, Zero]
        operators = [BackSpace, Clear, Plus, Minus, Multiply, Divide, Equal]
        others = [Square, Root, Point]

        for i in numbers:
            i.setStyleSheet("color: blue;")
            i.clicked.connect(self.numbers)
        
        for i in operators:
            i.setStyleSheet("color: darkviolet;")
        
        for i in operators[:2]:
            if i == BackSpace:
                i.clicked.connect(self.back)
            
            elif i == Clear:
                i.clicked.connect(self.clc)
        
        for i in operators[2:]:
            i.clicked.connect(self.operate)
        
        for i in others:
            i.setStyleSheet("color: red;")
            if i == Square:
                i.clicked.connect(self.squares)
            elif i == Root:
                i.clicked.connect(self.roots)
            elif i == Point:
                i.clicked.connect(self.points)

        names = [Square, Root, Clear, BackSpace,
                 Seven, Eight, Nine, Divide,
                 Four, Five, Six, Multiply,
                 One, Two, Three, Plus,
                 Zero, Point, Equal, Minus]
        positions = [(i+1, j) for i in range(5) for j in range(4)]
        Grid.addWidget(self.Display, 0, 0, 1, 4)
        for position, name in zip(positions, names):
            Grid.addWidget(name, *position)
        #     if name == "": #执行下一次循环迭代
        #         continue
        #     button = QPushButton(name) #button变量不断地绑定到不同的按钮对象上
        #     Grid.addWidget(button, *position) #因为*position才表示一个元组

        self.resize(300, 150)
        self.setWindowTitle("Simple Calculator")
        self.dirPath = getCurrentPath()
        self.setWindowIcon(QIcon(self.dirPath + "ico.png"))
        self.center()
        self.show()

    def center(self):
        Rect = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        Rect.moveCenter(cp)
        self.move(Rect.topLeft())
    
    def numbers(self):
        global number
        global newNumber
        global opVar
        sender = self.sender()
        newNumber = int(sender.text())
        if opVar == False:
            self.Display.setText(self.Display.text() + str(newNumber))
        else:
            self.Display.setText(str(newNumber))
            opVar = False
        
    def operate(self):
        global sumIterate
        global number
        global opVar
        global operator

        sumIterate += 1
        if sumIterate > 1:
            self.equals()
        
        number = self.Display.text()
        sender = self.sender()
        operator = sender.text()
        if operator == "+":
            self.Display.setText(self.Display.text() + "+")     

        opVar = True
    
    def equals(self):
        global sumIterate
        global sumAll
        global number
        global newNumber
        global operator
        global opVar

        sumIterate = 0.0
        newNumber = float(self.Display.text())
        if operator == "+":
            sumAll = float(number) + newNumber
        elif operator == "-":
            sumAll = float(number) - newNumber
        elif operator == "*":
            sumAll = float(number) * newNumber
        elif operator == "/":
            sumAll = float(number) / newNumber
        self.Display.setText(str(sumAll))
        opVar = True
    
    def roots(self):
        global number
        number = float(self.Display.text())
        number = sqrt(number)
        self.Display.setText(str(number))
    
    def squares(self):
        global number
        number = float(self.Display.text())
        number = number**2
        self.Display.setText(str(number))
    
    def points(self):
        if "." not in self.Display.text():
            self.Display.setText(self.Display.text() + ".")
    
    def back(self):
        self.Display.backspace()
    
    def clc(self):
        global number
        global newNumber
        global sumAll
        global operator

        self.Display.clear()
        number = 0.0
        newNumber = 0.0
        sumAll = 0.0
        operator = ""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    sys.exit(app.exec_())
```

`实验总结`：

- `QGridLayout`在实现类似计算器按键布局的网格布局功能方面很容易实现！
- 本实例实现的计算器功能非常有限，最好是使用`正则表达式`来提取`QLineEdit`中的`文本内容`根据数学计算优先级进行计算！

`运行效果`：

![2018-07-21 13-36-38屏幕截图.png](https://i.loli.net/2018/07/21/5b52c91a47264.png)

---
- 本文作者：LiuQiang
- 版权声明：本文为作者的原创文章，转载时请务必注明出处！