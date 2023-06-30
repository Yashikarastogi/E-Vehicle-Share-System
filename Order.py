# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 11:03:05 2022
Edit on Sat Oct 01 18:49 2022 -> add constructor docstring, and false situation of the two functions.
Edit on Mon Oct 03 23:33 2022 ->constructor default valuse and add 2 citylocationId
Edit on Fri Oct 14 19:35 2022 -> citylocationId in vehcile->nan when creating a new order,when return  citylocationId in 
vehcile-> returncitylocationId in order
@author: ZHOU
"""
import datetime
import mySQL
import pandas as pd
import numpy as np

class Order:
    """
    The order class contains the attributes:
        - orderId
        - vehicleId
        - userId
        - timeOrder
        - priceTotal
        - orderStatus
        - orderTimestamp
        - rentCityLocationId
        - returnCityLocationId
     and the methods:
         (- constructor)
         - returnVehicle
         - payOrder
    """

    orderId: int
    vehicleId: int
    # vehicleType could make sense here to add
    userId: int
    timeOrder: float
    priceTotal: float
    orderStatus: int
    orderTimestamp: str
    rentCityLocationId: int
    returnCityLocationId: int

    def __init__(self, vehicleId: int = None, userId: int = None, drivenMinutes: float = None,
                 orderId: int = None, rentCityLocationId: int = None):
    
        """
        Create a new Order object,set the orderStatus as 0, amd write it into the database.
        Parameters
        ----------
        vehicleId : int
            Indicates a vehicle was used during this order. Used to query from database for pricePerMinute of vechicle.
        userId : int
            Indicates a user trying to rent a vehicle from the system.
        drivenMinutes : float
            Should given by the user to calculate the total price of the order.
        Returns
        -------
        Object of Class Order
        """
        if orderId is not None and (vehicleId is None and userId is None and drivenMinutes is None and 
                     rentCityLocationId is None):
            # query data from sql database for existing order in database 
            orderDF = mySQL.loadOrders()
            orderDF2 = orderDF[orderDF["orderId"] == orderId]
            if orderDF2.empty:
                raise ValueError("Not found the order")
            else:
                # print(orderDF2)
                orderDF2.set_index('orderId', inplace = True)
                # print(orderDF2)
                self.orderId = orderId
                self.userId = orderDF2.loc[orderId, 'userId']
                self.vehicleId = orderDF2.loc[orderId, 'vehicleId']
                self.timeOrder = orderDF2.loc[orderId, 'timeOrder']
                self.priceTotal = orderDF2.loc[orderId, 'priceTotal']
                self.orderStatus = orderDF2.loc[orderId, 'orderStatus']
                self.orderTimestamp = orderDF2.loc[orderId, 'orderTimestamp']
                self.rentCityLocationId = orderDF2.loc[orderId, 'rentCityLocationId']
                self.returnCityLocationId = orderDF2.loc[orderId, 'returnCityLocationId']
        elif orderId is None and (vehicleId is not None and userId is not None and drivenMinutes is not None and 
                     rentCityLocationId is not None):
            # Create a new instance and write it to database
            
            pass
            # 是否检查非空？？whether check if vehicle exists in db
            vehicleDF = mySQL.loadVehicles()
            vehicleDF.set_index('vehicleID', inplace = True)
            pricePerMinute = vehicleDF.loc[vehicleId,'pricePerMin']
            self.priceTotal = drivenMinutes * pricePerMinute
            # print(pricePerMinute,self.priceTotal)
            self.orderTimestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # print(self.orderTimestamp)
            self.orderStatus = 1
            self.returnCityLocationId = "NULL"
            self.vehicleId = vehicleId
            self.userId = userId
            self.timeOrder = drivenMinutes
            self.rentCityLocationId = rentCityLocationId
            mySQL.updateCityLocationId(vehicleId, "NULL")
            # self.orderId = 50   # according to the database add it to the last of order table
          
            mySQL.addNewOrder(self.vehicleId, self.userId, self.timeOrder, self.priceTotal,
                                          self.orderStatus, str(self.orderTimestamp),
                                          self.rentCityLocationId, self.returnCityLocationId)
            
            latest = mySQL.loadTheLatestIdInOrders().loc[0, 'orderId']
            self.orderId = latest
        else:
            raise ValueError("Wrong constructor arguments.")

    def returnVehicle(self, returnCityLocationId: int) -> bool:
        """
        Return a vehicle to a cityLocation. Change the orderStatus from 0 to 1 and write the return city location.
        -------
        bool
            Returns true if return vechicle process was successful and database is updated.

        """
        if self.orderStatus == 1:
            
            self.orderStatus = 2
            self.returnCityLocationId = returnCityLocationId
            mySQL.updateReturnCityLocationId(orderId=self.orderId,returnCityLocationId=self.returnCityLocationId)
            mySQL.updateOrderStatus(orderId=self.orderId,orderStatusId=self.orderStatus)
            mySQL.updateCityLocationId(self.vehicleId, self.returnCityLocationId)
            return True
        else:
            return False
        
    # this is an optional function which may be removed in the future
    def payOrder(self) -> bool:
        """
        Pay for the order. Only change the orderStatus from 1 to 2.
        -------
        bool
            Returns true if payment process was successful and database is updated.

        """
        if self.orderStatus == 2:
            self.orderStatus = 3
            mySQL.updateOrderStatus(orderId=self.orderId,orderStatusId=self.orderStatus)
            return True
        else:
            return False


# This is only used to test the class Order
    def test(self):
        print("orderID:", self.orderId)
        print("vechicleID", self.vehicleId)
        print("userID", self.userId)
        print("timeOder", self.timeOrder)
        print("priceTotal", self.priceTotal)
        print("orderStatus", self.orderStatus)
        print("orderTimestamp", self.orderTimestamp)
        print("rentCityLocationId", self.rentCityLocationId)
        print("returnCityLocationId", self.returnCityLocationId)

if __name__ == "__main__":
    pd.set_option('display.max_columns',10)
    order1 = Order(orderId = 164)
    # order1 = Order(vehicleId =4, userId =1, drivenMinutes =4.5, 
    #               rentCityLocationId =4)
    order1.test()
    # mySQL.updateOrderStatus(1,1)
    
    order1.returnVehicle(returnCityLocationId=1)
    order1.test()
    # vehicleDF = mySQL.loadVehicles()
    #################还车order return location，vehcile： citylocation
    
    # mySQL.updateReturnCityLocationId(orderId=100,returnCityLocationId=8)
    # order1.payOrder()
    # order1.test()
     
    
    orderDF = mySQL.loadOrders()
    vehicleDF = mySQL.loadVehicles()
    # latest = mySQL.loadTheLatestIdInOrders().loc[0, 'orderId']
    # print(latest)
    
    
    #################还车order return location，vehcile： citylocation
    ##借车查找我当前位置的citylocation
    ##借车：vehicle changecitylocation，order returnvehicle.