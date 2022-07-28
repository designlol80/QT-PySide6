from PySide6.QtWidgets import *
from PySide6.QtCore import Qt#para usar banderas o flag
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        radial=QRadioButton("Botón Radial")
        radial.toggled.connect(self.estado_cambiado)
        radial.setChecked(False)
        print("Radial Activado",radial.isChecked())

        self.setCentralWidget(radial)

    def estado_cambiado(self, estado):
        if estado:
            print("Radial Marcado")
        else:
            print("Radial Desmarcado")


if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()#clase
    window.show()
    sys.exit(app.exec_())