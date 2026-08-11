import os

#os.environ["QT_QPA_PLATFORM"] = "minimal"

# Hier folgen danach deine restlichen Imports...
from bin.interface import Ui_MainWindow
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *




class UpscaylRecursive(QMainWindow):
    def __init__(self, Ui_MainWindow):
        super(UpscaylRecursive, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        
        
        
        
        
if __name__ == "__main__":
    app = QApplication([])
    window = UpscaylRecursive(Ui_MainWindow)
    window.show()
    app.exec()