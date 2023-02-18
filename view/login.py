from PyQt5.QtWidgets import QMainWindow
from templates import Ui_LoginForm


class LoginView(QMainWindow):
    def __init__(self):
        super(LoginView, self).__init__()
        self.ui = Ui_LoginForm(self)
        self.init_UI()

    def init_UI(self):
        self.hide_interface()
                
    def hide_interface(self):
        pass