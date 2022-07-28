from PySide6.QtWidgets import *
import sys

class Dialogo(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(240,120)
        self.setWindowTitle('Hola')

        layout=QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(QLabel("Dialogo de prueba"))

        botones=QDialogButtonBox(QDialogButtonBox.Ok|QDialogButtonBox.Cancel)
        botones.accepted.connect(self.accept)#Capturamos la respuesta
        botones.rejected.connect(self.reject)#Capturamos la respuesta

        botones.button(QDialogButtonBox.Ok).setText("Aceptar")#Se le cambia el nombre
        botones.button(QDialogButtonBox.Cancel).setText("Cancelar")#Se le cambia el nombre

        layout.addWidget(botones)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480,320)

        boton=QPushButton("Mostrar Dialogo")
        boton.clicked.connect(self.boton_clicado)

        self.setCentralWidget(boton)

    def boton_clicado(self):
        dialogo=Dialogo()
        respuesta=dialogo.exec_()
        if respuesta:#mostramos la respuesta
            print("Dialogo Aceptado")
        else:
            print("Dialogo Denegado")
       
if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()#clase
    window.show()
    sys.exit(app.exec_())