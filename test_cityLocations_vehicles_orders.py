import pytest
from Vehicle import Vehicle
from Order import Order
from CityLocation import CityLocation
import mySQL


class TestCityLocations:
    def forAssignVehicle(self, cityLocationId, vType, drivenMin):
        result = True
        test_CityLocation = CityLocation(cityLocationIdRequested=cityLocationId)

        assignedVehicleId = test_CityLocation.assignVehicle(vehicleType=vType, drivenMinutes=drivenMin)
        if assignedVehicleId is not None:
            return result is True
        else:
            return result is False

    def testCaseAssignVehicle1(self):
        #Test in cityLocation1, type=1, drivenminute=20--->true
        assert self.forAssignVehicle(1, 1, 20) is True


    def testCaseAssignVehicle2(self):
        # Test in cityLocation1, type=1, drivenMinute=200(type 1's max drivenMinute)--->false
        assert self.forAssignVehicle(1, 1, 200) is False


    def testCaseAssignVehicle3(self):
        # Test in cityLocation1, type=2, drivenminute=20--->true
        assert self.forAssignVehicle(1, 2, 20) is True


    def testCaseAssignVehicle4(self):
        # Test in cityLocation1, type=2, drivenMinute=100(type 2's max drivenMinute)--->false
        assert self.forAssignVehicle(1, 2, 100) is False


    def testCaseAssignVehicle5(self):
        # Test in cityLocation2, type=1, drivenminute=20--->true
        assert self.forAssignVehicle(2, 1, 20) is True


    def testCaseAssignVehicle6(self):
        # Test in cityLocation2, type=1, drivenMinute=200(type 1's max drivenMinute)--->false
        assert self.forAssignVehicle(2, 1, 200) is False


    def testCaseAssignVehicle7(self):
        # Test in cityLocation2, type=2, drivenminute=20--->true
        assert self.forAssignVehicle(2, 2, 20) is True


    def testCaseAssignVehicle8(self):
        # Test in cityLocation2, type=2, drivenMinute=100(type 2's max drivenMinute)--->false
        assert self.forAssignVehicle(2, 2, 100) is False


    def testCaseAssignVehicle9(self):
        # Test in cityLocation3, type=1, drivenminute=20--->true
        assert self.forAssignVehicle(3, 1, 20) is True


    def testCaseAssignVehicle10(self):
        # Test in cityLocation3, type=1, drivenMinute=200(type 1's max drivenMinute)--->false
        assert self.forAssignVehicle(3, 1, 200) is False


    def testCaseAssignVehicle11(self):
        # Test in cityLocation3, type=2, drivenminute=20--->true
        assert self.forAssignVehicle(3, 2, 20) is True


    def testCaseAssignVehicle12(self):
        # Test in cityLocation3, type=2, drivenMinute=100(type 2's max drivenMinute)--->false
        assert self.forAssignVehicle(3, 2, 100) is False


"""
and the methods:
         (- constructor)
         - reduceBattery
         - defectVehicle
         - repairVehicle
         - chargeVehicle
         - changeLocation
"""
class TestVehicles:
    #type=1,cityLocation=1
    testVehicle1 = Vehicle(vehicleId=2)
    #type=2,cityLocation=1
    testVehicle2 = Vehicle(vehicleId=4)


    def forReduceBattery(self,vtype,drivenMin):
        result = True
        if vtype==1:
            if self.testVehicle1.reduceBattery(drivenMin):
                return result is True
            else:
                return result is False
        elif vtype==2:
            if self.testVehicle2.reduceBattery(drivenMin):
                return result is True
            else:
                return result is False

    def testCaseReduceBattery1(self):
        vtype=1
        assert self.forReduceBattery(vtype, 20) is True

    def testCaseReduceBattery2(self):
        vtype=1
        assert self.forReduceBattery(vtype, 200) is False

    def testCaseReduceBattery3(self):
        vtype=2
        assert self.forReduceBattery(vtype, 20) is True

    def testCaseReduceBattery4(self):
        vtype=2
        assert self.forReduceBattery(vtype, 100) is False

    def forDefectVehicle(self):
        result = True

        vehicleDf = mySQL.loadVehicles()
        currentStatus = int(vehicleDf[vehicleDf["vehicleID"] == self.testVehicle1.vehicleId]["vehicleStatus"])
        print("currentStatus is :",currentStatus)
        #self.testVehicle1.test()
        if currentStatus == 2:
            return result is False
        else:
            self.testVehicle1.defectVehicle()
            afterVehicleDf = mySQL.loadVehicles()
            nowStatus = int(afterVehicleDf[afterVehicleDf["vehicleID"] == self.testVehicle1.vehicleId]["vehicleStatus"])
            print("nowStatus is ",nowStatus)
            if nowStatus == 2:
                return result is True
            else:
                return result is False

    def testCaseDefectVevhicle1(self):
        assert self.forDefectVehicle() is True

    def testCaseDefectVevhicle2(self):
        assert self.forDefectVehicle() is False

    def forRepairVehicle(self):
        result = True

        vehicleDf = mySQL.loadVehicles()
        currentStatus = int(vehicleDf[vehicleDf["vehicleID"] == self.testVehicle1.vehicleId]["vehicleStatus"])
        print("currentStatus is :", currentStatus)
        # self.testVehicle1.test()
        if currentStatus == 1:
            return result is False
        else:
            self.testVehicle1.repairVehicle()
            afterVehicleDf = mySQL.loadVehicles()
            nowStatus = int(afterVehicleDf[afterVehicleDf["vehicleID"] == self.testVehicle1.vehicleId]["vehicleStatus"])
            print("nowStatus is ", nowStatus)
            if nowStatus == 1:
                return result is True
            else:
                return result is False

    def testCaseRepairVehicle1(self):
        assert self.forRepairVehicle() is True

    def testCaseDefectVevhicle2(self):
        assert self.forRepairVehicle() is False


    def forChargeVehicle(self):
        result = True

        vehicleDf = mySQL.loadVehicles()
        currentBatterySoc = float(vehicleDf[vehicleDf["vehicleID"] == self.testVehicle2.vehicleId]["batterySoc"])
        print("currentStatus is :", currentBatterySoc)

        self.testVehicle2.chargeVehicle()
        afterVehicleDf = mySQL.loadVehicles()
        nowBatterySoc = float(afterVehicleDf[afterVehicleDf["vehicleID"] == self.testVehicle2.vehicleId]["batterySoc"])
        print("nowStatus is ", nowBatterySoc)
        if nowBatterySoc==1:
            return result is True
        else:
            return result is False

    def testCaseChargeVehicle(self):
            assert self.forChargeVehicle() is True

    def forChangeLocation(self, newcityLocationId):
        result = True
        self.testVehicle1.changeLocation(newcityLocationId)
        vehicleDf = mySQL.loadVehicles()
        currentCityLocation = int(vehicleDf[vehicleDf["vehicleID"] == self.testVehicle1.vehicleId]["cityLocationId"])
        print("currentStatus is :", currentCityLocation)
        if currentCityLocation == newcityLocationId:
            return result is True
        else:
            return result is False

    def testCaseChangeLocation(self):
        assert self.forChangeLocation(2) is True


