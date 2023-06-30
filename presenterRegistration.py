# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 16:03:11 2022
Presenter of registration page.
@author: Calvin Pfob
"""
from PyQt5 import QtWidgets
from registrationPage import Ui_MainWindowRegistration
import presenterLogin
from mySQL import loadUsers, addNewUser

class PresenterRegistration():
    def __init__(self, window: QtWidgets.QMainWindow):
        """
        Constructor of PresenterRegistration class.

        Parameters
        ----------
        window : QtWidgets.QMainWindow
            Main Window to visualize page in UI.

        Returns
        -------
        None.

        """
        self.uiRegistration = Ui_MainWindowRegistration()
        self.uiRegistration.setupUi(window)
        self.window = window
        self.uiRegistration.submitRegistration.clicked.connect(lambda: self.submitRegistration())
        self.uiRegistration.goBackButton.clicked.connect(lambda: self.goBack())
        self.uiRegistration.checkBoxCustomer.clicked.connect(
            lambda: self.checkBoxSelect(self.uiRegistration.checkBoxOperator, self.uiRegistration.checkBoxManager))
        self.uiRegistration.checkBoxOperator.clicked.connect(
            lambda: self.checkBoxSelect(self.uiRegistration.checkBoxCustomer, self.uiRegistration.checkBoxManager))
        self.uiRegistration.checkBoxManager.clicked.connect(
            lambda: self.checkBoxSelect(self.uiRegistration.checkBoxOperator, self.uiRegistration.checkBoxCustomer))
    
    def goBack(self):
        """
        Return to Login Page

        Returns
        -------
        None.

        """
        presenterLogin.PresenterLogin(self.window)

    def submitRegistration(self):
        """
        Check if user input was valid for a successful registration. If all checks are passed, user will be registrated
        and entry to database will be made

        Returns
        -------
        None.

        """
        password = self.uiRegistration.passwordEntry.text()
        password2 = self.uiRegistration.passwordEntry_2.text()
        username = self.uiRegistration.usernameEntry.text()
        checkBoxCustomer = self.uiRegistration.checkBoxCustomer.isChecked()
        checkBoxOperator = self.uiRegistration.checkBoxOperator.isChecked()
        checkBoxManager = self.uiRegistration.checkBoxManager.isChecked()
        userDf = loadUsers()
        # check for wrong user input
        if not password == password2:
            print("Passwords are not matching")
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Registration notification")
            msg.setText("Registration unsuccessful. Passwords are not matching.")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.exec_()
        elif not len(password) >= 6:
            # password must be at least of length 6
            print("Passwords does not meet minimum requirements")
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Registration notification")
            msg.setText("Password must at least consist of 6 chars")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.exec_()
        elif not (checkBoxCustomer or checkBoxOperator or checkBoxManager):
            print("No user type has been specified")
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Registration notification")
            msg.setText("Registration unsuccessful. No user type has been specified.")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.exec_()
        elif not len(username) >= 6:
            # username must be at least of length 6
            print("Username does not meet minimum requirements")
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Registration notification")
            msg.setText("Username must at least consist of 6 chars")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.exec_()
        elif not userDf[userDf["userName"] == username].empty:
            print("Username already registrated. Choose a different name")
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Registration notification")
            msg.setText("Username already registrated. Choose a different nam")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.exec_()
        else:
            # valid registration
            if checkBoxCustomer:
                userType = 3
            elif checkBoxOperator:
                userType = 2
            else:  # manager
                userType = 1
            addNewUser(username, password, userType)
            print("Successful registration")
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Registration notification")
            msg.setText("Welcome to the community! Registration successful for user name: " + username)
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.exec_()
            presenterLogin.PresenterLogin(self.window)  # switch back to login screen

    def checkBoxSelect(self, checkBoxUnselect1: QtWidgets.QCheckBox, checkBoxUnselect2: QtWidgets.QCheckBox):
        """
        Ensures that only one Checkbox is checked at one time. If one additional checkBox is checked, the other checkboxes
        will be unchecked

        Parameters
        ----------
        checkBoxUnselect1 : QtWidgets.QCheckBox
            CheckBox to uncheck.
        checkBoxUnselect2 : QtWidgets.QCheckBox
            CheckBox to uncheck.

        Returns
        -------
        None.

        """
        checkBoxUnselect1.setChecked(False)
        checkBoxUnselect2.setChecked(False)
