from PySide6.QtWidgets import *
import sys

class Caja(QLabel):
    def __init__(self,color):
        super().__init__()
        self.setStyleSheet(f"background-color: {color}")
        

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        cuadricula=QGridLayout()
        cuadricula.addWidget(Caja("orange"),0,0)
        cuadricula.addWidget(Caja("purple"),1,1)
        cuadricula.addWidget(Caja("magenta"),2,2)

        widget=QWidget()#Tenemos que usarlo como puente
        widget.setLayout(cuadricula)#Tenemos que usarlo como puente
        self.setCentralWidget(widget)
        


if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()#clase
    window.show()
    sys.exit(app.exec_())