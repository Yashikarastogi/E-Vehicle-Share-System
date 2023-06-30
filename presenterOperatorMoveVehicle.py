# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 11:31:23 2022

@author: ZHOU
"""
import sys
from PyQt5 import QtWidgets
from moveVehiclePage import Ui_MainWindowOperatorMoveVehicle
import presenterOperator
# import presenterRegistration
# this can be removed if system is connected
# sys.path.insert(1, 'C:/Users/Calvin Pfob/Documents/sqlKristen')
import mySQL as mySQL
from PyQt5 import QtCore, QtGui, QtWidgets


class presenterOperatorMoveVehicle():
    def __init__(self, window,operator):
        """
        Constructor of presenterOperatorMoveVehicle class.

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
        self.uiOperatorMoveVehicle = Ui_MainWindowOperatorMoveVehicle() # Create an instance of our class
        # self.operator = operator
        self.uiOperatorMoveVehicle.setupUi(window)

        self.updatevehicle()
        self.updatecity()
        
        self.uiOperatorMoveVehicle.backButton.clicked.connect(lambda: presenterOperator.presenterOperator(window,operator))
        self.uiOperatorMoveVehicle.moveButton.clicked.connect(lambda: self.moveVehicle(window))
     
    def updatevehicle(self):
        """
        update the content in the comboboxvehicle according to the database.

        Returns
        -------
        None.

        """
        self.uiOperatorMoveVehicle.comboBoxVehicle.clear()
        vehicleDF = mySQL.loadVehicles()
        list1 = vehicleDF["vehicleID"].values.tolist()
        vList1 = list(map(str,list1))
        vList2 = vehicleDF["cityLocationName"].values.tolist()
       
        listv = zip(vList1,vList2)
        for item in listv:
            self.uiOperatorMoveVehicle.comboBoxVehicle.addItem(str(item[0])+"  "+item[1])
        
    def updatecity(self):
        """
        update the content in the comboboxcitylocation according to the database.

        Returns
        -------
        None.

        """
        self.uiOperatorMoveVehicle.comboBoxCitylocation.clear()
        citylocationDF = mySQL.loadAllCityLocations()
        list1 = citylocationDF["cityLocationName"].values.tolist()
        cList = list(map(str,list1))
        self.uiOperatorMoveVehicle.comboBoxCitylocation.addItems(cList)
      
    def moveVehicle(self,window):
        """
        move the vhicle to the specified citylocation.

        Parameters
        ----------
        window : QtWidgets.QMainWindow
            Main Window to visualize page in UI.

        Returns
        -------
        None.

        """
        citylocation = self.uiOperatorMoveVehicle.comboBoxCitylocation.currentText()
        vehicle = self.uiOperatorMoveVehicle.comboBoxVehicle.currentText()
        print(citylocation)
        print(vehicle)
        listvehicle=vehicle.split()
        citylocationDF = mySQL.loadAllCityLocations()
        citylocationIdlist = list(citylocationDF[citylocationDF["cityLocationName"] == citylocation]["cityLocationId"])
        print("City: "+str( citylocationIdlist[0]))
       # print(type(citylocationId))
        print("Vehicle "+str(listvehicle[0]))
       
        vehicleId = int(listvehicle[0])
        cityloctionId = citylocationIdlist[0] 
        # print(type(vehicleId ))
        # print(type(cityloctionId))
        #### operator.moveVehicle( vehicleId= vehicleId, cityLocationId=cityloctionId)
        self.operator.moveVehicle( vehicleId= vehicleId, cityLocationId=cityloctionId)
#        presenterOperatorMoveVehicle.presenterOperatorMoveVehicle(window)
        self.updatevehicle()
        self.updatecity()
        
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("change Sucessfully")
        msg.setText("Change successfully.")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.exec_()