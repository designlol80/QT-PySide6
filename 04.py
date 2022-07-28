from PySide6.QtWidgets import *
from PySide6.QtCore import QSize
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()#Heredamos el comportamiento de la clase QMainWindow
        self.setWindowTitle("Hola Mundo")
        Boton=QPushButton("Soy un Boton")
        self.setCentralWidget(Boton)
        
        #Variar tamaño de la ventana
        self.resize(480,360)
        #self.setMinimumSize(QSize(480,120))
        #self.setMaximumSize(QSize(600,320))
        #self.setFixedSize(QSize(200,200))

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()#clase
    window.show()
    sys.exit(app.exec_())