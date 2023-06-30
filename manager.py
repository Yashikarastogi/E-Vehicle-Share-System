"""
Created on Thu Oct 10 15:05:17 2022

@author: shengyunXu
"""
import mySQL
import pandas as pd

class Manager():
    """

    """


    def __init__(self, vehiclenumber :int):
        self.vehiclenumber = 0
        
    
    # query the order vehicle number in the limited time
    def limitedTimedVehicleNumber(self, start_time : str, end_time : str, vehicleTypeName: str) -> int:

        self.start_time = start_time
        self.end_time = end_time
        self.vehicleTypeName = vehicleTypeName
        
        # query
        dataframeO = mySQL.loadOrders()
        
        # check the vehicleType from the vehicleID in the order form
        dataframeV = mySQL.loadVehicles() 
        dataframeM = pd.merge(dataframeO, dataframeV, how='inner', left_on='vehicleId', right_on='vehicleID')                   
                 
        vehicledataframe = dataframeM[dataframeM['vehicleTypeName'] == vehicleTypeName]
                
            
        # # identufy the type name of vehicle by calculating th price
        # #dataframe['vehicleType'] = dataframe['priceTotal'] / dataframe['timeOrder']
        # #dataframe['vehicleType'] = ['bike' if x - 2.5 < 0.01 else 'scooter' for x in dataframe['vehicleType'] ]
        

        targetData = [ind for ind in vehicledataframe['orderTimestamp'] if start_time < str(ind) < end_time]

        if not targetData:  # if targetData is empty querying from database was not successful
            errorMsg = "Querying data from database was unsuccessful. Probably a wrong cityLocationIdRequested has been specified" 
            raise ValueError(errorMsg)
        else:
            return len(targetData)




    # calculate the average renting time in the limited time
    def batteryTotalVehicle(self, start_time : str, end_time : str, vehicleTypeName: str) -> int:
        """
        """
        self.start_time = start_time
        self.end_time = end_time
        self.vehicleTypeName = vehicleTypeName
        
        # query
        dataframe = mySQL.loadOrders() 
        # identify the type name of vehicle by calculating th price
        dataframe['vehicleType'] = dataframe['priceTotal'] / dataframe['timeOrder']
        dataframe['vehicleType'] = ['bike' if x - 2.5 < 0.01 else 'scooter' for x in dataframe['vehicleType'] ]
        vehicledataframe = dataframe[dataframe['vehicleType'] == vehicleTypeName]


        return vehicledataframe['timeOrder'].mean()
        

    # the number of rent vehicle in each street 
    def rentstreetVehicle(self, vehicleType: str, rentCityLocation: int) -> int:
        """
        """
        # query
        dataframe = mySQL.loadOrders() 
        streetdata = dataframe[dataframe['rentCityLocationId']==rentCityLocation]
        return len(streetdata)
    
    # sort the order by the using time for a specific vehicle
    def timeUsedAnalysis(self, vehicleTypeName: str) -> int:
        # query
        dataframe = mySQL.loadOrders() 
        # identify the type name of vehicle by calculating th price
        dataframe['vehicleType'] = dataframe['priceTotal'] / dataframe['timeOrder']
        dataframe['vehicleType'] = ['bike' if x - 2.5 < 0.01 else 'scooter' for x in dataframe['vehicleType'] ]
        vehicledataframe = dataframe[dataframe['vehicleType'] == vehicleTypeName]
        
        # each 10 mins will be divided into a group,for data visualization
        vehicledataframe['timeThreshold'] = vehicledataframe['timeOrder'] // 10
        return vehicledataframe['timeThreshold'].value_counts()
            
        

    # get the number of vehicles in each street at the moment, for moving, charging or managing the vehicle purpose
    def streetTotalVehicle(self, vehicleTypeName: str, cityLocation: int)->int:
        # query
        dataframe = mySQL.loadVehicles()
        vehicledataframe = dataframe[dataframe['vehicleTypeName'] == vehicleTypeName]
        streetdata = vehicledataframe[vehicledataframe['cityLocationId']==cityLocation]
        return len(streetdata)    
    
    
    # get the number of avaiable or damaged vehicles in the currrent time
    def vehicleAnalysis(self, vehicleTypeName: str, cityLocationId: int):
        # query
        dataframe = mySQL.loadVehicles()
        dataframe = dataframe[dataframe['cityLocationId'] == cityLocationId]
        ve_dataframe = dataframe[dataframe['vehicleTypeName'] == vehicleTypeName]
        

        avdata= ve_dataframe[ve_dataframe['vehicleStatus']=='available']
        dadata = ve_dataframe[ve_dataframe['vehicleStatus']=='damaged']
        return len(avdata) , len(dadata) 
        
    


    
if __name__ == "__main__":
    # this object is created only once in the main of program and will be handed over to each class

    try:
        mySQL.loadOrders()
        x = Manager(0)
        functiontest1 = x.limitedTimedVehicleNumber('2022-10-01 10:34:21' ,'2022-10-08 10:34:21', "scooter")
        functiontest2 = x.batteryTotalVehicle('2022-10-01 10:34:21' ,'2022-10-05 10:34:21', "bike")
        functiontest3 = x.rentstreetVehicle('bike',1)
        functiontest4 = x.timeUsedAnalysis("bike")
        functiontest5 = x.streetTotalVehicle('bike',3)
        functiontest6_avaiable, functiontest6_damaged = x.vehicleAnalysis('bike', 1)


        #print(functiontest1)
        #print(functiontest2)
        #print(functiontest3)
        #print(functiontest4)
        #print(functiontest5)
        #print(functiontest6_avaiable)
    except ValueError as error:
        print(error) # Error message in frontend
        
    #databaseConnection.db.close()
    
    
