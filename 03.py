from PySide6.QtWidgets import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()#Heredamos el comportamiento de la clase QMainWindow
        self.setWindowTitle("Hola Mundo")
        Boton=QPushButton("Soy un Boton")
        self.setCentralWidget(Boton)


if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()#clase
    window.show()
    sys.exit(app.exec_())