class TestOrders:
    testOrder3=Order(orderId = 163)
    def forExistingOrder(self,ExistingOrderId,testOrder:Order):
        result = True
        orderDf=mySQL.loadOrders()
        orderDf2=orderDf[orderDf["orderId"] == testOrder.orderId]
        if orderDf2.empty:
            return result is False
        else:
            nowOrderId = int(orderDf2["orderId"])
            print(nowOrderId)
            if nowOrderId == ExistingOrderId:
                return result is True
            else:
                return result is False

    def testCaseExistingOrder1(self):
        testOrder1 = Order(orderId=162)
        assert self.forExistingOrder(162, testOrder1) is True

    def testCaseExistingOrder2(self):
        testOrder2 = Order(orderId=164)
        assert self.forExistingOrder(164, testOrder2) is False

    def forNewOrder(self,testOrder:Order):#not finished
        result = True
        latestDf = mySQL.loadTheLatestIdInOrders()
        #print(latestDf)
        #latestOrderId=int(latestDf.loc[[0], ['orderId']])
        latest = mySQL.loadTheLatestIdInOrders().loc[0, 'orderId']
        orderDf=mySQL.loadOrders()
        lastOrderId = int(orderDf[orderDf['orderId'] == testOrder.orderId]['orderId'])
        if lastOrderId == latest:
            return result is True
        else:
            return result is False

    def testCaseNewOrder1(self):
        testOrder1 = Order(vehicleId=8, userId=10, drivenMinutes=10, rentCityLocationId=2)
        assert self.forNewOrder(testOrder1) is True

    def forReturnVehicle(self,returnCityLocationId):
        result = True

        orderDf = mySQL.loadOrders()
        currentStatus = int(orderDf[orderDf['orderId'] == self.testOrder3.orderId]['orderStatus'])
        print("currentStatus is :", currentStatus)

        if currentStatus == 1:
            self.testOrder3.returnVehicle(returnCityLocationId)
            afterVehicleDf = mySQL.loadVehicles()
            afterOrderDf = mySQL.loadOrders()
            nowStatus = int(afterOrderDf[afterOrderDf['orderId'] == self.testOrder3.orderId]['orderStatus'])
            nowOrderReturnId = int(
                afterOrderDf[afterOrderDf['orderId'] == self.testOrder3.orderId]['returnCityLocationId'])
            nowVehicleReturnId = int(
                afterVehicleDf[afterVehicleDf["vehicleID"] == self.testOrder3.vehicleId]["cityLocationId"])
            print("nowStatus is ", nowStatus)
            if nowStatus == 2 and nowOrderReturnId == returnCityLocationId and nowVehicleReturnId == returnCityLocationId:
                return result is True
            else:
                return result is False
        else:
            return result is False

    def testCaseReturnVehicle1(self):
        assert self.forReturnVehicle(3) is True

    def testCaseReturnVehicle2(self):
        assert self.forReturnVehicle(3) is False

    def forPayOrder(self):
        result = True

        orderDf = mySQL.loadOrders()
        currentStatus = int(orderDf[orderDf['orderId'] == self.testOrder3.orderId]['orderStatus'])
        print("currentStatus is :", currentStatus)

        if currentStatus == 3:
            return result is False
        elif currentStatus == 2:
            self.testOrder3.payOrder()
            afterOrderDf = mySQL.loadOrders()
            nowStatus = int(afterOrderDf[afterOrderDf['orderId'] == self.testOrder3.orderId]['orderStatus'])
            print("nowStatus is ", nowStatus)
            if nowStatus == 3:
                return result is True
            else:
                return result is False
        else:
            return result is False

    def testCasePayOrder1(self):
        assert self.forPayOrder() is True

    def testCasePayOrder2(self):
        assert self.forPayOrder() is False

#testVehicle=TestVehicles()
#testVehicle.forDefectVehicle()
if __name__ == "main":
    pytest.main(['-v', 'test_cityLocations_vehicles_orders.py'])