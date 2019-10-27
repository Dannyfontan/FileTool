一个用pyqt写的工具
=========
~~具体用处未知 花了不少时间来折腾~~

*算是练手吧*
#功能介绍#
#1.遍历指定目录文件
>之前是用QT5来实现 故用的是QDirIterator 直接使用即可 不用自己手动实现遍历
>
>使用QDirIterator来遍历的好处是得到一个iterator 其包含不少信息 可以直接用方法来得到这些信息
>
><https://doc.qt.io/archives/qt-4.8/qdiriterator.html>
>
>遍历完成之后 要将信息处理并用表格形式输出 ~~这就是个头大的点~~ 文件一多就会卡住
>
>之前试过用QThread来遍历 再将遍历得到的文件信息传回主进程
>
> 但是文件数目过多时还是有卡顿的问题

#2.搜索文件
>全局的文件搜索 实现方式和遍历一致 无奈技术有限 代码无法复用
>
>从遍历结果中来搜索文件就是遍历列表 ~~太low了~~
>
>至于模糊搜索 用的是fuzzy-wuzzy这个模块
>
><https://github.com/seatgeek/fuzzywuzzy>
#函数#
#1.slot_selectBut
>选择按钮对应的槽函数
>
>用的是QtWidgets.QFileDialog.getExistingDirectory()这个方法来弹出文件选择对话框

#2.slot_confirmBut
>确认按钮对应的槽函数 正常情况下开始遍历

#3.slot_searchBut
>搜索按钮对应的槽函数 根据框中的选项来确定搜索方式和搜索范围

#4.set_table_format & set_table_size
>前者把表格头设置好 后者根据勾选的输出格式 确定遍历后的输出格式
>
>根据勾选情况 将输出格式自编号 调用后返回 供遍历函数使用 ~~真的low~~

#5.formatsize
>将文件大小转化为KB/MB/GB 数学方法

#6.getFileMd5
>计算MD5值 用的是python的hashlib

#7.search_global
>全局搜索 但是路径是默认的(可更改) 方法和遍历一致

#8.search_local
>在遍历完输出的结果中遍历 即遍历表格






