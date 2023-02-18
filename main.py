# XDG_SESSION_TYPE=x11
import sys

from PyQt5.QtWidgets import QApplication, QStackedWidget

from view import (
    ChooseEnterView, 
    HomeView,
    LoginView,
    ProfileView,
    SignInView,
)


class App(QApplication):
    '''Main application class.'''
    
    current_view = None
    
    def __init__(self, *args):
        super().__init__(list(args))
        
        self.widgets = QStackedWidget()
        self.choose_enter_view = ChooseEnterView()
        self.home_view = HomeView()
        self.login_view = LoginView()
        self.profile_view = ProfileView()
        self.sign_in_view = SignInView()
        
        self.init_view()
        self.init_app()

    def init_app(self):
        # add widgets
        self.widgets.addWidget(self.choose_enter_view)
        self.widgets.addWidget(self.home_view)
        self.widgets.addWidget(self.login_view)
        self.widgets.addWidget(self.profile_view)
        self.widgets.addWidget(self.sign_in_view)
        # set size
        self.widgets.setFixedWidth(600)
        self.widgets.setFixedHeight(400)
        # show
        self.switch_view(self.choose_enter_view)
        self.widgets.show()
        
    def init_view(self):
        self.choose_enter_view.ui.login_pushButton.clicked.connect(self.goto_login)
        self.choose_enter_view.ui.sign_in_pushButton.clicked.connect(self.goto_sign_in)
        
        self.login_view.ui.login_pushButton.clicked.connect(self.login)
        self.sign_in_view.ui.sign_in_pushButton.clicked.connect(self.sign_in)
        
        self.home_view.ui.profile_pushButton.clicked.connect(self.goto_profile)
        self.home_view.ui.refresh_pushButton.clicked.connect(self.home_view.refresh)
        self.home_view.ui.search_pushButton.clicked.connect(self.home_view.search)
        self.home_view.ui.show_more_pushButton.clicked.connect(self.home_view.show_more)
        
        self.profile_view.ui.back_pushButton.clicked.connect(self.goto_home)
        self.profile_view.ui.save_pushButton.clicked.connect(self.profile_view.save)
        
    def switch_view(self, view):
        self.current_view = view
        self.widgets.setCurrentWidget(self.current_view)
        
    def goto_login(self):
        self.switch_view(self.login_view)
        
    def goto_sign_in(self):
        self.switch_view(self.sign_in_view)
        
    def goto_profile(self):
        self.switch_view(self.profile_view)
        
    def goto_home(self):
        self.switch_view(self.home_view)
        
    def login(self):
        self.switch_view(self.home_view)
        
    def sign_in(self):
        self.switch_view(self.home_view)


def application():
    app = App(sys.argv)
    app.setApplicationName("IHelpWeather")
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    application()
