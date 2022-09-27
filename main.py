
from PyQt6.QtWidgets import QApplication 
import sys
from controller.ui_main import MainWindow

app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()