# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sps.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_end(object):
    def setupUi(self, end):
        end.setObjectName("end")
        end.resize(620, 246)
        self.centralwidget = QtWidgets.QWidget(end)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 671, 321))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("sps.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 581, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        end.setCentralWidget(self.centralwidget)

        self.retranslateUi(end)
        QtCore.QMetaObject.connectSlotsByName(end)

    def retranslateUi(self, end):
        _translate = QtCore.QCoreApplication.translate
        end.setWindowTitle(_translate("end", "УЖЕ ВСЁ :)"))
        self.label_2.setText(_translate("end", "Вы прошли эту рубрику! Спасибо за прохождение!"))
