# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec


import sys 
#from PySide6.Qt3DCore import S
from PySide6.QtWidgets import(QApplication , QPushButton, QWidget, QVBoxLayout,
                              QMainWindow) 

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Minha janela bonita')

botao = QPushButton('Texto botão')
botao.setStyleSheet('font-size:40px; color:green;')
#botao.show() # adicionar o widget na hierarquia e exibe a janela 


botao2 = QPushButton('bt2')
botao2.setStyleSheet('font-size:40px; color:red;')


layout = QVBoxLayout()
central_widget.setLayout(layout)

layout.addWidget(botao)
layout.addWidget(botao2)

def slot_exemple(status_bar):
    status_bar.showMesage('meu slot foi exec')

def outro_slot(checked):
    print('esta marcado:', checked)

def terceiro_slot(action):
    def inner():
        outro_slot(action.isChecked())
    return inner 
#status bar 
status_bar = window.statusBar()
status_bar.showMessage("Mostar barra")

#menu bar 
menu = window.menuBar()
primeiro_menu = menu.addMenu('primeiro menu')
primeira_acao = primeiro_menu.addAction('primeira acao')
primeira_acao.triggered.connect(lambda: slot_exemple(status_bar))


segunda_acao = primeiro_menu.addAction('segunda acao')
segunda_acao.setCheckable(True)
segunda_acao.toggled.connect(outro_slot)
segunda_acao.hovered.connect(terceiro_slot(segunda_acao))

window.show()
app.exec() # loop da apliocação
