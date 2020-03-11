import sys
from PyQt5 import QtWidgets
from mywindow import MyWindow


#需要加入的功能:
#1.遍历时显示已遍历的文件个数和耗时 加入中断遍历机制
#2.大文件的MD5计算自动跳过(要是已选MD5计算的话), 用字典存储其所在行和其绝对地址, 待所有文件处理完后再处理
#3.条件查询？ 需要手动输入还是内置？ 目前仅是遍历+关键字搜索
#4.需要新增哪一些功能呢？

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())