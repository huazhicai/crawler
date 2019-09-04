# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'thread_crawler.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 600)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setBaseSize(QtCore.QSize(900, 600))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 6)
        self.start_btn = QtWidgets.QPushButton(Form)
        self.start_btn.setObjectName("start_btn")
        self.gridLayout.addWidget(self.start_btn, 1, 0, 1, 1)
        self.stop_btn = QtWidgets.QPushButton(Form)
        self.stop_btn.setObjectName("stop_btn")
        self.gridLayout.addWidget(self.stop_btn, 1, 1, 1, 1)
        self.clean_btn = QtWidgets.QPushButton(Form)
        self.clean_btn.setObjectName("clean_btn")
        self.gridLayout.addWidget(self.clean_btn, 1, 2, 1, 1)
        self.save_btn = QtWidgets.QPushButton(Form)
        self.save_btn.setObjectName("save_btn")
        self.gridLayout.addWidget(self.save_btn, 1, 3, 1, 1)
        self.timer_laber = QtWidgets.QLabel(Form)
        self.timer_laber.setMaximumSize(QtCore.QSize(200, 100))
        self.timer_laber.setObjectName("timer_laber")
        self.gridLayout.addWidget(self.timer_laber, 1, 4, 1, 1)
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout.addWidget(self.lcdNumber, 1, 5, 1, 1)

        self.retranslateUi(Form)
        self.start_btn.clicked.connect(Form.start_crawl)
        self.stop_btn.clicked.connect(Form.stop_crawl)
        self.clean_btn.clicked.connect(Form.clean_text)
        self.save_btn.clicked.connect(Form.save)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.start_btn.setText(_translate("Form", "Start"))
        self.stop_btn.setText(_translate("Form", "Stop"))
        self.clean_btn.setText(_translate("Form", "Clean"))
        self.save_btn.setText(_translate("Form", "Save"))
        self.timer_laber.setText(_translate("Form", "Timer"))
