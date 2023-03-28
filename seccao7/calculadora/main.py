import sys

from display import Display
from info import Info 
from main_window import MainWindow 
from buttons import ButtonsGrid
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from styles import setupTheme
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    #define icone 
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    #info 
    info = Info('Sua conta')
    window.addWidgetToVLayout(info)

    #display
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid 
    buttonsGrid = ButtonsGrid(display,info,window)
    window.vLayout.addLayout(buttonsGrid)
  


    #executa tudo 
    window.adjustFixedSize()
    window.show()
    app.exec()