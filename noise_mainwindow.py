# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'noise_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Noise_mainwindow(object):
    def setupUi(self, Noise_mainwindow):
        Noise_mainwindow.setObjectName("Noise_mainwindow")
        Noise_mainwindow.resize(626, 940)
        self.centralwidget = QtWidgets.QWidget(Noise_mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(0, 60))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lcdNumber = QtWidgets.QLCDNumber(self.widget)
        self.lcdNumber.setDigitCount(8)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout_3.addWidget(self.lcdNumber, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(45, 0))
        self.label.setMaximumSize(QtCore.QSize(45, 16777215))
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 80))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 80))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 1, 1, 1, 1)
        self.chipcfg_button = QtWidgets.QPushButton(self.groupBox_2)
        self.chipcfg_button.setObjectName("chipcfg_button")
        self.gridLayout_2.addWidget(self.chipcfg_button, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.Lo_freq = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.Lo_freq.setDecimals(4)
        self.Lo_freq.setObjectName("Lo_freq")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Lo_freq)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.time_duration = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.time_duration.setDecimals(0)
        self.time_duration.setMaximum(9999999999999.0)
        self.time_duration.setObjectName("time_duration")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.time_duration)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.tx_gain = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.tx_gain.setDecimals(0)
        self.tx_gain.setMaximum(31.0)
        self.tx_gain.setObjectName("tx_gain")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.tx_gain)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.rx_gain = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.rx_gain.setDecimals(0)
        self.rx_gain.setMaximum(31.0)
        self.rx_gain.setObjectName("rx_gain")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.rx_gain)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.sampling_rate = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.sampling_rate.setDecimals(0)
        self.sampling_rate.setProperty("value", 100.0)
        self.sampling_rate.setObjectName("sampling_rate")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.sampling_rate)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.decimation = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.decimation.setDecimals(0)
        self.decimation.setProperty("value", 100.0)
        self.decimation.setObjectName("decimation")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.decimation)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.formLayout_4 = QtWidgets.QFormLayout(self.groupBox_5)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_13 = QtWidgets.QLabel(self.groupBox_5)
        self.label_13.setObjectName("label_13")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.trigger_mode = QtWidgets.QComboBox(self.groupBox_5)
        self.trigger_mode.setObjectName("trigger_mode")
        self.trigger_mode.addItem("")
        self.trigger_mode.addItem("")
        self.trigger_mode.addItem("")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.trigger_mode)
        self.label_14 = QtWidgets.QLabel(self.groupBox_5)
        self.label_14.setObjectName("label_14")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.threshold_mode = QtWidgets.QComboBox(self.groupBox_5)
        self.threshold_mode.setObjectName("threshold_mode")
        self.threshold_mode.addItem("")
        self.threshold_mode.addItem("")
        self.threshold_mode.addItem("")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.threshold_mode)
        self.label_15 = QtWidgets.QLabel(self.groupBox_5)
        self.label_15.setObjectName("label_15")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.slice_length = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        self.slice_length.setDecimals(3)
        self.slice_length.setProperty("value", 0.012)
        self.slice_length.setObjectName("slice_length")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.slice_length)
        self.label_16 = QtWidgets.QLabel(self.groupBox_5)
        self.label_16.setObjectName("label_16")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.noise_space = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        self.noise_space.setDecimals(3)
        self.noise_space.setProperty("value", 0.1)
        self.noise_space.setObjectName("noise_space")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.noise_space)
        self.verticalLayout.addWidget(self.groupBox_5)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 60))
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 60))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.run_button = QtWidgets.QPushButton(self.groupBox_4)
        self.run_button.setObjectName("run_button")
        self.gridLayout_4.addWidget(self.run_button, 0, 1, 1, 1)
        self.vnacfg_button = QtWidgets.QPushButton(self.groupBox_4)
        self.vnacfg_button.setObjectName("vnacfg_button")
        self.gridLayout_4.addWidget(self.vnacfg_button, 0, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_4.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        Noise_mainwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Noise_mainwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 626, 23))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menusetting = QtWidgets.QMenu(self.menubar)
        self.menusetting.setObjectName("menusetting")
        Noise_mainwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Noise_mainwindow)
        self.statusbar.setObjectName("statusbar")
        Noise_mainwindow.setStatusBar(self.statusbar)
        self.actionopen = QtWidgets.QAction(Noise_mainwindow)
        self.actionopen.setObjectName("actionopen")
        self.actionsave = QtWidgets.QAction(Noise_mainwindow)
        self.actionsave.setObjectName("actionsave")
        self.menufile.addAction(self.actionopen)
        self.menufile.addAction(self.actionsave)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menusetting.menuAction())

        self.retranslateUi(Noise_mainwindow)
        self.run_button.clicked.connect(self.lcdNumber.setDecMode)
        QtCore.QMetaObject.connectSlotsByName(Noise_mainwindow)

    def retranslateUi(self, Noise_mainwindow):
        _translate = QtCore.QCoreApplication.translate
        Noise_mainwindow.setWindowTitle(_translate("Noise_mainwindow", "MainWindow"))
        self.label.setText(_translate("Noise_mainwindow", "Run"))
        self.groupBox_2.setTitle(_translate("Noise_mainwindow", "Load configuration"))
        self.pushButton_3.setText(_translate("Noise_mainwindow", "Run cfg"))
        self.chipcfg_button.setText(_translate("Noise_mainwindow", "Chip cfg"))
        self.groupBox.setTitle(_translate("Noise_mainwindow", "Noise config"))
        self.label_2.setText(_translate("Noise_mainwindow", "LO"))
        self.label_3.setText(_translate("Noise_mainwindow", "time"))
        self.label_5.setText(_translate("Noise_mainwindow", "RX"))
        self.label_4.setText(_translate("Noise_mainwindow", "TX"))
        self.label_6.setText(_translate("Noise_mainwindow", "Rate"))
        self.label_12.setText(_translate("Noise_mainwindow", "Decimation"))
        self.groupBox_5.setTitle(_translate("Noise_mainwindow", "Trigger"))
        self.label_13.setText(_translate("Noise_mainwindow", "Mode"))
        self.trigger_mode.setItemText(0, _translate("Noise_mainwindow", "Both"))
        self.trigger_mode.setItemText(1, _translate("Noise_mainwindow", "Noise"))
        self.trigger_mode.setItemText(2, _translate("Noise_mainwindow", "Pulse"))
        self.label_14.setText(_translate("Noise_mainwindow", "Threshold"))
        self.threshold_mode.setItemText(0, _translate("Noise_mainwindow", "Rotate"))
        self.threshold_mode.setItemText(1, _translate("Noise_mainwindow", "Pha"))
        self.threshold_mode.setItemText(2, _translate("Noise_mainwindow", "Mag"))
        self.label_15.setText(_translate("Noise_mainwindow", "Slice"))
        self.label_16.setText(_translate("Noise_mainwindow", "Space"))
        self.groupBox_3.setTitle(_translate("Noise_mainwindow", "Tone config"))
        self.pushButton.setText(_translate("Noise_mainwindow", "Tones"))
        self.groupBox_4.setTitle(_translate("Noise_mainwindow", "GroupBox"))
        self.run_button.setText(_translate("Noise_mainwindow", "Run"))
        self.vnacfg_button.setText(_translate("Noise_mainwindow", "Save cfg"))
        self.pushButton_4.setText(_translate("Noise_mainwindow", "Stop run"))
        self.menufile.setTitle(_translate("Noise_mainwindow", "file"))
        self.menusetting.setTitle(_translate("Noise_mainwindow", "setting"))
        self.actionopen.setText(_translate("Noise_mainwindow", "open hdf5"))
        self.actionsave.setText(_translate("Noise_mainwindow", " save data"))
