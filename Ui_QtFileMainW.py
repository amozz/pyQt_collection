# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Doc\my nuts\code\python\GUI\QtFile\QtFileMainW.ui'
#
# Created: Wed Feb 08 17:24:57 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(302, 340)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.openFile = QtGui.QPushButton(self.centralWidget)
        self.openFile.setGeometry(QtCore.QRect(210, 20, 75, 23))
        self.openFile.setText(QtGui.QApplication.translate("MainWindow", "打开文件", None, QtGui.QApplication.UnicodeUTF8))
        self.openFile.setObjectName(_fromUtf8("openFile"))
        self.searchStr = QtGui.QPlainTextEdit(self.centralWidget)
        self.searchStr.setGeometry(QtCore.QRect(20, 80, 261, 51))
        self.searchStr.setObjectName(_fromUtf8("searchStr"))
        self.replacedStr = QtGui.QPlainTextEdit(self.centralWidget)
        self.replacedStr.setGeometry(QtCore.QRect(20, 170, 261, 51))
        self.replacedStr.setObjectName(_fromUtf8("replacedStr"))
        self.withreplace = QtGui.QCheckBox(self.centralWidget)
        self.withreplace.setGeometry(QtCore.QRect(20, 150, 72, 17))
        self.withreplace.setText(QtGui.QApplication.translate("MainWindow", "替换为", None, QtGui.QApplication.UnicodeUTF8))
        self.withreplace.setObjectName(_fromUtf8("withreplace"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(20, 60, 81, 16))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "查找的字符串", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.fileName = QtGui.QLineEdit(self.centralWidget)
        self.fileName.setGeometry(QtCore.QRect(20, 20, 181, 21))
        self.fileName.setObjectName(_fromUtf8("fileName"))
        self.process = QtGui.QPushButton(self.centralWidget)
        self.process.setGeometry(QtCore.QRect(20, 240, 75, 23))
        self.process.setText(QtGui.QApplication.translate("MainWindow", "处理文件", None, QtGui.QApplication.UnicodeUTF8))
        self.process.setObjectName(_fromUtf8("process"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

