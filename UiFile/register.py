# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\teXiao\doodle\UiFile\register.ui',
# licensing of 'C:\Users\teXiao\doodle\UiFile\register.ui' applies.
#
# Created: Thu Jun 18 18:37:12 2020
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(883, 165)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.user = QtWidgets.QLabel(self.centralwidget)
        self.user.setObjectName("user")
        self.horizontalLayout.addWidget(self.user)
        self.userText = QtWidgets.QLineEdit(self.centralwidget)
        self.userText.setObjectName("userText")
        self.horizontalLayout.addWidget(self.userText)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.is_ok = QtWidgets.QPushButton(self.centralwidget)
        self.is_ok.setObjectName("is_ok")
        self.horizontalLayout_2.addWidget(self.is_ok)
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout_2.addWidget(self.cancel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 883, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.user.setText(QtWidgets.QApplication.translate("MainWindow", "姓名", None, -1))
        self.is_ok.setText(QtWidgets.QApplication.translate("MainWindow", "确认", None, -1))
        self.cancel.setText(QtWidgets.QApplication.translate("MainWindow", "取消", None, -1))

