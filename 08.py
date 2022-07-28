from PySide6.QtWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hola Mundo")
        self.resize(480,360)

        etiqueta=QLabel("Soy una etiqueta")
        fuente=etiqueta.font()
        fuente.setPointSize(26)
        etiqueta.setFont(fuente)

        self.setCentralWidget(etiqueta)

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()#clase
    window.show()
    sys.exit(app.exec_())