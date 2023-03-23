from variables import WINDOW_ICON_PATH
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication,QMainWindow,QVBoxLayout,QWidget,
                               QLabel)
class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None,*args,**kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        #configurando layout basico
        self.cw =QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)

        self.setCentralWidget(self.cw)

        #titulo da janela
        self.setWindowTitle("Calculadora")
        
        #define icone 
        icon = QIcon(str(WINDOW_ICON_PATH))
    def adjustFixedSize(self) -> None:
        #ultima coisa a ser feita
        self.adjustSize()   
        self.setFixedSize(self.width(),self.height())
    
    def addToVLayout(self,widget:QWidget):
        self.vLayout.addWidget(widget)
        self.adjustFixedSize()