# -*- coding: utf-8 -*-

"""
Module implementing QtFileMainWindow.
"""
import PyQt4,  PyQt4.QtGui
import sys,  fileinput, codecs
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature

from Ui_QtFileMainW import Ui_MainWindow

def replaceAll(file, searchStr, replaceStr):
    # the file must be in UTF-8 format
    for line in fileinput.input(file, inplace=1):
        if searchStr in unicode(line, 'utf-8'):
            #line = line.replace(searchStr, replaceStr)
            line = unicode(line, 'utf-8')
            line = line.replace(searchStr, replaceStr)            
            line = line.encode('utf-8')
        sys.stdout.write(line)

class QtFileMainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        #self.process.setEnabled(False)
        self.replacedStr.setEnabled(False)
        self.isreplace = False
        self.hasfilename = False

    
    @pyqtSignature("")
    def on_openFile_clicked(self):
        """
        Slot documentation goes here.
        """
        
        dlg = PyQt4.QtGui.QFileDialog(self)
        self.filename = dlg.getOpenFileName()
        self.hasfilename = True
        from os.path import isfile
        if isfile(unicode(self.filename)):
            self.fileName.setText(self.filename)
    
    @pyqtSignature("bool")
    def on_withreplace_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        
        if checked:
            self.replacedStr.setEnabled(True)
            self.isreplace = True
        else:
            self.replacedStr.setEnabled(False)
            self.isreplace = False
        
    @pyqtSignature("")
    def on_process_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.hasfilename:
            if self.isreplace:
                replaceAll(unicode(self.filename),  unicode(self.searchStr.toPlainText()),  unicode(self.replacedStr.toPlainText()))
            else:            
                replaceAll(unicode(self.filename),  unicode(self.searchStr.toPlainText()),  "")
            PyQt4.QtGui.QMessageBox.about(self, "", "%s" % u"处理完成")
        else:
            PyQt4.QtGui.QMessageBox.about(self, "", "%s" %  u'请输入文件名及要查找的字符串')
            


if __name__ == "__main__":
    app = PyQt4.QtGui.QApplication(sys.argv)
    myapp = QtFileMainWindow()
    myapp.show()
    
sys.exit(app.exec_())
    

