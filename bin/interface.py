# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerbywWIV.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QListView, QListWidget, QListWidgetItem,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QStatusBar, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 501)
        MainWindow.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setSpacing(9)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 9, 0, 0)
        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout = QGridLayout(self.widget_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.toolButton_inputPath = QToolButton(self.widget_5)
        self.toolButton_inputPath.setObjectName(u"toolButton_inputPath")
        self.toolButton_inputPath.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextOnly)
        self.toolButton_inputPath.setArrowType(Qt.ArrowType.NoArrow)

        self.gridLayout.addWidget(self.toolButton_inputPath, 2, 9, 1, 1)

        self.lineEdit_modelPath = QLineEdit(self.widget_5)
        self.lineEdit_modelPath.setObjectName(u"lineEdit_modelPath")

        self.gridLayout.addWidget(self.lineEdit_modelPath, 6, 8, 1, 1)

        self.lineEdit_upscaylPath = QLineEdit(self.widget_5)
        self.lineEdit_upscaylPath.setObjectName(u"lineEdit_upscaylPath")

        self.gridLayout.addWidget(self.lineEdit_upscaylPath, 5, 8, 1, 1)

        self.lineEdit_inputPath = QLineEdit(self.widget_5)
        self.lineEdit_inputPath.setObjectName(u"lineEdit_inputPath")

        self.gridLayout.addWidget(self.lineEdit_inputPath, 2, 8, 1, 1)

        self.toolButton_upscaylPath = QToolButton(self.widget_5)
        self.toolButton_upscaylPath.setObjectName(u"toolButton_upscaylPath")
        self.toolButton_upscaylPath.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextOnly)

        self.gridLayout.addWidget(self.toolButton_upscaylPath, 5, 9, 1, 1)

        self.lineEdit_modelName = QLineEdit(self.widget_5)
        self.lineEdit_modelName.setObjectName(u"lineEdit_modelName")

        self.gridLayout.addWidget(self.lineEdit_modelName, 7, 8, 1, 1)

        self.toolButton_modelPath = QToolButton(self.widget_5)
        self.toolButton_modelPath.setObjectName(u"toolButton_modelPath")
        self.toolButton_modelPath.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextOnly)

        self.gridLayout.addWidget(self.toolButton_modelPath, 6, 9, 1, 1)

        self.toolButton_outputPath = QToolButton(self.widget_5)
        self.toolButton_outputPath.setObjectName(u"toolButton_outputPath")
        self.toolButton_outputPath.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextOnly)

        self.gridLayout.addWidget(self.toolButton_outputPath, 3, 9, 1, 1)

        self.lineEdit_outputPath = QLineEdit(self.widget_5)
        self.lineEdit_outputPath.setObjectName(u"lineEdit_outputPath")

        self.gridLayout.addWidget(self.lineEdit_outputPath, 3, 8, 1, 1)

        self.label_5 = QLabel(self.widget_5)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 7, 1, 1)

        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 5, 7, 1, 1)

        self.label_3 = QLabel(self.widget_5)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 7, 7, 1, 1)

        self.label = QLabel(self.widget_5)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 3, 7, 1, 1)

        self.label_4 = QLabel(self.widget_5)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 6, 7, 1, 1)


        self.verticalLayout_3.addWidget(self.widget_5, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_6 = QWidget(self.widget_3)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout_2 = QGridLayout(self.widget_6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSlider_scale = QSlider(self.widget_6)
        self.horizontalSlider_scale.setObjectName(u"horizontalSlider_scale")
        self.horizontalSlider_scale.setMinimum(1)
        self.horizontalSlider_scale.setMaximum(4)
        self.horizontalSlider_scale.setPageStep(0)
        self.horizontalSlider_scale.setSliderPosition(1)
        self.horizontalSlider_scale.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider_scale.setInvertedAppearance(False)
        self.horizontalSlider_scale.setInvertedControls(False)
        self.horizontalSlider_scale.setTickPosition(QSlider.TickPosition.NoTicks)
        self.horizontalSlider_scale.setTickInterval(0)

        self.gridLayout_2.addWidget(self.horizontalSlider_scale, 1, 1, 1, 1)

        self.lineEdit_scale = QLineEdit(self.widget_6)
        self.lineEdit_scale.setObjectName(u"lineEdit_scale")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_scale.sizePolicy().hasHeightForWidth())
        self.lineEdit_scale.setSizePolicy(sizePolicy1)
        self.lineEdit_scale.setMaximumSize(QSize(27, 16777215))
        self.lineEdit_scale.setMaxLength(1)
        self.lineEdit_scale.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_scale.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_scale, 1, 2, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_6 = QLabel(self.widget_6)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.widget_6, 0, Qt.AlignmentFlag.AlignTop)

        self.groupBox = QGroupBox(self.widget_3)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.groupBox.setCheckable(True)
        self.groupBox.setChecked(False)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_7 = QWidget(self.groupBox)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_4 = QVBoxLayout(self.widget_7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lineEdit_customWidth = QLineEdit(self.widget_7)
        self.lineEdit_customWidth.setObjectName(u"lineEdit_customWidth")
        self.lineEdit_customWidth.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.lineEdit_customWidth)

        self.label_7 = QLabel(self.widget_7)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_4.addWidget(self.label_7, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.groupBox)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_5 = QVBoxLayout(self.widget_8)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lineEdit_customHeight = QLineEdit(self.widget_8)
        self.lineEdit_customHeight.setObjectName(u"lineEdit_customHeight")
        self.lineEdit_customHeight.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.lineEdit_customHeight)

        self.label_8 = QLabel(self.widget_8)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_5.addWidget(self.label_8, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.widget_8)


        self.verticalLayout_3.addWidget(self.groupBox, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_9 = QWidget(self.widget_3)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_10 = QWidget(self.widget_9)
        self.widget_10.setObjectName(u"widget_10")
        self.formLayout_2 = QFormLayout(self.widget_10)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(-1, -1, -1, 9)
        self.label_9 = QLabel(self.widget_10)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_9)

        self.comboBox_format = QComboBox(self.widget_10)
        self.comboBox_format.addItem("PNG")
        self.comboBox_format.addItem("JPG")
        self.comboBox_format.setItemText("JPEG")
        self.comboBox_format.addItem("WEBP")
        self.comboBox_format.setObjectName(u"comboBox_format")
        self.comboBox_format.setMaxCount(3)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.comboBox_format)

        self.checkBox_tta = QCheckBox(self.widget_10)
        self.checkBox_tta.setObjectName(u"checkBox_tta")
        self.checkBox_tta.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.checkBox_tta.setTristate(False)

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.checkBox_tta)


        self.horizontalLayout_4.addWidget(self.widget_10, 0, Qt.AlignmentFlag.AlignVCenter)

        self.widget_11 = QWidget(self.widget_9)
        self.widget_11.setObjectName(u"widget_11")
        self.formLayout_3 = QFormLayout(self.widget_11)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_10 = QLabel(self.widget_11)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_10)

        self.lineEdit_gpu = QLineEdit(self.widget_11)
        self.lineEdit_gpu.setObjectName(u"lineEdit_gpu")
        self.lineEdit_gpu.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit_gpu)

        self.checkBox_verbose = QCheckBox(self.widget_11)
        self.checkBox_verbose.setObjectName(u"checkBox_verbose")
        self.checkBox_verbose.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.checkBox_verbose)


        self.horizontalLayout_4.addWidget(self.widget_11, 0, Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_3.addWidget(self.widget_9)


        self.horizontalLayout_2.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.listWidget = QListWidget(self.widget_4)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMovement(QListView.Movement.Free)
        self.listWidget.setProperty(u"isWrapping", False)
        self.listWidget.setLayoutMode(QListView.LayoutMode.Batched)

        self.verticalLayout_2.addWidget(self.listWidget)

        self.progressBar = QProgressBar(self.widget_4)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout_2.addWidget(self.progressBar)


        self.horizontalLayout_2.addWidget(self.widget_4)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_save = QPushButton(self.widget)
        self.pushButton_save.setObjectName(u"pushButton_save")

        self.horizontalLayout.addWidget(self.pushButton_save)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_9)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_8)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_cancel = QPushButton(self.widget)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")

        self.horizontalLayout.addWidget(self.pushButton_cancel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.pushButton_ok = QPushButton(self.widget)
        self.pushButton_ok.setObjectName(u"pushButton_ok")

        self.horizontalLayout.addWidget(self.pushButton_ok)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"UpscaylRecursive", None))
        self.toolButton_inputPath.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_modelPath.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>The path where youre \u2018<span style=\" font-style:italic; text-decoration: underline;\">Upscayl</span>\u2019 models are located. It should usually be found in the \u2018<span style=\" font-style:italic; text-decoration: underline;\">.../Upscayl/resources/models</span>\u2019 folder.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lineEdit_upscaylPath.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>The path where '<span style=\" font-style:italic; text-decoration: underline;\">Upscayl-bin.exe</span>' is located. It should usually be found in the \u2018<span style=\" font-style:italic; text-decoration: underline;\">.../Upscayl/resources/bin</span>\u2019 folder.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lineEdit_inputPath.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>The path from which to start</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_upscaylPath.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_modelName.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>The model name you want to use. You can find it in your '<span style=\" font-style:italic; text-decoration: underline;\">Upscayl</span>' Model folder.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_modelPath.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButton_outputPath.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_outputPath.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>The path where the output should go</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Input Path", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Upscayl Path", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Model Name", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Output Path", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Model Path", None))
        self.lineEdit_scale.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.lineEdit_scale.setPlaceholderText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Scale", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Custom Size", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Format", None))
        self.comboBox_format.setItemText(0, QCoreApplication.translate("MainWindow", u"PNG", None))
        self.comboBox_format.setItemText(1, QCoreApplication.translate("MainWindow", u"JPG", None))
        self.comboBox_format.setItemText(2, QCoreApplication.translate("MainWindow", u"Webp", None))

        self.checkBox_tta.setText(QCoreApplication.translate("MainWindow", u"TTA", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"GPU", None))
        self.lineEdit_gpu.setText(QCoreApplication.translate("MainWindow", u"auto", None))
        self.checkBox_verbose.setText(QCoreApplication.translate("MainWindow", u"Verbose", None))
        self.pushButton_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.pushButton_ok.setText(QCoreApplication.translate("MainWindow", u"OK", None))
    # retranslateUi

