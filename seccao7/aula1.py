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
from PySide6.QtCore import Slot
from PySide6.QtWidgets import(QApplication , QPushButton, QWidget,
                              QMainWindow, QGridLayout) 

class MyWindow(QMainWindow):
    def __init__(self, parent= None):
        super().__init__(parent)
        
        self.central_widget = QWidget()

        self.window.setCentralWidget(self.entral_widget)
        self.window.setWindowTitle('Minha janela bonita')

        #BOTÃO
        self.botao = self.make_button('Texto botão')
        self.botao.clicked.connect(self.segunda_acao_marcada)

        #botao.show() # adicionar o widget na hierarquia e exibe a janela 


        self.botao2 = self.make_button('bt2')
        self.botao2.setStyleSheet('font-size:40px; color:red;')


        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        self.grid_layout.addWidget(self.botao)
        self.grid_layout.addWidget(self.botao2)

        self.status_bar = self.statusBar()
        self.status_bar.showMessage("Mostar barra")

        #menu bar 
        self.menu = self.menuBar()
        self.primeiro_menu = self.menu.addMenu('primeiro menu')
        self.primeira_acao = self.primeiro_menu.addAction('primeira acao')
        self.primeira_acao.triggered.connect(self.muda_mensagem_da_status_bar)


        self.segunda_acao = self.primeiro_menu.addAction('segunda acao')
        self.segunda_acao.setCheckable(True)
        self.segunda_acao.toggled.connect(self.segunda_acao_marcada)
        self.segunda_acao.hovered.connect(self.segunda_acao_marcada)

    @Slot()
    def muda_mensagem_da_status_bar(self):
        self.status_bar.showMessage('O meu slot foi executado')

    @Slot()
    def segunda_acao_marcada(self):
        print('Está marcado?', self.segunda_action.isChecked())

    def make_button(self, text):
        btn = QPushButton(text)
        btn.setStyleSheet('font-size: 80px;')
        return btn
#status bar 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec() # loop da apliocação
