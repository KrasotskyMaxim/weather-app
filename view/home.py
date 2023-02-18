from PyQt5.QtWidgets import QMainWindow
from templates import Ui_HomeForm


class HomeView(QMainWindow):
    def __init__(self):
        super(HomeView, self).__init__()
        self.ui = Ui_HomeForm(self)
        self.init_UI()

    def init_UI(self):
        self.hide_interface()
                
    def hide_interface(self):
        pass

    def refresh(self):
        print("RESRESH")
        
    def search(self):
        print("SEARCH")
        
    def show_more(self):
        print("SHOW MORE")
