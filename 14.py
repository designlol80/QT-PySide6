from PySide6.QtWidgets import *
from PySide6.QtCore import Qt#para usar banderas o flag
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        texto=QLineEdit()
        texto.setMaxLength(10)
        texto.setPlaceholderText("Escribe maximo 10 caracteres")
        texto.textChanged.connect(self.texto_cambiado)
        texto.returnPressed.connect(self.enter_presionado)

        self.setCentralWidget(texto)

    def texto_cambiado(self,texto):
        print("Texto Cambiado",texto)

    def enter_presionado(self):
        texto=self.centralWidget().text()#lo que tiene en el widget lo envia a la variable
        print("Enter presionado, texto: ",texto)

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()#clase
    window.show()
    sys.exit(app.exec_())