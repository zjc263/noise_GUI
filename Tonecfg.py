# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tonecfg.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tonecfg(object):
    def setupUi(self, tonecfg):
        tonecfg.setObjectName("tonecfg")
        tonecfg.resize(755, 843)
        self.centralwidget = QtWidgets.QWidget(tonecfg)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setObjectName("save")
        self.horizontalLayout.addWidget(self.save)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.add_row = QtWidgets.QPushButton(self.groupBox)
        self.add_row.setObjectName("add_row")
        self.horizontalLayout_2.addWidget(self.add_row)
        self.del_row = QtWidgets.QPushButton(self.groupBox)
        self.del_row.setObjectName("del_row")
        self.horizontalLayout_2.addWidget(self.del_row)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout.addWidget(self.groupBox)
        tonecfg.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(tonecfg)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 755, 23))
        self.menubar.setObjectName("menubar")
        tonecfg.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(tonecfg)
        self.statusbar.setObjectName("statusbar")
        tonecfg.setStatusBar(self.statusbar)

        self.retranslateUi(tonecfg)
        QtCore.QMetaObject.connectSlotsByName(tonecfg)

    def retranslateUi(self, tonecfg):
        _translate = QtCore.QCoreApplication.translate
        tonecfg.setWindowTitle(_translate("tonecfg", "MainWindow"))
        self.label_3.setText(_translate("tonecfg", "Tone number"))
        self.pushButton.setText(_translate("tonecfg", "start"))
        self.save.setText(_translate("tonecfg", "close save"))
        self.groupBox.setTitle(_translate("tonecfg", "GroupBox"))
        self.pushButton_2.setText(_translate("tonecfg", "PushButton"))
        self.add_row.setText(_translate("tonecfg", "addRow"))
        self.del_row.setText(_translate("tonecfg", "delRow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("tonecfg", "tone"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("tonecfg", "Freq(MHz)"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("tonecfg", "threshold"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("tonecfg", "alpha"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("tonecfg", "power(dBm)"))