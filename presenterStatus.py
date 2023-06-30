from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QPixmap
from PyQt5.QtWebEngineWidgets import QWebEngineView

import presenterLogin
import presenterManager
from Status_vis import Ui_WindowStatus_vis

import os
class presenterStatus():
    def __init__(self, window):
        self.Ui_Dialog = Ui_WindowStatus_vis()  # Create an instance of our class
        self.Ui_Dialog.setupUi(window)
        self.Ui_Dialog.homeButton.clicked.connect(lambda: presenterLogin.PresenterLogin(window))
        self.Ui_Dialog.ReturnButton.clicked.connect(lambda: presenterManager.presenterManger(window))

        #self.Ui_Dialog.label.setPixmap(QPixmap("./order_vis.jpg"));

        #self.Ui_Dialog.widget_2.load(QUrl('file:///ML4DS.html'))
        #self.Ui_Dialog.widget_2 = QWebEngineView()
        # url = os.getcwd() + '/ML4DS.html'
        # self.Ui_Dialog.widget_2.load(QUrl.fromLocalFile(url))


        #self.Ui_Dialog.widget_2.load(QtCore.QUrl(url))



