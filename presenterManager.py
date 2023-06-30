import presenterLogin
import presenterTime
import presenterStatus
import presenterOrder_vis
from manager2 import Ui_MainWindowManager
import presenterAreas

class presenterManger():

    def __init__(self, window):
        self.window = window


        self.Ui_Dialog = Ui_MainWindowManager()  # Create an instance of our class

        self.Ui_Dialog.setupUi(window)
        self.Ui_Dialog.homeButton.clicked.connect(lambda: presenterLogin.PresenterLogin(window))
        self.Ui_Dialog.ReturnButton.clicked.connect(lambda: presenterLogin.PresenterLogin(window))
        self.Ui_Dialog.orderbutton.clicked.connect(lambda: presenterOrder_vis.presenterOrder_vis(window))
        self.Ui_Dialog.areabutton.clicked.connect(lambda: presenterAreas.presenterAreas(window))
        self.Ui_Dialog.timebutton.clicked.connect(lambda: presenterTime.presenterTime(window))
        self.Ui_Dialog.status.clicked.connect(lambda: presenterStatus.presenterStatus(window))