# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 23:52:35 2022

@author: Noriko
"""

import pytest
import mySQL
from operatorUser import Operator
from customer import Customer


# test cases for methods of Operator Class
class TestOperator:
    # create an operator for test, here the test operator is: Bob (userId: 2)
    testOperator = Operator(2)

    # forTrackVehicle() contains the main logic for testing trackVehicle() method
    def forTrackVehicle(self, vehicleId, cityLocationId, answerDict):
        resultDict = {}     # ACTUAL VALUE: variable that stores result value after calling trackVehicle() method
        # calling trackVehicle() and get return dataframe
        trackVehicleDf = self.testOperator.trackVehicle(vehicleId, cityLocationId)
        # store vehicleId and cityLocationId of the dataframe into resultDict dictionary
        trackVehicleId = trackVehicleDf["vehicleID"].values
        trackVehicleCityId = trackVehicleDf["cityLocationId"].values
        for i in range(len(trackVehicleId)):
            resultDict[trackVehicleId[i]] = trackVehicleCityId[i]
        # check resultDict and answerDict (answerDict is EXPECTED VALUE)
        if resultDict == answerDict:
            return True
        else:
            return False

    def testCaseOperatorTrackVehicle1(self):
        # track vehicleId 2 in cityLocation 1
        assert self.forTrackVehicle(2, 1, {2: 1}) is True

    def testCaseOperatorTrackVehicle2(self):
        # track vehicleId 2 in cityLocation 3
        # vehicleId 2 in is cityLocation 1
        assert self.forTrackVehicle(2, 3, {2: 1}) is False

    def testCaseOperatorTrackVehicle3(self):
        # track vehicleId 3
        assert self.forTrackVehicle(3, None, {3: 3}) is True

    def testCaseOperatorTrackVehicle4(self):
        # track vehicleId 4
        # vehicleId 4 in is cityLocation 1
        assert self.forTrackVehicle(4, None, {4: 3}) is False

    def testCaseOperatorTrackVehicle5(self):
        # track all vehicleIds in cityLocation 1
        assert self.forTrackVehicle(None, 1, {2: 1, 4: 1, 11: 1}) is True

    def testCaseOperatorTrackVehicle6(self):
        # track all vehicleIds everywhere
        answerDict = {2: 1, 3: 3, 4: 1, 5: 3, 7: 3, 8: 3, 9: 2, 10: 3, 11: 1}
        assert self.forTrackVehicle(None, None, answerDict) is True

    # forChargeVehicle() contains the main logic for testing chargeVehicle() method
    def forChargeVehicle(self, batterySocThreshold, result):
        vehicleDf = mySQL.loadVehicles()    # get vehicle table dataframe
        # get all ids of vehicles that needs to be charged
        chargeVehicleIdList = list(vehicleDf[vehicleDf["batterySoc"] <= batterySocThreshold]["vehicleID"])
        # calling chargeVehicle()
        self.testOperator.chargeVehicle(batterySocThreshold)

        if chargeVehicleIdList != []:   # if there are vehicles that need to be charged
            vehicleDf = mySQL.loadVehicles()  # again, get vehicle table dataframe
            for eachId in chargeVehicleIdList:
                newBatterySco = vehicleDf[vehicleDf["vehicleID"] == eachId]["batterySoc"].values[0]
                if newBatterySco == 1.0:    # check whether these vehicles have been charged
                    continue
                else:   # if any of vehicles is the list does not be charged, return false
                    return result is False
            # if all vehicles in the list are charged, return true
            return result is True
        else:   # if there is no vehicle needs to be charged, return false
            return result is False

    # test cases for chargeVehicle
    def testCaseOperatorChargeVehicle1(self):
        # test all vehicles with batterySoc <= 0.5 have been charged
        assert self.forChargeVehicle(0.8, True) is True

    def testCaseOperatorChargeVehicle2(self):
        # test no vehicles with batterySoc <= 0.1
        assert self.forChargeVehicle(0.1, False) is True

    # forRepairVehicle() contains the main logic for testing repairVehicle() method
    def forRepairVehicle(self, result):
        vehicleDf = mySQL.loadVehicles()    # get vehicle table dataframe
        # get all ids of vehicles that needs to be repaired
        repairVehicleIdList = list(vehicleDf[vehicleDf["vehicleStatus"] == 2]["vehicleID"])
        # calling repairVehicle()
        self.testOperator.repairVehicle()

        if repairVehicleIdList != []:   # if there are vehicles that need to be repaired
            vehicleDf = mySQL.loadVehicles()    # again, get vehicle table dataframe
            for eachId in repairVehicleIdList:
                newVehicleStatus = vehicleDf[vehicleDf["vehicleID"] == eachId]["vehicleStatus"].values[0]
                if newVehicleStatus == 1:   # check whether these vehicles have been repaired
                    continue
                else:   # if any of vehicles is the list does not be repaired, return false
                    return result is False
            # if all vehicles in the list are repaired, return true
            return result is True
        else:   # if there is no vehicle needs to be repaired, return false
            return result is False

    def testCaseOperatorRepairVehicle1(self):
        # test if the vehicles have been repaired
        assert self.forRepairVehicle(True) is True

    def testCaseOperatorRepairVehicle2(self):
        # test no vehicles should be repaired
        assert self.forRepairVehicle(False) is True

    # forMoveVehicle() contains the main logic for testing moveVehicle() method
    def forMoveVehicle(self, vehicleId, cityLocationId):
        # calling moveVehicle()
        self.testOperator.moveVehicle(vehicleId, cityLocationId)
        vehicleDf = mySQL.loadVehicles()    # get vehicle table dataframe
        # test whether expected value equals to actual value
        if cityLocationId == vehicleDf[vehicleDf["vehicleID"] == vehicleId]["cityLocationId"].values[0]:
            return True
        else:
            return False

    def testCaseOperatorMove1(self):
        # test move vehicle 11 to cityLocation 3
        assert self.forMoveVehicle(11, 3) is True


class TestCustomer:
    # create a customer for test, here the test customer is: Cindy (userId: 3)
    testCustomer = Customer(3)

    def testCaseReturnVehicle1(self):
        # test when user has no order
        testAnotherCustomer = Customer(7)
        assert testAnotherCustomer.returnVehicle(1, 1) is False

    def testCaseReturnVehicle2(self):
        # test when user has only unpaid order
        testAnotherCustomer = Customer(4)
        assert testAnotherCustomer.returnVehicle(3, 1) is False

    def testCaseReturnVehicle3(self):
        # test user 3 return vehicle 1
        print("orderId:", self.testCustomer.orderId)
        assert self.testCustomer.returnVehicle(1, 1) is True

    # main logic for testing reportVehicle() method
    def forReportVehicle(self, vehicleId):
        self.testCustomer.reportVehicle(vehicleId)  # call reportVehicle()
        vehicleDf = mySQL.loadVehicles()
        currentStatus = vehicleDf[vehicleDf["vehicleID"] == vehicleId]["vehicleStatus"].values[0]
        # check whether vehicleStatus has been changed into damaged
        if currentStatus == 2:
            return True
        else:
            return False

    def testCaseReportVehicle1(self):
        vehicleId = 3
        self.forReportVehicle(vehicleId)
        assert self.forReportVehicle(vehicleId) is True

    def testCaseReportVehicle2(self):
        vehicleId = 5
        self.forReportVehicle(vehicleId)
        assert self.forReportVehicle(vehicleId) is True

    def testCaseReportVehicle3(self):
        vehicleId = 7
        self.forReportVehicle(vehicleId)
        assert self.forReportVehicle(vehicleId) is True

    def testCaseReportVehicle4(self):
        vehicleId = 8
        self.forReportVehicle(vehicleId)
        assert self.forReportVehicle(vehicleId) is True

    def testCaseReportVehicle5(self):
        vehicleId = 11
        self.forReportVehicle(vehicleId)
        assert self.forReportVehicle(vehicleId) is True

    def testCaseRentVehicle1(self):
        # test when user has no balance
        testAnotherCustomer = Customer(6)
        assert testAnotherCustomer.rentVehicle(1, 1, 20) is False

    def testCaseRentVehicle2(self):
        # test when there is no available vehicle to be assigned for user
        assert self.testCustomer.rentVehicle(2, 2, 20) is False

    def testCaseRentVehicle3(self):
        # test when there is no enough battery capacity
        assert self.testCustomer.rentVehicle(1, 2, 200) is False

    def testCaseRentVehicle4(self):
        # test when vehicleStatus is damaged
        assert self.testCustomer.rentVehicle(cityLocationId=3, vehicleType=1, drivenMinutes=10) is False

    def testCaseRentVehicle5(self):
        # test when there is available vehicle for user
        # and user have balance
        # and vehicle has enough battery capacity
        # and vehicleStatus is not damaged
        assert self.testCustomer.rentVehicle(3, 2, 20) is True

    # main logic for testing pay() method
    def forPay(self, payAmount):
        currentBalance = self.testCustomer.userBalance
        self.testCustomer.pay(payAmount)
        if currentBalance - payAmount == self.testCustomer.userBalance:
            return True
        else:
            return False

    def testCasePay1(self):
        payAmount = 15.0
        assert self.forPay(payAmount) is True

    # main logic for testing topUpBalance() method
    def forTopUpBalance(self, topUpAmount):
        currentBalance = self.testCustomer.userBalance
        self.testCustomer.topUpBalance(topUpAmount)
        if currentBalance + topUpAmount == self.testCustomer.userBalance:
            return True
        else:
            return False

    def testCaseTopUpBalance1(self):
        topUpAmount = 15.0
        assert self.forTopUpBalance(topUpAmount) is True


if __name__ == "main":
    pytest.main(['-v', 'test_operatorUser_customer.py'])
