# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 10:54:24 2022

@author: ZHOU
"""
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from operatorPage import Ui_MainWindowOperator
import presenterOperatorCharge
import presenterOperatorMoveVehicle
import presenterTrackVehicle
import presenterLogin
import presenterOperatorAddVehicle
# this can be removed if system is connected
# sys.path.insert(1, 'C:/Users/Calvin Pfob/Documents/sqlKristen')
from mySQL import loadUsers

class presenterOperator():
    def __init__(self, window,operator):
        """
        
        Constructor of presenterOperator class.

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
        self.uiLogIn = Ui_MainWindowOperator() # Create an instance of our class
        self.uiLogIn.setupUi(window)
        self.uiLogIn.trackButton.clicked.connect(lambda: presenterTrackVehicle.presenterTrackVehicle(window,operator))
        self.uiLogIn.chargeallButton.clicked.connect(lambda: presenterOperatorCharge.presenterOperatorCharge(window,operator))
        self.uiLogIn.moveVehicleButton.clicked.connect(lambda: presenterOperatorMoveVehicle.presenterOperatorMoveVehicle(window,operator))
        self.uiLogIn.repairallButton.clicked.connect(lambda: self.repairAllVehicle())
        self.uiLogIn.signOutButton.clicked.connect(lambda: presenterLogin.PresenterLogin(window))
        self.uiLogIn.addNewButton.clicked.connect(lambda: presenterOperatorAddVehicle.presenterOperatorAddVehicle(window, operator))
    def repairAllVehicle(self):
        """
        repair all the vehicles which are broken in the database.

        Returns
        -------
        None.

        """
        ifrepair = self.operator.repairVehicle() 
        print(ifrepair)
        if ifrepair:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Repair Sucessfully")
            msg.setText("Repair successful.All the vehicles are repaied.")
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.exec_()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Repair notification")
            msg.setText("Repair unsuccessful.There is no vehicle need to be repaired.")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.exec_()
            

    