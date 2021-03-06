# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'СПОРТ.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import random

import varR
from result import *


class Final(QtWidgets.QMainWindow, Ui_Final):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class Result(QtWidgets.QMainWindow, Ui_RESULT):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class Ui_SPORT(object):
    def __init__(self):
        self.finalWind = Final()
        self.resWind = Result()

    def setupUi(self, SPORT):
        SPORT.setObjectName("SPORT")
        SPORT.resize(732, 439)
        SPORT.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(SPORT)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 70, 651, 150))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 230, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 211, 34);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 230, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 211, 34);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 310, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 211, 34);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 310, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 211, 34);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 821, 441))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("imgonline-com-ua-Resize-klAP8X2qNJC84n.png"))
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        SPORT.setCentralWidget(self.centralwidget)

        self.retranslateUi(SPORT)
        QtCore.QMetaObject.connectSlotsByName(SPORT)

    def retranslateUi(self, SPORT):
        _translate = QtCore.QCoreApplication.translate
        SPORT.setWindowTitle(_translate("SPORT", "СПОРТ"))
        self.label.setText(_translate("SPORT", "ЙУцйуйц"))
        self.pushButton.setText(_translate("SPORT", "PushButton"))
        self.pushButton_2.setText(_translate("SPORT", "PushButton"))
        self.pushButton_3.setText(_translate("SPORT", "PushButton"))
        self.pushButton_4.setText(_translate("SPORT", "PushButton"))

        self.btn_grp = QtWidgets.QButtonGroup()
        self.btn_grp.setExclusive(True)
        self.btn_grp.addButton(self.pushButton)
        self.btn_grp.addButton(self.pushButton_2)
        self.btn_grp.addButton(self.pushButton_3)
        self.btn_grp.addButton(self.pushButton_4)

        self.btn_grp.buttonClicked.connect(self.answer)

        self.list = [('Cколько раз сборная СССР выиграла ЧМ по футболу?', '1', '2', '4', '0'),
                     ('Когда состоялась первая олимпиада?', '1896', '1898', '1900',
                      '1892'),
                     ('Какое количество игроков в кёрлинге?', '3', '4', '5',
                      '2'),
                     ('Канадский спортсмен, Коннор Макдэвид, звезда какого спорта?', 'Хоккей', "Футбол", "Баскетбол",
                      "Биатлон"),
                     ('Какова высота сетки в мужском волейболе?', "243", "223", "233",
                      "253"),
                     ('На какую оценку оцените себя?', '2', '3', '4', '5')]

        self.true = 0
        self.posl = [1, 2, 3, 4]
        random.shuffle(self.posl)
        self.label.setText(self.list[0][0])
        self.count = 1
        self.pushButton.setText(self.list[0][self.posl[0]])
        self.pushButton_2.setText(self.list[0][self.posl[1]])
        self.pushButton_3.setText(self.list[0][self.posl[2]])
        self.pushButton_4.setText(self.list[0][self.posl[3]])

    def answer(self, btn):
        if self.count < len(self.list):
            text = btn.text()
            self.label.setText(self.list[self.count][0])
            random.shuffle(self.posl)
            self.pushButton.setText(self.list[self.count][self.posl[0]])
            self.pushButton_2.setText(self.list[self.count][self.posl[1]])
            self.pushButton_3.setText(self.list[self.count][self.posl[2]])
            self.pushButton_4.setText(self.list[self.count][self.posl[3]])
            if self.count == 1:
                answer = '0'
                if text == answer:
                    self.true += 1
            if self.count == 2:
                answer = '1896'
                if text == answer:
                    self.true += 1
            if self.count == 3:
                answer = '4'
                if text == answer:
                    self.true += 1
            if self.count == 4:
                answer = 'Хоккей'
                if text == answer:
                    self.true += 1
            if self.count == 5:
                answer = '243'
                if text == answer:
                    self.true += 1
            self.count += 1
        elif self.count == 6:
            self.resWind.show()
            self.resWind.label_2.setText(f'{self.true}/5')
            if self.true == 0:
                self.resWind.label_3.setText('Вы совсем не молодец(')
            if self.true == 1:
                self.resWind.label_3.setText('Вы не молодец(')
            if self.true == 2:
                self.resWind.label_3.setText('Вам нужно больше стараться ^-^')
            if self.true == 3:
                self.resWind.label_3.setText('Неплохой результат!')
            if self.true == 4:
                self.resWind.label_3.setText('Вы молодец!')
            if self.true == 5:
                self.resWind.label_3.setText('Вы отлично справились!!!')
            self.hide()
            varR.schet += self.true
            if varR.predel == 7:
                self.finalWind.label_3.setText(f'{varR.schet}/25')
                self.resWind.hide()
                self.finalWind.show()
            print(varR.schet)
                
