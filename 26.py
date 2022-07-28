from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480,320)
        self.setWindowIcon(QIcon('./imagenes/Qt.ico'))

        boton=QPushButton("Mostrar Dialogo")
        boton.clicked.connect(self.boton_clicado)

        self.setCentralWidget(boton)

    ##MENSAJE PREGUNTA
    # def boton_clicado(self):
    #     dialogo=QMessageBox.question(self,"Pregunta","Esto es una pregunta")
    #     print(dialogo)
    #     if dialogo == QMessageBox.Yes:
    #         print("Ha respondido SI")
    #     else:
    #         print("Ha respondido NO")

    # #MENSAJE ACERCA DE..
    # def boton_clicado(self):
    #     dialogo=QMessageBox.about(self,"Acerca de","Información del programa\nOtro Párrafo")
    #     print(dialogo)#No envia nada

    ##MENSAJE CRITICO
    # def boton_clicado(self):
    #     dialogo=QMessageBox.critical(self,"Error","Ha ocurrido un error")
    #     print(dialogo)

    ##MENSAJE DE INFORMACION
    # def boton_clicado(self):
    #     dialogo=QMessageBox.information(self,"Información","Esto es un texto informativo")
    #     print(dialogo)

    ##MENSAJE ALERTA
    # def boton_clicado(self):
    #     dialogo=QMessageBox.warning(self,"Aviso","Cuidado con este diálogo")
    #     print(dialogo)

    ##MENSAJE ALERTA modificado
    def boton_clicado(self):
        dialogo=QMessageBox.warning(self,"Aviso","Seguro que deseas aplicar los cambios",buttons=QMessageBox.Apply|QMessageBox.Cancel)
        print(dialogo)
        if dialogo == QMessageBox.Apply:
            print("Aplicamos los cambios")
        else:
            print("No aplicamos los cambios")
    

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()#clase
    window.show()
    sys.exit(app.exec_())