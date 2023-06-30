# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 11:34:09 2022

@author: Calvin Pfob
"""
import mySQL

class User():
    """
    User class.

    The User class contains the attributes:
        - userId
        - userName
        - userBalance
    and the methods:
        (- constructor)

    """

    userId: int
    userName: str
    userBalance: str

    def __init__(self, userIdRequested: int):
        """
        Initialize the User class. Query user info from DB.

        Parameters
        ----------
        userIdRequested : str
            userIdRequested where data should be queied for DB.

        Returns
        -------
        Object of User class.

        """
        # get all the users info from DB
        userDf = mySQL.loadUsers()

        # check whether the user exists
        if userIdRequested in userDf["userID"].values:
            print("Find user!")
            userIndex = userDf[userDf["userID"] == userIdRequested].index.tolist()[0]

            self.userId = userIdRequested
            self.userName = userDf["userName"].loc[userIndex]
            self.userBalance = userDf["balance"].loc[userIndex]
        else:   # cannot find user in DB
            raise ValueError("Found no user in database...")
