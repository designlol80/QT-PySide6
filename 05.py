##Las SEÑALES(SOn notificaciones emitidas por los widgets) 
##Y los RECEPTORES(SLOT)(Se necesitan para enlazar la notificacion a una funcionalidad)
from PySide6.QtWidgets import *
from PySide6.QtCore import QSize
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hola Mundo")
        self.resize(480,360)

        Boton=QPushButton("Soy un Boton")
        
        #Boton.clicked.connect(self.boton_clicado)#Slot cuando se clicleado
        #Boton.pressed.connect(self.boton_pulsado)#Slot cuando se Pulsa
        #Boton.released.connect(self.boton_Liberado)#Slot cuando se Libera
        Boton.setCheckable(True)
        Boton.clicked.connect(self.boton_alternado)
        
        
        self.setCentralWidget(Boton)

    # def boton_clicado(self): #metodo que se llama cuando se cliclea el boton
    #     print ("Boton CLicleado")
    # def boton_pulsado(self): #metodo que se llama cuando se pulsa el boton
    #     print ("Boton Pulsado")
    # def boton_Liberado(self): #metodo que se llama cuando se Libera el boton
    #     print ("Boton Liberado")
    def boton_alternado(self, valor): 
        print ("Boton alternado",valor)

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()#clase
    window.show()
    sys.exit(app.exec_())