from posixpath import abspath
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import sys

class Caja(QLabel):
    def __init__(self,color):
        super().__init__()
        self.setStyleSheet(f"background-color: {color}")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480,320)
        self.setStatusBar(QStatusBar(self))
        self.construir_menu()
        self.construir_herramientas()

        self.construir_docks()
        self.setCentralWidget(Caja("gray"))

    def construir_docks(self):
        dock1=QDockWidget()
        dock1.setWindowTitle("Dock 1")
        dock1.setWidget(Caja("green"))
        # dock.setMinimumHeight(100)#Ancho
        # dock.setMinimumWidth(125)#Alto
        dock1.setMinimumSize(120,100)#Ancho y alto
        # dock.setFeatures(QDockWidget.NoDockWidgetFeatures)##Para dejarlo estatico
        # dock.setFeatures(QDockWidget.NoDockWidgetFeatures|
        #                  QDockWidget.DockWidgetFloatable)##Para dejarlo flotable(Doble click)
        # dock.setFeatures(QDockWidget.NoDockWidgetFeatures|
        #                  QDockWidget.DockWidgetFloatable|
        #                  QDockWidget.DockWidgetClosable)##Para cerrarlo
        dock1.setFeatures(QDockWidget.NoDockWidgetFeatures|
                          QDockWidget.DockWidgetFloatable|
                          QDockWidget.DockWidgetClosable|
                          QDockWidget.DockWidgetMovable)##Para moverlo

        self.addDockWidget(Qt.LeftDockWidgetArea,dock1)

        dock2=QDockWidget()
        dock2.setWindowTitle("Dock 2")
        dock2.setWidget(Caja("yellow"))
        dock2.setMinimumSize(120,100)
        self.addDockWidget(Qt.RightDockWidgetArea,dock2)

        dock3=QDockWidget()
        dock3.setWindowTitle("Dock 3")
        dock3.setWidget(Caja("blue"))
        dock3.setMinimumSize(120,100)
        self.addDockWidget(Qt.BottomDockWidgetArea,dock3)

    def construir_herramientas(self):
        herramientas=QToolBar("Barra de herramientas")
        herramientas.addAction(QIcon('./imagenes/Qt.ico'),"S&alir",self.close)
        herramientas.addAction(self.accion_info)#LLamamos a accion_info(al accesor)
        
        self.addToolBar(herramientas)

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

        self.accion_info=accion_info#creamos un accesor

    def mostrar_info(self):
        QMessageBox.information(self,"Información","Esto es un texto informativo")


if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()#clase
    window.show()
    sys.exit(app.exec_())