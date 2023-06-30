# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registrationPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindowRegistration(object):
    def setupUi(self, MainWindowRegistration):
        MainWindowRegistration.setObjectName("MainWindowRegistration")
        MainWindowRegistration.resize(977, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/Users/Calvin Pfob/Documents/guiDevelopment/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindowRegistration.setWindowIcon(icon)
        MainWindowRegistration.setIconSize(QtCore.QSize(25, 25))
        self.registrationPage = QtWidgets.QWidget(MainWindowRegistration)
        self.registrationPage.setObjectName("registrationPage")
        self.title = QtWidgets.QLabel(self.registrationPage)
        self.title.setGeometry(QtCore.QRect(0, 10, 981, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.backgroundPicture = QtWidgets.QLabel(self.registrationPage)
        self.backgroundPicture.setGeometry(QtCore.QRect(0, 0, 981, 481))
        self.backgroundPicture.setStyleSheet("background-image: url(:/login/tier-mobility-2021-05-min.png);")
        self.backgroundPicture.setText("")
        self.backgroundPicture.setPixmap(QtGui.QPixmap(":/login/tier-mobility-2021-05-min.png"))
        self.backgroundPicture.setScaledContents(True)
        self.backgroundPicture.setObjectName("backgroundPicture")
        self.submitRegistration = QtWidgets.QPushButton(self.registrationPage)
        self.submitRegistration.setGeometry(QtCore.QRect(540, 410, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.submitRegistration.setFont(font)
        self.submitRegistration.setStyleSheet("background-color: rgba(85, 153, 255, 150); color: white")
        self.submitRegistration.setObjectName("submitRegistration")
        self.backgroundFrame = QtWidgets.QFrame(self.registrationPage)
        self.backgroundFrame.setGeometry(QtCore.QRect(0, 0, 981, 481))
        self.backgroundFrame.setStyleSheet("background:rgba(0, 0, 0, 50)")
        self.backgroundFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.backgroundFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.backgroundFrame.setObjectName("backgroundFrame")
        self.usernameEntry = QtWidgets.QLineEdit(self.backgroundFrame)
        self.usernameEntry.setGeometry(QtCore.QRect(360, 130, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.usernameEntry.setFont(font)
        self.usernameEntry.setStyleSheet("background-color:white")
        self.usernameEntry.setText("")
        self.usernameEntry.setObjectName("usernameEntry")
        self.usernameLabel = QtWidgets.QLabel(self.backgroundFrame)
        self.usernameLabel.setGeometry(QtCore.QRect(260, 140, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setStyleSheet("color:rgb(255, 255, 255)")
        self.usernameLabel.setObjectName("usernameLabel")
        self.passwordEntry = QtWidgets.QLineEdit(self.backgroundFrame)
        self.passwordEntry.setGeometry(QtCore.QRect(360, 200, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(True)
        self.passwordEntry.setFont(font)
        self.passwordEntry.setStyleSheet("background-color:white")
        self.passwordEntry.setText("")
        self.passwordEntry.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEntry.setObjectName("passwordEntry")
        self.passwordLabel = QtWidgets.QLabel(self.backgroundFrame)
        self.passwordLabel.setGeometry(QtCore.QRect(260, 210, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setStyleSheet("color:rgb(255, 255, 255)")
        self.passwordLabel.setObjectName("passwordLabel")
        self.passwordEntry_2 = QtWidgets.QLineEdit(self.backgroundFrame)
        self.passwordEntry_2.setGeometry(QtCore.QRect(360, 270, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(True)
        self.passwordEntry_2.setFont(font)
        self.passwordEntry_2.setStyleSheet("background-color:white")
        self.passwordEntry_2.setText("")
        self.passwordEntry_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEntry_2.setObjectName("passwordEntry_2")
        self.passwordLabelRepeat = QtWidgets.QLabel(self.backgroundFrame)
        self.passwordLabelRepeat.setGeometry(QtCore.QRect(210, 280, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.passwordLabelRepeat.setFont(font)
        self.passwordLabelRepeat.setStyleSheet("color:rgb(255, 255, 255)")
        self.passwordLabelRepeat.setObjectName("passwordLabelRepeat")
        self.checkBoxCustomer = QtWidgets.QCheckBox(self.backgroundFrame)
        self.checkBoxCustomer.setGeometry(QtCore.QRect(270, 340, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxCustomer.sizePolicy().hasHeightForWidth())
        self.checkBoxCustomer.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.checkBoxCustomer.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.checkBoxCustomer.setFont(font)
        self.checkBoxCustomer.setMouseTracking(True)
        self.checkBoxCustomer.setStyleSheet("QCheckBox::indicator { width: 15px; height: 15px;}; color: rgb(255, 255, 255);\n"
"")
        self.checkBoxCustomer.setIconSize(QtCore.QSize(100, 100))
        self.checkBoxCustomer.setObjectName("checkBoxCustomer")
        self.checkBoxOperator = QtWidgets.QCheckBox(self.backgroundFrame)
        self.checkBoxOperator.setGeometry(QtCore.QRect(460, 340, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxOperator.sizePolicy().hasHeightForWidth())
        self.checkBoxOperator.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.checkBoxOperator.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.checkBoxOperator.setFont(font)
        self.checkBoxOperator.setMouseTracking(True)
        self.checkBoxOperator.setStyleSheet("QCheckBox::indicator { width: 15px; height: 15px;}; color: rgb(255, 255, 255);\n"
"")
        self.checkBoxOperator.setIconSize(QtCore.QSize(100, 100))
        self.checkBoxOperator.setObjectName("checkBoxOperator")
        self.checkBoxManager = QtWidgets.QCheckBox(self.backgroundFrame)
        self.checkBoxManager.setGeometry(QtCore.QRect(660, 340, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxManager.sizePolicy().hasHeightForWidth())
        self.checkBoxManager.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.checkBoxManager.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.checkBoxManager.setFont(font)
        self.checkBoxManager.setMouseTracking(True)
        self.checkBoxManager.setStyleSheet("QCheckBox::indicator { width: 15px; height: 15px;}; color: rgb(255, 255, 255);\n"
"")
        self.checkBoxManager.setIconSize(QtCore.QSize(100, 100))
        self.checkBoxManager.setObjectName("checkBoxManager")
        self.userTypeLabel = QtWidgets.QLabel(self.backgroundFrame)
        self.userTypeLabel.setGeometry(QtCore.QRect(150, 350, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.userTypeLabel.setFont(font)
        self.userTypeLabel.setStyleSheet("color:rgb(255, 255, 255)")
        self.userTypeLabel.setObjectName("userTypeLabel")
        self.goBackButton = QtWidgets.QPushButton(self.registrationPage)
        self.goBackButton.setGeometry(QtCore.QRect(260, 410, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.goBackButton.setFont(font)
        self.goBackButton.setStyleSheet("background-color: rgba(85, 153, 255, 150); color: white")
        self.goBackButton.setObjectName("goBackButton")
        self.backgroundPicture.raise_()
        self.backgroundFrame.raise_()
        self.title.raise_()
        self.submitRegistration.raise_()
        self.goBackButton.raise_()
        MainWindowRegistration.setCentralWidget(self.registrationPage)

        self.retranslateUi(MainWindowRegistration)
        QtCore.QMetaObject.connectSlotsByName(MainWindowRegistration)

    def retranslateUi(self, MainWindowRegistration):
        _translate = QtCore.QCoreApplication.translate
        MainWindowRegistration.setWindowTitle(_translate("MainWindowRegistration", "E-Vehicle Share System"))
        self.title.setText(_translate("MainWindowRegistration", "<html><head/><body><p><span style=\" font-size:36pt; color:#ffffff;\">Registration</span></p></body></html>"))
        self.submitRegistration.setText(_translate("MainWindowRegistration", "Register"))
        self.usernameLabel.setText(_translate("MainWindowRegistration", "Username:"))
        self.passwordLabel.setText(_translate("MainWindowRegistration", "Password:"))
        self.passwordLabelRepeat.setText(_translate("MainWindowRegistration", "Repeat Password:"))
        self.checkBoxCustomer.setText(_translate("MainWindowRegistration", "Customer"))
        self.checkBoxOperator.setText(_translate("MainWindowRegistration", "Operator"))
        self.checkBoxManager.setText(_translate("MainWindowRegistration", "Manager"))
        self.userTypeLabel.setText(_translate("MainWindowRegistration", "User type:"))
        self.goBackButton.setText(_translate("MainWindowRegistration", "Go back"))
import bg_rc