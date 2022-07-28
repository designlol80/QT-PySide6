from PySide6.QtWidgets import *
from PySide6.QtCore import Qt #para alinear
import sys

class Caja(QLabel):
    def __init__(self,color):
        super().__init__()
        self.setStyleSheet(f"background-color: {color}")
        

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        formulario=QFormLayout()
        formulario.addRow('Naranja',Caja('orange'))
        formulario.addRow('Morado',Caja('purple'))
        formulario.addRow('Magenta',Caja('magenta'))
        formulario.addRow('Gris',Caja('gray'))
        formulario.addRow('Rojo',Caja('red'))

        formulario.setLabelAlignment(Qt.AlignRight)
        formulario.setFormAlignment(Qt.AlignVCenter)

        widget=QWidget()#Tenemos que usarlo como puente
        widget.setLayout(formulario)#Tenemos que usarlo como puente
        self.setCentralWidget(widget)
        


if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()#clase
    window.show()
    sys.exit(app.exec_())