from PySide6.QtWidgets import *
import sys

app=QApplication(sys.argv)
window=QMainWindow()#Apartir del QMainWindow creamos una ventana es igual qu el QWidget pero con otras ventajas
window.setWindowTitle("Hola Mundo")
Boton=QPushButton("Soy un Boton")
window.setCentralWidget(Boton)
window.show()
sys.exit(app.exec_())
