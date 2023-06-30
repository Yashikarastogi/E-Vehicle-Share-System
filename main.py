# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 12:45:43 2022
Main Application file
@author: Calvin Pfob
"""

import sys
from PyQt5 import QtWidgets
import presenterLogin


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # Create an instance of QtWidgets.QApplication
    window = QtWidgets.QMainWindow()
    presenterLogin.PresenterLogin(window)
    window.show()
    window.activateWindow()
    sys.exit(app.exec())  # Start the application
