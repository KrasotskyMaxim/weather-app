# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profile-template.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProfileForm(object):
    def __init__(self, form) -> None:
        self.setupUi(form)

    def setupUi(self, ProfileForm):
        ProfileForm.setObjectName("ProfileForm")
        ProfileForm.resize(600, 400)
        self.profile_label = QtWidgets.QLabel(ProfileForm)
        self.profile_label.setGeometry(QtCore.QRect(240, 10, 101, 31))
        self.profile_label.setObjectName("profile_label")
        self.username_label = QtWidgets.QLabel(ProfileForm)
        self.username_label.setGeometry(QtCore.QRect(20, 50, 91, 21))
        self.username_label.setObjectName("username_label")
        self.city_label = QtWidgets.QLabel(ProfileForm)
        self.city_label.setGeometry(QtCore.QRect(70, 110, 41, 20))
        self.city_label.setObjectName("city_label")
        self.save_pushButton = QtWidgets.QPushButton(ProfileForm)
        self.save_pushButton.setGeometry(QtCore.QRect(480, 360, 101, 25))
        self.save_pushButton.setObjectName("save_pushButton")
        self.password_label = QtWidgets.QLabel(ProfileForm)
        self.password_label.setGeometry(QtCore.QRect(20, 80, 91, 20))
        self.password_label.setObjectName("password_label")
        self.back_pushButton = QtWidgets.QPushButton(ProfileForm)
        self.back_pushButton.setGeometry(QtCore.QRect(10, 360, 101, 25))
        self.back_pushButton.setObjectName("back_pushButton")
        self.username_lineEdit = QtWidgets.QLineEdit(ProfileForm)
        self.username_lineEdit.setGeometry(QtCore.QRect(120, 50, 113, 25))
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.password_lineEdit = QtWidgets.QLineEdit(ProfileForm)
        self.password_lineEdit.setGeometry(QtCore.QRect(120, 80, 113, 25))
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.city_lineEdit = QtWidgets.QLineEdit(ProfileForm)
        self.city_lineEdit.setGeometry(QtCore.QRect(120, 110, 113, 25))
        self.city_lineEdit.setObjectName("city_lineEdit")

        self.retranslateUi(ProfileForm)
        QtCore.QMetaObject.connectSlotsByName(ProfileForm)

    def retranslateUi(self, ProfileForm):
        _translate = QtCore.QCoreApplication.translate
        ProfileForm.setWindowTitle(_translate("ProfileForm", "Form"))
        self.profile_label.setText(_translate("ProfileForm", "<html><head/><body><p><span style=\" font-size:18pt;\">PROFILE</span></p></body></html>"))
        self.username_label.setText(_translate("ProfileForm", "<html><head/><body><p><span style=\" font-weight:600;\">USERNAME:</span></p></body></html>"))
        self.city_label.setText(_translate("ProfileForm", "<html><head/><body><p><span style=\" font-weight:600;\">CITY:</span></p></body></html>"))
        self.save_pushButton.setText(_translate("ProfileForm", "SAVE"))
        self.password_label.setText(_translate("ProfileForm", "<html><head/><body><p><span style=\" font-weight:600;\">PASSWORD:</span></p></body></html>"))
        self.back_pushButton.setText(_translate("ProfileForm", "BACK"))
        self.username_lineEdit.setText(_translate("ProfileForm", "Test"))
        self.password_lineEdit.setText(_translate("ProfileForm", "12345"))
        self.city_lineEdit.setText(_translate("ProfileForm", "Minsk"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProfileForm = QtWidgets.QWidget()
    ui = Ui_ProfileForm()
    ui.setupUi(ProfileForm)
    ProfileForm.show()
    sys.exit(app.exec_())
