from PyQt5.QtWidgets import QMessageBox


class LoginException(Exception):
    pass

class SignInException(Exception):
    pass

class DBConnectionException(Exception):
    pass

class UpdateProfileException(Exception):
    pass

class CityException(Exception):
    pass

def show_exception(title, message):
    error = QMessageBox()
    error.setWindowTitle(title)
    error.setText(message)
    error.setIcon(QMessageBox.Warning)
    error.setStandardButtons(QMessageBox.Ok)

    error.exec_()
