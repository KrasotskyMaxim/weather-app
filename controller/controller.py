import settings

from exceptions import (
    LoginException,
    SignInException,
)
from model.model import Model


class Controller:
    def __init__(self, view) -> None:
        self.model = Model(view)
        
    def login(self, username, password, confirm_password, city):
        try:
            self.model.check_empty_fields(settings.LOGIN_MODE, username, password, confirm_password, city)
            self.model.check_confirm_password(settings.LOGIN_MODE, password, confirm_password)
        except LoginException:
            raise

        self.model.save_user(username, password, city)
        
    def sign_in(self, username, password):
        try:
            self.model.check_exists_user(settings.SIGN_IN_MODE, username, password)
            self.model.prepare_home_view()
        except SignInException:
            raise
