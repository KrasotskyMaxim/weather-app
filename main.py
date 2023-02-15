# XDG_SESSION_TYPE=x11
from PyQt5.QtWidgets import QApplication, QStackedWidget

import sys


class App(QApplication):
    def __init__(self, *args):
        super().__init__(list(args))
        
        self.widgets = QStackedWidget()
        self.init_app()
        
    def init_app(self):
        self.widgets.setFixedHeight(400)
        self.widgets.setFixedWidth(600)
        # show
        self.widgets.show()
        

def application():
    app = App(sys.argv)
    app.setApplicationName("IHelpWeather")
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    application()