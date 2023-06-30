import pymysql
import pandas as pd

import mySQL


class Vehicle():

     """
     The Vehicle class contains the attributes:
        - vehicleType
        - vehicleId
        - vechicleStatus
        - batterySoc
        - drivenMinutes
        
     and the methods:
         (- constructor)
         - reduceBattery
         - defectVehicle
         - repairVehicle
         - chargeVehicle
         - changeLocation
    """
     vehicleTypeId: int
     vehicleId: int
     batterySoc: float
     # drivenMinutes: float
     cityLocationId: int
     vehicleStatus: int
     pricePerMin: float


     def __init__(self, vehicleId: int):
         #get the data from SQL database for specific vehicleId
         # Dummy data
         '''self.databaseConnection = databaseConnection
         self.vehicleType = vehicleType
         self.vehicleId = vehicleId
         self.vehicleStatus = vehicleStatus
         self.pricePerMinute = 0.5
         self.batterySoc = batterySoc
         self.drivenMinutes = drivenMinutes
         self.citylocationId = cityLocationId
         '''


         if vehicleId is not None :

             # query data from sql database for existing order in database
             vehiclesDF = mySQL.loadVehicles()
             vehiclesDF2 = vehiclesDF[vehiclesDF["vehicleID"] == vehicleId]
             print(vehiclesDF2)
             if vehiclesDF2.empty:
                 raise ValueError("Not found the vehicle")
             else :
                 vehiclesDF2.set_index('vehicleID', inplace=True)
                 # print(vehiclesDF2)
                 self.vehicleId =vehicleId
                 self.pricePerMin = vehiclesDF2.loc[vehicleId, 'pricePerMin']
                 self.vehicleTypeId = vehiclesDF2.loc[vehicleId, 'vehicleTypeId']
                   #self.vehicleId = vehiclesDF2.loc[vehicleId, 'vehicleId']
                 self.vehicleStatus = vehiclesDF2.loc[vehicleId, 'vehicleStatus']
                 self.batterySoc = vehiclesDF2.loc[vehicleId, 'batterySoc']
                 self.cityLocationId  = vehiclesDF2.loc[vehicleId, 'cityLocationId']
                 
                 #self.drivenMinutes = vehiclesDF2.loc[vehicleId, 'deivenMinutes']


     def reduceBattery(self, drivenMinutes: float) -> bool:
         """
         Return to whether the electric vehicle has enough power.
         Does it depend on the time of use?
         -------
         bool
             Return true if the vehicle has enough power,otherwise returns false

         """

         Soc_Reduction_Per_Minute = self.vehicleTypeId*0.01/2
         MIMMUM_SOC_THRESHOLD = 0.1
         testBattery = self.batterySoc - drivenMinutes*Soc_Reduction_Per_Minute
         
         if testBattery > MIMMUM_SOC_THRESHOLD : #Related to car drivenMinutes
             self.batterySoc = testBattery
             mySQL.updateBatterySoc(vehicleId=self.vehicleId, newBatterySoc=self.batterySoc)
             return True
         else :
             return False

     def  defectVehicle(self)-> bool:
         """
         Change the status of a vehicle in need of repair, only change the vechicleStatus from 0 to 1
         -------
         bool
             Change the status of the vehicles in the database that need to be repaired and return true
         """
         if self.vehicleStatus == 1:
             self.vehicleStatus = 2
             mySQL.updateVehicleStatus(vehicleId=self.vehicleId, vehicleStatus=self.vehicleStatus)
             return True
         else:
             return False

     def repairVehicle(self) -> bool:
         """
         Change the status of repaired vehicles and return true, only change the vechicleStatus from 1 to 0
         -------
         bool
             Change the status of repaired vehicles in the database and return true

         """
         if self.vehicleStatus == 2:
             self.vehicleStatus = 1
             mySQL.updateVehicleStatus(vehicleId=self.vehicleId, vehicleStatus=self.vehicleStatus)
             return True
         else:
             return False

     def chargeVehicle(self):
         """
         change the vehicle's remaining charge to 100%, only change the batterySoc
         -------
         bool
             If charging is complete, change the remaining charge of the vehicle in the database and return true
         """
         self.batterySoc = 1.0
         mySQL.updateBatterySoc(vehicleId=self.vehicleId, newBatterySoc=self.batterySoc)

     def changeLocation(self, newcityLocationId : int) -> int:
# updateCityLocationId(vehicleId:int,cityLocationId)
         self.cityLocationId = newcityLocationId
         mySQL.updateCityLocationId(vehicleId=self.vehicleId, cityLocationId=self.cityLocationId)

     def test(self):
         print("vechicleID", self.vehicleId)
         print("vehicleTypeId", self.vehicleTypeId)
         print("vehicleStatus", self.vehicleStatus)
         print("batterySoc", self.batterySoc)
         print("pricePerMin", self.pricePerMin)
         print("cityLocationId", self.cityLocationId)



    
    # vehicleType: int
    # vehicleId: int
    # vehicleState: int
    # batterySoc: float

    # cityLocationId: int

# if __name__ = "__main__":
# pd.set_option('display.max_columns',10)
# v1 = Vehicle(vehicleId=2)
# v1.test()

# v1.repairVehicle()
# v1.defectVehicle()
# v1.chargeVehicle()
# v1.reduceBattery(drivenMinutes= 20)
# v1.changeLocation(newcityLocationId=1) 

# v1.test()
