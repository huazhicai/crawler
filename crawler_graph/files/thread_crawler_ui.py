# -*- coding: utf-8 -*-

# Form implementation generated from reading files file 'thread_crawler.files'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Crawler(object):
    def setupUi(self, Crawler):
        Crawler.setObjectName("Crawler")
        Crawler.resize(763, 590)
        self.gridLayout = QtWidgets.QGridLayout(Crawler)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(Crawler)
        self.textBrowser.setBaseSize(QtCore.QSize(900, 600))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 8)
        self.start_btn = QtWidgets.QPushButton(Crawler)
        self.start_btn.setObjectName("start_btn")
        self.gridLayout.addWidget(self.start_btn, 1, 0, 1, 1)
        self.stop_btn = QtWidgets.QPushButton(Crawler)
        self.stop_btn.setObjectName("stop_btn")
        self.gridLayout.addWidget(self.stop_btn, 1, 1, 1, 1)
        self.continue_btn = QtWidgets.QPushButton(Crawler)
        self.continue_btn.setObjectName("continue_btn")
        self.gridLayout.addWidget(self.continue_btn, 1, 2, 1, 1)
        self.clean_btn = QtWidgets.QPushButton(Crawler)
        self.clean_btn.setObjectName("clean_btn")
        self.gridLayout.addWidget(self.clean_btn, 1, 3, 1, 1)
        self.save_btn = QtWidgets.QPushButton(Crawler)
        self.save_btn.setObjectName("save_btn")
        self.gridLayout.addWidget(self.save_btn, 1, 4, 1, 1)
        self.save_btn_2 = QtWidgets.QPushButton(Crawler)
        self.save_btn_2.setObjectName("save_btn_2")
        self.gridLayout.addWidget(self.save_btn_2, 1, 5, 1, 1)
        self.timer_laber = QtWidgets.QLabel(Crawler)
        self.timer_laber.setMaximumSize(QtCore.QSize(200, 100))
        self.timer_laber.setObjectName("timer_laber")
        self.gridLayout.addWidget(self.timer_laber, 1, 6, 1, 1)
        self.lcdNumber = QtWidgets.QLCDNumber(Crawler)
        self.lcdNumber.setStyleSheet("background-color: rgb(60, 60, 60);")
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout.addWidget(self.lcdNumber, 1, 7, 1, 1)

        self.retranslateUi(Crawler)
        self.start_btn.clicked.connect(Crawler.start_crawl)
        self.stop_btn.clicked.connect(Crawler.stop_crawl)
        self.clean_btn.clicked.connect(Crawler.clean_text)
        self.save_btn.clicked.connect(Crawler.save)
        self.continue_btn.clicked.connect(Crawler.continue_crawl)
        QtCore.QMetaObject.connectSlotsByName(Crawler)

    def retranslateUi(self, Crawler):
        _translate = QtCore.QCoreApplication.translate
        Crawler.setWindowTitle(_translate("Crawler", "Form"))
        self.start_btn.setText(_translate("Crawler", "Start"))
        self.stop_btn.setText(_translate("Crawler", "Stop"))
        self.continue_btn.setText(_translate("Crawler", "Continue"))
        self.clean_btn.setText(_translate("Crawler", "Clean"))
        self.save_btn.setText(_translate("Crawler", "Save"))
        self.save_btn_2.setText(_translate("Crawler", "Close"))
        self.timer_laber.setText(_translate("Crawler", "                Timer"))
