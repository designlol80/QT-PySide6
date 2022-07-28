from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        formulario=QFormLayout()
        formulario.addRow("QChechBox",QCheckBox())
        formulario.addRow("QRadioButton",QRadioButton())
        formulario.addRow("QLabel",QLabel("QLabel"))
        formulario.addRow("QPushButton",QPushButton("QbushButton"))
        formulario.addRow("QLineEdit",QLineEdit("QLineEdit"))
        formulario.addRow("QDateEdit",QDateEdit())
        formulario.addRow("QDateTimeEdit",QDateTimeEdit())
        formulario.addRow("QSpinBox",QSpinBox())
        formulario.addRow("QDoubleSpinBox",QDoubleSpinBox())
        formulario.addRow("QComboBox",QComboBox())
        formulario.addRow("QFontComboBox",QFontComboBox())
        formulario.addRow("QProgressBar",QProgressBar())
        formulario.addRow("QLCDNumber",QLCDNumber())
        formulario.addRow("QSlider",QSlider(Qt.Horizontal))
        formulario.addRow("QDial",QDial())

        widget=QWidget()
        widget.setLayout(formulario)
        self.setCentralWidget(widget)

if __name__=='__main__':
    app=QApplication(sys.argv)
    app.setStyle("Fusion")#Estilos
    window=MainWindow()#clase
    window.show()
    sys.exit(app.exec_())