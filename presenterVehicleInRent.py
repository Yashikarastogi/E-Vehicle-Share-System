# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 18:13:58 2022
Presenter of vehicle in rent page.
@author: Calvin Pfob
"""
from PyQt5 import QtWidgets
from vehicleInRentPage import Ui_MainWindowVehicleInRent
import presenterCustomer
from customer import Customer
from Order import Order
import pandas as pd

class PresenterVehicleInRent():
    def __init__(self, window: QtWidgets.QMainWindow, customer: Customer, order: Order, cityLocations: pd.DataFrame):
        """
        Constructor of Presenter Vehicle in rent class 

        Parameters
        ----------
        window : QtWidgets.QMainWindow
            Main window to show page to user.
        customer : Customer
            current customer that is logged in.
        order : Order
            current order that is active.
        cityLocations : pd.DataFrame
            Data from all available city locations.

        Returns
        -------
        None.

        """
        self.uiVehicleInRent = Ui_MainWindowVehicleInRent()  # Create an instance ui class
        self.window = window
        self.uiVehicleInRent.setupUi(self.window)
        self.currentCustomer = customer
        self.currentOrder = order

        # load return locations
        for _, locationName in cityLocations["cityLocationName"].items():
            QtWidgets.QListWidgetItem(locationName, self.uiVehicleInRent.returnLocationList)

        # load journey details
        self.uiVehicleInRent.vehicleIdOutput.setText(str(self.currentOrder.vehicleId))
        self.uiVehicleInRent.rentTimeOutput.setText(str(self.currentOrder.timeOrder))
        self.uiVehicleInRent.totalCostOutput.setText(str(self.currentOrder.priceTotal))

        self.uiVehicleInRent.returnVehicleButton.clicked.connect(lambda: self.returnVehicle(cityLocations))

    def returnVehicle(self, cityLocations: pd.DataFrame):
        """
        Checks if user input was valid for returning a vehicle. Further, customer can report issues and current balance
        will be shown to customer

        Parameters
        ----------
        cityLocations : pd.DataFrame
            Data from all available city locations..

        Returns
        -------
        None.

        """
        returnLocation = self.uiVehicleInRent.returnLocationList.currentRow()
        if returnLocation == -1:
            # no return location has been selected
            print("No return location has been selected")
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Current order notification")
            msg.setText("No return location has been selected")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.exec_()
        else:
            returnCityLocationId = cityLocations["cityLocationId"].iloc[returnLocation]
            self.currentCustomer.returnVehicle(self.currentOrder.vehicleId, returnCityLocationId)
            # no return vehicle is successful
            outputString = """Thanks for returning successfully the vehicle. The total costs have been deducted from your account balance.
                  Current balance: £""" + str(self.currentCustomer.userBalance)
            print(outputString)
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Current order notification")
            msg.setText(outputString)
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.exec_()
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Current order notification")
            msg.setIcon(QtWidgets.QMessageBox.Question)
            msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            msg.setText("Have there been any issues with the vehicle and want to report it?")
            retval = msg.exec_()
            if retval  == QtWidgets.QMessageBox.Yes:
                self.currentCustomer.reportVehicle(self.currentOrder.vehicleId)
                print("Thanks for reporting damaged vehicle. Our service team will try to fix it as soon as possible")
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Current order notification")
                msg.setText("Thanks for reporting damaged vehicle. Our service team will try to fix it as soon as possible")
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.exec_()
            else:
                # no issues with vehicle
                pass
            presenterCustomer.PresenterCustomer(self.window, self.currentCustomer)
