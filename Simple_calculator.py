import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QInputDialog, QLineEdit, QPushButton, QAction, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


#class App(QMainWindow):
    
class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Simple Calculator'
        self.left = 500
        self.top = 200
        self.width = 440
        self.height = 300
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        label1 = QLabel('Enter First No:', self)
        label1.setFont(QtGui.QFont('SansSerif', 15))
        label1.move(50,25)
        
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(250, 20)
        self.textbox1.resize(130,30)

        label2 = QLabel('Enter Second No:', self)
        label2.setFont(QtGui.QFont('SansSerif', 15))
        label2.move(50,85)
        
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(250, 80)
        self.textbox2.resize(130,30)

        label3 = QLabel('Result Number:', self)
        label3.setFont(QtGui.QFont('SansSerif', 15))
        label3.move(50,145)

        self.textbox3 = QLineEdit(self)
        self.textbox3.move(250, 140)
        self.textbox3.resize(130,30)

        

        add_button = QPushButton('Add', self)
        add_button.move(40,250)
        mul_button = QPushButton('Mul', self)
        mul_button.move(130,250)
        div_button = QPushButton('Div', self)
        div_button.move(230,250)
        sub_button = QPushButton('Sub', self)
        sub_button.move(320,250)
        #button.setToolTip('This is an example button')
        add_button.clicked.connect(self.added)
        mul_button.clicked.connect(self.mult)
        sub_button.clicked.connect(self.subb)
        div_button.clicked.connect(self.divv)
        
        self.show()
        
        #self.line.setText(str(sumAll))
        #opVar = True
        
    @pyqtSlot()

    def added(self):
        var3=0
        var1 = self.textbox1.text()
        var2 = self.textbox2.text()
        var3 = float(var1) + float(var2)
        #print(var3)
        self.textbox3.setText(str(var3))
        
    def subb(self):
        var3=0
        var1 = self.textbox1.text()
        var2 = self.textbox2.text()
        var3 = float(var1) - float(var2)
        #print(var3)
        self.textbox3.setText(str(var3))
        
    def divv(self):
        var3=0
        var1 = self.textbox1.text()
        var2 = self.textbox2.text()
        var3 = float(var1) / float(var2)
        #print(var3)
        self.textbox3.setText(str(var3))
        
    def mult(self):
        var3=0
        var1 = self.textbox1.text()
        var2 = self.textbox2.text()
        var3 = float(var1) * float(var2)
        #print(var3)
        self.textbox3.setText(str(var3))

        #self.textbox3.text() = str(var3)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
