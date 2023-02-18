from PyQt5.QtWidgets import QMainWindow
from templates import Ui_SignInForm


class SignInView(QMainWindow):
    def __init__(self):
        super(SignInView, self).__init__()
        self.ui = Ui_SignInForm(self)
        self.init_UI()

    def init_UI(self):
        self.hide_interface()
                
    def hide_interface(self):
        pass