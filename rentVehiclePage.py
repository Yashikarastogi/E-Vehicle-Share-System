# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rentVehiclePage.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindowRentVehicle(object):
    def setupUi(self, MainWindowRentVehicle):
        MainWindowRentVehicle.setObjectName("MainWindowRentVehicle")
        MainWindowRentVehicle.resize(977, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/Users/Calvin Pfob/Documents/guiDev/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindowRentVehicle.setWindowIcon(icon)
        MainWindowRentVehicle.setIconSize(QtCore.QSize(25, 25))
        self.rentVehiclePage = QtWidgets.QWidget(MainWindowRentVehicle)
        self.rentVehiclePage.setObjectName("rentVehiclePage")
        self.title = QtWidgets.QLabel(self.rentVehiclePage)
        self.title.setGeometry(QtCore.QRect(0, 10, 981, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.backgroundPicture = QtWidgets.QLabel(self.rentVehiclePage)
        self.backgroundPicture.setGeometry(QtCore.QRect(0, 0, 981, 481))
        self.backgroundPicture.setStyleSheet("background-image: url(:/login/tier-mobility-2021-05-min.png);")
        self.backgroundPicture.setText("")
        self.backgroundPicture.setPixmap(QtGui.QPixmap(":/login/tier-mobility-2021-05-min.png"))
        self.backgroundPicture.setScaledContents(True)
        self.backgroundPicture.setObjectName("backgroundPicture")
        self.requestRentButton = QtWidgets.QPushButton(self.rentVehiclePage)
        self.requestRentButton.setGeometry(QtCore.QRect(540, 410, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.requestRentButton.setFont(font)
        self.requestRentButton.setStyleSheet("background-color: rgba(85, 153, 255, 150); color: white")
        self.requestRentButton.setObjectName("requestRentButton")
        self.backgroundFrame = QtWidgets.QFrame(self.rentVehiclePage)
        self.backgroundFrame.setGeometry(QtCore.QRect(0, 0, 981, 481))
        self.backgroundFrame.setStyleSheet("background:rgba(0, 0, 0, 50)")
        self.backgroundFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.backgroundFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.backgroundFrame.setObjectName("backgroundFrame")
        self.vehicleTypeLabel = QtWidgets.QLabel(self.backgroundFrame)
        self.vehicleTypeLabel.setGeometry(QtCore.QRect(460, 160, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.vehicleTypeLabel.setFont(font)
        self.vehicleTypeLabel.setStyleSheet("color:rgb(255, 255, 255)")
        self.vehicleTypeLabel.setObjectName("vehicleTypeLabel")
        self.rentTimeEntry = QtWidgets.QLineEdit(self.backgroundFrame)
        self.rentTimeEntry.setGeometry(QtCore.QRect(590, 240, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(True)
        self.rentTimeEntry.setFont(font)
        self.rentTimeEntry.setAutoFillBackground(False)
        self.rentTimeEntry.setStyleSheet("background-color:white")
        self.rentTimeEntry.setText("")
        self.rentTimeEntry.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.rentTimeEntry.setObjectName("rentTimeEntry")
        self.rentTimeLabel = QtWidgets.QLabel(self.backgroundFrame)
        self.rentTimeLabel.setGeometry(QtCore.QRect(440, 250, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.rentTimeLabel.setFont(font)
        self.rentTimeLabel.setStyleSheet("color:rgb(255, 255, 255)")
        self.rentTimeLabel.setObjectName("rentTimeLabel")
        self.rentLocationLabel = QtWidgets.QLabel(self.backgroundFrame)
        self.rentLocationLabel.setGeometry(QtCore.QRect(120, 110, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.rentLocationLabel.setFont(font)
        self.rentLocationLabel.setStyleSheet("color:rgb(255, 255, 255)")
        self.rentLocationLabel.setObjectName("rentLocationLabel")
        self.rentLocationList = QtWidgets.QListWidget(self.backgroundFrame)
        self.rentLocationList.setGeometry(QtCore.QRect(120, 140, 256, 171))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.rentLocationList.setFont(font)
        self.rentLocationList.setAutoFillBackground(True)
        self.rentLocationList.setStyleSheet("color: white")
        self.rentLocationList.setObjectName("rentLocationList")
        self.vehicleTypeComboBox = QtWidgets.QComboBox(self.backgroundFrame)
        self.vehicleTypeComboBox.setGeometry(QtCore.QRect(590, 150, 211, 31))
        self.vehicleTypeComboBox.setAutoFillBackground(False)
        self.vehicleTypeComboBox.setStyleSheet("background-color: rgba(255, 255, 255, 255)")
        self.vehicleTypeComboBox.setObjectName("vehicleTypeComboBox")
        self.goBackButton = QtWidgets.QPushButton(self.rentVehiclePage)
        self.goBackButton.setGeometry(QtCore.QRect(260, 410, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.goBackButton.setFont(font)
        self.goBackButton.setStyleSheet("background-color: rgba(85, 153, 255, 150); color: white")
        self.goBackButton.setObjectName("goBackButton")
        self.backgroundPicture.raise_()
        self.backgroundFrame.raise_()
        self.title.raise_()
        self.requestRentButton.raise_()
        self.goBackButton.raise_()
        MainWindowRentVehicle.setCentralWidget(self.rentVehiclePage)

        self.retranslateUi(MainWindowRentVehicle)
        QtCore.QMetaObject.connectSlotsByName(MainWindowRentVehicle)

    def retranslateUi(self, MainWindowRentVehicle):
        _translate = QtCore.QCoreApplication.translate
        MainWindowRentVehicle.setWindowTitle(_translate("MainWindowRentVehicle", "E-Vehicle Share System"))
        self.title.setText(_translate("MainWindowRentVehicle", "<html><head/><body><p><span style=\" font-size:36pt; color:#ffffff;\">Rent vehicle</span></p></body></html>"))
        self.requestRentButton.setText(_translate("MainWindowRentVehicle", "Request Rent"))
        self.vehicleTypeLabel.setText(_translate("MainWindowRentVehicle", "Vehicle type: "))
        self.rentTimeLabel.setText(_translate("MainWindowRentVehicle", "Rent time (min): "))
        self.rentLocationLabel.setText(_translate("MainWindowRentVehicle", "Rent location: "))
        self.goBackButton.setText(_translate("MainWindowRentVehicle", "Go back"))
import bg_rc
