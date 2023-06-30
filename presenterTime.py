from PyQt5.QtGui import QPixmap

import presenterLogin

from Time_vis import Ui_WindowTime_vis
import presenterManager

class presenterTime():
    def __init__(self, window):
        self.Ui_Dialog = Ui_WindowTime_vis()  # Create an instance of our class
        self.Ui_Dialog.setupUi(window)
        self.Ui_Dialog.homeButton.clicked.connect(lambda: presenterLogin.PresenterLogin(window))
        self.Ui_Dialog.ReturnButton.clicked.connect(lambda: presenterManager.presenterManger(window))
        #self.widget_2.load(QtCore.QUrl("file:///image1.html"))



