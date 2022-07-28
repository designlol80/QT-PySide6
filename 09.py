from PySide6.QtWidgets import *
from PySide6.QtGui import QFont,QPixmap #tipo de fuente
from PySide6.QtCore import Qt #Para alinear el texto
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hola Mundo")
        self.resize(480,320)

        etiqueta=QLabel("Soy una etiqueta")
        fuente=QFont("Comic Sans MS",26)#tipo de fuente
        etiqueta.setFont(fuente)
        #etiqueta.setAlignment(Qt.AlignHCenter)#Alinear texto horizontal centro
        etiqueta.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)#Alinear horizontal y verticalmente...en otras palabra lo coloca en el centro
        
        imagen=QPixmap("./imagenes/Prueba.jpg")
        etiqueta.setPixmap(imagen)
        etiqueta.setScaledContents(True)
        
        self.setCentralWidget(etiqueta)

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()#clase
    window.show()
    sys.exit(app.exec_())