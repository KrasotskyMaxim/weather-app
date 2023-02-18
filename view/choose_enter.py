from PyQt5.QtWidgets import QMainWindow
from templates import Ui_ChooseEnterForm


class ChooseEnterView(QMainWindow):
    def __init__(self):
        super(ChooseEnterView, self).__init__()
        self.ui = Ui_ChooseEnterForm(self)
        self.init_UI()

    def init_UI(self):
        self.hide_interface()
                
    def hide_interface(self):
        pass