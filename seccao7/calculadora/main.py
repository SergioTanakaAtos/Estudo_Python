import sys

from display import Display
from info import Info 
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    #define icone 
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    #info 
    info = Info('2.0 ^ 10.0 = 1024')
    window.addToVLayout(info)

    #display
    display = Display()
    window.addToVLayout(display)

    #executa tudo 
    window.show()
    app.exec()