from PySide6.QtWidgets import *
from PySide6.QtCore import Qt#para usar banderas o flag
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        casilla=QCheckBox("Casilla de Verificacion")
        casilla.setCheckState(Qt.PartiallyChecked)#se usa para chequear el triestado...osea que no esta chequeado y chequeado que seria el estado uno
        casilla.stateChanged.connect(self.estado_cambiado)
        #casilla.setEnabled(False)#Para desactivar la casilla
        print("Activada",casilla.isChecked())
        print("Parcial",casilla.isTristate())

        self.setCentralWidget(casilla)

    def estado_cambiado(self,estado):
        print(estado)
        if estado==Qt.Checked:#aqui usamos esos flag que nos permite es ver una forma mas amigable 
            print("Casilla Marcada")
        if estado==Qt.Unchecked:#aqui usamos esos flag que nos permite es ver una forma mas amigable 
            print("Casilla Desmarcada")
        if estado==Qt.PartiallyChecked:#el tri estado(1)
            print("Casilla Parcial")
        

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()#clase
    window.show()
    sys.exit(app.exec_())