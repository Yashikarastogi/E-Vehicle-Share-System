import mySQL as sql
from user import User
from Vehicle import Vehicle
from CityLocation import CityLocation
from Order import Order


class Customer(User):
    orderId: int = None          # will be generated when new order is created

    def rentVehicle(self, cityLocationId: int, vehicleType: int, drivenMinutes: float) -> bool:
        """
        Customer rents the vehicle to which new order id is assigned

        Parameters
        ----------
        cityLocationId : int
            Unique id assigned to every location
        vehicleType : int
            Used to describe the type of vehicle
        drivenMinutes : float
            Time customer used the vehicle for

        Returns
        -------
        bool
            New order id is assigned, and total cost is calculated based on the time vehicle is rented and then returns true

        """
        if self.userBalance <= 0:
            return False
        cityLocation = CityLocation(cityLocationId)
        vehicleId = cityLocation.assignVehicle(vehicleType, drivenMinutes)
        if vehicleId == None:
            return False
        order = Order(vehicleId = vehicleId, userId = self.userId, drivenMinutes=drivenMinutes, rentCityLocationId=cityLocationId)
        self.orderId = order.orderId
        self.pay(order.priceTotal)
        return True

    def returnVehicle(self, vehicleId: int, cityLocationIdReturn: id) -> True:
        """
        Customer returns the rented vehicle to a new city location

        Parameters
        ----------
        vehicleId : int
            Id assigned to every vehicle
        cityLocationIdReturn : id
            Id of the city location where vehicle is returned

        Returns
        -------
        True
            Change the status of the vehicle to available after returned and returns true

        """
        # # @author: Wenhui
        if self.orderId is None:
            orderDf = sql.loadOrders()  # need to find user's previous orders
            # find unfinished orders (orderStatus: on the way)
            orderDf = orderDf[(orderDf["userId"] == self.userId) & (orderDf["orderStatus"] == 1)]
            if orderDf.empty:
                return False
            else:
                self.orderId = orderDf["orderId"].values[-1]  # load last order

        order = Order(orderId=self.orderId)
        order.returnVehicle(cityLocationIdReturn)
        return True

    def reportVehicle(self, vehicleId: int) -> bool:
        """
        Asks the user if the vehicle is defective
        Parameters
        ----------
        vehicleId : int
            Id assigned to every vehicle

        Returns
        -------
        bool
            Retruns true if customer reports the vehicle as defective

        """
        reportedVehicle = Vehicle(vehicleId)
        reportedVehicle.defectVehicle()
        return True

    def pay(self, paymentAmount: float) -> bool:
        """
        The cost of the journey is deducted from the available balance of the customer

        Parameters
        ----------
        paymentAmount : float
            total price for the journey

        Returns
        -------
        bool
            returns true if the payment is successfully made from the available balance

        """
        self.userBalance -= paymentAmount
        self.userBalance = round(self.userBalance, 2)
        sql.updateBalance(self.userId, self.userBalance)
        return True

    def topUpBalance(self, amountTopUp: float) -> bool:
        """
        customer can add amount to the available balance

        Parameters
        ----------
        amountTopUp : float
            amount to be added

        Returns
        -------
        bool
            Returns true if the amount is successfully updated

        """
        self.userBalance += amountTopUp
        self.userBalance = round(self.userBalance, 2)
        sql.updateBalance(self.userId, self.userBalance)
        return True
            