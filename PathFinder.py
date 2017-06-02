#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In this example, we create a simple
window in PyQt5.

author: Jan Bodnar
website: zetcode.com 
last edited: January 2015
"""

from PyQt5 import QtCore, QtWidgets
from math import acos, cos, sin, fabs, sqrt, pi

__author__ = "Psycho_Coder"


# noinspection PyUnresolvedReferences
class MainUiWindow(object):
    def __init__(self):
        # Main Window
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        """
        Using Grid Layouts for Widgets Alignment
        """
        # Grid Layout for Main Grid Layout
        self.maingrid_layout = QtWidgets.QGridLayout(self.centralwidget)

        # Grid Layout for Result Section Layout
        self.resultgird = QtWidgets.QGridLayout()

        # Grid Layout for Information section
        self.infogrid = QtWidgets.QGridLayout()

        # Grid Layout for holding all the widgets in place
        self.outergrid = QtWidgets.QGridLayout()

        # Button to clear all test input
        self.clearall = QtWidgets.QPushButton(self.centralwidget)

        # Button to show the final result by append
        self.showres = QtWidgets.QPushButton(self.centralwidget)

        # Horizontal layout to hold the result section horizontally
        self.horizontal_layout = QtWidgets.QHBoxLayout()

        """
        Show results widgets
        """
        self.fullname = QtWidgets.QLabel(self.centralwidget)
        self.result = QtWidgets.QLabel(self.centralwidget)

        """
        Get Names info section
        """
        self.firstname = QtWidgets.QLabel(self.centralwidget)
        self.lastname = QtWidgets.QLabel(self.centralwidget)

        # TextBox to get user input
        self.fname = QtWidgets.QLineEdit(self.centralwidget)
        self.lname = QtWidgets.QLineEdit(self.centralwidget)

    def init_gui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        MainWindow.setStyleSheet(open("style.qss", "r").read())
        MainWindow.setAutoFillBackground(True)
        MainWindow.resize(328, 166)

        self.centralwidget.setObjectName("centralwidget")

        self.maingrid_layout.setObjectName("maingrid_layout")
        self.outergrid.setObjectName("outergrid")
        self.infogrid.setObjectName("infogrid")

        self.firstname.setObjectName("firstname")
        self.infogrid.addWidget(self.firstname, 0, 0, 1, 1)

        self.fname.setObjectName("fname")
        self.infogrid.addWidget(self.fname, 0, 1, 1, 1)

        self.lastname.setObjectName("lastname")
        self.infogrid.addWidget(self.lastname, 1, 0, 1, 1)

        self.lname.setObjectName("lname")
        self.infogrid.addWidget(self.lname, 1, 1, 1, 1)

        self.outergrid.addLayout(self.infogrid, 0, 0, 1, 1)

        self.fullname.setObjectName("fullname")

        self.result.setMaximumSize(QtCore.QSize(140, 16777215))
        self.result.setObjectName("result")

        self.resultgird.setObjectName("resultgird")
        self.resultgird.addWidget(self.fullname, 0, 0, 1, 1)
        self.resultgird.addWidget(self.result, 0, 1, 1, 1)

        self.outergrid.addLayout(self.resultgird, 1, 0, 1, 1)

        self.showres.setObjectName("showres")
        self.clearall.setObjectName("clearall")

        self.horizontal_layout.setObjectName("horizontal_layout")
        self.horizontal_layout.addWidget(self.showres)
        self.horizontal_layout.addWidget(self.clearall)

        self.outergrid.addLayout(self.horizontal_layout, 2, 0, 1, 1)
        self.maingrid_layout.addLayout(self.outergrid, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslate_gui(MainWindow)

        # Add signals of clear to LineEdit widgets to clear the texts
        self.clearall.clicked.connect(self.result.clear)
        self.clearall.clicked.connect(self.lname.clear)
        self.clearall.clicked.connect(self.fname.clear)
        self.showres.clicked.connect(self.__name)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def __name(self):
        name = self.fname.text() + " " + self.lname.text()
        self.result.setText("<font color=\"#ffffff\"><b><u>" + name + "</u></b></font>")

    def retranslate_gui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "Name Concatenation"))
        self.lastname.setText(_translate("MainWindow", "Last Name :"))
        self.firstname.setText(_translate("MainWindow", "First Name :"))
        self.fullname.setText(_translate("MainWindow", "Concatenated Name :-"))
        self.result.setText(_translate("MainWindow", "<Name>"))
        self.showres.setText(_translate("MainWindow", "Show Name!"))
        self.clearall.setText(_translate("MainWindow", "Clear All"))


class Helpers(object):
    cities = {
        'Bialystok': (53.132549, 23.169454),
        'Lomza': (53.178030, 22.059080),
        'Warsaw': (52.228649, 21.025483),
        'Olsztyn': (53.778628, 20.480804),
        'Wroclaw': (51.108092, 17.035121),
    }
    betterCities = {
        'Bialystok': (53.132489, 23.168840),
        'Lomza': (53.178120, 22.059032),
        'Warsaw': (52.229676, 21.012229),
        'Olsztyn': (53.778422, 20.480119),
        'Wroclaw': (51.107885, 17.038538),
        'Gdansk': (54.352025, 18.646638),
        'Slupsk': (54.464148, 17.028482),
        'a': (54.366667, 18.633333),  # Gdansk
        'b': (54.466667, 17.016667),  # Slupsk
    }

    def __init__(self):
        pass

    @staticmethod
    def calculate_distance(pA, pB):
        """
        # useful links
        # https://pl.wikibooks.org/wiki/Astronomiczne_podstawy_geografii/Odleg%C5%82o%C5%9Bci
        # http://www.latlong.net/
        
        WORK IN PROGRESSSSSSSSSS
      
        """

        # maxLat = 90
        # degreeToMeteres = 111100
        #
        # print(pA)
        # print(pB)
        # dLatA = maxLat - pA[0]
        # dLatB = maxLat - pB[0]
        #
        # print(dLatA)
        # print(dLatB)
        #
        #
        # distance = 0
        #
        # partial = cos(dLatA) * cos(dLatB) + sin(dLatA) * sin(dLatB) * cos(pA[1]-pB[1])
        # print(partial)
        # l = acos(partial)
        # print(l)
        # distance = l * degreeToMeteres

        # Obliczanie odległości w linii prostej pomiędzy dwoma punktami na mapie pomijając krzywiznę Ziemi.
        # Zwracan wartość jest w kilometrach.
        distance = (pA[0] - pB[0])**2
        distance += (cos((pA[0] * pi)/180) * (pB[1] - pA[1]))**2
        distance = sqrt(distance) * (40075.704/360)
        print("Distance: " + str(distance))

        return distance


if __name__ == "__main__":
    import sys

    Helpers.calculate_distance(Helpers.betterCities['a'], Helpers.betterCities['b'])

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainUiWindow()
    ui.init_gui(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
