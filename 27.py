from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
from PySide6.QtCore import QTranslator,QLibraryInfo

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480,320)

        boton=QPushButton("Mostrar Dialogo")
        boton.clicked.connect(self.boton_clicado)

        self.setCentralWidget(boton)

    def boton_clicado(self):
        dialogo=QMessageBox.warning(self,"Diálogo de aviso","¿Estás seguro de aplicar los cambios?",buttons=QMessageBox.Apply|QMessageBox.Cancel)
        print(dialogo)
        if dialogo == QMessageBox.Apply:
            print("Aplicamos los cambios")
        else:
            print("No aplicamos los cambios")
    

if __name__=='__main__':
    app=QApplication(sys.argv)

    traductor=QTranslator(app)
    traducciones=QLibraryInfo.location(QLibraryInfo.TranslationsPath)
    traductor.load("qt_es",traducciones)
    app.installTranslator(traductor)
    print(traducciones)
    
    window=MainWindow()#clase
    window.show()
    sys.exit(app.exec_())