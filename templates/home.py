# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home-template.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_HomeForm(object):
    def __init__(self, form=None) -> None:
        self.setupUi(form)

    def setupUi(self, HomeForm):
        HomeForm.setObjectName("HomeForm")
        HomeForm.resize(600, 400)
        
        self.verticalLayoutWidget = QtWidgets.QWidget(HomeForm)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 151, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        
        self.weather_verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.weather_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.weather_verticalLayout.setObjectName("weather_verticalLayout")
        
        self.weather_icon_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.weather_icon_label.setStyleSheet("background-color: #65a5d5;")
        self.weather_icon_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.weather_icon_label.setText("")
        self.weather_icon_label.setScaledContents(False)
        self.weather_icon_label.setAlignment(QtCore.Qt.AlignCenter)
        self.weather_icon_label.setObjectName("weather_icon_label")
        self.weather_verticalLayout.addWidget(self.weather_icon_label)
        
        self.weather_info_textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.weather_info_textBrowser.setObjectName("weather_info_textBrowser")
        self.weather_verticalLayout.addWidget(self.weather_info_textBrowser)
        
        self.refresh_pushButton = QtWidgets.QPushButton(HomeForm)
        self.refresh_pushButton.setGeometry(QtCore.QRect(40, 360, 89, 25))
        self.refresh_pushButton.setObjectName("refresh_pushButton")
        self.profile_pushButton = QtWidgets.QPushButton(HomeForm)
        self.profile_pushButton.setGeometry(QtCore.QRect(500, 360, 89, 25))
        self.profile_pushButton.setObjectName("profile_pushButton")
        self.current_datetime_textBrowser = QtWidgets.QTextBrowser(HomeForm)
        self.current_datetime_textBrowser.setGeometry(QtCore.QRect(480, 10, 111, 65))
        self.current_datetime_textBrowser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.current_datetime_textBrowser.setObjectName("current_datetime_textBrowser")
        self.current_datetime_label = QtWidgets.QLabel(HomeForm)
        self.current_datetime_label.setGeometry(QtCore.QRect(400, 20, 81, 31))
        self.current_datetime_label.setObjectName("current_datetime_label")
        self.search_lineEdit = QtWidgets.QLineEdit(HomeForm)
        self.search_lineEdit.setGeometry(QtCore.QRect(170, 10, 211, 25))
        self.search_lineEdit.setObjectName("search_lineEdit")
        self.search_pushButton = QtWidgets.QPushButton(HomeForm)
        self.search_pushButton.setGeometry(QtCore.QRect(230, 40, 89, 25))
        self.search_pushButton.setObjectName("search_pushButton")
        self.show_more_pushButton = QtWidgets.QPushButton(HomeForm)
        self.show_more_pushButton.setGeometry(QtCore.QRect(390, 360, 101, 25))
        self.show_more_pushButton.setObjectName("show_more_pushButton")

        self.retranslateUi(HomeForm)
        QtCore.QMetaObject.connectSlotsByName(HomeForm)

    def retranslateUi(self, HomeForm):
        _translate = QtCore.QCoreApplication.translate
        HomeForm.setWindowTitle(_translate("HomeForm", "Form"))
        self.refresh_pushButton.setText(_translate("HomeForm", "REFRESH"))
        self.profile_pushButton.setText(_translate("HomeForm", "PROFILE"))
        self.current_datetime_label.setText(_translate("HomeForm", "<html><head/><body><p>CURRENT<br/>DATETIME:</p></body></html>"))
        self.search_pushButton.setText(_translate("HomeForm", "SEARCH"))
        self.show_more_pushButton.setText(_translate("HomeForm", "SHOW MORE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HomeForm = QtWidgets.QWidget()
    ui = Ui_HomeForm()
    ui.setupUi(HomeForm)
    HomeForm.show()
    sys.exit(app.exec_())
