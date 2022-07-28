from PySide6.QtWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480,320)

        boton=QPushButton("Mostrar Dialogo")
        boton.clicked.connect(self.boton_clicado)

        self.setCentralWidget(boton)

    def boton_clicado(self):
        dialogo=QMessageBox(self)
        dialogo.setWindowTitle("Titulo de ejemplo")
        dialogo.setText("Esto es un dialogo de prueba")

        dialogo.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        dialogo.button(QMessageBox.Ok).setText('Aceptar')
        dialogo.button(QMessageBox.Cancel).setText('Cancelar')

        dialogo.setIcon(QMessageBox.Question)#Iconos
        #dialogo.setIcon(QMessageBox.Information)

        respuesta=dialogo.exec_()
        if respuesta==QMessageBox.Ok:
            print("Dialogo Aceptado")
        else:
            print("Dialogo Denegado")
       
if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()#clase
    window.show()
    sys.exit(app.exec_())