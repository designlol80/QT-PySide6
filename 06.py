#si deseamos acceder aun widget desde un metodo estan sencillo que almacenamos un acceso a ese widget
#en la propia instancia de la ventana es decir usar un atributo de clase

from PySide6.QtWidgets import *
from PySide6.QtCore import QSize
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hola Mundo")
        self.resize(480,360)

        Boton=QPushButton("Soy un Boton")
        Boton.setCheckable(True)
        Boton.clicked.connect(self.boton_alternado)
        self.setCentralWidget(Boton)

        self.Boton=Boton#Usamos Un atributo de clase

    def boton_alternado(self, valor):
        if valor:
            self.Boton.setText("Estoy Activado")#aqui lo usamos
        else:
            self.Boton.setText("Estoy Desactivado")#aqui lo usamos

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()#clase
    window.show()
    sys.exit(app.exec_())