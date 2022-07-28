from posixpath import abspath
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480,320)
        self.setStatusBar(QStatusBar(self))

        self.construir_menu()

    def construir_menu(self):
        menu=self.menuBar()
        menu_archivo=menu.addMenu("&Menú")#presionando Alt + M, en este caso(M)
        menu_archivo.addAction("&Prueba")
        submenu_archivo=menu_archivo.addMenu("&SubMenú")
        submenu_archivo.addAction("SubOpción &1")
        submenu_archivo.addAction("SubOpción &2")
        menu_archivo.addSeparator()
        menu_archivo.addAction(QIcon('./imagenes/Qt.ico'),"S&alir",self.close,"ctrl+Q")
    
        menu_ayuda=menu.addMenu("Ay&uda")
        accion_info=QAction("&Información",self)#Hace referencia a la propia ventana principal(Instanciamos)
        accion_info.setIcon(QIcon("./imagenes/Qt.ico"))
        accion_info.setShortcut("ctrl+I")
        accion_info.triggered.connect(self.mostrar_info)
        accion_info.setStatusTip("Muestra informacion irrelevante")
        menu_ayuda.addAction(accion_info)#primero se instancia y despues la agregamos al menu    

    def mostrar_info(self):
        QMessageBox.information(self,"Información","Esto es un texto informativo")


if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()#clase
    window.show()
    sys.exit(app.exec_())