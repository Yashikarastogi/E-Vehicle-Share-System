# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 15:14:22 2022
Presenter file of rent vehicle page
@author: Calvin Pfob
"""
from PyQt5 import QtWidgets
from rentVehiclePage import Ui_MainWindowRentVehicle
import presenterVehicleInRent
import presenterCustomer
from customer import Customer
from mySQL import loadAllCityLocations, loadVehicles
import pandas as pd
from Order import Order


class PresenterRentVehicle():
    def __init__(self, window: QtWidgets.QMainWindow, customer: Customer):
        """
        Constructor of PresenterRentVehicle class

        Parameters
        ----------
        window : QtWidgets.QMainWindow
            Main window to visualize UI page to user.
        customer : Customer
            Object of customer that is currently logged in.

        Returns
        -------
        None.

        """
        self.uiRentVehicle = Ui_MainWindowRentVehicle()  # Create an instance ui class
        self.window = window
        self.uiRentVehicle.setupUi(self.window)
        self.currentCustomer = customer

        # load city Locations
        cityLocations = loadAllCityLocations()
        for _, locationName in cityLocations["cityLocationName"].items():
            QtWidgets.QListWidgetItem(locationName, self.uiRentVehicle.rentLocationList)

        # load vehicle types:
        vehicles =  loadVehicles()
        vehicleTypes = vehicles["vehicleTypeName"].unique()
        self.uiRentVehicle.vehicleTypeComboBox.addItems(vehicleTypes)

        self.uiRentVehicle.goBackButton.clicked.connect(lambda: self.goBack())
        self.uiRentVehicle.requestRentButton.clicked.connect(lambda: self.requestRent(cityLocations, vehicles))


    def goBack(self):
        """
        Return to customer main page.

        Returns
        -------
        None.

        """
        presenterCustomer.PresenterCustomer(self.window, self.currentCustomer)

    def requestRent(self, cityLocations: pd.DataFrame, vehicles: pd.DataFrame):
        """
        Request to rent a vehicle of specific vehicle type and for a specific rent time at a cityLocation.
        User will be notified whether suitable vehicle is available and if user input was valid or not

        Parameters
        ----------
        cityLocations : pd.DataFrame
            Data of all registered cityLocations.
        vehicles : pd.DataFrame
            Data of all registered vehicles.

        Returns
        -------
        None.

        """
        vehicleType = self.uiRentVehicle.vehicleTypeComboBox.currentText()
        vehicleTypeId = vehicles[vehicles["vehicleTypeName"]==vehicleType]["vehicleTypeId"].iloc[0]
        rentLocation = self.uiRentVehicle.rentLocationList.currentRow()
        rentTime = self.uiRentVehicle.rentTimeEntry.text()
        try:
            # check if rentTime amount is valid
            rentTime = float(rentTime)
        except ValueError:
            print("Rent time invalid or not specified at all")
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Rent vehicle notification")
            msg.setText("Rent time invalid or not specified at all")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.exec_()
            return
        if rentLocation == -1:
            # no location has been selected
            print("No rent location has been selected")
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Rent vehicle notification")
            msg.setText("No rent location has been selected")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.exec_()
        else:
            # rent vehicle
            rentLocationId = cityLocations["cityLocationId"].iloc[rentLocation]
            rentRequestPossible = self.currentCustomer.rentVehicle(rentLocationId, vehicleTypeId, rentTime)

            if rentRequestPossible:
                # rent request was successful
                currentOrder = Order(orderId = self.currentCustomer.orderId)
                print("Rent vehicle was successful. The rented vehicle has the id: " + str(currentOrder.vehicleId) + ". Have fun!")
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Rent vehicle notification")
                msg.setText("Rent vehicle was successful. The rented vehicle has the id: " + str(currentOrder.vehicleId) + ". Have fun!")
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.exec_()
                presenterVehicleInRent.PresenterVehicleInRent(self.window, self.currentCustomer, currentOrder, cityLocations)
            else:
                # no suitable vehicle available
                print("No suitable vehicle available at rent location or account balance insufficient. We apologize for that!")
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Rent vehicle notification")
                msg.setText("No suitable vehicle available at rent location or account balance insufficient. We apologize for that!")
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.exec_()
                return
