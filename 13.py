from PySide6.QtWidgets import *
from PySide6.QtCore import Qt#para usar banderas o flag
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        lista=QListWidget()
        lista.addItems(["Opcion 1","Opcion 2","Opcion 3"])
        lista.currentItemChanged.connect(self.item_cambiado)
        
        print(lista.currentItem())

        self.setCentralWidget(lista)

    def item_cambiado(self,item):
        print("Nuevo Item",item.text())

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()#clase
    window.show()
    sys.exit(app.exec_())