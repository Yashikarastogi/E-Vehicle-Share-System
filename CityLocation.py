"""Script contains the CityLocation class."""
import Vehicle
from mySQL import loadCityLocations, loadAvailableVehicles

class CityLocation():
    """
    The CityLocation class contains the attributes:
        - cityLocationId
    and the methods:
        (- constructor)
        - assignVehicle
    """
    cityLocationId: int

    def __init__(self, cityLocationIdRequested: int):
        """
        Constructor of the class. Query the data from data base for a specified cityLocationId

        Parameters
        ----------
        cityLocationIdRequested : int
            cityLocationId where data should be queried from database.

        Raises
        ------
        ValueError
            Raises ValueError if cityLocationIdRequested has been handed over which is not available in database.

        Returns
        -------
        Object of Class CityLocation

        """
        # check if locationId is available in database table
        cityLocationData = loadCityLocations(cityLocationIdRequested)
        if cityLocationData.empty:  # if cityLocationData is empty querying from database was not successful
            errorMsg = "Querying data from database was unsuccessful. Probably wrong cityLocationIdRequested has been specified"
            raise ValueError(errorMsg)
        else:
            self.cityLocationId = cityLocationIdRequested

    def assignVehicle(self, vehicleType: int, drivenMinutes: float) -> int:
        """
        Assign suitable vehicleId to the customer based on his/her preferences.
        It returns None if it was not able to find a suitable vehicle at the city location.

        Parameters
        ----------
        vehicleType : int
            Specifies the vehicleType.
        drivenMinutes : float
            Specifies how many minutes the customer wants to rent the vehicle.

        Returns
        -------
        int
            Assigned vehicleId to customer based on his/her preferences. Returns None if there is not a suitable
            vehicle available at the city location

        """
        vehiclesAvailable = loadAvailableVehicles(self.cityLocationId, vehicleType)
        for _, vehicleId in vehiclesAvailable["vehicleId"].items():
            currentVehicle = Vehicle.Vehicle(vehicleId)
            if not currentVehicle.reduceBattery(drivenMinutes):
                continue
            else:  # vehicle can be assigned to customer and is suitable
                return vehicleId
        # no suitable vehicle was found at cityLocation
        return None


if __name__ == "__main__":
    try:
        x = CityLocation(cityLocationIdRequested=1)
    except ValueError as error:
        print(error)  # Error message in frontend
    assignedVehicleId = x.assignVehicle(vehicleType=1, drivenMinutes=20)
    print(assignedVehicleId)
