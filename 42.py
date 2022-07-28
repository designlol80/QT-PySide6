from PySide6.QtWidgets import *
from pathlib import Path
import sys

def absPath(file):
    return str(Path(__file__).parent.absolute()/file)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        formulario=QFormLayout()
        formulario.addRow("QChechBox",QCheckBox())
        formulario.addRow("QRadioButton",QRadioButton())
        formulario.addRow("QLabel",QLabel("QLabel"))
        formulario.addRow("QPushButton",QPushButton("QbushButton"))
        formulario.addRow("QLineEdit",QLineEdit("QLineEdit"))
        formulario.addRow("QSpinBox",QSpinBox())


        widget=QWidget()
        widget.setLayout(formulario)
        self.setCentralWidget(widget)
        #en este caso afecta de forma global para evitar eso hay qye agrear un identificador en el proximo script lo vemos.
        self.setStyleSheet("""
            QMainWindow {background-color: #212121}
            QLabel{color:#e9e9e9}
            QPushButton{
                background-color:orange;
                font-family:"Arial";
                font-size:14px;
                font-weight:bold}
        """)

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()#clase
    window.show()
    sys.exit(app.exec_())