# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1019, 683)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.insertButton = QtWidgets.QPushButton(self.centralwidget)
        self.insertButton.setGeometry(QtCore.QRect(60, 170, 111, 31))
        self.insertButton.setObjectName("insertButton")
        self.labels1 = QtWidgets.QLabel(self.centralwidget)
        self.labels1.setGeometry(QtCore.QRect(30, 70, 91, 16))
        self.labels1.setObjectName("labels1")
        self.labels2 = QtWidgets.QLabel(self.centralwidget)
        self.labels2.setGeometry(QtCore.QRect(30, 40, 91, 16))
        self.labels2.setObjectName("labels2")
        self.labels3 = QtWidgets.QLabel(self.centralwidget)
        self.labels3.setGeometry(QtCore.QRect(30, 100, 91, 16))
        self.labels3.setObjectName("labels3")
        self.MplWidget = MplWidget(self.centralwidget)
        self.MplWidget.setEnabled(True)
        self.MplWidget.setGeometry(QtCore.QRect(460, 20, 500, 500))
        self.MplWidget.setMouseTracking(True)
        self.MplWidget.setTabletTracking(True)
        self.MplWidget.setObjectName("MplWidget")
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(270, 20, 141, 61))
        self.resetButton.setObjectName("resetButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 40, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit2.setGeometry(QtCore.QRect(100, 70, 113, 20))
        self.lineEdit2.setObjectName("lineEdit2")
        self.lineEdit3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit3.setGeometry(QtCore.QRect(100, 100, 113, 20))
        self.lineEdit3.setObjectName("lineEdit3")
        self.labels4 = QtWidgets.QLabel(self.centralwidget)
        self.labels4.setGeometry(QtCore.QRect(30, 130, 91, 16))
        self.labels4.setObjectName("labels4")
        self.lineEdit4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit4.setGeometry(QtCore.QRect(100, 130, 113, 20))
        self.lineEdit4.setObjectName("lineEdit4")
        self.createButton = QtWidgets.QPushButton(self.centralwidget)
        self.createButton.setGeometry(QtCore.QRect(270, 100, 141, 61))
        self.createButton.setObjectName("createButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 210, 405, 210))
        self.tableWidget.setMinimumSize(QtCore.QSize(211, 0))
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.hslider = QtWidgets.QSlider(self.centralwidget)
        self.hslider.setGeometry(QtCore.QRect(610, 570, 261, 22))
        self.hslider.setMinimum(-180)
        self.hslider.setMaximum(180)
        self.hslider.setOrientation(QtCore.Qt.Horizontal)
        self.hslider.setObjectName("hslider")
        self.labels5 = QtWidgets.QLabel(self.centralwidget)
        self.labels5.setGeometry(QtCore.QRect(470, 570, 111, 21))
        self.labels5.setObjectName("labels5")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(470, 540, 121, 22))
        self.comboBox.setObjectName("comboBox")
        self.hslider2 = QtWidgets.QSlider(self.centralwidget)
        self.hslider2.setGeometry(QtCore.QRect(610, 610, 261, 22))
        self.hslider2.setMinimum(-180)
        self.hslider2.setMaximum(180)
        self.hslider2.setOrientation(QtCore.Qt.Horizontal)
        self.hslider2.setObjectName("hslider2")
        self.labels6 = QtWidgets.QLabel(self.centralwidget)
        self.labels6.setGeometry(QtCore.QRect(470, 610, 111, 21))
        self.labels6.setObjectName("labels6")
        self.comboBox2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox2.setGeometry(QtCore.QRect(20, 10, 91, 22))
        self.comboBox2.setEditable(False)
        self.comboBox2.setObjectName("comboBox2")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.tableWidget2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget2.setGeometry(QtCore.QRect(50, 450, 331, 191))
        self.tableWidget2.setObjectName("tableWidget2")
        self.tableWidget2.setColumnCount(3)
        self.tableWidget2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(2, item)
        self.labels1.raise_()
        self.labels2.raise_()
        self.labels3.raise_()
        self.MplWidget.raise_()
        self.resetButton.raise_()
        self.lineEdit.raise_()
        self.lineEdit2.raise_()
        self.lineEdit3.raise_()
        self.labels4.raise_()
        self.lineEdit4.raise_()
        self.createButton.raise_()
        self.tableWidget.raise_()
        self.hslider.raise_()
        self.labels5.raise_()
        self.comboBox.raise_()
        self.hslider2.raise_()
        self.labels6.raise_()
        self.insertButton.raise_()
        self.comboBox2.raise_()
        self.tableWidget2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1019, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit, self.lineEdit2)
        MainWindow.setTabOrder(self.lineEdit2, self.lineEdit3)
        MainWindow.setTabOrder(self.lineEdit3, self.lineEdit4)
        MainWindow.setTabOrder(self.lineEdit4, self.insertButton)
        MainWindow.setTabOrder(self.insertButton, self.createButton)
        MainWindow.setTabOrder(self.createButton, self.resetButton)
        MainWindow.setTabOrder(self.resetButton, self.comboBox2)
        MainWindow.setTabOrder(self.comboBox2, self.tableWidget)
        MainWindow.setTabOrder(self.tableWidget, self.tableWidget2)
        MainWindow.setTabOrder(self.tableWidget2, self.comboBox)
        MainWindow.setTabOrder(self.comboBox, self.hslider)
        MainWindow.setTabOrder(self.hslider, self.hslider2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Forward Kinematic Simulator"))
        self.insertButton.setText(_translate("MainWindow", "Insert link"))
        self.labels1.setText(_translate("MainWindow", "alpha"))
        self.labels2.setText(_translate("MainWindow", "theta"))
        self.labels3.setText(_translate("MainWindow", "a"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        self.labels4.setText(_translate("MainWindow", "d"))
        self.createButton.setText(_translate("MainWindow", "Create Simulator"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "theta"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "alpha"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "a"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "d"))
        self.labels5.setText(_translate("MainWindow", "Joint theta Angle : "))
        self.labels6.setText(_translate("MainWindow", "Joint alpha Angle : "))
        self.comboBox2.setCurrentText(_translate("MainWindow", "Tangan"))
        self.comboBox2.setItemText(0, _translate("MainWindow", "Tangan"))
        self.comboBox2.setItemText(1, _translate("MainWindow", "Kaki"))
        item = self.tableWidget2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "X"))
        item = self.tableWidget2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Y"))
        item = self.tableWidget2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Z"))
from mplwidget import MplWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
