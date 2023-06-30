# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 17:35:52 2022

@author: ZHOU
"""
import sys
from PyQt5 import QtWidgets
from trackVehiclePage import Ui_MainWindowOperatorTrackVehicle
import presenterOperator
import mySQL as mySQL
# this can be removed if system is connected
# sys.path.insert(1, 'C:/Users/Calvin Pfob/Documents/sqlKristen')
#import presenterLogin


class presenterTrackVehicle():
    def __init__(self, window,operator):
        """
        Constructor of presenterTrackVehicle class.

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
        self.uiOperatorTrackVehcile = Ui_MainWindowOperatorTrackVehicle()
        
        self.uiOperatorTrackVehcile.setupUi(window)
        self.updatevehicle()
        self.updatecity()
        # self.uiOperatorTrackVehcile.retranslateUi(window)
        self.uiOperatorTrackVehcile.backButton.clicked.connect(lambda: presenterOperator.presenterOperator(window,operator))
        self.uiOperatorTrackVehcile.trackButton.clicked.connect(lambda: self.updatetxt())
    def updatevehicle(self):
        """
        update the content in the comboboxvehicle according to the database.

        Returns
        -------
        None.

        """
        self.uiOperatorTrackVehcile.comboBoxVehicle.clear()
        vehicleDF = mySQL.loadVehicles()
        list1 = vehicleDF["vehicleID"].values.tolist()
        vList = list(map(str,list1))
        vList.insert(0, " ")
        self.uiOperatorTrackVehcile.comboBoxVehicle.addItems(vList)
        
    def updatecity(self):
        """
        update the content in the comboboxcitylocation according to the database.

        Returns
        -------
        None.

        """
        self.uiOperatorTrackVehcile.comboBoxCitylocation.clear()
        citylocationDF = mySQL.loadAllCityLocations()
        list1 = citylocationDF["cityLocationName"].values.tolist()
        cList = list(map(str,list1))
        cList.insert(0, " ")
        self.uiOperatorTrackVehcile.comboBoxCitylocation.addItems(cList)
    
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
    
    def updatetxt(self):
        """
        update the details of the vehicles matched with inputs.

        Returns
        -------
        None.

        """
        self.uiOperatorTrackVehcile.textEdit.clear()
        city = self.uiOperatorTrackVehcile.comboBoxCitylocation.currentText()
        vehicle = self.uiOperatorTrackVehcile.comboBoxVehicle.currentText()
        if(city != " "):
            cityLocationId=self.checkcity(city)
        else:
            cityLocationId = None
        if(vehicle != " "):
            vehicle=int(vehicle)
        else:
            vehicle = None
        
        result = self.operator.trackVehicle(vehicleId=vehicle,cityLocationId= cityLocationId)
        if result.empty:
              self.uiOperatorTrackVehcile.textEdit.setText("Nothing matched")
        else:
            # self.uiOperatorTrackVehcile.textEdit.setText("sad")
            self.printframe(result)
    def printframe(self, frame):
        """
        print the details of the mathced vehicles into textedit        

        Parameters
        ----------
        frame : Dataframe
            details of the matched vehicles.

        Returns
        -------
        None.

        """
        col = frame.columns.values.tolist()
        # print( col )
        # for item in col:
        #     self.uiOperatorTrackVehcile.textEdit.append(item + "  ")
        
        self.uiOperatorTrackVehcile.textEdit.append("ID"+" \t"+"Type"+" \t"+"Status"+" \t"+"Price"+" \t"+"Battery"+" \t"+"now in")
        
        for indexs in frame.index:
            # print(frame.loc[indexs].values, frame.loc[indexs].values[0], frame.loc[indexs].values[2], frame.loc[indexs].values[4]
            #       , frame.loc[indexs].values[5], frame.loc[indexs].values[6], frame.loc[indexs].values[8])
            
            self.uiOperatorTrackVehcile.textEdit.append(str(frame.loc[indexs].values[0])+" \t"+
                str(frame.loc[indexs].values[2])+" \t"+str( frame.loc[indexs].values[4])+" \t"+
                  str(frame.loc[indexs].values[5])+" \t"+str(frame.loc[indexs].values[6])+" \t"+
                  str(frame.loc[indexs].values[8])+" \t")