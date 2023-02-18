# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login-template.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginForm(object):
    def __init__(self, form) -> None:
        self.setupUi(form)

    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.resize(600, 400)
        self.login_pushButton = QtWidgets.QPushButton(LoginForm)
        self.login_pushButton.setGeometry(QtCore.QRect(250, 320, 89, 25))
        self.login_pushButton.setObjectName("pushButton")
        self.username_lineEdit = QtWidgets.QLineEdit(LoginForm)
        self.username_lineEdit.setGeometry(QtCore.QRect(240, 40, 113, 25))
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.password_lineEdit = QtWidgets.QLineEdit(LoginForm)
        self.password_lineEdit.setGeometry(QtCore.QRect(240, 80, 113, 25))
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.username_label = QtWidgets.QLabel(LoginForm)
        self.username_label.setGeometry(QtCore.QRect(140, 40, 81, 20))
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(LoginForm)
        self.password_label.setGeometry(QtCore.QRect(140, 80, 91, 20))
        self.password_label.setObjectName("password_label")
        self.confirm_password_lineEdit = QtWidgets.QLineEdit(LoginForm)
        self.confirm_password_lineEdit.setGeometry(QtCore.QRect(240, 120, 113, 25))
        self.confirm_password_lineEdit.setObjectName("confirm_password_lineEdit")
        self.confirm_password_label = QtWidgets.QLabel(LoginForm)
        self.confirm_password_label.setGeometry(QtCore.QRect(140, 110, 91, 41))
        self.confirm_password_label.setObjectName("confirm_password_label")
        self.city_name_label = QtWidgets.QLabel(LoginForm)
        self.city_name_label.setGeometry(QtCore.QRect(140, 160, 81, 20))
        self.city_name_label.setObjectName("city_name_label")
        self.city_name_lineEdit = QtWidgets.QLineEdit(LoginForm)
        self.city_name_lineEdit.setGeometry(QtCore.QRect(240, 160, 113, 25))
        self.city_name_lineEdit.setObjectName("city_name_lineEdit")

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)

    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "Form"))
        self.login_pushButton.setText(_translate("LoginForm", "LOGIN"))
        self.username_label.setText(_translate("LoginForm", "USERNAME:"))
        self.password_label.setText(_translate("LoginForm", "PASSWORD:"))
        self.confirm_password_label.setText(_translate("LoginForm", "<html><head/><body><p>CONFIRM<br/>PASSWORD:</p></body></html>"))
        self.city_name_label.setText(_translate("LoginForm", "CITY NAME:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginForm = QtWidgets.QWidget()
    ui = Ui_LoginForm()
    ui.setupUi(LoginForm)
    LoginForm.show()
    sys.exit(app.exec_())
