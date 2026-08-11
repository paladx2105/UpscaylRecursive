from bin.interface import Ui_MainWindow
from bin.upscayl import run_upscayl_batch
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *




class UpscaylRecursive(QMainWindow):
    def __init__(self, Ui_MainWindow):
        super(Ui_MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        
        
        
        
        
if __name__ == "__main__":
    app = QApplication([])
    window = UpscaylRecursive(Ui_MainWindow)
    window.show()
    app.exec()