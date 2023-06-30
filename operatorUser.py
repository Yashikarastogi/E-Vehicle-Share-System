# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 23:09:03 2022.

@author: Wenhui He
"""

import mySQL
import pandas as pd
from Vehicle import Vehicle
from user import User

class Operator(User):
    """
    The Operator class inherits of User class.

    The User class contains the inherited attributes:
        - userId
        - userName
        - userBalance
    and the methods:
        - trackVehicle
        - chargeVehicle
        - repairVehicle
        - moveVehicle
    """

    def trackVehicle(self, vehicleId: int = None, cityLocationId: int = None):
        """
        Track vehivle according to specified vehicleID and/or cityLocationId.

        If no vehicleId and cityLocationId are given, return all vehicles anywhere.

        Parameters
        ----------
        vehicleId : int
            vechileId of the vehicle that operator wants to query.
        cityLocationId : int
            cityLocationId that operator wants to query.

        Returns
        -------
        result : DataFrame
            It returns a table containing vehicles info on specified vehiccleId and cityLocationId.

        """
        # get all vehicle info from DB
        vehicleDf = mySQL.loadVehicles()

        if vehicleId is None:
            if cityLocationId is None:  # return all vehicles
                result = vehicleDf
            else:   # return vehicles based on specified cityLocationId
                result = vehicleDf[vehicleDf["cityLocationId"] == cityLocationId]
        else:
            if cityLocationId is None:    # return vehicle info on specified vehicleId
                result = vehicleDf[vehicleDf["vehicleID"] == vehicleId]
            else:   # return vehicle info on specified vehicleId and cityLocationId
                result = (vehicleDf[(vehicleDf["vehicleID"] == vehicleId)
                                    & (vehicleDf["cityLocationId"] == cityLocationId)])
        return result

    def chargeVehicle(self, batterySocThreshold: float):
        """
        Charge any vehicle that has battrtySoc less than or equal to threshold value.

        Parameters
        ----------
        batterySocThreshold : float
            specify threshold value of batterySoc.

        Returns
        -------
        result : boolean

        """
        # get all vehicle info form DB
        vehicleDf = mySQL.loadVehicles()
        # filter vehicles that have batterySoc less than or equal to threshold value
        chargeVehicleIdList = list(vehicleDf[vehicleDf["batterySoc"] <= batterySocThreshold]["vehicleID"])

        if chargeVehicleIdList != []:
            for eachId in chargeVehicleIdList:
                newVehicle = Vehicle(eachId)
                newVehicle.chargeVehicle()
            return True
        else:
            return False

    def repairVehicle(self):
        """
        Repaire all the vehicle that are damaged.

        Returns
        -------
        result : Boolean

        """
        # get all vehicle info from DB
        vehicleDf = mySQL.loadVehicles()
        # query vehicles that have "damage" status
        repairVehicleIdList = list(vehicleDf[vehicleDf["vehicleStatus"] == 2]["vehicleID"])
        
        if repairVehicleIdList != []:
            for eachId in repairVehicleIdList:
                newVehicle = Vehicle(eachId)
                newVehicle.repairVehicle()
            return True
        else:
            return False

    def moveVehicle(self, vehicleId: int, cityLocationId: int):
        """
        Move specified vehicle to specified city location.

        Parameters
        ----------
        vehicleId : int
            specify vehicleId of vehicle that needs to be moved.
        cityLocationId : int
            specify cityLocationId where specified vehicle needs to be move to.

        Returns
        -------
        None.

        """
        newVehicle = Vehicle(vehicleId)
        newVehicle.changeLocation(cityLocationId)


if __name__ == "__main__":
    # show more info of dataframe in Spyder console
    pd.set_option('display.max_columns', 10)
    pd.set_option('display.max_rows', 20)
    
    def test():
        mySQL.updateBatterySoc(2, 0.2)
        mySQL.updateBatterySoc(3, 0.2)
        mySQL.updateBatterySoc(4, 0.2)
        mySQL.updateBatterySoc(5, 0.2)
        mySQL.updateVehicleStatus(2, 2)
        mySQL.updateVehicleStatus(3, 2)
        mySQL.updateVehicleStatus(4, 2)
        mySQL.updateVehicleStatus(5, 2)
    
    # test()
    
    # test_user = Operator(2)
    #test_user.moveVehicle(3,3)
    # test_user.chargeVehicle(0.5)
    #test_user.repairVehicle()
    # print(mySQL.loadVehicles())
    #print(test_user.userBalance)
    
