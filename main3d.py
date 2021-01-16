import numpy as np

import sys
#sys.path.append(".")
from calculator import calculator
import calculator as fk
from MainUI import *


class main3d(Ui_MainWindow):
    dhTable = fk.dhTable
    count = 0
    row = 0
    index = 0
    created = False
    sliderCreated = False
    kaki = False

    def __init__(self, window):
        self.setupUi(window)
        self.labels5.setText("Joint Angle: ")
        self.labels6.setText("Joint Angle: ")
        self.createButton.setEnabled(False)
        self.resetButton.setEnabled(False)
        self.insertButton.setEnabled(False)
        self.insertButton.setAutoDefault(True)
        self.hslider.setEnabled(False)
        self.hslider2.setEnabled(False)
        self.comboBox.setEnabled(False)

        #process
        self.insertButton.clicked.connect(self.insertDH)
        self.createButton.clicked.connect(self.createSimulator)
        self.resetButton.clicked.connect(self.reset)
        self.comboBox.currentIndexChanged.connect(self.indexChanged)
        self.comboBox2.currentIndexChanged.connect(self.indexChanged2)
        self.tableWidget.itemChanged.connect(self.tableChanged)
        self.hslider.valueChanged.connect(self.label1)
        self.hslider2.valueChanged.connect(self.label2)
        self.lineEdit.returnPressed.connect(self.insertButton.click)
        self.lineEdit2.returnPressed.connect(self.insertButton.click)
        self.lineEdit3.returnPressed.connect(self.insertButton.click)
        self.lineEdit4.returnPressed.connect(self.insertButton.click)
        self.lineEdit.setValidator(QtGui.QIntValidator(-999, 999))
        self.lineEdit2.setValidator(QtGui.QIntValidator(-999, 999))
        self.lineEdit3.setValidator(QtGui.QIntValidator(1, 99999))
        self.lineEdit4.setValidator(QtGui.QIntValidator(1, 99999))
        self.lineEdit.textChanged.connect(self.enableInsert)
        self.lineEdit2.textChanged.connect(self.enableInsert)
        self.lineEdit3.textChanged.connect(self.enableInsert)
        self.lineEdit4.textChanged.connect(self.enableInsert)
        # self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    # def onkey(self, event):
    #     print("berhasil")

    def insertDH(self):
        self.tableWidget.blockSignals(True)
        j1 = self.lineEdit.text()
        j2 = self.lineEdit2.text()
        j3 = self.lineEdit3.text()
        j4 = self.lineEdit4.text()

        self.count += 1
        if self.count == 1:
            self.dhTable = np.hstack((self.dhTable, np.array([np.deg2rad(int(j1)), np.deg2rad(int(j2)), int(j3), int(j4)])))
        else:
            self.dhTable = np.vstack((self.dhTable, np.array([np.deg2rad(int(j1)), np.deg2rad(int(j2)), int(j3), int(j4)])))
        self.lineEdit.clear()
        self.lineEdit2.clear()
        self.lineEdit3.clear()
        self.lineEdit4.clear()
        self.loadTable(j1,j2,j3,j4)
        self.comboBox.addItem("Joint " + str(self.count), self.count)
        self.lineEdit.setFocus()
        if self.count > 0:
            self.createButton.setEnabled(True)
            self.resetButton.setEnabled(True)
        self.tableWidget.blockSignals(False)

    def loadTable(self,j1,j2,j3,j4):
        self.tableWidget.setRowCount(self.count)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setItem(self.row, 0, QtWidgets.QTableWidgetItem(str(j1)))
        self.tableWidget.setItem(self.row, 1, QtWidgets.QTableWidgetItem(str(j2)))
        self.tableWidget.setItem(self.row, 2, QtWidgets.QTableWidgetItem(str(j3)))
        self.tableWidget.setItem(self.row, 3, QtWidgets.QTableWidgetItem(str(j4)))
        self.row += 1

    def loadXYZTable(self, ee):
        self.tableWidget2.setRowCount(self.count)
        self.tableWidget2.setColumnCount(3)
        if self.count == 1:
            self.tableWidget2.setItem(0, 0, QtWidgets.QTableWidgetItem(str('{:.2f}'.format(ee[0,self.count+1]))))
            self.tableWidget2.setItem(0, 1, QtWidgets.QTableWidgetItem(str('{:.2f}'.format(ee[1,self.count+1]))))
            self.tableWidget2.setItem(0, 2, QtWidgets.QTableWidgetItem(str('{:.2f}'.format(ee[2,self.count+1]))))
        else:
            for i in range(self.count):
                self.tableWidget2.setItem(i, 0, QtWidgets.QTableWidgetItem(str('{:.2f}'.format(ee[0, i+2]))))
                self.tableWidget2.setItem(i, 1, QtWidgets.QTableWidgetItem(str('{:.2f}'.format(ee[1, i+2]))))
                self.tableWidget2.setItem(i, 2, QtWidgets.QTableWidgetItem(str('{:.2f}'.format(ee[2, i+2]))))

    def reset(self):
        self.dhTable = ([])
        self.count = 0
        self.index = 0
        self.row = 0
        self.created = False
        self.sliderCreated = False
        self.createButton.setEnabled(False)
        self.resetButton.setEnabled(False)
        self.hslider.setEnabled(False)
        self.hslider2.setEnabled(False)
        self.comboBox.setEnabled(False)
        self.comboBox2.setEnabled(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget2.setRowCount(0)
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.draw()
        self.comboBox.clear()

    def createSimulator(self):
        self.tableWidget.blockSignals(True)
        self.hslider.blockSignals(True)
        self.hslider2.blockSignals(True)
        self.created = True
        self.comboBox.setEnabled(True)
        self.hslider.setProperty("value", self.tableWidget.item(self.index, 0).text())
        self.hslider2.setProperty("value", self.tableWidget.item(self.index, 1).text())
        self.labels5.setText("Joint Angle: " + str(self.tableWidget.item(0, 0).text()) + u'\N{DEGREE SIGN}')
        self.labels6.setText("Joint Angle: " + str(self.tableWidget.item(0, 1).text()) + u'\N{DEGREE SIGN}')
        self.slidercreated = True
        self.hslider.setEnabled(True)
        self.hslider2.setEnabled(True)
        self.comboBox2.setEnabled(False)

        self.draw()
        self.tableWidget.blockSignals(False)
        self.hslider.blockSignals(False)
        self.hslider2.blockSignals(False)

    def draw(self):
        Tm = calculator.dh_kine(self.dhTable, self.count)
        ee = calculator.xyzpos(Tm, self.count)
        x,y,z = ee[0,:],ee[1,:],ee[2,:]

        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(x, y, z, marker='o', color='green', linewidth=4, markersize=10)
        self.MplWidget.canvas.axes.text(ee[0,self.count+1], ee[1,self.count+1], ee[2,self.count+1], '({:.2f}, {:.2f}, {:.2f})'.format(ee[0,self.count+1], ee[1,self.count+1], ee[2,self.count+1]), weight='bold', fontsize=10,)

        self.MplWidget.canvas.axes.set_xlabel('x')
        self.MplWidget.canvas.axes.set_ylabel('y')
        self.MplWidget.canvas.axes.set_zlabel('z')
        self.MplWidget.canvas.axes.set_xlim([-10, 10])
        self.MplWidget.canvas.axes.set_ylim([-10, 10])
        self.loadXYZTable(ee)
        if self.kaki:
            self.MplWidget.canvas.axes.set_zlim([10, -10])
        else:
            self.MplWidget.canvas.axes.set_zlim([-10, 10])

        self.MplWidget.canvas.draw()

    def slider(self, joint):
        if self.count == 1:
            tupleToList = list(self.dhTable)
            tupleToList[0] = np.deg2rad(int(self.hslider.value()))
            tupleToList[1] = np.deg2rad(int(self.hslider2.value()))
            self.dhTable = tuple(tupleToList)
        else:
            tupleToList = list(self.dhTable[joint])
            tupleToList[0] = np.deg2rad(int(self.hslider.value()))
            tupleToList[1] = np.deg2rad(int(self.hslider2.value()))
            self.dhTable[joint] = tuple(tupleToList)
        self.draw()
        self.tableWidget.blockSignals(False)

    def indexChanged(self, index):
        self.index = index
        if self.created:
            self.hslider.setProperty("value", self.tableWidget.item(self.index, 0).text())
            self.hslider2.setProperty("value", self.tableWidget.item(self.index, 1).text())
            self.tableWidget.setItem(self.index, 0, QtWidgets.QTableWidgetItem(str(self.hslider.value())))
            self.tableWidget.setItem(self.index, 1, QtWidgets.QTableWidgetItem(str(self.hslider2.value())))

    def indexChanged2(self, index):
        if index == 1:
            self.kaki = True
        else:
            self.kaki = False

    def tableChanged(self, item):
        index = self.tableWidget.selectionModel().currentIndex().row()
        self.tableWidget.blockSignals(True)
        if self.count == 1:
            tupleToList = list(self.dhTable)
        else:
            tupleToList = list(self.dhTable[index])

        tupleToList[0] = np.deg2rad(int(self.tableWidget.item(index, 0).text()))
        tupleToList[1] = np.deg2rad(int(self.tableWidget.item(index, 1).text()))
        tupleToList[2] = int(self.tableWidget.item(index, 2).text())
        tupleToList[3] = int(self.tableWidget.item(index, 3).text())

        if self.count == 1:
            self.dhTable = tuple(tupleToList)
        else:
            self.dhTable[index] = tuple(tupleToList)

        self.tableWidget.blockSignals(False)
        if self.created and index == self.index:
            self.labels5.setText("Joint Angle: " + str(self.tableWidget.item(index, 0).text()) + u'\N{DEGREE SIGN}')
            self.labels6.setText("Joint Angle: " + str(self.tableWidget.item(index, 1).text()) + u'\N{DEGREE SIGN}')
            self.hslider.setProperty("value", self.tableWidget.item(index, 0).text())
            self.hslider2.setProperty("value", self.tableWidget.item(index, 1).text())

        self.draw()

    def label1(self):
        self.tableWidget.blockSignals(True)
        self.labels5.setText("Joint Angle: " + str(self.hslider.value()) + u'\N{DEGREE SIGN}')
        self.tableWidget.setItem(self.index, 0, QtWidgets.QTableWidgetItem(str(self.hslider.value())))
        self.slider(self.index)

    def label2(self):
        self.tableWidget.blockSignals(True)
        self.labels6.setText("Joint Angle: " + str(self.hslider2.value()) + u'\N{DEGREE SIGN}')
        self.tableWidget.setItem(self.index, 1, QtWidgets.QTableWidgetItem(str(self.hslider2.value())))
        self.slider(self.index)

    def enableInsert(self):
        if self.lineEdit.text() != "" and self.lineEdit2.text() != "" and self.lineEdit3.text() != "" and self.lineEdit4.text() != "":
            self.insertButton.setEnabled(True)
        else:
            self.insertButton.setEnabled(False)

app = QtWidgets.QApplication(sys.argv)
MainWindow=QtWidgets.QMainWindow()
ui=main3d(MainWindow)
MainWindow.show()
app.exec_()