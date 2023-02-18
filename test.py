import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextBrowser
from PyQt5.QtCore import QTimer, QTime, QDate, Qt


class ClockWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Clock")
        self.setGeometry(100, 100, 400, 200)

        self.current_datetime_textBrowser = QTextBrowser(self)
        self.current_datetime_textBrowser.setAlignment(Qt.AlignCenter)
        self.current_datetime_textBrowser.setStyleSheet("font-size: 40px; font-family: 'Arial';")

        self.setCentralWidget(self.current_datetime_textBrowser)

        timer = QTimer(self)
        timer.timeout.connect(self.update_time)
        timer.start(1000)

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss")
        current_date = QDate.currentDate().toString("ddd MMM d yyyy")
        self.current_datetime_textBrowser.setText(f"{current_time}\n{current_date}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClockWindow()
    window.show()
    sys.exit(app.exec_())
