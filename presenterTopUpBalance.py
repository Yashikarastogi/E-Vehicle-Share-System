# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 16:58:45 2022
Presenter Top Up Balance
@author: Calvin Pfob
"""
from PyQt5 import QtWidgets
from topUpBalancePage import Ui_MainWindowTopUpBalance
import presenterCustomer
from customer import Customer
from datetime import date


class PresenterTopUpBalance():
    def __init__(self, window: QtWidgets.QMainWindow, customer: Customer):
        """
        Constructor of PresenterTopUpBalacne class

        Parameters
        ----------
        window : QtWidgets.QMainWindow
            Main window for showing page to user.
        customer : Customer
            Current customer object that is logged in.

        Returns
        -------
        None.

        """
        self.uiTopUpBalance = Ui_MainWindowTopUpBalance()  # Create an instance of our class
        self.uiTopUpBalance.setupUi(window)
        self.currentCustomer = customer
        self.window = window
        self.uiTopUpBalance.goBackButton.clicked.connect(lambda: self.goBack())
        self.uiTopUpBalance.topUpButton.clicked.connect(lambda: self.topUpBalance())
        # set current Balance
        currentBalance = self.currentCustomer.userBalance
        self.uiTopUpBalance.currentBalanceOutput.setText("£‎" + str(currentBalance))


    def goBack(self):
        """
        Return to Customer Page

        Returns
        -------
        None.

        """
        presenterCustomer.PresenterCustomer(self.window, self.currentCustomer)


    def topUpBalance(self):
        """
        Check if provided details by user corresponds to a valid credit card. If this is the case and all checks are passed,
        the specified amount will e topped up to the customer balance

        Returns
        -------
        None.

        """
        cardHolderName = self.uiTopUpBalance.cardHolderNameEntry.text()
        cardNumber = self.uiTopUpBalance.cardNumberEntry.text()
        amountOfDigitCardNumber = sum(c.isdigit() for c in cardNumber)
        amountOfAlphaCardNumber = sum(c.isalpha() for c in cardNumber)
        cvv = self.uiTopUpBalance.cvvEntry.text()
        amountOfDigitCvv = sum(c.isdigit() for c in cvv)
        topUpAmount = self.uiTopUpBalance.topUpAmountEntry.text()
        expirationDate = self.uiTopUpBalance.expirationDateInput.date().toPyDate()
        if cardHolderName == "":
            print("Card holder name has not been specified.")
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Top-up balance notification")
            msg.setText("Card holder name has not been specified.")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.exec_()
        elif amountOfDigitCardNumber < 15 or amountOfDigitCardNumber > 19 or amountOfAlphaCardNumber is not 0:
            # check if card Number could be valid
            print("Card number is invalid.")
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Top-up balance notification")
            msg.setText("Card number is invalid.")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.exec_()
        elif len(cvv) > 4 or len(cvv) < 3 or len(cvv) is not amountOfDigitCvv:
            # check if cvv is valid
            print("Cvv is invalid.")
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Top-up balance notification")
            msg.setText("Cvv is invalid.")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.exec_()
        if expirationDate < date.today():
            # check if expiration date is valid
            print("Expiration date specified because card is expired.")
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Top-up balance notification")
            msg.setText("Expiration date specified because card is expired.")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.exec_()
        else:
            try:
                # check if top up amount is valid
                topUpAmount = float(topUpAmount)
            except ValueError:
                print("Top-up amount invalid or not specified at all")
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Top-up balance notification")
                msg.setText("Top-up amount invalid or not specified at all")
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.exec_()
                return
            self.currentCustomer.topUpBalance(topUpAmount)
            print("Successful top Up Balance")
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Top-up balance notification")
            msg.setText("Top-up process was successful. Your new balance is now : £" + str(self.currentCustomer.userBalance))
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.exec_()
            