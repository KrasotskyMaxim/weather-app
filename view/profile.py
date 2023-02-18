from PyQt5.QtWidgets import QMainWindow
from templates import Ui_ProfileForm


class ProfileView(QMainWindow):
    def __init__(self):
        super(ProfileView, self).__init__()
        self.ui = Ui_ProfileForm(self)
        self.init_UI()

    def init_UI(self):
        self.hide_interface()
                
    def hide_interface(self):
        pass
    
    def save(self):
        print("SAVE")