from PySide6.QtWidgets import *
import sys

class Caja(QLabel):
    def __init__(self,color):
        super().__init__()
        self.setStyleSheet(f"background-color: {color}")
        

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        layoutHor=QHBoxLayout()
        layoutVer1=QVBoxLayout()
        layoutVer2=QVBoxLayout()

        layoutHor.addWidget(Caja("green"))
        layoutHor.addLayout(layoutVer1)
        layoutHor.addLayout(layoutVer2)

        layoutVer1.addWidget(Caja("blue"))
        layoutVer1.addWidget(Caja("red"))

        layoutVer2.addWidget(Caja("orange"))
        layoutVer2.addWidget(Caja("magenta"))
        layoutVer2.addWidget(Caja("purple"))

        widget=QWidget()#Tenemos que usarlo como puente
        widget.setLayout(layoutHor)#Tenemos que usarlo como puente
        self.setCentralWidget(widget)
        


if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()#clase
    window.show()
    sys.exit(app.exec_())