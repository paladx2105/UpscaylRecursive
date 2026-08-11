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
        # Schließe das Fenster sauber über `close()` (ruft `closeEvent` auf)
        self.ui.pushButton_cancel.clicked.connect(self.close)

        # Slider initial setzen und mit dem GroupBox-Status synchronisieren
        self.ui.horizontalSlider_scale.setEnabled(not self.ui.groupBox.isChecked())
        self.ui.groupBox.toggled.connect(lambda checked: self.ui.horizontalSlider_scale.setEnabled(not checked))

        self.ui.lineEdit_scale.setText(str(self.ui.horizontalSlider_scale.value()))
        self.ui.horizontalSlider_scale.valueChanged.connect(
            lambda value: self.ui.lineEdit_scale.setText(str(value))
        )

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Beenden', 'Möchten Sie das Programm wirklich beenden?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
                self.save_settings()
            except Exception:
                pass
            event.accept()
        else:
            event.ignore()
            
    def save_settings(self):
        output_path = self.ui.lineEdit_outputPath.text()
        input_path = self.ui.lineEdit_inputPath.text()
        binary_path = self.ui.lineEdit_binaryPath.text()
        model_path = self.ui.lineEdit_modelPath.text()
        model_name = self.ui.lineEdit_modelName.text()

        if self.ui.groupBox.isChecked():
            width_scale = self.ui.lineEdit_width.text()
            height_scale = self.ui.lineEdit_height.text()
        else:
            slider_scale = self.ui.lineEdit_scale.text()
            
        format = self.ui.comboBox_format.currentText()
        gpu = self.ui.self.lineEdit_gpu.text()
        
        if self.ui.checkBox_tta.isChecked():
            tta = True
        else:
            tta = False
            
        if self.ui.checkBox_verbose.isChecked():
            verbose = True
        else:
            verbose = False

        settings = QSettings('UpscaylRecursive', 'settings')
        settings.setValue('output_path', output_path)
        settings.setValue('input_path', input_path)
        settings.setValue('binary_path', binary_path)
        settings.setValue('model_path', model_path)
        settings.setValue('model_name', model_name)
        settings.setValue('width_scale',width_scale)
        settings.setValue('height_scale', height_scale)
        settings.setValue('slider_scale',slider_scale)
        settings.setValue('format', format)
        settings.setValue('gpu', gpu)
        settings.setValue('tta', tta)
        settings.setValue('verbose', verbose)
        settings.sync()
        
        
        
        
if __name__ == "__main__":
    app = QApplication([])
    window = UpscaylRecursive(Ui_MainWindow)
    window.show()
    app.exec()