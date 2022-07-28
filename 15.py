from PySide6.QtWidgets import *
from PySide6.QtCore import Qt#para usar banderas o flag
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        numero=QSpinBox()
        #numero.setMinimum(0)
        #numero.setMaximum(20)
        numero.setRange(0,20)
        numero.setSingleStep(2)#numero de pasos
        numero.setPrefix("$")
        numero.setSuffix("%")
        numero.setValue(8)
        print(numero.value())
        numero.valueChanged.connect(self.valor_cambiado)

        self.setCentralWidget(numero)

    def valor_cambiado(self,numero):
        print("Valor Cambiado",numero)

    def enter_presionado(self):
        texto=self.centralWidget().text()#lo que tiene en el widget lo envia a la variable
        print("Enter presionado, texto: ",texto)

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()#clase
    window.show()
    sys.exit(app.exec_())