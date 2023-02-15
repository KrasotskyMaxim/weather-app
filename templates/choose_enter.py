# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choose-enter-template.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChooseEnterForm(object):
    def setupUi(self, ChooseEnterForm):
        ChooseEnterForm.setObjectName("ChooseEnterForm")
        ChooseEnterForm.resize(600, 400)
        self.login_pushButton = QtWidgets.QPushButton(ChooseEnterForm)
        self.login_pushButton.setGeometry(QtCore.QRect(190, 150, 89, 25))
        self.login_pushButton.setObjectName("login_pushButton")
        self.sign_in_pushButton = QtWidgets.QPushButton(ChooseEnterForm)
        self.sign_in_pushButton.setGeometry(QtCore.QRect(290, 150, 89, 25))
        self.sign_in_pushButton.setObjectName("sign_in_pushButton")

        self.retranslateUi(ChooseEnterForm)
        QtCore.QMetaObject.connectSlotsByName(ChooseEnterForm)

    def retranslateUi(self, ChooseEnterForm):
        _translate = QtCore.QCoreApplication.translate
        ChooseEnterForm.setWindowTitle(_translate("ChooseEnterForm", "Form"))
        self.login_pushButton.setText(_translate("ChooseEnterForm", "LOGIN"))
        self.sign_in_pushButton.setText(_translate("ChooseEnterForm", "SIGN IN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChooseEnterForm = QtWidgets.QWidget()
    ui = Ui_ChooseEnterForm()
    ui.setupUi(ChooseEnterForm)
    ChooseEnterForm.show()
    sys.exit(app.exec_())
