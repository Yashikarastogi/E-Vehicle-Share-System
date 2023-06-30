import sys

from PyQt5.QtGui import QPixmap

import presenterLogin
from Order_vis import Ui_WindowOrder_vis
from manager2 import Ui_MainWindowManager
import presenterManager
class presenterOrder_vis():
    def __init__(self, window):
        self.Ui_Dialog = Ui_WindowOrder_vis()  # Create an instance of our class
        self.Ui_Dialog.setupUi(window)
        self.Ui_Dialog.homeButton.clicked.connect(lambda: presenterLogin.PresenterLogin(window))
        self.Ui_Dialog.ReturnButton.clicked.connect(lambda: presenterManager.presenterManger(window))


