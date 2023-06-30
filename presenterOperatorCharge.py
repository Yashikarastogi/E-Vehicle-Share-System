# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 11:16:57 2022

@author: ZHOU
"""
import sys
from PyQt5 import QtWidgets
from chargeVehiclePage import Ui_MainWindowOperatorCharge
import presenterOperator
# import presenterRegistration
# this can be removed if system is connected
# sys.path.insert(1, 'C:/Users/Calvin Pfob/Documents/sqlKristen')
from mySQL import loadUsers

class presenterOperatorCharge():
    def __init__(self, window,operator):
        """
        Constructor of presenterOperatorCharge class.

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
        self.uiLogIn = Ui_MainWindowOperatorCharge() # Create an instance of our class
        self.uiLogIn.setupUi(window)
        self.uiLogIn.backButton.clicked.connect(lambda: presenterOperator.presenterOperator(window,operator))   
        self.uiLogIn.chargeConfirmButton.clicked.connect(lambda: self.chargeAllVehicle())   
        
    def chargeAllVehicle(self):
        """
        charge all the vehicle which battery is below the given threshold. 

        Returns
        -------
        None.

        """
        threshold = self.uiLogIn.thresholdEntry.text()
        try:
            threshold = float(threshold)
            if threshold<=1 and threshold>=0:
                
                ####call ifcharge = operator.chargeVehicle(batterySocThreshol=threshold);
                ifcharge = self.operator.chargeVehicle( batterySocThreshold = threshold)
                if ifcharge:
                   # print("sucessful")
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle("Charge Sucessfully")
                    msg.setText("Charge successful.All the vehicles under %.2f are Charged."%threshold)
                    msg.setIcon(QtWidgets.QMessageBox.Information)
                    msg.exec_()
                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle("Charge notification")
                    msg.setText("Charge unsuccessful.There is no vehicle need to be charged.")
                    msg.setIcon(QtWidgets.QMessageBox.Critical)
                    msg.exec_()
                
            else:
                print("Either wrong float")
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Input notification")
                msg.setText("Charge unsuccessful.Your float should between 0 and 1 (inclusive).")
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.exec_()
        except:
            print("Either wrong type")
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Input notification")
            msg.setText("Charge unsuccessful.Your should enter a float.")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.exec_()
       
        