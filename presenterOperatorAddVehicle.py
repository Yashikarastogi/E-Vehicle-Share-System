# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 20:52:08 2022

@author: ZHOU
"""
import sys
from PyQt5 import QtWidgets
from addVehiclePage import Ui_MainWindowOperatorAddVehicle
import presenterOperator
import mySQL as mySQL
# this can be removed if sy

class presenterOperatorAddVehicle():
    def __init__(self, window,operator):
        """
        Constructor of presenterOperatorAddVehicle class.

        Parameters
        ----------
        window : QtWidgets.QMainWindow
            Main Window to visualize page in UI.
        operator : Operator
           Object of operator that is currently logged in.

        Returns
        -------
        None.

        """
        self.operator =operator
        self.uiOperatoraddVehicle = Ui_MainWindowOperatorAddVehicle() # Create an instance of our class
        self.uiOperatoraddVehicle.setupUi(window)
        self.updatecity()
        
        self.uiOperatoraddVehicle.backButton.clicked.connect(lambda: presenterOperator.presenterOperator(window,operator))
        self.uiOperatoraddVehicle.addButton.clicked.connect(lambda: self.addVehicle())
    
    def updatecity(self):
        """
        update the content in the comboboxcitylocation according to the database.

        Returns
        -------
        None.

        """
        self.uiOperatoraddVehicle.comboBoxCitylocation.clear()
        citylocationDF = mySQL.loadAllCityLocations()
        list1 = citylocationDF["cityLocationName"].values.tolist()
        cList = list(map(str,list1))
        self.uiOperatoraddVehicle.comboBoxCitylocation.addItems(cList)
    
    def checkcity(self,cityName):
        """
        change the name of citylcation into the id of citylocation
        
        Parameters
        ----------
        cityName : String
            The name of citylocation.

        Returns
        -------
        cityloctionId : int
            The id of citylocation.

        """
        citylocationDF = mySQL.loadAllCityLocations()
        citylocationIdlist = list(citylocationDF[citylocationDF["cityLocationName"] == cityName]["cityLocationId"])
        cityloctionId = citylocationIdlist[0] 
        return cityloctionId
    
    def addVehicle(self):
        """
        add a new vehicle according to the inputs into database directly.

        Returns
        -------
        None.

        """
        print(mySQL.loadVehicles())  
        citylocation = self.uiOperatoraddVehicle.comboBoxCitylocation.currentText()
        vehicleType = self.uiOperatoraddVehicle.comboBoxVehicleType.currentText()
        print(citylocation)
        print(vehicleType)
        if vehicleType == "bike":
            vehicleType = 1
        elif vehicleType == "scooter":
            vehicleType = 2
        
        citylocationId = self.checkcity(citylocation)
        
        print(vehicleType)
        print(citylocationId)
        print(type(vehicleType))
        print(type(citylocationId))
        
        mySQL.addNewVehicle(vtype = vehicleType, vstatus = 1, batterySoc = 1, cityLocationId =citylocationId)
        print(mySQL.loadVehicles())
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("add Sucessfully")
        msg.setText("add successfully.")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.exec_()