from PyQt5 import QtCore, QtGui, QtWidgets
from fuzzywuzzy import fuzz
import os
import hashlib
import time

class MyWindow(QtWidgets.QMainWindow):
    count = 0
    size_type = 0
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setWindowTitle("Fucking Test")
        self.resize(1920, 1080)
        self.centralWidget = QtWidgets.QWidget()
        self.centralWidget.setObjectName("centralWidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(180, 10, 861, 91))
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.PathLabel = QtWidgets.QLabel(self.groupBox)
        self.PathLabel.setEnabled(True)
        self.PathLabel.setMinimumSize(QtCore.QSize(86, 55))
        self.PathLabel.setObjectName("PathLabel")
        self.horizontalLayout.addWidget(self.PathLabel)
        self.PathText = QtWidgets.QLineEdit(self.groupBox)
        self.PathText.setObjectName("PathText")
        self.horizontalLayout.addWidget(self.PathText)
        self.selectBut = QtWidgets.QPushButton(self.groupBox)
        self.selectBut.setObjectName("selectBut")
        self.horizontalLayout.addWidget(self.selectBut)
        self.confirmBut = QtWidgets.QPushButton(self.groupBox)
        self.confirmBut.setObjectName("confirmBut")
        self.horizontalLayout.addWidget(self.confirmBut)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_2.setGeometry(QtCore.QRect(180, 100, 861, 69))
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.nameChk = QtWidgets.QCheckBox(self.groupBox_2)
        self.nameChk.setObjectName("nameChk")
        self.horizontalLayout_2.addWidget(self.nameChk)
        self.pathChk = QtWidgets.QCheckBox(self.groupBox_2)
        self.pathChk.setObjectName("pathChk")
        self.horizontalLayout_2.addWidget(self.pathChk)
        self.sizeChk = QtWidgets.QCheckBox(self.groupBox_2)
        self.sizeChk.setObjectName("sizeChk")
        self.horizontalLayout_2.addWidget(self.sizeChk)
        self.typeChk = QtWidgets.QCheckBox(self.groupBox_2)
        self.typeChk.setObjectName("typeChk")
        self.horizontalLayout_2.addWidget(self.typeChk)
        self.timeChk = QtWidgets.QCheckBox(self.groupBox_2)
        self.timeChk.setObjectName("timeChk")
        self.horizontalLayout_2.addWidget(self.timeChk)
        self.md5Chk = QtWidgets.QCheckBox(self.groupBox_2)
        self.md5Chk.setObjectName("md5Chk")
        self.horizontalLayout_2.addWidget(self.md5Chk)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_4.setGeometry(QtCore.QRect(1060, 10, 651, 91))
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.comboBox_type = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_type.setObjectName("comboBox_type")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_area = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_area.setObjectName("comboBox_area")
        self.comboBox_area.addItem("")
        self.comboBox_area.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_type)
        self.horizontalLayout_3.addWidget(self.comboBox_area)
        self.searchBut = QtWidgets.QPushButton(self.groupBox_4)
        self.searchBut.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.searchBut)
        self.tableWidget = QtWidgets.QTableWidget(self.centralWidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 180, 1920, 830))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.progressBar = QtWidgets.QProgressBar(self.centralWidget)
        self.progressBar.setGeometry(QtCore.QRect(1060, 127, 651, 43))
        self.progressBar.setObjectName("progressBar")
        self.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar()
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1920, 28))
        self.menuBar.setObjectName("menuBar")
        self.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(self)
        self.mainToolBar.setObjectName("mainToolBar")
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(self)
        self.statusBar.setObjectName("statusBar")
        self.setStatusBar(self.statusBar)
        

        self.groupBox.setTitle("遍历文件夹")
        self.PathLabel.setText("选择或输入路径")
        self.selectBut.setText("选择")
        self.confirmBut.setText("确认")
        self.groupBox_2.setTitle("选择输出格式")
        self.nameChk.setText("文件名")
        self.pathChk.setText("路径")
        self.sizeChk.setText("大小")
        self.typeChk.setText("类型")
        self.timeChk.setText("修改时间")
        self.md5Chk.setText("Md5")
        self.groupBox_4.setTitle("搜索")
        self.label.setText("输入文件名")
        self.comboBox_type.setItemText(0, "精确搜索")
        self.comboBox_type.setItemText(1, "模糊搜索")
        self.comboBox_area.setItemText(0, "全局搜索")
        self.comboBox_area.setItemText(1, "结果中搜索")
        self.searchBut.setText("搜索")

        #各组件状态的设定
        self.PathText.setClearButtonEnabled(True)
        self.lineEdit.setClearButtonEnabled(True)
        self.progressBar.setRange(0,100)
        self.progressBar.setValue(0)
        self.nameChk.setChecked(True)
        self.nameChk.setDisabled(True)
        self.pathChk.setChecked(True)
        self.pathChk.setDisabled(True)
        self.sizeChk.setChecked(True)
        self.sizeChk.setDisabled(True)
        self.typeChk.setChecked(True)
        self.typeChk.setDisabled(True)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        
        #按钮绑定槽函数
        self.selectBut.clicked.connect(self.slot_selectBut)
        self.confirmBut.clicked.connect(self.slot_confirmBut)
        self.searchBut.clicked.connect(self.slot_searchBut)

    #槽函数
    def slot_selectBut(self):                   #选择按钮的槽函数
            self.PathText.clear()
            self.tableWidget.clearContents()
            selectedDir = QtWidgets.QFileDialog.getExistingDirectory(self,'选择文件夹','D:\\')
            
            if selectedDir:
                self.PathText.insert(selectedDir)
            
    def slot_confirmBut(self):                  #确认按钮的槽函数
        self.confirmBut.setDisabled(True)
        self.searchBut.setDisabled(True)
        path = self.PathText.text()             #获得框中的路径
        
        if(not path):
            QtWidgets.QMessageBox.warning(self, 'Error', '请输入或选择路径')
            self.confirmBut.setDisabled(False)
            self.searchBut.setDisabled(False)
            return

        if not os.path.exists(path):
            QtWidgets.QMessageBox.critical(self, 'Error', '路径不存在')
            self.confirmBut.setDisabled(False)
            self.searchBut.setDisabled(False)
            return

        count = 0
        self.progressBar.setValue(0)
        size_type =  self.set_table_size()
        self.progressBar.setMinimum(0)          #让进度条滚动
        self.progressBar.setMaximum(0)  

        iter = QtCore.QDirIterator(path, QtCore.QDir.Files | QtCore.QDir.CaseSensitive | QtCore.QDir.NoDotAndDotDot, QtCore.QDirIterator.Subdirectories)
        #starttime = QtCore.QTime.currentTime()
        
        while(iter.hasNext()):
            iter.next()
            self.tableWidget.insertRow(count)
            self.tableWidget.setItem(count, 0, QtWidgets.QTableWidgetItem(iter.fileInfo().fileName()))
            self.tableWidget.setItem(count, 1, QtWidgets.QTableWidgetItem(iter.fileInfo().absoluteFilePath()))
            self.tableWidget.setItem(count, 2, QtWidgets.QTableWidgetItem(self.formatsize(iter.fileInfo().size())))
            self.tableWidget.setItem(count, 3, QtWidgets.QTableWidgetItem(iter.fileInfo().suffix()))
        
            if(size_type == 2):
                absolu_path = iter.fileInfo().absoluteFilePath()
                self.tableWidget.setItem(count, 4, QtWidgets.QTableWidgetItem(self.getFileMd5(absolu_path)))

            elif(size_type == 3):
               self.tableWidget.setItem(count, 4, QtWidgets.QTableWidgetItem(iter.fileInfo().created().toString("yyyy-MM-dd hh:mm:ss")))
            
            elif(size_type == 4): 
                absolu_path = iter.fileInfo().absoluteFilePath()
                self.tableWidget.setItem(count, 4, QtWidgets.QTableWidgetItem(iter.fileInfo().created().toString("yyyy-MM-dd hh:mm:ss")))
                self.tableWidget.setItem(count, 5, QtWidgets.QTableWidgetItem(self.getFileMd5(absolu_path)))

            elif(size_type == 1):
                pass

            else:
                QtWidgets.QMessageBox.warning(self, 'Error', '选择的类型错误')
            count = count + 1
            QtWidgets.QApplication.processEvents()
            #TODO:
            #endtime = QtCore.QTime.currentTime()
            #diff = starttime.msecsTo(endtime)

        self.progressBar.setMaximum(100)                        #停止滚动
        self.progressBar.setValue(100)
        self.confirmBut.setDisabled(False)
        self.searchBut.setDisabled(False)

    def slot_searchBut(self):                                  #搜索键的槽函数
        match_type = self.comboBox_type.currentIndex()
        search_type =self.comboBox_area.currentIndex()
        filename = self.lineEdit.text()
        
        if(not self.lineEdit.text()):
            QtWidgets.QMessageBox.warning(self, 'Error', '文件名有误')
            return

        if(search_type == 0):
            self.searchBut.setDisabled(True)
            self.search_global(filename, match_type)
            self.searchBut.setDisabled(False)

        elif(search_type == 1):
            self.searchBut.setDisabled(True)
            self.search_local(filename, match_type)
            self.searchBut.setDisabled(False)

        else:
            QtWidgets.QMessageBox.critical(self, 'Error', '搜索方式有问题')
            return

    def set_table_format(self, columnTitles):                   #设定表头
        self.tableWidget.setHorizontalHeaderLabels(columnTitles)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Interactive)
    
    def set_table_size(self):                                   #根据勾选项确定输出格式
        if(self.md5Chk.isChecked() and not self.timeChk.isChecked()):
            self.tableWidget.setRowCount(0)
            self.tableWidget.setColumnCount(5)
            columnTitles = ['Name', 'Path', 'Size', 'Type','Md5']
            self.set_table_format(columnTitles)        
            return 2

        elif(self.timeChk.isChecked() and not self.md5Chk.isChecked()):
            self.tableWidget.setRowCount(0)
            self.tableWidget.setColumnCount(5)
            columnTitles = ['Name', 'Path', 'Size', 'Type', 'Time']
            self.set_table_format(columnTitles)
            return 3

        elif(self.md5Chk.isChecked() and self.timeChk.isChecked()):
            self.tableWidget.setRowCount(0)
            self.tableWidget.setColumnCount(6)
            columnTitles = ['Name', 'Path', 'Size', 'Type', 'Time', 'Md5']
            self.set_table_format(columnTitles)
            return 4

        else:
            self.tableWidget.setRowCount(0)
            self.tableWidget.setColumnCount(4)
            columnTitles = ['Name', 'Path', 'Size', 'Type']
            self.set_table_format(columnTitles)
            return 1
    
    def formatsize(self, size):                         #将文件大小格式化
        size = int(size)
        if(size < 1024):
            res = str(size) + 'b'

        elif(size >= 1024 and size < 1048576):
            size /= 1024
            size = round(size, 2)
            res = str(size) + 'kb'

        elif(size >= 1048576 and size < 1048576 * 1024):
            size /= 1024
            size /= 1024
            size = round(size, 2)
            res = str(size) + 'MB'

        else:
            size /= 1024
            size /= 1024
            size /= 1024
            size = round(size, 2)
            res = str(size) + 'GB'
        return res
    
    def getFileMd5(self,path):                              #计算MD5
        if not os.path.exists(path):
            QtWidgets.QMessageBox.critical(self, 'Error', '文件不存在')
            return "file does not exist"

        hash = hashlib.md5()
        f = open(path, 'rb')
        while True:
            b = f.read(8096)
            if not b:
                break
            hash.update(b)
        f.close()
        return hash.hexdigest() 

    def search_global(self, filename, match_type):              #全局搜索
        default_path = 'D:\\'
        count = 0
        size_type = self.set_table_size()
        self.progressBar.setValue(0)
        self.searchBut.setDisabled(True)
        self.confirmBut.setDisabled(True) 
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(0)
        file_found = False

        iter = QtCore.QDirIterator(default_path, QtCore.QDir.Files | QtCore.QDir.CaseSensitive | QtCore.QDir.NoDotAndDotDot, QtCore.QDirIterator.Subdirectories)
        
        while(iter.hasNext()):
            iter.next()
            if( ((match_type == 0) and (filename == iter.fileInfo().fileName())) or ( (match_type == 1) and (fuzz.partial_ratio(filename, iter.fileInfo().fileName()) >= 90) ) ):
                self.tableWidget.insertRow(count)
                file_found = True
                self.tableWidget.setItem(count, 0, QtWidgets.QTableWidgetItem(iter.fileInfo().fileName()))
                self.tableWidget.setItem(count, 1, QtWidgets.QTableWidgetItem(iter.fileInfo().absoluteFilePath()))
                self.tableWidget.setItem(count, 2, QtWidgets.QTableWidgetItem(self.formatsize(iter.fileInfo().size())))
                self.tableWidget.setItem(count, 3, QtWidgets.QTableWidgetItem(iter.fileInfo().suffix()))

                if(size_type == 2): 
                    absolu_path = iter.fileInfo().absoluteFilePath()
                    self.tableWidget.setItem(count, 4, QtWidgets.QTableWidgetItem(self.getFileMd5(absolu_path)))
                
                elif(size_type == 3):
                    self.tableWidget.setItem(count, 4, QtWidgets.QTableWidgetItem(iter.fileInfo().created().toString("yyyy-MM-dd hh:mm:ss")))
                
                elif(size_type == 4): 
                    absolu_path = iter.fileInfo().absoluteFilePath()
                    self.tableWidget.setItem(count, 4, QtWidgets.QTableWidgetItem(iter.fileInfo().created().toString("yyyy-MM-dd hh:mm:ss")))
                    self.tableWidget.setItem(count, 5, QtWidgets.QTableWidgetItem(self.getFileMd5(absolu_path)))
                
                elif(size_type == 1):
                    pass

                else:
                    QtWidgets.QMessageBox.warning(self, 'Error', 'Error in size type')
                
                count = count + 1
                QtWidgets.QApplication.processEvents()

        if(not file_found):
            QtWidgets.QMessageBox.warning(self, 'Warning', 'can\'t find file')

        self.progressBar.setMaximum(100)            
        self.progressBar.setValue(100)
        self.searchBut.setDisabled(False) 
        self.confirmBut.setDisabled(False) 
        
    def search_local(self, filename, match_type):           #在已有的结果中搜索
        rowCount = self.tableWidget.rowCount()
        colCount = self.tableWidget.columnCount()
        
        if(rowCount == 0):
            QtWidgets.QMessageBox.warning(self, 'Error', '当前结果为空')
            return
        
        count = 0
        self.progressBar.setValue(0)
        self.searchBut.setDisabled(True)
        self.confirmBut.setDisabled(True)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(0)
        file_found = False

        for i in range(rowCount):
            if( ((match_type == 0) and (filename == self.tableWidget.item(i, 0).text())) or ( (match_type == 1) and (fuzz.partial_ratio(filename, self.tableWidget.item(i, 0).text()) >= 90) ) ):
                file_found = True
                for j in range(colCount):
                    self.tableWidget.setItem(count, j, QtWidgets.QTableWidgetItem(self.tableWidget.item(i, j).text()))
                count = count + 1
        
        for j in range(rowCount - count):
            self.tableWidget.removeRow(count)

        if(not file_found):
            QtWidgets.QMessageBox.warning(self, 'Error', '未找到文件')
        
        self.progressBar.setMaximum(100)            
        self.progressBar.setValue(100)
        self.searchBut.setDisabled(False) 
        self.confirmBut.setDisabled(False)