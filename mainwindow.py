# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
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
        self.comboBox = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.tableWidget = QtWidgets.QTableWidget(self.centralWidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 180, 1920, 830))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.progressBar = QtWidgets.QProgressBar(self.centralWidget)
        self.progressBar.setGeometry(QtCore.QRect(1060, 127, 651, 43))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1920, 28))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        #slot func connect
        self.selectBut.clicked.connect(self.slot_selectBut)
        self.confirmBut.clicked.connect(self.slot_confirmBut)

        self.PathText.setClearButtonEnabled(True)
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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "list out"))
        self.PathLabel.setText(_translate("MainWindow", "Keyin file name"))
        self.selectBut.setText(_translate("MainWindow", "select"))
        self.confirmBut.setText(_translate("MainWindow", "confirm"))
        self.groupBox_2.setTitle(_translate("MainWindow", "choce the out type"))
        self.nameChk.setText(_translate("MainWindow", "Name"))
        self.pathChk.setText(_translate("MainWindow", "Path"))
        self.sizeChk.setText(_translate("MainWindow", "Size"))
        self.typeChk.setText(_translate("MainWindow", "Type"))
        self.timeChk.setText(_translate("MainWindow", "Time"))
        self.md5Chk.setText(_translate("MainWindow", "Md5"))
        self.groupBox_4.setTitle(_translate("MainWindow", "search"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.comboBox.setItemText(0, _translate("MainWindow", "a"))
        self.comboBox.setItemText(1, _translate("MainWindow", "b"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))

    #define slot function
    def slot_selectBut(self):
        self.PathText.clear()
        self.tableWidget.clearContents()
        selectedDir = QFileDialog.getExistingDirectory(self,'选择文件夹','D:\\')
        if selectedDir:
            self.PathText.insert(selectedDir)

    def slot_confirmBut(self):
        content = self.PathText.text()
        size_type = self.set_table_size()
        if(not content):
            QtWidgets.QMessageBox.warning(self, 'Warning', 'Error in selecting path')
        if(size_type == 1):
            self.browse_one()
        elif(size_type == 2):
            self.browse_two()
        elif(size_type == 3):
            self.browse_three()
        elif(size_type == 4):
            print('4')

    #other functions
    def set_table_size(self):
        if(self.md5Chk.isChecked() and not self.timeChk.isChecked()):
            self.tableWidget.setRowCount(700)
            self.tableWidget.setColumnCount(5)
            columnTitles = ['Name', 'Path', 'Size', 'Type','Md5']
            self.tableWidget.setHorizontalHeaderLabels(columnTitles)
            self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            return 2

        elif(self.timeChk.isChecked() and not self.md5Chk.isChecked()):
            self.tableWidget.setRowCount(700)
            self.tableWidget.setColumnCount(5)
            columnTitles = ['Name', 'Path', 'Size', 'Type', 'Time']
            self.tableWidget.setHorizontalHeaderLabels(columnTitles)
            self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            return 3

        elif(self.md5Chk.isChecked() and self.timeChk.isChecked()):
            self.tableWidget.setRowCount(700)
            self.tableWidget.setColumnCount(6)
            columnTitles = ['Name', 'Path', 'Size', 'Type', 'Time', 'Md5']
            self.tableWidget.setHorizontalHeaderLabels(columnTitles)
            self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            return 4

        else:
            self.tableWidget.setRowCount(700)
            self.tableWidget.setColumnCount(4)
            columnTitles = ['Name', 'Path', 'Size', 'Type']
            self.tableWidget.setHorizontalHeaderLabels(columnTitles)
            self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            return 1

    def formatsize(self, size):
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

    def getFileMd5(self,path):
        localFile = QtCore.QFile(path)
        if(not localFile.open(QtCore.QFile.ReadOnly)):
            QtWidgets.QMessageBox.warning(self,'Warning','Error in opening file')
            return 'Error'
        ch = QtCore.QCryptographicHash(QtCore.QCryptographicHash.Md5)
        totalBytes = localFile.size()
        bytesWritten = 0
        bytesToWrite = totalBytes
        loadSize = 1024 * 4
        buf = QtCore.QByteArray()
        
        while(True):
            if(bytesToWrite > 0):
                buf = QtCore.QByteArray(localFile.read(min(bytesToWrite, loadSize)))
                ch.addData(buf)
                bytesWritten = bytesWritten + buf.length()
                bytesToWrite = bytesToWrite - buf.length()
                buf.resize(0)
            else:
                break
            if(bytesWritten == totalBytes):
                break
        
        localFile.close()
        md5 = str(type(ch.result()))
        return md5

    def browse_one(self):
        count = 0
        path = self.PathText.text()
        iter = QtCore.QDirIterator(path, QtCore.QDir.Files | QtCore.QDir.CaseSensitive | QtCore.QDir.NoDotAndDotDot, QtCore.QDirIterator.Subdirectories)
        while(iter.hasNext()):
            iter.next()
            file_info = iter.fileInfo()
            self.tableWidget.setItem(count,0,QtWidgets.QTableWidgetItem(file_info.fileName()))
            self.tableWidget.setItem(count, 1, QtWidgets.QTableWidgetItem(file_info.absoluteFilePath()))
            self.tableWidget.setItem(count, 2, QtWidgets.QTableWidgetItem(self.formatsize(file_info.size())))
            self.tableWidget.setItem(count, 3, QtWidgets.QTableWidgetItem(file_info.suffix()))
            count = count + 1

    def browse_two(self):
        count = 0
        path = self.PathText.text()
        iter = QtCore.QDirIterator(path, QtCore.QDir.Files | QtCore.QDir.CaseSensitive | QtCore.QDir.NoDotAndDotDot, QtCore.QDirIterator.Subdirectories)
        while(iter.hasNext()):
            iter.next()
            file_info = iter.fileInfo()
            absolu_path = file_info.absoluteFilePath()
            self.tableWidget.setItem(count,0,QtWidgets.QTableWidgetItem(file_info.fileName()))
            self.tableWidget.setItem(count, 1, QtWidgets.QTableWidgetItem(file_info.absoluteFilePath()))
            self.tableWidget.setItem(count, 2, QtWidgets.QTableWidgetItem(self.formatsize(file_info.size())))
            self.tableWidget.setItem(count, 3, QtWidgets.QTableWidgetItem(file_info.suffix()))
            self.tableWidget.setItem(count, 4, QtWidgets.QTableWidgetItem(self.getFileMd5(absolu_path)))
            count = count + 1

    def browse_three(self):
        count = 0
        path = self.PathText.text()
        iter = QtCore.QDirIterator(path, QtCore.QDir.Files | QtCore.QDir.CaseSensitive | QtCore.QDir.NoDotAndDotDot, QtCore.QDirIterator.Subdirectories)
        while(iter.hasNext()):
            iter.next()
            file_info = iter.fileInfo()
            self.tableWidget.setItem(count,0,QtWidgets.QTableWidgetItem(file_info.fileName()))
            self.tableWidget.setItem(count, 1, QtWidgets.QTableWidgetItem(file_info.absoluteFilePath()))
            self.tableWidget.setItem(count, 2, QtWidgets.QTableWidgetItem(self.formatsize(file_info.size())))
            self.tableWidget.setItem(count, 3, QtWidgets.QTableWidgetItem(file_info.suffix()))
            self.tableWidget.setItem(count, 4, QtWidgets.QTableWidgetItem(file_info.created().toString("yyyy-MM-dd hh:mm:ss")))
            count = count + 1