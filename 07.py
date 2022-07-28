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

        texto=QLineEdit()
        texto.textChanged.connect(self.texto_modificado)
        self.setCentralWidget(texto)

        self.texto=texto#atributo
    
    def texto_modificado(self):
        texto_recuperado=self.texto.text()#aqui lo usamos
        self.setWindowTitle(texto_recuperado)

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()#clase
    window.show()
    sys.exit(app.exec_())