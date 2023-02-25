from PyQt5.QtWidgets import QMainWindow
from templates import Ui_ProfileForm

from exceptions import show_exception, UpdateProfileException


class ProfileView(QMainWindow):
    def __init__(self, controller):
        super(ProfileView, self).__init__()
        self.ui = Ui_ProfileForm(self)
        self.controller = controller
        self.init_UI()

    def init_UI(self):
        self.hide_interface()
                
    def hide_interface(self):
        pass
    
    def set_user_profile(self, user_data):
        self.ui.username_lineEdit.setText(user_data.username)
        self.ui.password_lineEdit.setText(user_data.password)
        self.ui.city_lineEdit.setText(user_data.city)
    
    def save(self):
        try:
            self.controller.save_profile(
                username=self.ui.username_lineEdit.text(),
                password=self.ui.password_lineEdit.text(),
                city=self.ui.city_lineEdit.text(),
            )
        except UpdateProfileException as e:
            show_exception("Update profile error", str(e))