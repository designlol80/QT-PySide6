from PySide6.QtWidgets import *
import sys
import random

class SubVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(240,120)
        self.setWindowTitle("Subventana")
        etiqueta=QLabel(f"Soy una Subventana....{random.randint(0,100)}")
        layout=QVBoxLayout()
        layout.addWidget(etiqueta)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana Principal")

        layout=QVBoxLayout()
        widget=QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        boton_mostrar=QPushButton("Mostrar Subventana")
        boton_mostrar.clicked.connect(self.mostrar_subventana)
        layout.addWidget(boton_mostrar)

        boton_ocultar=QPushButton("Ocultar Subventana")
        boton_ocultar.clicked.connect(self.ocultar_subventana)
        layout.addWidget(boton_ocultar)

        self.subventana=None

    def ocultar_subventana(self):
        if self.subventana and self.subventana.isVisible():
            self.subventana.hide()

    def mostrar_subventana(self):
        print("Subventana abierta")
        if not self.subventana:
            self.subventana=SubVentana()
        self.subventana.show()

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()#clase
    window.show()
    sys.exit(app.exec_())