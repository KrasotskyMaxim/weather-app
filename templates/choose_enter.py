# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choose-enter-template.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChooseEnterForm(object):
    def __init__(self, form) -> None:
        self.setupUi(form)

    def setupUi(self, ChooseEnterForm):
        ChooseEnterForm.setObjectName("ChooseEnterForm")
        ChooseEnterForm.resize(600, 400)
        self.login_pushButton = QtWidgets.QPushButton(ChooseEnterForm)
        self.login_pushButton.setGeometry(QtCore.QRect(200, 150, 89, 25))
        self.login_pushButton.setObjectName("login_pushButton")
        self.sign_in_pushButton = QtWidgets.QPushButton(ChooseEnterForm)
        self.sign_in_pushButton.setGeometry(QtCore.QRect(300, 150, 89, 25))
        self.sign_in_pushButton.setObjectName("sign_in_pushButton")
        self.tip_textBrowser = QtWidgets.QTextBrowser(ChooseEnterForm)
        self.tip_textBrowser.setGeometry(QtCore.QRect(50, 200, 501, 131))
        self.tip_textBrowser.setObjectName("tip_textBrowser")
        self.next_tip_login_pushButton = QtWidgets.QPushButton(ChooseEnterForm)
        self.next_tip_login_pushButton.setGeometry(QtCore.QRect(300, 340, 89, 25))
        self.next_tip_login_pushButton.setObjectName("next_tip_login_pushButton")
        self.prev_tip_login_pushButton = QtWidgets.QPushButton(ChooseEnterForm)
        self.prev_tip_login_pushButton.setGeometry(QtCore.QRect(200, 340, 89, 25))
        self.prev_tip_login_pushButton.setObjectName("prev_tip_login_pushButton")
        self.choose_enter_label = QtWidgets.QLabel(ChooseEnterForm)
        self.choose_enter_label.setGeometry(QtCore.QRect(220, 10, 141, 31))
        self.choose_enter_label.setObjectName("choose_enter_label")

        self.retranslateUi(ChooseEnterForm)
        QtCore.QMetaObject.connectSlotsByName(ChooseEnterForm)

    def retranslateUi(self, ChooseEnterForm):
        _translate = QtCore.QCoreApplication.translate
        ChooseEnterForm.setWindowTitle(_translate("ChooseEnterForm", "Form"))
        self.login_pushButton.setText(_translate("ChooseEnterForm", "LOGIN"))
        self.sign_in_pushButton.setText(_translate("ChooseEnterForm", "SIGN IN"))
        self.tip_textBrowser.setHtml(_translate("ChooseEnterForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Some tip...</p></body></html>"))
        self.next_tip_login_pushButton.setText(_translate("ChooseEnterForm", "->"))
        self.prev_tip_login_pushButton.setText(_translate("ChooseEnterForm", "<-"))
        self.choose_enter_label.setText(_translate("ChooseEnterForm", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">IHelpWeather</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChooseEnterForm = QtWidgets.QWidget()
    ui = Ui_ChooseEnterForm()
    ui.setupUi(ChooseEnterForm)
    ChooseEnterForm.show()
    sys.exit(app.exec_())
