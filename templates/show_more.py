# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'show-more.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ShowMoreForm(object):
    def __init__(self, form) -> None:
        self.setupUi(form)                              
        
    def setupUi(self, ShowMoreForm):
        ShowMoreForm.setObjectName("ShowMoreForm")
        ShowMoreForm.resize(600, 400)
        self.forecast_label = QtWidgets.QLabel(ShowMoreForm)
        self.forecast_label.setGeometry(QtCore.QRect(200, 10, 181, 31))
        self.forecast_label.setObjectName("forecast_label")
        self.verticalLayoutWidget = QtWidgets.QWidget(ShowMoreForm)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 50, 111, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.one_verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.one_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.one_verticalLayout.setObjectName("one_verticalLayout")
        self.one_icon_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.one_icon_label.setStyleSheet("background-color: rgb(101, 165, 213);")
        self.one_icon_label.setText("")
        # self.one_icon_label.setPixmap(QtGui.QPixmap("../../images/01d.png"))
        self.one_icon_label.setObjectName("one_icon_label")
        self.one_verticalLayout.addWidget(self.one_icon_label)
        self.one_textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.one_textBrowser.setObjectName("one_textBrowser")
        self.one_verticalLayout.addWidget(self.one_textBrowser)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(ShowMoreForm)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(120, 50, 111, 281))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.two_verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.two_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.two_verticalLayout.setObjectName("two_verticalLayout")
        self.two_icon_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.two_icon_label.setStyleSheet("background-color: rgb(101, 165, 213);")
        self.two_icon_label.setText("")
        self.two_icon_label.setPixmap(QtGui.QPixmap("../../images/01n.png"))
        self.two_icon_label.setObjectName("two_icon_label")
        self.two_verticalLayout.addWidget(self.two_icon_label)
        self.two_textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget_2)
        self.two_textBrowser.setObjectName("two_textBrowser")
        self.two_verticalLayout.addWidget(self.two_textBrowser)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(ShowMoreForm)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(240, 50, 111, 281))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.three_verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.three_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.three_verticalLayout.setObjectName("three_verticalLayout")
        self.three_icon_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.three_icon_label.setStyleSheet("background-color: rgb(101, 165, 213);")
        self.three_icon_label.setText("")
        self.three_icon_label.setPixmap(QtGui.QPixmap("../../images/02d.png"))
        self.three_icon_label.setObjectName("three_icon_label")
        self.three_verticalLayout.addWidget(self.three_icon_label)
        self.three_textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget_3)
        self.three_textBrowser.setObjectName("three_textBrowser")
        self.three_verticalLayout.addWidget(self.three_textBrowser)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(ShowMoreForm)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(480, 50, 111, 281))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.five_verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.five_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.five_verticalLayout.setObjectName("five_verticalLayout")
        self.five_icon_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.five_icon_label.setStyleSheet("background-color: rgb(101, 165, 213);")
        self.five_icon_label.setText("")
        self.five_icon_label.setPixmap(QtGui.QPixmap("../../images/03n.png"))
        self.five_icon_label.setObjectName("five_icon_label")
        self.five_verticalLayout.addWidget(self.five_icon_label)
        self.five_textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.five_textBrowser.setObjectName("five_textBrowser")
        self.five_verticalLayout.addWidget(self.five_textBrowser)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(ShowMoreForm)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(360, 50, 111, 281))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.four_verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.four_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.four_verticalLayout.setObjectName("four_verticalLayout")
        self.four_icon_label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.four_icon_label.setStyleSheet("background-color: rgb(101, 165, 213);")
        self.four_icon_label.setText("")
        self.four_icon_label.setPixmap(QtGui.QPixmap("../../images/02n.png"))
        self.four_icon_label.setObjectName("four_icon_label")
        self.four_verticalLayout.addWidget(self.four_icon_label)
        self.four_textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget_5)
        self.four_textBrowser.setObjectName("four_textBrowser")
        self.four_verticalLayout.addWidget(self.four_textBrowser)
        self.back_pushButton = QtWidgets.QPushButton(ShowMoreForm)
        self.back_pushButton.setGeometry(QtCore.QRect(500, 360, 89, 25))
        self.back_pushButton.setObjectName("back_pushButton")

        self.retranslateUi(ShowMoreForm)
        QtCore.QMetaObject.connectSlotsByName(ShowMoreForm)

    def retranslateUi(self, ShowMoreForm):
        _translate = QtCore.QCoreApplication.translate
        ShowMoreForm.setWindowTitle(_translate("ShowMoreForm", "Form"))
        self.forecast_label.setText(_translate("ShowMoreForm", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">5-DAY FORECAST</span></p></body></html>"))
        self.one_textBrowser.setHtml(_translate("ShowMoreForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Weather:</span> Clouds <span style=\" font-style:italic;\">(overcast clouds)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Temp:</span> -3 <span style=\" font-family:\'arial,sans-serif\'; font-weight:600; color:#202124; background-color:#ffffff;\">°</span><span style=\" font-family:\'arial,sans-serif\'; color:#202124; background-color:#ffffff;\">C</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Wind: </span>6m/s</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Humidity:</span> 93</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">07/02/2023</span></p></body></html>"))
        self.two_textBrowser.setHtml(_translate("ShowMoreForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Weather:</span> Clouds <span style=\" font-style:italic;\">(overcast clouds)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Temp:</span> -3 <span style=\" font-family:\'arial,sans-serif\'; font-weight:600; color:#202124; background-color:#ffffff;\">°</span><span style=\" font-family:\'arial,sans-serif\'; color:#202124; background-color:#ffffff;\">C</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Wind: </span>6m/s</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Humidity:</span> 93</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">08/02/2023</span></p></body></html>"))
        self.three_textBrowser.setHtml(_translate("ShowMoreForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Weather:</span> Clouds <span style=\" font-style:italic;\">(overcast clouds)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Temp:</span> -3 <span style=\" font-family:\'arial,sans-serif\'; font-weight:600; color:#202124; background-color:#ffffff;\">°</span><span style=\" font-family:\'arial,sans-serif\'; color:#202124; background-color:#ffffff;\">C</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Wind: </span>6m/s</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Humidity:</span> 93</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">09/02/2023</span></p></body></html>"))
        self.five_textBrowser.setHtml(_translate("ShowMoreForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Weather:</span> Clouds <span style=\" font-style:italic;\">(overcast clouds)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Temp:</span> -3 <span style=\" font-family:\'arial,sans-serif\'; font-weight:600; color:#202124; background-color:#ffffff;\">°</span><span style=\" font-family:\'arial,sans-serif\'; color:#202124; background-color:#ffffff;\">C</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Wind: </span>6m/s</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Humidity:</span> 93</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">11/02/2023</span></p></body></html>"))
        self.four_textBrowser.setHtml(_translate("ShowMoreForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Weather:</span> Clouds <span style=\" font-style:italic;\">(overcast clouds)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Temp:</span> -3 <span style=\" font-family:\'arial,sans-serif\'; font-weight:600; color:#202124; background-color:#ffffff;\">°</span><span style=\" font-family:\'arial,sans-serif\'; color:#202124; background-color:#ffffff;\">C</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Wind: </span>6m/s</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Humidity:</span> 93</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">10/02/2023</span></p></body></html>"))
        self.back_pushButton.setText(_translate("ShowMoreForm", "BACK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ShowMoreForm = QtWidgets.QWidget()
    ui = Ui_ShowMoreForm()
    ui.setupUi(ShowMoreForm)
    ShowMoreForm.show()
    sys.exit(app.exec_())
