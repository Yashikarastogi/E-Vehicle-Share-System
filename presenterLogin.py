# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 16:02:53 2022
Presenter file of Log-in
@author: Calvin Pfob
"""
from PyQt5 import QtWidgets
from loginPage import Ui_MainWindowLogin
import presenterRegistration
from mySQL import loadUsers, loadVehicles, loadOrders
import presenterCustomer
from customer import Customer
from operatorUser import Operator
from manager import Manager
from presenterOperator import presenterOperator
import presenterManager
import image_total

class PresenterLogin():
    """
    Presenter class of login page
    """
    def __init__(self, window: QtWidgets.QMainWindow):
        """
        Constructor of presenter of login page

        Parameters
        ----------
        window : QtWidgets.QMainWindow
            Main window for show page to user.

        Returns
        -------
        None.

        """
        self.uiLogIn = Ui_MainWindowLogin() # Create an instance of our class
        self.window = window
        self.uiLogIn.setupUi(self.window)
        self.uiLogIn.logInButton.clicked.connect(lambda: self.logInCheck())
        self.uiLogIn.registerButton.clicked.connect(lambda: presenterRegistration.PresenterRegistration(self.window))

    def logInCheck(self):
        """
        Check if username and password is matching to database entry and load according page based
        on user type (operator, manager, customer)

        Returns
        -------
        None.

        """
        username = self.uiLogIn.usernameEntry.text()
        password = self.uiLogIn.passwordEntry.text()
        userDf = loadUsers()

        filteredDf = userDf[(userDf["userName"] == username) & (userDf["userPassword"] == password)]
        if filteredDf.empty:
            print("Either wrong password or username")
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Login notification")
            msg.setText("Login unsuccessful. Either password or username is wrong.")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.exec_()
    
        else:
            userType = filteredDf["userType"].reset_index(drop=True)[0].title()
            print("Log in successful for user type:", userType)
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Login notification")
            msg.setText("Login successful for user type: " + userType)
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.exec_()
            userId = filteredDf["userID"].reset_index(drop=True)[0]
            if userType.lower() == "customer":
                customer = Customer(userId)
                presenterCustomer.PresenterCustomer(self.window, customer)
                # call customer Page with userId information
            elif userType.lower() == "operator":
                operator = Operator(userId)
                presenterOperator(self.window, operator)
            else:  # userType.lower() == "manager"
                # call manager page with userId information
                dataframeV = loadVehicles()
                dataframeO = loadOrders()
                image_total.image1(dataframeO, dataframeV)
                image_total.image2(dataframeO, dataframeV)
                image_total.image3(dataframeO, dataframeV, 'Proportion of vehicle status in each block') 
                image_total.image4_test(dataframeO, dataframeV)
                image_total.image5(dataframeO, dataframeV)
                presenterManager.presenterManger(self.window)