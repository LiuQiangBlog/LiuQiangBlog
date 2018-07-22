---
title: PyQt5笔记01
date: 2018-07-20 17:49:11
components: true
reward: true
toc: true
tags:
	- PyQt5
---

### 创建一个简单的窗口程序

`需求说明`：使用`PyQt5`中的`QApplication`和`QWidget`实现一个简单的界面应用程序！

`模块导入`：

- `import sys`
- `from PyQt5.QtWidgets import QApplication, QWidget`

`完整代码`：

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget
if __name__ == "__main__":
    app = QApplication(sys.argv) #创建一个应用程序对象，用于管理和响应窗口系统的资源
    window = QWidget() #创建一个窗口对象
    window.resize(640, 480) #设置窗口界面的尺寸大小，单位是像素（pixel）
    window.move(600, 200) #移动窗口的左上定点到屏幕的指定位置，默认是在窗口的（0,0）位置
    window.setWindowTitle("Simple Window") #设置窗口的标题
    window.show() #显式窗口，默认窗口是关闭的
    # sys.exit()函数确保了界面应用程序完整干净的退出过程
    # 当我们调用exit()方法或者关闭主窗口时，主循环会被终止
    sys.exit(app.exec_()) #进入应用程序主循环，主循环从窗口系统接收事件并匹配到特定的窗口部件上
```

`实例总结`：

- 这是基于`PyQt5`界面编程中的`Hello World`，非常的简单，虽然只有简单的12行代码，但是却非常的重要，因为这是开发界面应用程序的基础，其他功能丰富的界面应用程序是在此基础之上不断添加更多功能实现的。

`运行效果`：

![2018-07-20 19-13-55屏幕截图.png](https://i.loli.net/2018/07/20/5b51c428ab2b7.png)

---

- 本文作者：LiuQiang
- 版权声明：本文为作者的原创文章，转载时请务必注明出处！