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
        
        layout=QStackedLayout()
        layout.addWidget(Caja("orange"))

        layout.addWidget(Caja("orange"))
        layout.addWidget(Caja("magenta"))
        layout.addWidget(Caja("purple"))
        layout.addWidget(Caja("red"))

        widget=QWidget()#Tenemos que usarlo como puente
        widget.setLayout(layout)#Tenemos que usarlo como puente
        
        self.setCentralWidget(widget)
        self.layout=layout#para gestionar el layout del widget que esta por encima de los demas lo hacemos con este atributo de clase
        
        
    def keyPressEvent(self, event):
        indice=self.layout.currentIndex()
        print(indice)
        indice_maximo=self.layout.count()-1
        print(indice_maximo)

        if event.key()==Qt.Key_Right:
            print("Flecha derecha presionada")
            indice+=1
        elif event.key()==Qt.Key_Left:
            print("Flecha izquierda presionada")
            indice-=1

        if indice>indice_maximo:
            indice=0
        elif indice<0:
            indice=indice_maximo

        self.layout.setCurrentIndex(indice)

        event.accept()#Gestionalo tu

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()#clase
    window.show()
    sys.exit(app.exec_())