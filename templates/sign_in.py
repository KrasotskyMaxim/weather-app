# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sign-in-template.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SignInForm(object):
    def __init__(self, form) -> None:
        self.setupUi(form)

    def setupUi(self, SignInForm):
        SignInForm.setObjectName("SignInForm")
        SignInForm.resize(600, 400)
        self.sign_in_pushButton = QtWidgets.QPushButton(SignInForm)
        self.sign_in_pushButton.setGeometry(QtCore.QRect(250, 330, 89, 25))
        self.sign_in_pushButton.setObjectName("sign_in_pushButton")
        self.username_label = QtWidgets.QLabel(SignInForm)
        self.username_label.setGeometry(QtCore.QRect(160, 40, 81, 20))
        self.username_label.setObjectName("username_label")
        self.username_lineEdit = QtWidgets.QLineEdit(SignInForm)
        self.username_lineEdit.setGeometry(QtCore.QRect(260, 40, 113, 25))
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.password_lineEdit = QtWidgets.QLineEdit(SignInForm)
        self.password_lineEdit.setGeometry(QtCore.QRect(260, 80, 113, 25))
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.password_label = QtWidgets.QLabel(SignInForm)
        self.password_label.setGeometry(QtCore.QRect(160, 80, 91, 20))
        self.password_label.setObjectName("password_label")

        self.retranslateUi(SignInForm)
        QtCore.QMetaObject.connectSlotsByName(SignInForm)

    def retranslateUi(self, SignInForm):
        _translate = QtCore.QCoreApplication.translate
        SignInForm.setWindowTitle(_translate("SignInForm", "Form"))
        self.sign_in_pushButton.setText(_translate("SignInForm", "SIGN IN"))
        self.username_label.setText(_translate("SignInForm", "USERNAME:"))
        self.password_label.setText(_translate("SignInForm", "PASSWORD:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignInForm = QtWidgets.QWidget()
    ui = Ui_SignInForm()
    ui.setupUi(SignInForm)
    SignInForm.show()
    sys.exit(app.exec_())
