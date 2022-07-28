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

        self.subventana=SubVentana()#hay que ponerlo antes de crear los botones para que lo tome

        boton_mostrar=QPushButton("Mostrar Subventana")
        boton_mostrar.clicked.connect(self.subventana.show)
        layout.addWidget(boton_mostrar)

        boton_ocultar=QPushButton("Ocultar Subventana")
        boton_ocultar.clicked.connect(self.subventana.hide)
        layout.addWidget(boton_ocultar)



if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()#clase
    window.show()
    sys.exit(app.exec_())