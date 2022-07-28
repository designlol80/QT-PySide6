from PySide6.QtWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480,320)

        boton=QPushButton("Mostrar Dialogo")
        boton.clicked.connect(self.boton_clicado)

        self.setCentralWidget(boton)

        self.boton=boton#Para la fuente y el color

    def boton_clicado(self):
        ##Abrir archivo
        # fichero,_=QFileDialog.getOpenFileName(self,"Abrir archivo",".")
        # print(fichero)

        ##Guardar archivo
        # fichero,_=QFileDialog.getSaveFileName(self,"Guardar archivo",".")
        # print(fichero)

        ##Ingresar Texto(Devuelve una tupla)
        # valor,confirmado=QInputDialog.getText(self,"Título","Texto")
        # print(confirmado)
        # if confirmado:
        #     print(valor)

        ##Ingresar Entero(Devuelve una tupla)
        # valor,confirmado=QInputDialog.getInt(self,"Título","Entero")
        # print(confirmado)
        # if confirmado:
        #     print(valor)

        ##Ingresar Decimal(Devuelve una tupla)
        # valor,confirmado=QInputDialog.getDouble(self,"Título","Decimal")
        # print(confirmado)
        # if confirmado:
        #     print(valor)

        ##Ingresar Decimal(Devuelve una tupla)
        # valor,confirmado=QInputDialog.getItem(self,"Título","Colores",["Rojo","Azul","Verde","Blanco"],editable=False)#False o True
        # print(confirmado)
        # if confirmado:
        #     print(valor)

        ##Fuente
        # confirmado,fuente=QFontDialog.getFont(self)
        # print(confirmado)
        # if confirmado:
        #     print(fuente)
        #     self.boton.setFont(fuente)

        ##Color
        color=QColorDialog.getColor()
        print(color.name())
        if color.isValid():
            self.boton.setStyleSheet(f"background-color:{color.name()}")

        
    
if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()#clase
    window.show()
    sys.exit(app.exec_())