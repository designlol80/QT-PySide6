from PySide6.QtWidgets import *
from PySide6.QtCore import Qt#para usar banderas o flag
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        desplegable=QComboBox()
        desplegable.addItems(["Opcion 1","Opcion 2","Opcion 3"])
        desplegable.currentIndexChanged.connect(self.indice_cambiado)
        desplegable.currentTextChanged.connect(self.texto_cambiado)
        
        print("Indice Actual",desplegable.currentIndex())
        print("Texto Actual",desplegable.currentText())

        self.setCentralWidget(desplegable)

    def indice_cambiado(self,indice):
        print("Nuevo Indice",indice)
    
    def texto_cambiado(self,texto):
        print("Nuevo texto",texto)

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()#clase
    window.show()
    sys.exit(app.exec_())