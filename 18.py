from PySide6.QtWidgets import *
import sys

class Caja(QLabel):
    def __init__(self,color):
        super().__init__()
        self.setStyleSheet(f"background-color: {color}")
        

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        layout=QVBoxLayout()#Vertical
        #layout=QHBoxLayout()#Horizontal
        layout.addWidget(Caja("green"))
        layout.addWidget(Caja("blue"))
        layout.addWidget(Caja("red"))
        layout.setContentsMargins(0,0,0,0)#Margen respecto al borde iz,arri,der,abaj
        layout.setSpacing(3)#espacio entre layout

        widget=QWidget()#Tenemos que usarlo como puente
        widget.setLayout(layout)#Tenemos que usarlo como puente
        self.setCentralWidget(widget)
        


if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()#clase
    window.show()
    sys.exit(app.exec_())